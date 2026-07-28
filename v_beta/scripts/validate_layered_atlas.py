#!/usr/bin/env python3
"""Validate Ether Frontier layered sprite-atlas manifests.

Template mode validates contracts that intentionally have null geometry.
Production mode additionally opens the PNG, verifies tight alpha rects, bounds,
overlaps, pivots, attachments, animation references, and the 5 MB limit.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from PIL import Image

MAX_ATLAS_BYTES = 5 * 1024 * 1024
QA_NAME_PARTS = ("review", "preview", "grid", "pivot_cross", "label")
TRACK_PROPERTY_SUFFIXES = (".rotation", ".position", ".visibility", ".frame")
PATTERN_RE = re.compile(r"^(.*?)(\d+)\.\.(\d+)$")


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def expand_pattern(name: str, spec: dict[str, Any]) -> list[str]:
    if not spec.get("pattern"):
        return [name]
    match = PATTERN_RE.match(name)
    if not match:
        return [name]
    prefix, start_text, end_text = match.groups()
    start, end = int(start_text), int(end_text)
    width = len(start_text)
    return [f"{prefix}{value:0{width}d}" for value in range(start, end + 1)]


def validate_common(data: dict[str, Any], errors: list[str]) -> set[str]:
    required = ("schemaVersion", "pipeline", "objectId", "familyId", "atlas", "sprites", "animations")
    for key in required:
        if key not in data:
            error(errors, f"missing top-level field: {key}")

    if data.get("pipeline") != "layered-object-v2":
        error(errors, "pipeline must be layered-object-v2")
    if data.get("objectId") != "watchtower":
        error(errors, "objectId must be watchtower for this contract")
    if data.get("familyId") != "wind_ranged":
        error(errors, "familyId must be wind_ranged")

    atlas = data.get("atlas", {})
    if atlas.get("maxSizeBytes") != MAX_ATLAS_BYTES:
        error(errors, f"atlas.maxSizeBytes must equal {MAX_ATLAS_BYTES}")
    if atlas.get("compactPacked") is not True:
        error(errors, "atlas.compactPacked must be true")
    if atlas.get("transparent") is not True:
        error(errors, "atlas.transparent must be true")

    expanded: set[str] = set()
    sprites = data.get("sprites", {})
    draw_orders: list[int] = []
    for name, spec in sprites.items():
        if any(part in name.lower() for part in QA_NAME_PARTS):
            error(errors, f"QA-only name present in runtime sprites: {name}")
        names = expand_pattern(name, spec)
        if spec.get("pattern") and len(names) != spec.get("count"):
            error(errors, f"{name}: count does not match numeric range")
        expanded.update(names)
        if spec.get("pattern"):
            order_range = spec.get("drawOrderRange")
            if not isinstance(order_range, list) or len(order_range) != 2:
                error(errors, f"{name}: pattern requires drawOrderRange")
            elif order_range[1] - order_range[0] + 1 != len(names):
                error(errors, f"{name}: drawOrderRange length mismatch")
            else:
                draw_orders.extend(range(order_range[0], order_range[1] + 1))
        elif not isinstance(spec.get("drawOrder"), int):
            error(errors, f"{name}: missing integer drawOrder")
        else:
            draw_orders.append(spec["drawOrder"])
        if spec.get("runtimeOnly") is not True:
            error(errors, f"{name}: runtimeOnly must be true")

    if len(draw_orders) != len(set(draw_orders)):
        error(errors, "drawOrder values overlap")

    anchors = data.get("anchors", {})
    for name, spec in sprites.items():
        attachment = spec.get("attachment")
        if attachment and attachment not in anchors:
            error(errors, f"{name}: unknown attachment {attachment}")

    groups = {spec.get("parent") for spec in sprites.values() if spec.get("parent")}
    for animation_name, animation in data.get("animations", {}).items():
        if not isinstance(animation.get("durationMs"), int) or animation["durationMs"] <= 0:
            error(errors, f"animation {animation_name}: invalid durationMs")
        if not isinstance(animation.get("loop"), bool):
            error(errors, f"animation {animation_name}: loop must be boolean")
        for track in animation.get("tracks", []):
            base = track
            for suffix in TRACK_PROPERTY_SUFFIXES:
                if base.endswith(suffix):
                    base = base[: -len(suffix)]
                    break
            if base in groups:
                continue
            if base in sprites:
                continue
            if any(base in expand_pattern(name, spec) for name, spec in sprites.items()):
                continue
            error(errors, f"animation {animation_name}: unknown track {track}")

    required_animations = {"idle", "aim", "fire", "recover", "disabled", "destroy"}
    missing_animations = required_animations - set(data.get("animations", {}))
    if missing_animations:
        error(errors, f"missing animations: {sorted(missing_animations)}")

    return expanded


def rect_values(rect: Any) -> tuple[int, int, int, int] | None:
    if isinstance(rect, list) and len(rect) == 4 and all(isinstance(value, int) for value in rect):
        return tuple(rect)
    if isinstance(rect, dict):
        values = tuple(rect.get(key) for key in ("x", "y", "w", "h"))
        if all(isinstance(value, int) for value in values):
            return values
    return None


def validate_production(data: dict[str, Any], manifest_path: Path, errors: list[str]) -> None:
    for name, spec in data["sprites"].items():
        if spec.get("pattern"):
            error(errors, f"{name}: production manifest must expand pattern entries")
            continue
        if rect_values(spec.get("rect")) is None:
            error(errors, f"{name}: missing production rect")
        pivot = spec.get("pivotPx")
        master_pivot = spec.get("masterPivotPx")
        if not (isinstance(pivot, list) and len(pivot) == 2):
            error(errors, f"{name}: pivotPx missing")
        if not (isinstance(master_pivot, list) and len(master_pivot) == 2):
            error(errors, f"{name}: masterPivotPx missing")

    atlas_meta = data["atlas"]
    image_name = atlas_meta.get("image")
    if not image_name:
        error(errors, "atlas.image is required")
        image_path = None
    else:
        image_path = manifest_path.parent / image_name
    if image_path is not None and not image_path.is_file():
        error(errors, f"atlas PNG does not exist: {image_path}")
        image_path = None

    if image_path is not None:
        size_bytes = image_path.stat().st_size
        if size_bytes > MAX_ATLAS_BYTES:
            error(errors, f"atlas exceeds 5 MB: {size_bytes} bytes")
        if atlas_meta.get("sizeBytes") != size_bytes:
            error(errors, f"atlas.sizeBytes mismatch: manifest={atlas_meta.get('sizeBytes')} actual={size_bytes}")

    if image_path is not None:
        with Image.open(image_path) as image:
            image = image.convert("RGBA")
            width, height = image.size
            if atlas_meta.get("width") != width or atlas_meta.get("height") != height:
                error(errors, "atlas width/height do not match PNG")

            occupied: list[tuple[str, tuple[int, int, int, int]]] = []
            for name, spec in data["sprites"].items():
                if spec.get("pattern"):
                    continue
                rect = rect_values(spec.get("rect"))
                if rect is None:
                    continue
                x, y, w, h = rect
                if w <= 0 or h <= 0 or x < 0 or y < 0 or x + w > width or y + h > height:
                    error(errors, f"{name}: rect out of bounds or empty: {rect}")
                    continue
                crop = image.crop((x, y, x + w, y + h))
                alpha = crop.getchannel("A")
                bbox = alpha.getbbox()
                if bbox is None:
                    error(errors, f"{name}: rect contains no visible pixels")
                elif bbox != (0, 0, w, h):
                    error(errors, f"{name}: rect is not alpha-tight; local alpha bbox={bbox}")
                occupied.append((name, rect))

            for index, (name_a, rect_a) in enumerate(occupied):
                ax, ay, aw, ah = rect_a
                for name_b, rect_b in occupied[index + 1 :]:
                    bx, by, bw, bh = rect_b
                    if ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by:
                        error(errors, f"runtime rect overlap: {name_a} / {name_b}")

    for anchor_name, anchor in data.get("anchors", {}).items():
        if not (isinstance(anchor, list) and len(anchor) == 2 and all(isinstance(v, (int, float)) for v in anchor)):
            error(errors, f"anchor {anchor_name}: production coordinates missing")

    if data.get("master", {}).get("approved") is not True:
        error(errors, "master.approved must be true in production")
    if data.get("qa", {}).get("validated") is not True:
        error(errors, "qa.validated must be true in production")
    if data.get("status") != "production":
        error(errors, "status must be production")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--mode", choices=("template", "production"), default="production")
    args = parser.parse_args()

    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    expanded = validate_common(data, errors)
    if args.mode == "production":
        validate_production(data, args.manifest, errors)

    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for item in errors:
            print(f"- {item}")
        return 1
    print(f"PASS: {args.mode} manifest; {len(expanded)} expanded sprite names")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Pack full-canvas transparent layer PNGs into a production layered atlas.

The builder never invents pivots. A geometry JSON must provide approved master
pivots and anchors. Input images retain the approved master canvas; the builder
alpha-crops them, computes local pivots, packs tight rectangles, and writes the
runtime PNG/manifest.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from pathlib import Path
from typing import Any

from PIL import Image

from validate_layered_atlas import expand_pattern

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = (
    ROOT
    / "assets/staging/candidates/watchtower/watchtower_layered_manifest_template_v1.json"
)
PADDING = 2
MAX_DIMENSION = 4096


def expand_sprites(template_sprites: dict[str, Any]) -> dict[str, dict[str, Any]]:
    expanded: dict[str, dict[str, Any]] = {}
    for pattern_name, source_spec in template_sprites.items():
        names = expand_pattern(pattern_name, source_spec)
        if not source_spec.get("pattern"):
            expanded[pattern_name] = copy.deepcopy(source_spec)
            continue
        start_order, _ = source_spec["drawOrderRange"]
        for offset, name in enumerate(names):
            spec = {
                key: copy.deepcopy(value)
                for key, value in source_spec.items()
                if key not in {"pattern", "count", "drawOrderRange", "geometry"}
            }
            spec["drawOrder"] = start_order + offset
            spec["rect"] = None
            spec["sourceSize"] = None
            spec["pivotPx"] = None
            spec["masterPivotPx"] = None
            expanded[name] = spec
    return expanded


def next_power_of_two(value: int) -> int:
    return 1 if value <= 1 else 1 << math.ceil(math.log2(value))


def pack_shelves(
    sizes: list[tuple[str, int, int]], max_width: int = 2048, padding: int = PADDING
) -> tuple[int, int, dict[str, tuple[int, int, int, int]]]:
    """Deterministic height-first shelf packing with transparent padding."""
    ordered = sorted(sizes, key=lambda item: (-item[2], -item[1], item[0]))
    placements: dict[str, tuple[int, int, int, int]] = {}
    x = padding
    y = padding
    shelf_height = 0
    used_width = 0
    for name, width, height in ordered:
        if width <= 0 or height <= 0:
            raise ValueError(f"{name}: invalid content size {width}x{height}")
        if width + padding * 2 > max_width:
            raise ValueError(f"{name}: width {width} exceeds packing width {max_width}")
        if x + width + padding > max_width and shelf_height:
            x = padding
            y += shelf_height + padding
            shelf_height = 0
        placements[name] = (x, y, width, height)
        x += width + padding
        shelf_height = max(shelf_height, height)
        used_width = max(used_width, x)
    used_height = y + shelf_height + padding
    atlas_width = next_power_of_two(max(1, used_width))
    atlas_height = next_power_of_two(max(1, used_height))
    if atlas_width > MAX_DIMENSION or atlas_height > MAX_DIMENSION:
        raise ValueError(f"packed atlas exceeds {MAX_DIMENSION}px: {atlas_width}x{atlas_height}")
    return atlas_width, atlas_height, placements


def load_geometry(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "approved_geometry":
        raise ValueError("geometry.status must be approved_geometry")
    if data.get("master", {}).get("approved") is not True:
        raise ValueError("geometry master must be approved")
    return data


def point(value: Any, label: str) -> list[float]:
    if not (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(item, (int, float)) for item in value)
    ):
        raise ValueError(f"{label}: expected [x, y]")
    return value


def build(
    template_path: Path,
    geometry_path: Path,
    layer_dir: Path,
    output_png: Path,
    output_manifest: Path,
    max_width: int,
) -> None:
    template = json.loads(template_path.read_text(encoding="utf-8"))
    geometry = load_geometry(geometry_path)
    sprites = expand_sprites(template["sprites"])
    geometry_layers = geometry.get("layers", {})

    required = set(sprites)
    expected_files = {f"{name}.png" for name in required}
    actual_files = {path.name for path in layer_dir.glob("*.png")}
    missing = sorted(expected_files - actual_files)
    unexpected = sorted(actual_files - expected_files)
    if missing:
        raise ValueError(f"missing {len(missing)} layer PNGs: {', '.join(missing[:12])}")
    if unexpected:
        raise ValueError(f"unexpected layer PNGs: {', '.join(unexpected[:12])}")

    images: dict[str, Image.Image] = {}
    bboxes: dict[str, tuple[int, int, int, int]] = {}
    source_size: tuple[int, int] | None = None
    for name in sorted(required):
        image = Image.open(layer_dir / f"{name}.png").convert("RGBA")
        if source_size is None:
            source_size = image.size
        if image.size != source_size:
            raise ValueError(f"{name}: source canvas {image.size} != {source_size}")
        bbox = image.getchannel("A").getbbox()
        if bbox is None:
            raise ValueError(f"{name}: layer is fully transparent")
        images[name] = image.crop(bbox)
        bboxes[name] = bbox

    master = geometry["master"]
    if [source_size[0], source_size[1]] != [master.get("width"), master.get("height")]:
        raise ValueError("layer source canvas does not match approved master dimensions")

    for name in required:
        if name not in geometry_layers:
            raise ValueError(f"{name}: missing geometry entry")
        point(geometry_layers[name].get("masterPivotPx"), f"{name}.masterPivotPx")

    sizes = [(name, image.width, image.height) for name, image in images.items()]
    atlas_width, atlas_height, placements = pack_shelves(sizes, max_width)
    atlas = Image.new("RGBA", (atlas_width, atlas_height), (0, 0, 0, 0))

    for name, spec in sprites.items():
        x, y, width, height = placements[name]
        atlas.alpha_composite(images[name], (x, y))
        left, top, _, _ = bboxes[name]
        master_pivot = point(
            geometry_layers[name]["masterPivotPx"], f"{name}.masterPivotPx"
        )
        spec["rect"] = [x, y, width, height]
        spec["sourceSize"] = [source_size[0], source_size[1]]
        spec["masterPivotPx"] = master_pivot
        spec["pivotPx"] = [master_pivot[0] - left, master_pivot[1] - top]
        if "attachment" in geometry_layers[name]:
            spec["attachment"] = geometry_layers[name]["attachment"]

    anchors = {
        name: point(value, f"anchor {name}")
        for name, value in geometry.get("anchors", {}).items()
    }
    if set(anchors) != set(template["anchors"]):
        missing_anchors = sorted(set(template["anchors"]) - set(anchors))
        extra_anchors = sorted(set(anchors) - set(template["anchors"]))
        raise ValueError(
            f"anchor set mismatch; missing={missing_anchors}, extra={extra_anchors}"
        )

    output_png.parent.mkdir(parents=True, exist_ok=True)
    output_manifest.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(output_png, optimize=True)

    manifest = copy.deepcopy(template)
    manifest["status"] = "production"
    manifest["master"] = copy.deepcopy(master)
    manifest["anchors"] = anchors
    manifest["sprites"] = sprites
    manifest["footprint"] = copy.deepcopy(geometry["footprint"])
    manifest["atlas"]["image"] = output_png.name
    manifest["atlas"]["width"] = atlas_width
    manifest["atlas"]["height"] = atlas_height
    manifest["atlas"]["sizeBytes"] = output_png.stat().st_size
    manifest["qa"]["validated"] = False
    output_manifest.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"built {output_png.name}: {atlas_width}x{atlas_height}, "
        f"{len(sprites)} sprites, {output_png.stat().st_size} bytes"
    )
    print("manifest remains QA-unapproved until review artifacts pass")


def inventory(template_path: Path) -> int:
    template = json.loads(template_path.read_text(encoding="utf-8"))
    names = sorted(expand_sprites(template["sprites"]))
    for name in names:
        print(name)
    print(f"TOTAL={len(names)}", file=sys.stderr)
    return 0


def write_geometry_template(
    template_path: Path, output_path: Path, master_width: int, master_height: int
) -> int:
    template = json.loads(template_path.read_text(encoding="utf-8"))
    sprites = expand_sprites(template["sprites"])
    geometry = {
        "schemaVersion": 1,
        "status": "draft_geometry",
        "objectId": template["objectId"],
        "master": {
            "image": None,
            "width": master_width,
            "height": master_height,
            "approved": False,
        },
        "footprint": {
            "shape": "circle",
            "centerMasterPx": None,
            "radiusPx": None,
            "lockedAnimations": copy.deepcopy(
                template["footprint"]["lockedAnimations"]
            ),
        },
        "anchors": {name: None for name in template["anchors"]},
        "layers": {
            name: {
                "masterPivotPx": None,
                "attachment": spec.get("attachment"),
            }
            for name, spec in sprites.items()
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(geometry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote draft geometry for {len(sprites)} layers: {output_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--write-geometry-template", type=Path)
    parser.add_argument("--master-width", type=int)
    parser.add_argument("--master-height", type=int)
    parser.add_argument("--geometry", type=Path)
    parser.add_argument("--layers", type=Path)
    parser.add_argument("--output-png", type=Path)
    parser.add_argument("--output-manifest", type=Path)
    parser.add_argument("--max-width", type=int, default=2048)
    args = parser.parse_args()

    if args.inventory:
        return inventory(args.template)
    if args.write_geometry_template:
        if not args.master_width or not args.master_height:
            parser.error(
                "--write-geometry-template requires --master-width and --master-height"
            )
        return write_geometry_template(
            args.template,
            args.write_geometry_template,
            args.master_width,
            args.master_height,
        )
    required_args = {
        "--geometry": args.geometry,
        "--layers": args.layers,
        "--output-png": args.output_png,
        "--output-manifest": args.output_manifest,
    }
    missing = [name for name, value in required_args.items() if value is None]
    if missing:
        parser.error(f"required unless --inventory: {', '.join(missing)}")
    try:
        build(
            args.template,
            args.geometry,
            args.layers,
            args.output_png,
            args.output_manifest,
            args.max_width,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

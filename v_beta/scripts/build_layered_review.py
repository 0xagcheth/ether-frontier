#!/usr/bin/env python3
"""Build QA-only review grid and assembled composite from a layered manifest."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

QA_BACKGROUND = "#202326"
CELL_BACKGROUND = "#151719"
LABEL_BACKGROUND = "#30363b"
LABEL_COLOR = "#f2e6cb"
GRID_COLOR = "#596168"


def rect_values(rect: Any) -> tuple[int, int, int, int]:
    if isinstance(rect, list) and len(rect) == 4:
        return tuple(int(value) for value in rect)
    if isinstance(rect, dict):
        return tuple(int(rect[key]) for key in ("x", "y", "w", "h"))
    raise ValueError(f"invalid rect: {rect}")


def load_runtime(manifest_path: Path) -> tuple[dict[str, Any], Image.Image]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    image_path = manifest_path.parent / manifest["atlas"]["image"]
    image = Image.open(image_path).convert("RGBA")
    if list(image.size) != [manifest["atlas"]["width"], manifest["atlas"]["height"]]:
        raise ValueError("manifest atlas size does not match PNG")
    if manifest.get("status") != "production":
        raise ValueError("review builder requires a filled production manifest")
    return manifest, image


def sprite_image(atlas: Image.Image, spec: dict[str, Any]) -> Image.Image:
    x, y, width, height = rect_values(spec["rect"])
    return atlas.crop((x, y, x + width, y + height))


def build_review_grid(
    manifest: dict[str, Any],
    atlas: Image.Image,
    output_path: Path,
    cell_size: int,
    columns: int,
) -> None:
    sprites = sorted(
        manifest["sprites"].items(),
        key=lambda item: (item[1]["drawOrder"], item[0]),
    )
    label_height = 34
    rows = math.ceil(len(sprites) / columns)
    canvas = Image.new(
        "RGBA",
        (columns * cell_size, rows * (cell_size + label_height)),
        QA_BACKGROUND,
    )
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=14)

    for index, (name, spec) in enumerate(sprites):
        column = index % columns
        row = index // columns
        x0 = column * cell_size
        y0 = row * (cell_size + label_height)
        draw.rectangle(
            (x0, y0, x0 + cell_size - 1, y0 + label_height - 1),
            fill=LABEL_BACKGROUND,
        )
        draw.text((x0 + 8, y0 + 9), name, fill=LABEL_COLOR, font=font)
        draw.rectangle(
            (
                x0,
                y0 + label_height,
                x0 + cell_size - 1,
                y0 + label_height + cell_size - 1,
            ),
            fill=CELL_BACKGROUND,
            outline=GRID_COLOR,
        )
        sprite = sprite_image(atlas, spec)
        limit = cell_size - 28
        if sprite.width > limit or sprite.height > limit:
            sprite.thumbnail((limit, limit), Image.Resampling.LANCZOS)
        px = x0 + (cell_size - sprite.width) // 2
        py = y0 + label_height + (cell_size - sprite.height) // 2
        canvas.alpha_composite(sprite, (px, py))

        pivot = spec["pivotPx"]
        scale_x = sprite.width / rect_values(spec["rect"])[2]
        scale_y = sprite.height / rect_values(spec["rect"])[3]
        pivot_x = round(px + pivot[0] * scale_x)
        pivot_y = round(py + pivot[1] * scale_y)
        draw.line((pivot_x - 6, pivot_y, pivot_x + 6, pivot_y), fill="#ff4d4d", width=1)
        draw.line((pivot_x, pivot_y - 6, pivot_x, pivot_y + 6), fill="#ff4d4d", width=1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, optimize=True)


def build_composite(
    manifest: dict[str, Any], atlas: Image.Image, output_path: Path
) -> None:
    master = manifest["master"]
    width, height = int(master["width"]), int(master["height"])
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    default_layers = [
        (name, spec)
        for name, spec in manifest["sprites"].items()
        if spec.get("defaultVisible")
    ]
    for name, spec in sorted(default_layers, key=lambda item: item[1]["drawOrder"]):
        sprite = sprite_image(atlas, spec)
        master_pivot = spec["masterPivotPx"]
        local_pivot = spec["pivotPx"]
        left = round(master_pivot[0] - local_pivot[0])
        top = round(master_pivot[1] - local_pivot[1])
        if left < 0 or top < 0 or left + sprite.width > width or top + sprite.height > height:
            raise ValueError(f"{name}: composite placement clips master canvas")
        canvas.alpha_composite(sprite, (left, top))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--review-grid", type=Path, required=True)
    parser.add_argument("--composite", type=Path, required=True)
    parser.add_argument("--cell-size", type=int, default=256)
    parser.add_argument("--columns", type=int, default=6)
    args = parser.parse_args()
    try:
        manifest, atlas = load_runtime(args.manifest)
        build_review_grid(
            manifest, atlas, args.review_grid, args.cell_size, args.columns
        )
        build_composite(manifest, atlas, args.composite)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"wrote QA review grid: {args.review_grid}")
    print(f"wrote QA composite: {args.composite}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

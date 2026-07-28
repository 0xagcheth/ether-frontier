from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


TRANSPARENT = (0, 0, 0, 0)


def parse_args():
    parser = argparse.ArgumentParser(description="Pack prepared sprite PNGs into a sprite atlas.")
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--out-png", required=True, type=Path)
    parser.add_argument("--out-json", required=True, type=Path)
    parser.add_argument("--prefix", default="")
    parser.add_argument("--cell", type=int, default=64)
    parser.add_argument("--columns", type=int, default=8)
    parser.add_argument("--padding", type=int, default=2)
    parser.add_argument("--chroma-key-black", action="store_true")
    return parser.parse_args()


def transparentize_black(image: Image.Image):
    image = image.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a == 0 or (r == 0 and g == 0 and b == 0):
                pixels[x, y] = TRANSPARENT
    return image


def normalize_to_cell(image: Image.Image, cell: int, chroma_key_black: bool):
    image = transparentize_black(image) if chroma_key_black else image.convert("RGBA")
    if image.width > cell or image.height > cell:
        raise ValueError(f"image {image.size} exceeds atlas cell {cell}")
    output = Image.new("RGBA", (cell, cell), TRANSPARENT)
    x = (cell - image.width) // 2
    y = cell - image.height
    output.alpha_composite(image, (x, y))
    return output


def main():
    args = parse_args()
    files = sorted(args.input_dir.glob("*.png"))
    if args.prefix:
        files = [path for path in files if path.stem.startswith(args.prefix)]
    if not files:
        raise SystemExit("No PNG files found for atlas packing")

    rows = (len(files) + args.columns - 1) // args.columns
    atlas_w = args.padding + args.columns * (args.cell + args.padding)
    atlas_h = args.padding + rows * (args.cell + args.padding)
    atlas = Image.new("RGBA", (atlas_w, atlas_h), TRANSPARENT)
    frames = {}

    for index, path in enumerate(files):
        col = index % args.columns
        row = index // args.columns
        x = args.padding + col * (args.cell + args.padding)
        y = args.padding + row * (args.cell + args.padding)
        cell_img = normalize_to_cell(Image.open(path), args.cell, args.chroma_key_black)
        atlas.alpha_composite(cell_img, (x, y))
        frames[path.stem] = {
            "x": x,
            "y": y,
            "w": args.cell,
            "h": args.cell,
            "source": path.name,
            "pivot": {"x": args.cell // 2, "y": args.cell},
        }

    args.out_png.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(args.out_png)
    manifest = {
        "meta": {
            "image": args.out_png.name,
            "size": {"w": atlas.width, "h": atlas.height},
            "cell": args.cell,
            "padding": args.padding,
            "transparent": True,
        },
        "frames": frames,
    }
    args.out_json.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"packed {len(files)} frames into {args.out_png}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build an exact four-direction master by rotating one complete sprite."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--preview", required=True, type=Path)
    parser.add_argument("--cell", type=int, default=512)
    return parser.parse_args()


def remove_magenta(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    pixels = rgba.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, _ = pixels[x, y]
            keyed = r > 120 and b > 120 and g < 155 and r > g * 1.3 and b > g * 1.3
            white_grid = r > 225 and g > 225 and b > 225
            pixels[x, y] = (r, g, b, 0 if keyed or white_grid else 255)
    return rgba


def main() -> None:
    args = parse_args()
    source = Image.open(args.input).convert("RGB")
    # Canonical up-facing object is the top-left cell of the approved master.
    canonical = source.crop((4, 4, source.width // 2 - 4, source.height // 2 - 4))
    canonical = remove_magenta(canonical)
    bbox = canonical.getbbox()
    if not bbox:
        raise SystemExit("No sprite found in canonical cell")
    canonical = canonical.crop(bbox)
    scale = min((args.cell - 72) / canonical.width, (args.cell - 72) / canonical.height)
    canonical = canonical.resize(
        (round(canonical.width * scale), round(canonical.height * scale)),
        Image.Resampling.LANCZOS,
    )

    rotations = {
        "up": canonical,
        "down": canonical.rotate(180, expand=True, resample=Image.Resampling.BICUBIC),
        "left": canonical.rotate(90, expand=True, resample=Image.Resampling.BICUBIC),
        "right": canonical.rotate(-90, expand=True, resample=Image.Resampling.BICUBIC),
    }
    order = ("up", "down", "left", "right")
    atlas = Image.new("RGBA", (args.cell * 2, args.cell * 2))
    for index, name in enumerate(order):
        sprite = rotations[name]
        x = index % 2 * args.cell + (args.cell - sprite.width) // 2
        y = index // 2 * args.cell + (args.cell - sprite.height) // 2
        atlas.alpha_composite(sprite, (x, y))

    preview = Image.new("RGBA", atlas.size, (255, 0, 255, 255))
    preview.alpha_composite(atlas)
    divider = Image.new("RGBA", atlas.size)
    px = divider.load()
    for x in range(atlas.width):
        px[x, args.cell] = (255, 255, 255, 255)
    for y in range(atlas.height):
        px[args.cell, y] = (255, 255, 255, 255)
    preview.alpha_composite(divider)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.preview.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(args.output)
    preview.convert("RGB").save(args.preview)


if __name__ == "__main__":
    main()

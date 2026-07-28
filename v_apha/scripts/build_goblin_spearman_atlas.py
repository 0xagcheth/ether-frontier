#!/usr/bin/env python3
"""Build the validated goblin spearman animation atlas from 4x2 source sheets."""

from __future__ import annotations

import argparse
import colorsys
import json
from pathlib import Path

from PIL import Image


SEQUENCES = (
    "walk_up",
    "walk_down",
    "walk_left",
    "walk_right",
    "spawn",
    "breach",
    "death",
    "attack",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--up", required=True, type=Path)
    parser.add_argument("--down", required=True, type=Path)
    parser.add_argument("--right", required=True, type=Path)
    parser.add_argument("--spawn", required=True, type=Path)
    parser.add_argument("--breach", required=True, type=Path)
    parser.add_argument("--death", required=True, type=Path)
    parser.add_argument("--attack", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--metadata", required=True, type=Path)
    parser.add_argument("--cell", type=int, default=256)
    return parser.parse_args()


def remove_magenta(frame: Image.Image) -> Image.Image:
    rgba = frame.convert("RGBA")
    pixels = rgba.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, _ = pixels[x, y]
            is_key = r > 115 and b > 115 and g < 150 and r > g * 1.35 and b > g * 1.35
            is_grid = r > 225 and g > 225 and b > 225
            alpha = 0 if is_key or is_grid else 255
            pixels[x, y] = (r, g, b, alpha)
    return rgba


def normalize_palette(sprite: Image.Image) -> Image.Image:
    out = sprite.copy()
    pixels = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            if 0.13 <= h <= 0.33 and s >= 0.18:
                h, s = 0.205, 0.46
            elif (h <= 0.13 or h >= 0.96) and s >= 0.18:
                h, s = 0.075, 0.54
            elif s < 0.2 and v > 0.28:
                h, s = 0.59, 0.07
            nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
            pixels[x, y] = (round(nr * 255), round(ng * 255), round(nb * 255), a)
    return out


def green_height(sprite: Image.Image | None) -> int:
    if sprite is None:
        return 0
    ys: list[int] = []
    for y in range(sprite.height):
        for x in range(sprite.width):
            r, g, b, a = sprite.getpixel((x, y))
            if a > 0 and g > r * 0.88 and g > b * 1.15 and g > 45:
                ys.append(y)
    return max(ys) - min(ys) + 1 if ys else 0


def extract_sprites(path: Path, clean_threshold: bool = False) -> list[Image.Image | None]:
    source = Image.open(path).convert("RGB")
    sprites: list[Image.Image | None] = []
    for index in range(8):
        col = index % 4
        row = index // 4
        left = round(col * source.width / 4) + 4
        right = round((col + 1) * source.width / 4) - 4
        top = round(row * source.height / 2) + 4
        bottom = round((row + 1) * source.height / 2) - 4
        frame = source.crop((left, top, right, bottom))
        if clean_threshold:
            px = frame.load()
            expected_y = 184 if row == 0 else 169
            for y in range(max(0, expected_y - 3), min(frame.height, expected_y + 4)):
                for x in range(frame.width):
                    r, g, b = px[x, y]
                    if r < 90 and g < 45 and b < 90:
                        px[x, y] = (255, 0, 255)
        frame = remove_magenta(frame)
        bbox = frame.getbbox()
        if bbox:
            sprites.append(normalize_palette(frame.crop(bbox)))
        else:
            sprites.append(None)
    return sprites


def normalize_sequence(
    sprites: list[Image.Image | None], cell_size: int, scale: float
) -> list[Image.Image]:
    frames: list[Image.Image] = []
    for sprite in sprites:
        normalized = Image.new("RGBA", (cell_size, cell_size))
        if sprite is not None:
            sprite = sprite.resize(
                (max(1, round(sprite.width * scale)), max(1, round(sprite.height * scale))),
                Image.Resampling.LANCZOS,
            )
            x = (cell_size - sprite.width) // 2
            y = cell_size - sprite.height - 10
            normalized.alpha_composite(sprite, (x, y))
        frames.append(normalized)
    return frames


def main() -> None:
    args = parse_args()
    raw = {
        "walk_up": extract_sprites(args.up),
        "walk_down": extract_sprites(args.down),
        "walk_right": extract_sprites(args.right),
        "spawn": extract_sprites(args.spawn),
        "breach": extract_sprites(args.breach, clean_threshold=True),
        "death": extract_sprites(args.death),
    }
    if args.attack:
        raw["attack"] = extract_sprites(args.attack)

    canonical_green = max(green_height(sprite) for sprite in raw["walk_up"])
    rows: dict[str, list[Image.Image]] = {}
    for name, sprites in raw.items():
        sequence_green = max((green_height(sprite) for sprite in sprites), default=canonical_green)
        identity_scale = canonical_green / max(1, sequence_green)
        max_width = max((sprite.width * identity_scale for sprite in sprites if sprite), default=1)
        max_height = max((sprite.height * identity_scale for sprite in sprites if sprite), default=1)
        fit_scale = min((args.cell - 20) / max_width, (args.cell - 20) / max_height, 1.0)
        rows[name] = normalize_sequence(sprites, args.cell, identity_scale * fit_scale)
    rows["walk_left"] = [frame.transpose(Image.Transpose.FLIP_LEFT_RIGHT) for frame in rows["walk_right"]]

    sequence_names = tuple(name for name in SEQUENCES if name in rows)
    atlas = Image.new("RGBA", (args.cell * 8, args.cell * len(sequence_names)))
    animations: dict[str, dict[str, object]] = {}
    for row, name in enumerate(sequence_names):
        for col, frame in enumerate(rows[name]):
            atlas.alpha_composite(frame, (col * args.cell, row * args.cell))
        animations[name] = {
            "row": row,
            "frames": 8,
            "frame_duration_ms": 100 if name.startswith("walk_") else 120,
            "loop": name.startswith("walk_") or name == "attack",
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(args.output)
    args.metadata.write_text(
        json.dumps(
            {
                "image": args.output.name,
                "frame_width": args.cell,
                "frame_height": args.cell,
                "columns": 8,
                "rows": len(sequence_names),
                "animations": animations,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

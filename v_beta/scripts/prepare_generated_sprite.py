#!/usr/bin/env python3
"""Prepare a generated image as a compact black-key sprite asset."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

OBJECT_DARK = (28, 23, 38)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--width", required=True, type=int)
    parser.add_argument("--height", required=True, type=int)
    parser.add_argument("--threshold", type=int, default=18)
    parser.add_argument("--padding", type=int, default=6)
    return parser.parse_args()


def is_object_pixel(rgb: tuple[int, int, int], threshold: int) -> bool:
    r, g, b = rgb
    return max(r, g, b) > threshold


def find_border_background(img: Image.Image, threshold: int) -> set[tuple[int, int]]:
    pixels = img.load()
    width, height = img.size
    stack: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()

    for x in range(width):
        stack.append((x, 0))
        stack.append((x, height - 1))
    for y in range(height):
        stack.append((0, y))
        stack.append((width - 1, y))

    while stack:
        x, y = stack.pop()
        if (x, y) in seen or x < 0 or y < 0 or x >= width or y >= height:
            continue
        if is_object_pixel(pixels[x, y], threshold):
            continue
        seen.add((x, y))
        stack.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
    return seen


def find_bbox(img: Image.Image, threshold: int) -> tuple[int, int, int, int]:
    pixels = img.load()
    xs: list[int] = []
    ys: list[int] = []
    for y in range(img.height):
        for x in range(img.width):
            if is_object_pixel(pixels[x, y], threshold):
                xs.append(x)
                ys.append(y)
    if not xs:
        return (0, 0, img.width, img.height)
    return (min(xs), min(ys), max(xs) + 1, max(ys) + 1)


def main() -> None:
    args = parse_args()
    source = Image.open(args.input).convert("RGB")
    pixels = source.load()
    background = find_border_background(source, args.threshold)
    for y in range(source.height):
        for x in range(source.width):
            if (x, y) in background:
                pixels[x, y] = (0, 0, 0)
            elif not is_object_pixel(pixels[x, y], args.threshold):
                pixels[x, y] = OBJECT_DARK

    bbox = find_bbox(source, args.threshold)
    cropped = source.crop(bbox)

    max_w = max(1, args.width - args.padding * 2)
    max_h = max(1, args.height - args.padding * 2)
    scale = min(max_w / cropped.width, max_h / cropped.height)
    resized = cropped.resize(
        (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale))),
        Image.Resampling.BOX,
    )

    out = Image.new("RGB", (args.width, args.height), (0, 0, 0))
    x = (args.width - resized.width) // 2
    y = args.height - resized.height - args.padding
    out.paste(resized, (x, y))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.save(args.output)


if __name__ == "__main__":
    main()

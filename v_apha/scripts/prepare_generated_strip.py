#!/usr/bin/env python3
"""Prepare a generated horizontal sprite strip into fixed-size cells."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

OBJECT_DARK = (28, 23, 38)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--frames", required=True, type=int)
    parser.add_argument("--cell-width", required=True, type=int)
    parser.add_argument("--cell-height", required=True, type=int)
    parser.add_argument("--threshold", type=int, default=18)
    parser.add_argument("--padding", type=int, default=2)
    return parser.parse_args()


def is_object_pixel(rgb: tuple[int, int, int], threshold: int) -> bool:
    return max(rgb) > threshold


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


def clean_background(img: Image.Image, threshold: int) -> Image.Image:
    out = img.convert("RGB")
    pixels = out.load()
    background = find_border_background(out, threshold)
    for y in range(out.height):
        for x in range(out.width):
            if (x, y) in background:
                pixels[x, y] = (0, 0, 0)
            elif not is_object_pixel(pixels[x, y], threshold):
                pixels[x, y] = OBJECT_DARK
    return out


def find_bbox(img: Image.Image, threshold: int) -> tuple[int, int, int, int]:
    pixels = img.load()
    min_x, min_y = img.width, img.height
    max_x, max_y = -1, -1
    for y in range(img.height):
        for x in range(img.width):
            if is_object_pixel(pixels[x, y], threshold):
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    if max_x < min_x:
        return (0, 0, img.width, img.height)
    return (min_x, min_y, max_x + 1, max_y + 1)


def fit_frame(frame: Image.Image, width: int, height: int, padding: int, threshold: int) -> Image.Image:
    cleaned = clean_background(frame, threshold)
    cropped = cleaned.crop(find_bbox(cleaned, threshold))
    max_w = max(1, width - padding * 2)
    max_h = max(1, height - padding * 2)
    scale = min(max_w / cropped.width, max_h / cropped.height)
    resized = cropped.resize(
        (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale))),
        Image.Resampling.BOX,
    )
    out = Image.new("RGB", (width, height), (0, 0, 0))
    x = (width - resized.width) // 2
    y = height - resized.height - padding
    out.paste(resized, (x, y))
    return out


def main() -> None:
    args = parse_args()
    source = Image.open(args.input).convert("RGB")
    source_cell_w = source.width / args.frames
    out = Image.new("RGB", (args.cell_width * args.frames, args.cell_height), (0, 0, 0))
    for i in range(args.frames):
        left = round(i * source_cell_w)
        right = round((i + 1) * source_cell_w)
        source_frame = source.crop((left, 0, right, source.height))
        out_frame = fit_frame(source_frame, args.cell_width, args.cell_height, args.padding, args.threshold)
        out.paste(out_frame, (i * args.cell_width, 0))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.save(args.output)


if __name__ == "__main__":
    main()

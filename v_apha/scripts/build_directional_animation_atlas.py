#!/usr/bin/env python3
"""Build a 4-direction, 8-frame atlas from a generated 4x2 UP master."""

from pathlib import Path
import sys

from PIL import Image, ImageDraw


MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
ROTATIONS = (0, 180, 90, 270)  # UP, DOWN, LEFT, RIGHT (Pillow CCW)


def frame_box(width: int, height: int, frame: int) -> tuple[int, int, int, int]:
    col = frame % 4
    row = frame // 4
    x0 = round(col * width / 4)
    x1 = round((col + 1) * width / 4)
    y0 = round(row * height / 2)
    y1 = round((row + 1) * height / 2)
    # Remove generated white separators from the source cell.
    inset = 3
    return x0 + inset, y0 + inset, x1 - inset, y1 - inset


def build(source: Path, destination: Path) -> None:
    image = Image.open(source).convert("RGB")
    frames = [image.crop(frame_box(*image.size, index)) for index in range(8)]
    cell = max(max(frame.size) for frame in frames)
    divider = 2
    atlas_width = cell * 8 + divider * 7
    atlas_height = cell * 4 + divider * 3
    atlas = Image.new("RGB", (atlas_width, atlas_height), MAGENTA)
    draw = ImageDraw.Draw(atlas)

    for direction, angle in enumerate(ROTATIONS):
        for frame_index, frame in enumerate(frames):
            square = Image.new("RGB", (cell, cell), MAGENTA)
            square.paste(frame, ((cell - frame.width) // 2, (cell - frame.height) // 2))
            rotated = square.rotate(angle, resample=Image.Resampling.BICUBIC, fillcolor=MAGENTA)
            x = frame_index * (cell + divider)
            y = direction * (cell + divider)
            atlas.paste(rotated, (x, y))

    for col in range(1, 8):
        x = col * cell + (col - 1) * divider
        draw.rectangle((x, 0, x + divider - 1, atlas_height - 1), fill=WHITE)
    for row in range(1, 4):
        y = row * cell + (row - 1) * divider
        draw.rectangle((0, y, atlas_width - 1, y + divider - 1), fill=WHITE)

    destination.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(destination, optimize=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: build_directional_animation_atlas.py SOURCE DESTINATION")
    build(Path(sys.argv[1]), Path(sys.argv[2]))

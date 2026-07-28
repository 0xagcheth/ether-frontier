#!/usr/bin/env python3
"""Normalize generated sprite atlases into 64px alpha atlases and frame files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/sprite-atlases/goblin-spearman/animations"
BASE_SOURCE = ROOT / "assets/sprite-atlases/goblin-spearman/goblin-spearman-directions-v2.png"
OUTPUT = SOURCE / "runtime-64"
HD_OUTPUT = SOURCE / "runtime-384"
FRAME_SIZE = 64
CONTENT_SIZE = 58
HD_FRAME_SIZE = 384
HD_NEUTRAL_EXTENT = 255
KEY = (255, 0, 255)


SPECS = {
    "walk": ("walk-all-directions-v1.png", 8, 4, 2, ("UP", "DOWN", "LEFT", "RIGHT"), 90),
    "attack": ("attack-all-directions-v1.png", 8, 4, 2, ("UP", "DOWN", "LEFT", "RIGHT"), 80),
    "death": ("death-all-directions-v1.png", 8, 4, 2, ("UP", "DOWN", "LEFT", "RIGHT"), 110),
    "spawn": ("spawn-v1.png", 4, 2, 0, ("UP",), 100),
    "breach": ("breach-v1.png", 4, 2, 0, ("UP",), 90),
}


def split_grid(image: Image.Image, columns: int, rows: int, divider: int) -> list[Image.Image]:
    width, height = image.size
    cell_width = (width - divider * (columns - 1)) / columns
    cell_height = (height - divider * (rows - 1)) / rows
    frames = []
    for row in range(rows):
        for column in range(columns):
            x0 = round(column * (cell_width + divider)) + 5
            x1 = round(column * (cell_width + divider) + cell_width) - 5
            y0 = round(row * (cell_height + divider)) + 5
            y1 = round(row * (cell_height + divider) + cell_height) - 5
            frames.append(image.crop((x0, y0, x1, y1)).convert("RGBA"))
    return frames


def key_to_alpha(image: Image.Image, preserve_white: bool = False) -> Image.Image:
    pixels = []
    for red, green, blue, _ in image.getdata():
        if not preserve_white and red >= 245 and green >= 245 and blue >= 245:
            pixels.append((red, green, blue, 0))
            continue
        # Generated chroma backgrounds contain gradients and compressed shadow hues,
        # so remove the full red+blue-dominant magenta family rather than one RGB key.
        magenta_red = red - green * 1.40
        magenta_blue = blue - green * 1.20
        chroma_score = min(magenta_red, magenta_blue)
        if red + blue > 170 and chroma_score >= 42:
            alpha = 0
        elif red + blue > 150 and chroma_score > 12:
            alpha = round(255 * (42 - chroma_score) / 30)
        else:
            alpha = 255
        if alpha < 255:
            # Despill partially transparent edges without changing opaque artwork.
            neutral = min(red, blue)
            red = round(red * alpha / 255 + neutral * (255 - alpha) / 255)
            blue = round(blue * alpha / 255 + neutral * (255 - alpha) / 255)
        pixels.append((red, green, blue, alpha))
    image.putdata(pixels)
    return image


def union_bbox(frames: Iterable[Image.Image]) -> tuple[int, int, int, int]:
    boxes = [frame.getchannel("A").getbbox() for frame in frames]
    valid = [box for box in boxes if box is not None]
    if not valid:
        return 0, 0, 1, 1
    return (
        min(box[0] for box in valid),
        min(box[1] for box in valid),
        max(box[2] for box in valid),
        max(box[3] for box in valid),
    )


def normalize(frames: list[Image.Image]) -> list[Image.Image]:
    bbox = union_bbox(frames)
    crop_width = bbox[2] - bbox[0]
    crop_height = bbox[3] - bbox[1]
    scale = min(CONTENT_SIZE / crop_width, CONTENT_SIZE / crop_height)
    size = (max(1, round(crop_width * scale)), max(1, round(crop_height * scale)))
    normalized = []
    for frame in frames:
        cropped = frame.crop(bbox).resize(size, Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
        canvas.alpha_composite(cropped, ((FRAME_SIZE - size[0]) // 2, (FRAME_SIZE - size[1]) // 2))
        normalized.append(canvas)
    return normalized


def largest_olive_component_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    width, height = image.size
    pixels = image.load()
    mask = set()
    for y in range(height):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            if alpha > 180 and green >= red * 0.72 and green > blue * 1.18 and red + green > 105:
                mask.add((x, y))
    largest = []
    while mask:
        seed = mask.pop()
        stack = [seed]
        component = [seed]
        while stack:
            x, y = stack.pop()
            for point in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if point in mask:
                    mask.remove(point)
                    stack.append(point)
                    component.append(point)
        if len(component) > len(largest):
            largest = component
    if not largest:
        return 0, 0, max(1, width // 3), max(1, height // 3)
    xs = [point[0] for point in largest]
    ys = [point[1] for point in largest]
    return min(xs), min(ys), max(xs) + 1, max(ys) + 1


def normalize_hd(frames: list[Image.Image], calibration_index: int = 0) -> list[Image.Image]:
    calibration_bbox = frames[calibration_index].getchannel("A").getbbox()
    if calibration_bbox is None:
        calibration_bbox = (0, 0, 1, 1)
    calibration_extent = max(
        calibration_bbox[2] - calibration_bbox[0],
        calibration_bbox[3] - calibration_bbox[1],
    )
    scale = HD_NEUTRAL_EXTENT / max(1, calibration_extent)
    normalized = []
    for frame in frames:
        resized = frame.resize(
            (max(1, round(frame.width * scale)), max(1, round(frame.height * scale))),
            Image.Resampling.LANCZOS,
        )
        content_bbox = resized.getchannel("A").getbbox()
        if content_bbox is None:
            normalized.append(Image.new("RGBA", (HD_FRAME_SIZE, HD_FRAME_SIZE), (0, 0, 0, 0)))
            continue
        content = resized.crop(content_bbox)
        canvas = Image.new("RGBA", (HD_FRAME_SIZE, HD_FRAME_SIZE), (0, 0, 0, 0))
        canvas.alpha_composite(
            content,
            ((HD_FRAME_SIZE - content.width) // 2, (HD_FRAME_SIZE - content.height) // 2),
        )
        normalized.append(canvas)
    return normalized


def build_animation(name: str, spec: tuple) -> dict:
    filename, columns, rows, divider, directions, duration = spec
    source = Image.open(SOURCE / filename)
    raw = [key_to_alpha(frame) for frame in split_grid(source, columns, rows, divider)]
    frames = normalize(raw)

    if len(directions) == 1:
        ordered = [frames[index] for index in range(8)]
        atlas_rows = 1
    else:
        ordered = frames
        atlas_rows = 4

    atlas = Image.new("RGBA", (FRAME_SIZE * 8, FRAME_SIZE * atlas_rows), (0, 0, 0, 0))
    frame_root = OUTPUT / "frames" / name
    for index, frame in enumerate(ordered):
        row = index // 8
        column = index % 8
        atlas.alpha_composite(frame, (column * FRAME_SIZE, row * FRAME_SIZE))
        direction = directions[row] if row < len(directions) else directions[0]
        frame_dir = frame_root / direction.lower()
        frame_dir.mkdir(parents=True, exist_ok=True)
        frame.save(frame_dir / f"{name}-{direction.lower()}-{column + 1:02d}.png", optimize=True)

    atlas_path = OUTPUT / f"{name}-64-alpha.png"
    atlas.save(atlas_path, optimize=True)
    return {
        "file": atlas_path.name,
        "columns": 8,
        "rows": atlas_rows,
        "frameWidth": FRAME_SIZE,
        "frameHeight": FRAME_SIZE,
        "directionRows": list(directions),
        "frameDurationMs": duration,
        "loop": name in {"walk"},
        "frameFiles": f"frames/{name}/<direction>/{name}-<direction>-01..08.png",
    }


def build_base_directions() -> dict:
    source = Image.open(BASE_SOURCE)
    frames = normalize([key_to_alpha(frame) for frame in split_grid(source, 2, 2, 0)])
    directions = ("UP", "DOWN", "LEFT", "RIGHT")
    atlas = Image.new("RGBA", (FRAME_SIZE * 4, FRAME_SIZE), (0, 0, 0, 0))
    frame_root = OUTPUT / "frames" / "idle"
    for index, (direction, frame) in enumerate(zip(directions, frames)):
        atlas.alpha_composite(frame, (index * FRAME_SIZE, 0))
        frame_root.mkdir(parents=True, exist_ok=True)
        frame.save(frame_root / f"idle-{direction.lower()}.png", optimize=True)
    atlas_path = OUTPUT / "idle-directions-64-alpha.png"
    atlas.save(atlas_path, optimize=True)
    return {
        "file": atlas_path.name,
        "columns": 4,
        "rows": 1,
        "frameWidth": FRAME_SIZE,
        "frameHeight": FRAME_SIZE,
        "columnOrder": list(directions),
        "frameFiles": "frames/idle/idle-<direction>.png",
    }


def build_hd_atlas(name: str, spec: tuple) -> dict:
    filename, columns, rows, divider, directions, duration = spec
    source = Image.open(SOURCE / filename)
    raw = [key_to_alpha(frame) for frame in split_grid(source, columns, rows, divider)]
    calibration_index = 7 if name == "spawn" else 0
    frames = normalize_hd(raw, calibration_index)
    atlas_rows = 1 if len(directions) == 1 else 4
    atlas = Image.new("RGBA", (HD_FRAME_SIZE * 8, HD_FRAME_SIZE * atlas_rows), (0, 0, 0, 0))
    for index, frame in enumerate(frames):
        atlas.alpha_composite(frame, ((index % 8) * HD_FRAME_SIZE, (index // 8) * HD_FRAME_SIZE))
    path = HD_OUTPUT / f"{name}-384-alpha.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(path, optimize=True)
    return {
        "file": path.name,
        "columns": 8,
        "rows": atlas_rows,
        "frameWidth": HD_FRAME_SIZE,
        "frameHeight": HD_FRAME_SIZE,
        "directionRows": list(directions),
        "frameDurationMs": duration,
        "loop": name == "walk",
        "normalization": "shared 255px neutral silhouette extent in a 384px safety cell; centered content with safe margins",
    }


def build_hd_base() -> dict:
    source = Image.open(BASE_SOURCE)
    raw = [key_to_alpha(frame) for frame in split_grid(source, 2, 2, 0)]
    frames = normalize_hd(raw)
    atlas = Image.new("RGBA", (HD_FRAME_SIZE * 4, HD_FRAME_SIZE), (0, 0, 0, 0))
    for index, frame in enumerate(frames):
        atlas.alpha_composite(frame, (index * HD_FRAME_SIZE, 0))
    path = HD_OUTPUT / "idle-directions-384-alpha.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(path, optimize=True)
    return {
        "file": path.name,
        "columns": 4,
        "rows": 1,
        "frameWidth": HD_FRAME_SIZE,
        "frameHeight": HD_FRAME_SIZE,
        "columnOrder": ["UP", "DOWN", "LEFT", "RIGHT"],
        "normalization": "shared 255px neutral silhouette extent in a 384px safety cell; centered content with safe margins",
    }


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "character": "goblin-spearman",
        "format": "RGBA PNG",
        "frameSize": [FRAME_SIZE, FRAME_SIZE],
        "origin": "center",
        "idleDirections": build_base_directions(),
        "animations": {name: build_animation(name, spec) for name, spec in SPECS.items()},
    }
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    HD_OUTPUT.mkdir(parents=True, exist_ok=True)
    hd_manifest = {
        "character": "goblin-spearman",
        "format": "RGBA PNG",
        "frameSize": [HD_FRAME_SIZE, HD_FRAME_SIZE],
        "origin": "center",
        "idleDirections": build_hd_base(),
        "animations": {name: build_hd_atlas(name, spec) for name, spec in SPECS.items()},
    }
    (HD_OUTPUT / "manifest.json").write_text(json.dumps(hd_manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()

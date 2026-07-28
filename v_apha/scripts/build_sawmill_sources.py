#!/usr/bin/env python3
"""Create Sawmill source strips from the selected cardboard master."""

from __future__ import annotations

from collections import deque
from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/sprite-atlases/sawmill/source"
RAW = SOURCE / "sawmill-master-raw-cardboard-v2.png"
MAGENTA = (255, 0, 255, 255)


def is_border_background(pixel: tuple[int, int, int, int]) -> bool:
    red, green, blue, alpha = pixel
    if alpha < 12:
        return True
    return min(red, green, blue) > 214 and max(red, green, blue) - min(red, green, blue) < 46


def remove_light_border(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    width, height = image.size
    pixels = image.load()
    queue: deque[tuple[int, int]] = deque()
    seen: set[tuple[int, int]] = set()
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))

    while queue:
        x, y = queue.popleft()
        if (x, y) in seen or not is_border_background(pixels[x, y]):
            continue
        seen.add((x, y))
        if x:
            queue.append((x - 1, y))
        if x + 1 < width:
            queue.append((x + 1, y))
        if y:
            queue.append((x, y - 1))
        if y + 1 < height:
            queue.append((x, y + 1))

    alpha = image.getchannel("A")
    alpha_pixels = alpha.load()
    for x, y in seen:
        alpha_pixels[x, y] = 0
    image.putalpha(alpha)
    return image


def on_magenta(image: Image.Image) -> Image.Image:
    output = Image.new("RGBA", image.size, MAGENTA)
    output.alpha_composite(image)
    return output.convert("RGB").convert("RGBA")


def bbox(image: Image.Image) -> tuple[int, int, int, int]:
    box = image.getchannel("A").getbbox()
    if not box:
        raise ValueError("empty sawmill source")
    return box


def paste_anchor(canvas: Image.Image, content: Image.Image, box: tuple[int, int, int, int], dx: int = 0, dy: int = 0) -> None:
    canvas.alpha_composite(content.crop(box), (box[0] + dx, box[1] + dy))


def add_sawdust(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], phase: int, alpha: int = 170) -> None:
    left, top, right, bottom = box
    cx = left + int((right - left) * 0.58)
    cy = top + int((bottom - top) * 0.68)
    for i in range(18):
        angle = (phase * 0.8 + i * 0.9) % (math.pi * 2)
        radius = 14 + (i % 5) * 7 + phase * 2
        x = cx + int(math.cos(angle) * radius)
        y = cy + int(math.sin(angle) * radius * 0.45) + phase * 2
        color = (222, 158, 75, max(45, alpha - i * 5))
        draw.rectangle((x, y, x + 2, y + 2), fill=color)


def add_saw_glint(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], phase: int) -> None:
    left, top, right, bottom = box
    cx = left + int((right - left) * 0.60)
    cy = top + int((bottom - top) * 0.61)
    radius = int((right - left) * 0.105)
    angle = phase * math.pi * 0.55
    x = cx + int(math.cos(angle) * radius)
    y = cy + int(math.sin(angle) * radius)
    draw.line((cx, cy, x, y), fill=(255, 255, 236, 118), width=5)
    draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(255, 240, 190, 130))


def make_idle(master: Image.Image) -> Image.Image:
    box = bbox(master)
    frames = []
    for phase in range(5):
        frame = master.copy()
        overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        add_saw_glint(draw, box, phase)
        add_sawdust(draw, box, phase, 150)
        frame.alpha_composite(overlay)
        frames.append(on_magenta(frame))
    strip = Image.new("RGBA", (master.width * 5, master.height), MAGENTA)
    for i, frame in enumerate(frames):
        strip.alpha_composite(frame, (i * master.width, 0))
    return strip


def make_destroy(master: Image.Image) -> Image.Image:
    box = bbox(master)
    left, top, right, bottom = box
    frames = []
    for phase in range(5):
        frame = Image.new("RGBA", master.size, (0, 0, 0, 0))
        if phase < 2:
            paste_anchor(frame, master, box)
        else:
            crop = master.crop(box)
            squash = 1.0 - phase * 0.045
            dark = ImageEnhance.Brightness(crop).enhance(1.0 - phase * 0.08)
            resized = dark.resize((crop.width, max(1, round(crop.height * squash))), Image.Resampling.LANCZOS)
            frame.alpha_composite(resized, (left, bottom - resized.height + phase * 3))
        overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        if phase:
            add_sawdust(draw, box, phase + 2, 210)
        if phase >= 2:
            for i in range(phase * 10):
                x = left + 50 + ((i * 73 + phase * 17) % max(1, right - left - 100))
                y = bottom - 76 + ((i * 29 + phase * 11) % 36)
                draw.rectangle((x, y, x + 8, y + 4), fill=(116, 72, 37, 190))
                draw.line((x, y, x + 8, y + 4), fill=(211, 148, 76, 125), width=1)
        frame.alpha_composite(overlay)
        frames.append(on_magenta(frame))
    strip = Image.new("RGBA", (master.width * 5, master.height), MAGENTA)
    for i, frame in enumerate(frames):
        strip.alpha_composite(frame, (i * master.width, 0))
    return strip


def main() -> None:
    SOURCE.mkdir(parents=True, exist_ok=True)
    master = remove_light_border(Image.open(RAW))
    on_magenta(master).save(SOURCE / "sawmill-master-v1.png", optimize=True)
    make_idle(master).save(SOURCE / "sawmill-idle-source-v1.png", optimize=True)
    make_destroy(master).save(SOURCE / "sawmill-destroy-source-v1.png", optimize=True)


if __name__ == "__main__":
    main()

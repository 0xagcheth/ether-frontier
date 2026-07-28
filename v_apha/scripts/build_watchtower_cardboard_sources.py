#!/usr/bin/env python3
"""Create cardboard-style Watchtower source strips from the selected master."""

from __future__ import annotations

from collections import deque
from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/sprite-atlases/watchtower/source"
RAW = SOURCE / "watchtower-master-raw-topdown-v3.png"
MAGENTA = (255, 0, 255, 255)


def is_light_border(pixel: tuple[int, int, int, int]) -> bool:
    red, green, blue, alpha = pixel
    if alpha < 12:
        return True
    return min(red, green, blue) > 216 and max(red, green, blue) - min(red, green, blue) < 52


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
        if (x, y) in seen or not is_light_border(pixels[x, y]):
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
    for point in seen:
        alpha_pixels[point] = 0
    image.putalpha(alpha)
    return image


def on_magenta(image: Image.Image) -> Image.Image:
    output = Image.new("RGBA", image.size, MAGENTA)
    output.alpha_composite(image)
    return output.convert("RGB").convert("RGBA")


def bbox(image: Image.Image) -> tuple[int, int, int, int]:
    box = image.getchannel("A").getbbox()
    if not box:
        raise ValueError("empty watchtower source")
    return box


def save_strip(frames: list[Image.Image], path: Path) -> None:
    width, height = frames[0].size
    strip = Image.new("RGBA", (width * len(frames), height), MAGENTA)
    for index, frame in enumerate(frames):
        strip.alpha_composite(on_magenta(frame), (index * width, 0))
    strip.save(path, optimize=True)


def draw_lantern_glow(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], phase: int) -> None:
    left, top, right, bottom = box
    cx = left + int((right - left) * 0.72)
    cy = top + int((bottom - top) * 0.78)
    radius = [13, 16, 18, 15, 13][phase]
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=(255, 174, 54, 34 + phase * 8))
    draw.polygon(
        [(cx, cy - 9), (cx + 6, cy + 4), (cx, cy + 10), (cx - 6, cy + 4)],
        fill=(255, 205, 82, 170),
    )


def draw_muzzle_flash(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], phase: int) -> None:
    left, top, right, bottom = box
    cx = left + int((right - left) * 0.06)
    cy = top + int((bottom - top) * 0.50)
    length = [18, 70, 98, 30][phase]
    alpha = [70, 220, 250, 110][phase]
    if phase in {1, 2}:
        draw.line((cx + 18, cy, cx - length, cy), fill=(255, 197, 48, alpha), width=10)
        draw.line((cx + 12, cy - 12, cx - length // 2, cy - 28), fill=(255, 236, 142, alpha // 2), width=4)
        draw.line((cx + 12, cy + 12, cx - length // 2, cy + 28), fill=(255, 236, 142, alpha // 2), width=4)
    draw.polygon(
        [(cx - length, cy), (cx - 6, cy - 12), (cx + 8, cy), (cx - 6, cy + 12)],
        fill=(255, 190, 58, alpha),
    )
    draw.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=(255, 231, 141, min(255, alpha + 30)))


def make_idle(master: Image.Image) -> list[Image.Image]:
    box = bbox(master)
    frames = []
    for phase in range(5):
        frame = master.copy()
        overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        draw_lantern_glow(draw, box, phase)
        frame.alpha_composite(overlay)
        frames.append(frame)
    return frames


def make_attack(master: Image.Image) -> list[Image.Image]:
    box = bbox(master)
    frames = []
    for phase in range(4):
        frame = master.copy()
        overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        draw_muzzle_flash(draw, box, phase)
        if phase in {1, 2}:
            left, top, right, bottom = box
            cx = (left + right) // 2
            cy = top + int((bottom - top) * 0.35)
            draw.arc((cx - 170, cy - 60, cx + 170, cy + 68), 203, 337, fill=(255, 231, 170, 115), width=5)
        frame.alpha_composite(overlay)
        frames.append(frame)
    return frames


def make_destroy(master: Image.Image) -> list[Image.Image]:
    box = bbox(master)
    left, top, right, bottom = box
    crop = master.crop(box)
    frames = []
    for phase in range(5):
        frame = Image.new("RGBA", master.size, (0, 0, 0, 0))
        if phase < 2:
            frame.alpha_composite(crop, (left, top))
        else:
            scale = 1.0 - phase * 0.055
            dark = ImageEnhance.Brightness(crop).enhance(1.0 - phase * 0.08)
            resized = dark.resize((max(1, round(crop.width * scale)), max(1, round(crop.height * scale))), Image.Resampling.LANCZOS)
            frame.alpha_composite(resized, (left + (crop.width - resized.width) // 2, top + phase * 14))
        overlay = Image.new("RGBA", master.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        if phase:
            for i in range(phase * 10):
                x = left + 50 + ((i * 83 + phase * 31) % max(1, right - left - 100))
                y = top + int((bottom - top) * 0.58) + ((i * 37 + phase * 19) % max(1, int((bottom - top) * 0.20)))
                angle = ((i + phase) % 8) * math.pi / 4
                x2 = x + int(math.cos(angle) * 10)
                y2 = y + int(math.sin(angle) * 7)
                draw.line((x, y, x2, y2), fill=(131, 86, 46, 190), width=4)
                draw.rectangle((x - 3, y - 3, x + 4, y + 4), fill=(102, 102, 95, 170))
        frame.alpha_composite(overlay)
        frames.append(frame)
    return frames


def make_projectile(size: int = 512) -> Image.Image:
    image = Image.new("RGBA", (size, size), MAGENTA)
    draw = ImageDraw.Draw(image)
    cx, cy = size // 2, size // 2
    draw.line((cx, cy + 58, cx, cy - 44), fill=(113, 77, 42, 255), width=16)
    draw.polygon([(cx, cy - 74), (cx + 22, cy - 34), (cx, cy - 46), (cx - 22, cy - 34)], fill=(192, 188, 169, 255))
    draw.polygon([(cx, cy + 72), (cx + 24, cy + 36), (cx, cy + 48), (cx - 24, cy + 36)], fill=(151, 45, 35, 245))
    draw.line((cx, cy + 54, cx, cy - 40), fill=(230, 177, 92, 170), width=4)
    return image


def main() -> None:
    master = remove_light_border(Image.open(RAW))
    on_magenta(master).save(SOURCE / "watchtower-master-v1.png", optimize=True)
    save_strip(make_idle(master), SOURCE / "watchtower-idle-source-v1.png")
    save_strip(make_attack(master), SOURCE / "watchtower-attack-source-v1.png")
    save_strip(make_destroy(master), SOURCE / "watchtower-destroy-source-v1.png")
    make_projectile().save(SOURCE / "watchtower-projectile-source-v1.png", optimize=True)


if __name__ == "__main__":
    main()

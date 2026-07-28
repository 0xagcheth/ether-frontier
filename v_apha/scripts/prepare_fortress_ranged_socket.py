#!/usr/bin/env python3
"""Promote the approved fortress_ranged socket and build a scale QA composite."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/staging/candidates/modules/fortress_ranged/fortress_ranged__center_socket__light_bearing_v1_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
BASE_IMAGE = CANON / "fortress_ranged__base_token__round_light_v1_alpha.png"
BASE_MANIFEST = CANON / "fortress_ranged__base_token__round_light_v1.json"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"

MODULE_NAME = "fortress_ranged__center_socket__light_bearing_v1"
TARGET_FOOTPRINT_RATIO = 0.34


def chroma_to_alpha(source: Image.Image) -> Image.Image:
    image = source.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, _ = pixels[x, y]
            distance = ((r - 255) ** 2 + g * g + (b - 255) ** 2) ** 0.5
            alpha = max(0, min(255, round((distance - 28) * 255 / 172)))
            if r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38:
                alpha = 0
            pixels[x, y] = (r, g, b, alpha)
    return image


def alpha_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty socket cutout")
    return bbox


def checker(size: tuple[int, int], cell: int = 32) -> Image.Image:
    out = Image.new("RGB", size, "#d9d1bd")
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#c8bea7")
    return out.convert("RGBA")


def centered_paste(canvas: Image.Image, layer: Image.Image) -> None:
    x = (canvas.width - layer.width) // 2
    y = (canvas.height - layer.height) // 2
    canvas.alpha_composite(layer, (x, y))


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)

    source = Image.open(SOURCE)
    cutout_full = chroma_to_alpha(source)
    cutout = cutout_full.crop(alpha_bbox(cutout_full))

    chroma_path = CANON / f"{MODULE_NAME}_chroma.png"
    alpha_path = CANON / f"{MODULE_NAME}_alpha.png"
    source.save(chroma_path, optimize=True)
    cutout.save(alpha_path, optimize=True)

    pivot = [cutout.width // 2, cutout.height // 2]
    base_meta = json.loads(BASE_MANIFEST.read_text())
    target_footprint = round(base_meta["footprintPx"] * TARGET_FOOTPRINT_RATIO)
    scale = target_footprint / max(cutout.size)
    composed_size = [round(cutout.width * scale), round(cutout.height * scale)]

    manifest = {
        "schemaVersion": 1,
        "module": "fortress_ranged__center_socket__light_bearing",
        "family": "fortress_ranged",
        "slot": "center_socket",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(cutout.size),
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / cutout.width, 6), round(pivot[1] / cutout.height, 6)],
        "projection": "true_top_down_orthographic_90deg",
        "sharedBy": ["watchtower", "ranger", "tracker", "assassin"],
        "attachment": {
            "parentSlot": "base_token.center",
            "positionNormalized": [0.5, 0.5],
            "scaleToParentFootprint": TARGET_FOOTPRINT_RATIO,
            "rotationDeg": 0,
        },
        "drawOrder": 10,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "magentaSpillPixels": 0,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{MODULE_NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    base = Image.open(BASE_IMAGE).convert("RGBA")
    socket_scaled = cutout.resize(tuple(composed_size), Image.Resampling.LANCZOS)
    margin = 80
    canvas_size = (base.width + margin * 2, base.height + margin * 2)

    transparent = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    centered_paste(transparent, base)
    centered_paste(transparent, socket_scaled)
    transparent_path = REVIEW / "fortress_ranged__base_plus_center_socket_v1_composite.png"
    transparent.save(transparent_path, optimize=True)

    qa = checker(canvas_size)
    centered_paste(qa, base)
    centered_paste(qa, socket_scaled)
    draw = ImageDraw.Draw(qa)
    cx, cy = qa.width // 2, qa.height // 2
    draw.line((cx - 20, cy, cx + 20, cy), fill="#d94841", width=3)
    draw.line((cx, cy - 20, cx, cy + 20), fill="#d94841", width=3)
    qa_path = REVIEW / "fortress_ranged__base_plus_center_socket_v1_review.png"
    qa.convert("RGB").save(qa_path, optimize=True)

    result = {
        "manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)),
        "composite": str(transparent_path.relative_to(ROOT)),
        "review": str(qa_path.relative_to(ROOT)),
        "sourceSize": list(source.size),
        "tightSize": list(cutout.size),
        "pivotPx": pivot,
        "composedSize": composed_size,
        "scaleToBaseFootprint": TARGET_FOOTPRINT_RATIO,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

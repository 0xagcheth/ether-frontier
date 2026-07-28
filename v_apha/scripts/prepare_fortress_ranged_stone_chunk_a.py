#!/usr/bin/env python3
"""Promote the first fortress-ranged stone debris piece and validate its scale."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
SOURCE = CANDIDATES / "fortress_ranged__debris__stone_rim_chunk_a_v1_chroma.png"
ALPHA_FULL = CANDIDATES / "fortress_ranged__debris__stone_rim_chunk_a_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
BASE_IMAGE = CANON / "fortress_ranged__base_token__round_light_v1_alpha.png"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"

NAME = "fortress_ranged__debris__stone_rim_chunk_a_v1"
SCALE_TO_BASE = 0.14


def tight_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty debris cutout")
    return bbox


def center_of_mass(image: Image.Image) -> list[int]:
    alpha = image.getchannel("A")
    weighted_x = weighted_y = total = 0
    for y in range(image.height):
        for x in range(image.width):
            weight = alpha.getpixel((x, y))
            if weight > 18:
                weighted_x += x * weight
                weighted_y += y * weight
                total += weight
    if not total:
        raise RuntimeError("debris has no visible mass")
    return [round(weighted_x / total), round(weighted_y / total)]


def checker(size: tuple[int, int], cell: int = 20) -> Image.Image:
    out = Image.new("RGB", size, "#d9d1bd")
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#c8bea7")
    return out.convert("RGBA")


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    full = Image.open(ALPHA_FULL).convert("RGBA")
    crop = full.crop(tight_bbox(full))
    pivot = center_of_mass(crop)

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    base = json.loads(BASE_META.read_text())
    target_width = round(base["footprintPx"] * SCALE_TO_BASE)
    scale = target_width / crop.width
    composed_size = [target_width, round(crop.height * scale)]
    composed_pivot = [round(pivot[0] * scale), round(pivot[1] * scale)]
    visible = [pixel for pixel in crop.getdata() if pixel[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38)

    manifest = {
        "schemaVersion": 1,
        "module": "fortress_ranged__debris__stone_rim_chunk_a",
        "family": "fortress_ranged",
        "slot": "debris",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(crop.size),
        "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height},
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / crop.width, 6), round(pivot[1] / crop.height, 6)],
        "pivotMethod": "alpha_weighted_center_of_mass",
        "projection": "true_top_down_orthographic_90deg",
        "sharedBy": ["watchtower", "ranger", "tracker", "assassin"],
        "runtimeScale": {"scaleToBaseFootprint": SCALE_TO_BASE},
        "destroyPhysics": {
            "massClass": "medium",
            "radialVelocityPxPerSec": [90, 170],
            "angularVelocityDegPerSec": [-220, 220],
            "linearDrag": 0.92,
            "lifetimeMs": [700, 1100],
        },
        "drawOrder": 60,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "singleConnectedPiece": True,
            "magentaSpillPixels": spill,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    base_image = Image.open(BASE_IMAGE).convert("RGBA")
    piece = crop.resize(tuple(composed_size), Image.Resampling.LANCZOS)
    tile = 620
    header = 40
    grid = Image.new("RGB", (tile * 2, tile + header), "#292a2b")
    font = ImageFont.load_default()

    # Panel 1: compare against the intact base rim.
    panel_a = checker((tile, tile), 24)
    base_preview = base_image.resize((540, round(base_image.height * 540 / base_image.width)), Image.Resampling.LANCZOS)
    panel_a.alpha_composite(base_preview, ((tile - base_preview.width) // 2, (tile - base_preview.height) // 2))
    comparison_scale = 540 / base_image.width
    piece_preview = crop.resize((round(composed_size[0] * comparison_scale), round(composed_size[1] * comparison_scale)), Image.Resampling.LANCZOS)
    panel_a.alpha_composite(piece_preview, (tile - piece_preview.width - 28, 60))

    # Panel 2: isolated game-scale piece with its center-of-mass pivot.
    panel_b = checker((tile, tile), 24)
    display = piece.resize((piece.width * 2, piece.height * 2), Image.Resampling.NEAREST)
    origin = ((tile - display.width) // 2, (tile - display.height) // 2)
    panel_b.alpha_composite(display, origin)
    px = origin[0] + composed_pivot[0] * 2
    py = origin[1] + composed_pivot[1] * 2
    draw_b = ImageDraw.Draw(panel_b)
    draw_b.line((px - 12, py, px + 12, py), fill="#e34b46", width=3)
    draw_b.line((px, py - 12, px, py + 12), fill="#e34b46", width=3)

    grid.paste(panel_a.convert("RGB"), (0, header))
    grid.paste(panel_b.convert("RGB"), (tile, header))
    draw = ImageDraw.Draw(grid)
    draw.text((12, 14), "RIM SCALE COMPARISON", font=font, fill="#f3ead3")
    draw.text((tile + 12, 14), "GAME SCALE + CENTER-OF-MASS PIVOT", font=font, fill="#f3ead3")
    review_path = REVIEW / "fortress_ranged__stone_rim_chunk_a_v1_review.png"
    grid.save(review_path, optimize=True)

    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(crop.size),
        "centerOfMassPivotPx": pivot,
        "composedSize": composed_size,
        "magentaSpillVisible": spill,
        "alphaBytes": alpha_path.stat().st_size,
        "under5MB": alpha_path.stat().st_size < 5_000_000,
        "review": str(review_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

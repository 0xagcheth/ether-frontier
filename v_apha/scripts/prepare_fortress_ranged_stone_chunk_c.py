#!/usr/bin/env python3
"""Promote inner-stone debris chunk C and render the A/B/C kit review."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, tight_bbox, center_of_mass, checker


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
SOURCE = CANDIDATES / "fortress_ranged__debris__stone_core_chunk_c_v1_chroma.png"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
NAME = "fortress_ranged__debris__stone_core_chunk_c_v1"
SCALE_TO_BASE = 0.095


def main() -> None:
    full = chroma_to_alpha(Image.open(SOURCE).convert("RGBA"))
    full.save(CANDIDATES / f"{NAME}_alpha_full.png", optimize=True)
    crop = full.crop(tight_bbox(full))
    pivot = center_of_mass(crop)
    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    base = json.loads(BASE_META.read_text())
    width = round(base["footprintPx"] * SCALE_TO_BASE)
    game_size = [width, round(crop.height * width / crop.width)]
    visible = [p for p in crop.getdata() if p[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 180 and b > 160 and g < 105 and min(r-g, b-g) > 90)
    manifest = {
        "schemaVersion": 1,
        "module": "fortress_ranged__debris__stone_core_chunk_c",
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
            "massClass": "small",
            "radialVelocityPxPerSec": [135, 225],
            "angularVelocityDegPerSec": [-340, 340],
            "linearDrag": 0.9,
            "lifetimeMs": [550, 950],
        },
        "drawOrder": 62,
        "qa": {"transparent": True, "tightRect": True, "singleConnectedPiece": True,
               "magentaSpillPixels": spill, "status": "canon"},
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    ids = [
        "fortress_ranged__debris__stone_rim_chunk_a_v1",
        "fortress_ranged__debris__stone_rim_chunk_b_v1",
        NAME,
    ]
    tile, header = 420, 52
    grid = Image.new("RGB", (tile * 3, tile + header), "#292a2b")
    font = ImageFont.load_default()
    sizes = []
    for index, asset_id in enumerate(ids):
        image = Image.open(CANON / f"{asset_id}_alpha.png").convert("RGBA")
        meta = json.loads((CANON / f"{asset_id}.json").read_text())
        game_w = round(base["footprintPx"] * meta["runtimeScale"]["scaleToBaseFootprint"])
        size = [game_w, round(image.height * game_w / image.width)]
        sizes.append(size)
        display = image.resize((size[0] * 2, size[1] * 2), Image.Resampling.LANCZOS)
        panel = checker((tile, tile), 21)
        origin = ((tile - display.width) // 2, (tile - display.height) // 2)
        panel.alpha_composite(display, origin)
        px = origin[0] + round(meta["pivot"][0] * display.width)
        py = origin[1] + round(meta["pivot"][1] * display.height)
        draw_panel = ImageDraw.Draw(panel)
        draw_panel.line((px - 10, py, px + 10, py), fill="#e34b46", width=3)
        draw_panel.line((px, py - 10, px, py + 10), fill="#e34b46", width=3)
        grid.paste(panel.convert("RGB"), (index * tile, header))
    draw = ImageDraw.Draw(grid)
    for i, (label, size) in enumerate(zip(("CHUNK A", "CHUNK B", "CHUNK C"), sizes)):
        draw.text((i * tile + 14, 18), f"{label}  {size[0]} x {size[1]} px", font=font, fill="#f3ead3")
    review_path = REVIEW / "fortress_ranged__stone_debris_a_b_c_v1_review.png"
    grid.save(review_path, optimize=True)

    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)), "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(crop.size), "centerOfMassPivotPx": pivot, "composedSize": game_size,
        "magentaSpillVisible": spill, "alphaBytes": alpha_path.stat().st_size,
        "under5MB": alpha_path.stat().st_size < 5_000_000,
        "review": str(review_path.relative_to(ROOT)), "kitSizes": sizes,
    }, indent=2))


if __name__ == "__main__":
    main()

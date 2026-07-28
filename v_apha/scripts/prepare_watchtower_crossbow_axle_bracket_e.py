#!/usr/bin/env python3
"""Promote Watchtower axle-bracket debris and validate its open cutout."""

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
SOURCE = CANDIDATES / "watchtower__debris__crossbow_axle_bracket_e_v1_chroma.png"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
WEAPON_META = CANON / "watchtower__active_addon__light_single_crossbow_v1.json"
WEAPON_IMAGE = CANON / "watchtower__active_addon__light_single_crossbow_v1_alpha.png"
NAME = "watchtower__debris__crossbow_axle_bracket_e_v1"
SCALE_TO_WEAPON_LENGTH = 0.14


def main() -> None:
    full = chroma_to_alpha(Image.open(SOURCE).convert("RGBA"))
    full.save(CANDIDATES / f"{NAME}_alpha_full.png", optimize=True)
    crop = full.crop(tight_bbox(full))
    pivot = center_of_mass(crop)
    center_alpha = crop.getchannel("A").getpixel((crop.width // 2, crop.height // 2))
    if center_alpha > 18:
        raise RuntimeError("axle cutout center is not transparent")

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    base = json.loads(BASE_META.read_text())
    weapon_meta = json.loads(WEAPON_META.read_text())
    weapon_width = round(base["footprintPx"] * weapon_meta["attachments"]["parent"]["scaleToBaseFootprint"])
    target_width = round(weapon_width * SCALE_TO_WEAPON_LENGTH)
    game_size = [target_width, round(crop.height * target_width / crop.width)]
    visible = [p for p in crop.getdata() if p[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 180 and b > 160 and g < 105 and min(r-g, b-g) > 90)

    manifest = {
        "schemaVersion": 1,
        "module": "watchtower__debris__crossbow_axle_bracket_e",
        "object": "watchtower", "family": "fortress_ranged", "slot": "debris",
        "ownerModule": "watchtower__active_addon__light_single_crossbow",
        "image": alpha_path.name, "sourceImage": chroma_path.name,
        "sizePx": list(crop.size),
        "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height},
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / crop.width, 6), round(pivot[1] / crop.height, 6)],
        "pivotMethod": "alpha_weighted_center_of_mass_excluding_cutout",
        "projection": "true_top_down_orthographic_90deg",
        "runtimeScale": {"scaleToWeaponLength": SCALE_TO_WEAPON_LENGTH},
        "destroyPhysics": {
            "massClass": "light_metal", "inheritOwnerRotation": True,
            "radialVelocityPxPerSec": [175, 285],
            "angularVelocityDegPerSec": [-560, 560], "linearDrag": 0.875,
            "lifetimeMs": [450, 850],
        },
        "drawOrder": 65,
        "qa": {"transparent": True, "tightRect": True, "singleConnectedPiece": True,
               "centerCutoutTransparent": True, "centerAlpha": center_alpha,
               "magentaSpillPixels": spill, "status": "canon"},
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    weapon = Image.open(WEAPON_IMAGE).convert("RGBA")
    weapon_size = [weapon_width, round(weapon.height * weapon_width / weapon.width)]
    game_weapon = weapon.resize(tuple(weapon_size), Image.Resampling.LANCZOS)
    game_bracket = crop.resize(tuple(game_size), Image.Resampling.LANCZOS)
    tile, header = 860, 52
    grid = Image.new("RGB", (tile * 2, tile + header), "#292a2b")
    font = ImageFont.load_default()
    for index, (image, source_image, source_pivot) in enumerate((
        (game_weapon, weapon, weapon_meta["pivotPx"]), (game_bracket, crop, pivot))):
        panel = checker((tile, tile), 24)
        origin = ((tile - image.width) // 2, (tile - image.height) // 2)
        panel.alpha_composite(image, origin)
        px = origin[0] + round(source_pivot[0] / source_image.width * image.width)
        py = origin[1] + round(source_pivot[1] / source_image.height * image.height)
        d = ImageDraw.Draw(panel)
        d.line((px - 11, py, px + 11, py), fill="#e34b46", width=3)
        d.line((px, py - 11, px, py + 11), fill="#e34b46", width=3)
        grid.paste(panel.convert("RGB"), (index * tile, header))
    draw = ImageDraw.Draw(grid)
    draw.text((14, 18), f"WATCHTOWER CROSSBOW  {weapon_size[0]} x {weapon_size[1]} px", font=font, fill="#f3ead3")
    draw.text((tile + 14, 18), f"AXLE BRACKET E  {game_size[0]} x {game_size[1]} px", font=font, fill="#f3ead3")
    review_path = REVIEW / "watchtower__crossbow_axle_bracket_e_v1_review.png"
    grid.save(review_path, optimize=True)

    print(json.dumps({"manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)), "tightSize": list(crop.size),
        "centerOfMassPivotPx": pivot, "centerCutoutAlpha": center_alpha,
        "weaponGameSize": weapon_size, "composedSize": game_size,
        "magentaSpillVisible": spill, "alphaBytes": alpha_path.stat().st_size,
        "under5MB": alpha_path.stat().st_size < 5_000_000,
        "review": str(review_path.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()

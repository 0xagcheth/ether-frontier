#!/usr/bin/env python3
"""Promote Ranger's detachable bolt magazine and validate weapon assembly."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
NAME = "ranger__ammo_child__bolt_magazine_v1"
CANDIDATES = ROOT / "assets/staging/candidates/modules/ranger"
SOURCE = CANDIDATES / f"{NAME}_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/ranger"
REVIEW = ROOT / "assets/staging/reviews/modules/ranger"
WEAPON_META = CANON / "ranger__active_primary__rapid_crossbow_v1.json"
WEAPON_IMAGE = CANON / "ranger__active_primary__rapid_crossbow_v1_alpha.png"
WIDTH_TO_WEAPON = 0.18


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    full = chroma_to_alpha(Image.open(SOURCE).convert("RGBA"))
    full_path = CANDIDATES / f"{NAME}_alpha_full.png"
    full.save(full_path, optimize=True)
    bounds = full.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bounds:
        raise RuntimeError("empty bolt-magazine cutout")
    crop = full.crop(bounds)
    pivot = [crop.width // 2, crop.height // 2]

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    weapon_meta = json.loads(WEAPON_META.read_text())
    weapon = Image.open(WEAPON_IMAGE).convert("RGBA")
    target_width = round(weapon.width * WIDTH_TO_WEAPON)
    scale = target_width / crop.width
    game_size = [target_width, round(crop.height * scale)]
    game_pivot = [round(pivot[0] * scale), round(pivot[1] * scale)]
    visible = [p for p in crop.getdata() if p[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 160 and b > 140 and g < 115 and min(r-g, b-g) > 65)

    manifest = {
        "schemaVersion": 1,
        "module": "ranger__ammo_child__bolt_magazine",
        "object": "ranger",
        "family": "fortress_ranged",
        "slot": "ammo_child",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(crop.size),
        "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height},
        "pivotPx": pivot,
        "pivot": [0.5, 0.5],
        "pivotMethod": "central_axle_lock",
        "projection": "true_top_down_orthographic_90deg",
        "forwardAxis": "+X",
        "runtimeScale": {"widthToParentWeapon": WIDTH_TO_WEAPON},
        "attachments": {
            "parent": {
                "module": "ranger__active_primary__rapid_crossbow",
                "anchor": "magazine_socket",
                "inheritRotation": True,
                "localRotationDeg": 90,
            }
        },
        "drawOrder": 31,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "centerOpeningPreserved": crop.getpixel(tuple(pivot))[3] == 0,
            "magentaSpillPixels": spill,
            "alphaBytes": alpha_path.stat().st_size,
            "under5MB": alpha_path.stat().st_size < 5_000_000,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    weapon_target_w = 714
    weapon_target_h = round(weapon.height * weapon_target_w / weapon.width)
    weapon_game = weapon.resize((weapon_target_w, weapon_target_h), Image.Resampling.LANCZOS)
    weapon_pivot = [round(weapon_meta["pivotPx"][0] * weapon_target_w / weapon.width),
                    round(weapon_meta["pivotPx"][1] * weapon_target_h / weapon.height)]
    magazine_target_w = round(weapon_target_w * WIDTH_TO_WEAPON)
    magazine_target_h = round(crop.height * magazine_target_w / crop.width)
    magazine_game = crop.resize((magazine_target_w, magazine_target_h), Image.Resampling.LANCZOS)
    magazine_game = magazine_game.rotate(-90, expand=True, resample=Image.Resampling.BICUBIC)
    magazine_pivot = [magazine_game.width // 2, magazine_game.height // 2]

    canvas_size = (920, 760)
    center = (canvas_size[0] // 2, canvas_size[1] // 2)
    weapon_layer = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    weapon_layer.alpha_composite(weapon_game, (center[0]-weapon_pivot[0], center[1]-weapon_pivot[1]))
    magazine_layer = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    socket_source = weapon_meta["attachments"]["magazine_socket"]["positionPx"]
    socket_preview = [center[0] + round((socket_source[0]-weapon_meta["pivotPx"][0]) * weapon_target_w / weapon.width),
                      center[1] + round((socket_source[1]-weapon_meta["pivotPx"][1]) * weapon_target_h / weapon.height)]
    magazine_layer.alpha_composite(magazine_game, (socket_preview[0]-magazine_pivot[0], socket_preview[1]-magazine_pivot[1]))

    panel = checker(canvas_size, 24)
    panel.alpha_composite(weapon_layer)
    panel.alpha_composite(magazine_layer)
    composite_path = REVIEW / f"{NAME}_rapid_crossbow_composite.png"
    panel.save(composite_path, optimize=True)

    tile, header = 620, 42
    grid = Image.new("RGB", (tile * 2, (tile + header) * 2), "#292a2b")
    font = ImageFont.load_default()
    for index, angle in enumerate((0, 90, 180, 270)):
        scene = checker(canvas_size, 24)
        scene.alpha_composite(weapon_layer.rotate(-angle, Image.Resampling.BICUBIC, center=center))
        scene.alpha_composite(magazine_layer.rotate(-angle, Image.Resampling.BICUBIC, center=center))
        thumb = scene.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        col, row = index % 2, index // 2
        y = row * (tile + header)
        grid.paste(thumb, (col*tile, y+header))
        ImageDraw.Draw(grid).text((col*tile+12, y+14), f"ASSEMBLED {angle:03d} DEG — MAGAZINE ORDER 31", font=font, fill="#f3ead3")
    review_path = REVIEW / f"{NAME}_assembly_rotation_grid.png"
    grid.save(review_path, optimize=True)

    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)), "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(crop.size), "pivotPx": pivot, "centerOpeningPreserved": manifest["qa"]["centerOpeningPreserved"],
        "gameSizeRelativeToCanonicalWeapon": game_size, "previewSize": [magazine_target_w, magazine_target_h],
        "drawOrder": 31, "localRotationDeg": 90, "socketPreviewPx": socket_preview,
        "magentaSpillVisible": spill, "alphaBytes": alpha_path.stat().st_size,
        "composite": str(composite_path.relative_to(ROOT)), "rotationGrid": str(review_path.relative_to(ROOT))
    }, indent=2))


if __name__ == "__main__":
    main()

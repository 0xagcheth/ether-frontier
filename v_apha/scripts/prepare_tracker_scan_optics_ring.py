#!/usr/bin/env python3
"""Promote Tracker scan ring and validate its independent rotation."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
NAME = "tracker__aim_child__scan_optics_ring_v1"
CANDIDATES = ROOT / "assets/staging/candidates/modules/tracker"
SOURCE = CANDIDATES / f"{NAME}_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/tracker"
REVIEW = ROOT / "assets/staging/reviews/modules/tracker"
WEAPON_META = CANON / "tracker__active_primary__long_range_crossbow_v1.json"
WEAPON_IMAGE = CANON / "tracker__active_primary__long_range_crossbow_v1_alpha.png"
WIDTH_TO_WEAPON = 0.25


def make_layer(size, image, pivot, point):
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.alpha_composite(image, (point[0] - pivot[0], point[1] - pivot[1]))
    return out


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    full = chroma_to_alpha(Image.open(SOURCE).convert("RGBA"))
    full.save(CANDIDATES / f"{NAME}_alpha_full.png", optimize=True)
    bounds = full.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bounds:
        raise RuntimeError("empty Tracker scan-ring cutout")
    crop = full.crop(bounds)
    pivot = [crop.width // 2, crop.height // 2]
    center_alpha = crop.getchannel("A").getpixel(tuple(pivot))
    if center_alpha > 18:
        raise RuntimeError(f"scan-ring center is not open: alpha={center_alpha}")

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)
    spill = sum(1 for r, g, b, a in crop.getdata()
                if a > 18 and r > 150 and b > 135 and g < 120 and min(r-g, b-g) > 60)
    weapon_meta = json.loads(WEAPON_META.read_text())
    target_width = round(weapon_meta["sizePx"][0] * WIDTH_TO_WEAPON)
    game_size = [target_width, round(crop.height * target_width / crop.width)]
    manifest = {
        "schemaVersion": 1,
        "module": "tracker__aim_child__scan_optics_ring",
        "object": "tracker",
        "family": "fortress_ranged",
        "slot": "aim_child",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(crop.size),
        "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height},
        "pivotPx": pivot,
        "pivot": [0.5, 0.5],
        "projection": "true_top_down_orthographic_90deg",
        "runtimeScale": {"widthToParentWeapon": WIDTH_TO_WEAPON},
        "attachments": {"parent": {"module": "tracker__active_primary__long_range_crossbow", "anchor": "scan_ring_socket", "inheritRotation": True, "rotation": "aimAngle + scanAngle"}},
        "animation": {"id": "scan", "type": "continuous_rotation", "degreesPerSecond": 42, "loop": True},
        "drawOrder": 32,
        "qa": {"transparent": True, "tightRect": True, "openCenter": center_alpha <= 18,
               "centerAlpha": center_alpha, "magentaSpillPixels": spill,
               "alphaBytes": alpha_path.stat().st_size, "under5MB": alpha_path.stat().st_size < 5_000_000,
               "status": "canon"},
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    canvas_size = (1120, 920)
    center = (canvas_size[0] // 2, canvas_size[1] // 2)
    weapon = Image.open(WEAPON_IMAGE).convert("RGBA")
    weapon_w = 844
    weapon_h = round(weapon.height * weapon_w / weapon.width)
    weapon_game = weapon.resize((weapon_w, weapon_h), Image.Resampling.LANCZOS)
    wp = [round(weapon_meta["pivotPx"][0] * weapon_w / weapon.width), round(weapon_meta["pivotPx"][1] * weapon_h / weapon.height)]
    weapon_layer = make_layer(canvas_size, weapon_game, wp, center)
    ring_w = round(weapon_w * WIDTH_TO_WEAPON)
    ring_h = round(crop.height * ring_w / crop.width)
    ring = crop.resize((ring_w, ring_h), Image.Resampling.LANCZOS)
    ring_layer = make_layer(canvas_size, ring, [ring.width // 2, ring.height // 2], center)

    tile, header = 560, 42
    grid = Image.new("RGB", (tile * 2, (tile + header) * 2), "#292a2b")
    font = ImageFont.load_default()
    for i, scan_angle in enumerate((0, 22.5, 45, 67.5)):
        scene = checker(canvas_size, 24)
        scene.alpha_composite(weapon_layer.rotate(18, Image.Resampling.BICUBIC, center=center))
        rotated_ring = ring_layer.rotate(18 - scan_angle, Image.Resampling.BICUBIC, center=center)
        scene.alpha_composite(rotated_ring)
        thumb = scene.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        col, row = i % 2, i // 2
        y = row * (tile + header)
        grid.paste(thumb, (col * tile, y + header))
        ImageDraw.Draw(grid).text((col * tile + 12, y + 14), f"AIM -18 DEG / LOCAL SCAN {scan_angle:04.1f} DEG", font=font, fill="#f3ead3")
    review_path = REVIEW / f"{NAME}_independent_rotation_grid.png"
    grid.save(review_path, optimize=True)
    composite = checker(canvas_size, 24)
    composite.alpha_composite(weapon_layer)
    composite.alpha_composite(ring_layer)
    composite_path = REVIEW / f"{NAME}_weapon_composite.png"
    composite.save(composite_path, optimize=True)
    print(json.dumps({"manifest": str(manifest_path.relative_to(ROOT)), "alpha": str(alpha_path.relative_to(ROOT)),
                      "tightSize": list(crop.size), "pivotPx": pivot, "centerAlpha": center_alpha,
                      "composedSize": game_size, "previewSize": [ring_w, ring_h],
                      "magentaSpillVisible": spill, "alphaBytes": alpha_path.stat().st_size,
                      "composite": str(composite_path.relative_to(ROOT)),
                      "rotationGrid": str(review_path.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()

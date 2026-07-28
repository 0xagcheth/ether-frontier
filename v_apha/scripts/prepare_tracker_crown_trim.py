#!/usr/bin/env python3
"""Promote Tracker crown trim and audit rotating-group clearance."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
NAME = "tracker__identity_child__crown_trim_v1"
CANDIDATES = ROOT / "assets/staging/candidates/modules/tracker"
SOURCE = CANDIDATES / f"{NAME}_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/tracker"
REVIEW = ROOT / "assets/staging/reviews/modules/tracker"
SHARED = ROOT / "assets/approved/canon/modules/fortress_ranged"
RANGER = ROOT / "assets/approved/canon/modules/ranger"
BASE_META = SHARED / "fortress_ranged__base_token__round_light_v1.json"
CORE = ROOT / "assets/staging/reviews/modules/fortress_ranged/fortress_ranged__base_socket_lantern_housing_v1_composite.png"
WEAPON_META = CANON / "tracker__active_primary__long_range_crossbow_v1.json"
WEAPON_IMAGE = CANON / "tracker__active_primary__long_range_crossbow_v1_alpha.png"
RING_META = CANON / "tracker__aim_child__scan_optics_ring_v1.json"
RING_IMAGE = CANON / "tracker__aim_child__scan_optics_ring_v1_alpha.png"
MAG_META = RANGER / "ranger__ammo_child__bolt_magazine_v1.json"
MAG_IMAGE = RANGER / "ranger__ammo_child__bolt_magazine_v1_alpha.png"
SCALE_TO_BASE = 0.105
POSITION = [0.79, 0.79]


def layer_at(size, image, pivot, point):
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
        raise RuntimeError("empty Tracker crown trim")
    crop = full.crop(bounds)
    pivot = [crop.width // 2, crop.height // 2]
    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)
    base = json.loads(BASE_META.read_text())
    target_w = round(base["footprintPx"] * SCALE_TO_BASE)
    game_size = [target_w, round(crop.height * target_w / crop.width)]
    spill = sum(1 for r, g, b, a in crop.getdata()
                if a > 18 and r > 150 and b > 135 and g < 120 and min(r-g, b-g) > 60)
    manifest = {
        "schemaVersion": 1, "module": "tracker__identity_child__crown_trim", "object": "tracker", "family": "fortress_ranged", "slot": "identity_child",
        "image": alpha_path.name, "sourceImage": chroma_path.name, "sizePx": list(crop.size),
        "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height}, "pivotPx": pivot, "pivot": [0.5, 0.5],
        "projection": "true_top_down_orthographic_90deg", "runtimeScale": {"scaleToBaseFootprint": SCALE_TO_BASE},
        "attachments": {"parent": {"module": "fortress_ranged__base_token__round_light", "anchor": "object_center", "positionNormalized": POSITION, "inheritRotation": False}},
        "drawOrder": 16,
        "qa": {"transparent": True, "tightRect": True, "magentaSpillPixels": spill,
               "alphaBytes": alpha_path.stat().st_size, "under5MB": alpha_path.stat().st_size < 5_000_000, "status": "canon"},
    }
    manifest_path = CANON / f"{NAME}.json"

    core = Image.open(CORE).convert("RGBA")
    center = (core.width // 2, core.height // 2)
    trim = crop.resize(tuple(game_size), Image.Resampling.LANCZOS)
    trim_point = (round(center[0] + (POSITION[0] - 0.5) * base["footprintPx"]),
                  round(center[1] + (POSITION[1] - 0.5) * base["footprintPx"]))
    trim_layer = layer_at(core.size, trim, [trim.width // 2, trim.height // 2], trim_point)
    weapon_meta = json.loads(WEAPON_META.read_text())
    weapon = Image.open(WEAPON_IMAGE).convert("RGBA")
    ww = round(base["footprintPx"] * weapon_meta["runtimeScale"]["scaleToBaseFootprint"])
    wh = round(weapon.height * ww / weapon.width)
    weapon = weapon.resize((ww, wh), Image.Resampling.LANCZOS)
    wp = [round(weapon_meta["pivotPx"][0] * ww / weapon_meta["sizePx"][0]), round(weapon_meta["pivotPx"][1] * wh / weapon_meta["sizePx"][1])]
    weapon_layer = layer_at(core.size, weapon, wp, center)
    ring_meta = json.loads(RING_META.read_text())
    ring = Image.open(RING_IMAGE).convert("RGBA")
    rw = round(ww * ring_meta["runtimeScale"]["widthToParentWeapon"])
    rh = round(ring.height * rw / ring.width)
    ring = ring.resize((rw, rh), Image.Resampling.LANCZOS)
    ring_layer = layer_at(core.size, ring, [ring.width // 2, ring.height // 2], center)
    mag_meta = json.loads(MAG_META.read_text())
    mag = Image.open(MAG_IMAGE).convert("RGBA")
    mw = round(ww * mag_meta["runtimeScale"]["widthToParentWeapon"])
    mh = round(mag.height * mw / mag.width)
    mag = mag.resize((mw, mh), Image.Resampling.LANCZOS).rotate(-90, expand=True, resample=Image.Resampling.BICUBIC)
    ms = weapon_meta["attachments"]["magazine_socket"]["positionPx"]
    mp = (center[0] + round((ms[0] - weapon_meta["pivotPx"][0]) * ww / weapon_meta["sizePx"][0]),
          center[1] + round((ms[1] - weapon_meta["pivotPx"][1]) * wh / weapon_meta["sizePx"][1]))
    mag_layer = layer_at(core.size, mag, [mag.width // 2, mag.height // 2], mp)

    tile, header = 620, 42
    grid = Image.new("RGB", (tile * 2, (tile + header) * 2), "#292a2b")
    font = ImageFont.load_default()
    overlaps = []
    for i, angle in enumerate((0, 90, 180, 270)):
        rotated = [layer.rotate(-angle, Image.Resampling.BICUBIC, center=center) for layer in (weapon_layer, ring_layer, mag_layer)]
        group = ImageChops.lighter(ImageChops.lighter(rotated[0].getchannel("A"), rotated[1].getchannel("A")), rotated[2].getchannel("A"))
        tm = trim_layer.getchannel("A").point(lambda a: 255 if a > 18 else 0)
        gm = group.point(lambda a: 255 if a > 18 else 0)
        overlap = sum(1 for a, b in zip(tm.getdata(), gm.getdata()) if a and b)
        overlaps.append(overlap)
        scene = checker(core.size, 24)
        scene.alpha_composite(core)
        scene.alpha_composite(trim_layer)
        for layer in rotated:
            scene.alpha_composite(layer)
        thumb = scene.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        col, row = i % 2, i // 2
        y = row * (tile + header)
        grid.paste(thumb, (col * tile, y + header))
        ImageDraw.Draw(grid).text((col * tile + 12, y + 14), f"TRACKER {angle:03d} DEG — CROWN OVERLAP {overlap} PX", font=font, fill="#f3ead3")
    review = REVIEW / f"{NAME}_full_platform_clearance_grid.png"
    grid.save(review, optimize=True)
    manifest["qa"]["weaponOverlapPixelsByAngle"] = dict(zip(("0", "90", "180", "270"), overlaps))
    manifest["qa"]["clearancePass"] = max(overlaps) == 0
    manifest["qa"]["status"] = "canon" if max(overlaps) == 0 else "needs_adjustment"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"manifest": str(manifest_path.relative_to(ROOT)), "alpha": str(alpha_path.relative_to(ROOT)),
                      "tightSize": list(crop.size), "pivotPx": pivot, "composedSize": game_size,
                      "positionNormalized": POSITION, "overlapPixels": overlaps,
                      "clearancePass": max(overlaps) == 0, "magentaSpillVisible": spill,
                      "alphaBytes": alpha_path.stat().st_size, "reviewGrid": str(review.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()

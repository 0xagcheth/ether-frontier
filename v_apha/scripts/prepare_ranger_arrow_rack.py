#!/usr/bin/env python3
"""Promote Ranger's empty arrow rack and validate platform clearance."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
NAME = "ranger__utility_child__arrow_rack_v1"
CANDIDATES = ROOT / "assets/staging/candidates/modules/ranger"
SOURCE = CANDIDATES / f"{NAME}_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/ranger"
REVIEW = ROOT / "assets/staging/reviews/modules/ranger"
SHARED = ROOT / "assets/approved/canon/modules/fortress_ranged"
BASE_META = SHARED / "fortress_ranged__base_token__round_light_v1.json"
CORE = ROOT / "assets/staging/reviews/modules/fortress_ranged/fortress_ranged__base_socket_lantern_housing_v1_composite.png"
WEAPON_META = CANON / "ranger__active_primary__rapid_crossbow_v1.json"
WEAPON_IMAGE = CANON / "ranger__active_primary__rapid_crossbow_v1_alpha.png"
MAG_META = CANON / "ranger__ammo_child__bolt_magazine_v1.json"
MAG_IMAGE = CANON / "ranger__ammo_child__bolt_magazine_v1_alpha.png"
SCALE_TO_BASE = 0.19
POSITION = [0.5, 0.12]


def layer_at(canvas_size, image, pivot, point):
    layer = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    layer.alpha_composite(image, (point[0]-pivot[0], point[1]-pivot[1]))
    return layer


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    full = chroma_to_alpha(Image.open(SOURCE).convert("RGBA"))
    full.save(CANDIDATES / f"{NAME}_alpha_full.png", optimize=True)
    bounds = full.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bounds:
        raise RuntimeError("empty arrow-rack cutout")
    crop = full.crop(bounds)
    pivot = [crop.width // 2, crop.height // 2]
    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    base = json.loads(BASE_META.read_text())
    target_width = round(base["footprintPx"] * SCALE_TO_BASE)
    game_size = [target_width, round(crop.height * target_width / crop.width)]
    spill = sum(1 for r,g,b,a in crop.getdata() if a > 18 and r > 160 and b > 140 and g < 115 and min(r-g,b-g) > 65)
    manifest = {
        "schemaVersion": 1, "module": "ranger__utility_child__arrow_rack", "object": "ranger",
        "family": "fortress_ranged", "slot": "utility_child", "image": alpha_path.name,
        "sourceImage": chroma_path.name, "sizePx": list(crop.size),
        "rect": {"x":0,"y":0,"w":crop.width,"h":crop.height}, "pivotPx": pivot, "pivot":[0.5,0.5],
        "projection": "true_top_down_orthographic_90deg",
        "runtimeScale": {"scaleToBaseFootprint": SCALE_TO_BASE},
        "attachments": {"parent": {"module":"fortress_ranged__base_token__round_light", "anchor":"object_center",
                                    "positionNormalized": POSITION, "inheritRotation": False}},
        "drawOrder": 15,
        "qa": {"transparent":True,"tightRect":True,"emptySlots":5,"magentaSpillPixels":spill,
               "alphaBytes":alpha_path.stat().st_size,"under5MB":alpha_path.stat().st_size < 5_000_000,"status":"canon"}
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")

    core = Image.open(CORE).convert("RGBA")
    center = (core.width//2, core.height//2)
    rack = crop.resize(tuple(game_size), Image.Resampling.LANCZOS)
    rack_point = (round(core.width*POSITION[0]), round(core.height*POSITION[1]))
    rack_layer = layer_at(core.size, rack, [rack.width//2,rack.height//2], rack_point)

    weapon_meta = json.loads(WEAPON_META.read_text())
    weapon = Image.open(WEAPON_IMAGE).convert("RGBA")
    weapon_w = round(base["footprintPx"] * weapon_meta["runtimeScale"]["scaleToBaseFootprint"])
    weapon_h = round(weapon.height * weapon_w / weapon.width)
    weapon = weapon.resize((weapon_w,weapon_h), Image.Resampling.LANCZOS)
    wp = [round(weapon_meta["pivotPx"][0]*weapon_w/weapon_meta["sizePx"][0]),
          round(weapon_meta["pivotPx"][1]*weapon_h/weapon_meta["sizePx"][1])]
    weapon_layer = layer_at(core.size, weapon, wp, center)

    mag_meta = json.loads(MAG_META.read_text())
    mag = Image.open(MAG_IMAGE).convert("RGBA")
    mag_w = round(weapon_w * mag_meta["runtimeScale"]["widthToParentWeapon"])
    mag_h = round(mag.height * mag_w / mag.width)
    mag = mag.resize((mag_w,mag_h), Image.Resampling.LANCZOS).rotate(-90,expand=True,resample=Image.Resampling.BICUBIC)
    socket = weapon_meta["attachments"]["magazine_socket"]["positionPx"]
    socket_point = (center[0]+round((socket[0]-weapon_meta["pivotPx"][0])*weapon_w/weapon_meta["sizePx"][0]),
                    center[1]+round((socket[1]-weapon_meta["pivotPx"][1])*weapon_h/weapon_meta["sizePx"][1]))
    mag_layer = layer_at(core.size, mag, [mag.width//2,mag.height//2], socket_point)

    tile, header = 620, 42
    grid = Image.new("RGB",(tile*2,(tile+header)*2),"#292a2b")
    font = ImageFont.load_default()
    overlap_counts = []
    for index,angle in enumerate((0,90,180,270)):
        scene = checker(core.size,24); scene.alpha_composite(core); scene.alpha_composite(rack_layer)
        rotated_weapon = weapon_layer.rotate(-angle,Image.Resampling.BICUBIC,center=center)
        rotated_mag = mag_layer.rotate(-angle,Image.Resampling.BICUBIC,center=center)
        group_alpha = ImageChops.lighter(rotated_weapon.getchannel("A"), rotated_mag.getchannel("A"))
        rack_mask = rack_layer.getchannel("A").point(lambda a:255 if a>18 else 0)
        group_mask = group_alpha.point(lambda a:255 if a>18 else 0)
        overlap = sum(1 for a,b in zip(rack_mask.getdata(),group_mask.getdata()) if a and b)
        overlap_counts.append(overlap)
        scene.alpha_composite(rotated_weapon); scene.alpha_composite(rotated_mag)
        thumb=scene.convert("RGB").resize((tile,tile),Image.Resampling.LANCZOS)
        col,row=index%2,index//2;y=row*(tile+header);grid.paste(thumb,(col*tile,y+header))
        ImageDraw.Draw(grid).text((col*tile+12,y+14),f"ROTATION {angle:03d} DEG — OVERLAP {overlap} PX",font=font,fill="#f3ead3")
    review_path=REVIEW/f"{NAME}_platform_clearance_grid.png";grid.save(review_path,optimize=True)
    manifest["qa"]["weaponOverlapPixelsByAngle"] = dict(zip(("0","90","180","270"),overlap_counts))
    manifest["qa"]["clearancePass"] = max(overlap_counts)==0
    manifest["qa"]["status"] = "canon" if max(overlap_counts)==0 else "needs_adjustment"
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"manifest":str(manifest_path.relative_to(ROOT)),"alpha":str(alpha_path.relative_to(ROOT)),
                      "tightSize":list(crop.size),"pivotPx":pivot,"composedSize":game_size,
                      "positionNormalized":POSITION,"overlapPixels":overlap_counts,"clearancePass":max(overlap_counts)==0,
                      "magentaSpillVisible":spill,"alphaBytes":alpha_path.stat().st_size,
                      "reviewGrid":str(review_path.relative_to(ROOT))},indent=2))


if __name__ == "__main__": main()

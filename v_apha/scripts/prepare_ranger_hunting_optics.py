#!/usr/bin/env python3
"""Promote Ranger hunting optics and validate the complete rotating group."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
NAME = "ranger__aim_child__hunting_optics_v1"
CANDIDATES = ROOT / "assets/staging/candidates/modules/ranger"
SOURCE = CANDIDATES / f"{NAME}_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/ranger"
REVIEW = ROOT / "assets/staging/reviews/modules/ranger"
WEAPON_META = CANON / "ranger__active_primary__rapid_crossbow_v1.json"
WEAPON_IMAGE = CANON / "ranger__active_primary__rapid_crossbow_v1_alpha.png"
MAG_META = CANON / "ranger__ammo_child__bolt_magazine_v1.json"
MAG_IMAGE = CANON / "ranger__ammo_child__bolt_magazine_v1_alpha.png"
WIDTH_TO_WEAPON = 0.27


def make_layer(size, image, pivot, point):
    out = Image.new("RGBA", size, (0,0,0,0))
    out.alpha_composite(image, (point[0]-pivot[0], point[1]-pivot[1]))
    return out


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True); REVIEW.mkdir(parents=True, exist_ok=True)
    full = chroma_to_alpha(Image.open(SOURCE).convert("RGBA"))
    full.save(CANDIDATES/f"{NAME}_alpha_full.png", optimize=True)
    bounds = full.getchannel("A").point(lambda a:255 if a>18 else 0).getbbox()
    if not bounds: raise RuntimeError("empty hunting-optics cutout")
    crop = full.crop(bounds); pivot = [crop.width//2,crop.height//2]
    alpha_path=CANON/f"{NAME}_alpha.png"; chroma_path=CANON/f"{NAME}_chroma.png"
    crop.save(alpha_path,optimize=True); shutil.copy2(SOURCE,chroma_path)
    spill=sum(1 for r,g,b,a in crop.getdata() if a>18 and r>160 and b>140 and g<115 and min(r-g,b-g)>65)

    weapon_meta=json.loads(WEAPON_META.read_text())
    target_width=round(weapon_meta["sizePx"][0]*WIDTH_TO_WEAPON)
    game_size=[target_width,round(crop.height*target_width/crop.width)]
    manifest={
      "schemaVersion":1,"module":"ranger__aim_child__hunting_optics","object":"ranger","family":"fortress_ranged",
      "slot":"aim_child","image":alpha_path.name,"sourceImage":chroma_path.name,"sizePx":list(crop.size),
      "rect":{"x":0,"y":0,"w":crop.width,"h":crop.height},"pivotPx":pivot,"pivot":[0.5,0.5],
      "projection":"true_top_down_orthographic_90deg","forwardAxis":"+X",
      "runtimeScale":{"widthToParentWeapon":WIDTH_TO_WEAPON},
      "attachments":{"parent":{"module":"ranger__active_primary__rapid_crossbow","anchor":"optics_socket","inheritRotation":True,"localRotationDeg":0}},
      "drawOrder":32,
      "qa":{"transparent":True,"tightRect":True,"magentaSpillPixels":spill,"alphaBytes":alpha_path.stat().st_size,
            "under5MB":alpha_path.stat().st_size<5_000_000,"status":"canon"}}
    manifest_path=CANON/f"{NAME}.json";manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")

    canvas_size=(920,760);center=(canvas_size[0]//2,canvas_size[1]//2)
    weapon=Image.open(WEAPON_IMAGE).convert("RGBA"); weapon_w=714; weapon_h=round(weapon.height*weapon_w/weapon.width)
    weapon_game=weapon.resize((weapon_w,weapon_h),Image.Resampling.LANCZOS)
    wp=[round(weapon_meta["pivotPx"][0]*weapon_w/weapon.width),round(weapon_meta["pivotPx"][1]*weapon_h/weapon.height)]
    weapon_layer=make_layer(canvas_size,weapon_game,wp,center)

    mag_meta=json.loads(MAG_META.read_text());mag=Image.open(MAG_IMAGE).convert("RGBA")
    mag_w=round(weapon_w*mag_meta["runtimeScale"]["widthToParentWeapon"]);mag_h=round(mag.height*mag_w/mag.width)
    mag=mag.resize((mag_w,mag_h),Image.Resampling.LANCZOS).rotate(-90,expand=True,resample=Image.Resampling.BICUBIC)
    ms=weapon_meta["attachments"]["magazine_socket"]["positionPx"]
    mp=(center[0]+round((ms[0]-weapon_meta["pivotPx"][0])*weapon_w/weapon.width),center[1]+round((ms[1]-weapon_meta["pivotPx"][1])*weapon_h/weapon.height))
    mag_layer=make_layer(canvas_size,mag,[mag.width//2,mag.height//2],mp)

    optic_w=round(weapon_w*WIDTH_TO_WEAPON);optic_h=round(crop.height*optic_w/crop.width)
    optic=crop.resize((optic_w,optic_h),Image.Resampling.LANCZOS)
    os=weapon_meta["attachments"]["optics_socket"]["positionPx"]
    op=(center[0]+round((os[0]-weapon_meta["pivotPx"][0])*weapon_w/weapon.width),center[1]+round((os[1]-weapon_meta["pivotPx"][1])*weapon_h/weapon.height))
    optic_layer=make_layer(canvas_size,optic,[optic.width//2,optic.height//2],op)

    tile,header=620,42;grid=Image.new("RGB",(tile*2,(tile+header)*2),"#292a2b");font=ImageFont.load_default()
    for i,angle in enumerate((0,90,180,270)):
      scene=checker(canvas_size,24)
      for layer in (weapon_layer,mag_layer,optic_layer): scene.alpha_composite(layer.rotate(-angle,Image.Resampling.BICUBIC,center=center))
      thumb=scene.convert("RGB").resize((tile,tile),Image.Resampling.LANCZOS);col,row=i%2,i//2;y=row*(tile+header)
      grid.paste(thumb,(col*tile,y+header));ImageDraw.Draw(grid).text((col*tile+12,y+14),f"ROTATING GROUP {angle:03d} DEG",font=font,fill="#f3ead3")
    review_path=REVIEW/f"{NAME}_weapon_rotation_grid.png";grid.save(review_path,optimize=True)
    composite=checker(canvas_size,24);composite.alpha_composite(weapon_layer);composite.alpha_composite(mag_layer);composite.alpha_composite(optic_layer)
    composite_path=REVIEW/f"{NAME}_weapon_composite.png";composite.save(composite_path,optimize=True)
    print(json.dumps({"manifest":str(manifest_path.relative_to(ROOT)),"alpha":str(alpha_path.relative_to(ROOT)),
      "tightSize":list(crop.size),"pivotPx":pivot,"composedSize":game_size,"previewSize":[optic_w,optic_h],
      "opticsSocketPreviewPx":op,"drawOrder":32,"magentaSpillVisible":spill,"alphaBytes":alpha_path.stat().st_size,
      "composite":str(composite_path.relative_to(ROOT)),"rotationGrid":str(review_path.relative_to(ROOT))},indent=2))


if __name__=="__main__":main()

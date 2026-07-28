#!/usr/bin/env python3
"""Promote Ranger's barbed bolt and validate muzzle spawn and trajectory."""

from __future__ import annotations

import json
import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT=Path(__file__).resolve().parents[1]
NAME="ranger__projectile__barbed_bolt_v1"
CANDIDATES=ROOT/"assets/staging/candidates/modules/ranger";SOURCE=CANDIDATES/f"{NAME}_chroma.png"
CANON=ROOT/"assets/approved/canon/modules/ranger";REVIEW=ROOT/"assets/staging/reviews/modules/ranger"
WEAPON_META=CANON/"ranger__active_primary__rapid_crossbow_v1.json";WEAPON_IMAGE=CANON/"ranger__active_primary__rapid_crossbow_v1_alpha.png"
SCALE_TO_WEAPON=.23

def layer_at(size,image,anchor,point):
 out=Image.new("RGBA",size,(0,0,0,0));out.alpha_composite(image,(point[0]-anchor[0],point[1]-anchor[1]));return out

def rotate_point(point,center,degrees):
 a=math.radians(degrees);x,y=point[0]-center[0],point[1]-center[1];return (center[0]+x*math.cos(a)-y*math.sin(a),center[1]+x*math.sin(a)+y*math.cos(a))

def main():
 CANON.mkdir(parents=True,exist_ok=True);REVIEW.mkdir(parents=True,exist_ok=True)
 full=chroma_to_alpha(Image.open(SOURCE).convert("RGBA"));full.save(CANDIDATES/f"{NAME}_alpha_full.png",optimize=True)
 bounds=full.getchannel("A").point(lambda a:255 if a>18 else 0).getbbox()
 if not bounds:raise RuntimeError("empty Ranger bolt")
 crop=full.crop(bounds);pivot=[crop.width//2,crop.height//2];tail=[0,pivot[1]];tip=[crop.width-1,pivot[1]]
 alpha_path=CANON/f"{NAME}_alpha.png";chroma_path=CANON/f"{NAME}_chroma.png";crop.save(alpha_path,optimize=True);shutil.copy2(SOURCE,chroma_path)
 weapon_meta=json.loads(WEAPON_META.read_text());target_w=round(weapon_meta["sizePx"][0]*SCALE_TO_WEAPON);game_size=[target_w,round(crop.height*target_w/crop.width)]
 spill=sum(1 for r,g,b,a in crop.getdata() if a>18 and r>160 and b>140 and g<115 and min(r-g,b-g)>65)
 manifest={"schemaVersion":1,"module":"ranger__projectile__barbed_bolt","object":"ranger","family":"fortress_ranged","slot":"projectile",
  "image":alpha_path.name,"sourceImage":chroma_path.name,"sizePx":list(crop.size),"rect":{"x":0,"y":0,"w":crop.width,"h":crop.height},
  "pivotPx":pivot,"pivot":[.5,.5],"projection":"true_top_down_orthographic_90deg","forwardAxis":"+X",
  "anchors":{"spawn_tail":{"positionPx":tail,"positionNormalized":[0,round(tail[1]/crop.height,6)]},"impact_tip":{"positionPx":tip,"positionNormalized":[1,round(tip[1]/crop.height,6)]}},
  "attachments":{"spawnFrom":{"module":"ranger__active_primary__rapid_crossbow","anchor":"muzzle_anchor","attachChildAnchor":"spawn_tail","inheritRotation":True}},
  "runtimeScale":{"lengthToParentWeapon":SCALE_TO_WEAPON},"runtimeTransform":{"translation":"projectilePosition","rotation":"trajectoryAngle"},"drawOrder":40,
  "qa":{"transparent":True,"tightRect":True,"straightAxis":True,"magentaSpillPixels":spill,"alphaBytes":alpha_path.stat().st_size,"under5MB":alpha_path.stat().st_size<5_000_000,"status":"canon"}}
 manifest_path=CANON/f"{NAME}.json";manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")

 canvas_size=(980,720);center=(340,360);weapon=Image.open(WEAPON_IMAGE).convert("RGBA");ww=600;wh=round(weapon.height*ww/weapon.width);weapon=weapon.resize((ww,wh),Image.Resampling.LANCZOS);wp=[round(weapon_meta["pivotPx"][0]*ww/weapon_meta["sizePx"][0]),round(weapon_meta["pivotPx"][1]*wh/weapon_meta["sizePx"][1])];weapon_layer=layer_at(canvas_size,weapon,wp,center)
 muzzle=weapon_meta["attachments"]["muzzle_anchor"]["positionPx"];muzzle_scene=(center[0]+round((muzzle[0]-weapon_meta["pivotPx"][0])*ww/weapon_meta["sizePx"][0]),center[1]+round((muzzle[1]-weapon_meta["pivotPx"][1])*wh/weapon_meta["sizePx"][1]))
 bw=round(ww*SCALE_TO_WEAPON);bh=round(crop.height*bw/crop.width);bolt=crop.resize((bw,bh),Image.Resampling.LANCZOS);bt=[0,bh//2];bp=[bw//2,bh//2]
 spawn_layer=layer_at(canvas_size,bolt,bt,muzzle_scene);spawn=checker(canvas_size,24);spawn.alpha_composite(weapon_layer);spawn.alpha_composite(spawn_layer);draw=ImageDraw.Draw(spawn);draw.line((muzzle_scene[0]-10,muzzle_scene[1],muzzle_scene[0]+10,muzzle_scene[1]),fill="#e34b46",width=3);draw.line((muzzle_scene[0],muzzle_scene[1]-10,muzzle_scene[0],muzzle_scene[1]+10),fill="#e34b46",width=3)
 spawn_path=REVIEW/f"{NAME}_muzzle_spawn_composite.png";spawn.save(spawn_path,optimize=True)
 tile,header=600,42;grid=Image.new("RGB",(tile*2,(tile+header)*2),"#292a2b");font=ImageFont.load_default()
 for i,angle in enumerate((0,45,90,180)):
  scene=checker((tile,tile),22);origin=(tile//2,tile//2);rot=bolt.rotate(-angle,expand=True,resample=Image.Resampling.BICUBIC);scene.alpha_composite(rot,(origin[0]-rot.width//2,origin[1]-rot.height//2));end=rotate_point((origin[0]+180,origin[1]),origin,angle);ImageDraw.Draw(scene).line((origin[0],origin[1],end[0],end[1]),fill="#d49b48",width=2)
  col,row=i%2,i//2;y=row*(tile+header);grid.paste(scene.convert("RGB"),(col*tile,y+header));ImageDraw.Draw(grid).text((col*tile+12,y+14),f"TRAJECTORY {angle:03d} DEG",font=font,fill="#f3ead3")
 trajectory=REVIEW/f"{NAME}_trajectory_review_grid.png";grid.save(trajectory,optimize=True)
 print(json.dumps({"manifest":str(manifest_path.relative_to(ROOT)),"alpha":str(alpha_path.relative_to(ROOT)),"tightSize":list(crop.size),"pivotPx":pivot,"tailAnchorPx":tail,"tipAnchorPx":tip,"composedSize":game_size,"muzzleScenePx":muzzle_scene,"magentaSpillVisible":spill,"alphaBytes":alpha_path.stat().st_size,"muzzleComposite":str(spawn_path.relative_to(ROOT)),"trajectoryGrid":str(trajectory.relative_to(ROOT))},indent=2))

if __name__=="__main__":main()

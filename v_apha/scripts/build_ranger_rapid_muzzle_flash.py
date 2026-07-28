#!/usr/bin/env python3
"""Split and normalize Ranger's four-frame rapid muzzle flash."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker

ROOT=Path(__file__).resolve().parents[1]
NAME="ranger__muzzle_fx__rapid_flash_loop_v1"
CANDIDATES=ROOT/"assets/staging/candidates/modules/ranger";SOURCE=CANDIDATES/f"{NAME}_source_chroma.png"
CANON=ROOT/"assets/approved/canon/modules/ranger";REVIEW=ROOT/"assets/staging/reviews/modules/ranger"
WEAPON_META=CANON/"ranger__active_primary__rapid_crossbow_v1.json"
ASSEMBLED=REVIEW/"ranger__aim_child__hunting_optics_v1_weapon_composite.png"
DURATIONS=[45,55,65,85];SCALE_TO_WEAPON=.17;PAD=10

def remove_magenta_fringe(image):
 out=image.convert("RGBA");pixels=[]
 for r,g,b,a in out.getdata():
  dominance=min(r-g,b-g)
  if a and r>120 and b>100 and g<175 and dominance>15: a=0
  pixels.append((r,g,b,a))
 out.putdata(pixels);return out

def main():
 CANON.mkdir(parents=True,exist_ok=True);REVIEW.mkdir(parents=True,exist_ok=True)
 source=Image.open(SOURCE).convert("RGBA");sheet=remove_magenta_fringe(chroma_to_alpha(source));sheet.save(CANDIDATES/f"{NAME}_source_alpha.png",optimize=True)
 hw,hh=source.width//2,source.height//2;quads=[(0,0,hw,hh),(hw,0,source.width,hh),(0,hh,hw,source.height),(hw,hh,source.width,source.height)]
 crops=[]
 for q in quads:
  part=sheet.crop(q);box=part.getchannel("A").point(lambda a:255 if a>18 else 0).getbbox()
  if not box:raise RuntimeError("empty rapid-flash quadrant")
  crops.append(part.crop(box))
 left_overhang=crops[0].width//2;pivot_x=PAD+left_overhang
 right_extent=max(crops[0].width-left_overhang,max(c.width for c in crops[1:]));max_h=max(c.height for c in crops)
 canvas_size=[pivot_x+right_extent+PAD,max_h+PAD*2];pivot=[pivot_x,canvas_size[1]//2]
 frames=[];records=[]
 for i,crop in enumerate(crops,1):
  frame=Image.new("RGBA",tuple(canvas_size),(0,0,0,0));anchor_x=crop.width//2 if i==1 else 0;offset=[pivot[0]-anchor_x,pivot[1]-crop.height//2];frame.alpha_composite(crop,tuple(offset))
  filename=f"ranger__muzzle_fx__rapid_flash__frame_{i:02d}_v1_alpha.png";frame.save(CANON/filename,optimize=True);frames.append(frame)
  records.append({"id":f"frame_{i:02d}","image":filename,"rect":{"x":0,"y":0,"w":canvas_size[0],"h":canvas_size[1]},"contentRect":{"x":offset[0],"y":offset[1],"w":crop.width,"h":crop.height},"pivotPx":pivot,"pivot":[round(pivot[0]/canvas_size[0],6),.5],"durationMs":DURATIONS[i-1]})
 source_copy=CANON/f"{NAME}_source_chroma.png";shutil.copy2(SOURCE,source_copy)
 manifest={"schemaVersion":1,"module":"ranger__muzzle_fx__rapid_flash","object":"ranger","owner":"ranger__active_primary__rapid_crossbow","slot":"muzzle_fx","sourceImage":source_copy.name,"projection":"true_top_down_orthographic_90deg","forwardAxis":"+X",
  "attachment":{"parentAnchor":"ranger__active_primary__rapid_crossbow.muzzle_anchor","pivotPx":pivot,"scaleToWeaponLength":SCALE_TO_WEAPON,"inheritRotation":True},"drawOrder":50,"frames":records,
  "animations":{"attack_flash":{"frames":[r["id"] for r in records],"durationsMs":DURATIONS,"loop":False,"holdLast":False,"totalDurationMs":sum(DURATIONS)}},
  "qa":{"segmentation":"fixed_quadrants","sharedCanvas":canvas_size,"sharedPivot":pivot,"runtimeLabels":False,"magentaSpillPerFrame":[],"status":"canon"}}
 spills=[sum(1 for r,g,b,a in f.getdata() if a>18 and r>135 and b>100 and g<120 and min(r-g,b-g)>45) for f in frames];manifest["qa"]["magentaSpillPerFrame"]=spills
 manifest_path=CANON/f"{NAME}.json";manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 tile,header=260,42;grid=Image.new("RGB",(tile*4,tile+header),"#292a2b");font=ImageFont.load_default();labels=["IGNITION","SPEAR","SPLIT","FADE"]
 for i,frame in enumerate(frames):
  thumb=checker((tile,tile),18);scale=min(230/canvas_size[0],230/canvas_size[1]);sprite=frame.resize((round(canvas_size[0]*scale),round(canvas_size[1]*scale)),Image.Resampling.LANCZOS);origin=(15,(tile-sprite.height)//2);thumb.alpha_composite(sprite,origin);grid.paste(thumb.convert("RGB"),(i*tile,header));draw=ImageDraw.Draw(grid);px=i*tile+origin[0]+round(pivot[0]*scale);py=header+origin[1]+round(pivot[1]*scale);draw.line((px-9,py,px+9,py),fill="#e34b46",width=2);draw.line((px,py-9,px,py+9),fill="#e34b46",width=2);draw.text((i*tile+10,14),f"{i+1:02d} {labels[i]} {DURATIONS[i]}ms",font=font,fill="#f3ead3")
 review=REVIEW/f"{NAME}_review_grid.png";grid.save(review,optimize=True)
 assembled=Image.open(ASSEMBLED).convert("RGBA");weapon=json.loads(WEAPON_META.read_text());center=[assembled.width//2,assembled.height//2];weapon_w=714;weapon_scale=weapon_w/weapon["sizePx"][0];m=weapon["attachments"]["muzzle_anchor"]["positionPx"];wp=weapon["pivotPx"];muzzle=[center[0]+round((m[0]-wp[0])*weapon_scale),center[1]+round((m[1]-wp[1])*weapon_scale)];target_w=round(weapon_w*SCALE_TO_WEAPON);ps=target_w/canvas_size[0];preview_size=[target_w,round(canvas_size[1]*ps)];preview_pivot=[round(pivot[0]*ps),round(pivot[1]*ps)];previews=[]
 for frame in frames:
  scene=assembled.copy();flash=frame.resize(tuple(preview_size),Image.Resampling.LANCZOS);scene.alpha_composite(flash,(muzzle[0]-preview_pivot[0],muzzle[1]-preview_pivot[1]));previews.append(scene.convert("RGB"))
 previews.append(assembled.convert("RGB"));gif=REVIEW/f"{NAME}_attack_preview.gif";previews[0].save(gif,save_all=True,append_images=previews[1:],duration=DURATIONS+[420],loop=0,optimize=True)
 total=sum((CANON/r["image"]).stat().st_size for r in records)
 print(json.dumps({"manifest":str(manifest_path.relative_to(ROOT)),"sharedCanvas":canvas_size,"sharedPivot":pivot,"contentSizes":[list(c.size) for c in crops],"durationsMs":DURATIONS,"totalDurationMs":sum(DURATIONS),"runtimeFrameBytes":total,"under5MB":total<5_000_000,"magentaSpillPerFrame":spills,"muzzleScenePx":muzzle,"composedFlashSize":preview_size,"reviewGrid":str(review.relative_to(ROOT)),"attackPreview":str(gif.relative_to(ROOT))},indent=2))

if __name__=="__main__":main()

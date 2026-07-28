#!/usr/bin/env python3
"""Split, normalize, and preview Ranger's barbed-bolt impact."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker

ROOT=Path(__file__).resolve().parents[1]
NAME="ranger__impact_fx__barbed_hit_v1"
CANDIDATES=ROOT/"assets/staging/candidates/modules/ranger";SOURCE=CANDIDATES/f"{NAME}_source_chroma.png"
CANON=ROOT/"assets/approved/canon/modules/ranger";REVIEW=ROOT/"assets/staging/reviews/modules/ranger"
BOLT_META=CANON/"ranger__projectile__barbed_bolt_v1.json";BOLT_IMAGE=CANON/"ranger__projectile__barbed_bolt_v1_alpha.png"
DURATIONS=[55,70,90,120];SCALE_TO_BOLT=.72

def despill(image):
 out=image.convert("RGBA");pixels=[]
 for r,g,b,a in out.getdata():
  if a and r>120 and b>100 and g<175 and min(r-g,b-g)>15:a=0
  pixels.append((r,g,b,a))
 out.putdata(pixels);return out

def main():
 CANON.mkdir(parents=True,exist_ok=True);REVIEW.mkdir(parents=True,exist_ok=True)
 source=Image.open(SOURCE).convert("RGBA");alpha=despill(chroma_to_alpha(source));alpha.save(CANDIDATES/f"{NAME}_source_alpha.png",optimize=True)
 w,h=alpha.size;slots=[(0,0,w//2,h//2),(w//2,0,w,h//2),(0,h//2,w//2,h),(w//2,h//2,w,h)];canvas=[w//2,h//2];pivot=[canvas[0]//2,canvas[1]//2]
 frames=[];records=[];spills=[]
 for i,(slot,duration) in enumerate(zip(slots,DURATIONS),1):
  frame=alpha.crop(slot);box=frame.getchannel("A").point(lambda a:255 if a>18 else 0).getbbox()
  if not box:raise RuntimeError(f"empty impact quadrant {i}")
  spill=sum(1 for r,g,b,a in frame.getdata() if a>18 and r>135 and b>100 and g<120 and min(r-g,b-g)>45);spills.append(spill)
  filename=f"ranger__impact_fx__barbed_hit__frame_{i:02d}_v1_alpha.png";frame.save(CANON/filename,optimize=True);frames.append(frame)
  records.append({"id":f"frame_{i:02d}","image":filename,"rect":{"x":0,"y":0,"w":canvas[0],"h":canvas[1]},"contentRect":{"x":box[0],"y":box[1],"w":box[2]-box[0],"h":box[3]-box[1]},"pivotPx":pivot,"pivot":[.5,.5],"durationMs":duration,"magentaSpillPixels":spill})
 source_copy=CANON/f"{NAME}_source_chroma.png";shutil.copy2(SOURCE,source_copy)
 manifest={"schemaVersion":1,"module":"ranger__impact_fx__barbed_hit","object":"ranger","family":"fortress_ranged","slot":"impact_fx","sourceImage":source_copy.name,"projection":"true_top_down_orthographic_90deg",
  "attachment":{"parentModule":"ranger__projectile__barbed_bolt","anchor":"impact_tip","scaleToProjectileLength":SCALE_TO_BOLT,"inheritRotation":False},"drawOrder":55,"frames":records,
  "animations":{"impact":{"frames":[r["id"] for r in records],"durationsMs":DURATIONS,"loop":False,"holdLast":False,"totalDurationMs":sum(DURATIONS)}},
  "qa":{"sharedCanvas":canvas,"sharedPivot":pivot,"runtimeLabels":False,"magentaSpillPerFrame":spills,"status":"canon"}}
 manifest_path=CANON/f"{NAME}.json";manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 tile,header=300,44;grid=Image.new("RGB",(tile*4,tile+header),"#292a2b");draw=ImageDraw.Draw(grid);font=ImageFont.load_default()
 for i,frame in enumerate(frames):
  panel=checker((tile,tile),18);preview=frame.resize((280,280),Image.Resampling.LANCZOS);panel.alpha_composite(preview,(10,10));grid.paste(panel.convert("RGB"),(i*tile,header));cx,cy=i*tile+tile//2,header+tile//2;draw.text((i*tile+10,15),f"FRAME {i+1:02d}  {DURATIONS[i]}ms",font=font,fill="#f3ead3");draw.line((cx-9,cy,cx+9,cy),fill="#e34b46",width=2);draw.line((cx,cy-9,cx,cy+9),fill="#e34b46",width=2)
 review=REVIEW/f"{NAME}_review_grid.png";grid.save(review,optimize=True)
 scene_size=(720,420);contact=(520,210);bolt=Image.open(BOLT_IMAGE).convert("RGBA");bolt_meta=json.loads(BOLT_META.read_text());bolt_w=170;bolt_h=round(bolt.height*bolt_w/bolt.width);bolt=bolt.resize((bolt_w,bolt_h),Image.Resampling.LANCZOS);tip=[bolt_w-1,bolt_h//2]
 previews=[]
 for x in (250,360,455):
  scene=checker(scene_size,24);scene.alpha_composite(bolt,(x-tip[0],contact[1]-tip[1]));previews.append(scene.convert("RGB"))
 effect_px=round(bolt_w*SCALE_TO_BOLT)
 for frame in frames:
  scene=checker(scene_size,24);fx=frame.resize((effect_px,effect_px),Image.Resampling.LANCZOS);scene.alpha_composite(fx,(contact[0]-effect_px//2,contact[1]-effect_px//2));previews.append(scene.convert("RGB"))
 gif=REVIEW/f"{NAME}_contact_preview.gif";previews[0].save(gif,save_all=True,append_images=previews[1:],duration=[70,70,70]+DURATIONS,loop=0,optimize=True)
 total=sum((CANON/r["image"]).stat().st_size for r in records)
 print(json.dumps({"manifest":str(manifest_path.relative_to(ROOT)),"frames":4,"sharedCanvas":canvas,"sharedPivot":pivot,"contentRects":[r["contentRect"] for r in records],"durationsMs":DURATIONS,"totalDurationMs":sum(DURATIONS),"magentaSpillPerFrame":spills,"runtimeFrameBytes":total,"under5MB":total<5_000_000,"effectPreviewPx":effect_px,"reviewGrid":str(review.relative_to(ROOT)),"contactPreview":str(gif.relative_to(ROOT))},indent=2))

if __name__=="__main__":main()

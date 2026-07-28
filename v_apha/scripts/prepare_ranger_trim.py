#!/usr/bin/env python3
"""Promote Ranger identity trim and validate full-platform clearance."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT=Path(__file__).resolve().parents[1]
NAME="ranger__identity_child__ranger_trim_v1"
CANDIDATES=ROOT/"assets/staging/candidates/modules/ranger";SOURCE=CANDIDATES/f"{NAME}_chroma.png"
CANON=ROOT/"assets/approved/canon/modules/ranger";REVIEW=ROOT/"assets/staging/reviews/modules/ranger"
SHARED=ROOT/"assets/approved/canon/modules/fortress_ranged"
BASE_META=SHARED/"fortress_ranged__base_token__round_light_v1.json"
CORE=ROOT/"assets/staging/reviews/modules/fortress_ranged/fortress_ranged__base_socket_lantern_housing_v1_composite.png"
WEAPON_META=CANON/"ranger__active_primary__rapid_crossbow_v1.json";WEAPON_IMAGE=CANON/"ranger__active_primary__rapid_crossbow_v1_alpha.png"
MAG_META=CANON/"ranger__ammo_child__bolt_magazine_v1.json";MAG_IMAGE=CANON/"ranger__ammo_child__bolt_magazine_v1_alpha.png"
OPT_META=CANON/"ranger__aim_child__hunting_optics_v1.json";OPT_IMAGE=CANON/"ranger__aim_child__hunting_optics_v1_alpha.png"
RACK_META=CANON/"ranger__utility_child__arrow_rack_v1.json";RACK_IMAGE=CANON/"ranger__utility_child__arrow_rack_v1_alpha.png"
SCALE_TO_BASE=.115;POSITION=[.79,.79]

def layer_at(size,image,pivot,point):
 out=Image.new("RGBA",size,(0,0,0,0));out.alpha_composite(image,(point[0]-pivot[0],point[1]-pivot[1]));return out

def main():
 CANON.mkdir(parents=True,exist_ok=True);REVIEW.mkdir(parents=True,exist_ok=True)
 full=chroma_to_alpha(Image.open(SOURCE).convert("RGBA"));full.save(CANDIDATES/f"{NAME}_alpha_full.png",optimize=True)
 bounds=full.getchannel("A").point(lambda a:255 if a>18 else 0).getbbox()
 if not bounds:raise RuntimeError("empty Ranger trim")
 crop=full.crop(bounds);pivot=[crop.width//2,crop.height//2]
 alpha_path=CANON/f"{NAME}_alpha.png";chroma_path=CANON/f"{NAME}_chroma.png";crop.save(alpha_path,optimize=True);shutil.copy2(SOURCE,chroma_path)
 base=json.loads(BASE_META.read_text());target_w=round(base["footprintPx"]*SCALE_TO_BASE);game_size=[target_w,round(crop.height*target_w/crop.width)]
 spill=sum(1 for r,g,b,a in crop.getdata() if a>18 and r>160 and b>140 and g<115 and min(r-g,b-g)>65)
 manifest={"schemaVersion":1,"module":"ranger__identity_child__ranger_trim","object":"ranger","family":"fortress_ranged","slot":"identity_child",
  "image":alpha_path.name,"sourceImage":chroma_path.name,"sizePx":list(crop.size),"rect":{"x":0,"y":0,"w":crop.width,"h":crop.height},
  "pivotPx":pivot,"pivot":[.5,.5],"projection":"true_top_down_orthographic_90deg","runtimeScale":{"scaleToBaseFootprint":SCALE_TO_BASE},
  "attachments":{"parent":{"module":"fortress_ranged__base_token__round_light","anchor":"object_center","positionNormalized":POSITION,"inheritRotation":False}},
  "drawOrder":16,"qa":{"transparent":True,"tightRect":True,"magentaSpillPixels":spill,"alphaBytes":alpha_path.stat().st_size,
  "under5MB":alpha_path.stat().st_size<5_000_000,"status":"canon"}}
 manifest_path=CANON/f"{NAME}.json"

 core=Image.open(CORE).convert("RGBA");center=(core.width//2,core.height//2)
 trim=crop.resize(tuple(game_size),Image.Resampling.LANCZOS);trim_point=(round(core.width*POSITION[0]),round(core.height*POSITION[1]));trim_layer=layer_at(core.size,trim,[trim.width//2,trim.height//2],trim_point)
 rack_meta=json.loads(RACK_META.read_text());rack=Image.open(RACK_IMAGE).convert("RGBA");rw=round(base["footprintPx"]*rack_meta["runtimeScale"]["scaleToBaseFootprint"]);rh=round(rack.height*rw/rack.width);rack=rack.resize((rw,rh),Image.Resampling.LANCZOS);rp=rack_meta["attachments"]["parent"]["positionNormalized"];rack_layer=layer_at(core.size,rack,[rw//2,rh//2],(round(core.width*rp[0]),round(core.height*rp[1])))
 weapon_meta=json.loads(WEAPON_META.read_text());weapon=Image.open(WEAPON_IMAGE).convert("RGBA");ww=round(base["footprintPx"]*weapon_meta["runtimeScale"]["scaleToBaseFootprint"]);wh=round(weapon.height*ww/weapon.width);weapon=weapon.resize((ww,wh),Image.Resampling.LANCZOS);wp=[round(weapon_meta["pivotPx"][0]*ww/weapon_meta["sizePx"][0]),round(weapon_meta["pivotPx"][1]*wh/weapon_meta["sizePx"][1])];weapon_layer=layer_at(core.size,weapon,wp,center)
 mag_meta=json.loads(MAG_META.read_text());mag=Image.open(MAG_IMAGE).convert("RGBA");mw=round(ww*mag_meta["runtimeScale"]["widthToParentWeapon"]);mh=round(mag.height*mw/mag.width);mag=mag.resize((mw,mh),Image.Resampling.LANCZOS).rotate(-90,expand=True,resample=Image.Resampling.BICUBIC);ms=weapon_meta["attachments"]["magazine_socket"]["positionPx"];mp=(center[0]+round((ms[0]-weapon_meta["pivotPx"][0])*ww/weapon_meta["sizePx"][0]),center[1]+round((ms[1]-weapon_meta["pivotPx"][1])*wh/weapon_meta["sizePx"][1]));mag_layer=layer_at(core.size,mag,[mag.width//2,mag.height//2],mp)
 opt_meta=json.loads(OPT_META.read_text());opt=Image.open(OPT_IMAGE).convert("RGBA");ow=round(ww*opt_meta["runtimeScale"]["widthToParentWeapon"]);oh=round(opt.height*ow/opt.width);opt=opt.resize((ow,oh),Image.Resampling.LANCZOS);os=weapon_meta["attachments"]["optics_socket"]["positionPx"];op=(center[0]+round((os[0]-weapon_meta["pivotPx"][0])*ww/weapon_meta["sizePx"][0]),center[1]+round((os[1]-weapon_meta["pivotPx"][1])*wh/weapon_meta["sizePx"][1]));opt_layer=layer_at(core.size,opt,[ow//2,oh//2],op)
 tile,header=620,42;grid=Image.new("RGB",(tile*2,(tile+header)*2),"#292a2b");font=ImageFont.load_default();overlaps=[]
 for i,angle in enumerate((0,90,180,270)):
  rwlay=weapon_layer.rotate(-angle,Image.Resampling.BICUBIC,center=center);rmlay=mag_layer.rotate(-angle,Image.Resampling.BICUBIC,center=center);rolay=opt_layer.rotate(-angle,Image.Resampling.BICUBIC,center=center)
  group=ImageChops.lighter(ImageChops.lighter(rwlay.getchannel("A"),rmlay.getchannel("A")),rolay.getchannel("A"));tm=trim_layer.getchannel("A").point(lambda a:255 if a>18 else 0);gm=group.point(lambda a:255 if a>18 else 0);overlap=sum(1 for a,b in zip(tm.getdata(),gm.getdata()) if a and b);overlaps.append(overlap)
  scene=checker(core.size,24);scene.alpha_composite(core);scene.alpha_composite(rack_layer);scene.alpha_composite(trim_layer);scene.alpha_composite(rwlay);scene.alpha_composite(rmlay);scene.alpha_composite(rolay)
  thumb=scene.convert("RGB").resize((tile,tile),Image.Resampling.LANCZOS);col,row=i%2,i//2;y=row*(tile+header);grid.paste(thumb,(col*tile,y+header));ImageDraw.Draw(grid).text((col*tile+12,y+14),f"FULL RANGER {angle:03d} DEG — TRIM OVERLAP {overlap} PX",font=font,fill="#f3ead3")
 review=REVIEW/f"{NAME}_full_platform_clearance_grid.png";grid.save(review,optimize=True)
 manifest["qa"]["weaponOverlapPixelsByAngle"]=dict(zip(("0","90","180","270"),overlaps));manifest["qa"]["clearancePass"]=max(overlaps)==0;manifest["qa"]["status"]="canon" if max(overlaps)==0 else "needs_adjustment";manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"manifest":str(manifest_path.relative_to(ROOT)),"alpha":str(alpha_path.relative_to(ROOT)),"tightSize":list(crop.size),"pivotPx":pivot,"composedSize":game_size,"positionNormalized":POSITION,"overlapPixels":overlaps,"clearancePass":max(overlaps)==0,"magentaSpillVisible":spill,"alphaBytes":alpha_path.stat().st_size,"reviewGrid":str(review.relative_to(ROOT))},indent=2))

if __name__=="__main__":main()

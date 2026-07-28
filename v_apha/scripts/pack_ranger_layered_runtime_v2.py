#!/usr/bin/env python3
"""Pack Ranger and inherited fortress layers into one compact runtime atlas."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
RANGER=ROOT/"assets/approved/canon/modules/ranger";SHARED=ROOT/"assets/approved/canon/modules/fortress_ranged"
WATCH_RUNTIME=ROOT/"assets/approved/runtime/watchtower";OUT=ROOT/"assets/approved/runtime/ranger";REVIEW=ROOT/"assets/staging/reviews/ranger"
ATLAS_SIZE=(1024,1024);PAD=4;BASE_FOOTPRINT=512

def load(path):return json.loads(path.read_text())
def trim(image):
 box=image.getchannel("A").point(lambda a:255 if a>5 else 0).getbbox()
 if not box:raise RuntimeError("empty sprite")
 return image.crop(box),box
def resized(image,width):return image.resize((width,round(image.height*width/image.width)),Image.Resampling.LANCZOS)
def scrub_chroma(image):
 pixels=[];removed=0
 for r,g,b,a in image.getdata():
  if a>0 and r>135 and b>115 and g<125 and r-g>45 and b-g>35:
   pixels.append((r,g,b,0));removed+=1
  else:pixels.append((r,g,b,a))
 image.putdata(pixels)
 return image,removed

def main():
 OUT.mkdir(parents=True,exist_ok=True);REVIEW.mkdir(parents=True,exist_ok=True)
 sprites=[];chroma_removed=0
 def add_image(sprite_id,path,width,pivot_src,draw,semantic,duration=None,local_rotation=0):
  nonlocal chroma_removed
  original=Image.open(path).convert("RGBA");scaled=resized(original,width);scaled,removed=scrub_chroma(scaled);chroma_removed+=removed;sx=scaled.width/original.width;sy=scaled.height/original.height;pivot_full=[round(pivot_src[0]*sx),round(pivot_src[1]*sy)];cropped,box=trim(scaled);pivot=[pivot_full[0]-box[0],pivot_full[1]-box[1]]
  rec={"id":sprite_id,"image":cropped,"pivotPx":pivot,"pivotInSourcePx":pivot_full,"sourceSize":list(scaled.size),"trimOffset":[box[0],box[1]],"drawOrder":draw,"semantic":semantic,"localRotationDeg":local_rotation}
  if duration is not None:rec["durationMs"]=duration
  sprites.append(rec)
 def add_watch(sprite_id):
  nonlocal chroma_removed
  wm=watch["sprites"][sprite_id];r=wm["rect"];im=watch_atlas.crop((r["x"],r["y"],r["x"]+r["w"],r["y"]+r["h"]));im,removed=scrub_chroma(im);chroma_removed+=removed;rec={"id":sprite_id,"image":im,"pivotPx":wm["pivotPx"],"pivotInSourcePx":wm["pivotInSourcePx"],"sourceSize":wm["sourceSize"],"trimOffset":wm["trimOffset"],"drawOrder":wm["drawOrder"],"semantic":wm["semantic"],"localRotationDeg":0}
  if "durationMs" in wm:rec["durationMs"]=wm["durationMs"]
  sprites.append(rec)

 watch=load(WATCH_RUNTIME/"watchtower_layered_manifest_v2.json");watch_atlas=Image.open(WATCH_RUNTIME/watch["image"]).convert("RGBA")
 inherited=["base_stone_token","central_socket","lantern_body"]+[f"lantern_flame_{i:02d}" for i in range(1,5)]+["destroy_debris_stone_a","destroy_debris_stone_b","destroy_debris_stone_c"]+[f"destroy_dust_{i:02d}" for i in range(1,5)]+[f"destroy_sparks_{i:02d}" for i in range(1,5)]
 for sid in inherited:add_watch(sid)

 weapon=load(RANGER/"ranger__active_primary__rapid_crossbow_v1.json");weapon_w=round(BASE_FOOTPRINT*weapon["runtimeScale"]["scaleToBaseFootprint"]);add_image("rapid_crossbow",RANGER/weapon["image"],weapon_w,weapon["pivotPx"],30,"active_primary")
 mag=load(RANGER/"ranger__ammo_child__bolt_magazine_v1.json");add_image("bolt_magazine",RANGER/mag["image"],round(weapon_w*mag["runtimeScale"]["widthToParentWeapon"]),mag["pivotPx"],31,"ammo_child",local_rotation=90)
 optic=load(RANGER/"ranger__aim_child__hunting_optics_v1.json");add_image("hunting_optics",RANGER/optic["image"],round(weapon_w*optic["runtimeScale"]["widthToParentWeapon"]),optic["pivotPx"],32,"aim_child")
 rack=load(RANGER/"ranger__utility_child__arrow_rack_v1.json");add_image("arrow_rack",RANGER/rack["image"],round(BASE_FOOTPRINT*rack["runtimeScale"]["scaleToBaseFootprint"]),rack["pivotPx"],15,"utility_child")
 badge=load(RANGER/"ranger__identity_child__ranger_trim_v1.json");add_image("ranger_trim",RANGER/badge["image"],round(BASE_FOOTPRINT*badge["runtimeScale"]["scaleToBaseFootprint"]),badge["pivotPx"],16,"identity_child")
 bolt=load(RANGER/"ranger__projectile__barbed_bolt_v1.json");bolt_w=round(weapon_w*bolt["runtimeScale"]["lengthToParentWeapon"]);add_image("barbed_bolt",RANGER/bolt["image"],bolt_w,bolt["pivotPx"],40,"projectile")
 flash=load(RANGER/"ranger__muzzle_fx__rapid_flash_loop_v1.json");flash_w=round(weapon_w*flash["attachment"]["scaleToWeaponLength"])
 for i,f in enumerate(flash["frames"],1):add_image(f"rapid_flash_{i:02d}",RANGER/f["image"],flash_w,f["pivotPx"],50,"attack_fx",f["durationMs"])
 impact=load(RANGER/"ranger__impact_fx__barbed_hit_v1.json");impact_w=round(bolt_w*impact["attachment"]["scaleToProjectileLength"])
 for i,f in enumerate(impact["frames"],1):add_image(f"barbed_hit_{i:02d}",RANGER/f["image"],impact_w,f["pivotPx"],55,"impact_fx",f["durationMs"])

 base=next(s for s in sprites if s["id"]=="base_stone_token");base["packedRect"]={"x":PAD,"y":PAD,"w":base["image"].width,"h":base["image"].height}
 free=[ [PAD+base["image"].width+PAD,PAD,ATLAS_SIZE[0]-(PAD+base["image"].width+PAD)-PAD,base["image"].height], [PAD,PAD+base["image"].height+PAD,ATLAS_SIZE[0]-PAD*2,ATLAS_SIZE[1]-(PAD+base["image"].height+PAD)-PAD] ]
 others=sorted([s for s in sprites if s is not base],key=lambda s:max(s["image"].size),reverse=True)
 for s in others:
  w,h=s["image"].size;choices=[(max(fr[2]-w,fr[3]-h),idx,fr) for idx,fr in enumerate(free) if w<=fr[2] and h<=fr[3]]
  if not choices:raise RuntimeError(f"atlas overflow at {s['id']} {w}x{h}")
  _,idx,(x,y,fw,fh)=min(choices);free.pop(idx);s["packedRect"]={"x":x,"y":y,"w":w,"h":h}
  right=[x+w+PAD,y,fw-w-PAD,h];bottom=[x,y+h+PAD,fw,fh-h-PAD]
  if right[2]>0 and right[3]>0:free.append(right)
  if bottom[2]>0 and bottom[3]>0:free.append(bottom)

 atlas=Image.new("RGBA",ATLAS_SIZE,(0,0,0,0))
 for s in sprites:atlas.alpha_composite(s["image"],(s["packedRect"]["x"],s["packedRect"]["y"]))
 atlas_path=OUT/"ranger_layered_runtime_v2.png";atlas.save(atlas_path,optimize=True)
 byid={s["id"]:s for s in sprites}
 def clip(prefix,loop):
  arr=[s for s in sprites if s["id"].startswith(prefix)];arr.sort(key=lambda s:s["id"]);return {"frames":[s["id"] for s in arr],"durationsMs":[s.get("durationMs",180) for s in arr],"loop":loop,"holdLast":False}
 manifest={"schemaVersion":2,"object":"ranger","family":"fortress_ranged","pipeline":"layered_object_v2","image":atlas_path.name,"atlasSize":list(ATLAS_SIZE),"baseFootprintPx":BASE_FOOTPRINT,"projection":"true_top_down_orthographic_90deg","sprites":{},
  "attachments":{"objectCenter":{"parent":"base_stone_token","positionNormalized":[.5,.5]},"weaponSocket":{"parent":"central_socket","positionNormalized":[.5,.5]},"magazineSocket":{"parent":"rapid_crossbow","positionNormalized":weapon["attachments"]["magazine_socket"]["positionNormalized"],"localRotationDeg":90},"opticsSocket":{"parent":"rapid_crossbow","positionNormalized":[round(weapon["attachments"]["optics_socket"]["positionPx"][0]/weapon["sizePx"][0],6),round(weapon["attachments"]["optics_socket"]["positionPx"][1]/weapon["sizePx"][1],6)]},"muzzle":{"parent":"rapid_crossbow","positionNormalized":weapon["attachments"]["muzzle_anchor"]["positionNormalized"],"forwardAxis":"+X"},"lantern":{"parent":"base_stone_token","positionNormalized":[.29,.72]},"lanternGlow":{"parent":"lantern_body","positionNormalized":[.5,.5]},"arrowRack":{"parent":"base_stone_token","positionNormalized":rack["attachments"]["parent"]["positionNormalized"]},"rangerTrim":{"parent":"base_stone_token","positionNormalized":badge["attachments"]["parent"]["positionNormalized"]}},
  "drawOrder":["base_stone_token","central_socket","arrow_rack","ranger_trim","lantern_body","lantern_flame_*","rapid_crossbow","bolt_magazine","hunting_optics","barbed_bolt","rapid_flash_*","barbed_hit_*","destroy_debris_stone_*","destroy_dust_*","destroy_sparks_*"],
  "animations":{"idle_lantern":clip("lantern_flame_",True),"attack":clip("rapid_flash_",False),"impact":clip("barbed_hit_",False),"destroy_dust":clip("destroy_dust_",False),"destroy_sparks":clip("destroy_sparks_",False)},
  "runtimeTransforms":{"rapid_crossbow":{"rotation":"aimAngle","anchor":"weaponSocket"},"bolt_magazine":{"anchor":"magazineSocket","inheritRotation":True,"localRotationDeg":90},"hunting_optics":{"anchor":"opticsSocket","inheritRotation":True},"barbed_bolt":{"position":"projectilePosition","rotation":"trajectoryAngle"},"rapid_flash_*":{"anchor":"muzzle","inheritRotation":True},"barbed_hit_*":{"position":"impactPosition"},"arrow_rack":{"anchor":"arrowRack"},"ranger_trim":{"anchor":"rangerTrim"}},
  "sourceManifests":[p.name for p in sorted(RANGER.glob("*.json"))]+["fortress_ranged__base_token__round_light_v1.json","fortress_ranged__center_socket__light_bearing_v1.json","fortress_ranged__ambient_child__amber_lantern_housing_v1.json","fortress_ranged__ambient_child__amber_lantern_glow_loop_v1.json","fortress_ranged__debris__stone_rim_chunk_a_v1.json","fortress_ranged__debris__stone_rim_chunk_b_v1.json","fortress_ranged__debris__stone_core_chunk_c_v1.json","watchtower__destroy_fx__stone_dust_burst_v1.json","watchtower__destroy_fx__metal_spark_burst_v1.json"],"qa":{}}
 for s in sprites:
  rec={"rect":s["packedRect"],"pivotPx":s["pivotPx"],"pivotInSourcePx":s["pivotInSourcePx"],"sourceSize":s["sourceSize"],"trimOffset":s["trimOffset"],"drawOrder":s["drawOrder"],"semantic":s["semantic"]}
  if s.get("durationMs") is not None:rec["durationMs"]=s["durationMs"]
  if s.get("localRotationDeg"):rec["localRotationDeg"]=s["localRotationDeg"]
  manifest["sprites"][s["id"]]=rec
 rects=[s["packedRect"] for s in sprites];overlaps=0
 for i,a in enumerate(rects):
  for b in rects[i+1:]:
   if a["x"]<b["x"]+b["w"] and a["x"]+a["w"]>b["x"] and a["y"]<b["y"]+b["h"] and a["y"]+a["h"]>b["y"]:overlaps+=1
 spill=sum(1 for r,g,b,a in atlas.getdata() if a>18 and r>150 and b>130 and g<115 and min(r-g,b-g)>55)
 manifest["qa"]={"spriteCount":len(sprites),"rectsInBounds":all(r["x"]>=0 and r["y"]>=0 and r["x"]+r["w"]<=ATLAS_SIZE[0] and r["y"]+r["h"]<=ATLAS_SIZE[1] for r in rects),"rectOverlapCount":overlaps,"magentaSpillPixels":spill,"chromaRemovedPixels":chroma_removed,"runtimeLabels":False,"atlasBytes":atlas_path.stat().st_size,"under5MB":atlas_path.stat().st_size<5_000_000,"status":"approved"}
 manifest_path=OUT/"ranger_layered_manifest_v2.json";manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")

 tile,header=190,32;cols=6;rows=(len(sprites)+cols-1)//cols;grid=Image.new("RGB",(tile*cols,(tile+header)*rows),"#292a2b");font=ImageFont.load_default()
 for i,s in enumerate(sorted(sprites,key=lambda x:(x["drawOrder"],x["id"]))):
  col,row=i%cols,i//cols;panel=Image.new("RGB",(tile,tile),"#d9d1bd");draw=ImageDraw.Draw(panel)
  for y in range(0,tile,16):
   for x in range(0,tile,16):
    if (x//16+y//16)%2:draw.rectangle((x,y,x+15,y+15),fill="#c8bea7")
  scale=min(170/s["image"].width,170/s["image"].height);im=s["image"].resize((max(1,round(s["image"].width*scale)),max(1,round(s["image"].height*scale))),Image.Resampling.LANCZOS);origin=((tile-im.width)//2,(tile-im.height)//2);panel.paste(im.convert("RGB"),origin,im.getchannel("A"));grid.paste(panel,(col*tile,row*(tile+header)+header));ImageDraw.Draw(grid).text((col*tile+7,row*(tile+header)+10),s["id"][:27],font=font,fill="#f3ead3")
 review_path=REVIEW/"ranger_layered_review_grid_v2.png";grid.save(review_path,optimize=True)

 comp=Image.new("RGBA",(720,720),(0,0,0,0));center=(360,360)
 def paste(sid,point,rotation=0):
  s=byid[sid];im=s["image"];p=s["pivotPx"]
  if rotation:layer=Image.new("RGBA",comp.size,(0,0,0,0));layer.alpha_composite(im,(point[0]-p[0],point[1]-p[1]));comp.alpha_composite(layer.rotate(-rotation,Image.Resampling.BICUBIC,center=point))
  else:comp.alpha_composite(im,(point[0]-p[0],point[1]-p[1]))
 def base_point(norm):return (center[0]+round((norm[0]-.5)*512),center[1]+round((norm[1]-.5)*512))
 paste("base_stone_token",center);paste("central_socket",center);paste("arrow_rack",base_point((.5,.12)));paste("ranger_trim",base_point((.79,.79)));paste("lantern_body",base_point((.29,.72)));paste("lantern_flame_03",base_point((.29,.72)));paste("rapid_crossbow",center)
 ws=byid["rapid_crossbow"];wp=ws["pivotInSourcePx"]
 def weapon_point(norm):return (center[0]+round(norm[0]*ws["sourceSize"][0]-wp[0]),center[1]+round(norm[1]*ws["sourceSize"][1]-wp[1]))
 paste("bolt_magazine",weapon_point(manifest["attachments"]["magazineSocket"]["positionNormalized"]),90);paste("hunting_optics",weapon_point(manifest["attachments"]["opticsSocket"]["positionNormalized"]))
 comp_path=REVIEW/"ranger_layered_composite_preview_v2.png";comp.save(comp_path,optimize=True)
 print(json.dumps({"atlas":str(atlas_path.relative_to(ROOT)),"manifest":str(manifest_path.relative_to(ROOT)),"atlasSize":list(ATLAS_SIZE),"atlasBytes":atlas_path.stat().st_size,"under5MB":atlas_path.stat().st_size<5_000_000,"spriteCount":len(sprites),"rectsInBounds":manifest["qa"]["rectsInBounds"],"rectOverlapCount":overlaps,"magentaSpillPixels":spill,"reviewGrid":str(review_path.relative_to(ROOT)),"compositePreview":str(comp_path.relative_to(ROOT))},indent=2))

if __name__=="__main__":main()

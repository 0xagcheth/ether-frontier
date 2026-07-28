#!/usr/bin/env python3
"""Correct Watchtower runtime: one projection, named layers, no baked composites."""

from __future__ import annotations

import json
import math
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/sprite-atlases/watchtower/layered-v2-candidate"
OUT = ROOT / "assets/sprite-atlases/watchtower/layered-runtime-v3"


def rgba(size): return Image.new("RGBA", size, (0, 0, 0, 0))


def source_parts():
    manifest = json.loads((SOURCE / "watchtower_layered_manifest.json").read_text())
    atlas = Image.open(SOURCE / manifest["image"]).convert("RGBA")
    keep = ["base_stone_token", "central_socket", "crossbow_rotatable", "projectile_bolt"]
    keep += [f"muzzle_flash_{i:02d}" for i in range(1, 5)]
    keep += [f"destroy_debris_{i:02d}" for i in range(1, 10)]
    result = {}
    for name in keep:
        r = manifest["sprites"][name]["rect"]
        result[name] = atlas.crop((r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"]))
    return result


def flag_socket():
    im = rgba((80, 80)); d = ImageDraw.Draw(im)
    d.ellipse((7, 7, 73, 73), fill=(62, 43, 28, 255), outline=(31, 24, 18, 255), width=6)
    d.ellipse((15, 15, 65, 65), fill=(171, 130, 74, 255), outline=(87, 58, 32, 255), width=5)
    d.ellipse((29, 29, 51, 51), fill=(69, 69, 64, 255), outline=(30, 30, 28, 255), width=4)
    return im


def pennant(phase):
    im = rgba((190, 104)); d = ImageDraw.Draw(im)
    wave = [0, 7, -5, 4][phase]
    outer = [(8, 25), (72, 17 + wave), (176, 48), (73, 86 - wave), (8, 77)]
    inner = [(18, 31), (72, 25 + wave), (158, 49), (72, 78 - wave), (18, 70)]
    d.polygon(outer, fill=(74, 48, 28, 255), outline=(31, 23, 17, 255))
    d.polygon(inner, fill=(139, 45, 40, 255), outline=(71, 25, 25, 255), width=3)
    d.line((30, 42, 128, 49, 34, 61), fill=(190, 77, 59, 150), width=4)
    # Top-down cardboard attachment tongue.
    d.rounded_rectangle((2, 36, 25, 68), radius=7, fill=(171, 130, 74, 255), outline=(42, 29, 20, 255), width=4)
    return im


def lantern_housing():
    im = rgba((112, 112)); d = ImageDraw.Draw(im)
    d.ellipse((7, 7, 105, 105), fill=(39, 35, 29, 255), outline=(18, 18, 16, 255), width=6)
    d.ellipse((18, 18, 94, 94), fill=(92, 88, 75, 255), outline=(30, 29, 25, 255), width=5)
    for angle in range(0, 360, 45):
        x=56+math.cos(math.radians(angle))*39; y=56+math.sin(math.radians(angle))*39
        d.ellipse((x-4,y-4,x+4,y+4),fill=(170,144,96,255))
    d.ellipse((33, 33, 79, 79), fill=(45, 38, 27, 255), outline=(21, 19, 16, 255), width=4)
    return im


def glow(phase):
    im=rgba((100,100)); d=ImageDraw.Draw(im); pulse=[38,44,48,42][phase]
    d.ellipse((50-pulse,50-pulse,50+pulse,50+pulse),fill=(255,154,34,42))
    d.ellipse((22,22,78,78),fill=(237,124,28,110))
    d.ellipse((31,31,69,69),fill=(255,190,54,220),outline=(95,48,20,255),width=3)
    d.ellipse((40,40,60,60),fill=(255,239,153,255))
    return im


def pack(parts, width=1536, pad=8):
    order=sorted(parts,key=lambda n:(-parts[n].height,-parts[n].width,n)); x=y=pad; row=0; pos={}
    for name in order:
        im=parts[name]
        if x+im.width+pad>width: x=pad; y+=row+pad; row=0
        pos[name]=(x,y); x+=im.width+pad; row=max(row,im.height)
    atlas=rgba((width,y+row+pad)); sprites={}
    for name,im in parts.items():
        x,y=pos[name]; atlas.alpha_composite(im,(x,y))
        sprites[name]={"rect":{"x":x,"y":y,"w":im.width,"h":im.height},"pivot":[.5,.5]}
    return atlas,sprites


def intact_layers(flag, glow_frame, flash=None, recoil=0):
    layers=[
      {"sprite":"base_stone_token","anchor":"object_center","sizePx":[255,256]},
      {"sprite":"central_socket","anchor":"object_center","sizePx":[116,109]},
      {"sprite":"flag_mount_socket","anchor":"flag_mount","sizePx":[20,20]},
      {"sprite":f"flag_pennant_topdown_{flag:02d}","anchor":"flag_mount","offsetPx":[11,0],"sizePx":[70,38],"pivot":[0,.5]},
      {"sprite":"lantern_housing_topdown","anchor":"lantern_mount","sizePx":[38,38]},
      {"sprite":f"lantern_glow_topdown_{glow_frame:02d}","anchor":"lantern_mount","sizePx":[28,28]},
      {"sprite":"crossbow_rotatable","anchor":"weapon_socket","offsetPx":[-recoil,0],"sizePx":[176,144],"rotation":"aimAngle"},
    ]
    if flash: layers.append({"sprite":f"muzzle_flash_{flash:02d}","anchor":"muzzle","offsetPx":[-recoil,0],"sizePx":[42,42],"pivot":[0,.5],"rotation":"aimAngle"})
    return layers


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    parts=source_parts()
    parts["flag_mount_socket"]=flag_socket()
    parts["lantern_housing_topdown"]=lantern_housing()
    for i in range(4):
        parts[f"flag_pennant_topdown_{i+1:02d}"]=pennant(i)
        parts[f"lantern_glow_topdown_{i+1:02d}"]=glow(i)
    layer_dir=OUT/"layers"; layer_dir.mkdir(exist_ok=True)
    for name,image in parts.items(): image.save(layer_dir/f"{name}.png",optimize=True)
    atlas,sprites=pack(parts)
    for name in sprites: sprites[name]["file"]=f"layers/{name}.png"
    atlas_path=OUT/"watchtower_layered_runtime_v3.png"; atlas.save(atlas_path,optimize=True)
    idle=[{"durationMs":180,"layers":intact_layers(i,i)} for i in (1,2,3,4)]
    attack=[{"durationMs":90,"layers":intact_layers(i,i,i,[0,5,9,3][i-1])} for i in (1,2,3,4)]
    destroy=[{"durationMs":130,"layers":intact_layers(1,1)}]
    debris=[n for n in parts if n.startswith("destroy_debris_")]
    for phase in range(1,5):
        layers=[]
        for i,name in enumerate(debris):
            angle=math.tau*i/len(debris)+.31; radius=18+phase*25
            layers.append({"sprite":name,"anchor":"object_center","offsetPx":[round(math.cos(angle)*radius),round(math.sin(angle)*radius)],"sizePx":[round(34-phase*3),round(34-phase*3)],"rotationDeg":(i%3-1)*phase*13})
        destroy.append({"durationMs":130,"layers":layers})
    actions={"idle":{"loop":True,"frames":idle},"attack":{"loop":False,"frames":attack},"destroy":{"loop":False,"holdLast":True,"frames":destroy},"projectile":{"loop":False,"frames":[{"durationMs":0,"layers":[{"sprite":"projectile_bolt","anchor":"object_center","sizePx":[82,50],"rotation":"trajectoryAngle"}]}]}}
    action_dir=OUT/"actions";action_dir.mkdir(exist_ok=True)
    for name,data in actions.items(): (action_dir/f"{name}.json").write_text(json.dumps({"object":"watchtower","action":name,**data},ensure_ascii=False,indent=2)+"\n")
    manifest={
      "schemaVersion":3,"object":"watchtower","pipeline":"layered-object-v3-runtime-composition","image":atlas_path.name,"atlasSize":list(atlas.size),"sprites":sprites,
      "coordinateSystem":"local 384x384; origin top-left; +x right; +y down; exact 90-degree top-down",
      "anchors":{"object_center":[192,192],"weapon_socket":[192,192],"flag_mount":[132,122],"lantern_mount":[132,258],"muzzle":[286,192]},
      "drawOrder":["base","socket","flag_mount","flag_pennant","lantern_housing","lantern_glow","weapon","muzzle_fx"],
      "actionFiles":{name:f"actions/{name}.json" for name in actions},"actions":actions,
      "qa":{"bakedCompositeFrames":False,"allRuntimeSpritesNamed":True,"singleProjection":"true-top-down-orthographic","discardedSourceLayers":["flag_pole","flag_cloth_wind_*","lantern_body","lantern_flame_*"],"reason":"source layers were side/elevation view"}
    }
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"atlas":str(atlas_path),"size":atlas.size,"bytes":atlas_path.stat().st_size,"sprites":len(sprites)},indent=2))

if __name__=="__main__": main()

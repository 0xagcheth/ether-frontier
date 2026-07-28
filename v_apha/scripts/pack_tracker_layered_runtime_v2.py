#!/usr/bin/env python3
"""Pack Tracker and inherited fortress/Ranger layers into one runtime atlas."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import checker


ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "assets/approved/canon/modules/tracker"
RANGER = ROOT / "assets/approved/canon/modules/ranger"
WATCH_RUNTIME = ROOT / "assets/approved/runtime/watchtower"
OUT = ROOT / "assets/approved/runtime/tracker"
REVIEW = ROOT / "assets/staging/reviews/tracker"
ATLAS_SIZE = (1024, 1024)
PAD = 4
BASE_FOOTPRINT = 512


def load(path):
    return json.loads(path.read_text())


def trim(image):
    box = image.getchannel("A").point(lambda a: 255 if a > 5 else 0).getbbox()
    if not box:
        raise RuntimeError("empty sprite")
    return image.crop(box), box


def resized(image, width):
    return image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)


def scrub_chroma(image):
    pixels = []
    removed = 0
    for r, g, b, a in image.getdata():
        if a > 0 and r > 135 and b > 115 and g < 125 and r-g > 45 and b-g > 35:
            pixels.append((r, g, b, 0)); removed += 1
        else:
            pixels.append((r, g, b, a))
    image.putdata(pixels)
    return image, removed


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    sprites = []
    chroma_removed = 0

    def add_image(sprite_id, path, width, pivot_src, draw, semantic, duration=None, source_size=None, trim_offset=None, local_rotation=0):
        nonlocal chroma_removed
        original = Image.open(path).convert("RGBA")
        scaled = resized(original, width)
        scaled, removed = scrub_chroma(scaled); chroma_removed += removed
        sx, sy = scaled.width / original.width, scaled.height / original.height
        if source_size:
            source_scaled = [round(source_size[0] * sx), round(source_size[1] * sy)]
            offset_scaled = [round(trim_offset[0] * sx), round(trim_offset[1] * sy)]
            pivot_full = [round((pivot_src[0] + trim_offset[0]) * sx), round((pivot_src[1] + trim_offset[1]) * sy)]
        else:
            source_scaled = list(scaled.size); offset_scaled = [0, 0]
            pivot_full = [round(pivot_src[0] * sx), round(pivot_src[1] * sy)]
        cropped, box = trim(scaled)
        offset_scaled = [offset_scaled[0] + box[0], offset_scaled[1] + box[1]]
        pivot = [pivot_full[0] - offset_scaled[0], pivot_full[1] - offset_scaled[1]]
        rec = {"id": sprite_id, "image": cropped, "pivotPx": pivot, "pivotInSourcePx": pivot_full,
               "sourceSize": source_scaled, "trimOffset": offset_scaled, "drawOrder": draw,
               "semantic": semantic, "localRotationDeg": local_rotation}
        if duration is not None:
            rec["durationMs"] = duration
        sprites.append(rec)

    watch = load(WATCH_RUNTIME / "watchtower_layered_manifest_v2.json")
    watch_atlas = Image.open(WATCH_RUNTIME / watch["image"]).convert("RGBA")
    def add_watch(sprite_id):
        nonlocal chroma_removed
        wm = watch["sprites"][sprite_id]; r = wm["rect"]
        image = watch_atlas.crop((r["x"], r["y"], r["x"]+r["w"], r["y"]+r["h"]))
        image, removed = scrub_chroma(image); chroma_removed += removed
        rec = {"id": sprite_id, "image": image, "pivotPx": wm["pivotPx"],
               "pivotInSourcePx": wm["pivotInSourcePx"], "sourceSize": wm["sourceSize"],
               "trimOffset": wm["trimOffset"], "drawOrder": wm["drawOrder"],
               "semantic": wm["semantic"], "localRotationDeg": 0}
        if "durationMs" in wm: rec["durationMs"] = wm["durationMs"]
        sprites.append(rec)

    inherited = ["base_stone_token", "central_socket", "lantern_body"] + [f"lantern_flame_{i:02d}" for i in range(1,5)] + ["destroy_debris_stone_a", "destroy_debris_stone_b", "destroy_debris_stone_c"] + [f"destroy_dust_{i:02d}" for i in range(1,5)] + [f"destroy_sparks_{i:02d}" for i in range(1,5)]
    for sid in inherited: add_watch(sid)

    weapon = load(TRACKER / "tracker__active_primary__long_range_crossbow_v1.json")
    weapon_w = round(BASE_FOOTPRINT * weapon["runtimeScale"]["scaleToBaseFootprint"])
    add_image("long_range_crossbow", TRACKER / weapon["image"], weapon_w, weapon["pivotPx"], 30, "active_primary")
    ring = load(TRACKER / "tracker__aim_child__scan_optics_ring_v1.json")
    add_image("scan_optics_ring", TRACKER / ring["image"], round(weapon_w * ring["runtimeScale"]["widthToParentWeapon"]), ring["pivotPx"], 32, "aim_child")
    crown = load(TRACKER / "tracker__identity_child__crown_trim_v1.json")
    add_image("crown_trim", TRACKER / crown["image"], round(BASE_FOOTPRINT * crown["runtimeScale"]["scaleToBaseFootprint"]), crown["pivotPx"], 16, "identity_child")
    mag = load(RANGER / "ranger__ammo_child__bolt_magazine_v1.json")
    add_image("bolt_magazine", RANGER / mag["image"], round(weapon_w * mag["runtimeScale"]["widthToParentWeapon"]), mag["pivotPx"], 33, "ammo_child", local_rotation=90)
    bolt = load(RANGER / "ranger__projectile__barbed_bolt_v1.json")
    bolt_w = round(weapon_w * bolt["runtimeScale"]["lengthToParentWeapon"])
    add_image("barbed_bolt", RANGER / bolt["image"], bolt_w, bolt["pivotPx"], 40, "projectile")
    flash = load(RANGER / "ranger__muzzle_fx__rapid_flash_loop_v1.json")
    flash_w = round(weapon_w * flash["attachment"]["scaleToWeaponLength"])
    for i, f in enumerate(flash["frames"], 1):
        add_image(f"rapid_flash_{i:02d}", RANGER / f["image"], flash_w, f["pivotPx"], 50, "attack_fx", f["durationMs"])
    impact = load(RANGER / "ranger__impact_fx__barbed_hit_v1.json")
    impact_w = round(bolt_w * impact["attachment"]["scaleToProjectileLength"])
    for i, f in enumerate(impact["frames"], 1):
        add_image(f"barbed_hit_{i:02d}", RANGER / f["image"], impact_w, f["pivotPx"], 55, "impact_fx", f["durationMs"])
    rune = load(TRACKER / "tracker__targeting_fx__rune_loop_v1.json")
    rune_canvas_w = round(BASE_FOOTPRINT * rune["runtimeScale"]["scaleToBaseFootprint"])
    for i, f in enumerate(rune["frames"], 1):
        visible_w = round(f["sizePx"][0] * rune_canvas_w / f["sourceSize"][0])
        add_image(f"targeting_rune_{i:02d}", TRACKER / f["image"], visible_w, f["pivotPx"], 31, "targeting_fx", f["durationMs"], f["sourceSize"], f["trimOffset"])

    base = next(s for s in sprites if s["id"] == "base_stone_token")
    base["packedRect"] = {"x": PAD, "y": PAD, "w": base["image"].width, "h": base["image"].height}
    free = [[PAD+base["image"].width+PAD, PAD, ATLAS_SIZE[0]-(PAD+base["image"].width+PAD)-PAD, base["image"].height],
            [PAD, PAD+base["image"].height+PAD, ATLAS_SIZE[0]-PAD*2, ATLAS_SIZE[1]-(PAD+base["image"].height+PAD)-PAD]]
    for s in sorted([s for s in sprites if s is not base], key=lambda s: max(s["image"].size), reverse=True):
        w, h = s["image"].size
        choices = [(max(fr[2]-w, fr[3]-h), idx, fr) for idx, fr in enumerate(free) if w <= fr[2] and h <= fr[3]]
        if not choices: raise RuntimeError(f"atlas overflow at {s['id']} {w}x{h}")
        _, idx, (x, y, fw, fh) = min(choices); free.pop(idx)
        s["packedRect"] = {"x": x, "y": y, "w": w, "h": h}
        right = [x+w+PAD, y, fw-w-PAD, h]; bottom = [x, y+h+PAD, fw, fh-h-PAD]
        if right[2] > 0 and right[3] > 0: free.append(right)
        if bottom[2] > 0 and bottom[3] > 0: free.append(bottom)

    atlas = Image.new("RGBA", ATLAS_SIZE, (0,0,0,0))
    for s in sprites: atlas.alpha_composite(s["image"], (s["packedRect"]["x"], s["packedRect"]["y"]))
    atlas_path = OUT / "tracker_layered_runtime_v2.png"; atlas.save(atlas_path, optimize=True)
    byid = {s["id"]: s for s in sprites}
    def clip(prefix, loop):
        arr = sorted([s for s in sprites if s["id"].startswith(prefix)], key=lambda s:s["id"])
        return {"frames":[s["id"] for s in arr], "durationsMs":[s.get("durationMs",180) for s in arr], "loop":loop, "holdLast":False}
    manifest = {"schemaVersion":2,"object":"tracker","family":"fortress_ranged","pipeline":"layered_object_v2","image":atlas_path.name,
      "atlasSize":list(ATLAS_SIZE),"baseFootprintPx":BASE_FOOTPRINT,"projection":"true_top_down_orthographic_90deg","sprites":{},
      "attachments":{"objectCenter":{"parent":"base_stone_token","positionNormalized":[.5,.5]},"weaponSocket":{"parent":"central_socket","positionNormalized":[.5,.5]},
       "magazineSocket":{"parent":"long_range_crossbow","positionNormalized":weapon["attachments"]["magazine_socket"]["positionNormalized"],"localRotationDeg":90},
       "scanRingSocket":{"parent":"long_range_crossbow","positionNormalized":weapon["attachments"]["scan_ring_socket"]["positionNormalized"]},
       "muzzle":{"parent":"long_range_crossbow","positionNormalized":weapon["attachments"]["muzzle_anchor"]["positionNormalized"],"forwardAxis":"+X"},
       "lantern":{"parent":"base_stone_token","positionNormalized":[.29,.72]},"lanternGlow":{"parent":"lantern_body","positionNormalized":[.5,.5]},
       "crownTrim":{"parent":"base_stone_token","positionNormalized":crown["attachments"]["parent"]["positionNormalized"]}},
      "drawOrder":["base_stone_token","central_socket","crown_trim","lantern_body","lantern_flame_*","long_range_crossbow","targeting_rune_*","scan_optics_ring","bolt_magazine","barbed_bolt","rapid_flash_*","barbed_hit_*","destroy_debris_stone_*","destroy_dust_*","destroy_sparks_*"],
      "animations":{"idle_lantern":clip("lantern_flame_",True),"targeting_scan":clip("targeting_rune_",True),"attack":clip("rapid_flash_",False),"impact":clip("barbed_hit_",False),"destroy_dust":clip("destroy_dust_",False),"destroy_sparks":clip("destroy_sparks_",False)},
      "runtimeTransforms":{"long_range_crossbow":{"rotation":"aimAngle","anchor":"weaponSocket"},"targeting_rune_*":{"anchor":"scanRingSocket","inheritRotation":True},"scan_optics_ring":{"anchor":"scanRingSocket","rotation":"aimAngle + scanAngle"},"bolt_magazine":{"anchor":"magazineSocket","inheritRotation":True,"localRotationDeg":90},"barbed_bolt":{"position":"projectilePosition","rotation":"trajectoryAngle"},"rapid_flash_*":{"anchor":"muzzle","inheritRotation":True},"barbed_hit_*":{"position":"impactPosition"},"crown_trim":{"anchor":"crownTrim"}},
      "sourceManifests":[p.name for p in sorted(TRACKER.glob("*.json"))]+["ranger__ammo_child__bolt_magazine_v1.json","ranger__projectile__barbed_bolt_v1.json","ranger__muzzle_fx__rapid_flash_loop_v1.json","ranger__impact_fx__barbed_hit_v1.json"],"qa":{}}
    for s in sprites:
        rec={"rect":s["packedRect"],"pivotPx":s["pivotPx"],"pivotInSourcePx":s["pivotInSourcePx"],"sourceSize":s["sourceSize"],"trimOffset":s["trimOffset"],"drawOrder":s["drawOrder"],"semantic":s["semantic"]}
        if s.get("durationMs") is not None: rec["durationMs"] = s["durationMs"]
        if s.get("localRotationDeg"): rec["localRotationDeg"] = s["localRotationDeg"]
        manifest["sprites"][s["id"]] = rec
    rects=[s["packedRect"] for s in sprites];overlaps=0
    for i,a in enumerate(rects):
        for b in rects[i+1:]:
            if a["x"]<b["x"]+b["w"] and a["x"]+a["w"]>b["x"] and a["y"]<b["y"]+b["h"] and a["y"]+a["h"]>b["y"]: overlaps+=1
    spill=sum(1 for r,g,b,a in atlas.getdata() if a>18 and r>150 and b>130 and g<115 and min(r-g,b-g)>55)
    manifest["qa"]={"spriteCount":len(sprites),"rectsInBounds":all(r["x"]>=0 and r["y"]>=0 and r["x"]+r["w"]<=ATLAS_SIZE[0] and r["y"]+r["h"]<=ATLAS_SIZE[1] for r in rects),"rectOverlapCount":overlaps,"magentaSpillPixels":spill,"chromaRemovedPixels":chroma_removed,"runtimeLabels":False,"atlasBytes":atlas_path.stat().st_size,"under5MB":atlas_path.stat().st_size<5_000_000,"status":"approved"}
    manifest_path=OUT/"tracker_layered_manifest_v2.json";manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")

    tile,header,cols=180,32,6;rows=(len(sprites)+cols-1)//cols
    grid=Image.new("RGB",(tile*cols,(tile+header)*rows),"#292a2b");font=ImageFont.load_default()
    for i,s in enumerate(sorted(sprites,key=lambda x:(x["drawOrder"],x["id"]))):
        col,row=i%cols,i//cols;panel=checker((tile,tile),16);scale=min(164/s["image"].width,164/s["image"].height);im=s["image"].resize((max(1,round(s["image"].width*scale)),max(1,round(s["image"].height*scale))),Image.Resampling.LANCZOS);panel.alpha_composite(im,((tile-im.width)//2,(tile-im.height)//2));grid.paste(panel.convert("RGB"),(col*tile,row*(tile+header)+header));ImageDraw.Draw(grid).text((col*tile+7,row*(tile+header)+10),s["id"][:26],font=font,fill="#f3ead3")
    review_path=REVIEW/"tracker_layered_review_grid_v2.png";grid.save(review_path,optimize=True)

    comp=Image.new("RGBA",(720,720),(0,0,0,0));center=(360,360)
    def paste(sid,point,rotation=0):
        s=byid[sid];im=s["image"];p=s["pivotPx"]
        if rotation:
            layer=Image.new("RGBA",comp.size,(0,0,0,0));layer.alpha_composite(im,(round(point[0]-p[0]),round(point[1]-p[1])));comp.alpha_composite(layer.rotate(-rotation,Image.Resampling.BICUBIC,center=point))
        else: comp.alpha_composite(im,(round(point[0]-p[0]),round(point[1]-p[1])))
    def base_point(norm): return (center[0]+round((norm[0]-.5)*512),center[1]+round((norm[1]-.5)*512))
    paste("base_stone_token",center);paste("central_socket",center);paste("crown_trim",base_point(crown["attachments"]["parent"]["positionNormalized"]));lantern=base_point((.29,.72));paste("lantern_body",lantern);paste("lantern_flame_03",lantern);paste("long_range_crossbow",center);paste("targeting_rune_03",center);paste("scan_optics_ring",center);ws=byid["long_range_crossbow"];wp=ws["pivotInSourcePx"]
    def weapon_point(norm): return (center[0]+round(norm[0]*ws["sourceSize"][0]-wp[0]),center[1]+round(norm[1]*ws["sourceSize"][1]-wp[1]))
    paste("bolt_magazine",weapon_point(manifest["attachments"]["magazineSocket"]["positionNormalized"]),90)
    comp_path=REVIEW/"tracker_layered_composite_preview_v2.png";comp.save(comp_path,optimize=True)
    print(json.dumps({"atlas":str(atlas_path.relative_to(ROOT)),"manifest":str(manifest_path.relative_to(ROOT)),"atlasSize":list(ATLAS_SIZE),"atlasBytes":atlas_path.stat().st_size,"under5MB":manifest["qa"]["under5MB"],"spriteCount":len(sprites),"rectsInBounds":manifest["qa"]["rectsInBounds"],"rectOverlapCount":overlaps,"magentaSpillPixels":spill,"reviewGrid":str(review_path.relative_to(ROOT)),"compositePreview":str(comp_path.relative_to(ROOT))},indent=2))


if __name__=="__main__": main()

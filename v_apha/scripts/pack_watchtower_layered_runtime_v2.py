#!/usr/bin/env python3
"""Pack all approved Watchtower modules into one tight production runtime atlas."""

from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
OUT = ROOT / "assets/approved/runtime/watchtower"
REVIEW = ROOT / "assets/staging/reviews/watchtower"
IDLE_PREVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged/watchtower__range_pennant_wind_loop_v1_idle_preview.gif"
ATLAS_NAME = "watchtower_layered_runtime_v2.png"
MANIFEST_NAME = "watchtower_layered_manifest_v2.json"
BASE_FOOTPRINT = 512
PADDING = 4


def load_json(name: str) -> dict:
    return json.loads((CANON / name).read_text())


def tight_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    value = image.getchannel("A").point(lambda a: 255 if a > 4 else 0).getbbox()
    if not value:
        raise RuntimeError("empty runtime sprite")
    return value


def next_pow2(value: int) -> int:
    return 1 << max(0, value - 1).bit_length()


def checker(size: tuple[int, int], cell: int = 16) -> Image.Image:
    out = Image.new("RGB", size, "#d9d1bd")
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x+cell-1, y+cell-1), fill="#c8bea7")
    return out.convert("RGBA")


def remove_runtime_magenta(image: Image.Image) -> Image.Image:
    """Remove residual key-colored fringe exposed by runtime downsampling."""
    cleaned = image.copy()
    pixels = []
    for r, g, b, a in cleaned.getdata():
        if a > 0 and r > 165 and b > 145 and g < 125 and min(r-g, b-g) > 55:
            pixels.append((r, g, b, 0))
        else:
            pixels.append((r, g, b, a))
    cleaned.putdata(pixels)
    return cleaned


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    sprites: list[dict] = []

    def add(sprite_id: str, image_name: str, desired_size: tuple[int, int], pivot_source: list[int],
            draw_order: int, semantic: str, duration: int | None = None) -> None:
        source = Image.open(CANON / image_name).convert("RGBA")
        runtime_full = remove_runtime_magenta(source.resize(desired_size, Image.Resampling.LANCZOS))
        box = tight_bbox(runtime_full)
        trimmed = runtime_full.crop(box)
        scale_x, scale_y = desired_size[0] / source.width, desired_size[1] / source.height
        pivot_in_source = [round(pivot_source[0] * scale_x), round(pivot_source[1] * scale_y)]
        pivot_trimmed = [pivot_in_source[0] - box[0], pivot_in_source[1] - box[1]]
        sprites.append({"id": sprite_id, "image": trimmed, "sourceImage": image_name,
            "sourceSize": list(desired_size), "trimOffset": [box[0], box[1]],
            "pivotPx": pivot_trimmed, "pivotInSourcePx": pivot_in_source,
            "drawOrder": draw_order, "semantic": semantic, "durationMs": duration})

    base = load_json("fortress_ranged__base_token__round_light_v1.json")
    base_scale = BASE_FOOTPRINT / base["footprintPx"]
    add("base_stone_token", base["image"],
        (round(base["sizePx"][0]*base_scale), round(base["sizePx"][1]*base_scale)),
        base["pivotPx"], 0, "base_token")

    socket = load_json("fortress_ranged__center_socket__light_bearing_v1.json")
    socket_w = round(BASE_FOOTPRINT * socket["attachment"]["scaleToParentFootprint"])
    add("central_socket", socket["image"], (socket_w, round(socket["sizePx"][1]*socket_w/socket["sizePx"][0])),
        socket["pivotPx"], socket["drawOrder"], "center_socket")

    housing = load_json("fortress_ranged__ambient_child__amber_lantern_housing_v1.json")
    housing_w = round(BASE_FOOTPRINT * housing["attachments"]["parent"]["scaleToParentFootprint"])
    add("lantern_body", housing["image"], (housing_w, round(housing["sizePx"][1]*housing_w/housing["sizePx"][0])),
        housing["pivotPx"], housing["drawOrder"], "ambient_child")

    glow = load_json("fortress_ranged__ambient_child__amber_lantern_glow_loop_v1.json")
    glow_canvas = round(housing_w * glow["attachment"]["scaleToParentFootprint"])
    for frame in glow["frames"]:
        add(f"lantern_flame_{frame['id'][-2:]}", frame["image"], (glow_canvas, glow_canvas),
            frame["pivotPx"], glow["drawOrder"], "ambient_animation", frame["durationMs"])

    crossbow = load_json("watchtower__active_addon__light_single_crossbow_v1.json")
    crossbow_w = round(BASE_FOOTPRINT * crossbow["attachments"]["parent"]["scaleToBaseFootprint"])
    crossbow_h = round(crossbow["sizePx"][1] * crossbow_w / crossbow["sizePx"][0])
    add("crossbow_rotatable", crossbow["image"], (crossbow_w, crossbow_h),
        crossbow["pivotPx"], crossbow["drawOrder"], "active_addon")

    projectile = load_json("watchtower__projectile__simple_bolt_v1.json")
    projectile_w = round(crossbow_w * projectile["runtimeTransform"]["scaleToWeaponLength"])
    add("projectile_bolt", projectile["image"],
        (projectile_w, round(projectile["sizePx"][1]*projectile_w/projectile["sizePx"][0])),
        projectile["pivotPx"], projectile["drawOrder"], "projectile")

    muzzle = load_json("watchtower__muzzle_fx__compact_golden_flash_loop_v1.json")
    muzzle_w = round(crossbow_w * muzzle["attachment"]["scaleToWeaponLength"])
    muzzle_h = round(muzzle["frames"][0]["rect"]["h"] * muzzle_w / muzzle["frames"][0]["rect"]["w"])
    for frame in muzzle["frames"]:
        add(f"muzzle_flash_{frame['id'][-2:]}", frame["image"], (muzzle_w, muzzle_h),
            frame["pivotPx"], muzzle["drawOrder"], "attack_fx", frame["durationMs"])

    mount = load_json("watchtower__flag_mount__range_pennant_socket_v1.json")
    mount_w = round(BASE_FOOTPRINT * mount["attachments"]["parent"]["scaleToBaseFootprint"])
    add("flag_pole", mount["image"], (mount_w, round(mount["sizePx"][1]*mount_w/mount["sizePx"][0])),
        mount["pivotPx"], mount["drawOrder"], "flag_mount")

    pennant = load_json("watchtower__ambient_child__range_pennant_wind_loop_v1.json")
    pennant_w = round(BASE_FOOTPRINT * pennant["attachment"]["scaleToBaseFootprint"])
    pennant_h = round(pennant["frames"][0]["rect"]["h"] * pennant_w / pennant["frames"][0]["rect"]["w"])
    for frame in pennant["frames"]:
        add(f"flag_cloth_wind_{frame['id'][-2:]}", frame["image"], (pennant_w, pennant_h),
            frame["pivotPx"], pennant["drawOrder"], "ambient_animation", frame["durationMs"])

    debris_names = [
        "fortress_ranged__debris__stone_rim_chunk_a_v1.json",
        "fortress_ranged__debris__stone_rim_chunk_b_v1.json",
        "fortress_ranged__debris__stone_core_chunk_c_v1.json",
        "watchtower__debris__crossbow_arm_shard_d_v1.json",
        "watchtower__debris__crossbow_axle_bracket_e_v1.json",
    ]
    debris_ids = ["destroy_debris_stone_a", "destroy_debris_stone_b", "destroy_debris_stone_c",
                  "destroy_debris_wood_d", "destroy_debris_metal_e"]
    debris_physics = {}
    for sprite_id, name in zip(debris_ids, debris_names):
        meta = load_json(name)
        if "scaleToBaseFootprint" in meta["runtimeScale"]:
            width = round(BASE_FOOTPRINT * meta["runtimeScale"]["scaleToBaseFootprint"])
        else:
            width = round(crossbow_w * meta["runtimeScale"]["scaleToWeaponLength"])
        add(sprite_id, meta["image"], (width, round(meta["sizePx"][1]*width/meta["sizePx"][0])),
            meta["pivotPx"], meta["drawOrder"], "destroy_debris")
        debris_physics[sprite_id] = meta["destroyPhysics"]

    dust = load_json("watchtower__destroy_fx__stone_dust_burst_v1.json")
    dust_canvas = round(BASE_FOOTPRINT * dust["attachment"]["scaleToBaseFootprint"])
    for frame in dust["frames"]:
        add(f"destroy_dust_{frame['id'][-2:]}", frame["image"], (dust_canvas, dust_canvas),
            frame["pivotPx"], dust["drawOrder"], "destroy_fx", frame["durationMs"])

    sparks = load_json("watchtower__destroy_fx__metal_spark_burst_v1.json")
    spark_canvas = round(crossbow_w * sparks["attachment"]["scaleToParentLength"])
    for frame in sparks["frames"]:
        add(f"destroy_sparks_{frame['id'][-2:]}", frame["image"], (spark_canvas, spark_canvas),
            frame["pivotPx"], sparks["drawOrder"], "destroy_fx", frame["durationMs"])

    # Shelf-pack largest sprites first; only the tight trimmed images enter runtime.
    atlas_width = 1024
    ordered = sorted(sprites, key=lambda s: (-s["image"].height, -s["image"].width, s["id"]))
    x = y = PADDING
    row_h = 0
    for sprite in ordered:
        image = sprite["image"]
        if x + image.width + PADDING > atlas_width:
            x = PADDING
            y += row_h + PADDING
            row_h = 0
        sprite["packedRect"] = {"x": x, "y": y, "w": image.width, "h": image.height}
        x += image.width + PADDING
        row_h = max(row_h, image.height)
    atlas_height = next_pow2(y + row_h + PADDING)
    if atlas_height > 2048:
        raise RuntimeError(f"unexpected atlas height {atlas_height}")
    atlas = Image.new("RGBA", (atlas_width, atlas_height), (0,0,0,0))
    for sprite in ordered:
        rect = sprite["packedRect"]
        atlas.alpha_composite(sprite["image"], (rect["x"], rect["y"]))
    atlas_path = OUT / ATLAS_NAME
    atlas.save(atlas_path, optimize=True)

    sprite_records = {}
    for sprite in sprites:
        record = {"rect": sprite["packedRect"], "pivotPx": sprite["pivotPx"],
            "pivotInSourcePx": sprite["pivotInSourcePx"], "sourceSize": sprite["sourceSize"],
            "trimOffset": sprite["trimOffset"], "drawOrder": sprite["drawOrder"],
            "semantic": sprite["semantic"]}
        if sprite["durationMs"] is not None:
            record["durationMs"] = sprite["durationMs"]
        sprite_records[sprite["id"]] = record

    def clip(prefix: str, loop: bool, hold: bool = False) -> dict:
        ids = [f"{prefix}_{i:02d}" for i in range(1,5)]
        return {"frames": ids, "durationsMs": [sprite_records[i]["durationMs"] for i in ids],
                "loop": loop, "holdLast": hold}

    manifest = {"schemaVersion": 2, "object": "watchtower", "family": "fortress_ranged",
        "pipeline": "layered_object_v2", "image": ATLAS_NAME,
        "atlasSize": [atlas_width, atlas_height], "baseFootprintPx": BASE_FOOTPRINT,
        "projection": "true_top_down_orthographic_90deg", "sprites": sprite_records,
        "attachments": {
            "objectCenter": {"parent": "base_stone_token", "positionNormalized": [0.5,0.5]},
            "weaponSocket": {"parent": "central_socket", "positionNormalized": [0.5,0.5]},
            "muzzle": {"parent": "crossbow_rotatable", "positionNormalized": crossbow["attachments"]["muzzle_anchor"]["positionNormalized"], "forwardAxis": "+X"},
            "flagMount": {"parent": "base_stone_token", "positionNormalized": mount["attachments"]["parent"]["positionNormalized"]},
            "flagCloth": {"parent": "flag_pole", "positionNormalized": mount["attachments"]["cloth_anchor"]["positionNormalized"], "forwardAxis": "+X"},
            "lantern": {"parent": "base_stone_token", "positionNormalized": housing["attachments"]["parent"]["positionNormalized"]},
            "lanternGlow": {"parent": "lantern_body", "positionNormalized": [0.5,0.5]},
        },
        "drawOrder": ["base_stone_token", "central_socket", "flag_pole", "flag_cloth_wind_*",
            "lantern_body", "lantern_flame_*", "crossbow_rotatable", "projectile_bolt",
            "muzzle_flash_*", "destroy_debris_*", "destroy_dust_*", "destroy_sparks_*"],
        "animations": {"idle_flag": clip("flag_cloth_wind", True),
            "idle_lantern": clip("lantern_flame", True), "attack": clip("muzzle_flash", False),
            "destroy_dust": clip("destroy_dust", False), "destroy_sparks": clip("destroy_sparks", False)},
        "runtimeTransforms": {"crossbow_rotatable": {"rotation": "aimAngle", "anchor": "weaponSocket"},
            "projectile_bolt": {"position": "projectilePosition", "rotation": "trajectoryAngle"},
            "flag_cloth_wind_*": {"anchor": "flagCloth"}, "lantern_flame_*": {"anchor": "lanternGlow"},
            "muzzle_flash_*": {"anchor": "muzzle", "inheritRotation": True},
            "destroy_debris": debris_physics},
        "sourceManifests": sorted(p.name for p in CANON.glob("*.json")),
        "qa": {"oneObjectFamily": True, "spriteCount": len(sprites), "tightRects": True,
            "transparentRuntime": True, "runtimeLabels": False, "runtimeGrid": False,
            "rectsInBounds": True, "rectsNonOverlapping": True,
            "fileSizeBytes": atlas_path.stat().st_size,
            "under5MB": atlas_path.stat().st_size < 5_000_000, "status": "approved_candidate"}}
    manifest_path = OUT / MANIFEST_NAME
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    # Human-only review grid.
    cell_w, cell_h, cols = 220, 190, 5
    rows = math.ceil(len(sprites)/cols)
    grid = Image.new("RGB", (cell_w*cols, cell_h*rows), "#292a2b")
    draw = ImageDraw.Draw(grid)
    font = ImageFont.load_default()
    for index, sprite in enumerate(sprites):
        col, row = index % cols, index // cols
        panel = checker((cell_w, cell_h-30), 14)
        image = sprite["image"].copy()
        scale = min((cell_w-24)/image.width, (cell_h-54)/image.height, 1.5)
        preview = image.resize((max(1,round(image.width*scale)), max(1,round(image.height*scale))), Image.Resampling.LANCZOS)
        origin = ((cell_w-preview.width)//2, (cell_h-30-preview.height)//2)
        panel.alpha_composite(preview, origin)
        grid.paste(panel.convert("RGB"), (col*cell_w, row*cell_h+30))
        draw.rectangle((col*cell_w, row*cell_h, (col+1)*cell_w-1, (row+1)*cell_h-1), outline="#68645b", width=1)
        draw.text((col*cell_w+7, row*cell_h+10), sprite["id"][:33], font=font, fill="#f3ead3")
        px = col*cell_w + origin[0] + round(sprite["pivotPx"][0]*scale)
        py = row*cell_h + 30 + origin[1] + round(sprite["pivotPx"][1]*scale)
        draw.line((px-7,py,px+7,py), fill="#e34b46", width=2)
        draw.line((px,py-7,px,py+7), fill="#e34b46", width=2)
    review_path = REVIEW / "watchtower_layered_review_grid_v2.png"
    grid.save(review_path, optimize=True)

    composite = Image.open(IDLE_PREVIEW)
    composite.seek(0)
    composite_path = REVIEW / "watchtower_layered_composite_preview_v2.png"
    composite.convert("RGBA").save(composite_path, optimize=True)

    # Final validation from persisted files.
    parsed = json.loads(manifest_path.read_text())
    rects = list(parsed["sprites"].values())
    for record in rects:
        r = record["rect"]
        assert r["x"] >= 0 and r["y"] >= 0 and r["x"]+r["w"] <= atlas_width and r["y"]+r["h"] <= atlas_height
    values = list(parsed["sprites"].items())
    for i, (_, a) in enumerate(values):
        ar = a["rect"]
        for _, b in values[i+1:]:
            br = b["rect"]
            assert ar["x"]+ar["w"] <= br["x"] or br["x"]+br["w"] <= ar["x"] or ar["y"]+ar["h"] <= br["y"] or br["y"]+br["h"] <= ar["y"]
    print(json.dumps({"atlas": str(atlas_path.relative_to(ROOT)), "manifest": str(manifest_path.relative_to(ROOT)),
        "reviewGrid": str(review_path.relative_to(ROOT)),
        "compositePreview": str(composite_path.relative_to(ROOT)), "atlasSize": [atlas_width,atlas_height],
        "spriteCount": len(sprites), "atlasBytes": atlas_path.stat().st_size,
        "under5MB": atlas_path.stat().st_size < 5_000_000,
        "rectsInBounds": True, "rectsNonOverlapping": True}, indent=2))


if __name__ == "__main__":
    main()

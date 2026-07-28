#!/usr/bin/env python3
"""Build the Watchtower Layered Object Pipeline v2 candidate from its ImageGen sheet."""

from __future__ import annotations

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets/source/watchtower-layered-v2-restart"
CANDIDATE_DIR = ROOT / "assets/staging/candidates/watchtower-layered-v2-restart"
RUNTIME_DIR = ROOT / "assets/runtime/atlases/buildings/watchtower-layered-v2-restart"
REVIEW_DIR = ROOT / "assets/review/watchtower-layered-v2-restart"
SOURCE = SOURCE_DIR / "watchtower_layered_source_alpha.png"
ATLAS_PATH = RUNTIME_DIR / "watchtower_layered_runtime.png"
MANIFEST_PATH = RUNTIME_DIR / "watchtower_layered_manifest.json"
REVIEW_PATH = REVIEW_DIR / "watchtower_layered_review_grid.png"
PREVIEW_PATH = REVIEW_DIR / "watchtower_layered_composite_preview.png"


# Source rectangles are explicit provenance for the approved ImageGen sheet.
REGIONS = {
    "base_stone_token": (35, 18, 415, 395),
    "central_socket": (440, 55, 705, 325),
    "crossbow_rotatable": (765, 35, 1180, 365),
    "flag_pole": (1265, 90, 1395, 300),
    "flag_cloth_wind_01": (112, 395, 355, 560),
    "flag_cloth_wind_02": (450, 395, 725, 560),
    "flag_cloth_wind_03": (805, 395, 1085, 560),
    "flag_cloth_wind_04": (1170, 395, 1480, 560),
    "lantern_body": (40, 570, 210, 775),
    "lantern_flame_01": (275, 590, 365, 745),
    "lantern_flame_02": (405, 600, 500, 745),
    "lantern_flame_03": (530, 605, 615, 745),
    "lantern_flame_04": (650, 620, 735, 745),
    "muzzle_flash_01": (800, 585, 1005, 770),
    "muzzle_flash_02": (995, 590, 1165, 755),
    "muzzle_flash_03": (1160, 605, 1320, 755),
    "muzzle_flash_04": (1310, 625, 1450, 745),
    "projectile_bolt": (35, 785, 290, 855),
    "destroy_debris_01": (30, 865, 170, 1005),
    "destroy_debris_02": (190, 880, 300, 1005),
    "destroy_debris_03": (320, 890, 405, 1005),
    "destroy_debris_04": (415, 825, 500, 1008),
    "destroy_debris_05": (505, 825, 610, 1008),
    "destroy_debris_06": (625, 825, 750, 1008),
    "destroy_debris_07": (760, 825, 920, 1008),
    "destroy_debris_08": (925, 825, 1065, 1008),
    "destroy_debris_09": (1060, 845, 1235, 1008),
    "destroy_debris_10": (1230, 825, 1395, 1008),
    "destroy_debris_11": (1380, 845, 1535, 1008),
}

DRAW_ORDER = {
    "base_stone_token": 0, "central_socket": 10, "crossbow_rotatable": 30,
    "flag_pole": 20, "lantern_body": 20, "projectile_bolt": 40,
}


def trim(image: Image.Image, pad: int = 2) -> tuple[Image.Image, tuple[int, int, int, int]]:
    bbox = image.getchannel("A").getbbox()
    if not bbox:
        raise ValueError("empty sprite")
    x0, y0, x1, y1 = bbox
    x0, y0 = max(0, x0-pad), max(0, y0-pad)
    x1, y1 = min(image.width, x1+pad), min(image.height, y1+pad)
    return image.crop((x0, y0, x1, y1)), (x0, y0, x1, y1)


def keep_largest_component(image: Image.Image, threshold: int = 20) -> Image.Image:
    """Remove isolated ImageGen/keying specks while preserving holes in the main art."""
    alpha = image.getchannel("A")
    width, height = image.size
    pixels = alpha.load()
    seen = set()
    components = []
    for y in range(height):
        for x in range(width):
            if pixels[x, y] <= threshold or (x, y) in seen:
                continue
            stack = [(x, y)]; seen.add((x, y)); component = []
            while stack:
                px, py = stack.pop(); component.append((px, py))
                for nx, ny in ((px-1,py),(px+1,py),(px,py-1),(px,py+1)):
                    if 0 <= nx < width and 0 <= ny < height and (nx,ny) not in seen and pixels[nx,ny] > threshold:
                        seen.add((nx,ny)); stack.append((nx,ny))
            components.append(component)
    if not components:
        return image
    keep = set(max(components, key=len))
    out = image.copy(); out_pixels = out.load()
    for y in range(height):
        for x in range(width):
            if pixels[x,y] > 0 and (x,y) not in keep:
                out_pixels[x,y] = (0,0,0,0)
    return out


def pivot_for(name: str, crop_box: tuple[int, int, int, int], source_box: tuple[int, int, int, int]):
    sx0, sy0, _, _ = source_box
    cx0, cy0, _, _ = crop_box
    if name == "crossbow_rotatable":
        point = (945 - sx0, 198 - sy0)  # axle center on source sheet
    elif name.startswith("flag_cloth"):
        point = (0, (crop_box[3] - crop_box[1]) // 2)
        return point
    elif name == "flag_pole":
        point = (1330 - sx0, 222 - sy0)
    elif name.startswith("muzzle_flash"):
        point = ((crop_box[2] - crop_box[0]) // 2, (crop_box[3] - crop_box[1]) // 2)
        return point
    else:
        point = ((source_box[2]-source_box[0]) // 2, (source_box[3]-source_box[1]) // 2)
    return [round(point[0] - cx0), round(point[1] - cy0)]


def layer_meta(name: str):
    if name.startswith("flag_cloth"):
        return "ambient_child", "flag_pole.cloth_anchor", 25
    if name.startswith("lantern_flame"):
        return "ambient_child", "lantern_body.flame_anchor", 25
    if name.startswith("muzzle_flash"):
        return "attack_fx", "crossbow_rotatable.muzzle_anchor", 40
    if name.startswith("destroy_debris"):
        return "destroy_debris", None, 50
    if name == "projectile_bolt":
        return "projectile", "crossbow_rotatable.muzzle_anchor", 40
    if name == "crossbow_rotatable":
        return "active_rotatable", "central_socket.weapon_anchor", 30
    return "static_child" if name != "base_stone_token" else "base", None, DRAW_ORDER.get(name, 20)


def pack(entries, max_width=1024, gap=4):
    x = y = gap
    row_h = 0
    placements = []
    for entry in sorted(entries, key=lambda e: e["image"].height, reverse=True):
        image = entry["image"]
        if x + image.width + gap > max_width:
            x, y, row_h = gap, y + row_h + gap, 0
        placements.append((entry, x, y))
        x += image.width + gap
        row_h = max(row_h, image.height)
    height = y + row_h + gap
    return placements, (max_width, height)


def checker(size, cell=16):
    out = Image.new("RGBA", size, (45, 48, 54, 255)); draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x//cell + y//cell) % 2:
                draw.rectangle((x, y, x+cell-1, y+cell-1), fill=(65, 69, 76, 255))
    return out


def main():
    for directory in (CANDIDATE_DIR, RUNTIME_DIR, REVIEW_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGBA")
    entries = []
    for name, box in REGIONS.items():
        raw = keep_largest_component(source.crop(box))
        cutout, crop_box = trim(raw)
        pivot = pivot_for(name, crop_box, box)
        semantic, attachment, draw_order = layer_meta(name)
        candidate_path = CANDIDATE_DIR / f"{name}.png"
        cutout.save(candidate_path, optimize=True)
        entries.append({"id": name, "image": cutout, "sourceRect": list(box),
                        "trimRectInSourceRegion": list(crop_box), "pivotPx": pivot,
                        "semantic": semantic, "attachment": attachment,
                        "drawOrder": draw_order})

    placements, atlas_size = pack(entries)
    atlas = Image.new("RGBA", atlas_size, (0, 0, 0, 0))
    sprites = {}
    for entry, x, y in placements:
        image = entry.pop("image")
        atlas.alpha_composite(image, (x, y))
        sprites[entry["id"]] = {k: v for k, v in entry.items() if k != "id"} | {
            "rect": {"x": x, "y": y, "w": image.width, "h": image.height},
            "pivot": [round(entry["pivotPx"][0]/image.width, 6), round(entry["pivotPx"][1]/image.height, 6)],
        }
    atlas.save(ATLAS_PATH, optimize=True)

    manifest = {
        "schemaVersion": 2,
        "object": "watchtower",
        "family": "watchtower",
        "pipeline": "layered-object-v2",
        "status": "rejected",
        "rejectionReasons": [
            "side_or_elevation_projection_in_child_modules",
            "children_do_not_all_read_as_independent_cardboard_cutouts",
            "overloaded_single_imagegen_source_sheet",
            "modular_structure_not_locked_before_generation",
        ],
        "image": ATLAS_PATH.name,
        "atlasSize": {"w": atlas.width, "h": atlas.height},
        "sourceImage": str(SOURCE.relative_to(ROOT)),
        "sprites": sprites,
        "attachments": {
            "base_stone_token.socket_anchor": {"positionPx": [190, 188]},
            "central_socket.weapon_anchor": {"positionPx": sprites["central_socket"]["pivotPx"]},
            "crossbow_rotatable.muzzle_anchor": {"positionPx": [sprites["crossbow_rotatable"]["rect"]["w"]-7, sprites["crossbow_rotatable"]["pivotPx"][1]]},
            "flag_pole.cloth_anchor": {"positionPx": [sprites["flag_pole"]["pivotPx"][0], 40]},
            "lantern_body.flame_anchor": {"positionPx": [sprites["lantern_body"]["pivotPx"][0], 68]},
        },
        "drawOrder": [k for k, _ in sorted(sprites.items(), key=lambda kv: kv[1]["drawOrder"])],
        "animations": {
            "flag_wind": {"frames": [f"flag_cloth_wind_{i:02d}" for i in range(1,5)], "frameDurationMs": 140, "loop": True},
            "lantern_flame": {"frames": [f"lantern_flame_{i:02d}" for i in range(1,5)], "frameDurationMs": 110, "loop": True},
            "attack_flash": {"frames": [f"muzzle_flash_{i:02d}" for i in range(1,5)], "frameDurationMs": 55, "loop": False, "holdLastFrame": False},
            "destroy": {"pieces": [f"destroy_debris_{i:02d}" for i in range(1,12)], "independentBodies": True},
        },
        "runtimeTransforms": {
            "crossbow_rotatable": {"rotationMode": "aimAtTarget", "inheritParentPosition": True},
            "projectile_bolt": {"rotationMode": "velocityDirection"},
        },
        "qa": {
            "runtimeContainsLabels": False, "runtimeContainsGrid": False,
            "runtimeContainsCompositePreview": False, "oneObjectFamilyOnly": True,
            "spriteCount": len(sprites), "rectsInBounds": True,
            "atlasBytes": ATLAS_PATH.stat().st_size,
            "under5MB": ATLAS_PATH.stat().st_size <= 5_000_000,
        },
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n")

    # Human-only QA grid.
    cols, cell_w, cell_h = 4, 360, 285
    rows = (len(entries) + cols - 1) // cols
    grid = checker((cols*cell_w, rows*cell_h), 18)
    draw = ImageDraw.Draw(grid); font = ImageFont.load_default()
    for index, entry in enumerate(entries):
        col, row = index % cols, index // cols
        ox, oy = col*cell_w, row*cell_h
        draw.rectangle((ox, oy, ox+cell_w-1, oy+cell_h-1), outline=(112,118,128,255), width=2)
        draw.text((ox+10, oy+9), entry["id"], fill=(245,238,218,255), font=font)
        image = Image.open(CANDIDATE_DIR / f"{entry['id']}.png").convert("RGBA")
        scale = min((cell_w-28)/image.width, (cell_h-48)/image.height, 1.0)
        shown = image.resize((max(1,round(image.width*scale)), max(1,round(image.height*scale))), Image.Resampling.LANCZOS)
        px, py = ox+(cell_w-shown.width)//2, oy+35+(cell_h-45-shown.height)//2
        grid.alpha_composite(shown, (px, py))
        pivot = entry["pivotPx"]
        cx, cy = px+round(pivot[0]*scale), py+round(pivot[1]*scale)
        draw.line((cx-8,cy,cx+8,cy), fill=(0,255,255,255), width=2)
        draw.line((cx,cy-8,cx,cy+8), fill=(0,255,255,255), width=2)
    grid.save(REVIEW_PATH, optimize=True)

    # Human-only assembled preview; runtime composes the same layers from JSON.
    preview = checker((768, 768), 24)
    center = (384, 390)
    def paste(name, anchor):
        image = Image.open(CANDIDATE_DIR / f"{name}.png").convert("RGBA")
        pivot = sprites[name]["pivotPx"]
        preview.alpha_composite(image, (round(anchor[0]-pivot[0]), round(anchor[1]-pivot[1])))
    paste("base_stone_token", center)
    paste("central_socket", center)
    paste("crossbow_rotatable", center)
    paste("flag_pole", (235, 505)); paste("flag_cloth_wind_02", (235, 505))
    paste("lantern_body", (530, 285)); paste("lantern_flame_02", (530, 285))
    ImageDraw.Draw(preview).text((20, 20), "WATCHTOWER / LAYERED COMPOSITE QA", fill=(245,238,218,255), font=font)
    preview.save(PREVIEW_PATH, optimize=True)

    print(json.dumps({"atlas": str(ATLAS_PATH), "size": atlas_size,
                      "bytes": ATLAS_PATH.stat().st_size, "sprites": len(sprites)}, indent=2))


if __name__ == "__main__":
    main()

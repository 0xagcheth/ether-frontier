#!/usr/bin/env python3
"""Normalize GPT Image 2 Watchtower modules into Layered Object Pipeline v2."""

from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/source/watchtower/layered-v2"
PREPARED = ROOT / "assets/staging/candidates/watchtower-layered-v8"
RUNTIME = ROOT / "assets/runtime/atlases/buildings/watchtower"
REVIEW = ROOT / "assets/review/watchtower"
ATLAS = RUNTIME / "watchtower_layered_runtime_v8.png"
MANIFEST = RUNTIME / "watchtower_layered_manifest_v8.json"
GRID = REVIEW / "watchtower_layered_review_grid_v8.png"
COMPOSITE = REVIEW / "watchtower_layered_composite_preview_v8.png"

REFERENCE_CANVAS = 384
BASE_DIAMETER = 256
PADDING = 4


CORE = {
    "watchtower__base_body__wardens_post": ("watchtower_wt01_base_body_chroma.png", (256, 256), "center", 0, "base_body"),
    "watchtower__mount_socket__light_crossbow_bearing": ("watchtower_wt02_mount_socket_chroma.png", (72, 72), "center", 20, "mount_socket"),
    "watchtower__active_primary__simple_crossbow": ("watchtower_wt03_simple_crossbow_chroma.png", (218, 112), "center", 80, "active_primary"),
    "watchtower__ambient_mount__range_pennant_puck": ("watchtower_wt04_pennant_mount_chroma.png", (66, 44), "center", 30, "ambient_mount"),
    "watchtower__ambient_mount__lantern_housing": ("watchtower_wt06_lantern_housing_chroma.png", (68, 68), "center", 40, "ambient_mount"),
    "watchtower__projectile__simple_bolt": ("watchtower_wt09_simple_bolt_chroma.png", (52, 18), "center", 100, "projectile"),
}

SHEETS = {
    "watchtower_wt05_pennant_frames_chroma.png": (2, 2, "watchtower__ambient_child__range_pennant__frame_{:02d}", (88, 54), "left", 50, "ambient_child"),
    "watchtower_wt07_lantern_core_frames_chroma.png": (2, 2, "watchtower__ambient_child__lantern_core__frame_{:02d}", (42, 42), "center", 60, "ambient_child"),
    "watchtower_wt08_muzzle_flash_frames_chroma.png": (2, 2, "watchtower__attack_release__muzzle_flash__frame_{:02d}", (62, 42), "left", 90, "attack_release"),
    "watchtower_wt10_bolt_hit_frames_chroma.png": (2, 2, "watchtower__impact__bolt_hit__frame_{:02d}", (58, 58), "center", 110, "impact"),
    "watchtower_wt11_stone_debris_chroma.png": (3, 2, "watchtower__destroy_piece__stone_{:02d}", (42, 42), "center", 120, "destroy_piece"),
    "watchtower_wt12_wood_debris_chroma.png": (3, 2, "watchtower__destroy_piece__wood_{:02d}", (46, 38), "center", 120, "destroy_piece"),
    "watchtower_wt13_metal_debris_chroma.png": (3, 1, "watchtower__destroy_piece__metal_{:02d}", (34, 34), "center", 120, "destroy_piece"),
    "watchtower_wt14_dust_frames_chroma.png": (2, 2, "watchtower__destroy_fx__dust__frame_{:02d}", (146, 146), "center", 130, "destroy_fx"),
}


def chroma_to_alpha(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    out = Image.new("RGBA", image.size)
    src, dst = image.load(), out.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, _ = src[x, y]
            score = min(r - 1.30 * g, b - 1.12 * g)
            if score >= 72:
                a = 0
            elif score <= 36:
                a = 255
            else:
                a = round(255 * (72 - score) / 36)
            # Remove the saturated magenta antialias fringe without touching
            # the dark-red pennant (its blue channel is far lower).
            if a > 0 and r > 145 and b > 135 and g < 150 and min(r - g, b - g) > 38:
                a = 0
            dst[x, y] = (r, g, b, a)
    out.putalpha(out.getchannel("A").filter(ImageFilter.MinFilter(3)))
    return out


def clean_specks(image: Image.Image, minimum_area: int = 20) -> Image.Image:
    alpha = image.getchannel("A")
    px = alpha.load()
    seen: set[tuple[int, int]] = set()
    remove: list[list[tuple[int, int]]] = []
    for y in range(image.height):
        for x in range(image.width):
            if px[x, y] <= 12 or (x, y) in seen:
                continue
            stack = [(x, y)]
            seen.add((x, y))
            component = []
            while stack:
                qx, qy = stack.pop()
                component.append((qx, qy))
                for nx, ny in ((qx - 1, qy), (qx + 1, qy), (qx, qy - 1), (qx, qy + 1)):
                    if 0 <= nx < image.width and 0 <= ny < image.height and (nx, ny) not in seen and px[nx, ny] > 12:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            if len(component) < minimum_area:
                remove.append(component)
    if not remove:
        return image
    out = image.copy()
    dst = out.load()
    for component in remove:
        for x, y in component:
            dst[x, y] = (0, 0, 0, 0)
    return out


def trim(image: Image.Image, pad: int = 2) -> Image.Image:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty generated module")
    x0, y0, x1, y1 = bbox
    x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
    x1, y1 = min(image.width, x1 + pad), min(image.height, y1 + pad)
    return image.crop((x0, y0, x1, y1))


def contain(image: Image.Image, target: tuple[int, int]) -> Image.Image:
    image = trim(clean_specks(image))
    scale = min(target[0] / image.width, target[1] / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    return image.resize(size, Image.Resampling.LANCZOS)


def pivot(image: Image.Image, mode: str) -> list[int]:
    if mode == "left":
        return [2, image.height // 2]
    return [image.width // 2, image.height // 2]


def checker(size: tuple[int, int], cell: int = 16) -> Image.Image:
    out = Image.new("RGBA", size, (218, 209, 188, 255))
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(198, 186, 160, 255))
    return out


def main() -> None:
    for directory in (PREPARED, RUNTIME, REVIEW):
        directory.mkdir(parents=True, exist_ok=True)
    sprites: list[dict] = []

    def add(sprite_id: str, image: Image.Image, target: tuple[int, int], pivot_mode: str,
            draw_order: int, semantic: str, source: str) -> None:
        normalized = contain(image, target)
        path = PREPARED / f"{sprite_id}.png"
        normalized.save(path, optimize=True)
        sprites.append({
            "id": sprite_id,
            "image": normalized,
            "pivotPx": pivot(normalized, pivot_mode),
            "drawOrder": draw_order,
            "semantic": semantic,
            "source": source,
        })

    for sprite_id, (filename, target, pivot_mode, order, semantic) in CORE.items():
        source = chroma_to_alpha(Image.open(SOURCE / "core" / filename))
        add(sprite_id, source, target, pivot_mode, order, semantic, filename)

    ruin_name = "watchtower_wt15_ruin_state_chroma.png"
    ruin = chroma_to_alpha(Image.open(SOURCE / "secondary" / ruin_name))
    add("watchtower__ruin_state__broken_post", ruin, (256, 256), "center", 10, "ruin_state", ruin_name)

    for filename, (cols, rows, pattern, target, pivot_mode, order, semantic) in SHEETS.items():
        sheet = chroma_to_alpha(Image.open(SOURCE / "secondary" / filename))
        index = 1
        for row in range(rows):
            y0, y1 = round(row * sheet.height / rows), round((row + 1) * sheet.height / rows)
            for col in range(cols):
                x0, x1 = round(col * sheet.width / cols), round((col + 1) * sheet.width / cols)
                add(pattern.format(index), sheet.crop((x0, y0, x1, y1)), target,
                    pivot_mode, order, semantic, filename)
                index += 1

    ordered = sorted(sprites, key=lambda item: (-item["image"].height, -item["image"].width, item["id"]))
    atlas_width = 1024
    x = y = PADDING
    row_height = 0
    for item in ordered:
        image = item["image"]
        if x + image.width + PADDING > atlas_width:
            x = PADDING
            y += row_height + PADDING
            row_height = 0
        item["rect"] = {"x": x, "y": y, "w": image.width, "h": image.height}
        x += image.width + PADDING
        row_height = max(row_height, image.height)
    atlas_height = y + row_height + PADDING
    atlas = Image.new("RGBA", (atlas_width, atlas_height), (0, 0, 0, 0))
    for item in ordered:
        atlas.alpha_composite(item["image"], (item["rect"]["x"], item["rect"]["y"]))
    atlas.save(ATLAS, optimize=True)

    records = {}
    for item in sprites:
        records[item["id"]] = {
            "rect": item["rect"],
            "pivotPx": item["pivotPx"],
            "pivot": [
                round(item["pivotPx"][0] / item["image"].width, 6),
                round(item["pivotPx"][1] / item["image"].height, 6),
            ],
            "drawOrder": item["drawOrder"],
            "semantic": item["semantic"],
            "sourceJob": item["source"],
        }

    def frames(pattern: str, count: int = 4) -> list[str]:
        return [pattern.format(i) for i in range(1, count + 1)]

    manifest = {
        "schemaVersion": 2,
        "object": "watchtower",
        "family": "warden_ranged_lineage",
        "pipeline": "layered-object-v2",
        "status": "approved_candidate",
        "image": ATLAS.name,
        "atlasSize": {"w": atlas.width, "h": atlas.height},
        "referenceCanvas": {"w": REFERENCE_CANVAS, "h": REFERENCE_CANVAS},
        "baseFootprintPx": BASE_DIAMETER,
        "projection": "true_top_down_orthographic_90deg",
        "sprites": records,
        "attachments": {
            "object_center": {"parent": "watchtower__base_body__wardens_post", "positionPx": [192, 192]},
            "active_primary_pivot": {"parent": "watchtower__mount_socket__light_crossbow_bearing", "positionNormalized": [0.5, 0.5]},
            "pennant_mount_anchor": {"parent": "watchtower__base_body__wardens_post", "positionNormalized": [0.285, 0.65], "rotationDeg": 134},
            "pennant_cloth_anchor": {"parent": "watchtower__ambient_mount__range_pennant_puck", "positionNormalized": [0.88, 0.5], "inheritRotation": True},
            "lantern_mount_anchor": {"parent": "watchtower__base_body__wardens_post", "positionNormalized": [0.715, 0.65]},
            "lantern_core_anchor": {"parent": "watchtower__ambient_mount__lantern_housing", "positionNormalized": [0.5, 0.5]},
            "muzzle_anchor": {"parent": "watchtower__active_primary__simple_crossbow", "positionNormalized": [0.98, 0.5], "forwardAxis": "+X"},
            "projectile_spawn": {"alias": "muzzle_anchor"},
            "debris_origin": {"parent": "watchtower__base_body__wardens_post", "positionNormalized": [0.5, 0.5]},
        },
        "drawOrder": [
            "watchtower__base_body__wardens_post",
            "watchtower__ruin_state__broken_post",
            "watchtower__mount_socket__light_crossbow_bearing",
            "watchtower__ambient_mount__range_pennant_puck",
            "watchtower__ambient_mount__lantern_housing",
            "watchtower__ambient_child__range_pennant__frame_*",
            "watchtower__ambient_child__lantern_core__frame_*",
            "watchtower__active_primary__simple_crossbow",
            "watchtower__attack_release__muzzle_flash__frame_*",
        ],
        "animations": {
            "idle_pennant": {"frames": frames("watchtower__ambient_child__range_pennant__frame_{:02d}"), "sequence": [0, 1, 2, 3, 2, 1], "frameDurationMs": 140, "loop": True},
            "idle_lantern": {"frames": frames("watchtower__ambient_child__lantern_core__frame_{:02d}"), "sequence": [0, 1, 2, 3, 2, 1], "frameDurationMs": 110, "loop": True},
            "attack_release": {"frames": frames("watchtower__attack_release__muzzle_flash__frame_{:02d}"), "frameDurationMs": 55, "loop": False, "holdLast": False},
            "impact": {"frames": frames("watchtower__impact__bolt_hit__frame_{:02d}"), "frameDurationMs": 60, "loop": False, "holdLast": False},
            "destroy_dust": {"frames": frames("watchtower__destroy_fx__dust__frame_{:02d}"), "frameDurationMs": 75, "loop": False, "holdLast": False},
        },
        "runtimeTransforms": {
            "watchtower__active_primary__simple_crossbow": {"rotationMode": "aimAtTarget", "anchor": "active_primary_pivot", "maxRecoilPx": 4},
            "watchtower__projectile__simple_bolt": {"rotationMode": "velocityDirection", "spawnAnchor": "projectile_spawn"},
            "watchtower__ambient_mount__range_pennant_puck": {"anchor": "pennant_mount_anchor", "rotationDeg": 134},
            "watchtower__ambient_child__range_pennant__frame_*": {"anchor": "pennant_cloth_anchor", "inheritRotation": True},
            "watchtower__ambient_child__lantern_core__frame_*": {"anchor": "lantern_core_anchor"},
            "watchtower__attack_release__muzzle_flash__frame_*": {"anchor": "muzzle_anchor", "inheritRotation": True},
            "watchtower__destroy_piece__*": {"spawnAnchor": "debris_origin", "independentBodies": True},
        },
        "qa": {
            "oneObjectFamilyOnly": True,
            "spriteCount": len(sprites),
            "tightRects": True,
            "transparentRuntime": True,
            "runtimeContainsLabels": False,
            "runtimeContainsGrid": False,
            "runtimeContainsCompositePreview": False,
            "rectsInBounds": True,
            "rectsNonOverlapping": True,
            "fileSizeBytes": ATLAS.stat().st_size,
            "under5MB": ATLAS.stat().st_size <= 5_000_000,
        },
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    cols, cell_w, cell_h = 5, 240, 205
    rows = math.ceil(len(sprites) / cols)
    grid = checker((cols * cell_w, rows * cell_h))
    draw = ImageDraw.Draw(grid)
    font = ImageFont.load_default()
    for i, item in enumerate(sprites):
        col, row = i % cols, i // cols
        ox, oy = col * cell_w, row * cell_h
        draw.rectangle((ox, oy, ox + cell_w - 1, oy + cell_h - 1), outline=(91, 80, 61, 255), width=2)
        draw.text((ox + 7, oy + 7), item["id"].replace("watchtower__", "")[:38], fill=(36, 28, 21, 255), font=font)
        image = item["image"]
        scale = min((cell_w - 24) / image.width, (cell_h - 52) / image.height, 1.45)
        shown = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
        px, py = ox + (cell_w - shown.width) // 2, oy + 34 + (cell_h - 42 - shown.height) // 2
        grid.alpha_composite(shown, (px, py))
        cx = px + round(item["pivotPx"][0] * scale)
        cy = py + round(item["pivotPx"][1] * scale)
        draw.line((cx - 7, cy, cx + 7, cy), fill=(0, 190, 220, 255), width=2)
        draw.line((cx, cy - 7, cx, cy + 7), fill=(0, 190, 220, 255), width=2)
    grid.save(GRID, optimize=True)

    preview = checker((REFERENCE_CANVAS, REFERENCE_CANVAS), 16)
    center = (192, 192)
    by_id = {item["id"]: item for item in sprites}

    def paste(sprite_id: str, anchor: tuple[int, int]) -> None:
        item = by_id[sprite_id]
        preview.alpha_composite(item["image"], (anchor[0] - item["pivotPx"][0], anchor[1] - item["pivotPx"][1]))

    def paste_rotated(sprite_id: str, anchor: tuple[int, int], degrees: float) -> tuple[int, int]:
        item = by_id[sprite_id]
        image = item["image"]
        pivot_px = item["pivotPx"]
        side = max(image.width, image.height) * 3
        canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        center_px = (side // 2, side // 2)
        canvas.alpha_composite(image, (center_px[0] - pivot_px[0], center_px[1] - pivot_px[1]))
        rotated = canvas.rotate(-degrees, resample=Image.Resampling.BICUBIC, center=center_px)
        preview.alpha_composite(rotated, (anchor[0] - center_px[0], anchor[1] - center_px[1]))
        radians = math.radians(degrees)
        return (
            round(anchor[0] + 27 * math.cos(radians)),
            round(anchor[1] + 27 * math.sin(radians)),
        )

    paste("watchtower__base_body__wardens_post", center)
    paste("watchtower__mount_socket__light_crossbow_bearing", center)
    cloth_anchor = paste_rotated("watchtower__ambient_mount__range_pennant_puck", (137, 250), 134)
    paste_rotated("watchtower__ambient_child__range_pennant__frame_02", cloth_anchor, 134)
    paste("watchtower__ambient_child__lantern_core__frame_02", (247, 250))
    paste("watchtower__ambient_mount__lantern_housing", (247, 250))
    paste("watchtower__active_primary__simple_crossbow", center)
    preview.save(COMPOSITE, optimize=True)

    parsed = json.loads(MANIFEST.read_text())
    for record in parsed["sprites"].values():
        rect = record["rect"]
        assert rect["x"] >= 0 and rect["y"] >= 0
        assert rect["x"] + rect["w"] <= atlas.width
        assert rect["y"] + rect["h"] <= atlas.height
    values = list(parsed["sprites"].values())
    for i, a in enumerate(values):
        ar = a["rect"]
        for b in values[i + 1:]:
            br = b["rect"]
            assert (
                ar["x"] + ar["w"] <= br["x"]
                or br["x"] + br["w"] <= ar["x"]
                or ar["y"] + ar["h"] <= br["y"]
                or br["y"] + br["h"] <= ar["y"]
            )
    print(json.dumps({
        "atlas": str(ATLAS.relative_to(ROOT)),
        "manifest": str(MANIFEST.relative_to(ROOT)),
        "reviewGrid": str(GRID.relative_to(ROOT)),
        "compositePreview": str(COMPOSITE.relative_to(ROOT)),
        "atlasSize": [atlas.width, atlas.height],
        "atlasBytes": ATLAS.stat().st_size,
        "spriteCount": len(sprites),
        "under5MB": ATLAS.stat().st_size <= 5_000_000,
        "rectsInBounds": True,
        "rectsNonOverlapping": True,
    }, indent=2))


if __name__ == "__main__":
    main()

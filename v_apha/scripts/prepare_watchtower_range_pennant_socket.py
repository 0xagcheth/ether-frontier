#!/usr/bin/env python3
"""Promote and place the Watchtower range-pennant mounting socket."""

from __future__ import annotations

import json
import math
import shutil
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
SOURCE = CANDIDATES / "watchtower__flag_mount__range_pennant_socket_v1_chroma.png"
ALPHA_FULL = CANDIDATES / "watchtower__flag_mount__range_pennant_socket_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
CORE = REVIEW / "fortress_ranged__base_socket_lantern_housing_v1_composite.png"
CROSSBOW = CANON / "watchtower__active_addon__light_single_crossbow_v1_alpha.png"
CROSSBOW_META = CANON / "watchtower__active_addon__light_single_crossbow_v1.json"

NAME = "watchtower__flag_mount__range_pennant_socket_v1"
POSITION_NORMALIZED = [0.24, 0.27]
SCALE_TO_BASE = 0.18


def tight_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty flag mount cutout")
    return bbox


def enclosed_transparent_components(image: Image.Image) -> list[dict]:
    alpha = image.getchannel("A")
    w, h = image.size
    transparent = bytearray(1 if value <= 18 else 0 for value in alpha.getdata())
    seen = bytearray(w * h)
    result = []
    for sy in range(h):
        for sx in range(w):
            start = sy * w + sx
            if not transparent[start] or seen[start]:
                continue
            queue = deque([(sx, sy)])
            seen[start] = 1
            area = sum_x = sum_y = 0
            touches = False
            min_x = max_x = sx
            min_y = max_y = sy
            while queue:
                x, y = queue.popleft()
                area += 1
                sum_x += x
                sum_y += y
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
                if x in (0, w - 1) or y in (0, h - 1):
                    touches = True
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        idx = ny * w + nx
                        if transparent[idx] and not seen[idx]:
                            seen[idx] = 1
                            queue.append((nx, ny))
            if not touches and area > 100:
                result.append({"area": area, "bbox": [min_x, min_y, max_x + 1, max_y + 1],
                               "center": [sum_x / area, sum_y / area]})
    return result


def checker(size: tuple[int, int], cell: int = 24) -> Image.Image:
    out = Image.new("RGB", size, "#d9d1bd")
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#c8bea7")
    return out.convert("RGBA")


def paste_at_pivot(canvas: Image.Image, layer: Image.Image, pivot: tuple[int, int], point: tuple[int, int]) -> None:
    canvas.alpha_composite(layer, (point[0] - pivot[0], point[1] - pivot[1]))


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    full = Image.open(ALPHA_FULL).convert("RGBA")
    crop = full.crop(tight_bbox(full))
    pivot = [crop.height // 2, crop.height // 2]
    holes = enclosed_transparent_components(crop)
    if not holes:
        raise RuntimeError("cloth attachment slot was not preserved")
    cloth_slot = max(holes, key=lambda item: item["center"][0])
    cloth_anchor = [round(cloth_slot["center"][0]), round(cloth_slot["center"][1])]

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    base = json.loads(BASE_META.read_text())
    target_width = round(base["footprintPx"] * SCALE_TO_BASE)
    scale = target_width / crop.width
    composed_size = [target_width, round(crop.height * scale)]
    composed_pivot = [round(pivot[0] * scale), round(pivot[1] * scale)]
    composed_cloth_anchor = [round(cloth_anchor[0] * scale), round(cloth_anchor[1] * scale)]
    visible = [pixel for pixel in crop.getdata() if pixel[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38)

    manifest = {
        "schemaVersion": 1,
        "module": "watchtower__flag_mount__range_pennant_socket",
        "object": "watchtower",
        "family": "fortress_ranged",
        "slot": "flag_mount",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(crop.size),
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / crop.width, 6), round(pivot[1] / crop.height, 6)],
        "projection": "true_top_down_orthographic_90deg",
        "forwardAxis": "+X",
        "attachments": {
            "parent": {
                "module": "fortress_ranged__base_token__round_light",
                "positionNormalized": POSITION_NORMALIZED,
                "scaleToBaseFootprint": SCALE_TO_BASE,
                "rotationDeg": 0,
            },
            "cloth_anchor": {
                "positionPx": cloth_anchor,
                "positionNormalized": [round(cloth_anchor[0] / crop.width, 6), round(cloth_anchor[1] / crop.height, 6)],
                "forwardAxis": "+X",
            },
        },
        "drawOrder": 15,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "clothSlotTransparent": True,
            "magentaSpillPixels": spill,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    core = Image.open(CORE).convert("RGBA")
    base_origin = ((core.width - base["sizePx"][0]) // 2, (core.height - base["sizePx"][1]) // 2)
    mount_point = [base_origin[0] + round(base["sizePx"][0] * POSITION_NORMALIZED[0]),
                   base_origin[1] + round(base["sizePx"][1] * POSITION_NORMALIZED[1])]
    mount = crop.resize(tuple(composed_size), Image.Resampling.LANCZOS)
    static = core.copy()
    paste_at_pivot(static, mount, tuple(composed_pivot), tuple(mount_point))

    crossbow_meta = json.loads(CROSSBOW_META.read_text())
    weapon = Image.open(CROSSBOW).convert("RGBA")
    weapon_width = round(base["footprintPx"] * crossbow_meta["attachments"]["parent"]["scaleToBaseFootprint"])
    weapon_scale = weapon_width / weapon.width
    weapon_size = [weapon_width, round(weapon.height * weapon_scale)]
    weapon_pivot = [round(crossbow_meta["pivotPx"][0] * weapon_scale), round(crossbow_meta["pivotPx"][1] * weapon_scale)]
    weapon = weapon.resize(tuple(weapon_size), Image.Resampling.LANCZOS)
    scene_center = (core.width // 2, core.height // 2)
    weapon_layer = Image.new("RGBA", core.size, (0, 0, 0, 0))
    paste_at_pivot(weapon_layer, weapon, tuple(weapon_pivot), scene_center)
    composite = static.copy()
    composite.alpha_composite(weapon_layer)
    composite_path = REVIEW / "watchtower__core_crossbow_range_pennant_socket_v1_composite.png"
    composite.save(composite_path, optimize=True)

    tile = 610
    header = 36
    grid = Image.new("RGB", (tile * 2, (tile + header) * 2), "#292a2b")
    font = ImageFont.load_default()
    for index, angle in enumerate((0, 90, 180, 270)):
        scene = checker(core.size)
        scene.alpha_composite(static)
        rotated = weapon_layer.rotate(-angle, resample=Image.Resampling.BICUBIC, center=scene_center)
        scene.alpha_composite(rotated)
        draw_scene = ImageDraw.Draw(scene)
        draw_scene.line((mount_point[0] - 12, mount_point[1], mount_point[0] + 12, mount_point[1]), fill="#e0a120", width=3)
        draw_scene.line((mount_point[0], mount_point[1] - 12, mount_point[0], mount_point[1] + 12), fill="#e0a120", width=3)
        thumb = scene.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        col, row = index % 2, index // 2
        y = row * (tile + header)
        grid.paste(thumb, (col * tile, y + header))
        ImageDraw.Draw(grid).text((col * tile + 12, y + 13), f"WEAPON {angle:03d} DEG", font=font, fill="#f3ead3")
    grid_path = REVIEW / "watchtower__range_pennant_socket_v1_weapon_clearance_grid.png"
    grid.save(grid_path, optimize=True)

    distance = math.dist(scene_center, mount_point)
    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(crop.size),
        "pivotPx": pivot,
        "clothSlot": cloth_slot,
        "clothAnchorPx": cloth_anchor,
        "composedSize": composed_size,
        "mountPointPx": mount_point,
        "distanceFromWeaponPivotPx": round(distance, 2),
        "magentaSpillVisible": spill,
        "composite": str(composite_path.relative_to(ROOT)),
        "clearanceGrid": str(grid_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

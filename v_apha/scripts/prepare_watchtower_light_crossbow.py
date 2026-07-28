#!/usr/bin/env python3
"""Promote the Watchtower crossbow and validate its pivoted rotation envelope."""

from __future__ import annotations

import json
import math
import shutil
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
SOURCE = CANDIDATES / "watchtower__active_addon__light_single_crossbow_v1_chroma.png"
ALPHA_FULL = CANDIDATES / "watchtower__active_addon__light_single_crossbow_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
BASE = CANON / "fortress_ranged__base_token__round_light_v1_alpha.png"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
CORE_COMPOSITE = REVIEW / "fortress_ranged__base_socket_lantern_housing_v1_composite.png"

NAME = "watchtower__active_addon__light_single_crossbow_v1"
SCALE_TO_BASE = 0.72


def threshold_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty crossbow cutout")
    return bbox


def enclosed_transparent_components(image: Image.Image) -> list[dict]:
    alpha = image.getchannel("A")
    w, h = image.size
    transparent = bytearray(1 if value <= 18 else 0 for value in alpha.getdata())
    seen = bytearray(w * h)
    components = []
    for sy in range(h):
        for sx in range(w):
            start = sy * w + sx
            if not transparent[start] or seen[start]:
                continue
            queue = deque([(sx, sy)])
            seen[start] = 1
            count = 0
            min_x = max_x = sx
            min_y = max_y = sy
            touches_border = False
            sum_x = sum_y = 0
            while queue:
                x, y = queue.popleft()
                count += 1
                sum_x += x
                sum_y += y
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
                if x == 0 or y == 0 or x == w - 1 or y == h - 1:
                    touches_border = True
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        idx = ny * w + nx
                        if transparent[idx] and not seen[idx]:
                            seen[idx] = 1
                            queue.append((nx, ny))
            if not touches_border and count >= 64:
                components.append({
                    "area": count,
                    "bbox": [min_x, min_y, max_x + 1, max_y + 1],
                    "center": [sum_x / count, sum_y / count],
                })
    return components


def checker(size: tuple[int, int], cell: int = 24) -> Image.Image:
    out = Image.new("RGB", size, "#d9d1bd")
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#c8bea7")
    return out.convert("RGBA")


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    full = Image.open(ALPHA_FULL).convert("RGBA")
    bbox = threshold_bbox(full)
    cutout = full.crop(bbox)

    components = enclosed_transparent_components(full)
    source_center = (full.width / 2, full.height / 2)
    pivot_component = min(
        components,
        key=lambda c: math.dist(c["center"], source_center),
    )
    pivot_source = [round(pivot_component["center"][0]), round(pivot_component["center"][1])]
    pivot = [pivot_source[0] - bbox[0], pivot_source[1] - bbox[1]]

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    cutout.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    alpha = cutout.getchannel("A")
    visible_points = [(x, y) for y in range(cutout.height) for x in range(cutout.width) if alpha.getpixel((x, y)) > 18]
    max_x = max(x for x, _ in visible_points)
    muzzle = [max_x, pivot[1]]

    base_meta = json.loads(BASE_META.read_text())
    target_width = round(base_meta["footprintPx"] * SCALE_TO_BASE)
    scale = target_width / cutout.width
    composed_size = [target_width, round(cutout.height * scale)]
    composed_pivot = [round(pivot[0] * scale), round(pivot[1] * scale)]
    composed_muzzle = [round(muzzle[0] * scale), round(muzzle[1] * scale)]
    envelope_source = max(math.dist((x, y), pivot) for x, y in visible_points)
    envelope_px = math.ceil(envelope_source * scale)
    base_radius = base_meta["footprintPx"] / 2

    visible = [p for p in cutout.getdata() if p[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38)

    manifest = {
        "schemaVersion": 1,
        "module": "watchtower__active_addon__light_single_crossbow",
        "object": "watchtower",
        "family": "fortress_ranged",
        "slot": "active_addon",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(cutout.size),
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / cutout.width, 6), round(pivot[1] / cutout.height, 6)],
        "projection": "true_top_down_orthographic_90deg",
        "forwardAxis": "+X",
        "attachments": {
            "parent": {
                "module": "fortress_ranged__center_socket__light_bearing",
                "anchor": "center",
                "scaleToBaseFootprint": SCALE_TO_BASE,
                "rotation": "aimAngle",
            },
            "muzzle_anchor": {
                "positionPx": muzzle,
                "positionNormalized": [round(muzzle[0] / cutout.width, 6), round(muzzle[1] / cutout.height, 6)],
                "forwardAxis": "+X",
                "inheritRotation": True,
            },
        },
        "drawOrder": 30,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "pivotDerivedFromAxleAperture": True,
            "rotationEnvelopeAtComposedScalePx": envelope_px,
            "rotationEnvelopeInsideBase": envelope_px <= base_radius,
            "magentaSpillPixels": spill,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    core = Image.open(CORE_COMPOSITE).convert("RGBA")
    scene_center = (core.width // 2, core.height // 2)
    weapon = cutout.resize(tuple(composed_size), Image.Resampling.LANCZOS)
    layer = Image.new("RGBA", core.size, (0, 0, 0, 0))
    origin = (scene_center[0] - composed_pivot[0], scene_center[1] - composed_pivot[1])
    layer.alpha_composite(weapon, origin)

    assembled = core.copy()
    assembled.alpha_composite(layer)
    assembled_path = REVIEW / "watchtower__core_plus_light_crossbow_v1_composite.png"
    assembled.save(assembled_path, optimize=True)

    tile = 610
    header = 36
    grid = Image.new("RGB", (tile * 2, (tile + header) * 2), "#292a2b")
    font = ImageFont.load_default()
    for index, angle in enumerate((0, 90, 180, 270)):
        rotated = layer.rotate(-angle, resample=Image.Resampling.BICUBIC, center=scene_center)
        scene = checker(core.size)
        scene.alpha_composite(core)
        scene.alpha_composite(rotated)
        draw_scene = ImageDraw.Draw(scene)
        draw_scene.ellipse((scene_center[0] - envelope_px, scene_center[1] - envelope_px,
                            scene_center[0] + envelope_px, scene_center[1] + envelope_px),
                           outline="#d94841", width=3)
        draw_scene.line((scene_center[0] - 14, scene_center[1], scene_center[0] + 14, scene_center[1]), fill="#d94841", width=3)
        draw_scene.line((scene_center[0], scene_center[1] - 14, scene_center[0], scene_center[1] + 14), fill="#d94841", width=3)
        thumb = scene.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        col, row = index % 2, index // 2
        y = row * (tile + header)
        grid.paste(thumb, (col * tile, y + header))
        draw = ImageDraw.Draw(grid)
        draw.text((col * tile + 12, y + 13), f"ROTATION {angle:03d} DEG", font=font, fill="#f3ead3")
    grid_path = REVIEW / "watchtower__light_crossbow_v1_rotation_review_grid.png"
    grid.save(grid_path, optimize=True)

    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(cutout.size),
        "pivotPx": pivot,
        "pivotAperture": pivot_component,
        "muzzleAnchorPx": muzzle,
        "composedSize": composed_size,
        "rotationEnvelopePx": envelope_px,
        "baseRadiusPx": base_radius,
        "rotationEnvelopePass": envelope_px <= base_radius,
        "magentaSpillVisible": spill,
        "composite": str(assembled_path.relative_to(ROOT)),
        "reviewGrid": str(grid_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

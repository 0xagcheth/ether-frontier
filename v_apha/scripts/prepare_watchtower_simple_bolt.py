#!/usr/bin/env python3
"""Promote the Watchtower bolt and validate spawn/trajectory anchors."""

from __future__ import annotations

import json
import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
SOURCE = CANDIDATES / "watchtower__projectile__simple_bolt_v1_chroma.png"
ALPHA_FULL = CANDIDATES / "watchtower__projectile__simple_bolt_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
CROSSBOW_META = CANON / "watchtower__active_addon__light_single_crossbow_v1.json"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
ASSEMBLED = REVIEW / "watchtower__core_plus_light_crossbow_v1_composite.png"

NAME = "watchtower__projectile__simple_bolt_v1"
SCALE_TO_WEAPON_LENGTH = 0.26


def tight_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty bolt cutout")
    return bbox


def checker(size: tuple[int, int], cell: int = 22) -> Image.Image:
    out = Image.new("RGB", size, "#d9d1bd")
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#c8bea7")
    return out.convert("RGBA")


def paste_at_anchor(canvas: Image.Image, sprite: Image.Image, anchor: tuple[int, int], point: tuple[int, int]) -> None:
    canvas.alpha_composite(sprite, (point[0] - anchor[0], point[1] - anchor[1]))


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    full = Image.open(ALPHA_FULL).convert("RGBA")
    crop = full.crop(tight_bbox(full))
    pivot = [crop.width // 2, crop.height // 2]
    spawn = [0, pivot[1]]
    impact = [crop.width - 1, pivot[1]]

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    crossbow_meta = json.loads(CROSSBOW_META.read_text())
    base_meta = json.loads(BASE_META.read_text())
    weapon_composed_width = round(base_meta["footprintPx"] * crossbow_meta["attachments"]["parent"]["scaleToBaseFootprint"])
    target_width = round(weapon_composed_width * SCALE_TO_WEAPON_LENGTH)
    scale = target_width / crop.width
    composed_size = [target_width, round(crop.height * scale)]
    composed_spawn = [round(spawn[0] * scale), round(spawn[1] * scale)]
    composed_pivot = [round(pivot[0] * scale), round(pivot[1] * scale)]

    visible = [p for p in crop.getdata() if p[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38)

    manifest = {
        "schemaVersion": 1,
        "module": "watchtower__projectile__simple_bolt",
        "object": "watchtower",
        "owner": "watchtower__active_addon__light_single_crossbow",
        "slot": "projectile",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(crop.size),
        "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height},
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / crop.width, 6), round(pivot[1] / crop.height, 6)],
        "projection": "true_top_down_orthographic_90deg",
        "forwardAxis": "+X",
        "attachments": {
            "spawn_anchor": {
                "positionPx": spawn,
                "positionNormalized": [0.0, round(spawn[1] / crop.height, 6)],
                "attachTo": "watchtower__active_addon__light_single_crossbow.muzzle_anchor",
            },
            "impact_anchor": {
                "positionPx": impact,
                "positionNormalized": [round(impact[0] / crop.width, 6), round(impact[1] / crop.height, 6)],
            },
        },
        "runtimeTransform": {
            "position": "projectilePosition",
            "rotation": "trajectoryAngle",
            "rotationPivot": "pivotPx",
            "scaleToWeaponLength": SCALE_TO_WEAPON_LENGTH,
        },
        "drawOrder": 40,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "trajectoryPivotCentered": True,
            "magentaSpillPixels": spill,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    assembled = Image.open(ASSEMBLED).convert("RGBA")
    center = [assembled.width // 2, assembled.height // 2]
    weapon_scale = weapon_composed_width / crossbow_meta["sizePx"][0]
    weapon_pivot = crossbow_meta["pivotPx"]
    weapon_muzzle = crossbow_meta["attachments"]["muzzle_anchor"]["positionPx"]
    muzzle_scene = [
        center[0] + round((weapon_muzzle[0] - weapon_pivot[0]) * weapon_scale),
        center[1] + round((weapon_muzzle[1] - weapon_pivot[1]) * weapon_scale),
    ]

    bolt = crop.resize(tuple(composed_size), Image.Resampling.LANCZOS)
    spawned = assembled.copy()
    paste_at_anchor(spawned, bolt, tuple(composed_spawn), tuple(muzzle_scene))
    spawn_path = REVIEW / "watchtower__simple_bolt_v1_muzzle_spawn_composite.png"
    spawned.save(spawn_path, optimize=True)

    tile = 620
    header = 38
    grid = Image.new("RGB", (tile * 2, (tile + header) * 2), "#292a2b")
    font = ImageFont.load_default()
    states = ((0, "MUZZLE SPAWN +X"), (0, "FLIGHT +X"), (45, "FLIGHT +45 DEG"), (-45, "FLIGHT -45 DEG"))
    for index, (angle, label) in enumerate(states):
        scene = checker(assembled.size)
        scene.alpha_composite(assembled)
        if index == 0:
            paste_at_anchor(scene, bolt, tuple(composed_spawn), tuple(muzzle_scene))
        else:
            flight_point = (center[0] + 310, center[1])
            layer = Image.new("RGBA", assembled.size, (0, 0, 0, 0))
            paste_at_anchor(layer, bolt, tuple(composed_pivot), flight_point)
            rotated = layer.rotate(-angle, resample=Image.Resampling.BICUBIC, center=flight_point)
            scene.alpha_composite(rotated)
            draw_scene = ImageDraw.Draw(scene)
            radians = math.radians(angle)
            end = (flight_point[0] + round(math.cos(radians) * 155), flight_point[1] - round(math.sin(radians) * 155))
            draw_scene.line((*flight_point, *end), fill="#d94841", width=3)
        thumb = scene.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        col, row = index % 2, index // 2
        y = row * (tile + header)
        grid.paste(thumb, (col * tile, y + header))
        ImageDraw.Draw(grid).text((col * tile + 12, y + 14), label, font=font, fill="#f3ead3")
    grid_path = REVIEW / "watchtower__simple_bolt_v1_trajectory_review_grid.png"
    grid.save(grid_path, optimize=True)

    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(crop.size),
        "trajectoryPivotPx": pivot,
        "spawnAnchorPx": spawn,
        "impactAnchorPx": impact,
        "composedSize": composed_size,
        "muzzleScenePx": muzzle_scene,
        "magentaSpillVisible": spill,
        "spawnComposite": str(spawn_path.relative_to(ROOT)),
        "reviewGrid": str(grid_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

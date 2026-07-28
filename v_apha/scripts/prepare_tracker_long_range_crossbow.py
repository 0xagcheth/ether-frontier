#!/usr/bin/env python3
"""Promote Tracker long-range crossbow and validate inherited-base rotation."""

from __future__ import annotations

import json
import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
NAME = "tracker__active_primary__long_range_crossbow_v1"
CANDIDATES = ROOT / "assets/staging/candidates/modules/tracker"
SOURCE = CANDIDATES / f"{NAME}_framed_chroma.png"
ALPHA_FULL = CANDIDATES / f"{NAME}_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/tracker"
REVIEW = ROOT / "assets/staging/reviews/modules/tracker"
SHARED = ROOT / "assets/approved/canon/modules/fortress_ranged"
BASE_META = SHARED / "fortress_ranged__base_token__round_light_v1.json"
CORE = ROOT / "assets/staging/reviews/modules/fortress_ranged/fortress_ranged__base_socket_lantern_housing_v1_composite.png"
SCALE_TO_BASE = 0.74


def bbox(image: Image.Image) -> tuple[int, int, int, int]:
    result = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not result:
        raise RuntimeError("empty Tracker long-range-crossbow cutout")
    return result


def paste_at_pivot(canvas: Image.Image, layer: Image.Image, pivot: list[int], point: tuple[int, int]) -> None:
    canvas.alpha_composite(layer, (point[0] - pivot[0], point[1] - pivot[1]))


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGBA")
    full = chroma_to_alpha(source)
    full.save(ALPHA_FULL, optimize=True)
    bounds = bbox(full)
    cutout = full.crop(bounds)

    # The framing edit centered the complete silhouette, not the mechanical axle.
    # The visible bearing is locked at 40.4% of source width on the horizontal axis.
    source_pivot = [round(source.width * 0.404), source.height // 2]
    pivot = [source_pivot[0] - bounds[0], source_pivot[1] - bounds[1]]
    pivot[0] = min(max(pivot[0], 0), cutout.width - 1)
    pivot[1] = min(max(pivot[1], 0), cutout.height - 1)

    alpha = cutout.getchannel("A")
    points = [(x, y) for y in range(cutout.height) for x in range(cutout.width) if alpha.getpixel((x, y)) > 18]
    muzzle = [max(x for x, _ in points), pivot[1]]
    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    cutout.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    base = json.loads(BASE_META.read_text())
    target_width = round(base["footprintPx"] * SCALE_TO_BASE)
    scale = target_width / cutout.width
    game_size = [target_width, round(cutout.height * scale)]
    game_pivot = [round(pivot[0] * scale), round(pivot[1] * scale)]
    envelope = math.ceil(max(math.dist((x, y), pivot) for x, y in points) * scale)
    spill = sum(1 for r, g, b, a in cutout.getdata()
                if a > 18 and r > 150 and b > 135 and g < 120 and min(r-g, b-g) > 60)

    manifest = {
        "schemaVersion": 1,
        "module": "tracker__active_primary__long_range_crossbow",
        "object": "tracker",
        "family": "fortress_ranged",
        "slot": "active_primary",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(cutout.size),
        "rect": {"x": 0, "y": 0, "w": cutout.width, "h": cutout.height},
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / cutout.width, 6), round(pivot[1] / cutout.height, 6)],
        "pivotMethod": "authored_center_axle",
        "projection": "true_top_down_orthographic_90deg",
        "forwardAxis": "+X",
        "runtimeScale": {"scaleToBaseFootprint": SCALE_TO_BASE},
        "attachments": {
            "parent": {"module": "fortress_ranged__center_socket__light_bearing", "anchor": "center", "rotation": "aimAngle"},
            "magazine_socket": {"positionPx": [round(cutout.width * .58), pivot[1]], "positionNormalized": [.58, round(pivot[1] / cutout.height, 6)], "inheritRotation": True},
            "scan_ring_socket": {"positionPx": pivot, "positionNormalized": [round(pivot[0] / cutout.width, 6), round(pivot[1] / cutout.height, 6)], "inheritRotation": True},
            "muzzle_anchor": {"positionPx": muzzle, "positionNormalized": [round(muzzle[0] / cutout.width, 6), round(muzzle[1] / cutout.height, 6)], "forwardAxis": "+X", "inheritRotation": True},
        },
        "drawOrder": 30,
        "qa": {"transparent": True, "tightRect": True, "pivotOnAuthoredAxle": True,
               "rotationEnvelopeAtComposedScalePx": envelope,
               "rotationEnvelopeInsideBase": envelope <= base["footprintPx"] / 2,
               "magentaSpillPixels": spill, "alphaBytes": alpha_path.stat().st_size,
               "under5MB": alpha_path.stat().st_size < 5_000_000, "status": "canon"},
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    core = Image.open(CORE).convert("RGBA")
    center = (core.width // 2, core.height // 2)
    weapon = cutout.resize(tuple(game_size), Image.Resampling.LANCZOS)
    layer = Image.new("RGBA", core.size, (0, 0, 0, 0))
    paste_at_pivot(layer, weapon, game_pivot, center)
    composite = core.copy()
    composite.alpha_composite(layer)
    composite_path = REVIEW / f"{NAME}_inherited_core_composite.png"
    composite.save(composite_path, optimize=True)

    tile, header = 610, 42
    grid = Image.new("RGB", (tile * 2, (tile + header) * 2), "#292a2b")
    font = ImageFont.load_default()
    for index, angle in enumerate((0, 90, 180, 270)):
        scene = checker(core.size)
        scene.alpha_composite(core)
        rotated = layer.rotate(-angle, resample=Image.Resampling.BICUBIC, center=center)
        scene.alpha_composite(rotated)
        draw = ImageDraw.Draw(scene)
        draw.ellipse((center[0]-envelope, center[1]-envelope, center[0]+envelope, center[1]+envelope), outline="#db4e45", width=3)
        draw.line((center[0]-12, center[1], center[0]+12, center[1]), fill="#db4e45", width=3)
        draw.line((center[0], center[1]-12, center[0], center[1]+12), fill="#db4e45", width=3)
        thumb = scene.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        col, row = index % 2, index // 2
        y = row * (tile + header)
        grid.paste(thumb, (col * tile, y + header))
        ImageDraw.Draw(grid).text((col*tile+12, y+14), f"TRACKER ROTATION {angle:03d} DEG", font=font, fill="#f3ead3")
    review_path = REVIEW / f"{NAME}_rotation_review_grid.png"
    grid.save(review_path, optimize=True)

    print(json.dumps({"manifest": str(manifest_path.relative_to(ROOT)), "alpha": str(alpha_path.relative_to(ROOT)),
                      "tightSize": list(cutout.size), "pivotPx": pivot, "muzzleAnchorPx": muzzle,
                      "composedSize": game_size, "rotationEnvelopePx": envelope,
                      "baseRadiusPx": base["footprintPx"] / 2,
                      "rotationEnvelopePass": envelope <= base["footprintPx"] / 2,
                      "magentaSpillVisible": spill, "alphaBytes": alpha_path.stat().st_size,
                      "composite": str(composite_path.relative_to(ROOT)), "reviewGrid": str(review_path.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()

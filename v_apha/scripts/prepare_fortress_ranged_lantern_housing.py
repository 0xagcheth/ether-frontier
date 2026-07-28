#!/usr/bin/env python3
"""Promote the approved lantern housing and build the family-core QA composite."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
SOURCE = CANDIDATES / "fortress_ranged__ambient_child__amber_lantern_housing_v1_chroma.png"
ALPHA_FULL = CANDIDATES / "fortress_ranged__ambient_child__amber_lantern_housing_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"

BASE = CANON / "fortress_ranged__base_token__round_light_v1_alpha.png"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
SOCKET = CANON / "fortress_ranged__center_socket__light_bearing_v1_alpha.png"
SOCKET_META = CANON / "fortress_ranged__center_socket__light_bearing_v1.json"

NAME = "fortress_ranged__ambient_child__amber_lantern_housing_v1"
POSITION_NORMALIZED = [0.29, 0.72]
SCALE_TO_BASE = 0.18


def tight_crop(image: Image.Image) -> Image.Image:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty lantern housing cutout")
    return image.crop(bbox)


def checker(size: tuple[int, int], cell: int = 32) -> Image.Image:
    out = Image.new("RGB", size, "#d9d1bd")
    draw = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#c8bea7")
    return out.convert("RGBA")


def paste_at_pivot(canvas: Image.Image, layer: Image.Image, point: tuple[int, int]) -> None:
    canvas.alpha_composite(layer, (point[0] - layer.width // 2, point[1] - layer.height // 2))


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)

    cutout = tight_crop(Image.open(ALPHA_FULL).convert("RGBA"))
    chroma_path = CANON / f"{NAME}_chroma.png"
    alpha_path = CANON / f"{NAME}_alpha.png"
    shutil.copy2(SOURCE, chroma_path)
    cutout.save(alpha_path, optimize=True)

    pivot = [cutout.width // 2, cutout.height // 2]
    base_meta = json.loads(BASE_META.read_text())
    base_footprint = base_meta["footprintPx"]
    target = round(base_footprint * SCALE_TO_BASE)
    scale = target / max(cutout.size)
    composed_size = [round(cutout.width * scale), round(cutout.height * scale)]

    manifest = {
        "schemaVersion": 1,
        "module": "fortress_ranged__ambient_child__amber_lantern_housing",
        "family": "fortress_ranged",
        "slot": "ambient_child",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(cutout.size),
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / cutout.width, 6), round(pivot[1] / cutout.height, 6)],
        "projection": "true_top_down_orthographic_90deg",
        "sharedBy": ["watchtower", "ranger", "tracker"],
        "attachments": {
            "parent": {
                "slot": "base_token",
                "positionNormalized": POSITION_NORMALIZED,
                "scaleToParentFootprint": SCALE_TO_BASE,
                "rotationDeg": 0,
            },
            "glow_anchor": {
                "positionNormalized": [0.5, 0.5],
                "inheritRotation": True,
            },
        },
        "drawOrder": 20,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "centralApertureTransparent": cutout.getpixel(tuple(pivot))[3] == 0,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    base = Image.open(BASE).convert("RGBA")
    socket = Image.open(SOCKET).convert("RGBA")
    socket_meta = json.loads(SOCKET_META.read_text())
    socket_target = round(base_footprint * socket_meta["attachment"]["scaleToParentFootprint"])
    socket_scale = socket_target / max(socket.size)
    socket_scaled = socket.resize(
        (round(socket.width * socket_scale), round(socket.height * socket_scale)),
        Image.Resampling.LANCZOS,
    )
    lantern_scaled = cutout.resize(tuple(composed_size), Image.Resampling.LANCZOS)

    margin = 80
    canvas_size = (base.width + margin * 2, base.height + margin * 2)
    center = (canvas_size[0] // 2, canvas_size[1] // 2)
    base_origin = ((canvas_size[0] - base.width) // 2, (canvas_size[1] - base.height) // 2)
    lantern_point = (
        base_origin[0] + round(base.width * POSITION_NORMALIZED[0]),
        base_origin[1] + round(base.height * POSITION_NORMALIZED[1]),
    )

    transparent = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    transparent.alpha_composite(base, base_origin)
    paste_at_pivot(transparent, socket_scaled, center)
    paste_at_pivot(transparent, lantern_scaled, lantern_point)
    composite_path = REVIEW / "fortress_ranged__base_socket_lantern_housing_v1_composite.png"
    transparent.save(composite_path, optimize=True)

    qa = checker(canvas_size)
    qa.alpha_composite(transparent)
    draw = ImageDraw.Draw(qa)
    for x, y, color in ((*center, "#d94841"), (*lantern_point, "#e0a120")):
        draw.line((x - 14, y, x + 14, y), fill=color, width=3)
        draw.line((x, y - 14, x, y + 14), fill=color, width=3)
    review_path = REVIEW / "fortress_ranged__base_socket_lantern_housing_v1_review.png"
    qa.convert("RGB").save(review_path, optimize=True)

    visible = [p for p in cutout.getdata() if p[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38)
    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(cutout.size),
        "pivotPx": pivot,
        "centralApertureTransparent": manifest["qa"]["centralApertureTransparent"],
        "magentaSpillVisible": spill,
        "composedSize": composed_size,
        "lanternPointPx": list(lantern_point),
        "review": str(review_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

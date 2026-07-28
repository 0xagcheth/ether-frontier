#!/usr/bin/env python3
"""Promote fortress-ranged stone debris chunk B and compare the shared kit."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
SOURCE = CANDIDATES / "fortress_ranged__debris__stone_rim_chunk_b_v1_chroma.png"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
CHUNK_A_IMAGE = CANON / "fortress_ranged__debris__stone_rim_chunk_a_v1_alpha.png"
CHUNK_A_META = CANON / "fortress_ranged__debris__stone_rim_chunk_a_v1.json"
NAME = "fortress_ranged__debris__stone_rim_chunk_b_v1"
SCALE_TO_BASE = 0.115


def chroma_to_alpha(source: Image.Image) -> Image.Image:
    out = source.convert("RGBA")
    pixels = []
    for r, g, b, _ in out.getdata():
        # Key the saturated magenta field while retaining the tan cut edge.
        dominance = min(r - g, b - g)
        # ImageGen leaves a thin compressed pink fringe around the cut line.
        # This asset has no legitimate pink material, so remove the full hue family.
        alpha = 0 if r > 130 and b > 120 and g < 145 and dominance > 32 else 255
        pixels.append((r, g, b, alpha))
    out.putdata(pixels)
    return out


def tight_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").getbbox()
    if not bbox:
        raise RuntimeError("empty debris cutout")
    return bbox


def center_of_mass(image: Image.Image) -> list[int]:
    alpha = image.getchannel("A")
    weighted_x = weighted_y = total = 0
    for y in range(image.height):
        for x in range(image.width):
            weight = alpha.getpixel((x, y))
            if weight:
                weighted_x += x * weight
                weighted_y += y * weight
                total += weight
    if not total:
        raise RuntimeError("debris has no visible mass")
    return [round(weighted_x / total), round(weighted_y / total)]


def checker(size: tuple[int, int], cell: int = 20) -> Image.Image:
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
    source = Image.open(SOURCE).convert("RGBA")
    full = chroma_to_alpha(source)
    full.save(CANDIDATES / f"{NAME}_alpha_full.png", optimize=True)
    crop = full.crop(tight_bbox(full))
    pivot = center_of_mass(crop)

    alpha_path = CANON / f"{NAME}_alpha.png"
    chroma_path = CANON / f"{NAME}_chroma.png"
    crop.save(alpha_path, optimize=True)
    shutil.copy2(SOURCE, chroma_path)

    base = json.loads(BASE_META.read_text())
    target_width = round(base["footprintPx"] * SCALE_TO_BASE)
    scale = target_width / crop.width
    composed_size = [target_width, round(crop.height * scale)]
    composed_pivot = [round(pivot[0] * scale), round(pivot[1] * scale)]
    visible = [pixel for pixel in crop.getdata() if pixel[3] > 18]
    spill = sum(1 for r, g, b, _ in visible if r > 180 and b > 160 and g < 105 and min(r-g, b-g) > 90)

    manifest = {
        "schemaVersion": 1,
        "module": "fortress_ranged__debris__stone_rim_chunk_b",
        "family": "fortress_ranged",
        "slot": "debris",
        "image": alpha_path.name,
        "sourceImage": chroma_path.name,
        "sizePx": list(crop.size),
        "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height},
        "pivotPx": pivot,
        "pivot": [round(pivot[0] / crop.width, 6), round(pivot[1] / crop.height, 6)],
        "pivotMethod": "alpha_weighted_center_of_mass",
        "projection": "true_top_down_orthographic_90deg",
        "sharedBy": ["watchtower", "ranger", "tracker", "assassin"],
        "runtimeScale": {"scaleToBaseFootprint": SCALE_TO_BASE},
        "destroyPhysics": {
            "massClass": "medium_small",
            "radialVelocityPxPerSec": [110, 195],
            "angularVelocityDegPerSec": [-280, 280],
            "linearDrag": 0.915,
            "lifetimeMs": [650, 1050],
        },
        "drawOrder": 61,
        "qa": {
            "transparent": True,
            "tightRect": True,
            "singleConnectedPiece": True,
            "magentaSpillPixels": spill,
            "status": "canon",
        },
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    chunk_a = Image.open(CHUNK_A_IMAGE).convert("RGBA")
    meta_a = json.loads(CHUNK_A_META.read_text())
    width_a = round(base["footprintPx"] * meta_a["runtimeScale"]["scaleToBaseFootprint"])
    size_a = (width_a, round(chunk_a.height * width_a / chunk_a.width))
    game_a = chunk_a.resize(size_a, Image.Resampling.LANCZOS)
    game_b = crop.resize(tuple(composed_size), Image.Resampling.LANCZOS)

    tile, header = 560, 52
    grid = Image.new("RGB", (tile * 2, tile + header), "#292a2b")
    font = ImageFont.load_default()
    panels = [checker((tile, tile), 22), checker((tile, tile), 22)]
    displays = [game_a.resize((game_a.width * 3, game_a.height * 3), Image.Resampling.NEAREST),
                game_b.resize((game_b.width * 3, game_b.height * 3), Image.Resampling.NEAREST)]
    pivots = [meta_a["pivotPx"], pivot]
    crops = [chunk_a, crop]
    for panel, display, source_crop, source_pivot in zip(panels, displays, crops, pivots):
        origin = ((tile - display.width) // 2, (tile - display.height) // 2)
        panel.alpha_composite(display, origin)
        px = origin[0] + round(source_pivot[0] / source_crop.width * display.width)
        py = origin[1] + round(source_pivot[1] / source_crop.height * display.height)
        draw = ImageDraw.Draw(panel)
        draw.line((px - 12, py, px + 12, py), fill="#e34b46", width=3)
        draw.line((px, py - 12, px, py + 12), fill="#e34b46", width=3)
    grid.paste(panels[0].convert("RGB"), (0, header))
    grid.paste(panels[1].convert("RGB"), (tile, header))
    draw = ImageDraw.Draw(grid)
    draw.text((14, 18), f"CHUNK A — {size_a[0]} x {size_a[1]} px", font=font, fill="#f3ead3")
    draw.text((tile + 14, 18), f"CHUNK B — {composed_size[0]} x {composed_size[1]} px", font=font, fill="#f3ead3")
    review_path = REVIEW / "fortress_ranged__stone_rim_chunks_a_b_v1_review.png"
    grid.save(review_path, optimize=True)

    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "alpha": str(alpha_path.relative_to(ROOT)),
        "tightSize": list(crop.size),
        "centerOfMassPivotPx": pivot,
        "composedSize": composed_size,
        "magentaSpillVisible": spill,
        "alphaBytes": alpha_path.stat().st_size,
        "under5MB": alpha_path.stat().st_size < 5_000_000,
        "review": str(review_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

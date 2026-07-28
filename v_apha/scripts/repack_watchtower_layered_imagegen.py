#!/usr/bin/env python3
"""Repack ImageGen Watchtower layered sheet into a code-friendly fixed grid atlas."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "assets/sprite-atlases/watchtower/layered-imagegen-v1"
SRC_ATLAS = SRC_DIR / "watchtower_layered_imagegen_v1_atlas.png"
SRC_MANIFEST = SRC_DIR / "watchtower_layered_imagegen_v1_manifest.json"
OUT_DIR = ROOT / "assets/sprite-atlases/watchtower/layered-imagegen-v1/packed-grid"

CELL = 512
COLS = 4

RUNTIME_ORDER = [
    "base_stone_token",
    "central_socket",
    "crossbow_rotatable",
    "flag_pole",
    "flag_cloth_wind_01",
    "flag_cloth_wind_02",
    "flag_cloth_wind_03",
    "flag_cloth_wind_04",
    "lantern_body",
    "lantern_flame_01",
    "lantern_flame_02",
    "lantern_flame_03",
    "lantern_flame_04",
    "muzzle_flash_01",
    "muzzle_flash_02",
    "muzzle_flash_03",
    "projectile_bolt",
]

DEBRIS_SOURCE = "destroy_debris_group"


def crop_sprite(source: Image.Image, rect: dict[str, int]) -> Image.Image:
    x, y, w, h = rect["x"], rect["y"], rect["w"], rect["h"]
    crop = source.crop((x, y, x + w, y + h))
    box = crop.getchannel("A").getbbox()
    if not box:
        return crop
    return crop.crop(box)


def alpha_components(image: Image.Image, threshold: int = 24) -> list[tuple[int, tuple[int, int, int, int]]]:
    alpha = image.getchannel("A")
    pix = alpha.load()
    w, h = image.size
    seen: set[tuple[int, int]] = set()
    components: list[tuple[int, tuple[int, int, int, int]]] = []
    for y in range(h):
        for x in range(w):
            if pix[x, y] < threshold or (x, y) in seen:
                continue
            stack = [(x, y)]
            seen.add((x, y))
            xs: list[int] = []
            ys: list[int] = []
            while stack:
                cx, cy = stack.pop()
                xs.append(cx)
                ys.append(cy)
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen and pix[nx, ny] >= threshold:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            if len(xs) >= 120:
                components.append((len(xs), (min(xs), min(ys), max(xs) + 1, max(ys) + 1)))
    components.sort(reverse=True)
    return components


def keep_largest_component(image: Image.Image) -> Image.Image:
    alpha = image.getchannel("A")
    pix = alpha.load()
    w, h = image.size
    seen: set[tuple[int, int]] = set()
    best: list[tuple[int, int]] = []
    for y in range(h):
        for x in range(w):
            if pix[x, y] < 24 or (x, y) in seen:
                continue
            stack = [(x, y)]
            seen.add((x, y))
            points: list[tuple[int, int]] = []
            while stack:
                cx, cy = stack.pop()
                points.append((cx, cy))
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen and pix[nx, ny] >= 24:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            if len(points) > len(best):
                best = points
    if not best:
        return image
    xs = [p[0] for p in best]
    ys = [p[1] for p in best]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs) + 1, max(ys) + 1
    out = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    src = image.load()
    dst = out.load()
    for x, y in best:
        dst[x - x0, y - y0] = src[x, y]
    return out


def split_debris(source: Image.Image, rect: dict[str, int]) -> list[Image.Image]:
    debris = crop_sprite(source, rect)
    pieces: list[Image.Image] = []
    for area, box in alpha_components(debris):
        if area < 350:
            continue
        piece = debris.crop(box)
        if piece.width > CELL - 24 or piece.height > CELL - 24:
            piece.thumbnail((CELL - 24, CELL - 24), Image.Resampling.LANCZOS)
        pieces.append(piece)
    return pieces[:14]


def pivot_for(name: str, source_pivot: list[float], paste_x: int, paste_y: int, crop: Image.Image) -> list[float]:
    """Return normalized pivot within the fixed 512 cell."""
    # Most components are centered in their cell.
    px = paste_x + crop.width * source_pivot[0]
    py = paste_y + crop.height * source_pivot[1]
    if name.startswith("flag_cloth"):
        # Flag cloth attaches to the pole from its left-center edge.
        px = paste_x + crop.width * 0.02
        py = paste_y + crop.height * 0.5
    elif name.startswith("lantern_flame"):
        px = paste_x + crop.width * 0.5
        py = paste_y + crop.height * 0.72
    elif name.startswith("muzzle_flash"):
        # Flash is placed at the weapon muzzle; attach from right-center so it can face out from the crossbow tip.
        px = paste_x + crop.width * 0.92
        py = paste_y + crop.height * 0.5
    return [round(px / CELL, 4), round(py / CELL, 4)]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    source = Image.open(SRC_ATLAS).convert("RGBA")
    source_manifest = json.loads(SRC_MANIFEST.read_text())
    debris_pieces = split_debris(source, source_manifest["sprites"][DEBRIS_SOURCE]["rect"])
    debris_names = [f"destroy_debris_{index + 1:02d}" for index in range(len(debris_pieces))]
    runtime_order = [*RUNTIME_ORDER, *debris_names]
    rows = (len(runtime_order) + COLS - 1) // COLS
    atlas = Image.new("RGBA", (COLS * CELL, rows * CELL), (0, 0, 0, 0))
    review = Image.new("RGBA", atlas.size, (34, 24, 42, 255))
    sprites: dict[str, dict] = {}

    for index, name in enumerate(runtime_order):
        if name.startswith("destroy_debris_"):
            debris_index = debris_names.index(name)
            src_sprite = {"rect": source_manifest["sprites"][DEBRIS_SOURCE]["rect"], "pivot": [0.5, 0.5]}
            crop = debris_pieces[debris_index]
        else:
            src_sprite = source_manifest["sprites"][name]
            crop = crop_sprite(source, src_sprite["rect"])
            if name.startswith("flag_cloth") or name in {
                "base_stone_token",
                "central_socket",
                "crossbow_rotatable",
                "flag_pole",
                "lantern_body",
                "projectile_bolt",
            }:
                crop = keep_largest_component(crop)
        if crop.width > CELL - 24 or crop.height > CELL - 24:
            crop.thumbnail((CELL - 24, CELL - 24), Image.Resampling.LANCZOS)
        col = index % COLS
        row = index // COLS
        cell_x = col * CELL
        cell_y = row * CELL
        paste_x = cell_x + (CELL - crop.width) // 2
        paste_y = cell_y + (CELL - crop.height) // 2
        atlas.alpha_composite(crop, (paste_x, paste_y))
        review.alpha_composite(crop, (paste_x, paste_y))
        pivot = pivot_for(name, src_sprite.get("pivot", [0.5, 0.5]), paste_x - cell_x, paste_y - cell_y, crop)
        sprites[name] = {
            "cell": {"col": col, "row": row, "x": cell_x, "y": cell_y, "w": CELL, "h": CELL},
            "contentRect": {"x": paste_x, "y": paste_y, "w": crop.width, "h": crop.height},
            "contentRectInCell": {"x": paste_x - cell_x, "y": paste_y - cell_y, "w": crop.width, "h": crop.height},
            "pivot": pivot,
            "source": {
                "image": "../watchtower_layered_imagegen_v1_atlas.png",
                "rect": src_sprite["rect"],
            },
        }

    draw = ImageDraw.Draw(review)
    for x in range(0, atlas.size[0] + 1, CELL):
        draw.line((x, 0, x, atlas.size[1]), fill=(255, 255, 255, 155), width=2)
    for y in range(0, atlas.size[1] + 1, CELL):
        draw.line((0, y, atlas.size[0], y), fill=(255, 255, 255, 155), width=2)
    for name, sprite in sprites.items():
        cell = sprite["cell"]
        x, y = cell["x"], cell["y"]
        draw.rectangle((x + 1, y + 1, x + CELL - 2, y + CELL - 2), outline=(255, 210, 92, 220), width=2)
        draw.rectangle((x + 8, y + 8, x + min(CELL - 8, 12 + len(name) * 8), y + 31), fill=(0, 0, 0, 190))
        draw.text((x + 12, y + 12), name, fill=(255, 232, 150, 255))
        px = x + round(sprite["pivot"][0] * CELL)
        py = y + round(sprite["pivot"][1] * CELL)
        draw.line((px - 12, py, px + 12, py), fill=(0, 255, 255, 230), width=2)
        draw.line((px, py - 12, px, py + 12), fill=(0, 255, 255, 230), width=2)

    atlas_path = OUT_DIR / "watchtower_layered_imagegen_v1_packed_512.png"
    review_path = OUT_DIR / "watchtower_layered_imagegen_v1_packed_512_review.png"
    manifest_path = OUT_DIR / "watchtower_layered_imagegen_v1_packed_512_manifest.json"
    atlas.save(atlas_path, optimize=True)
    review.save(review_path, optimize=True)

    manifest = {
        "object": "watchtower",
        "pipeline": "layered-object-v2-packed-grid",
        "status": "packed_grid_for_user_validation",
        "generator": "built-in imagegen source, deterministic code repack",
        "image": atlas_path.name,
        "reviewImage": review_path.name,
        "sourceImage": "../watchtower_layered_imagegen_v1_atlas.png",
        "sourceManifest": "../watchtower_layered_imagegen_v1_manifest.json",
        "atlasSize": list(atlas.size),
        "cellSize": [CELL, CELL],
        "grid": {"cols": COLS, "rows": rows},
        "format": "RGBA PNG",
        "fileSizeBytes": atlas_path.stat().st_size,
        "maxFileSizeBytes": 5_000_000,
        "under5MB": atlas_path.stat().st_size <= 5_000_000,
        "drawOrder": source_manifest["drawOrder"],
        "sprites": sprites,
        "attachments": {
            "object_center": {"sprite": "base_stone_token", "pivot": sprites["base_stone_token"]["pivot"]},
            "weapon_pivot": {"sprite": "crossbow_rotatable", "pivot": sprites["crossbow_rotatable"]["pivot"], "runtimeTransform": "rotate_to_target"},
            "flag_anchor": {"sprite": "flag_cloth_wind_*", "pivot": "left_center", "runtimeTransform": "wind_direction_or_wind_phase"},
            "lantern_anchor": {"sprite": "lantern_flame_*", "pivot": "lower_center", "runtimeTransform": "flame_loop"},
            "muzzle_anchor": {"sprite": "muzzle_flash_*", "pivot": "right_center", "runtimeTransform": "attack_once"},
            "projectile_spawn": {"sprite": "projectile_bolt", "pivot": sprites["projectile_bolt"]["pivot"], "runtimeTransform": "rotate_along_trajectory"},
        },
        "animations": {
            "idle": {
                "static": ["base_stone_token", "central_socket", "flag_pole", "lantern_body", "crossbow_rotatable"],
                "loops": {
                    "flag_cloth_wind": ["flag_cloth_wind_01", "flag_cloth_wind_02", "flag_cloth_wind_03", "flag_cloth_wind_04"],
                    "lantern_flame": ["lantern_flame_01", "lantern_flame_02", "lantern_flame_03", "lantern_flame_04"],
                },
                "durationMs": 140,
                "loop": True,
            },
            "attack": {
                "runtimeRotation": "crossbow_rotatable follows target angle around weapon_pivot",
                "once": ["muzzle_flash_01", "muzzle_flash_02", "muzzle_flash_03"],
                "durationMs": 80,
                "loop": False,
            },
            "projectile": {"sprite": "projectile_bolt", "runtimeRotation": "rotate_along_trajectory"},
            "destroy": {"pieces": debris_names, "loop": False, "holdLast": True},
        },
        "qa": {
            "oneSpritePerCell": True,
            "fixedCellGrid": True,
            "transparentRuntimeBackground": True,
            "noReviewPreviewInsideRuntimeAtlas": True,
            "debrisSplitIntoIndividualCells": True,
            "knownIssues": [
                "ImageGen source still has three strong muzzle flash frames; production generation should request a fourth distinct frame."
            ],
        },
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(atlas_path)
    print(review_path)
    print(manifest_path)
    print("bytes", atlas_path.stat().st_size)


if __name__ == "__main__":
    main()

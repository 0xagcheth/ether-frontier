#!/usr/bin/env python3
"""Segment and normalize the Watchtower four-frame muzzle-flash one-shot."""

from __future__ import annotations

import json
import shutil
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
SOURCE = CANDIDATES / "watchtower__muzzle_fx__compact_golden_flash_loop_v1_chroma.png"
ALPHA_SHEET = CANDIDATES / "watchtower__muzzle_fx__compact_golden_flash_loop_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
CROSSBOW_META = CANON / "watchtower__active_addon__light_single_crossbow_v1.json"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
ASSEMBLED = REVIEW / "watchtower__core_plus_light_crossbow_v1_composite.png"

FRAME_DURATION_MS = 90
SCALE_TO_WEAPON_LENGTH = 0.20
PAD = 8


def connected_components(image: Image.Image) -> list[dict]:
    alpha = image.getchannel("A")
    w, h = image.size
    foreground = bytearray(1 if value > 18 else 0 for value in alpha.getdata())
    seen = bytearray(w * h)
    components = []
    for sy in range(h):
        for sx in range(w):
            start = sy * w + sx
            if not foreground[start] or seen[start]:
                continue
            queue = deque([(sx, sy)])
            seen[start] = 1
            count = sum_x = sum_y = 0
            min_x = max_x = sx
            min_y = max_y = sy
            while queue:
                x, y = queue.popleft()
                count += 1
                sum_x += x
                sum_y += y
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        idx = ny * w + nx
                        if foreground[idx] and not seen[idx]:
                            seen[idx] = 1
                            queue.append((nx, ny))
            if count >= 1000:
                components.append({
                    "area": count,
                    "bbox": [min_x, min_y, max_x + 1, max_y + 1],
                    "centroid": [sum_x / count, sum_y / count],
                })
    if len(components) != 4:
        raise RuntimeError(f"expected four muzzle components, found {len(components)}")
    return sorted(components, key=lambda c: (c["centroid"][1] >= image.height / 2, c["centroid"][0]))


def checker(size: tuple[int, int], cell: int = 18) -> Image.Image:
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
    sheet = Image.open(ALPHA_SHEET).convert("RGBA")
    components = connected_components(sheet)
    crops = [sheet.crop(tuple(component["bbox"])) for component in components]
    max_width = max(crop.width for crop in crops)
    max_height = max(crop.height for crop in crops)
    canvas_size = [max_width + PAD * 2, max_height + PAD * 2]
    pivot = [PAD, canvas_size[1] // 2]

    frames = []
    records = []
    for index, crop in enumerate(crops, 1):
        frame = Image.new("RGBA", tuple(canvas_size), (0, 0, 0, 0))
        offset = [PAD, pivot[1] - crop.height // 2]
        frame.alpha_composite(crop, tuple(offset))
        name = f"watchtower__muzzle_fx__compact_golden_flash__frame_{index:02d}_v1_alpha.png"
        path = CANON / name
        frame.save(path, optimize=True)
        frames.append(frame)
        records.append({
            "id": f"frame_{index:02d}",
            "image": name,
            "rect": {"x": 0, "y": 0, "w": canvas_size[0], "h": canvas_size[1]},
            "contentRect": {"x": offset[0], "y": offset[1], "w": crop.width, "h": crop.height},
            "pivotPx": pivot,
            "pivot": [round(pivot[0] / canvas_size[0], 6), 0.5],
            "durationMs": FRAME_DURATION_MS,
        })

    source_copy = CANON / "watchtower__muzzle_fx__compact_golden_flash_loop_v1_chroma.png"
    shutil.copy2(SOURCE, source_copy)
    manifest = {
        "schemaVersion": 1,
        "module": "watchtower__muzzle_fx__compact_golden_flash",
        "object": "watchtower",
        "owner": "watchtower__active_addon__light_single_crossbow",
        "slot": "muzzle_fx",
        "sourceImage": source_copy.name,
        "projection": "true_top_down_orthographic_90deg",
        "forwardAxis": "+X",
        "attachment": {
            "parentAnchor": "watchtower__active_addon__light_single_crossbow.muzzle_anchor",
            "pivotPx": pivot,
            "scaleToWeaponLength": SCALE_TO_WEAPON_LENGTH,
            "inheritRotation": True,
        },
        "drawOrder": 50,
        "frames": records,
        "animations": {
            "attack_flash": {
                "frames": [record["id"] for record in records],
                "loop": False,
                "holdLast": False,
                "totalDurationMs": FRAME_DURATION_MS * len(records),
            }
        },
        "qa": {
            "segmentation": "connected_components",
            "sharedCanvas": canvas_size,
            "sharedPivot": pivot,
            "runtimeLabels": False,
            "status": "canon",
        },
    }
    manifest_path = CANON / "watchtower__muzzle_fx__compact_golden_flash_loop_v1.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    # Separate human-review grid.
    tile = 250
    header = 42
    grid = Image.new("RGB", (tile * 4, tile + header), "#292a2b")
    font = ImageFont.load_default()
    labels = ("IGNITION", "EXPANSION", "PEAK", "FADE")
    for index, frame in enumerate(frames):
        thumb = checker((tile, tile))
        scale = min(220 / canvas_size[0], 220 / canvas_size[1])
        sprite = frame.resize((round(canvas_size[0] * scale), round(canvas_size[1] * scale)), Image.Resampling.LANCZOS)
        origin = (15, (tile - sprite.height) // 2)
        thumb.alpha_composite(sprite, origin)
        grid.paste(thumb.convert("RGB"), (index * tile, header))
        draw = ImageDraw.Draw(grid)
        px = index * tile + origin[0] + round(pivot[0] * scale)
        py = header + origin[1] + round(pivot[1] * scale)
        draw.line((px - 9, py, px + 9, py), fill="#e34b46", width=2)
        draw.line((px, py - 9, px, py + 9), fill="#e34b46", width=2)
        draw.text((index * tile + 10, 14), f"{index + 1:02d} {labels[index]} {FRAME_DURATION_MS}ms", font=font, fill="#f3ead3")
    grid_path = REVIEW / "watchtower__compact_golden_muzzle_flash_loop_v1_review_grid.png"
    grid.save(grid_path, optimize=True)

    # Animated one-shot preview over the approved static Watchtower assembly.
    assembled = Image.open(ASSEMBLED).convert("RGBA")
    crossbow = json.loads(CROSSBOW_META.read_text())
    base = json.loads(BASE_META.read_text())
    center = [assembled.width // 2, assembled.height // 2]
    weapon_width = round(base["footprintPx"] * crossbow["attachments"]["parent"]["scaleToBaseFootprint"])
    weapon_scale = weapon_width / crossbow["sizePx"][0]
    muzzle = crossbow["attachments"]["muzzle_anchor"]["positionPx"]
    weapon_pivot = crossbow["pivotPx"]
    muzzle_scene = [center[0] + round((muzzle[0] - weapon_pivot[0]) * weapon_scale),
                    center[1] + round((muzzle[1] - weapon_pivot[1]) * weapon_scale)]
    target_width = round(weapon_width * SCALE_TO_WEAPON_LENGTH)
    preview_scale = target_width / canvas_size[0]
    preview_size = [target_width, round(canvas_size[1] * preview_scale)]
    preview_pivot = [round(pivot[0] * preview_scale), round(pivot[1] * preview_scale)]
    previews = []
    for frame in frames:
        scene = checker(assembled.size, 28)
        scene.alpha_composite(assembled)
        flash = frame.resize(tuple(preview_size), Image.Resampling.LANCZOS)
        scene.alpha_composite(flash, (muzzle_scene[0] - preview_pivot[0], muzzle_scene[1] - preview_pivot[1]))
        previews.append(scene.convert("RGB").resize((612, 621), Image.Resampling.LANCZOS))
    blank = checker(assembled.size, 28)
    blank.alpha_composite(assembled)
    previews.append(blank.convert("RGB").resize((612, 621), Image.Resampling.LANCZOS))
    gif_path = REVIEW / "watchtower__compact_golden_muzzle_flash_loop_v1_attack_preview.gif"
    previews[0].save(gif_path, save_all=True, append_images=previews[1:], duration=[90, 90, 90, 90, 450], loop=0, optimize=True)

    total_bytes = sum((CANON / record["image"]).stat().st_size for record in records)
    spill = []
    for frame in frames:
        spill.append(sum(1 for r, g, b, a in frame.getdata() if a > 18 and r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38))
    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "components": components,
        "sharedCanvas": canvas_size,
        "sharedPivot": pivot,
        "runtimeFrameBytes": total_bytes,
        "under5MB": total_bytes < 5_000_000,
        "magentaSpillPerFrame": spill,
        "composedFlashSize": preview_size,
        "reviewGrid": str(grid_path.relative_to(ROOT)),
        "attackPreview": str(gif_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

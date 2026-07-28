#!/usr/bin/env python3
"""Segment, normalize, and preview the Watchtower range-pennant idle loop."""

from __future__ import annotations

import json
import shutil
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "assets/staging/candidates/modules/fortress_ranged"
SOURCE = CANDIDATES / "watchtower__ambient_child__range_pennant_wind_loop_v1_chroma.png"
ALPHA_SHEET = CANDIDATES / "watchtower__ambient_child__range_pennant_wind_loop_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
MOUNT_META = CANON / "watchtower__flag_mount__range_pennant_socket_v1.json"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
ASSEMBLED = REVIEW / "watchtower__core_crossbow_range_pennant_socket_v1_composite.png"

FRAME_DURATION_MS = 180
SCALE_TO_BASE = 0.22
PAD = 8


def components(image: Image.Image) -> list[dict]:
    alpha = image.getchannel("A")
    w, h = image.size
    foreground = bytearray(1 if value > 18 else 0 for value in alpha.getdata())
    seen = bytearray(w * h)
    found = []
    for sy in range(h):
        for sx in range(w):
            start = sy * w + sx
            if not foreground[start] or seen[start]:
                continue
            queue = deque([(sx, sy)])
            seen[start] = 1
            area = sum_x = sum_y = 0
            min_x = max_x = sx
            min_y = max_y = sy
            while queue:
                x, y = queue.popleft()
                area += 1
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
            if area > 1000:
                found.append({"area": area, "bbox": [min_x, min_y, max_x + 1, max_y + 1],
                              "centroid": [sum_x / area, sum_y / area]})
    if len(found) != 4:
        raise RuntimeError(f"expected four pennant components, found {len(found)}")
    return sorted(found, key=lambda item: (item["centroid"][1] >= h / 2, item["centroid"][0]))


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
    detected = components(sheet)
    crops = [sheet.crop(tuple(item["bbox"])) for item in detected]
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
        name = f"watchtower__ambient_child__range_pennant_wind__frame_{index:02d}_v1_alpha.png"
        path = CANON / name
        frame.save(path, optimize=True)
        frames.append(frame)
        records.append({
            "id": f"frame_{index:02d}",
            "image": name,
            "rect": {"x": 0, "y": 0, "w": canvas_size[0], "h": canvas_size[1]},
            "contentRect": {"x": offset[0], "y": offset[1], "w": crop.width, "h": crop.height},
            "pivotPx": pivot,
            "pivot": [round(pivot[0] / canvas_size[0], 6), round(pivot[1] / canvas_size[1], 6)],
            "durationMs": FRAME_DURATION_MS,
        })

    source_copy = CANON / "watchtower__ambient_child__range_pennant_wind_loop_v1_chroma.png"
    shutil.copy2(SOURCE, source_copy)
    manifest = {
        "schemaVersion": 1,
        "module": "watchtower__ambient_child__range_pennant_wind",
        "object": "watchtower",
        "slot": "ambient_child",
        "sourceImage": source_copy.name,
        "projection": "true_top_down_orthographic_90deg",
        "forwardAxis": "+X",
        "attachment": {
            "parentAnchor": "watchtower__flag_mount__range_pennant_socket.cloth_anchor",
            "pivotPx": pivot,
            "scaleToBaseFootprint": SCALE_TO_BASE,
            "inheritRotation": True,
        },
        "drawOrder": 16,
        "frames": records,
        "animations": {
            "idle_wind": {
                "frames": [record["id"] for record in records],
                "loop": True,
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
    manifest_path = CANON / "watchtower__ambient_child__range_pennant_wind_loop_v1.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    # Human-only review grid.
    tile = 250
    header = 42
    labels = ("UP RIPPLE", "STRAIGHT", "DOWN RIPPLE", "RETURN")
    grid = Image.new("RGB", (tile * 4, tile + header), "#292a2b")
    font = ImageFont.load_default()
    for index, frame in enumerate(frames):
        thumb = checker((tile, tile))
        scale = min(230 / canvas_size[0], 210 / canvas_size[1])
        sprite = frame.resize((round(canvas_size[0] * scale), round(canvas_size[1] * scale)), Image.Resampling.LANCZOS)
        origin = (10, (tile - sprite.height) // 2)
        thumb.alpha_composite(sprite, origin)
        grid.paste(thumb.convert("RGB"), (index * tile, header))
        draw = ImageDraw.Draw(grid)
        px = index * tile + origin[0] + round(pivot[0] * scale)
        py = header + origin[1] + round(pivot[1] * scale)
        draw.line((px - 9, py, px + 9, py), fill="#e34b46", width=2)
        draw.line((px, py - 9, px, py + 9), fill="#e34b46", width=2)
        draw.text((index * tile + 10, 14), f"{index + 1:02d} {labels[index]} {FRAME_DURATION_MS}ms", font=font, fill="#f3ead3")
    grid_path = REVIEW / "watchtower__range_pennant_wind_loop_v1_review_grid.png"
    grid.save(grid_path, optimize=True)

    # Assembled idle preview.
    assembled = Image.open(ASSEMBLED).convert("RGBA")
    base = json.loads(BASE_META.read_text())
    mount = json.loads(MOUNT_META.read_text())
    base_origin = ((assembled.width - base["sizePx"][0]) // 2, (assembled.height - base["sizePx"][1]) // 2)
    mount_position = mount["attachments"]["parent"]["positionNormalized"]
    mount_point = [base_origin[0] + round(base["sizePx"][0] * mount_position[0]),
                   base_origin[1] + round(base["sizePx"][1] * mount_position[1])]
    mount_width = round(base["footprintPx"] * mount["attachments"]["parent"]["scaleToBaseFootprint"])
    mount_scale = mount_width / mount["sizePx"][0]
    mount_pivot = mount["pivotPx"]
    cloth_anchor = mount["attachments"]["cloth_anchor"]["positionPx"]
    cloth_scene = [mount_point[0] + round((cloth_anchor[0] - mount_pivot[0]) * mount_scale),
                   mount_point[1] + round((cloth_anchor[1] - mount_pivot[1]) * mount_scale)]
    target_width = round(base["footprintPx"] * SCALE_TO_BASE)
    preview_scale = target_width / canvas_size[0]
    preview_size = [target_width, round(canvas_size[1] * preview_scale)]
    preview_pivot = [round(pivot[0] * preview_scale), round(pivot[1] * preview_scale)]
    previews = []
    for frame in frames:
        scene = checker(assembled.size, 28)
        scene.alpha_composite(assembled)
        pennant = frame.resize(tuple(preview_size), Image.Resampling.LANCZOS)
        scene.alpha_composite(pennant, (cloth_scene[0] - preview_pivot[0], cloth_scene[1] - preview_pivot[1]))
        previews.append(scene.convert("RGB").resize((612, 621), Image.Resampling.LANCZOS))
    gif_path = REVIEW / "watchtower__range_pennant_wind_loop_v1_idle_preview.gif"
    previews[0].save(gif_path, save_all=True, append_images=previews[1:], duration=FRAME_DURATION_MS, loop=0, optimize=True)

    total_bytes = sum((CANON / record["image"]).stat().st_size for record in records)
    spill = [sum(1 for r, g, b, a in frame.getdata() if a > 18 and r > 135 and b > 85 and g < 120 and r - g > 60 and b - g > 38) for frame in frames]
    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "components": detected,
        "sharedCanvas": canvas_size,
        "sharedPivot": pivot,
        "runtimeFrameBytes": total_bytes,
        "under5MB": total_bytes < 5_000_000,
        "magentaSpillPerFrame": spill,
        "clothAnchorScenePx": cloth_scene,
        "composedPennantSize": preview_size,
        "reviewGrid": str(grid_path.relative_to(ROOT)),
        "idlePreview": str(gif_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Split, normalize, manifest, and preview the approved four-frame lantern glow loop."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/staging/candidates/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_glow_loop_v1_chroma.png"
ALPHA_SHEET = ROOT / "assets/staging/candidates/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_glow_loop_v1_alpha_full.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
COMPOSITE = REVIEW / "fortress_ranged__base_socket_lantern_housing_v1_composite.png"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
HOUSING_META = CANON / "fortress_ranged__ambient_child__amber_lantern_housing_v1.json"

FRAME_CANVAS = 440
FRAME_DURATION_MS = 180
GLOW_TO_HOUSING = 0.31


def alpha_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not bbox:
        raise RuntimeError("empty glow frame")
    return bbox


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
    sheet = Image.open(ALPHA_SHEET).convert("RGBA")
    source_sheet = Image.open(SOURCE)
    w, h = sheet.size
    slots = ((0, 0, w // 2, h // 2), (w // 2, 0, w, h // 2),
             (0, h // 2, w // 2, h), (w // 2, h // 2, w, h))

    frames: list[Image.Image] = []
    frame_records = []
    for index, slot in enumerate(slots, 1):
        quadrant = sheet.crop(slot)
        crop = quadrant.crop(alpha_bbox(quadrant))
        if crop.size != (427, 431):
            raise RuntimeError(f"frame {index} unexpected tight size {crop.size}")
        frame = Image.new("RGBA", (FRAME_CANVAS, FRAME_CANVAS), (0, 0, 0, 0))
        offset = ((FRAME_CANVAS - crop.width) // 2, (FRAME_CANVAS - crop.height) // 2)
        frame.alpha_composite(crop, offset)
        name = f"fortress_ranged__ambient_child__amber_lantern_glow__frame_{index:02d}_v1_alpha.png"
        path = CANON / name
        frame.save(path, optimize=True)
        frames.append(frame)
        frame_records.append({
            "id": f"frame_{index:02d}",
            "image": name,
            "rect": {"x": 0, "y": 0, "w": FRAME_CANVAS, "h": FRAME_CANVAS},
            "contentRect": {"x": offset[0], "y": offset[1], "w": crop.width, "h": crop.height},
            "pivotPx": [FRAME_CANVAS // 2, FRAME_CANVAS // 2],
            "pivot": [0.5, 0.5],
            "durationMs": FRAME_DURATION_MS,
        })

    source_copy = CANON / "fortress_ranged__ambient_child__amber_lantern_glow_loop_v1_chroma.png"
    source_sheet.save(source_copy, optimize=True)
    manifest = {
        "schemaVersion": 1,
        "module": "fortress_ranged__ambient_child__amber_lantern_glow",
        "family": "fortress_ranged",
        "slot": "ambient_child",
        "sourceImage": source_copy.name,
        "projection": "true_top_down_orthographic_90deg",
        "sharedBy": ["watchtower", "ranger", "tracker"],
        "attachment": {
            "parentModule": "fortress_ranged__ambient_child__amber_lantern_housing",
            "anchor": "glow_anchor",
            "scaleToParentFootprint": GLOW_TO_HOUSING,
            "inheritRotation": True,
        },
        "drawOrder": 21,
        "frames": frame_records,
        "animations": {
            "idle_glow": {
                "frames": [record["id"] for record in frame_records],
                "loop": True,
                "totalDurationMs": FRAME_DURATION_MS * len(frame_records),
            }
        },
        "qa": {
            "sharedCanvas": [FRAME_CANVAS, FRAME_CANVAS],
            "sharedPivot": [FRAME_CANVAS // 2, FRAME_CANVAS // 2],
            "sourceCenterDriftMaxPx": 1,
            "runtimeLabels": False,
            "status": "canon",
        },
    }
    manifest_path = CANON / "fortress_ranged__ambient_child__amber_lantern_glow_loop_v1.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    # Separate human-QA grid. Labels, slot boxes, and pivot crosses live only here.
    tile = 250
    header = 42
    grid = Image.new("RGB", (tile * 4, tile + header), "#292a2b")
    draw = ImageDraw.Draw(grid)
    font = ImageFont.load_default()
    for i, frame in enumerate(frames):
        thumb = checker((tile, tile), 16)
        sprite = frame.resize((220, 220), Image.Resampling.LANCZOS)
        thumb.alpha_composite(sprite, (15, 15))
        cx = i * tile + tile // 2
        cy = header + tile // 2
        grid.paste(thumb.convert("RGB"), (i * tile, header))
        draw.rectangle((i * tile, header, (i + 1) * tile - 1, header + tile - 1), outline="#68645b", width=2)
        draw.text((i * tile + 10, 14), f"FRAME {i + 1:02d}  {FRAME_DURATION_MS}ms", font=font, fill="#f3ead3")
        draw.line((cx - 10, cy, cx + 10, cy), fill="#e34b46", width=2)
        draw.line((cx, cy - 10, cx, cy + 10), fill="#e34b46", width=2)
    grid_path = REVIEW / "fortress_ranged__amber_lantern_glow_loop_v1_review_grid.png"
    grid.save(grid_path, optimize=True)

    # Animated composed preview: no review marks inside the animation.
    composite = Image.open(COMPOSITE).convert("RGBA")
    base_meta = json.loads(BASE_META.read_text())
    housing_meta = json.loads(HOUSING_META.read_text())
    base_size = base_meta["sizePx"]
    margin = (composite.width - base_size[0]) // 2
    position = housing_meta["attachments"]["parent"]["positionNormalized"]
    lantern_point = (margin + round(base_size[0] * position[0]), margin + round(base_size[1] * position[1]))
    housing_px = round(base_meta["footprintPx"] * housing_meta["attachments"]["parent"]["scaleToParentFootprint"])
    glow_px = round(housing_px * GLOW_TO_HOUSING)
    preview_frames = []
    for frame in frames:
        scene = checker(composite.size, 32)
        scene.alpha_composite(composite)
        glow = frame.resize((glow_px, glow_px), Image.Resampling.LANCZOS)
        scene.alpha_composite(glow, (lantern_point[0] - glow_px // 2, lantern_point[1] - glow_px // 2))
        preview_frames.append(scene.convert("RGB").resize((612, 621), Image.Resampling.LANCZOS))
    gif_path = REVIEW / "fortress_ranged__amber_lantern_glow_loop_v1_composite.gif"
    preview_frames[0].save(gif_path, save_all=True, append_images=preview_frames[1:], duration=FRAME_DURATION_MS, loop=0, optimize=True)

    total_bytes = sum((CANON / record["image"]).stat().st_size for record in frame_records)
    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "frames": len(frames),
        "frameCanvas": [FRAME_CANVAS, FRAME_CANVAS],
        "contentRect": frame_records[0]["contentRect"],
        "pivotPx": [FRAME_CANVAS // 2, FRAME_CANVAS // 2],
        "runtimeFrameBytes": total_bytes,
        "under5MB": total_bytes < 5_000_000,
        "reviewGrid": str(grid_path.relative_to(ROOT)),
        "animatedPreview": str(gif_path.relative_to(ROOT)),
        "composedGlowPx": glow_px,
    }, indent=2))


if __name__ == "__main__":
    main()

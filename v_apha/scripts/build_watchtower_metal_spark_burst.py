#!/usr/bin/env python3
"""Normalize the Watchtower spark burst and build the final destroy preview."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageSequence

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/staging/candidates/modules/fortress_ranged/watchtower__destroy_fx__metal_spark_burst_v1_source_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
DUST_PREVIEW = REVIEW / "watchtower__stone_dust_burst_v1_destroy_preview.gif"
FRAME_DURATIONS = [55, 65, 75, 95]
SCALE_TO_WEAPON = 0.34


def bbox(image: Image.Image) -> tuple[int, int, int, int]:
    value = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not value:
        raise RuntimeError("empty spark frame")
    return value


def main() -> None:
    source = Image.open(SOURCE).convert("RGBA")
    alpha = chroma_to_alpha(source)
    alpha.save(SOURCE.with_name("watchtower__destroy_fx__metal_spark_burst_v1_source_alpha.png"), optimize=True)
    w, h = alpha.size
    slots = ((0, 0, w//2, h//2), (w//2, 0, w, h//2),
             (0, h//2, w//2, h), (w//2, h//2, w, h))
    canvas = [w//2, h//2]
    pivot = [canvas[0]//2, canvas[1]//2]
    frames, records = [], []
    total_spill = 0
    for index, (slot, duration) in enumerate(zip(slots, FRAME_DURATIONS), 1):
        frame = alpha.crop(slot)
        content = bbox(frame)
        visible = [p for p in frame.getdata() if p[3] > 18]
        spill = sum(1 for r,g,b,_ in visible if r > 180 and b > 160 and g < 105 and min(r-g,b-g) > 90)
        total_spill += spill
        name = f"watchtower__destroy_fx__metal_spark_burst__frame_{index:02d}_v1_alpha.png"
        frame.save(CANON / name, optimize=True)
        frames.append(frame)
        records.append({"id": f"frame_{index:02d}", "image": name,
            "rect": {"x": 0, "y": 0, "w": frame.width, "h": frame.height},
            "contentRect": {"x": content[0], "y": content[1], "w": content[2]-content[0], "h": content[3]-content[1]},
            "pivotPx": pivot, "pivot": [0.5, 0.5], "durationMs": duration,
            "magentaSpillPixels": spill})

    source_copy = CANON / "watchtower__destroy_fx__metal_spark_burst_v1_source_chroma.png"
    source.save(source_copy, optimize=True)
    manifest = {"schemaVersion": 1, "module": "watchtower__destroy_fx__metal_spark_burst",
        "object": "watchtower", "family": "fortress_ranged", "slot": "destroy_fx",
        "sourceImage": source_copy.name, "projection": "true_top_down_orthographic_90deg",
        "attachment": {"parentModule": "watchtower__active_addon__light_single_crossbow",
            "anchor": "pivot", "scaleToParentLength": SCALE_TO_WEAPON,
            "inheritRotation": True},
        "drawOrder": 71, "frames": records,
        "animations": {"destroy_sparks": {"frames": [r["id"] for r in records],
            "loop": False, "holdLast": False, "totalDurationMs": sum(FRAME_DURATIONS)}},
        "qa": {"sharedCanvas": canvas, "sharedPivot": pivot, "runtimeLabels": False,
            "magentaSpillPixels": total_spill, "status": "canon"}}
    manifest_path = CANON / "watchtower__destroy_fx__metal_spark_burst_v1.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    tile, header = 300, 44
    grid = Image.new("RGB", (tile*4, tile+header), "#292a2b")
    draw = ImageDraw.Draw(grid)
    font = ImageFont.load_default()
    for i, frame in enumerate(frames):
        panel = checker((tile, tile), 18)
        preview = frame.resize((280, 280), Image.Resampling.LANCZOS)
        panel.alpha_composite(preview, (10, 10))
        grid.paste(panel.convert("RGB"), (i*tile, header))
        cx, cy = i*tile+tile//2, header+tile//2
        draw.text((i*tile+10, 15), f"FRAME {i+1:02d}  {FRAME_DURATIONS[i]}ms", font=font, fill="#f3ead3")
        draw.line((cx-9,cy,cx+9,cy), fill="#e34b46", width=2)
        draw.line((cx,cy-9,cx,cy+9), fill="#e34b46", width=2)
    grid_path = REVIEW / "watchtower__metal_spark_burst_v1_review_grid.png"
    grid.save(grid_path, optimize=True)

    dust_gif = Image.open(DUST_PREVIEW)
    base_frames = [f.convert("RGBA") for f in ImageSequence.Iterator(dust_gif)]
    combined = [base_frames[0].convert("RGB")]
    effect_px = round(base_frames[0].width * 0.42)
    for index, base in enumerate(base_frames[1:5]):
        spark = frames[index].resize((effect_px, effect_px), Image.Resampling.LANCZOS)
        center = (base.width//2, base.height//2)
        base.alpha_composite(spark, (center[0]-effect_px//2, center[1]-effect_px//2))
        combined.append(base.convert("RGB"))
    final_path = REVIEW / "watchtower__destroy_v1_final_preview.gif"
    combined[0].save(final_path, save_all=True, append_images=combined[1:],
        duration=[350, 85, 105, 125, 175], loop=0, optimize=True)

    total_bytes = sum((CANON / r["image"]).stat().st_size for r in records)
    print(json.dumps({"manifest": str(manifest_path.relative_to(ROOT)), "frames": 4,
        "sharedCanvas": canvas, "sharedPivot": pivot,
        "contentRects": [r["contentRect"] for r in records],
        "totalDurationMs": sum(FRAME_DURATIONS), "magentaSpillVisible": total_spill,
        "runtimeFrameBytes": total_bytes, "under5MB": total_bytes < 5_000_000,
        "reviewGrid": str(grid_path.relative_to(ROOT)),
        "finalDestroyPreview": str(final_path.relative_to(ROOT)), "previewEffectPx": effect_px}, indent=2))


if __name__ == "__main__":
    main()

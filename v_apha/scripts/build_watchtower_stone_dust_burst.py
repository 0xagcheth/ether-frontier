#!/usr/bin/env python3
"""Split, normalize, manifest, and preview the approved Watchtower dust burst."""

from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/staging/candidates/modules/fortress_ranged/watchtower__destroy_fx__stone_dust_burst_v1_source_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/fortress_ranged"
REVIEW = ROOT / "assets/staging/reviews/modules/fortress_ranged"
BASE_META = CANON / "fortress_ranged__base_token__round_light_v1.json"
IDLE_PREVIEW = REVIEW / "watchtower__range_pennant_wind_loop_v1_idle_preview.gif"
FRAME_DURATIONS = [85, 105, 125, 175]
SCALE_TO_BASE = 0.76


def bbox(image: Image.Image) -> tuple[int, int, int, int]:
    value = image.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
    if not value:
        raise RuntimeError("empty dust frame")
    return value


def main() -> None:
    source = Image.open(SOURCE).convert("RGBA")
    alpha = chroma_to_alpha(source)
    alpha.save(SOURCE.with_name("watchtower__destroy_fx__stone_dust_burst_v1_source_alpha.png"), optimize=True)
    w, h = alpha.size
    slots = ((0, 0, w // 2, h // 2), (w // 2, 0, w, h // 2),
             (0, h // 2, w // 2, h), (w // 2, h // 2, w, h))
    canvas_size = [w // 2, h // 2]
    pivot = [canvas_size[0] // 2, canvas_size[1] // 2]
    frames, records = [], []
    total_spill = 0
    for index, (slot, duration) in enumerate(zip(slots, FRAME_DURATIONS), 1):
        frame = alpha.crop(slot)
        content = bbox(frame)
        visible = [p for p in frame.getdata() if p[3] > 18]
        spill = sum(1 for r, g, b, _ in visible if r > 180 and b > 160 and g < 105 and min(r-g, b-g) > 90)
        total_spill += spill
        name = f"watchtower__destroy_fx__stone_dust_burst__frame_{index:02d}_v1_alpha.png"
        frame.save(CANON / name, optimize=True)
        frames.append(frame)
        records.append({"id": f"frame_{index:02d}", "image": name,
            "rect": {"x": 0, "y": 0, "w": frame.width, "h": frame.height},
            "contentRect": {"x": content[0], "y": content[1], "w": content[2]-content[0], "h": content[3]-content[1]},
            "pivotPx": pivot, "pivot": [0.5, 0.5], "durationMs": duration,
            "magentaSpillPixels": spill})

    source_copy = CANON / "watchtower__destroy_fx__stone_dust_burst_v1_source_chroma.png"
    source.save(source_copy, optimize=True)
    manifest = {"schemaVersion": 1, "module": "watchtower__destroy_fx__stone_dust_burst",
        "object": "watchtower", "family": "fortress_ranged", "slot": "destroy_fx",
        "sourceImage": source_copy.name, "projection": "true_top_down_orthographic_90deg",
        "attachment": {"parentModule": "fortress_ranged__base_token__round_light",
            "anchor": "objectCenter", "scaleToBaseFootprint": SCALE_TO_BASE,
            "inheritRotation": False},
        "drawOrder": 70, "frames": records,
        "animations": {"destroy_dust": {"frames": [r["id"] for r in records],
            "loop": False, "holdLast": False, "totalDurationMs": sum(FRAME_DURATIONS)}},
        "qa": {"sharedCanvas": canvas_size, "sharedPivot": pivot,
            "runtimeLabels": False, "magentaSpillPixels": total_spill, "status": "canon"}}
    manifest_path = CANON / "watchtower__destroy_fx__stone_dust_burst_v1.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    tile, header = 300, 44
    grid = Image.new("RGB", (tile * 4, tile + header), "#292a2b")
    draw = ImageDraw.Draw(grid)
    font = ImageFont.load_default()
    for i, frame in enumerate(frames):
        panel = checker((tile, tile), 18)
        preview = frame.resize((280, 280), Image.Resampling.LANCZOS)
        panel.alpha_composite(preview, (10, 10))
        grid.paste(panel.convert("RGB"), (i * tile, header))
        cx, cy = i * tile + tile // 2, header + tile // 2
        draw.text((i * tile + 10, 15), f"FRAME {i+1:02d}  {FRAME_DURATIONS[i]}ms", font=font, fill="#f3ead3")
        draw.line((cx-9, cy, cx+9, cy), fill="#e34b46", width=2)
        draw.line((cx, cy-9, cx, cy+9), fill="#e34b46", width=2)
    grid_path = REVIEW / "watchtower__stone_dust_burst_v1_review_grid.png"
    grid.save(grid_path, optimize=True)

    intact = Image.open(IDLE_PREVIEW).convert("RGBA")
    scene_size = intact.size
    center = (scene_size[0] // 2, scene_size[1] // 2)
    base_meta = json.loads(BASE_META.read_text())
    effect_px = round(scene_size[0] * 0.72)
    debris_ids = ["fortress_ranged__debris__stone_rim_chunk_a_v1",
                  "fortress_ranged__debris__stone_rim_chunk_b_v1",
                  "fortress_ranged__debris__stone_core_chunk_c_v1",
                  "watchtower__debris__crossbow_arm_shard_d_v1",
                  "watchtower__debris__crossbow_axle_bracket_e_v1"]
    directions = [(-1.0,-.25),(.65,-.75),(.35,.8),(-.55,.65),(1.0,.2)]
    preview_frames = [intact.convert("RGB")]
    for fi, dust in enumerate(frames):
        scene = checker(scene_size, 24)
        if fi == 0:
            scene.alpha_composite(intact)
        dust_scaled = dust.resize((effect_px, effect_px), Image.Resampling.LANCZOS)
        scene.alpha_composite(dust_scaled, (center[0]-effect_px//2, center[1]-effect_px//2))
        progress = (fi + 1) / len(frames)
        for asset_id, direction in zip(debris_ids, directions):
            image = Image.open(CANON / f"{asset_id}_alpha.png").convert("RGBA")
            meta = json.loads((CANON / f"{asset_id}.json").read_text())
            if "scaleToBaseFootprint" in meta["runtimeScale"]:
                width_px = round(scene_size[0] * meta["runtimeScale"]["scaleToBaseFootprint"] * .72)
            else:
                width_px = round(scene_size[0] * .72 * .72 * meta["runtimeScale"]["scaleToWeaponLength"])
            sprite = image.resize((width_px, round(image.height * width_px / image.width)), Image.Resampling.LANCZOS)
            angle = (fi + 1) * (18 if direction[0] > 0 else -16)
            sprite = sprite.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
            distance = 38 + 135 * progress
            pos = (round(center[0] + direction[0]*distance - sprite.width/2),
                   round(center[1] + direction[1]*distance - sprite.height/2))
            scene.alpha_composite(sprite, pos)
        preview_frames.append(scene.convert("RGB"))
    gif_path = REVIEW / "watchtower__stone_dust_burst_v1_destroy_preview.gif"
    preview_frames[0].save(gif_path, save_all=True, append_images=preview_frames[1:],
        duration=[350] + FRAME_DURATIONS, loop=0, optimize=True)

    total_bytes = sum((CANON / r["image"]).stat().st_size for r in records)
    print(json.dumps({"manifest": str(manifest_path.relative_to(ROOT)), "frames": len(frames),
        "sharedCanvas": canvas_size, "sharedPivot": pivot,
        "contentRects": [r["contentRect"] for r in records],
        "totalDurationMs": sum(FRAME_DURATIONS), "magentaSpillVisible": total_spill,
        "runtimeFrameBytes": total_bytes, "under5MB": total_bytes < 5_000_000,
        "reviewGrid": str(grid_path.relative_to(ROOT)),
        "assembledPreview": str(gif_path.relative_to(ROOT)), "effectRuntimePx": effect_px}, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Split and normalize Tracker's four-frame targeting-rune loop."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from prepare_fortress_ranged_stone_chunk_b import chroma_to_alpha, checker


ROOT = Path(__file__).resolve().parents[1]
NAME = "tracker__targeting_fx__rune_loop_v1"
CANDIDATES = ROOT / "assets/staging/candidates/modules/tracker"
SOURCE = CANDIDATES / f"{NAME}_source_chroma.png"
CANON = ROOT / "assets/approved/canon/modules/tracker"
REVIEW = ROOT / "assets/staging/reviews/modules/tracker"
WEAPON_PREVIEW = REVIEW / "tracker__aim_child__scan_optics_ring_v1_weapon_composite.png"
RING_IMAGE = CANON / "tracker__aim_child__scan_optics_ring_v1_alpha.png"
BASE_FOOTPRINT = 1082
SCALE_TO_BASE = 0.34
TIMINGS = [180, 180, 240, 220]
# ImageGen returned the lower pair swapped relative to requested reading order.
# Runtime scan order is top -> right -> bottom lock -> left fade.
QUADRANTS = [(0, 0), (1, 0), (1, 1), (0, 1)]


def main() -> None:
    CANON.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGBA")
    cell_w, cell_h = source.width // 2, source.height // 2
    frames = []
    spill_counts = []
    for index, (col, row) in enumerate(QUADRANTS, 1):
        quadrant = source.crop((col * cell_w, row * cell_h, (col + 1) * cell_w, (row + 1) * cell_h))
        alpha_full = chroma_to_alpha(quadrant)
        box = alpha_full.getchannel("A").point(lambda a: 255 if a > 18 else 0).getbbox()
        if not box:
            raise RuntimeError(f"empty targeting rune frame {index}")
        crop = alpha_full.crop(box)
        pivot = [cell_w // 2 - box[0], cell_h // 2 - box[1]]
        spill = sum(1 for r, g, b, a in crop.getdata()
                    if a > 18 and r > 150 and b > 135 and g < 120 and min(r-g, b-g) > 60)
        path = CANON / f"{NAME}__frame_{index:02d}.png"
        crop.save(path, optimize=True)
        frames.append({"id": f"targeting_rune_{index:02d}", "image": path.name,
                       "rect": {"x": 0, "y": 0, "w": crop.width, "h": crop.height},
                       "sizePx": list(crop.size), "sourceSize": [cell_w, cell_h],
                       "trimOffset": [box[0], box[1]], "pivotPx": pivot,
                       "durationMs": TIMINGS[index - 1]})
        spill_counts.append(spill)

    manifest = {
        "schemaVersion": 1, "module": "tracker__targeting_fx__rune_loop", "object": "tracker",
        "family": "fortress_ranged", "slot": "targeting_fx",
        "sourceImage": SOURCE.name, "projection": "true_top_down_orthographic_90deg",
        "sharedSourceSize": [cell_w, cell_h], "sharedPivotInSourcePx": [cell_w // 2, cell_h // 2],
        "runtimeScale": {"scaleToBaseFootprint": SCALE_TO_BASE},
        "attachments": {"parent": {"module": "tracker__active_primary__long_range_crossbow", "anchor": "scan_ring_socket", "inheritRotation": True}},
        "animation": {"id": "targeting_scan", "frames": [f["id"] for f in frames],
                      "durationsMs": TIMINGS, "loop": True, "totalDurationMs": sum(TIMINGS)},
        "drawOrder": 31, "frames": frames,
        "qa": {"transparent": True, "tightRects": True, "stableSourceFootprint": True,
               "openCenter": True, "magentaSpillPixelsByFrame": spill_counts,
               "magentaSpillPixels": sum(spill_counts),
               "under5MB": all((CANON / f["image"]).stat().st_size < 5_000_000 for f in frames),
               "status": "canon" if sum(spill_counts) == 0 else "needs_despill"},
    }
    manifest_path = CANON / f"{NAME}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    tile, header = 360, 42
    grid = Image.new("RGB", (tile * 4, tile + header), "#292a2b")
    font = ImageFont.load_default()
    rgba_frames = []
    for index, frame in enumerate(frames):
        image = Image.open(CANON / frame["image"]).convert("RGBA")
        panel = checker((tile, tile), 18)
        scale = min(320 / image.width, 320 / image.height)
        shown = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
        panel.alpha_composite(shown, ((tile - shown.width) // 2, (tile - shown.height) // 2))
        grid.paste(panel.convert("RGB"), (index * tile, header))
        ImageDraw.Draw(grid).text((index * tile + 10, 15), f"FRAME {index+1:02d} / {TIMINGS[index]} MS", font=font, fill="#f3ead3")
        rgba_frames.append(image)
    review_path = REVIEW / f"{NAME}_review_grid.png"
    grid.save(review_path, optimize=True)

    base = Image.open(WEAPON_PREVIEW).convert("RGBA")
    center = (base.width // 2, base.height // 2)
    target_source_w = round(BASE_FOOTPRINT * SCALE_TO_BASE)
    ring_source = Image.open(RING_IMAGE).convert("RGBA")
    ring_w = round(844 * 0.25)
    ring = ring_source.resize((ring_w, round(ring_source.height * ring_w / ring_source.width)), Image.Resampling.LANCZOS)
    gif_frames = []
    for frame, image in zip(frames, rgba_frames):
        scale = target_source_w / frame["sourceSize"][0]
        shown = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
        pivot = [round(frame["pivotPx"][0] * scale), round(frame["pivotPx"][1] * scale)]
        scene = base.copy()
        scene.alpha_composite(shown, (center[0] - pivot[0], center[1] - pivot[1]))
        # Runtime order is weapon (30), rune (31), metal scan ring (32).
        scene.alpha_composite(ring, (center[0] - ring.width // 2, center[1] - ring.height // 2))
        gif_frames.append(scene.convert("P", palette=Image.Palette.ADAPTIVE, colors=255))
    gif_path = REVIEW / f"{NAME}_weapon_preview.gif"
    gif_frames[0].save(gif_path, save_all=True, append_images=gif_frames[1:], duration=TIMINGS, loop=0, disposal=2)
    print(json.dumps({"manifest": str(manifest_path.relative_to(ROOT)), "frameCount": len(frames),
                      "sourceCell": [cell_w, cell_h], "durationsMs": TIMINGS,
                      "spillPixelsByFrame": spill_counts,
                      "reviewGrid": str(review_path.relative_to(ROOT)),
                      "weaponPreview": str(gif_path.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()

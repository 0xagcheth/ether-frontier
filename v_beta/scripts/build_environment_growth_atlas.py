#!/usr/bin/env python3
"""Build a transparent 384px environment growth atlas and final idle sprite."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from PIL import Image

from build_runtime_sprite_pack import key_to_alpha, split_grid


FRAME = 384
FINAL_EXTENT = 255


def normalize_growth(frames: list[Image.Image]) -> list[Image.Image]:
    final_bbox = frames[-1].getchannel("A").getbbox()
    if final_bbox is None:
        raise ValueError("final growth frame is empty")
    extent = max(final_bbox[2] - final_bbox[0], final_bbox[3] - final_bbox[1])
    scale = FINAL_EXTENT / extent
    output = []
    previous_extent = 0
    for frame in frames:
        resized = frame.resize(
            (max(1, round(frame.width * scale)), max(1, round(frame.height * scale))),
            Image.Resampling.LANCZOS,
        )
        bbox = resized.getchannel("A").getbbox()
        canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
        if bbox is not None:
            content = resized.crop(bbox)
            current_extent = max(content.width, content.height)
            if current_extent < previous_extent:
                correction = previous_extent / current_extent
                content = content.resize(
                    (round(content.width * correction), round(content.height * correction)),
                    Image.Resampling.LANCZOS,
                )
                current_extent = max(content.width, content.height)
            previous_extent = current_extent
            canvas.alpha_composite(content, ((FRAME - content.width) // 2, (FRAME - content.height) // 2))
        output.append(canvas)
    return output


def build(source: Path, output_dir: Path, slug: str) -> None:
    image = Image.open(source)
    frames = [key_to_alpha(frame) for frame in split_grid(image, 4, 2, 0)]
    frames = normalize_growth(frames)
    output_dir.mkdir(parents=True, exist_ok=True)
    atlas = Image.new("RGBA", (FRAME * 8, FRAME), (0, 0, 0, 0))
    frame_dir = output_dir / "frames"
    frame_dir.mkdir(parents=True, exist_ok=True)
    for index, frame in enumerate(frames):
        atlas.alpha_composite(frame, (index * FRAME, 0))
        frame.save(frame_dir / f"{slug}-grow-{index + 1:02d}.png", optimize=True)
    atlas.save(output_dir / f"{slug}-grow-384-alpha.png", optimize=True)
    frames[-1].save(output_dir / f"{slug}-idle-384-alpha.png", optimize=True)
    bounds = [frame.getchannel("A").getbbox() for frame in frames]
    extents = [max(box[2] - box[0], box[3] - box[1]) if box else 0 for box in bounds]
    clipped = [
        index + 1
        for index, box in enumerate(bounds)
        if box and (box[0] <= 0 or box[1] <= 0 or box[2] >= FRAME or box[3] >= FRAME)
    ]
    monotonic = all(current >= previous for previous, current in zip(extents, extents[1:]))
    if clipped or not monotonic:
        raise ValueError(f"growth QA failed: clipped={clipped}, extents={extents}")
    manifest = {
        "object": slug,
        "format": "RGBA PNG",
        "frameSize": [FRAME, FRAME],
        "pivot": [0.5, 0.5],
        "idle": {"file": f"{slug}-idle-384-alpha.png", "frame": 8},
        "grow": {
            "file": f"{slug}-grow-384-alpha.png",
            "columns": 8,
            "rows": 1,
            "frameDurationMs": 120,
            "loop": False,
            "holdLast": True,
        },
        "normalization": "final frame extent 255px in a 384px safety cell; centered content",
        "qa": {
            "extents": extents,
            "monotonic": monotonic,
            "clippedFrames": clipped,
        },
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: build_environment_growth_atlas.py SOURCE OUTPUT_DIR SLUG")
    build(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3])

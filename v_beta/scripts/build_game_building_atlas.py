#!/usr/bin/env python3
"""Pack one 384px building runtime set for the browser game."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from PIL import Image


FRAME = 384


def build(runtime_dir: Path, output_dir: Path, slug: str) -> None:
    manifest = json.loads((runtime_dir / "manifest.json").read_text())
    actions = manifest["actions"]
    animated = [(name, spec) for name, spec in actions.items() if "frames" in spec]
    rows = len(animated)
    columns = max(spec["frames"] for _, spec in animated)
    atlas = Image.new("RGBA", (columns * FRAME, rows * FRAME), (0, 0, 0, 0))
    frames: dict[str, dict] = {}
    animations: dict[str, dict] = {}

    for row, (action, spec) in enumerate(animated):
        strip = Image.open(runtime_dir / spec["file"]).convert("RGBA")
        names = []
        for index in range(spec["frames"]):
            frame = strip.crop((index * FRAME, 0, (index + 1) * FRAME, FRAME))
            x, y = index * FRAME, row * FRAME
            atlas.alpha_composite(frame, (x, y))
            name = f"{slug}_{action}_{index + 1:02d}"
            names.append(name)
            frames[name] = {
                "frame": {"x": x, "y": y, "w": FRAME, "h": FRAME},
                "spriteSourceSize": {"x": 0, "y": 0, "w": FRAME, "h": FRAME},
                "sourceSize": {"w": FRAME, "h": FRAME},
            }
        animations[action] = {
            "frames": names,
            "durationMs": spec["durationMs"],
            "loop": spec["loop"],
        }

    output_dir.mkdir(parents=True, exist_ok=True)
    image_name = f"{slug}_atlas.png"
    atlas.save(output_dir / image_name, optimize=True)
    data = {
        "frames": frames,
        "animations": animations,
        "meta": {"image": image_name, "size": {"w": atlas.width, "h": atlas.height}},
    }
    metadata_path = output_dir / f"{slug}_atlas.json"
    metadata_path.write_text(json.dumps(data, indent=2) + "\n")
    registry = {
        path.name.removesuffix("_atlas.json"): json.loads(path.read_text())
        for path in sorted(output_dir.glob("*_atlas.json"))
    }
    (output_dir / "building_atlases.js").write_text(
        "window.BUILDING_SPRITE_ATLASES = " + json.dumps(registry, separators=(",", ":")) + ";\n"
    )


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: build_game_building_atlas.py RUNTIME_DIR OUTPUT_DIR SLUG")
    build(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3])

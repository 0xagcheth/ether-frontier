#!/usr/bin/env python3
import json
import sys
from pathlib import Path

from PIL import Image


def main() -> int:
    if len(sys.argv) not in (4, 7, 8):
        print(
            "usage: prepare_static_tree_candidate.py <input-alpha-png> <atlas-png> <atlas-json> "
            "[object-name frame-name category [cell-size]]"
        )
        return 2

    source_path = Path(sys.argv[1])
    atlas_path = Path(sys.argv[2])
    json_path = Path(sys.argv[3])

    cell_arg = sys.argv[7] if len(sys.argv) == 8 else "96"
    if "x" in cell_arg:
        cell_w, cell_h = [int(part) for part in cell_arg.lower().split("x", 1)]
    else:
        cell_w = cell_h = int(cell_arg)
    padding = 6
    object_name = sys.argv[4] if len(sys.argv) >= 7 else "tree_oak"
    frame_name = sys.argv[5] if len(sys.argv) >= 7 else "tree_oak_static_0"
    category = sys.argv[6] if len(sys.argv) >= 7 else "environment.decor.tree"
    kind = "building" if category.startswith("building.") else "decor"

    src = Image.open(source_path).convert("RGBA")
    alpha = src.getchannel("A")
    bbox = alpha.getbbox()
    if not bbox:
        raise ValueError(f"no alpha content found in {source_path}")

    cutout = src.crop(bbox)
    max_draw_w = cell_w - padding * 2
    max_draw_h = cell_h - padding * 2
    scale = min(max_draw_w / cutout.width, max_draw_h / cutout.height)
    draw_w = max(1, round(cutout.width * scale))
    draw_h = max(1, round(cutout.height * scale))
    resized = cutout.resize((draw_w, draw_h), Image.Resampling.LANCZOS)

    pixels = resized.load()
    for py in range(resized.height):
        for px in range(resized.width):
            r, g, b, a = pixels[px, py]
            if a > 0 and r < 18 and g < 18 and b < 18:
                pixels[px, py] = (24, 29, 40, a)

    atlas = Image.new("RGBA", (cell_w, cell_h), (0, 0, 0, 0))
    x = (cell_w - draw_w) // 2
    y = cell_h - padding - draw_h
    atlas.alpha_composite(resized, (x, y))
    atlas.save(atlas_path)

    meta = {
        "meta": {
            "image": atlas_path.name,
            "format": "RGBA8888",
            "size": {"w": cell_w, "h": cell_h},
            "scale": 1,
            "trimmed": False,
            "layout": "single static frame",
            "object": object_name,
            "category": category,
            "atlasType": "static",
            "cell": {"w": cell_w, "h": cell_h},
            "source": source_path.name,
        },
        "frames": {
            frame_name: {
                "frame": {"x": 0, "y": 0, "w": cell_w, "h": cell_h},
                "sourceSize": {"w": cell_w, "h": cell_h},
                "spriteSourceSize": {"x": 0, "y": 0, "w": cell_w, "h": cell_h},
                "pivot": {"x": cell_w // 2, "y": cell_h - padding},
                "tags": {
                    "kind": kind,
                    "object": object_name,
                    "action": "static",
                    "candidateCanon": True,
                },
            }
        },
        "animations": {
            "static": {
                "frames": [frame_name],
                "fps": 1,
                "loop": False,
                "holdLast": True,
            }
        },
    }
    json_path.write_text(json.dumps(meta, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Build a normalized transparent 384px static environment sprite."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from PIL import Image

from build_runtime_sprite_pack import key_to_alpha


FRAME = 384
TARGET_EXTENT = 255


def normalize(image: Image.Image) -> Image.Image:
    image = key_to_alpha(image.convert("RGBA"))
    bbox = image.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("source sprite is empty after chroma-key removal")
    content = image.crop(bbox)
    scale = TARGET_EXTENT / max(content.width, content.height)
    content = content.resize(
        (max(1, round(content.width * scale)), max(1, round(content.height * scale))),
        Image.Resampling.LANCZOS,
    )
    canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
    canvas.alpha_composite(content, ((FRAME - content.width) // 2, (FRAME - content.height) // 2))
    return canvas


def build(source: Path, output_dir: Path, slug: str) -> None:
    sprite = normalize(Image.open(source))
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{slug}-idle-384-alpha.png"
    sprite.save(output_dir / filename, optimize=True)
    bbox = sprite.getchannel("A").getbbox()
    if bbox is None or bbox[0] <= 0 or bbox[1] <= 0 or bbox[2] >= FRAME or bbox[3] >= FRAME:
        raise ValueError(f"unsafe sprite bounds: {bbox}")
    manifest = {
        "object": slug,
        "format": "RGBA PNG",
        "frameSize": [FRAME, FRAME],
        "pivot": [0.5, 0.5],
        "idle": {"file": filename},
        "bounds": list(bbox),
        "normalization": "object extent 255px in a 384px safety cell; centered content",
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: build_environment_static.py SOURCE OUTPUT_DIR SLUG")
    build(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3])

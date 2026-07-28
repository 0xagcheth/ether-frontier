import json
import math
from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "assets/staging/candidates/watchtower/decomposition_v3"
    / "watchtower_crossbow_unstrung_master_v1_alpha.png"
)
OUT = ROOT / "assets/staging/candidates/watchtower/decomposition_v3/crossbow_layers_v4"
MANIFEST = OUT / "watchtower_crossbow_layers_v4.fragment.json"
NORMALIZED = OUT / "crossbow_unstrung_normalized_reference.png"
COMPOSITE = (
    ROOT
    / "assets/staging/candidates/watchtower/decomposition_v3"
    / "watchtower_crossbow_unstrung_composite_v4.png"
)

CANVAS = (1254, 1254)
PIVOT = (627, 627)
TARGET = (540, 529)


def normalize() -> Image.Image:
    source = Image.open(SOURCE).convert("RGBA")
    bbox = source.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("Empty unstrung master")
    image = source.crop(bbox)
    ratio = min(TARGET[0] / image.width, TARGET[1] / image.height)
    size = (round(image.width * ratio), round(image.height * ratio))
    image = image.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    position = (PIVOT[0] - size[0] // 2, PIVOT[1] - size[1] // 2)
    canvas.alpha_composite(image, position)
    canvas.save(NORMALIZED, optimize=True)
    return canvas


def save_part(
    source: Image.Image, mask: np.ndarray, layer_id: str, draw_order: int
) -> dict:
    alpha = np.asarray(source.getchannel("A"))
    part_alpha = np.where(mask, alpha, 0).astype(np.uint8)
    part = source.copy()
    part.putalpha(Image.fromarray(part_alpha))
    bbox = part.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError(f"{layer_id} is empty")
    tight = part.crop(bbox)
    path = OUT / f"{layer_id}.png"
    tight.save(path, optimize=True)
    return {
        "id": layer_id,
        "file": path.name,
        "sourceRect": {
            "x": bbox[0],
            "y": bbox[1],
            "w": bbox[2] - bbox[0],
            "h": bbox[3] - bbox[1],
        },
        "pivot": {"x": PIVOT[0] - bbox[0], "y": PIVOT[1] - bbox[1]},
        "attachment": "active_primary_pivot",
        "parent": "crossbow_group",
        "drawOrder": draw_order,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    source = normalize()
    alpha = np.asarray(source.getchannel("A"))
    yy, xx = np.indices((CANVAS[1], CANVAS[0]))
    perpendicular = (xx + yy - PIVOT[0] - PIVOT[1]) / math.sqrt(2)
    visible = alpha > 0

    left_mask = visible & (perpendicular < -46)
    right_mask = visible & (perpendicular > 46)
    body_mask = visible & (np.abs(perpendicular) <= 112)

    layers = [
        save_part(source, left_mask, "crossbow_left_arm_stack", 120),
        save_part(source, right_mask, "crossbow_right_arm_stack", 121),
        save_part(source, body_mask, "crossbow_body_stack", 130),
    ]

    reconstructed = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    for layer in layers:
        image = Image.open(OUT / layer["file"]).convert("RGBA")
        reconstructed.alpha_composite(
            image, (layer["sourceRect"]["x"], layer["sourceRect"]["y"])
        )
    reconstructed.save(COMPOSITE, optimize=True)

    manifest = {
        "schema": "ether-frontier.layer-fragment.v1",
        "object": "watchtower",
        "group": "crossbow_group",
        "projectionMaster": "watchtower_projection_master_v4",
        "geometrySource": "watchtower_crossbow_unstrung_master_v1",
        "activePrimaryPivot": {"x": PIVOT[0], "y": PIVOT[1]},
        "normalization": {"target": {"w": TARGET[0], "h": TARGET[1]}},
        "layers": layers,
        "pending": [
            "loaded_bolt",
            "crossbow_string_tense",
            "crossbow_string_release_01..02",
            "crossbow_recoil_overlay_01..03",
        ],
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(MANIFEST)
    print(COMPOSITE)


if __name__ == "__main__":
    main()

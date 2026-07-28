import json
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets/staging/candidates/watchtower/decomposition_v3"
OUT = SOURCE_DIR / "crossbow_layers"
MANIFEST = OUT / "watchtower_crossbow_layers_v3.fragment.json"
COMPOSITE = SOURCE_DIR / "watchtower_crossbow_composite_v3.png"

CANVAS = (1254, 1254)
PIVOT = (627, 627)

SOURCES = {
    "crossbow_body_stack": {
        "file": "watchtower_crossbow_body_stack_v1_alpha.png",
        "max_size": (570, 570),
        "center": (627, 627),
        "drawOrder": 130,
    },
    "crossbow_arm_stacks": {
        "file": "watchtower_crossbow_arm_stacks_v1_alpha.png",
        "max_size": (500, 500),
        "center": (627, 627),
        "drawOrder": 120,
    },
    "loaded_bolt": {
        "file": "watchtower_loaded_bolt_v1_alpha.png",
        "max_size": (430, 430),
        "center": (735, 520),
        "drawOrder": 170,
    },
}


def tight(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    bbox = image.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("Empty image")
    return image.crop(bbox)


def normalize(spec: dict) -> Image.Image:
    image = tight(Image.open(SOURCE_DIR / spec["file"]))
    image.thumbnail(spec["max_size"], Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    x = round(spec["center"][0] - image.width / 2)
    y = round(spec["center"][1] - image.height / 2)
    canvas.alpha_composite(image, (x, y))
    return canvas


def save_tight(
    canvas: Image.Image,
    layer_id: str,
    draw_order: int,
    parent: str = "crossbow_group",
) -> dict:
    bbox = canvas.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError(f"{layer_id} is empty")
    image = canvas.crop(bbox)
    path = OUT / f"{layer_id}.png"
    image.save(path, optimize=True)
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
        "parent": parent,
        "drawOrder": draw_order,
    }


def split_arms(canvas: Image.Image) -> list[Image.Image]:
    alpha = np.asarray(canvas.getchannel("A"))
    mask = alpha > 24
    labels, count = ndimage.label(mask)
    components = []
    for label_id in range(1, count + 1):
        component = labels == label_id
        area = int(component.sum())
        if area > 4000:
            cy, cx = ndimage.center_of_mass(component)
            components.append((cx, cy, component))
    if len(components) != 2:
        raise ValueError(f"Expected two arm components, got {len(components)}")
    components.sort(key=lambda item: item[0] + item[1])
    outputs = []
    for _cx, _cy, component in components:
        expanded = ndimage.binary_dilation(component, iterations=1)
        part = canvas.copy()
        part.putalpha(Image.fromarray((expanded * alpha).astype(np.uint8)))
        outputs.append(part)
    return outputs


def translate(canvas: Image.Image, dx: int, dy: int) -> Image.Image:
    moved = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    moved.alpha_composite(canvas, (dx, dy))
    return moved


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    normalized = {name: normalize(spec) for name, spec in SOURCES.items()}

    layers = []
    arm_parts = split_arms(normalized["crossbow_arm_stacks"])
    arm_parts[0] = translate(arm_parts[0], 30, -24)
    arm_parts[1] = translate(arm_parts[1], -72, -112)
    layers.append(save_tight(arm_parts[0], "crossbow_left_arm_stack", 120))
    layers.append(save_tight(arm_parts[1], "crossbow_right_arm_stack", 121))
    layers.append(
        save_tight(normalized["crossbow_body_stack"], "crossbow_body_stack", 130)
    )
    layers.append(save_tight(normalized["loaded_bolt"], "loaded_bolt", 170))

    composite = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    composite.alpha_composite(arm_parts[0])
    composite.alpha_composite(arm_parts[1])
    composite.alpha_composite(normalized["crossbow_body_stack"])
    composite.alpha_composite(normalized["loaded_bolt"])
    composite.save(COMPOSITE, optimize=True)

    manifest = {
        "schema": "ether-frontier.layer-fragment.v1",
        "object": "watchtower",
        "group": "crossbow_group",
        "projectionMaster": "watchtower_projection_master_v4",
        "activePrimaryPivot": {"x": PIVOT[0], "y": PIVOT[1]},
        "layers": layers,
        "pending": [
            "crossbow_body_lower",
            "crossbow_body_upper",
            "crossbow_trigger_block",
            "crossbow_fastener_01..04",
            "crossbow_string_tense",
            "crossbow_string_release_01..02",
            "crossbow_recoil_overlay_01..03",
        ],
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(layers)} crossbow layers")
    print(MANIFEST)
    print(COMPOSITE)


if __name__ == "__main__":
    main()

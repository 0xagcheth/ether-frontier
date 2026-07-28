import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "assets/staging/candidates/watchtower/decomposition_v3"
    / "watchtower_bearing_group_v1_alpha.png"
)
OUT = ROOT / "assets/staging/candidates/watchtower/decomposition_v3/bearing_layers"
MANIFEST = OUT / "watchtower_bearing_layers_v3.fragment.json"
NORMALIZED = OUT / "bearing_group_normalized_reference.png"

CANVAS_SIZE = 1254
CENTER = (627, 627)
TARGET_DIAMETER = 500


def normalize_source() -> Image.Image:
    source = Image.open(SOURCE).convert("RGBA")
    bbox = source.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("Bearing source is empty")
    tight = source.crop(bbox)
    tight.thumbnail((TARGET_DIAMETER, TARGET_DIAMETER), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    x = CENTER[0] - tight.width // 2
    y = CENTER[1] - tight.height // 2
    canvas.alpha_composite(tight, (x, y))
    canvas.save(NORMALIZED, optimize=True)
    return canvas


def ring_mask(inner: int, outer: int) -> Image.Image:
    mask = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(
        (
            CENTER[0] - outer,
            CENTER[1] - outer,
            CENTER[0] + outer,
            CENTER[1] + outer,
        ),
        fill=255,
    )
    if inner:
        draw.ellipse(
            (
                CENTER[0] - inner,
                CENTER[1] - inner,
                CENTER[0] + inner,
                CENTER[1] + inner,
            ),
            fill=0,
        )
    return mask


def save_layer(
    source: Image.Image,
    mask: Image.Image,
    layer_id: str,
    draw_order: int,
    runtime_candidate: bool = True,
) -> dict:
    alpha = ImageChops.multiply(source.getchannel("A"), mask)
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError(f"{layer_id} is empty")
    image = source.crop(bbox)
    image.putalpha(alpha.crop(bbox))
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
        "pivot": {
            "x": CENTER[0] - bbox[0],
            "y": CENTER[1] - bbox[1],
        },
        "attachment": "object_center",
        "drawOrder": draw_order,
        "runtimeCandidate": runtime_candidate,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    source = normalize_source()
    pixels = np.asarray(source)
    red, green, blue, alpha = (pixels[:, :, index] for index in range(4))

    layers = [
        save_layer(source, ring_mask(112, 250), "bearing_lower_washer", 90),
        save_layer(source, ring_mask(48, 112), "bearing_upper_washer", 100),
        save_layer(source, ring_mask(0, 48), "bearing_socket", 110),
    ]

    copper = (
        (alpha > 100)
        & (red > 105)
        & (red.astype(int) > green.astype(int) + 15)
        & (green.astype(int) > blue.astype(int) + 8)
    )
    copper = ndimage.binary_opening(copper, iterations=1)
    labels, count = ndimage.label(copper)
    components = []
    for label_id in range(1, count + 1):
        component = labels == label_id
        area = int(component.sum())
        if area < 180:
            continue
        cy, cx = ndimage.center_of_mass(component)
        radius = ((cx - CENTER[0]) ** 2 + (cy - CENTER[1]) ** 2) ** 0.5
        if 145 <= radius <= 245:
            components.append((area, label_id))
    components.sort(reverse=True)

    for index, (_area, label_id) in enumerate(components[:4], start=1):
        component = labels == label_id
        component = ndimage.binary_dilation(component, iterations=2)
        mask = Image.fromarray((component * 255).astype(np.uint8), mode="L")
        layers.append(
            save_layer(
                source,
                mask,
                f"bearing_copper_route_{index:02d}",
                94 + index,
            )
        )

    manifest = {
        "schema": "ether-frontier.layer-fragment.v1",
        "object": "watchtower",
        "group": "bearing_group",
        "projectionMaster": "watchtower_projection_master_v4",
        "normalization": {
            "source": SOURCE.name,
            "targetDiameter": TARGET_DIAMETER,
            "center": {"x": CENTER[0], "y": CENTER[1]},
        },
        "layers": layers,
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(layers)} bearing layers")
    print(MANIFEST)


if __name__ == "__main__":
    main()

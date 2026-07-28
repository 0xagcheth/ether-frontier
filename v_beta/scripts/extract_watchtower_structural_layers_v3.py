import json
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "assets/staging/candidates/watchtower/decomposition_v3"
    / "watchtower_structural_base_master_v1_alpha.png"
)
OUT = ROOT / "assets/staging/candidates/watchtower/decomposition_v3/structural_layers"
MANIFEST = OUT / "watchtower_structural_layers_v3.fragment.json"

CANVAS = (1254, 1254)
CENTER = (627.0, 627.0)


def angle_mask(start_deg: float, end_deg: float, inner: float, outer: float) -> Image.Image:
    mask = Image.new("L", CANVAS, 0)
    draw = ImageDraw.Draw(mask)
    points = []
    steps = max(12, round(abs(end_deg - start_deg) * 2))
    for index in range(steps + 1):
        angle = math.radians(start_deg + (end_deg - start_deg) * index / steps)
        points.append(
            (
                CENTER[0] + outer * math.cos(angle),
                CENTER[1] + outer * math.sin(angle),
            )
        )
    for index in range(steps, -1, -1):
        angle = math.radians(start_deg + (end_deg - start_deg) * index / steps)
        points.append(
            (
                CENTER[0] + inner * math.cos(angle),
                CENTER[1] + inner * math.sin(angle),
            )
        )
    draw.polygon(points, fill=255)
    return mask


def radial_mask(inner: float, outer: float) -> Image.Image:
    mask = Image.new("L", CANVAS, 0)
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
    if inner > 0:
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
    source_alpha: Image.Image,
    mask: Image.Image,
    layer_id: str,
    draw_order: int,
    runtime_candidate: bool = True,
) -> dict:
    alpha = ImageChops.multiply(source_alpha, mask)
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError(f"{layer_id} is empty")
    tight = source.crop(bbox)
    tight.putalpha(alpha.crop(bbox))
    path = OUT / f"{layer_id}.png"
    tight.save(path, optimize=True)
    pivot = {
        "x": round(CENTER[0] - bbox[0], 3),
        "y": round(CENTER[1] - bbox[1], 3),
    }
    return {
        "id": layer_id,
        "file": path.name,
        "sourceCanvas": {"width": CANVAS[0], "height": CANVAS[1]},
        "sourceRect": {
            "x": bbox[0],
            "y": bbox[1],
            "w": bbox[2] - bbox[0],
            "h": bbox[3] - bbox[1],
        },
        "pivot": pivot,
        "drawOrder": draw_order,
        "runtimeCandidate": runtime_candidate,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGBA")
    source_alpha = source.getchannel("A")
    layers = []

    layers.append(
        save_layer(
            source,
            source_alpha,
            radial_mask(0, 474),
            "deck_full_reference",
            20,
            False,
        )
    )

    for index in range(8):
        start = -90 + index * 45 + 0.7
        end = -90 + (index + 1) * 45 - 0.7
        layers.append(
            save_layer(
                source,
                source_alpha,
                angle_mask(start, end, 0, 444),
                f"deck_sector_{index + 1:02d}",
                30 + index,
            )
        )

    pixels = np.asarray(source)
    yy, xx = np.indices((CANVAS[1], CANVAS[0]))
    radius = np.hypot(xx - CENTER[0], yy - CENTER[1])
    red, green, blue, alpha = (pixels[:, :, index] for index in range(4))
    stone_faces = (
        (alpha > 200)
        & (radius > 455)
        & (radius < 585)
        & (red > 50)
        & (green > 50)
        & (blue > 50)
        & (blue.astype(int) >= red.astype(int) + 3)
        & (green.astype(int) >= red.astype(int) - 1)
    )
    stone_faces = ndimage.binary_closing(stone_faces, iterations=1)
    labels, label_count = ndimage.label(stone_faces)
    centers = []
    for label_id in range(1, label_count + 1):
        component = labels == label_id
        area = int(component.sum())
        if area < 1500:
            continue
        cy, cx = ndimage.center_of_mass(component)
        angle = math.degrees(math.atan2(cy - CENTER[1], cx - CENTER[0])) % 360
        centers.append((angle, area, cx, cy))
    centers.sort()
    if len(centers) != 20:
        raise ValueError(f"Expected 20 stone faces, detected {len(centers)}")

    extended = [centers[-1][0] - 360] + [item[0] for item in centers] + [
        centers[0][0] + 360
    ]
    for index, (angle, _area, _cx, _cy) in enumerate(centers):
        previous_angle = extended[index]
        next_angle = extended[index + 2]
        start = (previous_angle + angle) / 2 + 0.25
        end = (angle + next_angle) / 2 - 0.25
        layers.append(
            save_layer(
                source,
                source_alpha,
                angle_mask(start, end, 440, 604),
                f"parapet_stone_{index + 1:02d}",
                60 + index,
            )
        )

    manifest = {
        "schema": "ether-frontier.layer-fragment.v1",
        "object": "watchtower",
        "projectionMaster": "watchtower_projection_master_v4",
        "coordinateSystem": {
            "canvas": {"width": CANVAS[0], "height": CANVAS[1]},
            "objectCenter": {"x": CENTER[0], "y": CENTER[1]},
        },
        "layers": layers,
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(layers)} layers")
    print(MANIFEST)


if __name__ == "__main__":
    main()

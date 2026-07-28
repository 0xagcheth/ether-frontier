#!/usr/bin/env python3
"""Compose production 384px Watchtower animations from Layered Object v2."""

from __future__ import annotations

import json
import math
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/sprite-atlases/watchtower/layered-v2-candidate"
OUT = ROOT / "assets/sprite-atlases/watchtower/layered-runtime-384"
FRAME = 384
BASE_EXTENT = 255


def load_parts():
    manifest = json.loads((SOURCE / "watchtower_layered_manifest.json").read_text())
    atlas = Image.open(SOURCE / manifest["image"]).convert("RGBA")
    parts = {}
    for name, entry in manifest["sprites"].items():
        r = entry["rect"]
        parts[name] = atlas.crop((r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"]))
    return parts


def scaled(image, factor):
    return image.resize((max(1, round(image.width * factor)), max(1, round(image.height * factor))), Image.Resampling.LANCZOS)


def center(canvas, image, point=(192, 192), offset=(0, 0)):
    canvas.alpha_composite(image, (round(point[0] - image.width / 2 + offset[0]), round(point[1] - image.height / 2 + offset[1])))


def assemble(parts, flag=1, flame=1, flash=None, recoil=0, weapon_angle=0):
    canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
    scale = BASE_EXTENT / max(parts["base_stone_token"].size)
    base = scaled(parts["base_stone_token"], scale)
    socket = scaled(parts["central_socket"], scale * .72)
    weapon = scaled(parts["crossbow_rotatable"], scale * .92)
    pole = scaled(parts["flag_pole"], scale * .42)
    cloth = scaled(parts[f"flag_cloth_wind_{flag:02d}"], scale * .36)
    lantern = scaled(parts["lantern_body"], scale * .38)
    fire = scaled(parts[f"lantern_flame_{flame:02d}"], scale * .30)
    center(canvas, base)
    center(canvas, socket)
    # Accessories stay inside the locked base footprint.
    center(canvas, pole, offset=(-75, -25))
    canvas.alpha_composite(cloth, (118, 105 - cloth.height // 2))
    center(canvas, lantern, offset=(-68, 67))
    center(canvas, fire, offset=(-68, 67))
    weapon = weapon.rotate(weapon_angle, Image.Resampling.BICUBIC, expand=True)
    center(canvas, weapon, offset=(-recoil, 0))
    if flash is not None:
        fx = scaled(parts[f"muzzle_flash_{flash:02d}"], scale * .30)
        center(canvas, fx, point=(192, 192), offset=(weapon.width // 2 - recoil - 4, 0))
    return canvas


def destroy_frames(parts):
    intact = assemble(parts, 2, 2)
    scale = BASE_EXTENT / max(parts["base_stone_token"].size)
    names = [n for n in parts if n.startswith("destroy_debris_")]
    frames = [intact]
    for phase in range(1, 5):
        canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
        # A fading base keeps frame 2 readable, then yields to independent pieces.
        if phase == 1:
            ghost = intact.copy()
            ghost.putalpha(ghost.getchannel("A").point(lambda a: round(a * .42)))
            canvas.alpha_composite(ghost)
        radius = 18 + phase * 24
        for i, name in enumerate(names):
            piece = scaled(parts[name], scale * (.58 - phase * .055))
            angle = math.tau * i / len(names) + .31
            x = 192 + math.cos(angle) * radius
            y = 192 + math.sin(angle) * radius
            piece = piece.rotate((i % 3 - 1) * phase * 13, Image.Resampling.BICUBIC, expand=True)
            center(canvas, piece, point=(x, y))
        frames.append(canvas)
    return frames


def save_strip(name, frames):
    strip = Image.new("RGBA", (FRAME * len(frames), FRAME), (0, 0, 0, 0))
    for i, frame in enumerate(frames):
        strip.alpha_composite(frame, (i * FRAME, 0))
    path = OUT / f"watchtower-{name}-384-alpha.png"
    strip.save(path, optimize=True)
    return path


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    parts = load_parts()
    idle = [assemble(parts, f, f) for f in (1, 2, 3, 4, 1)]
    attack = [
        assemble(parts, 1, 1, 1, 0),
        assemble(parts, 2, 2, 2, 5),
        assemble(parts, 3, 3, 3, 9),
        assemble(parts, 4, 4, 4, 3),
    ]
    destroy = destroy_frames(parts)
    projectile = scaled(parts["projectile_bolt"], 82 / max(parts["projectile_bolt"].size))
    projectile_frame = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
    center(projectile_frame, projectile)
    actions = {"idle": idle, "attack": attack, "destroy": destroy, "projectile": [projectile_frame]}
    strips = {name: save_strip(name, frames) for name, frames in actions.items()}

    rows = len(actions)
    cols = max(len(frames) for frames in actions.values())
    atlas = Image.new("RGBA", (cols * FRAME, rows * FRAME), (0, 0, 0, 0))
    action_manifest = {}
    for row, (name, frames) in enumerate(actions.items()):
        rects = []
        for col, frame in enumerate(frames):
            atlas.alpha_composite(frame, (col * FRAME, row * FRAME))
            rects.append({"x": col * FRAME, "y": row * FRAME, "w": FRAME, "h": FRAME})
        action_manifest[name] = {
            "strip": strips[name].name,
            "frames": rects,
            "frameDurationMs": {"idle": 180, "attack": 90, "destroy": 130, "projectile": 0}[name],
            "loop": name == "idle",
            "holdLast": name == "destroy",
        }
    atlas_path = OUT / "watchtower-animation-atlas-384.png"
    atlas.save(atlas_path, optimize=True)
    manifest = {
        "schemaVersion": 2,
        "object": "watchtower",
        "pipeline": "layered-object-v2-composite-animation",
        "image": atlas_path.name,
        "atlasSize": list(atlas.size),
        "frameSize": [FRAME, FRAME],
        "pivot": [.5, .5],
        "normalization": "locked 255px base footprint in centered 384px safety cell",
        "actions": action_manifest,
        "source": "../layered-v2-candidate/watchtower_layered_manifest.json",
        "qa": {"baseFootprintPx": BASE_EXTENT, "clippedFrames": [], "transparentBackground": True},
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"atlas": str(atlas_path), "size": atlas.size, "bytes": atlas_path.stat().st_size}, indent=2))


if __name__ == "__main__":
    main()

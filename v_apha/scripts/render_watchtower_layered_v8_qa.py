#!/usr/bin/env python3
"""Render Watchtower layered-v8 QA animation from independent PNG modules."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "assets/staging/candidates/watchtower-layered-v8"
OUT = ROOT / "assets/review/watchtower"
SIZE = 384
CENTER = (192, 192)


def load(sprite_id: str) -> Image.Image:
    return Image.open(PARTS / f"{sprite_id}.png").convert("RGBA")


def checker() -> Image.Image:
    image = Image.new("RGBA", (SIZE, SIZE), (224, 215, 194, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, SIZE, 16):
        for x in range(0, SIZE, 16):
            if (x // 16 + y // 16) % 2:
                draw.rectangle((x, y, x + 15, y + 15), fill=(204, 192, 166, 255))
    return image


def paste_center(canvas: Image.Image, image: Image.Image, anchor: tuple[int, int]) -> None:
    canvas.alpha_composite(image, (anchor[0] - image.width // 2, anchor[1] - image.height // 2))


def rotate_about_pivot(image: Image.Image, pivot: tuple[int, int], degrees: float) -> tuple[Image.Image, tuple[int, int]]:
    side = max(image.width, image.height) * 4
    center = (side // 2, side // 2)
    stage = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    stage.alpha_composite(image, (center[0] - pivot[0], center[1] - pivot[1]))
    rotated = stage.rotate(-degrees, resample=Image.Resampling.BICUBIC, center=center)
    return rotated, center


def paste_rotated(canvas: Image.Image, image: Image.Image, pivot: tuple[int, int],
                  anchor: tuple[int, int], degrees: float) -> None:
    rotated, rpivot = rotate_about_pivot(image, pivot, degrees)
    canvas.alpha_composite(rotated, (anchor[0] - rpivot[0], anchor[1] - rpivot[1]))


def rotated_point(origin: tuple[int, int], local: tuple[float, float], degrees: float) -> tuple[int, int]:
    radians = math.radians(degrees)
    return (
        round(origin[0] + local[0] * math.cos(radians) - local[1] * math.sin(radians)),
        round(origin[1] + local[0] * math.sin(radians) + local[1] * math.cos(radians)),
    )


BASE = load("watchtower__base_body__wardens_post")
SOCKET = load("watchtower__mount_socket__light_crossbow_bearing")
CROSSBOW = load("watchtower__active_primary__simple_crossbow")
FLAG_MOUNT = load("watchtower__ambient_mount__range_pennant_puck")
LANTERN = load("watchtower__ambient_mount__lantern_housing")
RUIN = load("watchtower__ruin_state__broken_post")
FLAGS = [load(f"watchtower__ambient_child__range_pennant__frame_{i:02d}") for i in range(1, 5)]
CORES = [load(f"watchtower__ambient_child__lantern_core__frame_{i:02d}") for i in range(1, 5)]
FLASHES = [load(f"watchtower__attack_release__muzzle_flash__frame_{i:02d}") for i in range(1, 5)]
DUST = [load(f"watchtower__destroy_fx__dust__frame_{i:02d}") for i in range(1, 5)]
DEBRIS = [
    load(f"watchtower__destroy_piece__stone_{i:02d}") for i in range(1, 7)
] + [
    load(f"watchtower__destroy_piece__wood_{i:02d}") for i in range(1, 7)
] + [
    load(f"watchtower__destroy_piece__metal_{i:02d}") for i in range(1, 4)
]


def intact_base(flag_index: int, core_index: int) -> Image.Image:
    canvas = checker()
    paste_center(canvas, BASE, CENTER)
    paste_center(canvas, SOCKET, CENTER)

    flag_anchor = (137, 250)
    flag_angle = 134
    paste_rotated(canvas, FLAG_MOUNT, (FLAG_MOUNT.width // 2, FLAG_MOUNT.height // 2), flag_anchor, flag_angle)
    cloth_anchor = rotated_point(flag_anchor, (27, 0), flag_angle)
    paste_rotated(canvas, FLAGS[flag_index], (2, FLAGS[flag_index].height // 2), cloth_anchor, flag_angle)

    lantern_anchor = (247, 250)
    paste_center(canvas, CORES[core_index], lantern_anchor)
    paste_center(canvas, LANTERN, lantern_anchor)
    return canvas


def idle_frame(index: int) -> Image.Image:
    sequence = [0, 1, 2, 3, 2, 1]
    canvas = intact_base(sequence[index % 6], sequence[(index * 2) % 6])
    paste_rotated(canvas, CROSSBOW, (CROSSBOW.width // 2, CROSSBOW.height // 2), CENTER, 0)
    return canvas


def aim_frame(index: int) -> Image.Image:
    canvas = intact_base(1, index % 4)
    angle = -50 + index * 10
    paste_rotated(canvas, CROSSBOW, (CROSSBOW.width // 2, CROSSBOW.height // 2), CENTER, angle)
    return canvas


def attack_frame(index: int) -> Image.Image:
    canvas = intact_base(1, index % 4)
    angle = -22
    recoil = [0, -2, -4, -2, 0, 0, 0, 0][index]
    weapon_anchor = rotated_point(CENTER, (recoil, 0), angle)
    paste_rotated(canvas, CROSSBOW, (CROSSBOW.width // 2, CROSSBOW.height // 2), weapon_anchor, angle)
    if index < 4:
        muzzle = rotated_point(weapon_anchor, (CROSSBOW.width * 0.48, 0), angle)
        paste_rotated(canvas, FLASHES[index], (2, FLASHES[index].height // 2), muzzle, angle)
    return canvas


def destroy_frame(index: int) -> Image.Image:
    canvas = checker()
    if index == 0:
        return idle_frame(0)
    paste_center(canvas, RUIN, CENTER)
    dust_index = min(3, index - 1)
    paste_center(canvas, DUST[dust_index], CENTER)
    distance = 5 + index * 6
    for i, piece in enumerate(DEBRIS):
        angle = i * (360 / len(DEBRIS)) + 13
        anchor = rotated_point(CENTER, (distance + (i % 3) * 5, 0), angle)
        paste_rotated(canvas, piece, (piece.width // 2, piece.height // 2), anchor, angle + index * 9)
    return canvas


def label(frame: Image.Image, text: str) -> Image.Image:
    draw = ImageDraw.Draw(frame)
    draw.rectangle((0, 0, 118, 22), fill=(30, 27, 23, 220))
    draw.text((7, 6), text, font=ImageFont.load_default(), fill=(248, 239, 216, 255))
    return frame


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    frames = []
    for index in range(12):
        sheet = Image.new("RGBA", (SIZE * 2, SIZE * 2), (0, 0, 0, 0))
        sheet.alpha_composite(label(idle_frame(index), "IDLE / CHILD LOOPS"), (0, 0))
        sheet.alpha_composite(label(aim_frame(index), "AIM / WEAPON ONLY"), (SIZE, 0))
        sheet.alpha_composite(label(attack_frame(index % 8), "ATTACK / FLASH + RECOIL"), (0, SIZE))
        sheet.alpha_composite(label(destroy_frame(min(7, index)), "DESTROY / RUIN + PIECES"), (SIZE, SIZE))
        frames.append(sheet.convert("P", palette=Image.Palette.ADAPTIVE))
    gif = OUT / "watchtower_layered_runtime_animation_proof_v8.gif"
    frames[0].save(gif, save_all=True, append_images=frames[1:], duration=130, loop=0, disposal=2)

    # Static assembly proof showing the actual independent input PNGs.
    proof = Image.new("RGBA", (SIZE * 4, SIZE), (0, 0, 0, 0))
    proof.alpha_composite(label(idle_frame(1), "ASSEMBLED"), (0, 0))
    base_only = checker()
    paste_center(base_only, BASE, CENTER)
    proof.alpha_composite(label(base_only, "BASE ONLY"), (SIZE, 0))
    weapon_only = checker()
    paste_center(weapon_only, SOCKET, CENTER)
    paste_center(weapon_only, CROSSBOW, CENTER)
    proof.alpha_composite(label(weapon_only, "SOCKET + WEAPON"), (SIZE * 2, 0))
    children_only = checker()
    flag_anchor = (137, 250)
    paste_rotated(children_only, FLAG_MOUNT, (FLAG_MOUNT.width // 2, FLAG_MOUNT.height // 2), flag_anchor, 134)
    paste_rotated(children_only, FLAGS[1], (2, FLAGS[1].height // 2), rotated_point(flag_anchor, (27, 0), 134), 134)
    paste_center(children_only, CORES[1], (247, 250))
    paste_center(children_only, LANTERN, (247, 250))
    proof.alpha_composite(label(children_only, "CHILDREN ONLY"), (SIZE * 3, 0))
    proof.save(OUT / "watchtower_layered_assembly_proof_v8.png", optimize=True)
    print(gif)


if __name__ == "__main__":
    main()

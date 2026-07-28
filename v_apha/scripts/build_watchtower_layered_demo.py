#!/usr/bin/env python3
"""Build a demo layered Watchtower atlas and manifest.

This is a validation artifact for the new layered-object pipeline:
one object family, separated layers, explicit pivots/anchors, and a review grid.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/sprite-atlases/watchtower/layered-demo"
CELL = 256
ATLAS_COLS = 4
ATLAS_ROWS = 5
ATLAS_SIZE = (CELL * ATLAS_COLS, CELL * ATLAS_ROWS)


def rgba(size: tuple[int, int]) -> Image.Image:
    return Image.new("RGBA", size, (0, 0, 0, 0))


def add_noise_texture(image: Image.Image, seed: int, alpha: int = 18) -> Image.Image:
    noise = rgba(image.size)
    px = noise.load()
    source_alpha = image.getchannel("A").load()
    w, h = image.size
    for y in range(h):
        for x in range(w):
            if source_alpha[x, y] == 0:
                continue
            v = ((x * 37 + y * 71 + seed * 101) % 43) - 21
            px[x, y] = (255 if v > 0 else 0, 255 if v > 0 else 0, 255 if v > 0 else 0, alpha)
    out = image.copy()
    out.alpha_composite(noise)
    return out


def draw_cardboard_outline(draw: ImageDraw.ImageDraw, pts: list[tuple[int, int]], fill: tuple[int, int, int, int]) -> None:
    draw.polygon(pts, fill=(70, 52, 32, 255))
    inset = []
    cx = sum(x for x, _ in pts) / len(pts)
    cy = sum(y for _, y in pts) / len(pts)
    for x, y in pts:
        inset.append((round(cx + (x - cx) * 0.94), round(cy + (y - cy) * 0.94)))
    draw.polygon(inset, fill=(177, 145, 91, 255))
    inner = []
    for x, y in pts:
        inner.append((round(cx + (x - cx) * 0.86), round(cy + (y - cy) * 0.86)))
    draw.polygon(inner, fill=fill)


def platform() -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    cx, cy = 128, 128
    pts = []
    for i in range(28):
        angle = math.tau * i / 28
        r = 111 + (i * 13 % 9) - 4
        pts.append((round(cx + math.cos(angle) * r), round(cy + math.sin(angle) * r)))
    draw_cardboard_outline(draw, pts, (94, 96, 89, 255))
    # Stone slabs.
    stones = [
        (52, 34, 111, 74), (111, 30, 168, 72), (166, 44, 207, 93),
        (32, 82, 88, 132), (88, 75, 142, 129), (142, 77, 205, 132),
        (43, 135, 103, 189), (103, 132, 159, 189), (159, 137, 211, 185),
        (72, 188, 132, 221), (132, 186, 184, 219),
    ]
    for idx, box in enumerate(stones):
        color = (108 + idx % 3 * 9, 110 + idx % 4 * 6, 103 + idx % 2 * 7, 255)
        draw.rounded_rectangle(box, radius=10, fill=color, outline=(40, 42, 39, 235), width=3)
        draw.line((box[0] + 9, box[1] + 10, box[2] - 7, box[3] - 8), fill=(146, 148, 139, 80), width=2)
    img = add_noise_texture(img, 3, 10)
    return img


def central_socket() -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    draw.ellipse((58, 58, 198, 198), fill=(44, 37, 31, 255), outline=(17, 18, 17, 255), width=4)
    for r, color in [(62, (120, 77, 41, 255)), (47, (93, 62, 38, 255)), (31, (105, 68, 36, 255))]:
        draw.ellipse((128 - r, 128 - r, 128 + r, 128 + r), outline=color, width=10)
    draw.ellipse((88, 88, 168, 168), fill=(83, 84, 80, 255), outline=(26, 27, 25, 255), width=4)
    for angle in range(0, 360, 60):
        x = 128 + round(math.cos(math.radians(angle)) * 30)
        y = 128 + round(math.sin(math.radians(angle)) * 30)
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(38, 39, 38, 255), outline=(154, 146, 127, 220))
    draw.line((128, 70, 128, 186), fill=(51, 34, 24, 145), width=3)
    draw.line((70, 128, 186, 128), fill=(51, 34, 24, 145), width=3)
    return add_noise_texture(img, 7, 9)


def crossbow() -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    # Bow arc.
    draw.arc((32, 40, 108, 216), 82, 278, fill=(24, 20, 15, 255), width=16)
    draw.arc((40, 48, 102, 208), 84, 276, fill=(112, 72, 40, 255), width=9)
    draw.line((62, 57, 131, 128), fill=(212, 196, 154, 255), width=4)
    draw.line((62, 199, 131, 128), fill=(212, 196, 154, 255), width=4)
    # Main stock.
    draw.rounded_rectangle((40, 107, 226, 149), radius=7, fill=(39, 25, 16, 255))
    draw.rounded_rectangle((45, 112, 218, 144), radius=6, fill=(121, 76, 39, 255), outline=(23, 18, 13, 255), width=3)
    draw.rectangle((46, 118, 220, 124), fill=(153, 99, 54, 120))
    draw.rectangle((48, 136, 215, 141), fill=(61, 38, 24, 160))
    # Metal plates.
    draw.rounded_rectangle((42, 98, 83, 157), radius=6, fill=(70, 70, 65, 255), outline=(17, 17, 16, 255), width=3)
    draw.rounded_rectangle((183, 101, 226, 154), radius=5, fill=(70, 70, 65, 255), outline=(17, 17, 16, 255), width=3)
    for x in (55, 73, 197, 216):
        draw.ellipse((x - 5, 122, x + 5, 132), fill=(38, 39, 37, 255), outline=(150, 144, 128, 220))
    # Bolt head.
    draw.polygon([(16, 128), (48, 111), (48, 145)], fill=(180, 176, 160, 255), outline=(24, 25, 23, 255))
    draw.line((16, 128, 221, 128), fill=(35, 26, 17, 255), width=3)
    # Pivot marker.
    draw.ellipse((119, 119, 137, 137), fill=(241, 177, 70, 230), outline=(34, 23, 13, 255), width=3)
    return add_noise_texture(img, 11, 9)


def flag_pole() -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((116, 42, 134, 208), radius=8, fill=(44, 26, 14, 255))
    draw.rounded_rectangle((120, 46, 130, 204), radius=5, fill=(135, 80, 36, 255))
    draw.ellipse((108, 32, 142, 66), fill=(118, 76, 38, 255), outline=(28, 19, 13, 255), width=4)
    draw.ellipse((96, 190, 154, 226), fill=(57, 59, 56, 255), outline=(24, 25, 23, 255), width=4)
    return add_noise_texture(img, 17, 8)


def flag_cloth(phase: int) -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    y = 112
    wave = phase * 6
    pts = [
        (45, y - 31), (86, y - 38 + wave // 2), (132, y - 28 - wave),
        (199, y - 34 + wave // 3), (221, y - 7),
        (188, y + 1 + wave // 4), (222, y + 26),
        (139, y + 22 - wave // 3), (88, y + 34 + wave // 3), (45, y + 25),
    ]
    draw.polygon(pts, fill=(52, 17, 15, 255))
    inner = [(round(58 + (x - 45) * 0.88), round(y + (py - y) * 0.82)) for x, py in pts]
    draw.polygon(inner, fill=(129, 42, 35, 255))
    draw.line((62, y - 17, 197, y - 12 + phase), fill=(175, 72, 54, 120), width=4)
    draw.line((66, y + 15, 176, y + 18 - phase), fill=(58, 18, 18, 130), width=4)
    draw.line((111, y - 12, 137, y + 10, 163, y - 12), fill=(190, 145, 76, 210), width=4)
    return add_noise_texture(img, 23 + phase, 8)


def lantern_body() -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((85, 78, 171, 178), radius=13, fill=(32, 29, 24, 255))
    draw.rounded_rectangle((96, 89, 160, 166), radius=8, fill=(83, 82, 76, 255), outline=(18, 18, 16, 255), width=4)
    draw.polygon((111, 106, 145, 88, 158, 133, 127, 158, 97, 132), fill=(226, 155, 44, 235), outline=(26, 19, 11, 255))
    draw.line((128, 70, 128, 48), fill=(30, 25, 19, 255), width=7)
    draw.arc((104, 38, 152, 84), 190, 350, fill=(72, 68, 58, 255), width=6)
    return add_noise_texture(img, 31, 7)


def flame(phase: int) -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    cx, cy = 128, 130
    h = 44 + phase * 5
    draw.ellipse((cx - 44, cy - 28, cx + 44, cy + 42), fill=(255, 158, 43, 50))
    draw.polygon([(cx, cy - h), (cx + 23, cy + 8), (cx + 4, cy + 35), (cx - 22, cy + 8)], fill=(255, 176, 38, 230))
    draw.polygon([(cx + 3, cy - h + 18), (cx + 12, cy + 8), (cx, cy + 24), (cx - 10, cy + 8)], fill=(255, 235, 126, 235))
    return img.filter(ImageFilter.GaussianBlur(0.25))


def muzzle_flash(phase: int) -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    cx, cy = 128, 128
    length = [42, 72, 98, 52][phase]
    alpha = [120, 220, 245, 150][phase]
    draw.polygon([(cx - length, cy), (cx - 12, cy - 20), (cx + 18, cy), (cx - 12, cy + 20)], fill=(255, 189, 47, alpha))
    draw.line((cx + 12, cy, cx - length + 12, cy), fill=(255, 239, 148, min(255, alpha + 20)), width=7)
    draw.line((cx - 4, cy - 20, cx - length // 2, cy - 42), fill=(255, 222, 101, alpha // 2), width=4)
    draw.line((cx - 4, cy + 20, cx - length // 2, cy + 42), fill=(255, 222, 101, alpha // 2), width=4)
    return img.filter(ImageFilter.GaussianBlur(0.15))


def projectile() -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    draw.line((128, 195, 128, 68), fill=(52, 33, 18, 255), width=13)
    draw.line((128, 188, 128, 74), fill=(169, 111, 54, 255), width=7)
    draw.polygon([(128, 42), (154, 84), (128, 70), (102, 84)], fill=(180, 176, 160, 255), outline=(27, 28, 26, 255))
    draw.polygon([(128, 212), (158, 166), (128, 182), (98, 166)], fill=(134, 42, 35, 245), outline=(29, 20, 15, 255))
    return add_noise_texture(img, 43, 5)


def debris() -> Image.Image:
    img = rgba((CELL, CELL))
    draw = ImageDraw.Draw(img)
    pieces = [
        ((60, 81), (89, 64), (105, 91), (75, 107), (100, 95, 87, 245)),
        ((126, 54), (153, 78), (140, 111), (111, 89), (120, 72, 40, 245)),
        ((169, 129), (202, 120), (215, 148), (184, 166), (92, 93, 87, 245)),
        ((71, 169), (106, 151), (123, 180), (92, 204), (154, 119, 67, 245)),
        ((138, 178), (165, 165), (185, 190), (157, 214), (79, 80, 76, 245)),
    ]
    for piece in pieces:
        *pts, color = piece
        draw.polygon(pts, fill=color, outline=(25, 24, 22, 230))
    return add_noise_texture(img, 51, 8)


def place(atlas: Image.Image, cell_index: int, sprite: Image.Image) -> dict[str, int]:
    col = cell_index % ATLAS_COLS
    row = cell_index // ATLAS_COLS
    x = col * CELL
    y = row * CELL
    atlas.alpha_composite(sprite, (x, y))
    return {"x": x, "y": y, "w": CELL, "h": CELL}


def build_preview(parts: dict[str, Image.Image]) -> Image.Image:
    canvas = rgba((384, 384))
    def comp(name: str, pos: tuple[int, int], rotate: float = 0) -> None:
        sprite = parts[name]
        if rotate:
            sprite = sprite.rotate(rotate, resample=Image.Resampling.BICUBIC, expand=False)
        canvas.alpha_composite(sprite, pos)
    comp("base_stone_token", (64, 64))
    comp("central_socket", (64, 64))
    comp("flag_pole", (162, 42))
    comp("flag_cloth_wind_02", (168, 44))
    comp("lantern_body", (178, 158))
    comp("lantern_flame_02", (178, 158))
    comp("crossbow_rotatable", (64, 64), rotate=0)
    comp("muzzle_flash_02", (16, 64))
    return canvas


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    parts: dict[str, Image.Image] = {
        "base_stone_token": platform(),
        "central_socket": central_socket(),
        "crossbow_rotatable": crossbow(),
        "flag_pole": flag_pole(),
        "flag_cloth_wind_01": flag_cloth(0),
        "flag_cloth_wind_02": flag_cloth(1),
        "flag_cloth_wind_03": flag_cloth(2),
        "flag_cloth_wind_04": flag_cloth(3),
        "lantern_body": lantern_body(),
        "lantern_flame_01": flame(0),
        "lantern_flame_02": flame(1),
        "lantern_flame_03": flame(2),
        "lantern_flame_04": flame(3),
        "muzzle_flash_01": muzzle_flash(0),
        "muzzle_flash_02": muzzle_flash(1),
        "muzzle_flash_03": muzzle_flash(2),
        "muzzle_flash_04": muzzle_flash(3),
        "projectile_bolt": projectile(),
        "destroy_debris": debris(),
    }
    order = [
        "base_stone_token", "central_socket", "crossbow_rotatable", "flag_pole",
        "flag_cloth_wind_01", "flag_cloth_wind_02", "flag_cloth_wind_03", "flag_cloth_wind_04",
        "lantern_body", "lantern_flame_01", "lantern_flame_02", "lantern_flame_03",
        "lantern_flame_04", "muzzle_flash_01", "muzzle_flash_02", "muzzle_flash_03",
        "muzzle_flash_04", "projectile_bolt", "destroy_debris",
    ]
    atlas = rgba(ATLAS_SIZE)
    sprites = {}
    for idx, name in enumerate(order):
        sprites[name] = {
            "rect": place(atlas, idx, parts[name]),
            "pivot": [0.5, 0.5],
            "cell": [CELL, CELL],
        }
    atlas.save(OUT / "watchtower_layered_demo_atlas.png", optimize=True)

    review = Image.new("RGBA", ATLAS_SIZE, (255, 0, 255, 255))
    review.alpha_composite(atlas)
    draw = ImageDraw.Draw(review)
    for x in range(0, ATLAS_SIZE[0] + 1, CELL):
        draw.line((x, 0, x, ATLAS_SIZE[1]), fill=(255, 255, 255, 130), width=2)
    for y in range(0, ATLAS_SIZE[1] + 1, CELL):
        draw.line((0, y, ATLAS_SIZE[0], y), fill=(255, 255, 255, 130), width=2)
    review.save(OUT / "watchtower_layered_demo_review_grid.png", optimize=True)

    preview = build_preview(parts)
    preview.save(OUT / "watchtower_layered_demo_composite_preview.png", optimize=True)

    manifest = {
        "object": "watchtower",
        "pipeline": "layered-object-demo-v2",
        "status": "demo_for_user_validation",
        "image": "watchtower_layered_demo_atlas.png",
        "reviewImage": "watchtower_layered_demo_review_grid.png",
        "compositePreview": "watchtower_layered_demo_composite_preview.png",
        "atlasSize": list(ATLAS_SIZE),
        "cellSize": [CELL, CELL],
        "format": "RGBA PNG",
        "maxFileSizeBytes": 5_000_000,
        "camera": "true top-down orthographic 90deg",
        "style": "cardboard tabletop board-game token, matte paper, exposed tan cardboard edge",
        "drawOrder": [
            "base_stone_token",
            "central_socket",
            "flag_pole",
            "flag_cloth_wind",
            "lantern_body",
            "lantern_flame",
            "crossbow_rotatable",
            "muzzle_flash",
        ],
        "attachments": {
            "object_center": {"pivot": [0.5, 0.5], "px": [128, 128]},
            "crossbow_center": {"layer": "crossbow_rotatable", "pivot": [0.5, 0.5], "px": [128, 128], "rotation": "runtime_angle_to_target"},
            "flag_anchor": {"layer": "flag_pole", "px": [128, 86], "animation": "wind_direction_selects_flag_cloth_frame"},
            "lantern_anchor": {"layer": "lantern_body", "px": [128, 128], "animation": "lantern_flame_loop"},
            "muzzle_anchor": {"layer": "crossbow_rotatable", "px": [28, 128], "animation": "muzzle_flash_once"},
        },
        "sprites": sprites,
        "animations": {
            "idle": {
                "base": ["base_stone_token", "central_socket", "flag_pole", "lantern_body", "crossbow_rotatable"],
                "loops": {
                    "flag_cloth_wind": ["flag_cloth_wind_01", "flag_cloth_wind_02", "flag_cloth_wind_03", "flag_cloth_wind_04"],
                    "lantern_flame": ["lantern_flame_01", "lantern_flame_02", "lantern_flame_03", "lantern_flame_04"],
                },
                "durationMs": 140,
                "loop": True,
            },
            "attack": {
                "runtimeRotation": "crossbow_rotatable follows target angle around crossbow_center",
                "once": ["muzzle_flash_01", "muzzle_flash_02", "muzzle_flash_03", "muzzle_flash_04"],
                "durationMs": 80,
                "loop": False,
            },
        },
        "validationRules": [
            "production atlas png must be <= 5 MB",
            "one object family per atlas",
            "base/body footprint must remain locked",
            "rotating layers must declare pivot and attachment",
            "animated layers must not shift object anchor",
            "no baked perspective, facade, side-view, or old tall-tower read",
        ],
    }
    (OUT / "watchtower_layered_demo_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()

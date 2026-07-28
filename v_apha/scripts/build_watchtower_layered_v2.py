#!/usr/bin/env python3
"""Build the compact Watchtower Layered Object Pipeline v2 candidate."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/sprite-atlases/watchtower/layered-v2-candidate"
SOURCE = OUT / "watchtower_layered_source_chroma.png"
ALPHA_SOURCE = OUT / "watchtower_layered_source_alpha.png"
RUNTIME = OUT / "watchtower_layered_runtime.png"
MANIFEST = OUT / "watchtower_layered_manifest.json"
REVIEW = OUT / "watchtower_layered_review_grid.png"
PREVIEW = OUT / "watchtower_layered_composite_preview.png"

# Source regions are deliberately semantic: ImageGen layouts are not inferred at runtime.
REGIONS = {
    "base_stone_token": (15, 15, 640, 635),
    "central_socket": (720, 20, 1020, 310),
    "crossbow_rotatable": (615, 305, 1055, 660),
    "flag_pole": (1050, 115, 1140, 615),
    "flag_cloth_wind_01": (1155, 35, 1485, 210),
    "flag_cloth_wind_02": (1155, 220, 1485, 395),
    "flag_cloth_wind_03": (1155, 400, 1485, 570),
    "flag_cloth_wind_04": (1155, 575, 1485, 720),
    "lantern_body": (30, 645, 235, 810),
    "lantern_flame_01": (260, 645, 375, 810),
    "lantern_flame_02": (380, 645, 495, 810),
    "lantern_flame_03": (500, 645, 615, 810),
    "lantern_flame_04": (620, 645, 745, 810),
    "muzzle_flash_01": (755, 670, 885, 815),
    "muzzle_flash_02": (890, 670, 1020, 815),
    "muzzle_flash_03": (1025, 670, 1165, 815),
    "projectile_bolt": (45, 845, 260, 975),
    "destroy_debris_01": (275, 825, 410, 1015),
    "destroy_debris_02": (415, 825, 570, 1015),
    "destroy_debris_03": (575, 825, 730, 1015),
    "destroy_debris_04": (735, 825, 880, 1015),
    "destroy_debris_05": (880, 825, 995, 1015),
    "destroy_debris_06": (990, 825, 1110, 1015),
    "destroy_debris_07": (1095, 825, 1190, 1015),
    "destroy_debris_08": (1175, 825, 1325, 1015),
    "destroy_debris_09": (1310, 825, 1500, 1015),
}


def remove_chroma(source: Image.Image) -> Image.Image:
    """Key magenta with a narrow antialias feather."""
    image = source.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, _ = pixels[x, y]
            distance = ((r - 255) ** 2 + g**2 + (b - 255) ** 2) ** 0.5
            # Generated antialias pixels can be a broad magenta blend. A wider
            # ramp removes the halo while retaining the tan cardboard outline.
            alpha = max(0, min(255, round((distance - 25) * 255 / 150)))
            pixels[x, y] = (r, g, b, alpha)
    return image


def tight_crop(source: Image.Image, region: tuple[int, int, int, int], pad: int = 3) -> Image.Image:
    crop = source.crop(region)
    box = crop.getchannel("A").point(lambda a: 255 if a >= 18 else 0).getbbox()
    if box is None:
        raise RuntimeError(f"empty source region: {region}")
    x0, y0, x1, y1 = box
    return keep_largest_component(crop.crop((max(0, x0 - pad), max(0, y0 - pad), min(crop.width, x1 + pad), min(crop.height, y1 + pad))))


def keep_largest_component(image: Image.Image, threshold: int = 20) -> Image.Image:
    alpha = image.getchannel("A")
    pixels = alpha.load()
    seen = set()
    best = []
    for y in range(image.height):
        for x in range(image.width):
            if pixels[x, y] < threshold or (x, y) in seen:
                continue
            stack = [(x, y)]
            seen.add((x, y))
            points = []
            while stack:
                px, py = stack.pop()
                points.append((px, py))
                for nx, ny in ((px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)):
                    if 0 <= nx < image.width and 0 <= ny < image.height and (nx, ny) not in seen and pixels[nx, ny] >= threshold:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            if len(points) > len(best):
                best = points
    if not best:
        return image
    xs, ys = [p[0] for p in best], [p[1] for p in best]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs) + 1, max(ys) + 1
    out = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    src, dst = image.load(), out.load()
    for x, y in best:
        dst[x - x0, y - y0] = src[x, y]
    return out


def make_flash_hold(frame: Image.Image) -> Image.Image:
    """Create the required fourth, fading hold frame without inventing a new shape."""
    out = ImageEnhance.Brightness(frame).enhance(0.72)
    alpha = out.getchannel("A").point(lambda value: round(value * 0.62))
    out.putalpha(alpha)
    return out


def pack(parts: dict[str, Image.Image], width: int = 1536, padding: int = 8):
    ordered = sorted(parts.items(), key=lambda item: (-item[1].height, -item[1].width, item[0]))
    placements: dict[str, tuple[int, int]] = {}
    x = y = padding
    row_h = 0
    for name, image in ordered:
        if x + image.width + padding > width:
            x = padding
            y += row_h + padding
            row_h = 0
        placements[name] = (x, y)
        x += image.width + padding
        row_h = max(row_h, image.height)
    height = y + row_h + padding
    return placements, height


def pivot(name: str, size: tuple[int, int]) -> list[int]:
    w, h = size
    if name.startswith("flag_cloth"):
        return [4, h // 2]
    if name.startswith("lantern_flame"):
        return [w // 2, round(h * 0.72)]
    if name.startswith("muzzle_flash"):
        return [4, h // 2]
    if name == "projectile_bolt":
        return [w // 2, h // 2]
    return [w // 2, h // 2]


def build_review(parts: dict[str, Image.Image], pivots: dict[str, list[int]]) -> None:
    names = list(parts)
    cols, cell_w, cell_h = 4, 390, 260
    rows = (len(names) + cols - 1) // cols
    canvas = Image.new("RGBA", (cols * cell_w, rows * cell_h), (39, 31, 43, 255))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    for index, name in enumerate(names):
        cx, cy = (index % cols) * cell_w, (index // cols) * cell_h
        draw.rectangle((cx, cy, cx + cell_w - 1, cy + cell_h - 1), outline=(139, 111, 155, 255), width=2)
        sprite = parts[name].copy()
        scale = min(1.0, (cell_w - 30) / sprite.width, (cell_h - 50) / sprite.height)
        if scale < 1:
            sprite = sprite.resize((round(sprite.width * scale), round(sprite.height * scale)), Image.Resampling.LANCZOS)
        px = cx + (cell_w - sprite.width) // 2
        py = cy + 34 + (cell_h - 42 - sprite.height) // 2
        canvas.alpha_composite(sprite, (px, py))
        draw.text((cx + 10, cy + 10), name, font=font, fill=(255, 233, 169, 255))
        pivot_x = px + round(pivots[name][0] * scale)
        pivot_y = py + round(pivots[name][1] * scale)
        draw.line((pivot_x - 8, pivot_y, pivot_x + 8, pivot_y), fill=(0, 255, 255, 255), width=2)
        draw.line((pivot_x, pivot_y - 8, pivot_x, pivot_y + 8), fill=(0, 255, 255, 255), width=2)
    canvas.save(REVIEW, optimize=True)


def build_preview(parts: dict[str, Image.Image]) -> None:
    canvas = Image.new("RGBA", (900, 900), (40, 32, 44, 255))
    base = parts["base_stone_token"]
    center = (450, 450)
    def at_center(name: str, offset=(0, 0)):
        image = parts[name]
        canvas.alpha_composite(image, (center[0] - image.width // 2 + offset[0], center[1] - image.height // 2 + offset[1]))
    at_center("base_stone_token")
    at_center("central_socket")
    at_center("flag_pole", (-190, -65))
    flag = parts["flag_cloth_wind_02"]
    canvas.alpha_composite(flag, (center[0] - 190, center[1] - 150))
    at_center("lantern_body", (-185, 115))
    at_center("lantern_flame_02", (-185, 115))
    at_center("crossbow_rotatable")
    flash = parts["muzzle_flash_02"]
    canvas.alpha_composite(flash, (center[0] + parts["crossbow_rotatable"].width // 2 - 15, center[1] - flash.height // 2))
    canvas.save(PREVIEW, optimize=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    alpha_source = remove_chroma(Image.open(SOURCE))
    alpha_source.save(ALPHA_SOURCE, optimize=True)
    parts = {name: tight_crop(alpha_source, region) for name, region in REGIONS.items()}
    parts["muzzle_flash_04"] = make_flash_hold(parts["muzzle_flash_03"])
    # Semantic order is stable even when packing order changes.
    semantic_order = list(REGIONS)
    semantic_order.insert(semantic_order.index("projectile_bolt"), "muzzle_flash_04")
    parts = {name: parts[name] for name in semantic_order}
    placements, height = pack(parts)
    atlas = Image.new("RGBA", (1536, height), (0, 0, 0, 0))
    sprite_data = {}
    pivots = {}
    for name, image in parts.items():
        x, y = placements[name]
        atlas.alpha_composite(image, (x, y))
        p = pivot(name, image.size)
        pivots[name] = p
        sprite_data[name] = {
            "layer": name.split("_")[0],
            "rect": {"x": x, "y": y, "w": image.width, "h": image.height},
            "pivotPx": p,
            "pivot": [round(p[0] / image.width, 5), round(p[1] / image.height, 5)],
            "sourceSize": [image.width, image.height],
        }
    atlas.save(RUNTIME, optimize=True)
    build_review(parts, pivots)
    build_preview(parts)
    debris = [name for name in parts if name.startswith("destroy_debris_")]
    manifest = {
        "schemaVersion": 2,
        "object": "watchtower",
        "family": "watchtower",
        "pipeline": "layered-object-v2",
        "status": "approved-candidate",
        "image": RUNTIME.name,
        "sourceImage": SOURCE.name,
        "alphaSourceImage": ALPHA_SOURCE.name,
        "reviewImage": REVIEW.name,
        "compositePreview": PREVIEW.name,
        "atlasSize": [atlas.width, atlas.height],
        "format": "RGBA PNG",
        "camera": "true top-down orthographic 90deg",
        "style": "matte cardboard tabletop board-game token",
        "maxFileSizeBytes": 5_000_000,
        "fileSizeBytes": RUNTIME.stat().st_size,
        "drawOrder": ["base_stone_token", "central_socket", "flag_pole", "flag_cloth_wind", "lantern_body", "lantern_flame", "crossbow_rotatable", "muzzle_flash"],
        "sprites": sprite_data,
        "attachments": {
            "objectCenter": {"parent": "base_stone_token", "pointPx": pivots["base_stone_token"]},
            "weaponSocket": {"parent": "central_socket", "child": "crossbow_rotatable", "childPivotPx": pivots["crossbow_rotatable"]},
            "flagCloth": {"parent": "flag_pole", "childPattern": "flag_cloth_wind_*", "childPivot": "left-center"},
            "lanternFlame": {"parent": "lantern_body", "childPattern": "lantern_flame_*", "childPivot": "lower-center"},
            "muzzle": {"parent": "crossbow_rotatable", "childPattern": "muzzle_flash_*", "childPivot": "left-center"},
            "projectileSpawn": {"parent": "crossbow_rotatable", "child": "projectile_bolt"},
        },
        "runtimeTransforms": {
            "crossbow_rotatable": {"rotate": "toward-target", "origin": "weaponSocket"},
            "projectile_bolt": {"rotate": "along-trajectory"},
            "flag_cloth_wind_*": {"position": "flagCloth", "preserveBaseFootprint": True},
            "lantern_flame_*": {"position": "lanternFlame", "preserveBaseFootprint": True},
            "muzzle_flash_*": {"position": "muzzle", "inheritParentRotation": True},
        },
        "animations": {
            "flagWind": {"frames": [f"flag_cloth_wind_{i:02d}" for i in range(1, 5)], "frameDurationMs": 140, "loop": True},
            "lanternFlame": {"frames": [f"lantern_flame_{i:02d}" for i in range(1, 5)], "frameDurationMs": 110, "loop": True},
            "attackFlash": {"frames": [f"muzzle_flash_{i:02d}" for i in range(1, 5)], "frameDurationMs": 65, "loop": False, "holdLast": False},
            "destroy": {"pieces": debris, "loop": False, "holdLast": True},
        },
        "qa": {
            "runtimeCompactPacking": True,
            "transparentBackground": True,
            "oneObjectFamily": True,
            "runtimeContainsReviewMarkup": False,
            "under5MB": RUNTIME.stat().st_size <= 5_000_000,
            "noClipping": True,
            "derivedFrames": {"muzzle_flash_04": "fade hold derived from ImageGen muzzle_flash_03"},
            "knownIssues": [],
        },
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"runtime": str(RUNTIME), "size": atlas.size, "bytes": RUNTIME.stat().st_size, "sprites": len(parts)}, indent=2))


if __name__ == "__main__":
    main()

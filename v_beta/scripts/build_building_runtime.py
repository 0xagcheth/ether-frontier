#!/usr/bin/env python3
"""Build normalized 384px building animation strips from generated sources."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from PIL import Image, ImageDraw

from build_runtime_sprite_pack import key_to_alpha, split_grid


FRAME = 384
BUILDING_EXTENT = 255
PROJECTILE_EXTENTS = {
    "watchtower": 82,
    "ranger": 130,
    "tracker": 130,
    "ballista": 146,
    "scorpion": 146,
    "hailstorm": 118,
    "cannon": 96,
    "mortar": 104,
    "grapeshot": 124,
    "palisade": 120,
    "obelisk": 112,
    "beacon": 92,
    "pal-censer": 102,
    "pal-reliquary": 112,
    "mage-frost": 104,
    "mage-tesla": 110,
    "mage-prism": 116,
    "hunt-roost": 110,
    "hunt-hive": 108,
}
IMPACT_EXTENTS = {
    "ballista": 112,
    "scorpion": 112,
    "hailstorm": 118,
    "cannon": 128,
    "mortar": 132,
    "grapeshot": 140,
    "palisade": 128,
    "obelisk": 136,
    "beacon": 132,
    "pal-censer": 140,
    "pal-reliquary": 152,
    "mage-frost": 148,
    "mage-tesla": 148,
    "mage-prism": 160,
    "hunt-snare": 144,
    "hunt-roost": 132,
    "hunt-hive": 148,
}
CLEAN_FRINGE_SLUGS = {
    "watchtower",
    "sawmill",
    "quarry",
    "castle",
    "pal-ward",
    "pal-censer",
    "pal-reliquary",
    "mage-frost",
    "mage-tesla",
    "hunt-snare",
}


def alpha_source(path: Path) -> Image.Image:
    return key_to_alpha(Image.open(path).convert("RGBA"), preserve_white=True)


def border_connected_key_to_alpha(image: Image.Image) -> Image.Image:
    """Remove only border-connected magenta so violet portal art stays opaque."""
    image = image.convert("RGBA")
    width, height = image.size
    pixels = image.load()

    def chroma_score(x: int, y: int) -> float:
        red, green, blue, _ = pixels[x, y]
        if red + blue <= 150:
            return -1
        return min(red - green * 1.40, blue - green * 1.20)

    stack = []
    seen = set()
    for x in range(width):
        stack.extend(((x, 0), (x, height - 1)))
    for y in range(height):
        stack.extend(((0, y), (width - 1, y)))
    while stack:
        x, y = stack.pop()
        if (x, y) in seen or chroma_score(x, y) <= 12:
            continue
        seen.add((x, y))
        if x:
            stack.append((x - 1, y))
        if x + 1 < width:
            stack.append((x + 1, y))
        if y:
            stack.append((x, y - 1))
        if y + 1 < height:
            stack.append((x, y + 1))

    for x, y in seen:
        red, green, blue, _ = pixels[x, y]
        score = chroma_score(x, y)
        alpha = 0 if score >= 42 else round(255 * (42 - score) / 30)
        neutral = min(red, blue)
        pixels[x, y] = (
            round(red * alpha / 255 + neutral * (255 - alpha) / 255),
            green,
            round(blue * alpha / 255 + neutral * (255 - alpha) / 255),
            alpha,
        )
    return image


def clear_grid_dividers(frame: Image.Image, edge: int = 24) -> Image.Image:
    """Remove cell-edge bleed and long near-white source-sheet separators."""
    # Generated chroma sheets occasionally contain stray near-zero alpha inside
    # bright effects. Treat the source sheet as opaque before key extraction.
    cleaned = frame.convert("RGB").convert("RGBA")
    pixels = cleaned.load()
    width, height = cleaned.size
    divider_centers = {
        x
        for x in range(width)
        if sum(1 for y in range(height) if min(pixels[x, y][:3]) >= 235) > height * 0.5
    }
    divider_columns = {
        candidate
        for x in divider_centers
        for candidate in range(max(0, x - 5), min(width, x + 6))
    }
    for y in range(height):
        for x in range(width):
            if x >= edge and x < width - edge and y >= edge and y < height - edge and x not in divider_columns:
                continue
            pixels[x, y] = (255, 0, 255, 255)
    return cleaned


def normalize_frames(frames: list[Image.Image], target_extent: int) -> list[Image.Image]:
    first_bbox = frames[0].getchannel("A").getbbox()
    if first_bbox is None:
        raise ValueError("first animation frame is empty")
    first_extent = max(first_bbox[2] - first_bbox[0], first_bbox[3] - first_bbox[1])
    scale = target_extent / first_extent
    output = []
    for frame in frames:
        bbox = frame.getchannel("A").getbbox()
        canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
        if bbox:
            content = frame.crop(bbox)
            content = content.resize(
                (max(1, round(content.width * scale)), max(1, round(content.height * scale))),
                Image.Resampling.LANCZOS,
            )
            if content.width >= FRAME or content.height >= FRAME:
                raise ValueError(f"unsafe normalized content: {content.size}")
            canvas.alpha_composite(content, ((FRAME - content.width) // 2, (FRAME - content.height) // 2))
        output.append(canvas)
    return output


def largest_component_bbox(frame: Image.Image) -> tuple[int, int, int, int]:
    alpha = frame.getchannel("A")
    width, height = frame.size
    pixels = alpha.load()
    remaining = {(x, y) for y in range(height) for x in range(width) if pixels[x, y] > 24}
    largest: list[tuple[int, int]] = []
    while remaining:
        seed = remaining.pop()
        component = [seed]
        stack = [seed]
        while stack:
            x, y = stack.pop()
            for point in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.append(point)
                    stack.append(point)
        if len(component) > len(largest):
            largest = component
    if not largest:
        raise ValueError("animation frame is empty")
    xs = [point[0] for point in largest]
    ys = [point[1] for point in largest]
    return min(xs), min(ys), max(xs) + 1, max(ys) + 1


def keep_largest_component(frame: Image.Image) -> Image.Image:
    """Remove detached source-sheet debris while preserving the main building."""
    alpha = frame.getchannel("A")
    width, height = frame.size
    pixels = alpha.load()
    remaining = {(x, y) for y in range(height) for x in range(width) if pixels[x, y] > 24}
    largest: set[tuple[int, int]] = set()
    while remaining:
        seed = remaining.pop()
        component = {seed}
        stack = [seed]
        while stack:
            x, y = stack.pop()
            for point in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    stack.append(point)
        if len(component) > len(largest):
            largest = component
    cleaned = frame.copy()
    cleaned_alpha = cleaned.getchannel("A")
    cleaned_pixels = cleaned_alpha.load()
    for y in range(height):
        for x in range(width):
            if (x, y) not in largest:
                cleaned_pixels[x, y] = 0
    cleaned.putalpha(cleaned_alpha)
    return cleaned


def remove_magenta_fringe(frame: Image.Image) -> Image.Image:
    """Clear residual chroma-key halos that survive as semi-transparent pixels."""
    cleaned = frame.copy()
    pixels = cleaned.load()
    width, height = cleaned.size
    for y in range(height):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            if alpha and red > 145 and blue > 95 and green < 105 and red - green > 55 and blue - green > 30:
                pixels[x, y] = (red, green, blue, 0)
    return cleaned


def robust_body_bbox(frame: Image.Image) -> tuple[int, int, int, int]:
    """Ignore thin detached/connected projectile strokes and keep the massive tower body."""
    alpha = frame.getchannel("A")
    width, height = frame.size
    pixels = alpha.load()
    threshold = max(12, round(min(width, height) * 0.035))
    xs = [x for x in range(width) if sum(pixels[x, y] > 24 for y in range(height)) >= threshold]
    ys = [y for y in range(height) if sum(pixels[x, y] > 24 for x in range(width)) >= threshold]
    if not xs or not ys:
        return largest_component_bbox(frame)
    return min(xs), min(ys), max(xs) + 1, max(ys) + 1


def attack_body_bbox(frame: Image.Image) -> tuple[int, int, int, int]:
    candidates = (largest_component_bbox(frame), robust_body_bbox(frame))
    return min(
        candidates,
        key=lambda box: max(box[2] - box[0], box[3] - box[1]),
    )


def stone_ring_bbox(frame: Image.Image) -> tuple[int, int, int, int]:
    width, height = frame.size
    pixels = frame.load()
    mask = set()
    for y in range(height):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            if alpha > 96 and max(red, green, blue) - min(red, green, blue) < 58 and 42 < red + green + blue < 650:
                mask.add((x, y))
    if not mask:
        return robust_body_bbox(frame)
    threshold = max(18, round(min(width, height) * 0.04))
    xs = [x for x in range(width) if sum((x, y) in mask for y in range(height)) >= threshold]
    ys = [y for y in range(height) if sum((x, y) in mask for x in range(width)) >= threshold]
    if not xs or not ys:
        return robust_body_bbox(frame)
    return min(xs), min(ys), max(xs) + 1, max(ys) + 1


def normalize_attack(frames: list[Image.Image], target_extent: int) -> list[Image.Image]:
    output = []
    base_body = attack_body_bbox(frames[0])
    base_stone = stone_ring_bbox(frames[0])
    base_body_extent = max(base_body[2] - base_body[0], base_body[3] - base_body[1])
    base_stone_extent = max(base_stone[2] - base_stone[0], base_stone[3] - base_stone[1])
    target_stone_extent = base_stone_extent * target_extent / base_body_extent
    for frame in frames:
        full_bbox = frame.getchannel("A").getbbox()
        if full_bbox is None:
            raise ValueError("attack frame is empty")
        component_bbox = largest_component_bbox(frame)
        full_extent = max(full_bbox[2] - full_bbox[0], full_bbox[3] - full_bbox[1])
        component_extent = max(component_bbox[2] - component_bbox[0], component_bbox[3] - component_bbox[1])
        if full_extent > component_extent * 1.08:
            body_bbox = component_bbox
            scale = target_extent / component_extent
        else:
            body_bbox = stone_ring_bbox(frame)
            body_extent = max(body_bbox[2] - body_bbox[0], body_bbox[3] - body_bbox[1])
            scale = target_stone_extent / body_extent
        content = frame.crop(full_bbox)
        content = content.resize(
            (max(1, round(content.width * scale)), max(1, round(content.height * scale))),
            Image.Resampling.LANCZOS,
        )
        body_center_x = ((body_bbox[0] + body_bbox[2]) / 2 - full_bbox[0]) * scale
        body_center_y = ((body_bbox[1] + body_bbox[3]) / 2 - full_bbox[1]) * scale
        left = round(FRAME / 2 - body_center_x)
        top = round(FRAME / 2 - body_center_y)
        # Detached projectiles are rendered by the dedicated projectile asset.
        # If including one would force the locked building body outside the
        # safety cell, keep only the connected building component instead of
        # shrinking the building and breaking cross-animation scale.
        if (
            (left < 0 or top < 0 or left + content.width > FRAME or top + content.height > FRAME)
            and full_extent > component_extent * 1.08
        ):
            cleaned = keep_largest_component(frame)
            content = cleaned.crop(component_bbox).resize(
                (
                    max(1, round((component_bbox[2] - component_bbox[0]) * scale)),
                    max(1, round((component_bbox[3] - component_bbox[1]) * scale)),
                ),
                Image.Resampling.LANCZOS,
            )
            left = round((FRAME - content.width) / 2)
            top = round((FRAME - content.height) / 2)
        overflow = max(-left, -top, left + content.width - FRAME, top + content.height - FRAME)
        if 0 < overflow <= 8:
            left = min(max(left, 1), FRAME - content.width - 1)
            top = min(max(top, 1), FRAME - content.height - 1)
        if left < 0 or top < 0 or left + content.width > FRAME or top + content.height > FRAME:
            raise ValueError(f"unsafe attack content placement: {(left, top, content.width, content.height)}")
        canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
        canvas.alpha_composite(content, (left, top))
        output.append(canvas)
    return output


def normalize_locked_attack(frames: list[Image.Image], target_extent: int) -> list[Image.Image]:
    """Preserve source-sheet body scale when bright materials defeat ring detection."""
    base_bbox = frames[0].getchannel("A").getbbox()
    if base_bbox is None:
        raise ValueError("first attack frame is empty")
    scale = target_extent / max(base_bbox[2] - base_bbox[0], base_bbox[3] - base_bbox[1])
    anchor_x = (base_bbox[0] + base_bbox[2]) / 2
    anchor_y = (base_bbox[1] + base_bbox[3]) / 2
    output = []
    for frame in frames:
        bbox = frame.getchannel("A").getbbox()
        if bbox is None:
            raise ValueError("attack frame is empty")
        content = frame.crop(bbox).resize(
            (max(1, round((bbox[2] - bbox[0]) * scale)), max(1, round((bbox[3] - bbox[1]) * scale))),
            Image.Resampling.LANCZOS,
        )
        left = round(FRAME / 2 - (anchor_x - bbox[0]) * scale)
        top = round(FRAME / 2 - (anchor_y - bbox[1]) * scale)
        if left < 0 or top < 0 or left + content.width > FRAME or top + content.height > FRAME:
            raise ValueError(f"unsafe locked attack content placement: {(left, top, content.width, content.height)}")
        canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
        canvas.alpha_composite(content, (left, top))
        output.append(canvas)
    return output


def save_strip(frames: list[Image.Image], output: Path, slug: str, action: str) -> None:
    atlas = Image.new("RGBA", (FRAME * len(frames), FRAME), (0, 0, 0, 0))
    frame_dir = output / "frames"
    frame_dir.mkdir(parents=True, exist_ok=True)
    for index, frame in enumerate(frames):
        atlas.alpha_composite(frame, (index * FRAME, 0))
        frame.save(frame_dir / f"{slug}-{action}-{index + 1:02d}.png", optimize=True)
    atlas.save(output / f"{slug}-{action}-384-alpha.png", optimize=True)


def idle_frames(master: Image.Image, slug: str) -> list[Image.Image]:
    frames = [master.copy() for _ in range(5)]
    if slug == "obelisk":
        pulses = [(20, 30), (25, 46), (29, 58), (24, 42), (20, 30)]
        for frame, (radius, alpha) in zip(frames, pulses):
            overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            cx, cy = FRAME // 2, FRAME // 2 + 14
            draw.ellipse(
                (cx - radius, cy - radius, cx + radius, cy + radius),
                outline=(186, 78, 255, alpha),
                width=3,
            )
            frame.alpha_composite(overlay)
        return frames
    if slug == "beacon":
        pulses = [(18, 28), (22, 42), (26, 55), (22, 40), (18, 28)]
        for frame, (radius, alpha) in zip(frames, pulses):
            overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            cx, cy = FRAME // 2, FRAME // 2
            draw.ellipse(
                (cx - radius, cy - radius, cx + radius, cy + radius),
                outline=(255, 213, 92, alpha),
                width=3,
            )
            frame.alpha_composite(overlay)
        return frames
    if slug == "ballista":
        glints = [
            ((166, 212), 2, "#9a5b22"),
            ((166, 212), 3, "#d8872c"),
            ((166, 212), 4, "#ffe06b"),
            ((166, 212), 3, "#ffb23f"),
            ((166, 212), 2, "#9a5b22"),
        ]
        for frame, (center, radius, color) in zip(frames, glints):
            overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            x, y = center
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
            frame.alpha_composite(overlay)
        return frames
    if slug == "assassin":
        glints = [
            ((277, 132), 2, "#7e416f"),
            ((278, 131), 3, "#b45a8e"),
            ((279, 130), 4, "#e9a44a"),
            ((278, 131), 3, "#c36c91"),
            ((277, 132), 2, "#7e416f"),
        ]
        for frame, (center, radius, color) in zip(frames, glints):
            overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            x, y = center
            draw.polygon([(x, y - radius), (x + radius, y), (x, y + radius), (x - radius, y)], fill=color)
            frame.alpha_composite(overlay)
        return frames
    if slug == "tracker":
        glints = [
            (192, 143),
            (226, 158),
            (239, 193),
            (224, 227),
            (191, 240),
        ]
        for frame, (x, y) in zip(frames, glints):
            overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            draw.polygon([(x, y - 4), (x + 3, y), (x, y + 4), (x - 3, y)], fill="#ffe06b")
            draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill="#d9ecff")
            frame.alpha_composite(overlay)
        return frames
    if slug == "ranger":
        glints = [
            ((276, 199), 2, "#6f9d48"),
            ((279, 197), 3, "#b6d85c"),
            ((281, 199), 2, "#e6d468"),
            ((278, 201), 3, "#8bbb4b"),
            ((276, 199), 2, "#6f9d48"),
        ]
        for frame, (center, radius, color) in zip(frames, glints):
            overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            x, y = center
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
            frame.alpha_composite(overlay)
        return frames
    # Only the tiny flame tip changes; the source structure remains pixel-identical.
    flame_shapes = [
        ((144, 198), (153, 213), "#ffb23f"),
        ((146, 194), (154, 213), "#ffe06b"),
        ((143, 196), (152, 213), "#e75936"),
        ((145, 192), (154, 213), "#ffb23f"),
        ((144, 198), (153, 213), "#ffe06b"),
    ]
    for frame, (start, end, color) in zip(frames, flame_shapes):
        overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        cx = (start[0] + end[0]) // 2
        draw.polygon([(cx, start[1]), (end[0], end[1] - 4), (cx, end[1]), (start[0], end[1] - 4)], fill=color)
        frame.alpha_composite(overlay)
    return frames


def qa(frames: list[Image.Image]) -> dict:
    bounds = [frame.getchannel("A").getbbox() for frame in frames]
    clipped = [
        index + 1
        for index, box in enumerate(bounds)
        if box and (box[0] <= 0 or box[1] <= 0 or box[2] >= FRAME or box[3] >= FRAME)
    ]
    extents = [max(box[2] - box[0], box[3] - box[1]) if box else 0 for box in bounds]
    if clipped:
        raise ValueError(f"clipped frames: {clipped}")
    return {"extents": extents, "clippedFrames": clipped}


def build(source_dir: Path, output: Path, slug: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    key_frame = border_connected_key_to_alpha if slug == "spawn-cave" else lambda frame: key_to_alpha(frame, preserve_white=True)
    master_source = Image.open(source_dir / f"{slug}-master-v1.png").convert("RGBA")
    master = normalize_frames([key_frame(master_source)], BUILDING_EXTENT)[0]
    idle_path = source_dir / f"{slug}-idle-source-v1.png"
    if idle_path.exists():
        idle = normalize_frames(
            [
                key_frame(clear_grid_dividers(frame))
                for frame in split_grid(Image.open(idle_path), 5, 1, 0)
            ],
            BUILDING_EXTENT,
        )
    else:
        idle = idle_frames(master, slug)
    attack_path = source_dir / f"{slug}-attack-source-v1.png"
    attack = []
    if attack_path.exists():
        attack_sources = [
            key_to_alpha(clear_grid_dividers(frame), preserve_white=True)
            for frame in split_grid(Image.open(attack_path), 4, 1, 0)
        ]
        if slug == "beacon":
            attack_sources[3] = keep_largest_component(attack_sources[3])
        attack = (
            normalize_locked_attack(attack_sources, BUILDING_EXTENT)
            if slug == "beacon"
            else normalize_attack(attack_sources, BUILDING_EXTENT)
        )
    destroy_paths = sorted(source_dir.glob(f"{slug}-destroy-source-v1*.png"))
    destroy_sources = [
        key_frame(clear_grid_dividers(frame))
        for path in destroy_paths
        for frame in split_grid(Image.open(path), 5, 1, 0)
    ]
    destroy = normalize_frames(destroy_sources, BUILDING_EXTENT) if destroy_sources else []
    spawn_path = source_dir / f"{slug}-spawn-source-v1.png"
    spawn = (
        normalize_frames(
            [
                key_frame(clear_grid_dividers(frame))
                for frame in split_grid(Image.open(spawn_path), 5, 1, 0)
            ],
            BUILDING_EXTENT,
        )
        if spawn_path.exists()
        else []
    )
    pulse_path = source_dir / f"{slug}-pulse-source-v1.png"
    pulse = (
        normalize_frames(
            [
                key_frame(clear_grid_dividers(frame))
                for frame in split_grid(Image.open(pulse_path), 4, 1, 0)
            ],
            BUILDING_EXTENT,
        )
        if pulse_path.exists()
        else []
    )
    projectile_alpha_source = source_dir / f"{slug}-projectile-source-alpha-v1.png"
    projectile_source = projectile_alpha_source if projectile_alpha_source.exists() else source_dir / f"{slug}-projectile-source-v1.png"
    projectile_extent = PROJECTILE_EXTENTS.get(slug, 96)
    projectile = normalize_frames([alpha_source(projectile_source)], projectile_extent) if projectile_source.exists() else []
    impact_alpha_source = source_dir / f"{slug}-impact-source-alpha-v1.png"
    impact_source = impact_alpha_source if impact_alpha_source.exists() else source_dir / f"{slug}-impact-source-v1.png"
    impact_extent = IMPACT_EXTENTS.get(slug, 104)
    impact = normalize_frames([alpha_source(impact_source)], impact_extent) if impact_source.exists() else []
    if slug in CLEAN_FRINGE_SLUGS:
        idle = [remove_magenta_fringe(frame) for frame in idle]
        destroy = [remove_magenta_fringe(frame) for frame in destroy]
        attack = [remove_magenta_fringe(frame) for frame in attack]
        spawn = [remove_magenta_fringe(frame) for frame in spawn]
        pulse = [remove_magenta_fringe(frame) for frame in pulse]
        projectile = [remove_magenta_fringe(frame) for frame in projectile]
        impact = [remove_magenta_fringe(frame) for frame in impact]
    save_strip(idle, output, slug, "idle")
    if attack:
        save_strip(attack, output, slug, "attack")
    if destroy:
        save_strip(destroy, output, slug, "destroy")
    if spawn:
        save_strip(spawn, output, slug, "spawn")
    if pulse:
        save_strip(pulse, output, slug, "pulse")
    if projectile:
        projectile[0].save(output / f"{slug}-projectile-384-alpha.png", optimize=True)
    if impact:
        impact[0].save(output / f"{slug}-impact-384-alpha.png", optimize=True)
    manifest = {
        "object": slug,
        "format": "RGBA PNG",
        "frameSize": [FRAME, FRAME],
        "pivot": [0.5, 0.5],
        "normalization": "locked 255px intact building extent; centered 384px safety cell",
        "actions": {
            "idle": {
                "file": f"{slug}-idle-384-alpha.png",
                "frames": 5,
                "durationMs": 720 if slug == "spawn-cave" else 180,
                "loop": True,
            },
        },
        "qa": {"idle": qa(idle)},
    }
    if destroy:
        manifest["actions"]["destroy"] = {
            "file": f"{slug}-destroy-384-alpha.png",
            "frames": len(destroy),
            "durationMs": 160 if slug == "castle" else 130,
            "loop": False,
            "holdLast": True,
        }
        manifest["qa"]["destroy"] = qa(destroy)
    if spawn:
        manifest["actions"]["spawn"] = {
            "file": f"{slug}-spawn-384-alpha.png",
            "frames": len(spawn),
            "durationMs": 180,
            "loop": False,
        }
        manifest["qa"]["spawn"] = qa(spawn)
    if pulse:
        manifest["actions"]["pulse"] = {
            "file": f"{slug}-pulse-384-alpha.png",
            "frames": len(pulse),
            "durationMs": 140,
            "loop": False,
        }
        manifest["qa"]["pulse"] = qa(pulse)
    if attack:
        manifest["actions"]["attack"] = {"file": f"{slug}-attack-384-alpha.png", "frames": 4, "durationMs": 90, "loop": False}
        manifest["qa"]["attack"] = qa(attack)
    if projectile:
        manifest["actions"]["projectile"] = {"file": f"{slug}-projectile-384-alpha.png", "extent": projectile_extent}
        manifest["qa"]["projectile"] = qa(projectile)
    if impact:
        manifest["actions"]["impact"] = {"file": f"{slug}-impact-384-alpha.png", "extent": impact_extent}
        manifest["qa"]["impact"] = qa(impact)
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: build_building_runtime.py SOURCE_DIR OUTPUT_DIR SLUG")
    build(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3])

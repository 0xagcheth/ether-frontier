from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "assets/staging/candidates/watchtower/decomposition_v3"
    / "watchtower_crossbow_group_v2_alpha.png"
)
OUTPUT = (
    ROOT
    / "assets/staging/candidates/watchtower/decomposition_v3"
    / "watchtower_crossbow_coherent_master_v4.png"
)

CANVAS = (1254, 1254)
OBJECT_CENTER = (627, 627)
TARGET_MAX_SIZE = (540, 540)


def main() -> None:
    source = Image.open(SOURCE).convert("RGBA")
    bbox = source.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("Crossbow source is empty")
    weapon = source.crop(bbox)
    weapon.thumbnail(TARGET_MAX_SIZE, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    position = (
        round(OBJECT_CENTER[0] - weapon.width / 2),
        round(OBJECT_CENTER[1] - weapon.height / 2),
    )
    canvas.alpha_composite(weapon, position)
    canvas.save(OUTPUT, optimize=True)
    print(OUTPUT)
    print({"position": position, "size": weapon.size, "pivot": OBJECT_CENTER})


if __name__ == "__main__":
    main()

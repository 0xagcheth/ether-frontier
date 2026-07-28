from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
LAYER_DIR = ROOT / "assets/staging/candidates/watchtower/layers"
OUT_DIR = ROOT / "assets/staging/candidates/watchtower"


def alpha_crop(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    box = image.getchannel("A").getbbox()
    if box is None:
        raise ValueError("Layer has no visible pixels")
    return image.crop(box)


def fit(layer_name: str, size: tuple[int, int]) -> Image.Image:
    image = alpha_crop(
        Image.open(LAYER_DIR / f"watchtower_{layer_name}_v1_alpha.png")
    )
    image.thumbnail(size, Image.Resampling.LANCZOS)
    return image


def place_center(
    canvas: Image.Image, image: Image.Image, center: tuple[int, int]
) -> None:
    x = round(center[0] - image.width / 2)
    y = round(center[1] - image.height / 2)
    canvas.alpha_composite(image, (x, y))


def build_composite() -> None:
    canvas = Image.new("RGBA", (1254, 1254), (0, 0, 0, 0))
    base = fit("base_body", (1110, 1110))
    place_center(canvas, base, (627, 620))

    bearing = fit("bearing", (350, 350))
    place_center(canvas, bearing, (627, 625))

    bolt_reserve = fit("bolt_reserve", (220, 145))
    place_center(canvas, bolt_reserve, (625, 900))

    crossbow = fit("crossbow", (400, 400))
    place_center(canvas, crossbow, (635, 610))

    signal_cloth = fit("signal_cloth", (220, 225))
    place_center(canvas, signal_cloth, (390, 465))

    lantern = fit("lantern_casing", (145, 145))
    place_center(canvas, lantern, (980, 655))

    canvas.save(OUT_DIR / "watchtower_decomposition_composite_v1.png", optimize=True)


def build_review_grid() -> None:
    names = [
        ("base_body", "01 base_body"),
        ("bearing", "02 bearing"),
        ("crossbow", "03 crossbow"),
        ("signal_cloth", "04 signal_cloth"),
        ("lantern_casing", "05 lantern_casing"),
        ("bolt_reserve", "06 bolt_reserve"),
    ]
    cell_w, cell_h = 430, 430
    header_h = 54
    grid = Image.new("RGBA", (cell_w * 3, (cell_h + header_h) * 2), "#202326")
    draw = ImageDraw.Draw(grid)
    font = ImageFont.load_default(size=22)

    for index, (name, label) in enumerate(names):
        col, row = index % 3, index // 3
        x0 = col * cell_w
        y0 = row * (cell_h + header_h)
        draw.rectangle(
            (x0, y0, x0 + cell_w - 1, y0 + header_h - 1), fill="#30363b"
        )
        draw.text((x0 + 16, y0 + 16), label, fill="#f2e6cb", font=font)
        draw.rectangle(
            (x0, y0 + header_h, x0 + cell_w - 1, y0 + header_h + cell_h - 1),
            fill="#151719",
            outline="#596168",
            width=1,
        )
        image = fit(name, (cell_w - 50, cell_h - 50))
        px = x0 + (cell_w - image.width) // 2
        py = y0 + header_h + (cell_h - image.height) // 2
        grid.alpha_composite(image, (px, py))

    grid.convert("RGB").save(
        OUT_DIR / "watchtower_decomposition_review_grid_v1.jpg",
        quality=92,
        optimize=True,
    )


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_composite()
    build_review_grid()

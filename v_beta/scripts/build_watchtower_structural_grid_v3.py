import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
LAYER_DIR = (
    ROOT / "assets/staging/candidates/watchtower/decomposition_v3/structural_layers"
)
MANIFEST = LAYER_DIR / "watchtower_structural_layers_v3.fragment.json"
OUTPUT = (
    ROOT
    / "assets/staging/candidates/watchtower/decomposition_v3"
    / "watchtower_structural_review_grid_v3.jpg"
)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    layers = [
        layer for layer in data["layers"] if layer.get("runtimeCandidate", True)
    ]
    columns = 7
    rows = (len(layers) + columns - 1) // columns
    cell_w, cell_h, header = 250, 250, 38
    grid = Image.new("RGB", (columns * cell_w, rows * (cell_h + header)), "#17191b")
    draw = ImageDraw.Draw(grid)
    font = ImageFont.load_default(size=16)

    for index, layer in enumerate(layers):
        col, row = index % columns, index // columns
        x0 = col * cell_w
        y0 = row * (cell_h + header)
        draw.rectangle((x0, y0, x0 + cell_w - 1, y0 + header - 1), fill="#30353a")
        draw.text((x0 + 10, y0 + 11), layer["id"], fill="#f1e2c5", font=font)
        image = Image.open(LAYER_DIR / layer["file"]).convert("RGBA")
        image.thumbnail((cell_w - 28, cell_h - 28), Image.Resampling.LANCZOS)
        tile = Image.new("RGBA", (cell_w, cell_h), "#101214")
        tile.alpha_composite(
            image, ((cell_w - image.width) // 2, (cell_h - image.height) // 2)
        )
        grid.paste(tile.convert("RGB"), (x0, y0 + header))

    grid.save(OUTPUT, quality=92, optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()

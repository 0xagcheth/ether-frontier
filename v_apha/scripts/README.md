# Asset Scripts

- Top-level scripts extract prompts and prepare generated sprites or strips.
- `asset_tools/pack_sprite_atlas.py` is the generic atlas packer.

All project paths must be derived from `Path(__file__)`; do not add machine-specific absolute paths. Inputs belong in `assets/staging/`, approved masters in `assets/approved/`, and outputs consumed by the game in `assets/runtime/`.

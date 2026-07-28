# Art Bible

## Visual Identity

Ether Frontier uses clean illustrated 2D near top-down with slight tilt game art. It is near top-down view with a slight angled tilt, not full isometric, not 3/4 side-view, not perspective, and not pixel art.

The master language lives in `master-visual-style.md`. This Art Bible summarizes the production rules that keep that language consistent.

## Reference Direction

References are allowed only as explanations of design principles, never as style targets to copy.

Allowed reference usage:

- Large readable RTS shape language means silhouettes and faction clarity, not surface rendering.
- Classic game readability means instant recognition, not imitation.
- Traditional late 1980s-1990s hand-painted animation means clean forms, expressive silhouettes, and disciplined color/light, not a studio look.
- Heroic material design means strong readable material identity, not texture noise.

## Camera

NEAR TOP-DOWN WITH SLIGHT TILT.

Objects are designed for a camera almost directly above the world with a small angled tilt.

Top planes must dominate: 85-90% of the read should come from roofs, crowns, upper surfaces, and top silhouettes. Side faces are only 10-15% subtle thickness cues. Assets must not rely on baked perspective, forced depth, or a fixed environment angle.

For ordinary gameplay towers, do not show a tall front facade, full doorway, staircase, or vertical wall dominating the asset.

## Palette Canon

- Fortress: cold stone grey and blue-grey shadow.
- Player power: warm amber, orange, candle-gold, torchlight.
- Horde bodies: green to grey-green skin and muted scrap materials.
- Horde magic: toxic green with restrained sickly purple accents.
- Grass: blue-green, never saturated generic green.
- Wood: warm brown.
- Gold: precious warm accent, not yellow plastic.
- Forbidden object pixels: pure black and near-black, except where a source file intentionally uses black as a pre-cutout key.

## Anti-Drift Rules

- Do not make assets 3D-rendered.
- Do not use pixel-art language as the active style requirement.
- Do not use full isometric, 3/4 side-view, or perspective camera language.
- Do not use tall facade, full doorway, staircase, or dominant vertical-wall language for ordinary gameplay towers.
- Do not use glossy AI rendering, concept-art rendering, photobashing, painterly brush noise, or random texture overlays.
- Do not let enemy magic become player amber.
- Do not let player towers inherit Horde toxic-green as their primary read.
- Do not create unrelated faction palettes without a creative-direction change.

## Canon Asset Comparison

Written art direction is not enough for production approval. Every new visual asset must be compared against the closest references in `../05_assets/canon-asset-registry.md`, must pass `style-self-review.md`, and must pass `style-drift.md`.

If a category has no Canon Asset yet, production should first create or nominate a reference candidate and review it through `../07_pipeline/quality-gate.md`.

## Source Material

Merged from archived lore/art style, the current prompt bible, and project requirements.

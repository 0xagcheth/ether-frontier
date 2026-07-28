# Quality Checklists

These checklists support `quality-gate.md`. They do not approve work by themselves.

An asset is not accepted because it looks beautiful. It is accepted only if style, readability, atlas, engine, palette, proportions, animation, and gameplay all pass the quality gate.

## Asset Acceptance

- Matches project vision and art bible.
- Uses correct near top-down with slight tilt object read: 85-90% top planes, 10-15% side thickness.
- Ordinary gameplay towers have no tall facade, full doorway, staircase, or dominant vertical wall.
- Uses correct faction palette.
- Has no pure-black object pixels.
- Has transparent or valid black-key background as required by pipeline stage.
- Owns a dedicated atlas under 5 MB.
- Contains no unrelated objects.
- Has stable scale, pivot, and baseline.
- For layered objects: runtime atlas is compact/transparent and driven by JSON tight rects.
- For layered objects: fixed-cell review grid is separate from runtime assets.
- For layered objects: review-only previews/labels/grid lines are absent from runtime atlas.
- Reads at gameplay size.
- Passes `../03_art/style-self-review.md`.

## Animation Acceptance

- Correct actions exist.
- Correct projections exist for directional units.
- Frame count matches contract.
- No baseline jitter.
- No building body breathing.
- Layered idle motion comes only from child layers such as flag, flame, smoke, gear, lens, rune, or active part.
- Rotatable gameplay parts declare pivots and can be aimed without redrawing the base/body.
- Death holds a readable final state.
- Attack anticipation and impact are readable.

## UI Acceptance

- Readable at gameplay scale.
- Consistent medieval fortress material language.
- Does not obscure tactical information.
- Mobile hit targets are large enough.
- Icons and text clarify action and state.

## Level Acceptance

- Paths read immediately.
- Buildable zones are clear.
- Enemy pressure is previewed.
- Resources support decisions.
- Boss waves have enough visual space.

## Code Acceptance

- Does not hard-code new art rules outside docs.
- Keeps naming aligned with asset contract.
- Does not expand legacy shared atlas as a production pattern.
- Adds validation where content can fail silently.

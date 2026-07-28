# Art Bible

## Visual Identity

Ether Frontier uses clean illustrated 2D board-game art printed on layered
cardboard. Runtime gameplay objects use exact true top-down orthographic 90°.
Gameplay-board concepts use an 80–90° overhead presentation; narrative key art
may be more expressive but never becomes a projection reference for sprites.

The master language lives in `master-visual-style.md`. This Art Bible summarizes the production rules that keep that language consistent.

## Reference Direction

References are allowed only as explanations of design principles, never as style targets to copy.

Allowed reference usage:

- Large readable RTS shape language means silhouettes and faction clarity, not surface rendering.
- Classic game readability means instant recognition, not imitation.
- Traditional late 1980s-1990s hand-painted animation means clean forms, expressive silhouettes, and disciplined color/light, not a studio look.
- Heroic material design means strong readable material identity, not texture noise.

## Camera

RUNTIME OBJECTS: TRUE TOP-DOWN ORTHOGRAPHIC 90°.

The camera is directly overhead. Top planes and cut silhouettes define the
object. Side faces never become facades; only thin punchboard edges reveal
physical thickness. Assets must not rely on baked perspective, forced depth or
a fixed environment angle.

For ordinary gameplay towers, do not show a tall front facade, full doorway, staircase, or vertical wall dominating the asset.

## Palette Canon

- Overall print: vivid heroic fantasy with clear mid-to-high saturation; never a
  uniformly faded beige/grey craft palette.
- Guardians/Yav: cold stone, wind blue, burgundy, pine green, golden ochre and
  warm amber memory light.
- Gromovik: copper, burgundy, warm white and controlled lightning cyan.
- Volkhv of the Name Circle: deep indigo, birch-bark tan, oxidized copper and
  warm ivory name-light.
- Amur Pathfinder: pine green, river blue-grey, bark tan and muted red accents.
- Lower City: marsh green, clay ochre, dark turquoise, dried red and bone.
- Grey: ash grey, pale lilac, cold cyan and precise white highlights.
- Damaged Nav: indigo, smoke white, oxidized green and restrained violet.
- Captured constructions: faded enamel, rust, copper, cable black-brown and pale
  Grey inserts.
- Grass: blue-green, never saturated generic green.
- Wood: warm brown.
- Gold: precious warm accent, not yellow plastic.
- Forbidden object pixels: pure black and near-black, except where a source file intentionally uses black as a pre-cutout key.

## Anti-Drift Rules

- Do not make assets 3D-rendered.
- Layered objects use smooth board-game punchboard, never visible corrugated
  packaging flutes.
- `Smooth punchboard` means solid rather than corrugated, not textureless. Fine
  paper fibers, pressed pulp variation and natural speckles remain visible on
  exposed cardboard and subtly through every printed color.
- Surface color reads as matte cute cartoon print on cardboard, not realistic
  paint or photoreal material rendering.
- Reject perfectly flat vector fills, airbrushed plastic gradients, polished
  foam, rubber, clay, or smooth 3D-token surfaces.
- Printed ornament uses sparse original Slavic/Old-Russian-inspired geometry:
  simple diamonds, stepped lines, small solar notches and short border rhythms.
  No ornate curls, filigree, baroque fantasy framing, all-over embossing, or
  copied sacred/historical symbols.
- Ornament is limited to one or two secondary pieces per object. Most printed
  surfaces stay plain; never repeat a motif across every layer or module.
- Sparse decoration must not desaturate the asset. Primary printed color masses
  stay warm, clear and moderately saturated; matte means non-glossy, not faded.
- Palette uses broad classic RTS readability principles—earthy heroic
  saturation and strong faction separation—without naming or copying any
  franchise, symbol, faction design, asset or surface pattern.
- Every overlapping cardboard child has a readable compact contact shadow on the
  layer directly beneath it.
- Every child also retains its own full cut outline, thin paperboard edge, and a
  tiny separation gap; color boundaries alone never represent layered parts.
- Do not use pixel-art language as the active style requirement.
- Do not use full isometric, 3/4 side-view, or perspective camera language.
- Do not use tall facade, full doorway, staircase, or dominant vertical-wall language for ordinary gameplay towers.
- Do not use glossy AI rendering, concept-art rendering, photobashing, painterly brush noise, or random texture overlays.
- Do not let Grey cyan or Lower City marsh-green become the main Zastava identity.
- Do not use the deprecated Goblin Horde palette or insignia.
- Do not use Kitezh-17, laboratory, facility-code or archive-stamp identity.
- Do not create unrelated faction palettes without a creative-direction change.

## Canon Asset Comparison

Written art direction is not enough for production approval. Every new visual asset must be compared against the closest references in `../05_assets/canon-asset-registry.md`, must pass `style-self-review.md`, and must pass `style-drift.md`.

If a category has no Canon Asset yet, production should first create or nominate a reference candidate and review it through `../07_pipeline/quality-gate.md`.

## Source Material

Merged from archived lore/art style, the current prompt bible, and project requirements.

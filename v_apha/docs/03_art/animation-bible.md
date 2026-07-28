# Animation Bible

## Unit Actions

Moving units use:

- `spawn`
- `walk`
- `attack`
- `death`
- `breach`

Ranged units also use directional `projectile` strips.

## Projections

Directional units use six projections:

- `front`
- `back`
- `3qr`
- `3ql`
- `sider`
- `sidel`

Mirror pairs may be derived during prototyping, but final production should preserve lighting and asymmetric gear.

## Building Actions

Buildings use:

- `idle`
- `attack`
- `destroy`

Economy and decor assets may use `idle` plus `destroy` only. Resources may use `grow`.

## Layered Animation Standard

New building, tower, resource, decor, projectile, and VFX work should be authored as layered animation where practical.

The preferred model is:

- the base/body layer stays locked;
- only named sub-elements animate;
- gameplay-facing parts rotate or move independently;
- transient effects are separate layers, not baked into every full-object frame;
- the engine or preview composer assembles the final object from the manifest.

For towers, examples:

- crossbow, cannon barrel, ballista arm, prism, lens, or crystal may rotate toward target;
- flag cloth uses a wind loop independent of attack timing;
- lanterns, braziers, crystals, runes, and gears use independent idle loops;
- muzzle flash and charge effects play once per attack;
- projectile and impact are separate owner-scoped sprites;
- destroy uses debris/ruin overlays and may fall back to baked collapse frames if true layer destruction is not readable.

For economy objects:

- saw blade, wheel, pulley, smoke, conveyor, crane, bucket, and dust should be independent layers when visible.

For resources/environment:

- growth, wind sway, sparkle, leaf motion, and collection debris should be separate layers when it improves readability or file size.

For units:

- keep the body readable first; separate weapons, shields, capes, glows, projectiles, and death debris when this improves animation quality.

## Locked-Body Idle Rule

Building idle animation must never scale, breathe, bob, redraw, or shift the solid structure. Only named physical sub-elements may animate:

- flame
- smoke
- gears
- wheels
- banners
- chains
- lenses
- crystals
- liquids
- sparks
- rune blink

If no physical sub-element can animate, idle is one static frame.

In layered atlases, this rule is enforced by keeping `base_token` / `body_static` constant across idle. Idle motion must come from child layers such as `flag_cloth`, `lantern_flame`, `gear`, `lens`, `smoke`, `rune`, or `active_part`, with their pivots and attachments declared in JSON.

## Frame Rules

- Enemies and heroes: target 5-7 frames per action.
- Buildings: idle 5-6, attack 4-5, destroy 5 unless overridden by object contract.
- Frame strips are horizontal, evenly spaced, and same cell size per object/action set.
- Baseline jitter is a rejection condition.

Layered atlases may use named cells instead of horizontal full-object strips. In that case the JSON manifest replaces strip position assumptions and must define:

- clip name;
- layer list;
- frame list;
- duration;
- loop/hold behavior;
- runtime transform source, if any.

The final composed preview must still pass the same no-jitter, no-clipping, and locked-footprint checks as a baked strip.

## Source Material

Merged from the prompt bible and the asset-pass progress notes about locked tower bodies.

# Watchtower Simple Bolt v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__projectile__simple_bolt_v1_chroma.png`

Module ID: `watchtower__projectile__simple_bolt`

Status: **canon module; composed trajectory pending user confirmation**

## Module contract

- Object: `watchtower`
- Owner: `watchtower__active_addon__light_single_crossbow`
- Slot: `projectile`
- Runtime behavior: spawn from crossbow `muzzle_anchor`; rotate along trajectory
- Local forward axis: `+X`, arrowhead toward image-right
- Contains: one wood shaft, one metal point, one restrained red fletching set
- Must not contain: crossbow, muzzle flash, trail, impact, glow, debris, extra ammunition, labels, grid, or pivot cross

## Visual review

- True 90° top-down projection: PASS
- Exact horizontal +X orientation: PASS
- Symmetry across the flight axis: PASS
- Flat die-cut cardboard construction: PASS
- Exposed tan cardboard edge around the silhouette: PASS
- Palette matches Watchtower wood/metal/red accents: PASS
- Arrowhead and tail are visually unambiguous: PASS
- Readable at later reduced game scale: PASS
- One isolated projectile with clear chroma margin: PASS
- No clipping: PASS
- No baked motion trail, flash, or impact: PASS
- No perspective or glossy 3D material: PASS

## Generation record

- Mode: built-in ImageGen
- Canvas: `1774 × 887 px`
- Chroma key: `#ff00ff`

Final prompt summary: one simple Watchtower crossbow bolt in exact overhead orthographic projection; horizontal with point toward local `+X`; warm wood shaft, dark metal point, restrained red paper fletching, tan cardboard cut edge; uniform magenta chroma; no weapon, trail, flash, impact, extra projectiles, labels, grid, shadows, perspective, or 3D rendering.

## Next gate

## Prepared runtime source

- Alpha layer: `assets/approved/canon/modules/fortress_ranged/watchtower__projectile__simple_bolt_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__projectile__simple_bolt_v1.json`
- Tight rect: `1553 × 263 px`
- `trajectoryPivot`: `[776, 131] px`
- Tail `spawn_anchor`: `[0, 131] px`
- Tip `impact_anchor`: `[1552, 131] px`
- Runtime scale: `0.26` of composed weapon length
- Composed size: `203 × 34 px`
- Draw order: `40`
- Alpha PNG size: approximately `412 KB`
- Visible magenta spill pixels: `0`

## Composed trajectory validation

- Tail aligns with crossbow `muzzle_anchor`: PASS
- Projectile forward axis matches weapon local `+X`: PASS
- Central pivot remains stable under trajectory rotation: PASS
- `+X`, `+45°`, and `-45°` directions remain readable: PASS
- No clipping in isolated runtime layer: PASS
- Projectile is separate from muzzle flash and impact: PASS
- Game-scale silhouette readability: PASS at `203 × 34 px`

Muzzle-spawn composite: `assets/staging/reviews/modules/fortress_ranged/watchtower__simple_bolt_v1_muzzle_spawn_composite.png`

Separate trajectory QA grid: `assets/staging/reviews/modules/fortress_ranged/watchtower__simple_bolt_v1_trajectory_review_grid.png`

After user approval of the trajectory preview:

1. lock the projectile transform in the Watchtower assembly contract;
2. generate all four compact muzzle-flash frames in one consistent source sheet;
3. normalize the flash loop to one muzzle-side pivot and validate the one-shot attack composition.

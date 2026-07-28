# Watchtower Light Single Crossbow v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__active_addon__light_single_crossbow_v1_chroma.png`

Module ID: `watchtower__active_addon__light_single_crossbow`

Status: **canon module; composed rotation pending user confirmation**

## Module contract

- Object: `watchtower`
- Family: `fortress_ranged`
- Slot: `active_addon`
- Runtime behavior: rotates independently around the center socket toward the target
- Local forward axis: `+X`, exactly image-right
- Contains: complete light crossbow body, limbs, string, trigger, reinforcement, mounting aperture
- Must not contain: projectile bolt, muzzle flash, base, socket, lantern, flag, operator, ammunition, labels, grid, or pivot cross

## Visual review

- True 90° top-down projection: PASS
- Firing axis horizontal toward image-right: PASS
- Symmetry across the horizontal weapon axis: PASS
- Flat cardboard tabletop construction: PASS
- Exposed tan cardboard edge around silhouette and axle opening: PASS
- Warm wood / dark blue-grey metal family palette: PASS
- Independent central rotation aperture: PASS
- Readable right-side muzzle for later attachment anchor: PASS
- No loaded projectile or baked attack effect: PASS
- One isolated component with clear chroma margin: PASS
- No clipping: PASS
- No side-view weapon body or glossy 3D material: PASS

## Generation record

- Mode: built-in ImageGen
- Canvas: `1536 × 1024 px`
- Chroma key: `#ff00ff`

Final prompt summary: one standalone lightweight Watchtower crossbow; exact top-down orthographic projection; firing direction right on local `+X`; centered mechanical rotation aperture; flat die-cut cardboard with warm printed wood, dark blue-grey metal, ink outlines, tan cut edge; uniform magenta chroma; no bolt, flash, parent layers, labels, grid, shadow, perspective, or 3D rendering.

## Next gate

## Prepared runtime source

- Alpha layer: `assets/approved/canon/modules/fortress_ranged/watchtower__active_addon__light_single_crossbow_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__active_addon__light_single_crossbow_v1.json`
- Tight rect: `1316 × 896 px`
- Rotation pivot: `[648, 447] px`
- Pivot source: centroid of the enclosed axle aperture, area `1768 px`
- Muzzle anchor: `[1315, 447] px`
- Scale relative to base footprint: `0.72`
- Composed size: `779 × 530 px`
- Draw order: `30`
- Alpha PNG size: approximately `675 KB`
- Visible magenta spill pixels: `0`

## Rotation-envelope validation

- Rotation envelope radius: `396 px`
- Base footprint radius: `541 px`
- Complete `360°` envelope remains inside the base footprint: PASS
- Pivot remains locked to the center socket at `0°/90°/180°/270°`: PASS
- Muzzle rotates with the weapon and preserves local `+X`: PASS
- No clipping at cardinal angles: PASS
- Base/body footprint remains unchanged: PASS
- Lantern housing may be visually crossed by the weapon at some angles but remains an independent lower draw-order child: PASS

Composite: `assets/staging/reviews/modules/fortress_ranged/watchtower__core_plus_light_crossbow_v1_composite.png`

Separate rotation QA grid: `assets/staging/reviews/modules/fortress_ranged/watchtower__light_crossbow_v1_rotation_review_grid.png`

After user approval of the composed scale and rotation:

1. lock the weapon transform in the Watchtower assembly contract;
2. generate the separate `watchtower__projectile__simple_bolt` aligned to local `+X`;
3. validate projectile pivot and trajectory rotation before generating muzzle flash frames.

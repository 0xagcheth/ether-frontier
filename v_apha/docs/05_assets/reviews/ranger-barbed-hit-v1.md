# Ranger barbed hit v1

Status: **canon — visual and technical gates passed**

## Identity

- ID: `ranger__impact_fx__barbed_hit_v1`
- Owner: `ranger`
- Family: `fortress_ranged`
- Slot: `impact_fx`
- Runtime role: four-frame non-looping effect spawned at `barbed_bolt.impact_tip`
- Candidate: `assets/staging/candidates/modules/ranger/ranger__impact_fx__barbed_hit_v1_source_chroma.png`

## Source-sheet structure

- Canvas: `1254 × 1254 px`
- Layout: exactly four isolated groups in reading-order `2 × 2`
- Top-left: compact four-direction contact burst
- Top-right: wider angular burst with one green accent fragment
- Bottom-left: expanded broken ring of grey and ochre shards
- Bottom-right: sparse fading fragments
- Stable empty contact center in every quadrant

## Modular contract

Included:

- four chronological paper/cardboard shard groups;
- ochre, dark iron-grey and restrained green accents;
- stable center suitable for tip/contact attachment.

Excluded:

- bolt, weapon, target, wound and blood;
- smoke, fire, glow, realistic explosion and blur;
- labels, grid, pivot marker, fifth group, shadow, perspective and 3D render.

## Visual QA

- [x] Exactly four isolated quadrant groups
- [x] Stable empty center and outward chronological expansion
- [x] Contact → larger burst → broken ring → fade progression
- [x] Physical matte paper/cardboard construction
- [x] No projectile, target, smoke, glow, labels, or grid
- [x] Generous chroma separation and no clipping

## Generation

- Mode: built-in ImageGen
- Earlier two requests failed with network errors and produced no files.
- Successful retry used the same built-in path and preserved the locked effect contract.

## Technical result

- Manifest: `assets/approved/canon/modules/ranger/ranger__impact_fx__barbed_hit_v1.json`
- Runtime frames: four separate transparent PNG files
- Shared canvas: `627 × 627 px`
- Shared contact pivot: `[313, 313] px`
- Timing: `55 / 70 / 90 / 120 ms`; total `335 ms`; non-looping
- Runtime scale: `0.72` of projectile length
- Draw order: `55`
- Runtime frame bytes: `1,216,374` — under `5 MB`
- Magenta spill by frame: `0 / 0 / 0 / 0 px`
- Review grid: `assets/staging/reviews/modules/ranger/ranger__impact_fx__barbed_hit_v1_review_grid.png`
- Contact preview: `assets/staging/reviews/modules/ranger/ranger__impact_fx__barbed_hit_v1_contact_preview.gif`

## Gate

Barbed hit promoted to canon after shared-center normalization, despill, timing, and bolt-tip contact validation. Ranger now has no missing owner-specific animation layers.

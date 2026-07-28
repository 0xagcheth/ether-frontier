# Fortress Ranged Stone Rim Chunk A v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_a_v1_chroma.png`

Module ID: `fortress_ranged__debris__stone_rim_chunk_a`

Status: **canon module; runtime scale pending user confirmation**

## Module contract

- Family: `fortress_ranged`
- Slot: `debris`
- Shared use: destruction animations for light fortress-ranged bases
- Runtime behavior: independent translation and rotation under destroy animation/physics
- Contains: one connected broken curved rim brick
- Must not contain: floor slab, assembled platform sector, neighboring bricks, pile, detached chips, dust, smoke, wood, metal hardware, labels, grid, or pivot cross

## Visual review

- Exactly one connected debris component: PASS
- Compact curved-trapezoid rim-brick silhouette: PASS
- True 90° top-down projection: PASS
- One curved outer edge and jagged broken inner edge: PASS
- Single printed structural crack: PASS
- Muted blue-grey stone face: PASS
- Exposed tan cardboard edge around complete silhouette: PASS
- No neighboring masonry or platform floor: PASS
- No detached chips or garbage pixels: PASS
- One isolated component with generous chroma margin: PASS
- No clipping, shadow, side view, or glossy 3D rendering: PASS

## Generation record

- Mode: built-in ImageGen
- Approved visual candidate canvas: `1635 × 962 px`
- Chroma key: `#ff00ff`
- First generated variant was rejected before project import because it depicted a large multi-stone platform sector rather than one addressable fragment

Final successful prompt summary: one small individual curved fortress rim brick, exact top-down view, compact `1.7:1` broken trapezoid, blue-grey printed stone, one crack, jagged inner break and tan cardboard cut edge; uniform magenta chroma; no platform slab, ring sector, neighboring blocks, rubble, detached chips, smoke, perspective, or 3D rendering.

## Next gate

## Prepared runtime source

- Alpha layer: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_a_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_a_v1.json`
- Tight rect: `1195 × 640 px`
- Alpha-weighted center-of-mass pivot: `[602, 299] px`
- Scale relative to base footprint: `0.14`
- Composed size: `151 × 81 px`
- Alpha PNG size: `1,473,554 bytes` — PASS under `5 MB`
- Visible magenta spill pixels: `0`
- Draw order during destruction: `60`
- Shared by: Watchtower, Ranger, Tracker, Assassin

## Destroy-physics defaults

- Mass class: `medium`
- Radial velocity: `90–170 px/s`
- Angular velocity: `−220…220°/s`
- Linear drag: `0.92`
- Lifetime: `700–1100 ms`

## Scale validation

- Size comparable to one intact outer-rim stone: PASS
- Center-of-mass pivot remains inside the dominant material area: PASS
- Shape remains readable at game scale: PASS
- No clipping or detached fragments: PASS

Separate scale/pivot review: `assets/staging/reviews/modules/fortress_ranged/fortress_ranged__stone_rim_chunk_a_v1_review.png`

After user approval of the runtime scale:

1. lock `stone_rim_chunk_a` in the shared debris kit;
2. generate `stone_rim_chunk_b` as a different individual silhouette;
3. continue one physical debris module at a time.

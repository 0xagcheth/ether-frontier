# Fortress Ranged — Stone Rim Chunk B v1

Status: **canon module — runtime pair awaiting confirmation**

## Asset

- ID: `fortress_ranged__debris__stone_rim_chunk_b_v1`
- Family: `fortress_ranged`
- Role: independently animated destruction debris
- Source: built-in ImageGen
- Candidate: `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_b_v1_chroma.png`
- Source canvas: `1254 × 1254 px`
- Source size: approximately `1.3 MB`

## Visual intent

- Exactly one connected loose stone-cardboard fragment.
- Strict 90-degree top-down orthographic projection.
- Compact near-square irregular silhouette, distinct from chunk A's wide curved form.
- Short intact upper rim, jagged broken perimeter, and one integrated bite-shaped notch.
- Flat muted blue-grey printed stone face, dark ink outline, and exposed tan cardboard edge.
- Uniform `#ff00ff` chroma field with generous isolation padding.

## Generation notes

The first generated attempt was rejected before import because it read as a large curved platform/ring sector. The accepted retry explicitly constrained the asset to a palm-sized loose fragment with no internal floor, wall course, concentric line, or neighboring masonry.

## Visual QA

- [x] One physical object only
- [x] One connected silhouette
- [x] True top-down projection
- [x] Flat tabletop-cardboard construction
- [x] Clearly distinct silhouette from chunk A
- [x] No detached crumbs or neighboring blocks
- [x] No platform, base, labels, grid, pivot mark, or baked shadow
- [x] Generous source padding; no clipping
- [x] User visual approval

## Prepared runtime source

- Alpha: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_b_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_b_v1.json`
- Tight rect: `541 × 612 px`
- Alpha-weighted center-of-mass pivot: `[268, 277] px`
- Runtime scale relative to base footprint: `0.115`
- Composed size: `124 × 140 px`
- Alpha PNG: `681,030 bytes` — PASS under `5 MB`
- Visible magenta spill: `0` pixels
- Draw order: `61`
- Shared by: Watchtower, Ranger, Tracker, Assassin

## Destruction defaults

- Mass class: `medium_small`
- Radial velocity: `110–195 px/s`
- Angular velocity: `−280…280°/s`
- Linear drag: `0.915`
- Lifetime: `650–1050 ms`

## Pair QA

- Chunk A game size: `151 × 81 px`
- Chunk B game size: `124 × 140 px`
- Silhouettes remain clearly distinguishable: PASS
- Both pivots remain inside dominant material: PASS
- Both pieces read at the same physical stone/cardboard scale: PASS
- Separate QA image: `assets/staging/reviews/modules/fortress_ranged/fortress_ranged__stone_rim_chunks_a_b_v1_review.png`

## Gate after approval

After confirmation of the A/B runtime pair, lock both modules in the shared destruction kit and generate the next individually addressable debris element. Runtime atlas packing remains deferred until the whole Watchtower family passes its object-level visual and technical gates.

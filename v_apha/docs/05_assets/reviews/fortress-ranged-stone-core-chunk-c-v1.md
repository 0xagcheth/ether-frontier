# Fortress Ranged — Stone Core Chunk C v1

Status: **canon module — A/B/C runtime kit awaiting confirmation**

## Asset

- ID: `fortress_ranged__debris__stone_core_chunk_c_v1`
- Family: `fortress_ranged`
- Role: independently animated inner-surface destruction debris
- Source: built-in ImageGen
- Candidate: `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__debris__stone_core_chunk_c_v1_chroma.png`
- Source canvas: `1254 × 1254 px`
- Source size: approximately `1.2 MB`

## Modular distinction

- Chunk A: wide curved outer-rim brick.
- Chunk B: compact near-square rim/corner fragment with a bite-shaped notch.
- Chunk C: irregular inner-stone shard with no curved rim edge or circular geometry.

This gives the destruction animation three independently addressable silhouette classes rather than rotated copies of one part.

## Generation record

- Mode: built-in ImageGen
- Final prompt summary: exactly one loose inner-stone chip; strict 90-degree top-down orthographic view; irregular triangular/pentagonal silhouette; jagged edges and one blunt corner; flat blue-grey printed stone cardboard with dark ink and a tan corrugated cut edge; uniform `#ff00ff`; no rim arc, platform, adjacent masonry, detached crumbs, shadows, labels, perspective, or 3D.

## Visual QA

- [x] Exactly one physical object
- [x] One connected silhouette
- [x] True top-down orthographic projection
- [x] Flat tabletop-cardboard construction
- [x] No curved outer-rim edge
- [x] Distinct from chunks A and B
- [x] No detached crumbs, neighbors, platform, or base
- [x] No labels, grid, pivot, shadow, perspective, or clipping
- [x] User visual approval

## Prepared runtime source

- Alpha: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__debris__stone_core_chunk_c_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__debris__stone_core_chunk_c_v1.json`
- Tight rect: `535 × 622 px`
- Alpha-weighted center-of-mass pivot: `[259, 316] px`
- Runtime scale relative to base footprint: `0.095`
- Composed size: `103 × 120 px`
- Alpha PNG: `595,574 bytes` — PASS under `5 MB`
- Visible magenta spill: `0` pixels
- Draw order: `62`
- Shared by: Watchtower, Ranger, Tracker, Assassin

## Destruction defaults

- Mass class: `small`
- Radial velocity: `135–225 px/s`
- Angular velocity: `−340…340°/s`
- Linear drag: `0.9`
- Lifetime: `550–950 ms`

## A/B/C kit QA

- A: `151 × 81 px` — wide curved rim brick
- B: `124 × 140 px` — compact notched corner fragment
- C: `103 × 120 px` — smaller inner-surface shard
- Distinct silhouettes: PASS
- Descending physical mass and increasing motion response: PASS
- Pivots inside dominant material: PASS
- Shared stone/cardboard scale: PASS
- Review: `assets/staging/reviews/modules/fortress_ranged/fortress_ranged__stone_debris_a_b_c_v1_review.png`

## Gate after approval

After confirmation, lock the three stone modules in the shared fortress-ranged destruction kit. The next required destruction layer should add a different material/animation role rather than another large stone duplicate. Runtime atlas packing remains deferred until the complete Watchtower family is validated.

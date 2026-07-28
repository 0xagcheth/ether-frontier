# Watchtower — Stone Dust Burst v1

Status: **canon one-shot animation — assembled preview awaiting confirmation**

## Asset

- ID: `watchtower__destroy_fx__stone_dust_burst_v1`
- Family: `fortress_ranged`
- Owner: `watchtower`
- Role: one-shot destruction child effect
- Source: built-in ImageGen, one request for the complete animation
- Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__destroy_fx__stone_dust_burst_v1_source_chroma.png`
- Layout: `2 × 2`, four frames in reading order
- Source canvas: `1254 × 1254 px`
- Source size: approximately `1.2 MB`

## Frame progression

1. Compact dense paper dust rosette.
2. Wider broken ring with large rounded lobes.
3. Larger and thinner fragmented ring.
4. Widest faint ring reduced to small isolated paper wisps.

## Generation record

- Mode: built-in ImageGen
- Final prompt summary: exactly four isolated top-down frames on one unlabeled 2×2 sheet; centered expanding stone-dust burst made from flat beige-grey paper/cardboard cloud pieces; uniform `#ff00ff`; no realistic translucent smoke, shadows, grid, labels, debris, perspective, or 3D.

## Visual QA

- [x] Exactly four animation groups
- [x] Correct 2×2 reading order
- [x] Stable effect center
- [x] Clear expansion and dissipation progression
- [x] Flat paper/cardboard tabletop construction
- [x] True top-down presentation
- [x] Wide chroma separation between slots
- [x] No labels, grid, pivot, solid debris, scenery, or clipping
- [x] User visual approval

## Runtime package

- Manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__destroy_fx__stone_dust_burst_v1.json`
- Frames: `watchtower__destroy_fx__stone_dust_burst__frame_01..04_v1_alpha.png`
- Shared frame canvas: `627 × 627 px`
- Shared center pivot: `[313, 313] px`
- Attachment: base `objectCenter`
- Runtime scale: `0.76` of base footprint
- Draw order: `70`
- Timing: `85 / 105 / 125 / 175 ms`
- Total one-shot duration: `490 ms`
- Loop: `false`; hold last: `false`
- Total frame size: `1,316,958 bytes` — PASS under `5 MB`
- Visible magenta spill: `0` pixels

## Normalized QA

- Shared center remains stable through all frames: PASS
- Content expands through frame 3 and visibly dissipates in frame 4: PASS
- Runtime frames contain no review labels, grid, or pivot crosses: PASS
- Separate QA grid: `assets/staging/reviews/modules/fortress_ranged/watchtower__stone_dust_burst_v1_review_grid.png`
- Assembled preview: `assets/staging/reviews/modules/fortress_ranged/watchtower__stone_dust_burst_v1_destroy_preview.gif`

The assembled preview composes the intact Watchtower, the four dust frames, shared stone debris A/B/C, wooden crossbow shard D, and metal axle bracket E. All marks and checkerboard presentation remain review-only.

## Gate after approval

After confirmation of the assembled destruction preview, lock the dust sequence. Then determine whether the Watchtower requires a separate spark one-shot or whether the current dust + solid debris package is sufficient before final family atlas packing.

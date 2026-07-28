# Watchtower — Metal Spark Burst v1

Status: **canon one-shot animation — final destroy preview awaiting confirmation**

## Asset

- ID: `watchtower__destroy_fx__metal_spark_burst_v1`
- Family: `fortress_ranged`
- Owner: `watchtower`
- Role: one-shot child effect for crossbow axle failure
- Source: built-in ImageGen, one request for the complete animation
- Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__destroy_fx__metal_spark_burst_v1_source_chroma.png`
- Layout: `2 × 2`, four frames in reading order
- Source canvas: `1254 × 1254 px`
- Source size: approximately `1.0 MB`

## Frame progression

1. Compact cluster of short golden paper rays.
2. Larger burst of long separated rays.
3. Expanded shorter amber fragments plus round flecks.
4. Four distant dark-amber remnants.

## Generation record

- Mode: built-in ImageGen
- Final prompt summary: four isolated top-down spark states on one unlabeled 2×2 sheet; flat die-cut golden, amber, and orange paper slivers radiating around a stable empty center; uniform `#ff00ff`; no glow bloom, realistic light, smoke, dust, hardware, shadows, grid, labels, perspective, or 3D.

## Visual QA

- [x] Exactly four animation groups
- [x] Correct 2×2 reading order
- [x] Stable empty effect center
- [x] Clear outward travel and dissipation
- [x] Flat paper/cardboard tabletop construction
- [x] No glow bloom or realistic light
- [x] Wide chroma separation between slots
- [x] No labels, grid, pivot, solid debris, scenery, or clipping
- [x] User visual approval

## Runtime package

- Manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__destroy_fx__metal_spark_burst_v1.json`
- Frames: `watchtower__destroy_fx__metal_spark_burst__frame_01..04_v1_alpha.png`
- Shared frame canvas: `627 × 627 px`
- Shared center pivot: `[313, 313] px`
- Attachment: canonical crossbow pivot
- Runtime scale: `0.34` of crossbow length
- Draw order: `71`
- Timing: `55 / 65 / 75 / 95 ms`
- Total one-shot duration: `290 ms`
- Loop: `false`; hold last: `false`
- Total frame size: `1,086,692 bytes` — PASS under `5 MB`
- Visible magenta spill: `0` pixels

## Normalized QA

- Stable empty center: PASS
- Outward travel and reduction from frames 1–4: PASS
- Paper rays remain readable without baked glow: PASS
- Runtime frames contain no review labels, grid, or pivot crosses: PASS
- Separate QA grid: `assets/staging/reviews/modules/fortress_ranged/watchtower__metal_spark_burst_v1_review_grid.png`
- Final assembled destroy preview: `assets/staging/reviews/modules/fortress_ranged/watchtower__destroy_v1_final_preview.gif`

The final preview composes the intact Watchtower, stone dust, metal sparks, stone debris A/B/C, wooden shard D, and metal bracket E as separately addressable layers.

## Gate after approval

After confirmation of the final destroy preview, freeze the Watchtower animation inventory and pack the complete family into a compact transparent runtime atlas using manifest content rects only.

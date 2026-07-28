# Tracker targeting rune loop v1 — review

Date: 2026-07-22

## Source and runtime files

- Source sheet: `assets/staging/candidates/modules/tracker/tracker__targeting_fx__rune_loop_v1_source_chroma.png`
- Manifest: `assets/approved/canon/modules/tracker/tracker__targeting_fx__rune_loop_v1.json`
- Runtime frames: `tracker__targeting_fx__rune_loop_v1__frame_01..04.png`
- Review grid: `assets/staging/reviews/modules/tracker/tracker__targeting_fx__rune_loop_v1_review_grid.png`
- Weapon preview: `assets/staging/reviews/modules/tracker/tracker__targeting_fx__rune_loop_v1_weapon_preview.gif`

## Animation contract

- Four independently addressable tight alpha sprites.
- Runtime order is explicitly remapped from ImageGen quadrants: `TL → TR → BR(lock) → BL(fade)`.
- Durations: `180 / 180 / 240 / 220 ms`; total `820 ms`; looped.
- Shared source footprint: `627 × 627 px`.
- Shared pivot in source: `[313, 313]`.
- Runtime diameter: `0.34` of the inherited base footprint.
- Attachment: Tracker crossbow `scan_ring_socket`.
- Layer order: weapon `30`, targeting rune `31`, metal scan ring `32`.

## QA

- Exact top-down flat paper/cardboard construction: pass.
- Stable outer footprint and open center: pass.
- Four isolated quadrants: pass.
- Clipping: none.
- Magenta spill by frame: `0 / 0 / 0 / 0 px`.
- Metal scan ring remains readable above the rune: pass after draw-order correction.
- Labels, review grid, and assembled GIF remain outside runtime assets.

## Gate

Tracker's unique module inventory is complete after visual confirmation of this loop. The next step is one compact Tracker family atlas, schema-v2 manifest, separate layer grid, composite/animation preview, and full technical audit.

# Ranger layered runtime v2 — final candidate

Date: 2026-07-22

## Result

- Runtime atlas: `assets/approved/runtime/ranger/ranger_layered_runtime_v2.png`
- Source-of-truth manifest: `assets/approved/runtime/ranger/ranger_layered_manifest_v2.json`
- Human QA grid: `assets/staging/reviews/ranger/ranger_layered_review_grid_v2.png`
- Assembled preview: `assets/staging/reviews/ranger/ranger_layered_composite_preview_v2.png`
- Reproducible packer: `scripts/pack_ranger_layered_runtime_v2.py`

## Runtime contract

- One `fortress_ranged / ranger` family per transparent atlas.
- Strict `true_top_down_orthographic_90deg` projection.
- Stable inherited `512 px` round fortress footprint.
- Crossbow, magazine, optics, arrow rack, Ranger trim, lantern, projectile, attack FX, impact FX, destruction debris, dust, and sparks remain independently addressable layers.
- Crossbow, magazine, and optics inherit the aim rotation as a hierarchy.
- Labels, checker grid, pivot crosses, and assembled preview are excluded from the runtime image.

## Technical audit

- Atlas dimensions: `1024 × 1024 px`.
- Runtime atlas size: `992,457 bytes` (`< 5 MB`).
- Sprite count: `32`.
- Rectangles in bounds: pass.
- Rectangle overlaps: `0`.
- Remaining magenta spill: `0 px`.
- Runtime labels: none.
- Attachments: `9` named sockets/anchors.
- Animation clips: lantern idle, rapid attack, barbed impact, destroy dust, destroy sparks.

## Validation state

Technical and internal visual validation pass. User confirmation was received on 2026-07-22; runtime status is `approved`, and Tracker production may proceed.

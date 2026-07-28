# Tracker layered runtime v2 — final candidate

Date: 2026-07-22

## Deliverables

- Runtime atlas: `assets/approved/runtime/tracker/tracker_layered_runtime_v2.png`
- Source-of-truth manifest: `assets/approved/runtime/tracker/tracker_layered_manifest_v2.json`
- Human QA grid: `assets/staging/reviews/tracker/tracker_layered_review_grid_v2.png`
- Assembled preview: `assets/staging/reviews/tracker/tracker_layered_composite_preview_v2.png`
- Reproducible packer: `scripts/pack_tracker_layered_runtime_v2.py`

## Runtime assembly

- Shared fortress base, center socket, lantern loop, stone debris, dust and sparks are inherited.
- Ranger bolt magazine, barbed bolt, rapid flash and barbed impact are reused as documented family descendants.
- Tracker owns the long-range crossbow, scan optics ring, crown trim and four-frame targeting rune.
- Weapon rotates around its corrected mechanical-bearing pivot.
- Magazine inherits weapon rotation with local `90°` transform.
- Targeting rune inherits aim rotation; metal scan ring adds independent `scanAngle` rotation.
- Crown and lantern remain static base children.

## Technical audit

- Atlas: `1024 × 1024 px`, transparent RGBA.
- Atlas size: `1,033,305 bytes`, below `5 MB`.
- Sprite count: `35`.
- All rects in bounds: pass.
- Rectangle overlaps: `0`.
- Remaining magenta spill: `0 px`.
- Chroma-edge pixels removed during packing: `705`.
- Runtime labels/grid/pivot crosses/assembled frames: absent.
- Base footprint: stable `512 px`.
- Named attachments: `8`.
- Animation clips: lantern idle, targeting scan, attack, impact, destruction dust and sparks.

## Validation state

Internal visual and technical validation pass. User confirmation was received on 2026-07-22; runtime status is `approved`. Live-lab integration is authorized before beginning Assassin.

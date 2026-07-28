# Ranger arrow rack v1

Status: **canon — visual and technical gates passed**

## Identity

- ID: `ranger__utility_child__arrow_rack_v1`
- Owner: `ranger`
- Family: `fortress_ranged`
- Slot: `utility_child`
- Runtime role: static replaceable child near the inherited platform rim
- Candidate: `assets/staging/candidates/modules/ranger/ranger__utility_child__arrow_rack_v1_chroma.png`

## Modular contract

Included:

- one shallow crescent-shaped wooden holder;
- five separate empty storage notches;
- two iron fastening plates at its ends;
- physical die-cut cardboard construction.

Excluded:

- arrows, bolts, projectile, ammunition bundle;
- crossbow, magazine, base, optics, trim, lantern and flag;
- labels, grid, pivot marker, shadow, perspective and 3D render.

## Visual QA

- [x] Exactly one connected isolated component
- [x] Strict top-down orthographic projection
- [x] Empty rack; ammunition remains independent
- [x] Five readable slots
- [x] Cardboard edge and printed material treatment
- [x] Generous chroma margin and no clipping

## Generation

- Mode: built-in ImageGen
- Canvas: `1254 × 1254 px`
- Prompt intent: one empty low-profile crescent rack for the outer fortress-platform edge, no arrows or parent layers.

## Technical result

- Alpha: `assets/approved/canon/modules/ranger/ranger__utility_child__arrow_rack_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/ranger/ranger__utility_child__arrow_rack_v1.json`
- Tight rect: `948 × 409 px`
- Pivot: `[474, 204] px`
- Runtime scale: `0.19` of inherited base footprint
- Static position: `[0.5, 0.12]` on the northern inner rim
- Draw order: `15`; does not inherit weapon rotation
- Weapon overlap at `0 / 90 / 180 / 270°`: `0 / 0 / 0 / 0 px`
- Visible magenta spill: `0 px`
- Alpha size: `614,630 bytes` — under `5 MB`
- Clearance grid: `assets/staging/reviews/modules/ranger/ranger__utility_child__arrow_rack_v1_platform_clearance_grid.png`

## Gate

Arrow rack promoted to canon after the original lower placement failed clearance and the corrected rim placement passed all four angles.

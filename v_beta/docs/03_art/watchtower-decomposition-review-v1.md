# Watchtower Decomposition Review v1

Updated: 2026-07-24

Status: **REJECTED**

Rejection reason: six independently centered generations were scaled and placed
approximately during compositing. Their attachment geometry does not reproduce
the approved projection master, and the set does not contain all animation,
projectile, impact and destruction children required by the object contract.

## Approved input

`watchtower_projection_master_v3` is the approved projection master.

## Independent ImageGen 2 sources

1. `watchtower_base_body_v1`
2. `watchtower_bearing_v1`
3. `watchtower_crossbow_v1`
4. `watchtower_signal_cloth_v1`
5. `watchtower_lantern_casing_v1`
6. `watchtower_bolt_reserve_v1`

Each module exists as its own chroma source and alpha-cleaned file. The modules
were not generated as cells on one shared sheet.

## Review artifacts

- Composite:
  `assets/staging/candidates/watchtower/watchtower_decomposition_composite_v1.png`
- Separate human-QA grid:
  `assets/staging/candidates/watchtower/watchtower_decomposition_review_grid_v1.jpg`

The QA grid is not a runtime asset.

## Elements that remain useful as visual references only

- stable true top-down base footprint;
- exactly two access notches;
- independent cardboard contours and attachment shadows;
- lore-specific archive, repair and inventory print language;
- bearing, weapon, cloth, lantern casing and bolt reserve establish material
  directions, but their v1 raster geometry is not runtime-approved;
- no labels, grid or pivots are baked into layer alpha files.

## Required replacement

- regenerate every child on a common 1254 × 1254 coordinate canvas inherited
  from the approved projection master;
- preserve the exact position, scale, orientation and attachment point while
  erasing unrelated components;
- complete the full layer inventory defined in
  `watchtower-layer-contract-v2.md`;
- create the composite by direct 1:1 alpha compositing without manual scaling.

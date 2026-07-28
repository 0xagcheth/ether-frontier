# Ranger — Rapid Crossbow v1

Status: **canon — visual and technical gates passed**

## Asset

- ID: `ranger__active_primary__rapid_crossbow_v1`
- Family: `fortress_ranged`
- Owner: `ranger`
- Role: independently rotatable primary weapon
- Forward axis: `+X`
- Source: built-in ImageGen
- Candidate: `assets/staging/candidates/modules/ranger/ranger__active_primary__rapid_crossbow_v1_chroma.png`
- Source canvas: `1254 × 1254 px`
- Source size: approximately `1.4 MB`

## Modular contract

Included in this layer:

- compact wooden rapid-crossbow chassis;
- broad shallow recurved limbs and string;
- central dark iron rotation hub;
- right-facing twin-groove launch rail.

Explicitly excluded for separate child modules:

- bolt magazine;
- bolts and Ranger projectile;
- arrow rack;
- hunting optics;
- Ranger trim;
- base, socket, lantern, flag, and effects.

## Generation record

- Mode: built-in ImageGen
- Two earlier built-in requests failed with backend network errors and produced no files.
- Successful prompt summary: exactly one compact rapid crossbow, strict direct-overhead orthographic view, horizontal +X orientation, short wooden stock, broad limbs, central iron hub and twin rail, flat die-cut cardboard with tan edge on uniform `#ff00ff`; no magazine, optics, arrows, rack, trim, base, labels, perspective, or 3D.

## Visual QA

- [x] Exactly one connected physical module
- [x] True top-down orthographic projection
- [x] Flat tabletop-cardboard construction
- [x] Central rotation hub is visible and unobstructed
- [x] Right-facing muzzle rail is available for attachments
- [x] No magazine, optics, projectile, rack, or trim baked in
- [x] Distinct silhouette from Watchtower single crossbow
- [x] No shadow, labels, grid, pivot marker, perspective, or clipping
- [x] User visual approval

## Technical result

- Alpha: `assets/approved/canon/modules/ranger/ranger__active_primary__rapid_crossbow_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/ranger/ranger__active_primary__rapid_crossbow_v1.json`
- Tight rect: `931 × 844 px`
- Axle pivot: `[462, 431] px`
- Muzzle attachment: `[930, 431] px`, local `+X`
- Runtime scale to inherited base footprint: `0.66`
- Rotation envelope: `362 px`; inherited base radius: `541 px` — PASS
- Visible magenta spill: `0 px`
- Alpha size: `1,102,178 bytes` — under `5 MB`
- Four-angle rotation review: `assets/staging/reviews/modules/ranger/ranger__active_primary__rapid_crossbow_v1_rotation_review_grid.png`
- Inherited-core composite: `assets/staging/reviews/modules/ranger/ranger__active_primary__rapid_crossbow_v1_inherited_core_composite.png`

## Gate

Primary module promoted to canon. Next isolated child: `ranger__ammo_child__bolt_magazine_v1`.

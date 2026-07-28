# Ranger bolt magazine v1

Status: **canon — visual and technical gates passed**

## Identity

- ID: `ranger__ammo_child__bolt_magazine_v1`
- Owner: `ranger`
- Family: `fortress_ranged`
- Slot: `ammo_child`
- Runtime role: separate child attached to `rapid_crossbow.magazine_socket`; inherits weapon rotation
- Candidate: `assets/staging/candidates/modules/ranger/ranger__ammo_child__bolt_magazine_v1_chroma.png`

## Included

- One closed shallow horizontal cartridge cassette
- Central circular axle-lock opening
- Two short symmetric fastening tabs
- Printed dark blue-grey casing with warm wood inserts
- Thick ink outline and exposed tan cardboard cut edge

## Explicitly excluded

- Rapid crossbow and base
- Visible bolts, arrows, projectile or loose ammunition
- Optics, rack, trim, lantern and flag
- Labels, grid, pivot marker, shadow, perspective and 3D render

## Visual QA

- [x] Exactly one connected object
- [x] Strict top-down orthographic presentation
- [x] Separate physical cardboard construction
- [x] Central mounting opening remains readable
- [x] Symmetric attachment silhouette
- [x] Uniform removable magenta field and generous padding
- [x] No clipping or forbidden parent modules

## Generation

- Mode: built-in ImageGen
- Canvas: `1254 × 1254 px`
- Prompt intent: one independent closed rapid-crossbow magazine cassette, exact overhead cardboard tabletop token, centered mount aperture, no ammunition or parent layers.

## Technical result

- Alpha: `assets/approved/canon/modules/ranger/ranger__ammo_child__bolt_magazine_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/ranger/ranger__ammo_child__bolt_magazine_v1.json`
- Tight rect: `1059 × 466 px`
- Pivot: `[529, 233] px`; transparent center opening preserved
- Runtime width: `0.18` of parent weapon
- Attachment: `rapid_crossbow.magazine_socket` at local `x=0.66`
- Local rotation: `90°`; inherits parent rotation
- Draw order: `31`, above weapon rail
- Visible magenta spill: `0 px`
- Alpha size: `1,082,119 bytes` — under `5 MB`
- Assembly grid: `assets/staging/reviews/modules/ranger/ranger__ammo_child__bolt_magazine_v1_assembly_rotation_grid.png`

## Gate

Magazine promoted to canon after assembled four-angle validation. Next isolated child: `ranger__utility_child__arrow_rack_v1`.

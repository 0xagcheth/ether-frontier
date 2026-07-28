# Ranger hunting optics v1

Status: **canon — visual and technical gates passed**

## Identity

- ID: `ranger__aim_child__hunting_optics_v1`
- Owner: `ranger`
- Family: `fortress_ranged`
- Slot: `aim_child`
- Runtime role: independently replaceable sight attached to `rapid_crossbow.optics_socket`; inherits weapon rotation
- Candidate: `assets/staging/candidates/modules/ranger/ranger__aim_child__hunting_optics_v1_chroma.png`
- Forward axis: local `+X`

## Modular contract

Included:

- one short low-profile sight rail;
- one round amber paper lens housing near the forward end;
- two mounting clamps and one brass adjustment wheel;
- physical die-cut cardboard construction.

Excluded:

- crossbow, magazine, rack, arrows, bolts and projectile;
- base, tower, trim, lantern and flag;
- detached lens, glow, labels, grid, pivot marker, shadow, perspective and 3D render.

## Visual QA

- [x] Exactly one connected isolated component
- [x] Strict top-down orthographic projection
- [x] Horizontal local `+X` orientation
- [x] Low flat sight rather than side-view telescope
- [x] Lens is a printed paper insert with no glow bloom
- [x] Separate cardboard edge and generous chroma padding
- [x] No clipping or parent layers

## Generation

- Mode: built-in ImageGen
- Canvas: `1254 × 1254 px`
- Prompt intent: one compact flat hunting sight module with amber lens, clamps and adjustment wheel, no weapon or other Ranger parts.

## Technical result

- Alpha: `assets/approved/canon/modules/ranger/ranger__aim_child__hunting_optics_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/ranger/ranger__aim_child__hunting_optics_v1.json`
- Tight rect: `918 × 393 px`
- Pivot: `[459, 196] px`
- Runtime width: `0.27` of parent weapon
- Attachment: `rapid_crossbow.optics_socket`; inherits parent rotation
- Draw order: `32`, above weapon and magazine
- Visible magenta spill: `0 px`
- Alpha size: `610,945 bytes` — under `5 MB`
- Assembly grid: `assets/staging/reviews/modules/ranger/ranger__aim_child__hunting_optics_v1_weapon_rotation_grid.png`

## Gate

Optics promoted to canon after four-angle assembled validation. Muzzle, axle pivot, magazine, limbs, and string remain readable.

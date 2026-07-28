# Watchtower — Crossbow Axle Bracket E v1

Status: **canon module — axle-relative scale awaiting confirmation**

## Asset

- ID: `watchtower__debris__crossbow_axle_bracket_e_v1`
- Family: `fortress_ranged`
- Owner: `watchtower`
- Role: independently animated small metal weapon debris
- Source: built-in ImageGen
- Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__debris__crossbow_axle_bracket_e_v1_chroma.png`
- Source canvas: `1254 × 1254 px`
- Source size: approximately `1.2 MB`

## Modular role

The bracket separates from the crossbow axle independently of the wooden arm shard D. It adds a small, fast-spinning metal mass without duplicating the shared stone pieces or the large wooden fragment.

## Generation record

- Mode: built-in ImageGen
- Final prompt summary: exactly one compact asymmetrical C-shaped broken axle collar, strict 90-degree top-down orthographic view, open inner cutout, two integrated rivets and one fractured side, flat dark iron-grey printed cardboard with tan corrugated edges, uniform `#ff00ff`; no complete ring, gear, crossbow, second piece, shadows, labels, perspective, or 3D.

## Visual QA

- [x] Exactly one connected physical object
- [x] True top-down orthographic projection
- [x] Flat tabletop-cardboard construction
- [x] Inner opening remains open to chroma
- [x] Two rivets are integrated, not detached sprites
- [x] Broken C-shaped silhouette differs from a complete washer or gear
- [x] Metal material differs from stone and wood debris
- [x] No labels, grid, pivot, shadow, perspective, or clipping
- [x] User visual approval

## Prepared runtime source

- Alpha: `assets/approved/canon/modules/fortress_ranged/watchtower__debris__crossbow_axle_bracket_e_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__debris__crossbow_axle_bracket_e_v1.json`
- Tight rect: `495 × 606 px`
- Alpha-weighted material pivot: `[231, 302] px`
- Center cutout alpha: `0` — PASS
- Scale relative to canonical crossbow length: `0.14`
- Runtime size: `109 × 133 px`
- Canonical crossbow runtime size: `779 × 530 px`
- Alpha PNG: `556,461 bytes` — PASS under `5 MB`
- Visible magenta spill: `0` pixels
- Draw order: `65`

## Destruction defaults

- Mass class: `light_metal`
- Inherits owner rotation at detachment: yes
- Radial velocity: `175–285 px/s`
- Angular velocity: `−560…560°/s`
- Linear drag: `0.875`
- Lifetime: `450–850 ms`

## Axle-relative QA

- Hardware is visibly smaller than the complete crossbow: PASS
- Scale remains readable beside the central axle: PASS
- Open center survives alpha conversion and runtime scaling: PASS
- Pivot is calculated from visible metal and excludes the cutout: PASS
- Review: `assets/staging/reviews/modules/fortress_ranged/watchtower__crossbow_axle_bracket_e_v1_review.png`

## Gate after approval

After confirmation, lock E beside wooden shard D in the Watchtower-owned destruction kit. The next required layer should be a short-lived destruction effect (dust/sparks) rather than another persistent solid fragment.

# Watchtower — Crossbow Arm Shard D v1

Status: **canon module — weapon-relative scale awaiting confirmation**

## Asset

- ID: `watchtower__debris__crossbow_arm_shard_d_v1`
- Family: `fortress_ranged`
- Owner: `watchtower`
- Role: independently animated weapon debris during destruction
- Source: built-in ImageGen
- Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__debris__crossbow_arm_shard_d_v1_chroma.png`
- Source canvas: `1254 × 1254 px`
- Source size: approximately `1.2 MB`

## Modular role

This is not another stone-base fragment. It belongs to the Watchtower-specific crossbow layer and lets the weapon break away independently while the shared fortress-ranged stone kit uses chunks A/B/C.

## Generation record

- Mode: built-in ImageGen
- Final prompt summary: exactly one short curved wooden crossbow-limb fragment, strict 90-degree top-down orthographic view, integrated dark metal end binding and one splintered break, flat brown printed wood cardboard with dark ink and tan corrugated edge, uniform `#ff00ff`; no string, complete crossbow, second fragment, shadow, labels, perspective, or 3D.

## Visual QA

- [x] Exactly one connected physical object
- [x] True top-down orthographic projection
- [x] Flat tabletop-cardboard construction
- [x] Wood material clearly distinct from stone debris
- [x] Manufactured bound end and broken splintered end readable
- [x] No string, bolt, full crossbow, or detached splinters
- [x] No platform, labels, grid, pivot, shadow, perspective, or clipping
- [x] User visual approval

## Prepared runtime source

- Alpha: `assets/approved/canon/modules/fortress_ranged/watchtower__debris__crossbow_arm_shard_d_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__debris__crossbow_arm_shard_d_v1.json`
- Tight rect: `845 × 314 px`
- Alpha-weighted center-of-mass pivot: `[424, 167] px`
- Scale relative to canonical crossbow length: `0.36`
- Runtime size: `280 × 104 px`
- Canonical crossbow runtime size: `779 × 530 px`
- Alpha PNG: `516,556 bytes` — PASS under `5 MB`
- Visible magenta spill: `0` pixels
- Draw order: `64`

## Destruction defaults

- Mass class: `light_wood`
- Inherits owner rotation at detachment: yes
- Radial velocity: `155–255 px/s`
- Angular velocity: `−420…420°/s`
- Linear drag: `0.885`
- Lifetime: `500–900 ms`

## Weapon-relative QA

- Fragment reads as a broken limb segment rather than a complete weapon: PASS
- Width is proportionate to one crossbow arm section: PASS
- Material and line weight match the canonical crossbow family: PASS
- Center-of-mass pivot remains inside the wooden face: PASS
- Review: `assets/staging/reviews/modules/fortress_ranged/watchtower__crossbow_arm_shard_d_v1_review.png`

## Gate after approval

After confirmation, lock the module in the Watchtower-owned destruction kit. The next destruction layer should represent a small secondary hardware fragment or a short-lived effect, not another large wooden duplicate.

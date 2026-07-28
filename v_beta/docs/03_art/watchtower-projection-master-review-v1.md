# Watchtower Projection Master Review v1

Updated: 2026-07-23

Status: **REJECTED**

Rejection reason: the assembled object reads as one continuous illustration.
The solid-cardboard substrate, independent die-cut contours, physical gaps and
contact shadows between child elements are not strong enough.

## Files

- ImageGen 2 chroma source:
  `assets/source/watchtower/watchtower_projection_master_v1_chroma.png`
- Alpha review master:
  `assets/staging/candidates/watchtower/watchtower_projection_master_v1_alpha.png`

The assembled image is a projection and construction master only. It must never
be shipped as a baked runtime sprite.

## Visual review

| Requirement | Result | Note |
|---|---|---|
| One Watchtower only | PASS | No unrelated object family is present |
| True top-down orthographic view | PASS | Roof/deck footprint is read from 90 degrees |
| No facade, side or rear view | PASS | No vertical elevation presentation |
| Circular stone lookout | PASS | Stable circular stone footprint |
| Exactly two opposite access notches | PASS | Clear opposing breaks in the ring |
| Central rotation bearing | PASS | Weapon rotation point is readable |
| One lightweight crossbow | PASS | Correct Watchtower-specific weapon |
| Weapon subordinate to tower | PASS | Near the upper acceptable visual-weight limit |
| Separate signal cloth | PASS | Burgundy cloth can become a child layer |
| Lantern and glow anchor | PASS | Amber lantern has a distinct attachment area |
| Bolt reserve | PASS | Ammunition language matches the crossbow |
| No character baked into object | PASS | Tower remains modular |
| Cardboard punchboard construction | PASS | Cut edges, printed fibers and layer shadows read clearly |
| Child-layer separation potential | PASS | Body, bearing, crossbow, cloth, lantern and bolts are distinguishable |
| Sparse ornament | PASS | Surface remains functional rather than decorative |
| No clipping | PASS | Entire object and shadow envelope fit inside the source |

## Technical review

- Source mode: RGB
- Alpha mode: RGBA
- Dimensions: 1254 × 1254 px
- Chroma source size: 2,371,197 bytes
- Alpha master size: 2,161,255 bytes
- Alpha bounding box: `(73, 75, 1181, 1166)`
- Transparent pixels: 650,682 of 1,572,516
- Partially transparent edge pixels: 4,486
- Corner alpha: fully transparent

## Constraints for decomposition

- Do not enlarge the crossbow.
- Simplify incidental micro-scratches when generating isolated child layers.
- Preserve the base footprint across all animation states.
- Generate body, bearing, crossbow, cloth, lantern/glow and bolt reserve as
  separately named cardboard pieces.
- Derive pivots and attachments from the approved assembled master.

## Gate

Ready for user visual review. Decomposition remains blocked until approval.

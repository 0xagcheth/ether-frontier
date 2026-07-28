# Watchtower v3 — Warden's Post projection master

Date: 2026-07-22
Status: rejected — material rendering is too realistic and does not satisfy the cardboard punchboard style

## Files

- Chroma source: `assets/source/watchtower-v3/watchtower__projection_master__wardens_post_v3_chroma.png`
- Alpha review: `assets/source/watchtower-v3/watchtower__projection_master__wardens_post_v3_alpha.png`

## Description compliance

- Reads as a compact fortified Warden's Post rather than a generic weapon platform.
- Distinct stone parapet with varied blocks and two access notches.
- Wood working deck contains radial construction, hatches, hardware and rope equipment.
- One small central crossbow on a centered circular bearing; architecture remains dominant.
- Dedicated north-west red flag station and south-west top-view amber lantern station.
- Exact true top-down orthographic projection shared by every component.
- Matte printed cardboard/paper construction with visible tan cut edges.
- No Ranger/Tracker/Assassin/ballista/cannon/magic-family elements.

## Technical review

- Source size: `1254 × 1254 px`.
- Chroma subject bounds: `(82, 88)–(1172, 1152)`.
- Safe margins: left `82 px`, top `88 px`, right `82 px`, bottom `102 px`.
- Alpha visible bounds: `(84, 89)–(1170, 1150)`.
- Transparent corner alpha: `0 / 0 / 0 / 0`.
- Visible magenta spill after removal: `0 px`.
- Chroma source size: `2,617,925 bytes`.
- Alpha review size: `2,384,780 bytes`.
- Clipping: none.

## Layering note

The master shows a loaded bolt to communicate the crossbow, but production decomposition must keep the bolt as a separate projectile/ammunition layer. The rotatable crossbow layer must not permanently bake the projectile into its weapon texture.

## Gate

The spatial layout may inform the next textual specification, but this image must not be used as a visual style reference or decomposed into production layers. Generate a fresh master with simplified flat printed-paper shapes, coarse screen-print texture, thick illustrated outlines and obvious corrugated-cardboard edges.

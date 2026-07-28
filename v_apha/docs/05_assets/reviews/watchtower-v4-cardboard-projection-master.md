# Watchtower v4 — cardboard Warden's Post projection master

Date: 2026-07-22
Status: rejected — too simplified and too close to a flat punchboard token

## Files

- Chroma source: `assets/source/watchtower-v3/watchtower__projection_master__wardens_post_v4_cardboard_chroma.png`
- Alpha review: `assets/source/watchtower-v3/watchtower__projection_master__wardens_post_v4_cardboard_alpha.png`

## Visual contract

- Exact overhead / orthographic circular footprint; no facade, rear view or tall perspective.
- Reads as a printed punchboard token: broad flat shapes, thick ink outlines, coarse halftone and an obvious tan cardboard cut edge.
- Warden's Post architecture remains dominant: grey stone parapet, radial wooden working deck and two access breaks.
- One small simple Watchtower crossbow sits on the central bearing and occupies less than one third of the platform diameter.
- Red paper flag and amber lantern remain visually distinct child-layer stations.
- No borrowed Ranger, Tracker, Assassin, artillery or magic-family identity.

## Technical review

- Source size: `1254 × 1254 px`.
- Alpha visible bounds: `(112, 94)–(1156, 1141)`.
- Safe margins: left `112 px`, top `94 px`, right `98 px`, bottom `113 px`.
- Transparent corner alpha: `0 / 0 / 0 / 0`.
- Transparent pixels: `726925 / 1572516`.
- Partially transparent edge pixels: `4942 / 1572516`.
- Alpha review size: `2,466,505 bytes`.
- Clipping: none.

## Intended production layers after approval

1. `watchtower_base_body` — stable stone-and-deck footprint, without movable children.
2. `watchtower_weapon_socket` — centered bearing and registration anchor.
3. `watchtower_crossbow` — separately rotatable simple crossbow, without a baked projectile.
4. `watchtower_bolt` — unique projectile/ammunition sprite.
5. `watchtower_flag` — independently animated paper flag frames.
6. `watchtower_lantern` — independent lantern housing plus glow/flicker frames.
7. `watchtower_fire_fx`, `watchtower_impact_fx`, `watchtower_debris` — owner-specific animation elements where required by the gameplay description.

## Gate

Do not generate, extract or pack individual layers from this image. The replacement must use the user-supplied battlefield reference as its visual target: richer multi-piece construction, 2–4 stacked paper layers, visible cut edges, restrained contact shadows and more structural detail while remaining exact overhead and unmistakably cardboard.

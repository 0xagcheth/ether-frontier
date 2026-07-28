# Watchtower Layer Contract v2

Updated: 2026-07-24

Status: **SUPERSEDED by `watchtower-layer-contract-v3.md`**

Current projection reference awaiting approval:
`assets/staging/candidates/watchtower/watchtower_projection_master_v4_alpha.png`

The v3-derived layer attempts are superseded because the user changed the
primary-mechanism proportion and cartoon hierarchy. Decomposition restarts only
after v4 approval.

## Coordinate rule

Every structural source is generated on the same 1254 × 1254 canvas as the
approved master. ImageGen must erase unrelated elements without centering,
resizing, rotating or redesigning the retained element.

Tight cropping happens only after common-canvas alignment is validated. The
manifest restores tight sprites through pivots and attachment coordinates.

## Fixed structure

| Layer ID | Contents |
|---|---|
| `base_stone` | complete stone ring and two access notches |
| `fixed_deck` | radial timber deck and printed archive mark |
| `bearing` | central stacked rotation washers |
| `bolt_reserve_rack` | fixed rack without removable bolts |
| `reserve_bolt_01..04` | four separately addressable stored bolts |

## Moving and animated children

| Layer ID | Contents |
|---|---|
| `crossbow_body` | guide, trigger housing and rear cap |
| `crossbow_left_arm` | left bow arm |
| `crossbow_right_arm` | right bow arm |
| `crossbow_string_tense` | idle/aim string |
| `crossbow_string_release` | released string overlay |
| `crossbow_recoil` | short recoil overlay/offset contract |
| `loaded_bolt` | bolt visible before release |
| `projectile_bolt` | owner-specific flying bolt |
| `signal_cloth_01..04` | four flat-cardboard deformation states |
| `lantern_casing` | fixed casing without emitted light |
| `lantern_flame_01..04` | four paper-flame states |
| `lantern_glow_01..04` | four separate translucent glow states |
| `attack_flash_01..03` | three paper-flash states |

## Impact and destruction

| Layer ID | Contents |
|---|---|
| `impact_01..04` | non-looping paper splinter/stone-chip impact |
| `debris_stone_01..05` | independent ring fragments |
| `debris_deck_01..04` | independent deck fragments |
| `debris_crossbow_body` | broken guide/mechanism |
| `debris_crossbow_left_arm` | detached left arm |
| `debris_crossbow_right_arm` | detached right arm |
| `debris_signal_cloth` | detached cloth |
| `debris_lantern` | detached casing |
| `debris_bolt_01..04` | scattered reserve bolts |
| `destroy_dust_01..05` | cardboard dust settling sequence |

## Required anchors

- `object_center`
- `active_primary_pivot`
- `muzzle_anchor`
- `projectile_spawn`
- `flag_anchor`
- `lantern_anchor`
- `debris_origin_stone`
- `debris_origin_wood`

## Draw order

`base_stone` → `fixed_deck` → `bearing` → `bolt_reserve_rack` → reserve bolts →
crossbow body/arms → string/recoil → loaded bolt → signal cloth → lantern casing
→ flame → glow → attack FX.

## Composite acceptance

- built by 1:1 compositing only;
- no per-layer scale correction;
- no per-layer rotation correction;
- silhouette matches the approved master;
- attachment gaps are intentional and under two source pixels unless the master
  visibly defines a wider gap;
- all required elements appear in the inventory before atlas packing.

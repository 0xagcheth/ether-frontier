# Assassin module contract v1

Date: 2026-07-22
Family: `fortress_ranged`
Parent lineage: fortress core with selected Ranger-derived ammunition geometry

## Inheritance

Assassin reuses:

- fortress round base, center socket and stable footprint;
- amber lantern housing/glow unless hidden by the shrouded insert;
- shared stone debris, dust and restrained metal sparks;
- barbed-bolt scale/trajectory contract where compatible, with Assassin palette handled as a separate projectile layer if visual validation requires it.

## Assassin-owned modules

| Order | Slot | Module | Behavior |
|---|---|---|---|
| 1 | `active_primary` | `assassin__active_primary__sniper_crossbow_v1` | rotates around center; exact local `+X` muzzle |
| 2 | `chassis_static` | `assassin__chassis_static__shrouded_rim_insert_v1` | static flat base insert; never rotates with weapon |
| 3 | `charge_child` | `assassin__charge_child__critical_lens_v1` | separate lens attached to weapon; charge animation remains separate |
| 4 | `attack_charge` | `assassin__attack_fx__critical_charge_loop_v1` | animated child around lens/pivot |
| 5 | `attack_release` | `assassin__attack_fx__violet_amber_shot_v1` | compact restrained release; no large generic muzzle burst |

## Projection/material rules

- Exact `90°` top-down orthographic projection.
- Flat die-cut cardboard/paper tabletop construction with matte printed texture and tan cut edge.
- No side/facade/rear view, perspective, isometric tilt, tall construction, glossy 3D, cast shadow or floor plane.
- One named module per source, uniform `#ff00ff` chroma, generous padding, no labels/grid/pivot crosses/assembled previews.

## First gate

Generate only the standalone sniper crossbow. It must remain mechanically related to the fortress-ranged family while being slimmer and more severe than Tracker: narrow asymmetric precision limbs, long enclosed rail, centered bearing, compact dark shroud accents and exact `+X` muzzle. Exclude lens, charge, projectile, rim insert and FX.

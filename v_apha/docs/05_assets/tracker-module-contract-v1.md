# Tracker module contract v1

Date: 2026-07-22
Family: `fortress_ranged`
Parent variant: `ranger`

## Inheritance

Tracker reuses without redrawing:

- fortress round base and stable `512 px` footprint;
- center socket;
- amber lantern housing and four-frame glow loop;
- shared stone debris, dust, and sparks;
- Ranger bolt magazine;
- Ranger barbed-bolt projectile.

## Tracker-owned replacements

| Order | Semantic slot | Module | Runtime behavior |
|---|---|---|---|
| 1 | `active_primary` | `tracker__active_primary__long_range_crossbow_v1` | rotates around the inherited center socket; local forward axis `+X` |
| 2 | `aim_child` | `tracker__aim_child__scan_optics_ring_v1` | independent rotating/scanning child attached to the weapon |
| 3 | `identity_child` | `tracker__identity_child__crown_trim_v1` | static base child outside the weapon rotation envelope |
| 4 | `targeting_fx` | `tracker__targeting_fx__rune_loop_v1` | separate animated child; never baked into the base or weapon |

## Projection and material lock

- Exact `90°` top-down orthographic view.
- Every element is a flat die-cut cardboard/paper game piece with printed ink texture and visible tan cut edge.
- No façade, rear, side, elevated, isometric, glossy 3D, cast shadow, floor plane, label, grid, pivot mark, or assembled platform.
- Each source contains one named module only on uniform `#ff00ff` chroma.
- Stable weapon pivot remains centered and muzzle faces local `+X`.

## First generation gate

Generate only the long-range crossbow projection master. It should remain visibly related to Ranger's rapid crossbow through the central bearing and material language, while replacing the compact rapid-fire silhouette with longer narrow limbs, a longer rail, and a cleaner precision profile. Magazine, scan ring, rune, projectile, platform, effects, and extra variants are excluded.

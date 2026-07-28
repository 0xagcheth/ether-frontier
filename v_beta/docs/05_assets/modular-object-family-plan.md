# Ether Frontier — Modular Object Family Plan

Status: **legacy / partially superseded**. Its atlas schema, naming, and technical slots remain useful. All visible-body reuse and family-sharing decisions are superseded by `object-family-and-variation-spec-v4.md`.

## 1. Purpose

Define the modular visual construction of every tower and building before any further ImageGen work.

The production objective is not to generate 26 unrelated finished pictures. The objective is to build a reusable library of physical cardboard modules and assemble each gameplay object from:

1. a shared family chassis;
2. shared structural modules;
3. object-specific replacement modules;
4. object-specific animation and VFX modules.

No new object proceeds to generation until its family, shared modules, unique modules, projection, anchors, and animation ownership are documented here.

## 2. Corrective decisions

This plan explicitly fixes the failures found during the Watchtower attempts.

### 2.1 Projection

- Runtime objects use true top-down orthographic 90°.
- Every child module uses the same camera and the same local XY plane as its parent.
- No module may be drawn as a facade, elevation, rear view, side-view prop, or tall perspective element.
- A physically vertical narrow object seen from above becomes a small top footprint. If it must remain readable, redesign it as a flat cardboard marker parallel to the board.
- Weapons are plan-view cutouts rotating in the board plane.
- Crystals, lenses, lanterns, braziers, gears, sockets, barrels, flags, and tools are top-view cutouts, not miniature side-view illustrations.

### 2.2 Physical cardboard construction

Every structural module must read as its own physical die-cut cardboard piece:

- matte printed paper face;
- exposed tan cardboard edge;
- shallow stacked-layer separation;
- simplified printed material pattern;
- restrained local-color outline, never a glossy 3D bevel;
- no photoreal stone, wood, metal, cloth, fire, or glass;
- no deep cast shadows or cinematic lighting.

An animated child is not a painted detail on the parent. It is an independent cutout with its own pivot and attachment.

### 2.3 No baked object animation

- Base and static body remain fixed.
- Runtime composes named layers.
- Rotation, recoil, swapping frames, glow, cloth movement, gears, projectiles, impacts, and debris operate on child modules.
- Fully assembled animation strips are optional exports only. They are never the source of truth.

### 2.4 No overloaded source sheet

Do not ask ImageGen to fit an entire object, every animation, projectile, impact, and debris into one image.

Allowed source-generation units:

| Source type | Maximum content | Recommended layout |
|---|---:|---|
| Projection master | 1 assembled object | centered single object |
| Static module | 1 module | centered single object |
| Closely related static variants | 2 modules | 2 columns |
| One animation family | 4 frames of one module | fixed 2×2 |
| Extended animation family | 6 frames of one module | fixed 3×2 |
| Debris family | 8 independent pieces of one material family | fixed 4×2 |
| Projectile family | 1 projectile plus optional 4-frame trail | projectile separately; trail 2×2 |
| Impact family | 4 frames of one impact | fixed 2×2 |

Labels, grid lines, pivots, filenames, and assembled previews are never requested inside generated art. They are added deterministically to the separate review grid.

## 3. Runtime package architecture

Shared modules must not be copied into every object atlas.

```text
assets/runtime/modules/<family>/
  <family>_core_atlas.png
  <family>_core_manifest.json

assets/runtime/objects/<object>/
  <object>_addon_atlas.png
  <object>_object_manifest.json
  <object>_review_grid.png
  <object>_composite_preview.png
```

The object manifest references module IDs from both packages:

```json
{
  "object": "tracker",
  "family": "fortress_ranged",
  "imports": [
    "../../modules/fortress_ranged/fortress_ranged_core_manifest.json",
    "../ranger/ranger_shared_manifest.json"
  ],
  "addons": "tracker_addon_atlas.png",
  "assembly": [
    "fortress_round_base",
    "ranger_garrison_trim",
    "tracker_long_range_crossbow",
    "tracker_optics_ring"
  ]
}
```

Rules:

- A family atlas contains only modules genuinely shared within that family.
- An addon atlas contains only unique modules owned by one object.
- Every PNG is under 5 MB.
- Tight packed runtime rects come from JSON.
- Review grids are separate human QA artifacts.
- Every module has a globally unique semantic ID.
- A shared projectile or impact is owned by the lowest common family package.
- An object-specific projectile or impact lives in that object's addon package.

## 4. Universal module schema

Every object assembly uses these semantic slots where applicable:

| Slot | Responsibility |
|---|---|
| `base_token` | Locked ground-facing footprint |
| `chassis_static` | Shared non-moving construction above the base |
| `faction_trim` | Replaceable palette/material/insignia layer |
| `center_socket` | Pivot receiver for active mechanisms |
| `active_primary` | Rotating weapon, lens, crystal, tool, or emitter |
| `active_secondary` | Magazine, counterweight, optics, shield, rack, or support mechanism |
| `ambient_child` | Flag, glow, flame, smoke, gear, rune, liquid, vine, or bird |
| `attack_charge` | Pre-fire energy or mechanical preparation |
| `attack_release` | Muzzle flash, recoil marker, discharge, or trigger overlay |
| `projectile` | Moving owner/family projectile |
| `impact` | Owner/family hit effect |
| `destroy_piece` | Independent physical debris |
| `destroy_fx` | Smoke, sparks, dust, ether residue |
| `ruin_state` | Optional persistent destroyed base module |

Required anchors:

- `object_center`
- `center_socket`
- `active_primary_pivot`
- `active_secondary_anchor`
- `ambient_anchor_*`
- `muzzle_anchor`
- `projectile_spawn`
- `impact_center`
- `debris_origin_*`

## 5. Family overview

| Family | Objects | Shared construction principle |
|---|---|---|
| `fortress_ranged` | watchtower, ranger, tracker, assassin | Light circular fortress emplacement with central ranged weapon socket |
| `fortress_ballista` | ballista, scorpion, hailstorm | Reinforced anti-air swivel chassis and heavy tension-weapon mounting |
| `fortress_siege` | cannon, mortar, grapeshot | Recoil-rated artillery platform with ammunition and blast ownership |
| `fortress_ritual` | obelisk, beacon, pal-ward, pal-censer, pal-reliquary, mage-frost, mage-tesla, mage-prism | Shared ritual-dais geometry with replaceable faction trim, core, conductors, and magic |
| `living_wood` | palisade, hunt-snare, hunt-roost, hunt-hive | Layered living-wood/cardboard construction with replaceable organic center mechanisms |
| `economy_worksite` | sawmill, quarry | Shared work-yard footprint with replaceable resource bed, tool head, storage, and moving mechanism |
| `strategic_unique` | castle, spawn-cave | Large unique objectives; share global cardboard rules but no structural chassis |

## 6. Family specifications

### 6.1 `fortress_ranged`

Shared core modules:

- `fortress_round_base_light`
- `fortress_light_rim_stone`
- `fortress_light_center_socket`
- `fortress_light_cardboard_edge`
- `fortress_amber_lantern_housing`
- `fortress_amber_lantern_glow_01..04`
- generic stone/wood/metal debris kit

Object differences:

| Object | Unique/replaced modules | Shared inheritance |
|---|---|---|
| `watchtower` | light single crossbow, simple bolt, flat red range pennant, compact muzzle flash | family base, socket, lantern, debris |
| `ranger` | rapid crossbow, bolt magazine, arrow rack, hunting optics, ranger trim | family base/socket/lantern; establishes ranger projectile family |
| `tracker` | long-range crossbow limbs, rotating scan/optics ring, crown trim, targeting rune | family base; ranger magazine/bolt projectile |
| `assassin` | sniper crossbow, shrouded rim insert, critical-charge lens, restrained violet-amber shot FX | family base/socket; no large generic muzzle burst |

### 6.2 `fortress_ballista`

Shared core modules:

- `fortress_round_base_heavy`
- `heavy_swivel_bearing`
- `heavy_tension_mount`
- `heavy_armor_quadrants`
- `heavy_ether_lens_housing`
- heavy wood/metal debris kit

Object differences:

| Object | Unique/replaced modules | Shared inheritance |
|---|---|---|
| `ballista` | single heavy ballista, amber lens, armored heavy bolt, metallic impact | complete heavy chassis; establishes heavy bolt/impact family |
| `scorpion` | harpoon launcher, segmented tail counterweight, tether/harpoon accents | heavy chassis; ballista projectile and impact family |
| `hailstorm` | repeater limbs, fan-loaded rack, string drum, volley flash | heavy chassis/bearing; unique volley projectile and swarm impact |

### 6.3 `fortress_siege`

Shared core modules:

- `fortress_artillery_base`
- `artillery_recoil_rails`
- `artillery_turntable`
- `artillery_ammo_mounts`
- bronze/stone/wood destruction kit

Object differences:

| Object | Unique/replaced modules | Shared inheritance |
|---|---|---|
| `cannon` | long cannon barrel, breech, alchemical chamber, heated cannonball, debris-ring impact | artillery base/rails/turntable |
| `mortar` | short wide tube, elevation cradle represented in top footprint, heavy shell, broad ground burst | artillery base/turntable/ammo mounts |
| `grapeshot` | seven-barrel fan, synchronized breech rack, pellet fan projectile, scatter impact | artillery base/rails/turntable |

### 6.4 `fortress_ritual`

Shared core modules:

- `ritual_round_dais`
- `ritual_center_receiver`
- `ritual_conductor_quadrants`
- `ritual_cardboard_edge`
- shared stone/gold debris geometry

Replaceable faction trims:

- `trim_fortress_captured_void`
- `trim_sun_seal`
- `trim_paladin_gold_ivory`
- `trim_mage_copper_arcane`

Object differences:

| Object | Unique/replaced modules |
|---|---|
| `obelisk` | flat top-view void monolith token, gold rune bands, violet arc charge/projectile/impact |
| `beacon` | solar lens, halo shutters, sun-bolt, radiant halo impact |
| `pal-ward` | holy seal plate, four ward points, pulse rings; no projectile |
| `pal-censer` | four top-view braziers/censers, ember cores, gold burst projectile/impact |
| `pal-reliquary` | fortified relic casing, amber relic core, shutter armor, relic burst |
| `mage-frost` | frost crystal cluster top footprint, cold conductor ring, frost shard/impact |
| `mage-tesla` | copper coil rings viewed from above, conductor nodes, electrical arc/impact |
| `mage-prism` | rotating prism plate, beam splitters, prism projectile/impact |

### 6.5 `living_wood`

Shared core modules:

- `living_wood_ring_segments`
- `living_root_socket`
- `vine_tie_connectors`
- `thorn_splinter_debris`
- shared leaf/sap ambient accents

Object differences:

| Object | Unique/replaced modules |
|---|---|
| `palisade` | reinforced stake wall footprint, launching thorn arm, stake projectile, splinter-vine impact |
| `hunt-snare` | bramble loop, trigger plate, net/vine closure frames; no projectile |
| `hunt-roost` | flat roost platform, perch/radial feathers, hawk marker or shot module, feather impact |
| `hunt-hive` | hive chambers viewed from above, toxin vents, insect/toxin projectile, toxic impact |

### 6.6 `economy_worksite`

Shared core modules:

- `worksite_round_or_square_base`
- `worksite_frame_beams`
- `worksite_pulley_socket`
- `worksite_storage_mounts`
- shared wood/stone/metal debris geometry

Object differences:

| Object | Unique/replaced modules |
|---|---|
| `sawmill` | log bed, saw wheel, belt/gears, wood stack, sawdust ambient |
| `quarry` | stone pit insert, pick/pulley arm, rock basket, rubble pile, dust ambient |

### 6.7 `strategic_unique`

These objects use the same module schema but do not reuse a chassis.

| Object | Required unique modules |
|---|---|
| `castle` | fortress footprint, wall/roof sections, gates, seal crystal, banners, breach sections, large debris families |
| `spawn-cave` | cave rim, void opening, vortex frames, corruption veins, spawn flare, rock/void debris |

## 7. Generation order

Production is family-first, not object-list-first.

1. Approve universal cardboard material swatch and edge treatment.
2. Approve `fortress_ranged` core chassis.
3. Build and approve Watchtower addons.
4. Build Ranger addons.
5. Build Tracker and Assassin as Ranger-derived variants.
6. Approve `fortress_ballista` core; build Ballista, Scorpion, Hailstorm.
7. Approve `fortress_siege` core; build Cannon, Mortar, Grapeshot.
8. Approve `fortress_ritual` core and faction trims; build ritual objects.
9. Approve `living_wood` kit; build Palisade and Hunter structures.
10. Approve `economy_worksite` core; build Sawmill and Quarry.
11. Build strategic unique objects: Castle and Spawn Cave.

## 8. Per-module production sequence

Every module follows this order:

1. Written module contract.
2. Single-module projection master.
3. Visual approval.
4. Animation-family generation, if needed.
5. Alpha extraction.
6. Tight crop and named layer PNG.
7. Family/addon atlas packing.
8. Manifest rect/pivot/anchor registration.
9. Composed preview using runtime code.
10. Visual and technical QA.

No later step may compensate for a failed earlier step.

## 9. Naming rules

```text
<family>__<slot>__<module>
<object>__<slot>__<module>
<object>__<slot>__<module>__frame_01
```

Examples:

```text
fortress_ranged__base_token__round_light
fortress_ranged__center_socket__light_bearing
watchtower__active_primary__light_crossbow
watchtower__ambient_child__range_pennant__frame_01
ranger__active_secondary__bolt_magazine
tracker__active_secondary__optics_ring__frame_03
```

Do not use ambiguous names such as `part_01`, `body2`, `thing`, `fx_big`, or coordinates as identity.

## 10. Quality gates

Before approving a module:

- exact top-down projection: PASS;
- reads as a separate cardboard cutout: PASS;
- no side-view miniature prop: PASS;
- matches family scale and palette: PASS;
- anchor and pivot are physically meaningful: PASS;
- silhouette readable at gameplay size: PASS;
- no baked unrelated layer: PASS;
- source contains only the permitted module family: PASS;
- alpha edges and cardboard edge remain clean: PASS.

Before approving an object:

- assembly uses documented family modules only;
- unique addons match the difference table;
- shared modules are referenced, not duplicated;
- base footprint is locked;
- runtime atlas/addon atlas are each under 5 MB;
- review grid and composed preview are separate;
- every animation is child-layer-driven;
- destroy uses independent physical pieces;
- no generation for the next object begins before approval.

## 11. Open decisions requiring approval

1. Confirm true 90° top-down for every ordinary tower, overriding older near-top-down slight-tilt language for this asset class.
2. Confirm that physical cardboard modularity has priority over detailed realistic material painting.
3. Confirm family-core atlases plus object addon atlases instead of duplicating complete assets per object.
4. Confirm the seven families and memberships listed above.
5. Confirm that the next visual task is a small cardboard material/edge swatch followed by `fortress_ranged` core — not another complete Watchtower sheet.

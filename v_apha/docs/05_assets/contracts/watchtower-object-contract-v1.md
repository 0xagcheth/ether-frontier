# Watchtower / Warden's Post — Layered Object Contract v1

Status: **candidate for documentation approval; no ImageGen work authorized yet**  
Object ID: `watchtower`  
Family: `warden_ranged_lineage`  
Pipeline: `layered-object-v2` under `object-family-and-variation-spec-v4.md`

## 1. Identity lock

The Watchtower is a compact Warden lookout post represented as a low circular cardboard emplacement seen exactly from above. Its identity comes from three readable shapes:

1. a broken-ring stone parapet around a warm timber center;
2. one lightweight simple crossbow rotating around the exact center;
3. two small asymmetric stations: a red range pennant mount and an amber lantern housing.

It is not a tall tower, roofed hut, side-view fortification, generic circular weapon platform, staffed Ranger platform, royal Tracker spire, or shrouded Assassin perch.

### Silhouette test

At 64×64, the assembled silhouette must read as:

- a compact circular post;
- one thin cross-shaped ranged mechanism;
- two small asymmetric edge accents;
- no tall vertical silhouette and no dominant facade.

If the silhouette reads only as “round base with a weapon,” the design is not specific enough and must be revised before module generation.

## 2. Projection lock

- Camera: true top-down orthographic 90°.
- Every module lies in the same board-parallel XY plane.
- Permitted depth cue: 2–4 px-equivalent exposed tan cardboard edge at final 256 px base scale.
- Forbidden: visible front wall, door, stairs, rear face, side of a pole, side flame, side lantern, side-mounted bow, isometric ellipse, foreshortened circular base, horizon-facing shadow.

### Top-view reinterpretation of nominally vertical parts

| Nominal part | Required top-view design |
|---|---|
| watch post | low circular parapet ring; its top stones dominate |
| crossbow | complete plan-view bow, stock, string and axle footprint |
| flag pole | small circular mounting puck with a short radial arm; no upright pole shaft |
| pennant | flat radial cloth cutout extending from the mounting puck in the board plane |
| lantern | shallow octagonal/radial metal-card housing seen from above |
| flame | concentric amber paper cutout inside the housing, not a teardrop side flame |
| muzzle flash | small radial star/wedge paper token starting at the muzzle |
| bolt | plan-view wooden shaft with symmetric fletching and triangular point |

## 3. Material lock

Every module is an individual die-cut cardboard piece.

| Material | Printed face | Exposed edge | Outline |
|---|---|---|---|
| stone | muted cold grey, large simplified blocks | tan cardboard | dark cool-grey local ink |
| wood | warm brown, broad grain shapes only | tan cardboard | dark brown local ink |
| metal | restrained charcoal/bronze printed shapes | tan cardboard still visible | dark bronze local ink |
| cloth | dark Warden red, two or three broad folds | tan cardboard | dark red-brown local ink |
| amber light | flat gold/amber printed paper layers | pale tan/gold edge | dark ochre local ink |
| smoke/dust | flat layered grey-beige paper tokens | tan edge | grey-brown local ink |

No material may use glossy highlights, realistic glass, translucent volumetrics, realistic fire, realistic smoke, or black comic outlines.

## 4. Locked footprint and scale

- Reference composed canvas: `384×384 px` transparent.
- Locked `base_body` diameter: `256 px` at reference scale.
- Base center/pivot: `[192, 192]` on the reference canvas.
- Maximum idle assembled extent: `320×320 px`.
- Attack FX may extend to `352×352 px` safe extent.
- Base/body alpha footprint must be identical in idle, aim, and attack.
- Child modules may rotate or swap frames without changing the measured base footprint.

These are production reference dimensions, not fixed runtime atlas cells. Runtime uses tight rects from the manifest.

## 5. Module ownership table

All modules are `object_owned` in v1. No visible Watchtower module is automatically promoted to a family-shared module.

| Module ID | Slot | Ownership | Motion | Required physical read |
|---|---|---|---|---|
| `watchtower__base_body__wardens_post` | `base_body` | object-owned | static | low stone ring plus timber center |
| `watchtower__mount_socket__light_crossbow_bearing` | `mount_socket` | object-owned | static | small centered round bearing puck |
| `watchtower__active_primary__simple_crossbow` | `active_primary` | object-owned | target rotation | light plan-view crossbow |
| `watchtower__ambient_mount__range_pennant_puck` | static child | object-owned | static | radial flag mounting puck/arm |
| `watchtower__ambient_child__range_pennant__frame_01..04` | `ambient_child` | object-owned | frame loop | flat radial red cloth cutouts |
| `watchtower__ambient_mount__lantern_housing` | static child | object-owned | static | shallow top-view octagonal housing |
| `watchtower__ambient_child__lantern_core__frame_01..04` | `ambient_child` | object-owned | frame loop | concentric amber paper cores |
| `watchtower__attack_release__muzzle_flash__frame_01..04` | `attack_release` | object-owned | one-shot | compact muzzle-aligned paper wedges |
| `watchtower__projectile__simple_bolt` | `projectile` | object-owned | velocity rotation | simple plan-view wooden bolt |
| `watchtower__impact__bolt_hit__frame_01..04` | `impact` | object-owned | one-shot | restrained splinter/amber hit tokens |
| `watchtower__destroy_piece__stone_01..06` | `destroy_piece` | object-owned | physics | independent parapet fragments |
| `watchtower__destroy_piece__wood_01..06` | `destroy_piece` | object-owned | physics | independent deck/crossbow fragments |
| `watchtower__destroy_piece__metal_01..03` | `destroy_piece` | object-owned | physics | bearing/lantern fittings |
| `watchtower__destroy_fx__dust__frame_01..04` | `destroy_fx` | object-owned | one-shot | flat dust-cloud paper layers |
| `watchtower__ruin_state__broken_post` | `ruin_state` | object-owned | persistent | broken ring and exposed timber center |

## 6. Assembly and draw order

Draw order from bottom to top:

1. `base_body`
2. `ruin_state` when destroyed; mutually exclusive with intact upper surface
3. `mount_socket`
4. `ambient_mount__range_pennant_puck`
5. `ambient_mount__lantern_housing`
6. `ambient_child__range_pennant`
7. `ambient_child__lantern_core`
8. `active_primary__simple_crossbow`
9. `attack_release__muzzle_flash`
10. debug-only attachment overlays in review files; never runtime

Projectile, impact, debris, and destroy FX are world-space spawned layers rather than persistent assembled children.

## 7. Anchors and pivots

Coordinates below are normalized relative to the 384×384 reference canvas. Exact pixel values are measured again after approved art is normalized.

| Anchor | Normalized reference | Owner | Consumer |
|---|---:|---|---|
| `object_center` | `[0.500, 0.500]` | base body | object placement |
| `active_primary_pivot` | `[0.500, 0.500]` | mount socket | crossbow |
| `pennant_mount_anchor` | `[0.285, 0.650]` | base body | pennant puck |
| `pennant_cloth_anchor` | local `[0.500, 0.500]` | pennant puck | cloth root |
| `lantern_mount_anchor` | `[0.715, 0.650]` | base body | lantern housing |
| `lantern_core_anchor` | local `[0.500, 0.500]` | lantern housing | amber core |
| `muzzle_anchor` | measured at forward stock tip | crossbow | muzzle flash/projectile |
| `projectile_spawn` | same as muzzle anchor | crossbow | simple bolt |
| `impact_center` | local `[0.500, 0.500]` | impact family | world hit point |
| `debris_origin` | `[0.500, 0.500]` | base body | destroy spawner |

Crossbow local axis points to `+X` in source art. Runtime rotates that axis toward the target.

## 8. Animation contracts

### Idle

- Base, timber center, bearing, crossbow and mounts remain pixel-static.
- Pennant cycles frames `01→02→03→04→03→02`, 140 ms per frame, loop.
- Lantern core cycles `01→02→03→04→03→02`, 110 ms per frame, loop.
- No whole-object breathing, rocking, scaling, or floating.

### Aim

- Only the complete `active_primary` rotating group changes rotation.
- Rotation pivot must coincide with the bearing center within 1 px at reference scale.
- Pennant and lantern do not inherit crossbow rotation.

### Attack

- Base/body remains locked.
- Optional crossbow recoil is a local translation along its own `-X` axis, maximum 4 px, returning to zero.
- Muzzle flash plays `01→02→03→04`, 55 ms per frame, once, then disappears.
- Projectile spawns from `projectile_spawn` and rotates along velocity.

### Impact

- Bolt-hit frames play once at the collision point.
- Impact must remain smaller than the base radius and must not resemble cannon, magic, or ballista impact language.

### Destroy

- Intact assembled children are hidden.
- Ruin state appears at the exact locked object center.
- Stone, wood and metal pieces spawn independently from documented origins.
- Dust frames play once; no baked complete-object destruction strip is source-of-truth.

## 9. Separate ImageGen production calls

The Watchtower requires at least the following independent generation calls. Combining these jobs is forbidden.

| Job | Generated contents | Layout | Approval dependency |
|---|---|---|---|
| `WT-00` | one assembled projection master | one centered object | contract approval |
| `WT-01` | base/body only | one centered module | WT-00 approved |
| `WT-02` | bearing socket only | one centered module | WT-00 approved |
| `WT-03` | simple crossbow only | one centered module | WT-00 approved |
| `WT-04` | pennant mounting puck only | one centered module | WT-00 approved |
| `WT-05` | four pennant cloth frames only | fixed 2×2 | WT-04 approved |
| `WT-06` | lantern housing only | one centered module | WT-00 approved |
| `WT-07` | four lantern core frames only | fixed 2×2 | WT-06 approved |
| `WT-08` | four muzzle flash frames only | fixed 2×2 | WT-03 approved |
| `WT-09` | simple bolt only | one centered module | WT-03 approved |
| `WT-10` | four bolt-hit frames only | fixed 2×2 | WT-09 approved |
| `WT-11` | six stone debris pieces only | fixed 3×2 | WT-01 approved |
| `WT-12` | six wood debris pieces only | fixed 3×2 | WT-01 and WT-03 approved |
| `WT-13` | three metal debris pieces only | fixed 3×1 | WT-02 and WT-06 approved |
| `WT-14` | four dust frames only | fixed 2×2 | WT-11 approved |
| `WT-15` | ruin state only | one centered module | WT-01 approved |

Every call uses a flat removable chroma-key background. Labels, cell borders and pivot crosses are added afterward by deterministic tooling.

## 10. Projection-master prompt requirements

The `WT-00` prompt must describe only one assembled Watchtower and must include:

- exact 90° orthographic plan view;
- compact circular Warden post;
- broken-ring stone parapet with broad top faces;
- warm timber center;
- centered lightweight plan-view crossbow;
- radial red pennant puck and flat cloth marker;
- shallow top-view octagonal lantern with concentric amber paper core;
- every visible part made from stacked die-cut cardboard;
- no animation variants, projectile, impact, debris, labels, or grid.

It must explicitly prohibit upright poles, teardrop side flames, side lanterns, facade walls, tall tower silhouettes, isometric ellipses, realistic metal, glossy 3D, and a generic interchangeable turret base.

## 11. Must differ from related objects

| Related object | Watchtower must not contain |
|---|---|
| Ranger | hunter-green platform, staffed markers, magazine, rapid limbs, tall arrow rack, hunting optics |
| Tracker | royal blue banners, crown trim, large scan ring, targeting runes, spotter-spire silhouette |
| Assassin | hooded/shrouded rim, sniper lens, heavy sniper-ballista, violet critical charge |
| Ballista | reinforced heavy chassis, large tension mount, ether lens, heavy bolt rack |
| Cannon/Mortar/Grapeshot | recoil rails, artillery turntable, barrels, shell storage, smoke-heavy attack language |
| Ritual objects | ritual dais, conductor quadrants, floating crystal/solar/magic core |

Approval of Watchtower does not authorize reuse of its base, crossbow, pennant, lantern, projectile, impact, or debris by another object.

## 12. Runtime package contract

```text
assets/runtime/objects/watchtower/
  watchtower_layered_runtime.png
  watchtower_layered_manifest.json

assets/review/watchtower/
  watchtower_layered_review_grid.png
  watchtower_layered_composite_preview.png
  watchtower_rotation_clearance_review.png
```

Runtime atlas requirements:

- one object only;
- tight transparent packing;
- under 5 MB;
- no labels, grid, preview, pivot crosses, or empty fixed cells;
- manifest owns rects, pivots, attachments, draw order, animations and transforms.

## 13. Visual acceptance gate

All must pass before module generation proceeds:

- assembled master reads as true 90° top-down;
- all nominally vertical features are successfully redesigned in plan view;
- silhouette reads as a Warden lookout at 64×64;
- every visible part reads as a separate cardboard cutout;
- crossbow is lightweight and simple, not Ranger/Tracker/Assassin/Ballista hardware;
- pennant is radial/top-view, not side-view cloth on an upright pole;
- lantern is shallow/top-view, not a side-view lantern icon;
- no glossy 3D, facade, isometric ellipse, realistic flame/smoke, or baked terrain;
- base/body has enough complete hidden art beneath child modules for rotation and swapping.

## 14. Technical acceptance gate

- PNG files open with correct alpha;
- source provenance recorded per generation job;
- all required module IDs exist;
- every rotatable/animated layer has pivot and attachment;
- base footprint is unchanged in idle/aim/attack;
- rotation clearance passes at 0°, 45°, 90°, 135°, 180°, 225°, 270°, and 315°;
- all rects are in bounds and non-overlapping;
- runtime atlas is under 5 MB;
- review-only content is absent from runtime;
- manifest parses and is the sole runtime source of rects;
- visual review explicitly approves the projection master before `WT-01` begins.

## 15. Current decision

The previous single-sheet Watchtower candidate is rejected and is not a reference for new generation. The next authorized production action after approval of this contract is `WT-00` only: one assembled projection master.

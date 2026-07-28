# Ether Frontier — Object Families and Variation Specification v5

> **SUPERSEDED FOR IDENTITY AND ABILITIES (2026-07-26).** Use only for generic
> technical notes that do not name a mechanism. All weapon families, roles and
> emitted effects are replaced by `seven-circles-object-redesign-v1.md` and
> `asset-prompt-bible-v7.md`.

Status: **archival weapon-led specification**  
Updated: 2026-07-24

V5 replaces the lore, names and visual ownership of v4. V4 remains a supporting
technical reference only for animation timing, anchors and action lists that do
not contradict this document, `technical-asset-contract.md` or an approved
per-object Layer Contract.

## 1. Non-negotiable construction

- exact true top-down orthographic 90°;
- smooth solid punchboard and printed paper, never corrugated packaging board;
- one complete die-cut perimeter and visible cardboard edge per physical piece;
- stable footprint for base/body during normal animation;
- moving, rotating, glowing, burning, smoking and deforming parts are children;
- the main gameplay mechanism is slightly enlarged and more saturated than the
  quiet base, but returns to ordinary proportions if it harms assembly;
- one object family per compact transparent runtime atlas, maximum 5 MB;
- labels, grids, pivots and assembled previews exist only in separate QA files;
- manifest JSON is the source of truth for rects, pivots, attachments,
  drawOrder and animations;
- projectile, impact and unique debris live in the owning family atlas;
- no object advances until visual and technical validation pass.

## 2. Reuse levels

### Level A — technical grammar

May be shared conceptually across all families: cardboard edge treatment,
contact-shadow logic, manifest schema, pivot conventions, packing and QA.

### Level B — family core

May be reused only inside one declared family: footprint class, deck or dais
logic, bearing type, attachment vocabulary and compatible repair pieces.

### Level C — object identity

Never silently reused: weapon, functional mechanism, ammunition, owner trim,
circle-specific child animation, projectile, impact and destruction signature.

Two similar towers do not become recolors. They may share a base grammar, but
the gameplay mechanism and silhouette must explain their different function.

## 3. Source-generation rule

ImageGen 2 must generate:

1. one coherent assembled projection master;
2. structural master without animated children;
3. one coherent master for each complex mechanism;
4. matching state edits from that same coherent geometry;
5. effect and debris families in separate calls when required.

Do not ask ImageGen to place the complete decomposition, labels, animation
frames and previews on one sheet. Normalization and atlas packing happen after
source generation.

## 4. Family map

| Family | Runtime IDs | Shared family core |
|---|---|---|
| Wind ranged | `watchtower`, `ranger`, `tracker`, `assassin` | low lookout footprint, radial deck grammar, wind-card attachment, compact bearing |
| Heavy tension | `ballista`, `scorpion`, `hailstorm` | heavy low base, reinforced swivel, tension mounts, armored quadrants |
| Thunder artillery | `cannon`, `mortar`, `grapeshot` | artillery footing, turntable, recoil/elevation mounts, ammunition anchors |
| Circle constructs | `obelisk`, `beacon`, `pal_ward`, `pal_censer`, `pal_reliquary`, `mage_frost`, `mage_tesla`, `mage_prism` | low ritual/work dais and center socket only; mechanisms remain object-specific |
| Living Root | `palisade`, `hunt_snare`, `hunt_roost`, `hunt_hive` | living wood connectors, root sockets, vine ties, leaf/splinter debris grammar |
| Worksites | `sawmill`, `quarry` | low worksite footprint, beam-frame grammar, pulley/storage anchors |
| Strategic unique | `castle`, `spawn_cave` | no reusable visual core |

## 5. Per-object contracts

### Wind ranged family

| ID / display name | Function and primary mechanism | Required independent identity pieces | Forbidden shortcut |
|---|---|---|---|
| `watchtower` — Ветровой дозор | early single-shot range; one simple lightweight crossbow | twenty stone tiles, eight deck sectors, layered bearing, four copper arcs, crossbow body/arms/string, loaded bolt, four-bolt rack, cloth, lantern/flame/glow, impact and debris | no oversized ballista, no facade tower |
| `ranger` — Стрелец Ветра | fast repeated direct fire; compact bow launcher with feed rail | twin short limbs, sliding bolt feed, small magazine, feathered wind vane, rapid-shot bolt family | not Watchtower with extra arrows |
| `tracker` — Соколиный круг | long-range marking; rotating sighting frame and bird-guided shot | long bow stave, open sight cards, separate bird marker, route ribbon, marked-shot projectile/impact | no generic sniper crossbow or targeting rune |
| `assassin` — Тихий омут | slow critical strike; concealed torsion dart mechanism | narrow torsion rails, covered dart bed, tension tabs, shadow-cloth shutters, heavy dart and silent fiber impact | no crossbow recolor, no firearm silhouette |

### Heavy tension family

| ID / display name | Function and primary mechanism | Unique parts |
|---|---|---|
| `ballista` — Громовой самострел | heavy direct anti-air bolt | massive separate arms, central stock, winch, tension ropes, heavy bolt, recoil slide |
| `scorpion` — Змеиный гарпун | hook/pull or armor break | single harpoon rail, segmented counterweight tail, chain/rope cards, hooked projectile |
| `hailstorm` — Стрибожья метель | multi-projectile volley | fan of short launch channels, rotating feed drum, separate loaded darts and spread impact |

The shared heavy base never implies a shared weapon. Ballista, harpoon rail and
volley fan require different coherent ImageGen masters.

### Thunder artillery family

| ID / display name | Function and primary mechanism | Unique parts |
|---|---|---|
| `cannon` — Громовой станок | direct explosive shot | long barrel card, breech, recoil rails, round charge, compact muzzle flash and smoke |
| `mortar` — Медвежья ступа | arcing area strike | short wide bowl, elevation cradle, pestle-like tube, heavy shell, broad ground burst |
| `grapeshot` — Семистрельный раскат | close cone damage | seven short guide channels, shared trigger plate, seven charge tabs, pellet fan |

No artillery object uses a bow, crossbow or tension-arm analogue.

### Circle constructs

| ID / display name | Circle/function | Enlarged primary mechanism and child layers |
|---|---|---|
| `obelisk` — Камень Имени | Stone + Name; disrupt command | stepped memory slabs around an absent center; separate name cards and copper bridges |
| `beacon` — Солнечная мера | Sun; reveal/empower | amber lens and low radial reflector; separate ochre shutters, beam cards and glow |
| `pal_ward` — Граница Грома | Thunder; protective boundary | four contract contacts on an open ring; separate shield cards and discharge arcs |
| `pal_censer` — Жаровня Солнца | Sun; heat aura | craft brazier and bellows; separate coals, flame, smoke and heat rings |
| `pal_reliquary` — Ларец Имён | Stone + Name; protective memory | squat layered chest; separate lid, name cards, ribbons and pulse |
| `mage_frost` — Зеркало Воды | Water; slow | four water-silver reflection cards, rotating cold focus, ripple and frost shards |
| `mage_tesla` — Медный раскат | Thunder; chain damage | low coil stack, contacts and insulators; separate orb and paper arcs |
| `mage_prism` — Призма Имени | Sun + Name; split beam | rotating prism-card assembly, movable splitters and independent ray children |

These objects share only dais/socket engineering. Crystal, lens, chest, brazier,
coil and stone are never treated as interchangeable skins.

### Living Root family

| ID / display name | Function | Unique parts |
|---|---|---|
| `palisade` — Плетень Корня | block and slow | individual stakes, living roots, closure vines, damage/breach states |
| `hunt_snare` — Силок Корня | trap and hold | concealed trigger card, independent loop, spring branch, open/closed states |
| `hunt_roost` — Соколиный дозор | ranged nature support | low platform, perch, separate bird marker, optic and feather effects |
| `hunt_hive` — Роевой короб | poison/swarm | layered bark chambers, comb cards, reservoir, insects and liquid overlays |

No living structure receives a mechanical crossbow unless its own runtime
function explicitly requires a launcher; current four contracts do not.

### Worksites

| ID / display name | Function | Unique parts |
|---|---|---|
| `sawmill` — Плотницкий круг | wood production and repair | radial bench, enlarged toothed saw wheel, belt/gears, log bed, wood stack, shavings |
| `quarry` — Каменный круг | stone production | open cut-stone pit, low derrick, pulley arm, basket, rubble and dust |

Normal working loops keep the base fixed. Saw, belt, pulley, basket, dust and
resource pieces are independent children.

### Strategic unique

| ID / display name | Contract |
|---|---|
| `castle` — Седьмой круг | low radial defended core built from seven visibly separate material languages, central name hearth and seven road sockets; no castle facade |
| `spawn_cave` — Разрыв Глубин | horizontal layered tear through soil, root, stone, Nav tracing and deep clay; opening/vortex and spawn flare are children; never a side-view cave mouth |

## 6. Approval order

1. `watchtower`;
2. remaining Wind ranged objects one at a time;
3. Heavy tension;
4. Thunder artillery;
5. Circle constructs;
6. Living Root;
7. Worksites;
8. Strategic unique objects;
9. heroes, enemies and environment according to their owning contracts.

Approval of one object authorizes only its family grammar, not automatic approval
of its relatives.

## 7. Per-object documentation gate

Before ImageGen, every object needs:

- runtime ID and display name;
- gameplay function;
- primary and optional secondary circle;
- stable footprint description;
- enlarged primary mechanism;
- complete named layer inventory;
- animation/action inventory;
- pivots and attachment plan;
- projectile/impact/debris ownership;
- explicit forbidden motifs;
- exact source-call sequence;
- visual and technical validation checklist.

If any item is missing, the object remains at documentation gate.

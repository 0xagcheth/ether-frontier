# Ether Frontier — Asset Prompt Bible v4

Status: canonical production prompt bible  
Updated: 2026-07-23

## 1. Назначение и приоритет

Этот документ полностью заменяет визуальные и сюжетные описания legacy-файла
`asset-prompt-bible.md`. Старый файл может использоваться только для проверки
исторических runtime-ID до удаления или архивирования.

Для точного объекта читать в порядке:

1. `object-family-and-variation-spec-v4.md`;
2. `object-lore-material-overlay-v4.md`;
3. этот prompt bible;
4. `technical-asset-contract.md`;
5. активный clean-restart prompt.

При конфликте объектная спецификация определяет конструкцию, lore overlay —
материал и владельца, этот файл — формулировку генерации.

## 2. Master ImageGen prompt

Raster source generation uses **built-in ImageGen 2** by explicit user
direction. Do not silently switch to another image model, CLI/API path, manual
raster drawing, or vector substitute for artistic sprite/concept generation.
Deterministic SVG remains allowed only for technical diagrams, pivot/attachment
QA, manifests and atlas tooling.

Использовать как общий префикс, после него добавлять только один текущий объект
или один модуль:

> Production game sprite source for Ether Frontier. Exact true top-down
> orthographic 90-degree camera, directly overhead, no facade and no visible
> vertical elevation. Handmade premium tabletop board-game construction from
> separately die-cut smooth solid punchboard and printed paper. Matte cartoon
> ink over visible fine paper fibers and pressed-pulp grain; thin tan solid-board
> cut edges; tiny separation gaps and compact soft contact shadows between
> physically separate layers. Warm clear moderately saturated earthy print
> colors, dark local-color ink edges, sparse original geometric accents.
> Cute simplified printed illustration, not a realistic miniature. Fully visible,
> centered, safe padding, uniform removable chroma background, no cast shadow on
> background. No glossy 3D, no plastic, no corrugated cardboard, no isometric
> view, no side view, no cinematic perspective, no labels, no grid, no pivot
> marks, no assembled review layout, no baked terrain.

### Gameplay-accent hierarchy

Every object uses an intentionally exaggerated cartoon gameplay hierarchy:

- the mechanism that communicates the object's primary action is 15–30% larger
  than a physically neutral proportion would suggest;
- the primary mechanism receives the clearest silhouette, strongest local
  contrast and most saturated functional color;
- secondary animated accents use the next-highest contrast;
- the stable base/body remains quieter, darker and less saturated;
- exaggeration must improve runtime readability without changing the locked
  footprint or making one class resemble a heavier specialization.

For firing towers the weapon and loaded projectile are the primary accent. For
resource, aura, trap and support objects, enlarge the actual gameplay mechanism
instead of adding an unrelated weapon.

### Negative prompt block

> Reject facade, rear view, side view, three-quarter view, isometric camera,
> tall perspective, horizon, floor plane, realistic architectural wall faces,
> glossy render, plastic toy, foam, clay, corrugated shipping cardboard,
> photoreal textures, airbrushed gradients, black comic outlines, excessive
> filigree, all-over runes, copied historical or sacred symbols, generic Western
> fantasy heraldry, characters baked into building art, unrelated weapons,
> labels, UI, grid, shadow on chroma, clipping.

## 3. Source-generation discipline

Один ImageGen call создаёт только одну из единиц:

- assembled projection master;
- `base_body`;
- один static child;
- кадры одного animation child;
- один projectile;
- один impact family;
- один debris material family.

Нельзя просить «все слои объекта на одном листе» до утверждения projection
master. Нельзя генерировать несколько разных объектов одной картинкой.

Каждая source unit наследует масштаб и ориентацию утверждённого master. Любое
изменение силуэта требует возврата к visual approval.

## 4. Универсальный object-contract template

Перед генерацией заполнить:

```text
Object:
Runtime aliases:
Family:
Gameplay role:
Canon sources:
Owner/cultural layer:
Identity sentence:
Silhouette test at runtime scale:
Locked footprint:
Base/body:
Mount/socket:
Primary mechanism:
Secondary modules:
Moving children:
Ambient children:
Projectile/effect:
Impact:
Destruction inventory:
Mechanical chain:
Allowed reuse:
Forbidden reuse:
Animations:
Required anchors:
Draw order:
Source-generation calls:
Visual acceptance:
Technical acceptance:
```

## 5. Watchtower — первый production baseline

### 5.1 Contract

**Object:** `watchtower`; runtime alias `fire`.  
**Display name:** Дозорная весь.  
**Family:** `warden_ranged_lineage`.  
**Role:** простая ранняя дальняя защита.

**Identity sentence:** компактный круглый каменный наблюдательный пост с
радиальным деревянным настилом, одним небольшим центральным самострелом,
сигнальной тканью и фонарём.

**Silhouette test:** при уменьшении должны различаться каменное кольцо,
крестообразный/радиальный настил и увеличенная направленная форма оружия.
Самострел получает примерно 20–25% cartoon exaggeration относительно
нейтральной пропорции, но остаётся внутри парапета и не читается как тяжёлая
Ballista.

**Locked footprint:** компактный неровный круг. Две малые выемки доступа входят
в основание, но не образуют фасад или ворота.

**Base/body:** низкое каменное кольцо, фиксированный деревянный настил, плоские
attachment zones для bearing, ткани и фонаря. В base нет оружия, огня, ткани,
болта или оператора.

**Mount/socket:** малый центральный подшипник строго в геометрическом центре.

**Primary mechanism:** лёгкий простой самострел сверху: деревянные плечи,
тетива, короткая направляющая и спуск. Это рабочий механизм, не декоративный
крест.

**Secondary:** плоская радиальная сигнальная ткань; низкий top-view корпус
фонаря; небольшой запас болтов без вертикальной стойки.

**Moving children:**

- `active_primary_crossbow`;
- `crossbow_string_release`;
- `crossbow_recoil`;
- `signal_cloth_01..04`;
- `lantern_flame_01..04`;
- `attack_flash_01..03`.

**Projectile:** простой деревянный болт Watchtower. Не ranger bolt.  
**Impact:** маленький бумажный скол дерева/камня.  
**Destroy:** 3–5 каменных частей кольца, 2–4 части настила, плечи самострела,
направляющая, ткань, фонарь, болты, древесная щепа, картонная пыль.

**Mechanical chain:** короткий запас болтов → ручная укладка в направляющую →
натянутая тетива → спуск → болт из `projectile_spawn` → компактный physical
impact.

**Allowed reuse:** только утверждённый Warden stone/wood material kit и
технический формат anchors.

**Forbidden reuse:** Ranger platform, ranger magazine, royal optics, heavy
ballista limbs, cannon parts, Antlan rings, Grey lens, character silhouette.

**Anchors:**

- `object_center`;
- `active_primary_pivot`;
- `muzzle_anchor`;
- `projectile_spawn`;
- `flag_anchor`;
- `lantern_anchor`;
- `debris_origin_stone`;
- `debris_origin_wood`.

**Draw order:** base stone → fixed deck → bearing → bolt reserve → rotating
crossbow → string/recoil overlay → signal cloth → lantern casing → flame →
attack FX.

### 5.2 Watchtower projection-master prompt

Добавить к master prompt:

> One assembled Ether Frontier Watchtower / "Dozornaya Ves": a compact low
> irregular circular lookout ring of cold grey printed stone-card pieces, a
> fixed radial dark-warm timber deck, exactly two small plan-view access notches,
> one small lightweight simple wooden crossbow centered on a circular bearing,
> one muted burgundy radial signal-cloth cutout and one tiny amber lantern casing.
> The weapon is modest and clearly subordinate to the lookout-post silhouette.
> Practical ancient-Rus frontier craft with restrained Soviet inventory logic;
> no person. Most surfaces plain; at most one short original stepped border on
> the signal-cloth mount. Every visible component reads as its own die-cut
> cardboard piece. The whole object is seen exactly from directly overhead.

### 5.3 Watchtower source calls

1. projection master;
2. base/body without children;
3. bearing;
4. complete rotating crossbow;
5. string/recoil child frames;
6. signal cloth 4-frame family;
7. lantern casing;
8. flame/glow 4-frame family;
9. wooden bolt;
10. impact 4-frame family;
11. stone debris family;
12. wood/mechanism debris family;
13. dust/smoke destruction FX.

### 5.4 Required animations

- `idle`: base fixed; cloth 4-frame loop; flame 4-frame loop;
- `aim`: crossbow rotates around exact center;
- `attack`: string release, short recoil, projectile spawn;
- `impact`: non-looping 4 frames;
- `destroy`: detach cloth and lantern, separate crossbow, break deck and ring,
  settle dust, hold final ruin if defined.

### 5.5 Watchtower rejection conditions

- any facade or visible tall wall;
- giant crossbow dominating the post;
- person, hands or helmet;
- shared ranger/ballista weapon;
- all parts painted on one flat disc;
- side-view flag or lantern;
- baked assembled attack frames;
- glossy stone or realistic fire;
- unsafe chroma contamination;
- unstable footprint;
- atlas above 5 MB;
- label or preview inside runtime atlas.

## 6. Player tower and building prompts

Каждая строка дополняется master prompt и полным contract из object spec.

| ID | Prompt identity |
|---|---|
| `ranger` | Object-owned hunter-green firing platform, rapid volley crossbow, tall fletched-bolt rack, separate magazine and hunting optics; visibly not the Watchtower body. |
| `tracker` | Royal-blue and rune-gold spotter construction shaped around a large rotating scan ring and precision launcher; no crown emblem copied from history, no Ranger recolor. |
| `assassin` | Low broken-silhouette sniper perch, radial dark shroud pieces, critical lens and heavy single-shot mechanism; no ninja or Gothic architecture. |
| `ballista` | Reinforced cold-stone and steel anti-air emplacement with huge single swivel ballista, tension mount, amber tracking lens and heavy bolt rack. |
| `scorpion` | Harpoon carriage dominated by a segmented counterweight tail, cable drum and ether harpoon cradle; not a normal ballista with a tail decoration. |
| `hailstorm` | Wide anti-swarm battery built around a fan-loaded small-bolt rack, rotating string drum and visible feed; unique spread attack. |
| `cannon` | Low stone-and-timber recoil carriage, original long alchemical/electromechanical barrel, copper buses and shell cradle; no real military model. |
| `mortar` | Broad armored top-view shell platform around a concentric mortar mouth, separate shell stacks and smoke-ring child; no side-pointing tube. |
| `grapeshot` | Wide radial seven-barrel battery with synchronized breech and pellet hoppers; exactly readable fan construction. |
| `palisade` | Reinforced living-wood wall footprint with rhythmic stakes, separate vines, thorn arm and root base; no medieval facade wall. |
| `obelisk` | Low stepped Veles memory-stone receiver with Daariyan copper rivers and a removable central name-card system; no tall monolith or Grey lens. |
| `beacon` | Broad low Dazhbog revelation circle with ochre printed reflectors, radial shutters and solar lens; no lighthouse. |
| `sawmill` | Compact expedition carpentry yard with log bed, storage zones, separate saw wheel, belt and sawdust tokens; no operator. |
| `quarry` | Open memory-stone worksite with cut blocks, pulley, derrick arm, rope basket and dust; one excavated Daariyan material trace. |
| `pal_ward` | Low open Perun contract ring with four ward points, separate shield cards and pulse rings; no projectile. |
| `pal_censer` | Radial Svarog craft-brazier with four chain sockets, separate coals, bellows, flame and smoke; not a church censer. |
| `pal_reliquary` | Squat armored archive chest for named ancestors, separate lid, cards, ribbons and protective pulse; no anonymous saint relic. |
| `mage_frost` | Daariya/Lelya cold-variant receiver with four displaced archive petals, frost focus and ice-card rings; not a snowflake decal tower. |
| `mage_tesla` | Low Kitezh/Perun radial copper coil with separate contacts, insulators, ether orb and paper lightning arcs; no side-view spire. |
| `mage_prism` | Low Prav receiver built around separately rotating prism cards and copper bridges; each beam is an independent paper FX layer. |
| `hunt_snare` | Low concealed bramble ring with trigger plate, loop, spring branch, closure vines and leaves; no projectile. |
| `hunt_roost` | Distinct timber-and-rope Pathfinder platform with separate hawk token, ranging optic and heavy hunting rig; not Watchtower with green trim. |
| `hunt_hive` | Gnarled cardboard hive/stump footprint with readable comb clusters, poison reservoir, separate swarm and liquid children. |
| `castle` | Kitezh-17 as a low radial layered archive site: Soviet frame, timber cell, four Daariyan copper rivers, one flooded Antlan fragment, separate gates, cables, antenna and searchlight; never a medieval castle. |
| `spawn_cave` | Horizontal multi-contour Peklo tear in the map, separate ground rim, Nav void, Lower City clay contour, Grey revision layer and pulsing seams; never a front-facing cave mouth. |

Runtime aliases `fire`, `ice`, `storm`, `sun`, `thorn`, `void` do not receive
separate prompts or atlases.

## 7. Hero prompts

Герои получают отдельные character atlases. Buildings never include them.

### Common character prefix

> Directional tabletop character sprite made from a small stack of separately
> cut printed cardboard body and equipment pieces. Stable readable body
> footprint, consistent scale, matte paper grain, top-down gameplay projection.
> Limbs and held equipment separated according to animation needs. No realistic
> human rendering, no portrait likeness, no ethnographic costume collage.

| ID | Identity and owned layers |
|---|---|
| `paladin` | Captain Lev Gordin: quilted field layer, lamellar cards, burgundy-white shield, copper contacts, compact hammer; body/feet, shield, hammer, spark and shield rings separate. |
| `mage` | Doctor Ilya Serov: dark-blue work clothing, copper measuring ring, birch-bark and paper bookmarks; body, ring, cards, bookmarks and slow field separate. |
| `hunter` | Marya Lytkina: practical pine/bark/river taiga clothing, short bow, rope, birch-bark box and hawk marker; body, bow, arrow, marker, trail and thorn burst separate. |

Required action families follow current gameplay: idle, move/facing, attack or
cast, hit, defeat/return. Exact direction count comes from `sprite-bible.md` and
runtime use, not from the legacy prompt.

## 8. Lower City enemy prompts

Common material prefix:

> Lower City construction language: clay-dark scale, bone, dark wood, woven
> material, shell plates and occasional repaired Daariyan copper hardware.
> Underground technology is specialized, not primitive. Broken-spiral shell
> sign is original and sparse.

| ID | Identity |
|---|---|
| `fast` | Lean low-running psoglav beast, minimal bone collar, red clan cards; fastest clean silhouette. |
| `warrior` | Upright reptilian citizen levy, short weapon, woven shield and practical load. |
| `brute` | Broad amphibious heavy body with layered mud armor and stone/wood club. |
| `raider` | Small asymmetric name thief with separate blank tags, hook and stolen survey cards. |
| `berserker` | Fast red-crested assault lizard with light bone plates and two cutting tools. |
| `shield` | Broad shell infantry with several separately named shield plates. |
| `tunneler` | Low digging caste with shovel claws, feelers and separate soil debris. |
| `spider` | Lower City rider attachment on broad radial cave arachnid; legs, rider and tether spools separate. |
| `air` | Lean plan-view reptilian flyer with separate membrane wings and harness plates. |

## 9. Grey enemy prompts

Common prefix:

> Grey revision language: pale ceramic shell, matte metal, seamless printed grey
> fields, cold cyan slits and replaceable probability lenses. Differences are
> deliberately reduced, but gameplay silhouettes remain distinct. No coding
> through real human ethnicity.

| ID | Identity |
|---|---|
| `witch_doc` | Slender Grey Mentor shell, oversized separate lens eyes and floating control cards. |
| `bomber` | Small pale viman disc with central lens, separate shutters and exactly two suspended charge pods. |
| `spellbreak` | Compact sign suppressor with separate incomplete rectangular interference frame. |
| `scout` | Small observation shell dominated by one rotating lens; remains planned until behavior approval. |

## 10. Damaged Nav prompts

Common prefix:

> Incomplete double paper contour, missing center, smoke-white and indigo print,
> cold copper patina. Glow and smoke are separate die-cut translucent-paper
> tokens, never volumetric neon.

| ID | Identity |
|---|---|
| `slime` | Irregular overlapping incomplete shapes with traces of uncompleted eyes/tools. |
| `necro` | Tall blank-record figure with separate strips, split stylus and repeat-frame cards. |
| `summoner` | Heavy caster built around a separate tear token and orbiting empty silhouettes. |
| `golem` | Large assembled body of slabs, bones, archive boxes and missing-name cards; each component separable. |
| `wraith` | Humanlike cutout with deliberately missing center and no assigned feet. |

## 11. Machine and owner-overlay prompts

| ID | Base identity |
|---|---|
| `machine` | Original Kitezh tracked/wheeled service platform with faded enamel, optical frame, cables and readable service permissions. |
| `iron_jug` | Heavy walking amalgam of crane parts, armor panels, copper bus bars and directive plates. |

Owner overlays are separately generated child packages:

- `grey_capture`: pale ceramic joint, probability lens, erased inventory card;
- `antlan_drowned`: broken brass ring, dark-turquoise panel, salt line;
- `league_debt`: removable empty weight, dark-blue debt ribbon, double clamp.

Overlay cannot obscure the base mechanical silhouette or silently create a new
entity.

## 12. Boss prompts

| ID | Prompt identity |
|---|---|
| `miniBossGround` | Large disciplined Lower City commander with separately layered clan armor and signal blade. |
| `bossGround` | Articulate armored Lizard Prince whose unique chest module is a split treaty plate. |
| `bossAir` | Huge radial sky serpent with three independently animated plan-view heads and separate layered wings. |
| `bossMachine` | Segmented Iron Serpent combining Kitezh reactor, Antlan Fatta ring and Grey lens; every segment independently named. |
| `dread_lord` | Human Arkady Kosteev in restrained grey suit surrounded by five separate death carriers: signal, container, tablet, line and needle; no fantasy dark armor. |
| `elder_dragon` | Multi-cell ancient Lower City guardian of separate stone-scale segments and contract attachments; not a European side-view dragon. |

## 13. Resources and environment prompts

| ID | Prompt identity |
|---|---|
| `res_gold` | Copper-gold contract token with an open name field, no real coin emblem. |
| `res_wood` | Living wood section with flexible growth line and fine fiber print. |
| `res_stone` | Memory-stone card with one readable material trace, no rune carpet. |
| `tree_oak` | Broad readable memory oak top canopy, separate trunk/leaf construction when animated. |
| `tree_pine` | Far-Eastern cedar/pine top canopy with layered needle-cluster cards. |
| `tree_oak_grow`, `tree_pine_grow` | Growth stages from restored cell links, not instant full tree magic. |
| `rock_a` | Cold Daariyan stone with one oxidized copper clamp. |
| `rock_b` | Antlan fragment with salt line and faded turquoise print. |
| `rock_c` | Kitezh excavation stone with one inventory mark. |
| `rock_grow` | Reassembly stages of remembered geometry. |
| `backgroud` | Defense map of sopka, river, taiga and buried layers; preserve misspelled runtime ID only in code. |

Background is the only retained environmental image category during the clean
restart. It is not packed into object-family atlases.

## 14. Projectile, impact and destruction prompts

### Projectile

> One isolated object-owned projectile in exact top view, aligned along its
> declared forward axis, separately die-cut printed cardboard/paper, transparent
> production target after chroma removal. No muzzle flash, no impact and no
> unrelated ammunition.

### Impact

> Frames of one object-owned impact family only. Physical paper effect tokens,
> consistent with the exact projectile material and force. Stable center, clear
> growth and settle phases, no realistic particles.

### Debris

> Up to eight isolated independently cut debris pieces from exactly one material
> family belonging to the approved object: varied mass and outline, no rectangular
> grid slicing, no complete miniature ruin.

## 15. Manifest minimum

Every runtime manifest declares:

- `schemaVersion`;
- `pipeline: layered-object-v2`;
- `objectId`;
- `familyId`;
- atlas image, pixel size and byte size;
- tight sprite rects;
- `pivotPx` and normalized pivot;
- `drawOrder`;
- attachments and parent relationships;
- footprint lock;
- animations, duration, loop and hold;
- active mechanism behavior;
- projectile spawn and behavior;
- destruction inventory;
- owner overlay metadata where relevant;
- source provenance;
- visual, technical and animation QA states.

No runtime reader may infer fixed cells from a review grid.

## 16. Required review outputs

For every approved object family:

- compact transparent runtime atlas;
- JSON manifest;
- separate labeled review grid;
- assembled composite preview;
- idle proof;
- aim proof if applicable;
- attack and projectile proof;
- impact proof;
- destruction proof;
- validation report;
- localhost QA view using actual atlas and manifest.

Review labels, grids, pivot crosses and assembled previews never enter runtime.

## 17. Production order and gate

1. Approve neutral material/projection baseline.
2. Approve Watchtower projection master.
3. Approve Watchtower decomposition and runtime package.
4. Continue in the order maintained by the authoritative family specification.
5. Stop after each object for visual and technical confirmation.

No production object begins while the material baseline remains unapproved.

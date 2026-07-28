# Entity Codex v3

Status: canonical content bible  
Updated: 2026-07-23

## Reading key

- **Runtime:** currently represented by combat logic in `game/game.js`.
- **Planned:** present in production design but not yet fully implemented in the
  browser prototype.
- Runtime IDs remain stable even when the canon display name changes.

Every layered object uses true top-down 90° projection and separately cut
cardboard parts. Descriptions below define identity and gameplay, not permission
to bake the whole object into one sprite.

## v4 lore integration overlays

The expanded Daariya/Antlan canon does not authorize silent creation of new
runtime IDs. Until a mechanic and production contract are approved:

- League of Empty Measure troops use mission-specific identity overlays on
  compatible existing functions, especially `raider`, `necro`, `spellbreak`,
  `machine` and `iron_jug`;
- Antlan Drowned Circuits use `machine`, `iron_jug` and `bossMachine` mechanics
  with owner-specific visual modules;
- Grey/Lelya forms continue to use `witch_doc`, `bomber`, `spellbreak`, `scout`
  and `machine`;
- no human skin color may be used as a faction or hostility marker;
- overlay modules must remain separately named cardboard layers and may not
  erase the base entity's required silhouette or animation contract.

If a League or Antlan concept requires behavior that these IDs cannot express,
it remains planned until a new gameplay definition is approved.

# 1. Player characters

## `paladin` — Громовик Заставы

**Status:** Runtime.

**Appearance:** A broad readable human silhouette in lamellar cardboard plates
over a quilted field jacket. Burgundy and warm-white shield, copper conductors
and a compact thunder hammer. The design combines an ancient oath-guard and a
Kitezh electrical technician without copying historical armor or a superhero.

**How it works:** Enters the Defense Record temporarily after tower kills charge
enough free connections. Fights near the base, adds shield charges immediately
and continues restoring protection in pulses.

**Lore function:** Represents Perun's contract: a border is real only while
someone openly accepts responsibility for holding it.

**Animation layers:** locked body/feet, separate shield, hammer swing, copper
contact spark, shield-charge rings and return-to-base marker.

## `mage` — Волхв Архива

**Status:** Runtime.

**Appearance:** Narrow dark-blue working coat, birch-bark and paper bookmarks,
oxidized copper measuring ring and several small cold-blue sign cards. His face
may briefly show different ages, but the gameplay silhouette remains stable.

**How it works:** Temporarily enters the field, grants one shield and slows
enemies. Passively increases resource-building yield and Watchtower perception.

**Lore function:** Reads alternative versions of a line before one becomes
dominant. His slowing effect forces each enemy step to be revalidated by the
Record.

**Animation layers:** body, copper head ring, rotating bookmarks, casting cards,
slow-field rings and small archive-glyph fragments.

## `hunter` — Следопытка Амура

**Status:** Runtime. Canon narrative identity: Marья Лыткина.

**Appearance:** Practical taiga clothing in pine green, bark tan and river
blue-grey; short bow, rope, birch-bark tool box and a separate falcon marker.
No copied ceremonial costume.

**How it works:** Enters the wave, wounds enemies around the base and adds a
shield. Passively gains more reward from infantry and strengthens towers' first
attacks.

**Lore function:** Reads the physical witnesses ignored by abstract archives:
tracks, current, wind, disturbed roots and animal behavior.

**Animation layers:** body, bow, arrow, falcon token, ranging mark, thorn burst
and returning trail.

# 2. Core placeable objects

## `watchtower` / `fire` — Дозорная весь

**Status:** Runtime; first production baseline.

**Appearance:** Compact irregular stone-card lookout ring with a radial timber
deck, two access cuts, one small central plan-view crossbow, muted red signal
cloth and amber lantern. It must resemble a working watch post, not a plain
round token and not a large crossbow with scenery.

**How it works:** Baseline ranged defense. Fast enough to handle early troops,
upgradeable into anti-infantry, anti-air or artillery lineages.

**Lore function:** The simplest complete defensive sentence in the Record:
someone watches, names a target and sends a physical bolt.

**Layers:** base/body, bearing, crossbow, bolt, flag, lantern/glow, muzzle token,
impact, stone/wood debris.

## `sawmill` / `ice` — Плотницкая артель

**Status:** Runtime.

**Appearance:** Top-view timber work yard occupying a forest cell: log bed,
separate saw wheel, belt, beam frame, compact storage and sawdust cards.

**How it works:** Does not attack. Produces Living Wood after each wave and opens
adjacent reconstruction space. When removed, the forest version of the cell can
return through regrowth.

**Lore function:** Converts flexible biological memory into beams, tethers,
weapon arms and replaceable cardboard bodies.

**Layers:** yard base, log stack, saw, belt/gears, sawdust loop, small smoke,
destroyed beams and regrowth marker.

## `quarry` / `storm` — Каменная артель

**Status:** Runtime.

**Appearance:** Open top-view pit with irregular memory-stone blocks, radial
derrick foot, independent pick arm, pulley, basket and dust tokens.

**How it works:** Produces Memory Stone after every wave and opens nearby cells.
It can only be placed on a stone deposit.

**Lore function:** Extracts forms stable enough to support heavy mechanisms and
high-level reconstruction.

**Layers:** pit/base, block piles, pick arm, pulley, basket, dust, rubble and
broken derrick.

## `palisade` / `thorn` — Лешачий плетень

**Status:** Runtime.

**Appearance:** Reinforced living-wood ring or wall footprint with a clear stake
rhythm, root socket, independent thorn arm, vines and a few leaf layers.

**How it works:** Rapid anti-infantry defense. Strong against ground troops,
weaker against air and machines.

**Lore function:** Persuades the map's living routes to reject unfamiliar feet.
Named after the forest's capacity to confuse paths, not a literal trapped deity.

**Layers:** locked stake body, thorn arm/pivot, vines, pulse, stake projectile,
splinter-vine impact and wood debris.

## `obelisk` / `void` — Камень Велеса

**Status:** Runtime.

**Appearance:** Low ritual receiver holding a dark wooden-stone fragment with
gold-ochre record bands. It is a broad top-view plate, never a tall monolith.

**How it works:** Slow armor-breaking attack with high damage against machines.
Its effect interrupts the relation between a machine and its controlling line.

**Lore function:** A secondary fragment of the root record governing names,
exchange and transitions between states.

**Layers:** receiver, active fragment, bands, pulse cards, branching interruption
token, machine-fracture impact and stone/wood debris.

## `beacon` / `sun` — Круг Дажьбога

**Status:** Runtime.

**Appearance:** Wide radial solar construct with ochre-gold lens, four or more
separate shutters and restrained amber rays. No lighthouse facade.

**How it works:** Long-range anti-air defense. Reveals and strikes flying or
partially detached forms.

**Lore function:** Applies the principle of manifestation: what is measured in
light must accept a position in Yav.

**Layers:** dais, lens, shutters, rays, sun-bolt, halo impact, lens fragments.

# 3. Watchtower specialization lineage

## `ranger` — Стрелецкий приказ

**Status:** Runtime specialization.

**Appearance:** A staffed/refitted firing platform with hunter-green fittings,
large bolt rack, magazine and optical range card. It must not reuse the complete
Watchtower body.

**How it works:** Anti-infantry branch: rapid attacks, repeated target marks,
execution damage and immediate target transfer after kills.

**Lore function:** A formal defense entry supported by trained witnesses rather
than a single watchman.

## `tracker` — Соколиный круг

**Status:** Runtime late subtype.

**Appearance:** Regal blue and record-gold spotter construction dominated by a
large rotating optics ring and falcon-shaped target marker.

**How it works:** Greater range, priority for threats near the base and reliable
slowing of marked infantry.

**Lore function:** Tracks a target through several possible positions and
forces the world to retain the least favorable route for it.

## `assassin` — Тихий омут

**Status:** Runtime late subtype.

**Appearance:** Low broken silhouette with radial dark shroud pieces, concealed
heavy bolt cradle and small critical lens. No large generic muzzle flash.

**How it works:** Prioritizes elite infantry, raises execution threshold and
creates periodic critical hits.

**Lore function:** Removes a hostile form by finding the one unsupported line
on which all its other claims depend.

# 4. Heavy anti-air lineage

## `ballista` — Перунов самострел

**Status:** Runtime specialization.

**Appearance:** Reinforced cold stone and faded steel emplacement built around a
huge single swivel bow, heavy bolt storage and copper tracking lens.

**How it works:** Long-range anti-air branch. Heavy bolts pierce targets, punish
new targets and slow flight.

**Lore function:** Grounds the open sky through a named trajectory and a
Perun-style enforcement of boundary.

## `scorpion` — Змеиный гарпун

**Status:** Runtime late subtype.

**Appearance:** Harpoon carriage with a defining segmented counterweight tail,
chain/tether spool and asymmetrical execution head.

**How it works:** Massive single-target damage to durable flyers and prolonged
wing breaking.

**Lore function:** Forces a flying enemy to share a connection with the ground,
making its detached version unsustainable.

## `hailstorm` — Стрибожья метель

**Status:** Runtime late subtype.

**Appearance:** Wide fan-loaded repeater, several small limbs, a visible string
drum and settling bolt rack.

**How it works:** Pierces and distributes damage through swarms; gains rate
against many weak air targets.

**Lore function:** Uses the Stri-bog principle of direction and multiplication:
one release becomes many paths.

# 5. Siege-artillery lineage

## `cannon` — Гром-батарея

**Status:** Runtime specialization.

**Appearance:** Ramshackle stone-timber recoil carriage, long copper-dark barrel,
Kitezh inventory plate, rails, fuse and shell cradle.

**How it works:** Area damage and anti-machine specialization with armor break,
slow and limited infantry stun.

**Lore function:** Reconstructed from ancient thunder craft and site equipment.
Its shell does not merely dent armor; it makes neighboring machine parts
temporarily disagree about belonging to the same object.

## `mortar` — Медвежья ступа

**Status:** Runtime late subtype.

**Appearance:** Compact armored platform with a broad concentric tube mouth,
heavy shell rings and bear-paw support geometry. The name evokes the familiar
mortar/ступа archetype without copying Baba Yaga imagery.

**How it works:** Slow maximum armor-piercing fire against machines, with deep
charges and repeated siege blows.

**Lore function:** Sends a weight outside the target's expected line of sight,
then forces it back into Yav from above.

## `grapeshot` — Семистрельный раскат

**Status:** Runtime late subtype.

**Appearance:** Seven short barrels in a readable top-view fan, synchronized
breech ring and separate pellet hoppers.

**How it works:** Wider area, stronger regional slow and improved fire rate.

**Lore function:** Seven imperfect reports agreeing on one location become more
convincing than one precise report.

# 6. Hero-specific buildings

## `pal_ward` — Перунов круг

**Status:** Planned.

**Appearance:** Low ivory/copper ward plate with four independent contact points
and a rotating inner sign.

**Function:** Support aura and periodic shield pulse; no projectile.

**Lore:** Extends the Gromovik's accepted responsibility to nearby models.

## `pal_censer` — Жаровня Сварога

**Status:** Planned.

**Appearance:** Radial forge-censer construction with four hanging heat bowls,
chain arcs and separate ember cards.

**Function:** Fires compact white-gold heated projectiles and creates a small
burning impact area.

**Lore:** Converts damaged material into a renewed form through controlled heat.

## `pal_reliquary` — Ларец предков

**Status:** Planned.

**Appearance:** Squat armored archive chest with shutters, amber memory core and
several inscribed witness plates.

**Function:** Heavy support/smite structure with stun detonation.

**Lore:** Makes a defense stronger by adding named prior witnesses rather than
an anonymous sacred relic.

## `mage_frost` — Студёная печать

**Status:** Planned.

**Appearance:** Snowflake-like plate, concentric cold conductors and a separate
cluster of blue-white paper crystals.

**Function:** Area slow and frost impact.

**Lore:** Reduces the number of valid next positions available to a moving form.

## `mage_tesla` — Катушка Перуна

**Status:** Planned.

**Appearance:** Top-view copper coil rings around an archive-blue core, with
enamel insulators and discrete lightning cutouts.

**Function:** Chain lightning against grouped enemies.

**Lore:** Kitezh engineers' attempt to express the Perun principle as a measured
electrical circuit.

## `mage_prism` — Призма Прави

**Status:** Planned.

**Appearance:** Broad multi-facet paper prism in a low receiver, rotating splitter
plates and a blue-ochre core.

**Function:** Refracts one attack into several related targets.

**Lore:** Demonstrates that one cause may support several outcomes without
making them identical.

## `hunt_snare` — Леший силок

**Status:** Planned.

**Appearance:** Camouflaged bramble ring, hidden trigger plate, trip cord and
separate closing vine jaws.

**Function:** Ground trap, immobilization and thorn burst; no projectile.

**Lore:** Rewrites a few steps of the path so the target repeatedly returns to
the same local decision.

## `hunt_roost` — Соколиная вышка

**Status:** Planned.

**Appearance:** Timber and rope marksman platform with radial canvas, heavy
hunting bow, optical marker and separate falcon.

**Function:** Precision long-range attacks and critical target marking.

**Lore:** Uses an animal witness whose perception is not encoded in Grey
prediction models.

## `hunt_hive` — Осиный короб

**Status:** Planned.

**Appearance:** Birch-bark box and gnarled stump footprint with readable comb
cells, toxin reservoir and separate insect-cloud tokens.

**Function:** Poison projectile and lingering damage area.

**Lore:** A compact ecosystem whose many small agents are difficult to erase as
one named target.

# 7. Strategic objects

## `castle` — Китеж-17

**Status:** Runtime base; full layered package planned.

**Appearance:** Large unique top-view footprint combining ancient timber/stone
Zastava, late-Soviet enamel blocks, antenna foundations, cable trenches and the
central Veles stone. It is not a medieval castle with a Soviet decal.

**How it works:** Player objective. Enemy breaches remove shields and then
stability. Hero guides manifest from its control table.

**Lore function:** Last operational junction between the root record and Yav.

**Layers:** foundation, ancient sections, lab sections, control core, markers,
signals, damage/breach modules and large debris.

## `spawn_cave` — Разлом Пекла

**Status:** Runtime spawn point; full layered package planned.

**Appearance:** Jagged top-view tear across several terrain-card layers, with
clay, indigo and pale-grey internal strata. Not a front-facing cave arch.

**How it works:** Opens in pulses and produces enemy waves on one or two paths.

**Lore function:** Pressure wound between the Lower City, damaged Nav and Yav.

**Layers:** torn rim, opening, pulse frames, faction-specific spawn flare,
veins, rock/paper debris.

# 8. Ordinary enemies

## `fast` — Псоглавые бегуны

**Status:** Runtime.

Lean low-running Lower City beasts with grey-green fur/scale mix, bone collar and
red clan marks. They are fast, fragile and punish slow defenses. Their breeding
line was designed to carry a minimal identity that the road can validate
quickly.

## `warrior` — Ящеры-ратники

**Status:** Runtime.

Baseline upright reptilian infantry with clay-dark scale, short weapon, woven
shield and broken-spiral Lower City sign. Balanced health and speed. They are
citizens under levy, not mindless monsters.

## `brute` — Болотные тяжеловесы

**Status:** Runtime.

Large amphibious caste with broad body, layered mud armor and a stone/wood club.
Slow, durable pressure unit. Their wet skin and sediment hold several local
terrain claims, making them harder to erase.

## `raider` — Похитители имён

**Status:** Runtime.

Small asymmetric lizards carrying blank tags, hooks and stolen survey plates.
They can leave the road briefly to attack resource and defense objects. Each
stolen label lets them claim that a nearby cell is part of their route.

## `witch_doc` — Серые наставники

**Status:** Runtime.

Slender pale shells with oversized lens eyes and two or three floating control
cards. Ranged/support identity. They direct Lower City units by offering
optimized futures and suppressing contradictory responses.

## `slime` — Навья жижа

**Status:** Runtime.

An irregular indigo-smoke mass made from overlapping incomplete paper shapes,
with traces of eyes or tools that never form a complete body. Slow and
moderately durable. It fills missing definitions by occupying any available
shape.

## `berserker` — Красногребневые

**Status:** Runtime.

Fast assault lizards with a bright dried-red crest, light bone plates and twin
cutting tools. Higher aggression and speed than common warriors. Their battle
ritual intentionally narrows identity to one command: reach the heart.

## `shield` — Панцирники

**Status:** Runtime.

Broad Lower City infantry carrying a layered shell shield that covers most of
the top silhouette. Slow tank unit. Multiple named shell plates act as redundant
witnesses, making low-pierce attacks ineffective.

## `tunneler` — Подкопники

**Status:** Runtime.

Low digging caste with shovel-claws, survey whiskers and soil-card debris.
Raid-capable and route-bending. They follow forgotten service lines below the
visible road.

## `necro` — Писцы Нави

**Status:** Runtime.

Tall incomplete figures wrapped in blank record strips, carrying a split stylus
or frame. They create or restore empty copies of lost units. Their power is not
raising corpses but repeating a form after removing its personal links.

## `bomber` — Малые виманы

**Status:** Runtime.

Pale Grey flying plates centered on one dark lens, with two separate suspended
charge pods. Fast air raiders. Their apparent smoothness is printed on layered
cardboard; every pod and shutter remains a child piece.

## `spellbreak` — Глушители знаков

**Status:** Runtime.

Compact Grey agents carrying rectangular interference frames. They suppress or
weaken named defense effects. Visually distinguished by an incomplete pale
square crossing the body.

## `spider` — Всадники-тенётники

**Status:** Runtime.

Lower City rider on a broad cave arachnid, with radial legs and tether spools.
Fast raid pressure. The web temporarily supplies alternative connections across
cells.

## `summoner` — Проводники Пекла

**Status:** Runtime.

Heavy damaged-Nav casters built around a small tear token and several orbiting
empty silhouettes. They open local incursion points or add bodies to a wave.

## `golem` — Курганники

**Status:** Runtime.

Large bodies assembled from stone slabs, bones, archive boxes and missing-name
cards. Slow boss-tier durability. Each component belongs to a different
abandoned story, so the whole remains stable after individual impacts.

## `air` — Крылатые ящеры

**Status:** Runtime.

Lean plan-view reptilian flyers with broad membrane wings, harness plates and
Lower City markings. Fast air pressure and raid capability. They use old
ventilation shafts and thermal seams from the opened city.

## `wraith` — Беспамятные

**Status:** Runtime.

Smoke-white and indigo humanlike cutouts with the center deliberately missing.
They hover because the Record cannot assign their feet to a place. They are
people or workers whose names were erased, not a separate evil species.

## `scout` — Серые наблюдатели

**Status:** Planned runtime gap: sprite/action metadata exists, `enemyDefs`
registration and final behavior do not.

Small pale Grey shells dominated by one rotating observation lens. Intended to
scan defense rhythm, increase following-wave accuracy or reveal targeting
priorities. Must receive a distinct gameplay mechanic before implementation.

## `machine` — Колесницы Серых

**Status:** Runtime.

Captured Kitezh tracked or wheeled platforms with faded enamel, optical frame,
cables and invasive pale ceramic. Machine-category raider. They exploit old
service permissions to approach work sites.

## `iron_jug` — Железные идолы

**Status:** Runtime.

Heavy walking amalgams of crane parts, armored panels, copper bus bars and Grey
joints. Slow super-tanks. Their directive plates contain redefined protection
orders from Kitezh-17.

# 9. Bosses

## `miniBossGround` — Воевода Нижней Чешуи

**Status:** Runtime.

Large disciplined Lower City commander with layered clan plates and signal
blade. Tests early anti-armor and target priority. Represents the organized
military will behind initial incursions.

## `bossGround` — Князь Ящер

**Status:** Runtime.

Armored but articulate ruler with a split treaty plate on his chest. Main ground
boss of Chapter I. He begins as an enemy seeking the city's name and can become
a conditional ally after learning of the Grey substitution.

## `bossAir` — Трёхглавый Змей Неба

**Status:** Runtime.

Huge radial flyer with three separately animated heads and layered wings.
Created or bred as an airspace enforcement beast. Tests anti-air coverage across
multiple target points.

## `bossMachine` — Железный Змей Китежа

**Status:** Runtime.

Mobile reactor/antenna assembled as a segmented mechanical serpent. Separate
coils, dish, engine plates and tail modules create its silhouette. It broadcasts
the machine revision and tests artillery plus anti-machine magic.

## `dread_lord` — Кощей-Редактор

**Status:** Runtime boss ID; detailed multi-phase narrative mechanics planned.

Human director in a restrained grey suit surrounded by nested death containers.
Should lose one independent layer per phase: signal, container, tablet, line and
needle. He is the ideological antagonist, not a dark-armored fantasy warlord.

## `elder_dragon` — Великий Ящер Под Сопкой

**Status:** Runtime final boss ID; final multi-cell presentation planned.

Ancient stone-scaled being too large for one conventional sprite. Its segmented
body should occupy several linked map positions while preserving top-down
projection. It claims to be the Lower City itself; the final fight separates
the individual from the people and place it monopolizes.

# 10. Resources and environment

## `res_gold` — Злато договора

Conductive stamped token representing available authorization and released
reality capacity. Used for construction, heroes and upgrades. Warm ochre-gold,
never glossy treasure.

## `res_wood` — Живое древо

Bundled cut timber/bark icon with green growth line. Represents flexible
structure memory. Generated by the Carpenter Artel.

## `res_stone` — Памятный камень

Stacked blue-grey stone-card fragments with one inventory notch. Represents
stable geometry. Generated by the Stone Artel.

## `tree_oak` — Дуб памяти

Broad layered crown, visible trunk center and sparse witness tags. A forest
resource with strong stable local identity.

## `tree_pine` — Кедр рубежа

Dark pine/cedar crown built from several cut foliage levels. Distinct narrow
silhouette and Far Eastern environment identity.

## `tree_oak_grow`, `tree_pine_grow`

Growth strips show the Record returning a displaced forest version: root marker,
small shoot, layered young crown and mature resource. No magical pop-in.

## `rock_a`, `rock_b`, `rock_c`

Three silhouettes of fragments from the buried city: slab stack, river-worn
cluster and fractured worked block. They provide stone cells without repeating
one generic rock.

## `rock_grow`

Represents a stone version reasserting itself after temporary worksite removal:
outline, small fragments, joined cluster and restored deposit.

## `backgroud` — Оборонительная карта Китежа-17

Opaque battlefield scene combining taiga, pale service roads, cable trenches,
ancient foundations and the site's central control area. It is the only major
background asset; runtime objects remain movable transparent layers above it.

# 11. Common animation logic

## Enemies and heroes

- `spawn`: the Record validates or reconstructs the form.
- `walk`: movement along a witnessed path.
- `attack`: class-specific strike, shot, interference or summon.
- `death`: connections fail and the form separates into material layers.
- `breach`: the unit argues directly against the base record.
- `projectile`: separate for ranged owners and every direction where needed.

## Buildings

- `idle`: locked base plus independent ambient loops.
- `attack`: active child rotation/recoil plus owner FX.
- `destroy`: named parts lose attachment and become debris.
- `projectile`/`impact`: live in the owner atlas when unique.

## No unexplained parts

Every visible module must have:

- an object owner;
- a gameplay or recognition purpose;
- a material/cultural source family;
- an anchor and draw order if movable;
- an animation reason if it changes;
- a destruction behavior if the object can be removed.

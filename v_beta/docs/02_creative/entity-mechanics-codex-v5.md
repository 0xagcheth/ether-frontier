# Ether Frontier — Entity and Mechanics Codex v5

Status: **canonical coverage for current runtime and planned registered assets**  
Updated: 2026-07-24

## 1. Runtime resources

| ID | Canon name | Mechanical role | Styled form |
|---|---|---|---|
| `gold` / `res_gold` | Zlato of Accord | liquid build currency, enemy and wave reward | ochre punched agreement discs, stamped by several hands |
| `wood` / `res_wood` | Living Timber | upgrade and structural material | green-edged fibre cards with growth direction |
| `stone` / `res_stone` | Memory Stone | upgrade and bearing material | cool layered chips retaining load marks |
| lives | Bearing Names | base integrity, starts at 20 | twenty removable name tabs around the central Knot |
| hero charge | Communal Answer | tower kills needed to manifest hero | layered response segments filling an open ring |

## 2. Buildable runtime structures

### `fire` / `watchtower` — Wind Watch

- Cost: 45 Zlato.
- Role: baseline direct ranged defence.
- Stable footprint: low irregular stone ring and radial deck.
- Mechanism: one small central rotating crossbow used as a trajectory gauge.
- Animation: acquire, rotate, string draw, bolt release, reload, cloth flutter,
  lantern, hit and destruction.
- Lore: a temporary witness that says where a moving body actually is.
- Visual: sky-blue Wind route card, copper bearing arcs, quiet grey base.

Development:

- L2 chooses ground, air or machine answer.
- L3–5 deepens the answer.
- L6 chooses subtype.
- L7–9 subtype identity.
- L10–12 mastery: damage, range, cadence.

### `ice` / `sawmill` — Carpenter Circle

- Cost: 35 Zlato.
- Placement: forest only.
- Yield: 22 / 42 / 68 / 100 Timber per wave.
- Max level: 4.
- Opens adjacent cells.
- Roadside raid health: 12.
- Mechanism: large toothed paper saw, feed bed, belts and repair bench.
- Lore: receives temporary cutting rights and must enable regrowth.

### `storm` / `quarry` — Stone Circle

- Cost: 35 Zlato.
- Placement: stone only.
- Yield: 20 / 38 / 62 / 92 Stone per wave.
- Max level: 4.
- Opens adjacent cells.
- Roadside raid health: 12.
- Mechanism: open cut, low derrick, pulley, basket and sorting cards.
- Lore: lifts memory-bearing stone without destroying the cell's bearing.

### `thorn` / `palisade` — Root Weave

- Blueprint: 200 Zlato; build cost in runtime definition: 100.
- Limit: 4.
- Requires an existing Watchtower footprint.
- Role: rapid fire/control; ×1.5 ground, ×0.75 air, ×0.65 machine.
- Mechanism: spring roots and thorn launch tabs, not a crossbow.
- Lore: rewrites a straight attack route into a living boundary.

### `void` / `obelisk` — Name Stone

- Blueprint: 250; build definition: 125.
- Limit: 6.
- Requires a Watchtower footprint.
- Role: armour/command break; ×1.8 machine.
- Mechanism: stepped slabs around an absent centre, rotating name bridges.
- Lore: forces captured machines to reveal the missing owner relation.

### `sun` / `beacon` — Sun Measure

- Blueprint: 270; build definition: 135.
- Limit: 4.
- Requires a Watchtower footprint.
- Role: long-range anti-air; ×1.55 air.
- Mechanism: amber lens, reflector petals and separate beam cards.
- Lore: makes false sky bearings visible.

## 3. Wind Watch branches

### Ground answer

| Runtime state | Name | Mechanics | Unique mechanism |
|---|---|---|---|
| `infantry` | Wind Ranger | 44 base damage, fast cadence, ground only | compact rapid launcher and feed rail |
| L3 | Bird Mark | every third shot multiplies damage | rotating bird-path marker |
| L4 | Finishing Relation | +60% below 35% HP | threshold tab and heavy bolt |
| L5 | Passed Answer | immediate follow-up after kill | sliding two-target feed |
| `tracker` | Соколиный круг | more range and slow | open sight frame and bird marker |
| `assassin` | Тихий омут | high critical single-target damage | concealed torsion dart bed |

### Air answer

| Runtime state | Name | Mechanics | Unique mechanism |
|---|---|---|---|
| `air` specialization | Thunder Ballista | air only, long range, pierce | large tension arms and heavy bolt |
| L3 | Heavy Bolt | pierces targets | reinforced guide |
| L4 | First Bearing | +80% first hit | resettable sight plate |
| L5 | Broken Flight | slow | tether fragment |
| `scorpion` | Змеиный гарпун | strong single target, long slow | harpoon rail, drum and cable |
| `hail` | Стрибожья метель | multi-target swarm answer | fan channels and rotating feed drum |

### Machine answer

| Runtime state | Name | Mechanics | Unique mechanism |
|---|---|---|---|
| `siege` | Thunder Engine | splash, machine bonus | dark barrel, breech and recoil slide |
| L3 | Stone Cut | larger splash | fragment ring |
| L4 | Broken Directive | ×2 machine damage | directive-splitting charge |
| L5 | Dull Thunder | concussion slow | broad paper pressure wave |
| `mortar` | Медвежья ступа | slower, heavier arcing hit | short bowl tube and elevation cradle |
| `grapeshot` | Семистрельный раскат | larger suppression area | seven short charge channels |

## 4. Heroes

### `paladin` — Borislav, Thunder Keeper

- Recruitment: 150 Zlato after five waves.
- Active: enters until wave end and grants three base shields.
- Passive: 12% higher wave payment.
- Field attack: 38 damage, 42 range, 0.72 cadence.
- Visual: broad ochre-red paper armour, separate shield and hammer, three
  detachable copper Answer plates.

### `mage` — Ayana, Name Reader

- Recruitment: 210.
- Active: enters, grants one shield and globally slows enemies.
- Passive: worksites produce 15% more.
- Passive: Wind Watches gain range.
- Visual: indigo layered coat, separate reading cards, water-silver reflection
  field; no generic wizard robe or copied ritual costume.

### `hunter` — Amba, Pathfinder

- Recruitment: 180.
- Active: enters, grants one shield and periodically damages enemies near base.
- Passive: ground rewards +20%.
- Passive: first tower attack is stronger.
- Visual: pine and berry paper layers, separate bow, route strips, quiver and
  animal-track cards.

## 5. Enemy roster

The table contains nineteen implemented standard enemies and one planned
registered enemy, `scout`. Six bosses are listed separately.

All enemy display is cardboard/paper, but their material construction signals
allegiance. Lower-Serpent units use warm clay and shed-scale cards; Nav uses
torn translucent layers; Greys use pale repeated templates; captured machines
retain colourful craft under removable grey directives.

| ID | Canon name | Runtime role | Styled identity |
|---|---|---|---|
| `fast` | Lizard Sprinter | fast light ground runner; gains one interruptible road run-up | low marsh-and-clay lizard body, long rear legs, stabilising tail and separate route-obligation plate |
| `warrior` | Scale Retainer | baseline ground | practical scale cards and one clan-colour obligation plate |
| `brute` | Stoneback | slow durable ground; three sequential breakable armour plates | broad low lizard body with three large blue-grey back slabs |
| `raider` | Grey Breaker | ground melee; leaves Road only to strike first-row structures | hunched long-nosed Grey shell with one two-jaw physical clamp |
| `witch_doc` | Antlan Slinger | ground ranged; attacks first and second rows with a visible three-disc cycle | compact Antlan operator, one U-shaped measuring sling and one disc holder |
| `slime` | Nav Dew | slow incomplete ground form | translucent torn pools and detached droplets |
| `berserker` | Red Crest | fast rage pressure | escalating crest layers and exposed joint tabs |
| `shield` | Shell Keeper | armoured front | huge independent shell card and small body |
| `tunneler` | Pressure Digger | bypass/raid | digging claws, soil cap and emergence debris |
| `necro` | Caller of Missing Names | summon/control identity | torn witness tabs and Nav threads |
| `bomber` | Air Freighter | slow durable air target; one inertial buffer against ordinary slow | broad copper-and-turquoise Vaitmana with short wings, one stone ballast and pale owner plate |
| `spellbreak` | Answer Silencer | interruption identity | broken response-ring tool and mute field |
| `spider` | Thread Rider | raid/control | independent legs, spool and web overlays |
| `summoner` | Interval Opener | brings additional pressure | portable tear frame and emerging blank cards |
| `golem` | Barrow Form | slow armoured ground | individually stacked mound stones around empty centre |
| `air` | Vaitmana Courier | fast air runner; gains one interruptible folded-wing acceleration | simple copper-and-turquoise craft, two guide wings, one tail and a pale owner plate |
| `wraith` | Nav Trace | fast invisible ground runner; permanently revealed after first detection | torn empty-centre outline, two long legs and two direction fins |
| `scout` | Grey Needler | air ranged; attacks first or second row and slows the next physical projectile | narrow pale craft with long sensor nose, two short wings and one three-needle holder |
| `machine` | Captured Craft | machine raider | colourful original chassis under detachable Grey owner plate |
| `iron_jug` | Directive Shell | heavy machine | thick walking paper shell and repeated blank plates |

## 6. Bosses

| ID | Name | Narrative/mechanical test | Visual focus |
|---|---|---|---|
| `miniBossGround` | Red-Scale Voivode | first organised ground command | signal blade and contradictory treaty plates |
| `bossGround` | Prince of the Depths | dual-lane political turning point | large pressure armour, debt plate removable from body |
| `bossAir` | Three-Headed Sky Keeper | anti-air build test | three independent heads, wing layers and false bearing discs |
| `bossMachine` | Empty-Name Engine | machine/splash test and capture theme | stolen parts from several tower families around blank hub |
| `dread_lord` | Grey Conductor | final uniformity argument | restrained humanlike carrier surrounded by separate editing tools |
| `elder_dragon` | Awakened World Serpent | whole-build spectacle | enormous segmented plan-view body; not inherently evil |

## 7. Planned registered support structures

These exist in the asset and lore registry but are **not currently buildable in
`game.js`**:

- `pal_ward` — Thunder Boundary, protective ring;
- `pal_censer` — Sun Brazier, heat aura;
- `pal_reliquary` — Name Casket, protective memory;
- `mage_frost` — Water Mirror, slow;
- `mage_tesla` — Copper Roll, chain damage;
- `mage_prism` — Name Prism, beam split;
- `hunt_snare` — Root Snare, hold;
- `hunt_roost` — Falcon Roost, ranged support;
- `hunt_hive` — Swarm Box, poison;
- `castle` — Last Knot;
- `spawn_cave` — Interval Tear.

Their prompts may be prepared, but gameplay claims remain planned until code
implements them.

## 8. Map and environment

### Current board — Last Knot

- true top-down tabletop board;
- two northern Road entries;
- forked/rejoining ochre path;
- central low circular Knot, never a castle facade;
- dense resource cells;
- three blocked structural zones;
- forest, quarry and buried-layer variants.

### Resource environment

- `tree_oak`: broad named canopy, slow return;
- `tree_pine`: radial needle layers, faster return;
- `rock_a`: old pressure stone;
- `rock_b`: water-marked stone;
- `rock_c`: locally repaired Knot stone;
- growth frames: five visible stages, each separate from runtime review labels.

## 9. Skills and effects

Every gameplay effect must have an owner:

- bolt, dart, harpoon, shell, pellet, beam and root projectile belong to tower;
- impact, smoke, dust, shards, thread and glow belong to owner atlas;
- hero shield, slow dome and thorn pulse belong to hero family;
- Grey correction, Nav thread and serpent dust belong to enemy family.

No generic magic rune effect is shared simply to save art production.

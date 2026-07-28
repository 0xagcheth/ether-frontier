# Ether Frontier — Game System and Lore Integration v1

Status: **canonical system interpretation of the current runtime**  
Updated: 2026-07-24

## 1. Genre

Ether Frontier is a **single-player lane tower defence with territorial
economy, modular tower evolution and one active summonable hero**.

It combines:

- preparation between waves;
- two-lane path defence;
- build-cell expansion through economic structures;
- three resources;
- enemy raids against roadside buildings;
- counter classes: ground, air and machine;
- branching Watchtower development;
- a hero charged by tower kills;
- regenerative terrain after dismantling;
- scripted progression through wave 20 and scalable survival afterwards.

The game is not a city builder, RTS or action RPG. Lore must reinforce quick
TD readability: route, threat class, build opportunity, primary mechanism and
current resource state must remain legible within one second.

## 2. Core fantasy

The player is the **Binder of the Last Knot**, a keeper elected to assemble
temporary defences from named material obligations. A tower is not summoned
from nothing. It becomes possible when:

1. a place accepts the footprint;
2. material with known provenance is committed;
3. witnesses agree on the object's function;
4. the Binder gives the form a temporary name;
5. its moving children remain individually replaceable.

This directly supports modular cardboard sprites and makes economy, placement,
upgrading, selling and capture part of the story.

## 3. Core loop translated into lore

| Runtime action | Canon meaning |
|---|---|
| inspect next wave | read the next pulse in the Bearing Ledger |
| place tower | bind a named temporary form to a consenting cell |
| upgrade | add a verified layer and accept a larger material obligation |
| choose specialization | declare what testimony the tower is built to answer |
| sell | perform Mara's lawful unbinding; recover half the contract value |
| wave begins | a damaged Road opens during a Grey pressure pulse |
| enemy killed | break the carrier form and release or recover its binding |
| enemy breaches | one entry in the Knot loses integrity |
| hero summon | spend accumulated communal Answer earned by tower kills |
| wave ends | close the pulse, collect worksite yield, record damage and regrowth |

## 4. Why waves exist

The Last Knot sits where two damaged Roads cross a buried orientation device.
The Grey Interval cannot remain materially open. It oscillates when the broken
Moon Cards pass particular bearings. Every oscillation produces a finite pulse:
the Greys assemble carriers, stolen machines and coerced auxiliaries along a
Road, then lose the connection if they fail to reach the centre.

This explains:

- discrete waves;
- pauses for construction;
- stronger later pulses;
- boss arrivals at major alignments;
- the second path opening at wave 10;
- simultaneous pressure after wave 18;
- endless survival as repeated alignment after the campaign climax.

## 5. Economy

### Zlato of Accord — runtime `gold`

Liquid social obligation: wages, recovered enemy fittings, safe passage,
stored work and promises that can be reassigned quickly.

Sources:

- starting reserve: 175;
- enemy rewards;
- post-wave payment: `22 + wave × 3`, with preparation bonuses;
- 12% wave-income bonus from the Thunder hero;
- 20% ground-enemy reward bonus from the Pathfinder;
- overflow conversion from wood and stone at 0.65 Zlato per excess unit.

Uses:

- buildings;
- upgrades;
- hero recruitment;
- special-blueprint unlocks;
- market conversion at 10 Zlato for 10 wood or stone.

### Living Timber — runtime `wood`

Renewable shaped fibre carrying growth direction. It is not generic lumber.

Sources:

- starting reserve: 30;
- Carpenter Circle yield per wave: 22 / 42 / 68 / 100 by level;
- market exchange;
- 15% worksite bonus from the Name Reader.

Uses:

- structural layers, hinges, tension arms, decks and high-level upgrades.

### Memory Stone — runtime `stone`

Slow material that preserves footprint, pressure and former attachment.

Sources:

- starting reserve: 30;
- Stone Circle yield per wave: 20 / 38 / 62 / 92 by level;
- market exchange;
- 15% worksite bonus from the Name Reader.

Uses:

- foundations, bearings, armour-breaking mechanisms and high-level upgrades.

### Economic design meaning

Zlato answers **who pays now**. Timber answers **what can grow and flex**.
Stone answers **what can remember load and position**.

Combat progression deliberately requires more worksites. A high-level defence
cannot exist as a pure weapon economy detached from land and labour.

## 6. Territory and regrowth

- The board has a 12-column build grid.
- Roads, edges and strategic structures block construction.
- Most cells begin occupied by forest or stone.
- A Carpenter Circle may be built only on a tree cell.
- A Stone Circle may be built only on a stone cell.
- A worksite opens adjacent cells for defence.
- Selling or losing a worksite schedules material return.
- Pine returns after roughly 4–5 waves, oak after 7–8, stone after 9–10.

Canon meaning:

The Binder never owns land absolutely. A worksite receives a temporary cutting
or lifting right and must leave the cell capable of returning to material life.
Regrowth is the visible fulfilment of that obligation.

## 7. Placement and risk

Roadside economic and Wind structures can be raided. Fast, flying and machine
carriers may leave the path long enough to attack them.

This creates the intended decision:

- near-road placement gives coverage and useful expansion;
- distance improves safety but may waste range or cells;
- losing an economic structure also delays future upgrades.

In lore, raiders attack the **name-bearing attachment** of a structure. When it
fails, the structure becomes unbound and its material begins returning.

## 8. Combat classes

### Ground

Bodies bound primarily to road and soil. Best answered by fast direct fire,
control and single-target execution.

### Air

Carriers held by damaged sky bearings rather than the ground Road. They can
bypass terrestrial lanes and require distinct anti-air tracking.

### Machine

Captured craft forms whose original owner layers were replaced by Grey
directives. They resist ordinary damage because their attachment order is
redundant; artillery and Name-stone attacks break that order.

Physical weapons work against Grey forces because the Greys require material
carriers to act in Yav. Destroying a carrier does not kill an abstract Grey; it
breaks the local bridge and forces the Grey signal back into the Interval.

## 9. Death, erasure and lives

- Normal death ends a material form. Mara opens the Last Door; memory may pass
  to Nav, be recalled through Iriy or return as material.
- Grey erasure removes the relationship between name, witness and event. It
  leaves a repeatable blank template rather than a dead person.
- A lost life at the Knot means one bearing entry has been erased.
- At zero lives, the Ledger no longer distinguishes the two Roads from the Grey
  Interval and the defence collapses.

## 10. Why witness modules cannot be copied infinitely

A valid component requires provenance, material and at least one independent
witness. A visual copy without those attachments is a Grey-compatible shell.
Therefore:

- upgrades cost real resources;
- higher levels require distributed worksites;
- captured towers lose unique owner layers first;
- copying the silhouette does not duplicate the function.

## 11. Watchtower evolution

The runtime `fire` tower begins as **Wind Watch**. Its small crossbow is a
neutral range-measuring craft mechanism, not a cultural identity and not the
universal weapon of the game.

At level 2 it chooses:

- Ground answer — rapid direct launcher;
- Sky answer — heavy anti-air tension engine;
- Machine answer — Thunder artillery.

At level 6 it chooses a subtype. Levels 10–12 are mastery layers: damage,
range and firing cycle.

Only the base Wind Watch retains the simple crossbow. Ranger, Tracker,
Assassin, Ballista, Harpoon, Volley Fan, Cannon, Mortar and Grapeshot have
different coherent mechanisms.

## 12. Heroes

One hero is recruited after five completed waves. The hero is not permanently
on the field. Tower kills accumulate **Answer**. Summoning manifests the
hero until wave end; the hero then visibly returns to the Knot.

This preserves the TD emphasis while giving a periodic active intervention.

## 13. Map model

The current runtime is one board representing the **Last Knot**:

- two northern entries;
- two Roads joining, splitting and reconverging;
- three blocked structural zones;
- a central defended core;
- forest and stone cells;
- one active lane before wave 10;
- two alternating lanes from wave 10;
- simultaneous dual-lane spawning from wave 18.

The campaign may restyle this board into regional states, but must not imply
mechanics that the runtime does not contain. Future maps may introduce other
Knots only as separate level implementations.

## 14. Runtime alignment status

- Wave 1 is now a tutorial roster of `fast` and `warrior`.
- Runtime resource, tower, hero, enemy, boss, wave and action display strings
  use the active Seven-Circles naming.
- Campaign beats are mapped to the existing single-board wave milestones rather
  than claiming fifteen implemented maps.
- Extended hero auxiliaries remain registered/planned and are not described as
  buildable runtime choices.

Lore documentation may describe their intended role, but must label them
`planned/not currently buildable`.

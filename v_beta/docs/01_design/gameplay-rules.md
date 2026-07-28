# Ether Frontier — Gameplay Rules

Status: **canonical current-runtime rules**  
Updated: 2026-07-24

## Core loop

1. Inspect the next Grey pulse.
2. Spend Zlato, Living Timber and Memory Stone.
3. Place worksites, open adjacent cells and assemble defences.
4. Start the wave at 1x, 2x or 3x speed.
5. Counter ground, air and machine pressure.
6. Accumulate Communal Answer from tower kills and summon one hero.
7. Collect wave payment and worksite yield.
8. Repair, specialize, dismantle or reposition before the next pulse.

## Starting state

- 175 Zlato;
- 30 Living Timber;
- 30 Memory Stone;
- 20 Bearing Names/lives;
- two seeded Ветровых дозора;
- one active Road;
- no recruited hero;
- no unlocked special structures.

## Economy

- Carpenter Circle: forest only; yields 22/42/68/100 Timber per wave.
- Stone Circle: stone only; yields 20/38/62/92 Stone per wave.
- Worksites open adjacent build cells.
- Timber and Stone cap at 350.
- Overflow converts to Zlato at 0.65.
- Market converts 10 Zlato to 10 Timber or Stone.
- Dismantling returns 50% of invested Zlato.
- Removed worksites schedule forest or stone regrowth.
- High combat levels require minimum numbers of worksites.

## Towers

- Wind Watch: baseline direct ranged defence.
- Root Weave: rapid anti-ground/control.
- Name Stone: anti-machine and directive break.
- Sun Measure: long-range anti-air.

Wind Watch level 2 branches into ground, air or machine answer. Level 6 selects
a subtype. Maximum combat level is 12; maximum worksite level is 4.

Special structures replace an existing Wind Watch footprint and have build
caps.

## Enemies

- Ground: answered by fast direct fire, control and execution.
- Air: bypasses ground-road assumptions and requires anti-air tracking.
- Machine: resistant captured constructions best answered by artillery and
  Name Stone.
- Raiders may leave the Road to attack nearby worksites and Wind Watches.
- Bosses test one major counter class at reduced unit clutter.

## Waves and paths

- Waves are discrete Grey pressure pulses.
- Second Road becomes active at wave 10.
- Paths alternate from wave 10.
- Both paths may spawn simultaneously from wave 18.
- Scripted progression runs through wave 20.
- Later waves scale health and composition indefinitely.

Wave 1 is a tutorial roster of `fast` and `warrior`: Бегуны Глубин and Ратники
Чешуи.

## Hero

- One of three heroes may be recruited after five completed waves.
- A hero charges only from tower kills while not already active/returning.
- Required kills scale as `18 + floor(wave × 0.6)`.
- Summoned hero fights until wave end, then returns to the Knot.

## Stable mechanics

Lore changes display names, descriptions, visuals and campaign framing.
Runtime IDs and current balance remain stable until a separate gameplay change
is approved.

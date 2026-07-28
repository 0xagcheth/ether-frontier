# Gameplay Rules

## Core Loop

The player defends Grimhold by placing and upgrading towers, harvesting resources, controlling one hero, and adapting to waves of Goblin Horde enemies.

Core loop:

1. Read next wave threat.
2. Spend gold, wood, and stone.
3. Place or upgrade towers.
4. Start wave and respond with hero abilities.
5. Harvest rewards and repair strategy.

## Required TD Features

- Speed control: 1x, 2x, and 3x.
- Wave preview before commitment.
- Tower sell or rebuild flexibility.
- Pause-and-place support.
- Distinct tower counters: infantry, air, machine, support, economy.
- Hero abilities on clear cooldowns.

## Current Tower Roles

- Watchtower: baseline ranged tower.
- Sawmill: wood economy.
- Quarry: stone economy.
- Palisade: anti-infantry / physical control.
- Obelisk: anti-machine / captured magic.
- Beacon: anti-air / sun-seal magic.

Specialized tower paths should change both gameplay and silhouette. A stat-only upgrade is not enough for a major branch.

## Enemy Roles

Enemy types must create counter-pressure:

- Fast enemies punish slow single-target builds.
- Shield and brute enemies punish low armor-pierce.
- Air enemies require dedicated anti-air.
- Casters and summoners force target priority.
- Machines require heavy or magic-specific counters.
- Bosses test the full build, not one gimmick.

## Hero Rules

One active hero may be present on the map. Hero identity must support the fortress fantasy: bound wardens, oathbreakers, scouts, battle-mages, or similarly grounded medieval-fantasy roles.

## Source Material

These rules describe the intended design represented by the current `game/game.js` tower and enemy structure.

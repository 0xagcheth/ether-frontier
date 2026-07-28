# Ether Frontier — Seven Circles Object Redesign v1

Status: **canonical mechanics and prompt basis**  
Updated: 2026-07-26

## Decision

The previous prompt chain inherited familiar tower-defence weapons and then
renamed them for the Seven Circles. That approach is superseded.

Prompts now preserve only:

- exact true top-down orthographic 90-degree projection;
- matte paper and smooth solid punchboard construction;
- complete separation of physical children;
- stable pivots, attachments and directional states;
- animation-ready state coverage;
- readable mobile-game silhouettes.

No weapon, projectile, class role, upgrade tree or visual mechanism may be
inherited from an older prompt. Each object begins with a lore action and a
material process.

## The seven gameplay verbs

| Circle | Lore question | Gameplay verb | Physical process | Animation language |
|---|---|---|---|---|
| Root | What may return without becoming a copy? | regrow / bind / reopen | graft table, root loops, seed cards, repair ties | extend, take hold, release, regrow, scar |
| Stone | What can remember load and position? | anchor / redistribute / hold | witness slabs, counterweights, load cords, pressure seats | weigh, settle, transfer load, crack, reseat |
| Thunder | When may a shared answer interrupt force? | synchronize / interrupt / discharge | contact drums, timed clappers, copper answer bridges | contribute, align, strike, interrupt, cool |
| Sun | Which layer is present and which is imposed? | reveal / separate / restore colour | comparison shutters, amber measure, exposure cards | open, compare, expose, peel, close |
| Wind | Which route is possible now? | forecast / redirect / accelerate passage | route vanes, fork cards, tension ribbons, bearing table | sample, turn, choose fork, redirect, settle |
| Water | What must be shared, delayed or returned? | transfer / slow / cleanse | shallow channels, exchange cups, silver-paper flow strips | fill, divide, carry, return, dry |
| Name | Who owns this action and may revoke it? | identify / release / prevent copying | owner sockets, provenance tabs, absent centre, revocation thread | witness, attach, dispute, revoke, return tab |

These are not seven damage colours. A Circle may affect enemies, structures,
Roads, resources or the Last Knot without firing a projectile.

## Core runtime-facing objects

Runtime IDs remain compatibility handles until code is refactored. They no
longer define visual identity.

| Runtime handle | New object | Circle | New function | Removed inheritance |
|---|---|---|---|---|
| `watchtower` / `fire` | Wind Route Table | Wind | samples the next movement choice and rotates a temporary fork card, redirecting or delaying a limited group | crossbow, bolts, ammunition, attack cadence |
| `sawmill` / `ice` | Root Return Nursery | Root | restores exhausted living cells and grows temporary binding roots across a Road | sawmill, extraction fantasy, frost identity |
| `quarry` / `storm` | Stone Load Chorus | Stone | anchors a cell, redistributes pressure and makes heavy/captured units expose detachable layers | mine, damage shell, lightning identity |
| `palisade` / `thorn` | Water Exchange Weir | Water | divides movement into delayed and returned steps; washes one imposed layer from a nearby friendly object | wall, thorn launcher, poison trap |
| `obelisk` / `void` | Name Witness Table | Name | identifies owner layers, prevents duplication and releases a captured object after witness agreement | obelisk, void bolt, armour-breaking shot |
| `beacon` / `sun` | Sun Comparison Measure | Sun | reveals copied directives and temporarily restores the original layer beneath an overwrite | anti-air beam, holy beacon, projectile |
| `cannon` branch handle | Thunder Answer Drum | Thunder | stores contributions from different Circles and interrupts one hostile action when their timing aligns | cannon, barrel, shell, explosion |

## Combination upgrades

Upgrades combine verbs rather than replacing one weapon with another:

- Wind + Root: living detour that disappears after passage;
- Wind + Stone: route commitment that delays heavy carriers;
- Wind + Name: distinction between intended traveller and copied route;
- Stone + Thunder: synchronized load release that interrupts a machine step;
- Thunder + Water: distributed interrupt through connected cells;
- Sun + Name: imposed directive exposure and owner-tab return;
- Root + Water: exhausted-cell recovery without duplication.

No combination implies a bow, gun, mortar, magic beam or generic elemental
spell.

## Heroes

- Borislav does not attack with a hammer. He lends three revocable Answer
  plates to different Circles; agreement cancels one hostile action and the
  plates physically return.
- Ayana does not cast a generic global slow. She opens a comparison field where
  each step shows provenance; copied steps take longer and captured layers
  become selectable.
- Amba does not deal periodic bow damage. She lays a temporary witnessed route
  through damaged cells; enemies crossing it reveal their route obligation.

Hero tools are practical handling tools, never inherited damage sources.

## Enemy interaction grammar

- Lower-Serpent communities respond to debt, pressure, route and treaty state.
- Nav witnesses respond to incomplete names, return paths and release.
- Greys respond to exposure, provenance disputes and loss of duplicated layers.
- Captured machines respond to owner recovery, directive removal and load
  interruption.

Show interactions through removable cards, gaps, routes, pressure pieces and
changed assemblies, not colour-coded damage effects.

## Production gate

All v6 object prompts, the old Watchtower source plan and weapon-led object
families are archival. No source may be generated until its brief is derived
from this document and `asset-prompt-bible-v7.md`.

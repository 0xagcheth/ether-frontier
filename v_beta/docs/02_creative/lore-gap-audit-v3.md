# Lore and Content Gap Audit v3

Status: canonical audit  
Updated: 2026-07-23

## Result

The v2 reboot established a coherent premise, factions, campaign, characters and
display-name map, but it did not yet describe every gameplay behavior and
production asset in sufficient detail. This audit defines the remaining gaps and
their resolution.

## Covered before this audit

- Yav, Nav and Prav;
- origin and accident of Kitezh-17;
- the Book of Veles as fictional reality-editing language;
- Zastava, Lower City, Grey, damaged Nav and captured-machine factions;
- three heroes;
- three campaign chapters and three endings;
- all named tower/building IDs;
- all planned enemy and boss IDs;
- resource and environment naming;
- cultural-reference policy;
- cardboard tabletop presentation.

## Gaps found

### Conflict mechanics

The previous lore did not explicitly explain why enemies must follow roads, why
defense objects can be placed during battle, why waves pause, why selling a tower
restores terrain, why resources regrow or why the hero requires kills to enter.

Resolution: defined in `game-lore-bible-v3.md` as the laws of the Defense Record,
the pulse cycle of the Rift and the memory cost of reconstruction.

### Implemented versus planned content

The current browser prototype implements:

- 3 heroes;
- 6 directly placeable base objects;
- 3 Watchtower specialization branches with 6 late subtypes total;
- 20 ordinary enemy runtime IDs including `scout` art metadata but only 19 IDs
  currently registered in `enemyDefs`;
- 6 boss IDs;
- two enemy paths;
- gold, wood, stone, trees, rocks, growth, selling, raiding, hero shields and
  multi-wave progression.

The production documentation additionally plans:

- 9 hero-specific special buildings;
- owner-specific projectile, impact, destruction and ambient layers;
- `scout` as a full Grey Observer enemy;
- castle and spawn-cave layered runtime packages;
- multiple resource/decor variants and growth strips.

Resolution: the codex marks every entry as `runtime` or `planned`.

### Character relationships

The three heroes previously had identities but no personal reason to stay at the
site and no relationship with one another.

Resolution: the story and character sections define their roles in the 1977
accident, present-day return and dispute over the final choice.

### Enemy motivation

The factions had goals but individual combat classes lacked a reason to perform
their gameplay behavior.

Resolution: every enemy codex entry now ties speed, armor, summoning, raiding,
flight or machine status to a faction function.

### Economy

Gold, wood and stone had symbolic names but no operational origin.

Resolution:

- Contract Gold is authorization and recoverable energy-value stored in stamped
  conductive tokens.
- Living Wood holds flexible local memory and supports rapid reconstruction.
- Memory Stone holds stable geometry and unlocks advanced structures.

### Visual causality

The cardboard style was intradiegetic but not fully explained.

Resolution: the Defense Record cannot safely manifest full matter during a
reality conflict. It produces layered material models whose named parts act as
stable proxies. Moving parts must therefore exist as separate layers.

### Terminology

`Peklo` was used as a proper place without definition.

Resolution: Peklo is the operators' name for a damaged pressure layer between
Yav and the Lower City. It is not identical to Nav or a universal hell.

## Remaining production debt

- Rewrite every artistic prompt in the legacy `asset-prompt-bible.md`.
- Add `scout` to runtime enemy definitions when its gameplay behavior is chosen.
- Implement hero-special building mechanics or mark them cut before production.
- Author mission briefing, between-wave dialogue and ending scripts.
- Replace temporary symbolic marks in the browser UI with approved original
  faction icons.
- Produce a pronunciation and English-localization guide after Russian canon
  names are approved.

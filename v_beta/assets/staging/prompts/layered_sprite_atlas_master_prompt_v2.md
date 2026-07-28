# Ether Frontier — Layered Sprite Atlas Master Prompt v2

> **SUPERSEDED / DO NOT RUN (2026-07-26).** Projection, cardboard material and
> animation packaging remain useful; object identity and abilities do not.
> Rebuild from `seven-circles-object-redesign-v1.md` and
> `asset-prompt-bible-v7.md`.

Use this in a new production task only after gameplay concept art is approved.

## Mission

Create production-ready layered sprite atlases for Ether Frontier: **Seven
Circles of Iriy — Seven Roads of the Last Knot**, beginning with `watchtower` / **Wind Watch** and
advancing one approved object at a time.

## Read first

1. `docs/02_creative/game-lore-bible-v6.md`;
2. `docs/01_design/game-system-and-lore-integration-v1.md`;
3. `docs/02_creative/entity-mechanics-codex-v5.md`;
4. `docs/05_assets/asset-prompt-bible-v6.md`;
5. `docs/05_assets/production-prompt-catalog-v1.md`;
6. `docs/05_assets/object-family-and-variation-spec-v5.md`;
7. the current per-object layer contract;
8. `docs/05_assets/technical-asset-contract.md`;
9. `docs/07_pipeline/quality-gate.md`.

## Visual lock

- built-in ImageGen 2 by default;
- exact true top-down orthographic 90 degrees;
- premium handmade tabletop diorama;
- smooth solid punchboard and printed paper;
- complete die-cut perimeters, tan edges, gaps and compact contact shadows;
- attractive slightly cartooned proportions;
- primary gameplay mechanism is clearest and most saturated;
- lore through material, process and function;
- no glossy 3D, plastic, realism, facade, side view or tall perspective;
- no copied sacred signs, fake runes, racial coding or generic ornament.

## Layer lock

- stable base/body footprint;
- every rotating, moving, firing, glowing, burning, smoking, deforming or
  swappable part is a separate child;
- distinct gameplay mechanisms require distinct coherent masters;
- no universal crossbow;
- projectile, impact and unique debris belong to the owner atlas;
- captured states use detachable Grey directive layers;
- matching states preserve coherent geometry and attachments.

## Per-object sequence

1. verify runtime role and canon description;
2. write exact layer/action inventory;
3. generate one coherent assembled projection master;
4. remove chroma key to alpha;
5. obtain user visual approval;
6. generate structural master without animated children;
7. generate coherent mechanism masters and matching state edits;
8. extract named layers in one shared coordinate system;
9. validate alpha, clipping, margins and projection;
10. pack a compact transparent runtime atlas;
11. write manifest JSON as source of truth;
12. create a separate labelled review grid;
13. create a separate clean composite and animation preview;
14. verify size, tight rects, pivots, attachments, draw order and actions;
15. request object approval;
16. only then begin the next object.

## Runtime output

- one family per atlas;
- atlas no larger than 5 MB;
- compact transparent packed sprites only;
- no labels, grids, pivots or previews inside runtime;
- JSON owns rect, pivot, attachment, drawOrder and animation data.

## Baseline — Wind Watch

- low twenty-stone ring;
- eight-part radial timber deck;
- modest central lightweight crossbow on layered bearing;
- body, arms, strings and bolt separated;
- four copper contact arcs;
- sky-blue Wind route card;
- separate signal cloth;
- lantern casing, flame and glow;
- four-bolt rack;
- projectile, impact and material-specific debris;
- crossbow smaller than a dedicated Ballista;
- no facade and no old Kitezh/archive markings.

Stop after Watchtower visual and technical validation and show every QA
artefact for approval.

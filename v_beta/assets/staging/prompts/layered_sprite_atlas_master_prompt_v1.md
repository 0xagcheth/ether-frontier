# Ether Frontier — Master Prompt for Layered Sprite Atlas Production v1

Status: **prepared for a new Codex/ImageGen window; inactive until concept approval**  
Updated: 2026-07-24

## Copy everything below into the new window

You are beginning the production of all layered gameplay sprite atlases for
`Ether Frontier: Семь кругов Ирия`.

The sole lore canon is Option C, Seven Circles of Iriy. First inspect the
project documentation and approved concept references. Never infer canon from
old generated images or archived prompts.

### Required authority order

1. `v_beta/docs/00_project/source-of-truth.md`
2. `v_beta/docs/00_project/project-vision.md`
3. `v_beta/docs/02_creative/game-lore-bible-v5.md`
4. `v_beta/docs/02_creative/faction-bible-v4.md`
5. `v_beta/docs/02_creative/entity-codex-v4.md`
6. `v_beta/docs/02_creative/visual-cultural-source-map-v4.md`
7. `v_beta/docs/03_art/master-visual-style.md`
8. `v_beta/docs/03_art/environment-bible.md`
9. `v_beta/docs/05_assets/object-lore-material-overlay-v5.md`
10. `v_beta/docs/05_assets/asset-prompt-bible-v5.md`
11. `v_beta/docs/05_assets/object-family-and-variation-spec-v5.md`
12. `v_beta/docs/05_assets/object-module-registry-v2.json`
13. the current object's layer contract;
14. approved concept references registered in
    `v_beta/docs/05_assets/canon-asset-registry.md`.

If sources conflict, the higher source wins. Options A/B, Kitezh-17, secret
laboratory, archive stamps, facility codes, Goblin Horde, Grimhold and old
generated towers are forbidden.

### Work order

Work on exactly one object family at a time, starting with Watchtower /
`Ветровой дозор`. Do not proceed to another object until the user confirms the
current assembled concept and it passes every visual and technical gate.

For each object:

1. write or verify its lore/function contract;
2. list stable footprint, unique silhouette and all named physical layers;
3. list moving groups, pivots, attachments, drawOrder and animation tracks;
4. list owned projectile, impact, VFX and material-specific debris;
5. generate one assembled projection master;
6. remove chroma to alpha and validate margins;
7. obtain explicit visual approval;
8. generate/extract full-canvas aligned child layers;
9. build a compact transparent runtime atlas;
10. create manifest JSON as source of truth;
11. create separate review grid and assembled/animated browser proof;
12. validate size, tight rects, pivots, attachments, animation resolution,
    clipping, stable footprint and style.

### Generation model

Use built-in ImageGen 2 for every artistic raster source. Do not replace failed
generation with hand-drawn raster, SVG, another model or legacy art.
Deterministic tools may perform chroma removal, masking, cropping, packing,
manifest generation and QA. If ImageGen is unavailable, pause artistic
generation and continue only deterministic/documentation work.

### Projection and material

- true top-down orthographic 90°, camera directly overhead;
- compact horizontal footprint; no facade, side, rear, isometric or tall view;
- smooth solid premium board-game punchboard, never corrugated;
- matte cartoon print with visible fibers and paper tooth;
- thin tan cut edges, complete perimeter for every child, small separation gaps;
- compact contact shadow only onto the immediately lower layer;
- moderately saturated earthy color fields; no beige/grey wash;
- restrained original Seven-Circles accents on at most one or two secondary
  pieces;
- no glossy 3D, plastic, clay, photoreal miniature or flat vector substitute;
- no character baked into an object atlas;
- no terrain, labels, grid, pivot crosses or assembled preview in runtime atlas.

### Structural rules

- one family per atlas;
- runtime atlas PNG plus manifest must stay within the project's 5 MB limit;
- stable base/body footprint never changes during animation;
- every moving part is a separate child layer;
- weapon, cannon, crossbow, lens or crystal rotates as its own named group;
- cloth, flame, smoke, rune-like original accent, gear and glow animate as
  separate children;
- unique projectile, impact and debris belong to the owner atlas;
- code reads exact tight rects, explicit pivots, attachments, drawOrder and
  animation tracks from JSON;
- never infer pivot from rect center;
- related objects reuse only modules explicitly approved in the module registry;
- never give unrelated towers the same weapon by visual habit.

### Watchtower first gate

Read `v_beta/docs/05_assets/watchtower-layer-contract-v4.md`. The assembled
`Ветровой дозор` must be a low circular Wind-circle lookout with exactly twenty
separate stone parapet cards, exactly two opposite access notches, exactly eight
radial deck sectors, and one lightweight crossbow mounted directly on the
central rotating bearing. It also owns four copper bearing arcs, one burgundy
signal cloth, one amber lantern, a rack with exactly four bolts plus one empty
fifth slot, and one faded sky-blue repair card with a broken three-bend wind
path. The central bearing may not be empty and the crossbow may not sit beside
it. No archive mark, laboratory plate, copied rune or extra weapon.

### Review rule

Never mark your own generated concept approved. Show the assembled concept at
review scale, state every PASS/FAIL against the written contract, and wait for
explicit user confirmation. Only after confirmation promote it to approved
canon and begin decomposition.

The runtime atlas contains only transparent packed production sprites. Human QA
labels, grid, pivots, layer names and previews belong only to separate review
files and the animation website.

## End of master prompt

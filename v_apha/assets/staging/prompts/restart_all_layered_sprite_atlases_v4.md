# SUPERSEDED — do not use

This prompt depends on previous generated references and has been replaced by:

`assets/staging/prompts/restart_all_layered_sprite_atlases_clean_v1.md`

# Ether Frontier — restart all layered sprite atlases from zero

Use this prompt in a new Codex/ImageGen task to restart production of every
game-object sprite atlas from the beginning.

The first baseline object is Watchtower. After Watchtower passes visual and
technical QA, continue through the documented object order. Do not treat
Watchtower as the structural template for every other object.

## Role

You are producing production-ready layered sprite atlases for Ether Frontier, a
2D top-down tower-defense game with a handmade cardboard tabletop-board-game
style.

Work autonomously inside the project, but preserve a strict approval gate:

1. finish one object;
2. show its local QA site and review artifacts;
3. receive user confirmation;
4. only then begin the next object.

Do not generate several object families in parallel.

## Authoritative documentation

Read these files before generating anything:

1. `docs/05_assets/object-family-and-variation-spec-v4.md`
2. `docs/05_assets/restart-description-driven-object-pipeline-v3.md`
3. `docs/05_assets/modular-object-family-plan.md`
4. `docs/05_assets/object-module-registry.json`
5. `docs/05_assets/asset-prompt-bible.md`
6. `docs/03_art/master-visual-style.md`
7. `docs/03_art/sprite-bible.md`
8. `assets/staging/prompts/restart_layered_generation_from_watchtower.md`

Conflict priority:

`object-family-and-variation-spec-v4.md` wins over v3, old atlases, archived
assets, old prompts and current placeholder game sprites.

Gameplay code may confirm stats and attack behavior, but it does not override the
visual identity matrix in v4.

## Approved visual reference

Use this actual image as a visual reference for every initial projection-master
generation:

`assets/source/watchtower/wt-00-projection-master/watchtower_wt00_projection_master_v5_chroma.png`

Watchtower v5 defines:

- exact overhead board-game readability;
- light, slightly cartoon-like cardboard construction;
- convincing corrugated tan cut edges;
- matte painted paper and restrained crayon texture;
- thick imperfect hand-painted outlines;
- minor dirt, glue marks and rubbed corners;
- chunky child-cut shapes;
- small contact shadows between separately glued cardboard layers.

It does **not** authorize copying Watchtower's:

- circular body;
- crossbow;
- flag;
- lantern;
- stone arrangement;
- attachments;
- ammunition;
- effects.

For every ImageGen request, pass Watchtower v5 as an actual image reference, not
only as text.

## Absolute projection rules

- True top-down orthographic camera, `90°` directly overhead.
- Show horizontal top planes and only thin cardboard cut edges.
- No facade.
- No side or rear view.
- No isometric or three-quarter angle.
- No tall perspective.
- No doorway or staircase dominating an ordinary gameplay object.
- No realistic architectural wall faces.
- No glossy 3D, plastic or cinematic render.
- No baked terrain, grass, floor or environment.
- One centered object, fully visible with generous padding.
- Perfect flat removable `#ff00ff` chroma-key background.
- No labels, text, numbers, UI, watermark, QA grid or pivot crosses in source or
  runtime art.

## Cardboard construction rules

- Every visible structural piece should read as individually cut cardboard or
  painted paper.
- Use believable corrugated tan edges.
- Keep the overall illustration slightly cartoon-like.
- Crayon/paint texture must remain restrained; do not turn the asset into a
  photorealistic craft photograph.
- Add slight cut irregularities, dirt, glue marks and abrasion.
- Every glued child element gets a small local contact shadow on the layer below.
- Contact shadows belong between object layers only; do not cast shadows on the
  chroma-key background.
- Avoid excessive micro-detail that disappears at runtime scale.

## No characters inside building atlases

Do not bake people, rangers, operators, heads, helmets, hands, bodies or humanoid
figures into building sprites.

Descriptions such as `manned`, `staffed`, `garrison` or `crew position` must be
communicated through:

- empty firing sockets;
- ammunition systems;
- weapon rests;
- racks;
- painted position markings;
- barricades;
- faction fittings.

Characters, if ever required, belong to a separate character family and atlas.

## Object identity rule

Every object owns its complete readable silhouette.

Shared family membership may reuse:

- material swatches;
- validated connector scale;
- compatible attachment vocabulary;
- genuinely identical generic hardware;
- generic dust or debris when explicitly approved.

Shared family membership may **not** automatically reuse:

- visible base/body;
- weapon;
- projectile;
- ammunition storage;
- impact;
- unique animation children;
- destruction identity.

Upgrade lineage does not mean “same platform with a different weapon.”

Before image generation, write a per-object contract containing:

- gameplay role;
- owned base/body silhouette;
- primary mechanism;
- secondary modules;
- animation children;
- projectile and impact;
- destruction materials;
- explicitly allowed shared modules;
- explicitly forbidden inherited modules.

## Weapon placement

For every tower with a freely rotating primary weapon:

- the weapon rotation pivot is exactly at the geometric center of the tower;
- the weapon is a separate sprite;
- the central mount/socket is a separate sprite when it moves or detaches;
- optics attached to the weapon rotate with it;
- ammunition feeds must stop before the pivot and must not block rotation;
- no decorative center object may displace the weapon from the center.

Exceptions require an explicit object description stating that the mechanism is
fixed, off-center, radial, distributed or non-rotating.

## Mechanical and attack logic validation

Before accepting a projection master, trace this complete chain:

`storage → feed/reload → weapon → release → projectile → impact`

Every link must describe the same attack technology.

Examples:

- Crossbow → physical bolts, string/limb snap, bolt impact. No firearm flame,
  shell casing or gun smoke.
- Cannon → shells/cannonballs, breech/fuse, recoil, muzzle smoke and matching
  explosion.
- Mortar → heavy shells, top-view mortar mouth, high-arc launch, vent smoke and
  broad ground impact.
- Ballista → heavy bolts/harpoons, heavy arm snap and matching piercing impact.
- Magic lens/crystal → energy charge, magic projectile and matching magical
  impact. No physical shell rack unless the description explicitly requires it.
- Economy object → no attack projectile or combat muzzle effect.

Reject an object when:

- storage ammunition differs from the projectile;
- two storage systems duplicate the same role without explanation;
- feed rails do not reach the weapon;
- an optic looks like an unrelated decorative crystal;
- an attack effect belongs to a different weapon technology;
- decorative modules dominate or unbalance the intended silhouette.

## Projection-master-first gate

For each object:

1. Read its authoritative description.
2. Write its object contract.
3. Generate one assembled projection master at large scale.
4. Pass the approved Watchtower v5 as style/projection reference.
5. Inspect the result for projection, silhouette, mechanical logic and material.
6. Show the user the master.
7. Do not decompose it until the user confirms the silhouette.

Do not begin with a source sheet containing all modules. Do not squeeze many
small elements into one ImageGen canvas.

## Decomposition rules

After projection-master approval, derive large individual module images from the
same approved master:

1. stable `base_body`;
2. central socket/mount;
3. primary weapon or active mechanism;
4. optics/lenses/crystals;
5. ammunition stores and feed mechanisms;
6. flags, cloth, lamps, flames, smoke, gears, runes or glows;
7. projectiles;
8. impacts;
9. individual destruction pieces;
10. destruction dust/smoke/energy frames.

Generate or edit one large module at a time. Never regenerate an unrelated
replacement design during decomposition.

For every module edit:

- Image 1 is the approved object master or current edit target.
- Watchtower v5 is a style/projection reference only.
- Preserve the approved footprint, scale and attachment locations.
- Save chroma source first.
- Remove chroma locally into alpha.
- Validate the alpha before atlas packing.

If ImageGen returns a non-uniform chroma background, do not use an aggressive
despill pass that changes object colors. Mark alpha QA as failed and create a
dedicated matte.

## Stable footprint

- `base_body` owns the stable footprint.
- Idle and attack never change the base silhouette.
- Rotating or animated child layers must not alter the base rect.
- Destruction begins from the intact layered assembly.
- Never swap instantly to an independently drawn ruin with a different outline.
- Never use whole-object transparency as the main destruction animation.

Validate decomposition by comparing the master and base-body:

- center delta target: `≤ 1 px`;
- maximum outer-edge delta target: `≤ 2 px`;
- no clipping;
- identical scale and orientation.

## Animation rules

Every movable component must be a separate runtime layer.

Examples:

- weapon rotation;
- recoil;
- string/limb snap;
- optic movement;
- magazine motion;
- flags and cloth;
- fire and smoke;
- gears;
- runes;
- crystals;
- glows;
- projectiles;
- impacts;
- debris.

No baked full-object animation frames unless an explicit engine constraint is
documented and approved.

### Attack

- Play mechanism-appropriate release motion.
- Spawn the correct projectile from a named attachment point.
- Rotate projectile along velocity when appropriate.
- Play a matching impact owned by the firing object when unique.
- Do not use firearm muzzle flashes for bows or crossbows.

### Destroy

Use a staged one-shot sequence:

1. impact shake;
2. child modules detach;
3. ammunition spills or energy elements break;
4. weapon/mount separates;
5. base sections split and fall;
6. dust/smoke/energy settles;
7. all remaining parts disappear.

The object must conceptually break apart into its actual modules and
material-appropriate fragments. Do not:

- simply fade the whole object;
- replace it with another silhouette;
- split it into an obvious rectangular image grid;
- make all pieces move identically;
- loop destruction forever.

## Runtime atlas contract

One object family per atlas.

Required outputs:

1. `object_layered_runtime.png`
   - transparent;
   - tightly packed;
   - no labels, grid, previews or pivot crosses;
   - `≤ 5 MB`.

2. `object_layered_manifest.json`
   - source of truth for runtime;
   - exact tight rects;
   - pixel pivots;
   - normalized pivots;
   - parent/child attachments;
   - draw order;
   - animation clips;
   - duration, loop and hold behavior;
   - projectile/impact ownership;
   - destroy-piece inventory.

3. `object_layered_review_grid.png`
   - separate human-QA artifact;
   - labels and fixed cells allowed;
   - never loaded at runtime.

4. `object_layered_composite_preview.png`
   - separate assembled QA preview;
   - never loaded at runtime.

5. Animation proofs
   - idle;
   - aim when relevant;
   - attack;
   - projectile;
   - impact;
   - destroy.

Code must read rects, pivots, attachments, draw order and animations from the
manifest. Do not hard-code atlas cells.

## Local QA site

For each object, update or create a local QA site that:

- runs only on localhost;
- reads local atlas and manifest files;
- assembles the object from runtime layers;
- exposes idle, aim, attack, projectile, impact and destroy where relevant;
- provides play/pause;
- allows weapon-angle control;
- allows toggling individual layers;
- displays pivots, attachments and footprint;
- displays atlas size, byte size, rect and clipping checks;
- never substitutes screenshots for runtime composition.

Do not publish externally unless the user explicitly asks.

## Required validation

Visual:

- correct object identity;
- correct true top-down projection;
- coherent silhouette;
- Watchtower v5 material language;
- no baked characters;
- mechanically coherent attack chain;
- centered rotating weapon where required;
- no unrelated inherited module;
- no clipping.

Technical:

- RGBA atlas;
- transparent corners;
- no chroma fringe;
- all tight rects in bounds;
- correct pivots and attachments;
- stable footprint;
- valid draw order;
- animations reference existing sprites;
- runtime atlas contains no review graphics;
- one family only;
- file size `≤ 5 MB`.

Animation:

- weapon rotates around correct center;
- projectile visibly leaves the weapon;
- impact matches projectile;
- destroy breaks actual layers apart;
- no abrupt silhouette substitution;
- no whole-object fade as the primary destroy mechanism;
- destruction finishes and holds its final state.

## Object identity matrix

Always confirm details in v4 before generation.

- Watchtower: compact Warden post, simple central crossbow, flag, lantern, simple
  bolt.
- Garrison Ranger: compact garrison tower, central rapid-volley crossbow,
  symmetric short-bolt cassettes/feed, hunting optic, ranger-green fittings; no
  people.
- Crown Tracker: royal spotter tower, central precision long-bolt launcher,
  large rune optics, royal-blue/gold range markers.
- Shadow Archer: low shrouded sniper tower, central heavy sniper-ballista, dark
  fabric rim, critical lens.
- Fortress Ballista: reinforced anti-air tower, central huge heavy swivel
  ballista, heavy bolt rack, tracking lens.
- Sky Scorpion: harpoon tower with scorpion-tail counterweight and harpoon
  carriage.
- Hailstorm Ballista: central multi-bolt repeater fan with spinning string drum.
- Field Cannon: central long alchemical cannon on a stone/timber recoil carriage;
  physical shells and muzzle smoke.
- Siege Mortar: central top-view short broad mortar mouth, heavy shell stacks,
  vent smoke and broad ground impact.
- Grapeshot Battery: central radial/fanned multi-barrel cluster, pellet storage,
  broad flash and spread smoke.
- Palisade: reinforced living-wood defense with thorn/stake launching mechanism,
  splinters and vines.
- Obelisk: captured-void ritual construct with rotating/floating shard, rune
  bands and violet arcs.
- Beacon: sun-seal construct with central solar lens, halo shutters and radiant
  projectile.
- Sawmill: economy worksite with logs, saw wheel, belt/gears, sawdust and smoke;
  no projectile.
- Quarry: economy worksite with stone pit, pick/pulley mechanism, basket, rubble
  and dust; no projectile.
- Castle / Grimhold: unique strategic fortress, gatehouse/seal crystal,
  banners/braziers and breach pieces; no ordinary tower chassis.
- Spawn Cave: unique enemy portal with jagged cave rim, void vortex, veins,
  drips and spawn flare.

## Production order

Follow the family-first order from `modular-object-family-plan.md`, but treat
every visible body as object-owned unless v4 explicitly permits reuse:

1. Watchtower.
2. Garrison Ranger.
3. Crown Tracker.
4. Shadow Archer.
5. Fortress Ballista.
6. Sky Scorpion.
7. Hailstorm Ballista.
8. Field Cannon.
9. Siege Mortar.
10. Grapeshot Battery.
11. Ritual objects, beginning with Obelisk and Beacon.
12. Living-wood objects, beginning with Palisade.
13. Economy objects: Sawmill and Quarry.
14. Strategic unique objects: Castle and Spawn Cave.

Do not advance to the next item until the current item passes user visual
approval and technical validation.

## Image generation execution

- Use built-in ImageGen by default.
- If built-in generation/edit repeatedly fails, report the failure.
- Do not silently switch model or path.
- CLI/API fallback requires explicit user approval and secure reuse/creation of
  `OPENAI_API_KEY`.
- When CLI fallback is approved, prefer `gpt-image-2`.
- Run long CLI image jobs in a persistent terminal process and wait for the real
  completion message and saved output.
- Never assume a job succeeded merely because it printed `Calling Image API`.
- Never overwrite approved sources; save versioned files.

## First action

Start from Watchtower again.

1. Read its current description and v4 contract.
2. Use approved Watchtower v5 only as the visual baseline/reference.
3. Reconfirm or regenerate its projection master.
4. Decompose it into large independent modules.
5. Build runtime atlas, manifest, review grid, composite and local QA site.
6. Validate attack and conceptual layered destruction.
7. Show the complete Watchtower result for confirmation.
8. Only then continue to Garrison Ranger.

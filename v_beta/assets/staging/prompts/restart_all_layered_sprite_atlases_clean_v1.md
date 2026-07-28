# Ether Frontier — clean restart of all layered sprite atlases

Use this prompt in a new Codex/ImageGen task after removing all previous generated
object assets.

This is a clean production restart. Do not use, recover, copy, inspect, imitate or
reference any previously generated sprite, projection master, source sheet,
atlas, review image, composite, animation proof or archived candidate.

Project documentation is the only source of object identity.

## Role

Produce production-ready layered sprite atlases for every gameplay object in
Ether Frontier.

The game uses a handmade cardboard tabletop-board-game visual language and a
true top-down runtime camera.

Work on one object at a time. Finish its complete visual and technical pipeline,
show it to the user and receive confirmation before beginning another object.

## Required documentation

Before generating assets, read:

- `docs/05_assets/object-family-and-variation-spec-v4.md`
- `docs/05_assets/restart-description-driven-object-pipeline-v3.md`
- `docs/05_assets/modular-object-family-plan.md`
- `docs/05_assets/object-module-registry.json`
- `docs/05_assets/asset-prompt-bible-v4.md`
- `docs/03_art/master-visual-style.md`
- `docs/03_art/sprite-bible.md`

When documentation conflicts, use this priority:

1. `object-family-and-variation-spec-v4.md`
2. `restart-description-driven-object-pipeline-v3.md`
3. `modular-object-family-plan.md`
4. `object-module-registry.json`
5. `asset-prompt-bible-v4.md`
6. art and sprite guides
7. gameplay code

Old generated assets and archives never override the documentation.

## Clean-start rule

- Assume no approved visual object reference exists.
- Do not reuse old object silhouettes.
- Do not reuse old weapons, projectiles, effects or bodies.
- Do not inherit design decisions from deleted generations.
- Do not search archives for reusable art.
- Do not use old atlases as style references.
- Do not restore deleted candidates.
- Generate the new style baseline and every gameplay object from zero.

## First production deliverable

Before generating the first gameplay object, create a new neutral cardboard
material-and-style baseline.

The baseline must establish:

- dense smooth board-game punchboard edge treatment, with no corrugated flutes;
- matte cartoon-printed surfaces;
- restrained crayon-like character inside the printed illustration;
- outline thickness;
- child-cut irregularity;
- dirt, abrasion and glue treatment;
- local contact-shadow treatment;
- runtime readability at intended scale;
- exact top-down projection language.

The baseline must contain no gameplay object, weapon, character, building or
recognizable reusable silhouette.

Show the neutral style baseline to the user. Do not begin object production until
it is confirmed.

## Projection rules

- True top-down orthographic view.
- Camera directly overhead.
- Horizontal top planes are primary.
- Cardboard thickness appears only as thin cut edges.
- No facade.
- No side or rear view.
- No isometric or three-quarter camera.
- No tall perspective.
- No cinematic angle.
- No realistic architectural wall faces.
- No floor plane.
- No baked terrain.
- No glossy 3D.
- No plastic.
- No background cast shadow.
- Object fully visible with safe padding.
- Source generation uses a flat removable chroma-key background.

## Material rules

- The object must look constructed from separately cut pieces of cardboard and
  painted paper.
- Thin compressed tan paper-fiber edges must remain readable.
- Never show corrugated packaging flutes, wavy channels or shipping-box edges.
- `Smooth board-game punchboard` means solid rather than corrugated; it never
  means textureless.
- Fine paper fibers, pressed-pulp variation, faint tooth and small natural
  speckles remain visibly present on every exposed and printed face.
- Printed ink partially reveals the substrate grain beneath it.
- Surfaces are matte.
- The surface image reads as a cute, simplified cartoon print on cardboard.
- A controlled crayon-like graphic character may remain inside the print, but the
  surface must not look realistically hand-painted.
- Printed ornament is sparse and restrained, using original
  Slavic/Old-Russian-inspired geometric accents such as simple diamonds, stepped
  lines, small solar notches and short repeating border fragments.
- No ornate curls, filigree, baroque fantasy borders, all-over embossing, or
  copied sacred/historical symbols.
- Ornament density is low: only one or two secondary pieces per object may carry
  one small motif or one short border fragment. Most surfaces remain plain.
- Never repeat decorative motifs on every ring, plate, layer, module or edge.
- Restrained ornament does not mean restrained chroma: large printed color fields
  remain warm, clear and moderately saturated with strong faction separation.
- Matte means non-glossy, not faded, dusty, beige-washed or grey-hazed.
- Palette may evoke classic Warcraft III readability through saturated but earthy
  heroic colors: burgundy red, deep royal blue, pine green, golden ochre and dark
  warm wood, with warm-light/cool-shadow separation.
- This is palette guidance only. Never copy Warcraft faction markings, icons,
  silhouettes, ornaments, textures, props, interfaces or other identifiable art.
- Avoid pure primary RGB and plastic toy saturation.
- Reject perfectly flat vector fills, airbrushed plastic gradients, polished
  foam, rubber, clay and smooth textureless 3D-token surfaces.
- Use warm, clear, moderately saturated earthy printed colors assigned by the
  current faction and cultural-layer documents. Accents remain readable but do
  not revert to generic Western heroic-fantasy heraldry.
- Do not reduce the complete asset set to faded beige, dusty grey, washed-out
  craft colors or uniformly desaturated surfaces.
- The mood may evoke a classic fantasy RTS, but all symbols, ornaments, faction
  motifs and surface designs must be original to Ether Frontier.
- Shapes may have small handmade irregularities.
- Add restrained dirt, worn edges and glue marks.
- Each glued child piece casts a clearly readable compact soft contact shadow on
  the layer beneath it, following the attachment edge closely.
- Contact shadow alone is not enough: every child piece needs its own complete cut
  perimeter, thin solid-paperboard edge and tiny visible separation gap.
- A viewer must be able to count the physical cardboard layers at gameplay scale.
- Never represent separate parts only as colored regions printed on one flat base.
- Do not cast object shadows on the chroma background.
- Avoid excessive realism.
- Avoid excessive micro-detail that disappears at runtime size.

## No characters inside object atlases

Do not bake people, operators, workers, soldiers, heads, faces, helmets, hands,
arms, bodies or humanoid figures into building or gameplay-object sprites.

If documentation describes an object as staffed, operated, inhabited or manned,
express that only through object construction, attachment points, storage,
controls, markings or equipment.

Characters require a separate character specification and atlas.

## Object identity

Every object owns its complete visible identity.

For each object, determine from documentation:

- role;
- complete base/body silhouette;
- primary mechanism;
- secondary modules;
- moving parts;
- ambient animation;
- projectile or emitted effect;
- impact;
- destruction materials;
- allowed shared hardware;
- forbidden inherited hardware.

Do not assume that objects in the same upgrade tree share the same body.

Do not assume that every tower uses the same weapon.

Do not transfer a weapon, projectile, effect, ammunition system, optic, flag,
lamp, crystal, rune, gear or decoration to another object unless documentation
explicitly allows it.

Shared modules are permitted only when they are genuinely identical in role,
scale, material, attachment and behavior.

## Per-object written contract

Before image generation, create a written contract for the current object.

The contract must contain:

- object name and family;
- authoritative description sources;
- gameplay role;
- owned silhouette;
- footprint;
- central structure;
- primary mechanism;
- secondary modules;
- moving child layers;
- ambient child layers;
- projectile/effect ownership;
- impact ownership;
- destruction inventory;
- allowed reuse;
- forbidden reuse;
- required animations;
- visual validation checklist;
- technical validation checklist.

Show the contract to the user only when a material ambiguity cannot be resolved
from documentation. Otherwise continue to the projection master.

## Mechanical coherence

For every active object, validate this complete functional chain:

`storage or energy source → feed or charge → active mechanism → release → projectile or emitted effect → impact`

All stages must use the same technology and material logic.

Reject the design when:

- stored ammunition differs from the projectile;
- the active mechanism cannot use the shown ammunition;
- feed or charge elements do not connect logically;
- moving parts block one another;
- optics are unrelated decorations;
- effects belong to another weapon technology;
- duplicated modules have no distinct purpose;
- the attack cannot be understood from the object construction.

Non-attacking objects must not receive combat projectiles, muzzle effects or
weapon mechanisms.

## Rotating mechanism placement

When documentation defines a freely rotating central weapon or active mechanism:

- its rotation pivot is exactly at the geometric center of the object;
- the rotating mechanism is a separate layer;
- its mount/socket is a separate layer when technically required;
- attached optics rotate with it;
- feed paths stop before the pivot;
- no decorative part displaces it from the center.

Do not apply this rule to mechanisms explicitly documented as fixed, radial,
distributed, articulated or off-center.

## Projection-master gate

For each object:

1. Read the authoritative description.
2. Write the object contract.
3. Create one new assembled projection master.
4. Generate at large readable scale.
5. Include the complete functional construction.
6. Inspect projection, silhouette, materials and mechanical coherence.
7. Reject internally any result that violates the contract.
8. Show the first valid master to the user.
9. Wait for confirmation.
10. Only then begin decomposition.

Do not begin with a sheet containing every layer.

Do not squeeze many small modules into one generated image.

Do not decompose an unapproved silhouette.

## Decomposition

Derive every layer from the approved projection master.

Generate or edit one large module at a time.

Required categories when applicable:

- stable base/body;
- mount/socket;
- primary mechanism;
- optics or targeting device;
- ammunition or energy storage;
- feed or charge mechanism;
- ambient modules;
- animated child frames;
- projectile or emitted effect;
- impact frames;
- individual destruction pieces;
- destruction effects.

The stable base/body:

- owns the footprint;
- excludes every detachable and moving component;
- preserves the projection-master scale and orientation;
- contains only flat attachment zones or fixed sockets.

Target decomposition tolerance:

- center delta no more than one pixel;
- outer footprint delta no more than two pixels;
- no clipping;
- no unplanned geometry change.

## Layer rules

- Every independently moving element is a separate layer.
- Every rotating element has its own pivot.
- Every child layer has a named parent attachment.
- Keep draw order explicit.
- Keep the base footprint stable during idle and attack.
- Do not bake complete assembled animation frames into the runtime atlas.
- Do not include review labels, grids, previews or pivot crosses in runtime art.

## Attack animation

- Animate the actual release or activation mechanism.
- Spawn the correct projectile or emitted effect from a named attachment.
- Apply rotation along trajectory when appropriate.
- Use an impact consistent with the emitted object or energy.
- Do not substitute a generic attack flash belonging to another technology.
- Do not hide a missing projectile behind a visual flash.

## Destruction animation

Destruction must use the actual object layers and material-appropriate debris.

Required progression:

1. impact response;
2. detachable children separate;
3. stored ammunition or energy elements react;
4. active mechanism and mount separate;
5. body sections break apart;
6. debris moves with varied mass and direction;
7. dust, smoke or energy settles;
8. all remaining pieces disappear or reach the documented final state.

Forbidden:

- replacing the object with an unrelated ruin silhouette;
- fading the complete object as the primary destruction;
- dividing a sprite into an obvious rectangular grid;
- making every piece follow the same trajectory;
- abruptly removing child modules;
- looping destruction indefinitely.

## Source processing

- Save every generated source inside the project.
- Keep versioned source files.
- Do not overwrite approved sources.
- Remove chroma into alpha locally.
- Validate alpha corners, edges and coverage.
- Reject non-uniform chroma cleanup that damages object colors.
- Create a dedicated matte when ordinary chroma removal is unsafe.
- Do not pack an asset whose alpha has not passed QA.

## Runtime atlas

Produce one compact transparent runtime atlas per object family.

Requirements:

- tight packing;
- tight sprite rectangles;
- no fixed empty review grid;
- no labels;
- no text;
- no review composite;
- no baked terrain;
- no unrelated object family;
- maximum file size of five megabytes.

## Manifest

The JSON manifest is the runtime source of truth.

It must contain:

- schema version;
- object and family;
- atlas image and size;
- exact tight rectangles;
- pixel pivots;
- normalized pivots;
- semantics;
- draw order;
- parent/child attachments;
- active-mechanism behavior;
- projectile behavior;
- animation clips;
- timing;
- loop and hold behavior;
- destruction-piece inventory;
- source provenance;
- QA status.

Runtime code reads the manifest. Do not hard-code atlas cells.

## Review artifacts

Create separately:

- human-readable review grid;
- assembled composite preview;
- idle proof;
- aim proof when applicable;
- attack proof;
- projectile/effect proof;
- impact proof;
- destruction proof;
- technical validation report.

Review artifacts never enter the runtime atlas.

## Local QA application

Create or update a local-only QA site.

It must:

- run on localhost;
- read local atlas and manifest files;
- assemble the object from actual runtime layers;
- expose every relevant animation state;
- support play and pause;
- support angle control when applicable;
- allow child-layer visibility toggles;
- display pivots, attachments and footprint;
- report atlas dimensions and byte size;
- report missing sprites, invalid rectangles and clipping;
- never substitute screenshots for runtime composition.

Do not publish the QA site externally unless explicitly requested.

## Validation gate

Visual validation:

- correct documented identity;
- correct projection;
- coherent silhouette;
- coherent construction;
- coherent mechanical chain;
- correct materials;
- no characters;
- no inherited unrelated module;
- no clipping.

Technical validation:

- valid RGBA;
- transparent corners;
- clean alpha edges;
- all rectangles in bounds;
- correct pivots;
- correct attachments;
- correct draw order;
- stable footprint;
- valid animation references;
- one object family only;
- runtime atlas no larger than five megabytes;
- runtime contains no review graphics.

Animation validation:

- moving mechanism uses the correct pivot;
- projectile or emitted effect visibly leaves its source;
- impact matches the attack;
- destruction uses real layers;
- no abrupt silhouette substitution;
- no whole-object fade as the main destruction;
- animation reaches and holds its documented final state.

Do not begin another object until all three validation groups pass and the user
confirms the current object.

## Production order

Use the family-first production order defined in:

`docs/05_assets/modular-object-family-plan.md`

Resolve the exact object sequence from current documentation at runtime.

Do not hard-code an example order into this prompt.

## Image-generation execution

- Use built-in ImageGen 2 for all artistic raster generation by explicit user
  direction.
- Do not replace ImageGen 2 output with manually drawn raster art, procedural
  placeholder art, SVG illustration, or another model.
- Deterministic SVG/code remains allowed for technical diagrams, manifests,
  atlas packing, pivots, attachments and QA overlays only.
- Use one request per distinct module or animation set.
- Do not silently change model or path.
- Report repeated generation or edit failures.
- CLI/API fallback requires explicit user approval.
- API credential reuse or creation requires explicit confirmation.
- Save every accepted result inside the project.
- Wait for the real completion message and verify that the output file exists.

## First action

1. Read all required documentation.
2. Confirm the current production order from documentation.
3. Create a new neutral cardboard material-and-style baseline.
4. Show the baseline to the user.
5. After approval, begin the first documented gameplay object from zero.

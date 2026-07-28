# Ether Frontier — restart asset generation from Watchtower

Use this prompt in a new Codex/ImageGen window to restart visual asset generation from the beginning using the confirmed Layered Object Pipeline v2.

## Role

You are producing production-ready layered sprite atlases for Ether Frontier, a 2D top-down tower-defense game with a cardboard tabletop board-game visual style.

Use built-in imagegen by default for raster generation. Do not silently switch to CLI/API fallback unless explicitly asked. If imagegen fails due to network/backend errors, report the blocker and retry once with a simpler generation prompt before falling back to local deterministic processing.

## Absolute visual baseline

Start from Watchtower.

The visual style must match the confirmed cardboard tabletop concept:

- true top-down orthographic 90° when readable;
- flat board-game/cardboard token look;
- matte paper texture;
- visible tan exposed cardboard cut edges;
- muted grey stone;
- warm brown wood;
- dark red fabric;
- amber lantern / attack glow;
- thick hand-painted ink outlines;
- no glossy 3D;
- no cinematic angle;
- no side/rear/facade/tall tower read;
- no isometric perspective;
- no baked terrain.

The object must look like layered cardboard/paper pieces on a tabletop board, not a rendered 3D tower.

## New production pipeline

Use Layered Object Pipeline v2 for every new/regenerated gameplay object.

Each object produces:

1. `object_layered_runtime.png`
   - compact transparent runtime atlas;
   - tight packing;
   - no labels;
   - no grid;
   - no review-only assembled preview;
   - one object family only;
   - final file size under 5 MB.

2. `object_layered_manifest.json`
   - image filename;
   - atlas pixel size;
   - every sprite `rect`;
   - every sprite `pivotPx` or normalized `pivot`;
   - optional source/content size;
   - semantic layer names;
   - attachment points;
   - draw order;
   - animation clips;
   - frame duration;
   - loop/hold behavior;
   - runtime transforms.

3. `object_layered_review_grid.png`
   - separate human QA sheet;
   - fixed cells are allowed here only;
   - labels are allowed here only;
   - pivot crosses are allowed here only;
   - grid lines are allowed here only;
   - not loaded by game runtime.

4. `object_layered_composite_preview.png`
   - optional review-only assembled preview.

Do not make the runtime atlas a huge fixed empty grid unless there is a real engine reason. The engine should read tight `rect` values from JSON.

## Watchtower first-object contract

Generate Watchtower first, then validate it before continuing to Ranger.

Required Watchtower layers:

- `base_stone_token`
  - static circular stone/cardboard platform;
  - locked footprint;
  - no weapon, no flag, no lantern baked into it.

- `central_socket`
  - separate round wood/metal rotation hub.

- `crossbow_rotatable`
  - complete standalone top-down crossbow;
  - centered around rotation pivot;
  - rotates toward enemy at runtime.

- `flag_pole`
  - separate pole/base.

- `flag_cloth_wind_01..04`
  - four red cloth wind frames;
  - attach to flag pole;
  - no readable text;
  - no detached garbage pixels.

- `lantern_body`
  - separate lantern casing.

- `lantern_flame_01..04`
  - four amber flame/glow frames;
  - attach to lantern body;
  - loop independently.

- `crossbow_release_01..04`
  - four mechanical string/recoil release frames;
  - attach to the crossbow;
  - no flame, smoke, sparks, or firearm-style muzzle flash;
  - play once per attack.

- `projectile_bolt`
  - separate projectile;
  - rotates along trajectory.

- `destroy_debris_01..N`
  - independent stone/wood/cardboard debris pieces;
  - not one huge grouped strip if the engine may animate pieces independently.

Optional:

- `impact_fx_01..04`, if the object owns a unique impact effect.

## ImageGen prompt template for Watchtower source sheet

Use this as the imagegen prompt for the initial source sheet:

```text
Use case: stylized-concept
Asset type: production layered sprite source sheet for Ether Frontier, 2D top-down tower-defense game

Primary request:
Create a high-quality layered source sheet for a Watchtower object decomposed into separate modular top-down components for runtime composition.

Scene/backdrop:
Perfectly flat solid #ff00ff chroma-key background. No shadows on the background. No floor plane. No labels, no text, no numbers, no UI, no watermark.

Subject:
Cardboard tabletop Watchtower token: circular stone platform with tan exposed cardboard edge, central wooden/metal rotation socket, separate rotatable crossbow, separate flag pole, red wind flag cloth, separate lantern body/flame, projectile bolt, muzzle flash, and debris.

Required separated components:
1. base_stone_token: circular stone cardboard platform only, no weapon, no flag, no lantern.
2. central_socket: separate circular wooden/metal rotation hub.
3. crossbow_rotatable: complete standalone top-down crossbow, horizontal, centered around its rotation pivot.
4. flag_pole: separate pole with round base.
5. flag_cloth_wind_01..04: four separate red torn cloth wind variants, same style, no readable text.
6. lantern_body: separate lantern casing.
7. lantern_flame_01..04: four small amber flame/glow variants.
8. crossbow_release_01..04: four mechanical string/recoil states with no flame or firearm muzzle flash.
9. projectile_bolt: one separate arrow/bolt projectile.
10. destroy_debris_01..N: individual stone/wood/cardboard debris pieces.

Style:
True top-down orthographic 90 degree view. Cardboard tabletop board-game token style. Matte paper texture, visible tan cardboard cut edges, thick hand-painted ink outlines, muted grey stone, warm brown wood, dark red fabric, amber lantern glow.

Technical constraints:
All components must be fully visible, isolated, not cropped, and not touching each other. Keep crisp cutout edges against #ff00ff. Do not use #ff00ff inside any object. No white background. No black background. No terrain. No drop shadows. No perspective distortion.

Avoid:
No side view, no rear view, no facade, no tall tower, no isometric camera, no cinematic angle, no glossy 3D, no plastic look, no merged/baked whole-object animation frames. No labels/text/watermark.
```

## Normalization after imagegen

After imagegen returns a source sheet:

1. Save the generated source into the project; never leave project assets only under `.codex/generated_images`.
2. Remove the #ff00ff chroma-key into alpha.
3. Detect components.
4. Split grouped debris into independent pieces.
5. Remove detached garbage pixels from single-component layers.
6. Create compact `object_layered_runtime.png` using tight packing.
7. Create `object_layered_manifest.json` with exact rects/pivots/attachments/animations.
8. Create a separate fixed-cell `object_layered_review_grid.png`.
9. Create optional composite preview.
10. Validate all output files.

## Required validation before asking for approval

Before saying the object is ready:

- Open and visually inspect the source sheet.
- Open and visually inspect the transparent runtime atlas.
- Open and visually inspect the review grid.
- Parse JSON manifest.
- Confirm runtime PNG is under 5 MB.
- Confirm one object family only.
- Confirm no labels/grid/preview inside runtime atlas.
- Confirm all required layers exist.
- Confirm rotatable layers have pivots.
- Confirm animated child layers do not move the base/body footprint.
- Confirm style still matches cardboard tabletop top-down baseline.

## First pass acceptance language

When finished with Watchtower, report:

- source sheet path;
- runtime atlas path;
- manifest path;
- review grid path;
- composite preview path, if created;
- atlas dimensions;
- file size;
- missing/weak layers, if any;
- whether it is “approved candidate” or “needs another imagegen pass”.

Do not continue to Ranger until Watchtower format is approved.

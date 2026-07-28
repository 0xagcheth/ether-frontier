# Technical Asset Contract

## Canonical Asset Formats

- Sprite atlas image: PNG.
- Sprite atlas data: JSON.
- Maximum atlas size: 5 MB.
- One visual object per atlas.
- No atlas may contain unrelated objects.
- New or regenerated objects should use the Layered Object Pipeline v2 unless there is a documented reason to keep a fully baked strip as the source of truth.

## Current Prototype Note

The old shared demo atlas was deleted. Do not recreate it. New production atlases must follow the one-object-family rule and live under `assets/runtime/atlases/`.

## Folder Responsibilities

- `assets/source/`: references and editable source masters.
- `assets/staging/incoming/`: untouched incoming exports.
- `assets/staging/candidates/`: normalized review candidates.
- `assets/staging/prompts/`: extracted per-object working prompts.
- `assets/approved/canon/`: explicitly approved visual references.
- `assets/approved/masters/`: approved object masters.
- `assets/runtime/sprites/`: categorized engine-ready sprite files.
- `assets/runtime/atlases/`: engine-ready PNG/JSON/JS atlases.
- `assets/review/`: temporary galleries, captures, and scorecards.
- `scripts/`: production pipeline scripts.
- `scripts/asset_tools/`: specialized atlas and asset utilities.
- `docs/05_assets/`: production asset rules and manifests.

## Naming

Enemies:

```text
<unit>_<action>_<projection>.png
<unit>_projectile_<projection>.png
```

Buildings:

```text
<building>_idle.png
<building>_attack.png
<building>_destroy.png
<building>_projectile.png
<building>_impact.png
```

Atlases:

```text
<object>_atlas.png
<object>_atlas.json
```

Layered atlas demo / source-of-truth atlases:

```text
<object>_layered_runtime.png
<object>_layered_manifest.json
<object>_layered_review_grid.png
<object>_layered_composite_preview.png
```

Production layered objects use:

- `<object>_layered_runtime.png`: compact transparent atlas consumed by the engine.
- `<object>_layered_manifest.json`: source of truth for rects, pivots, attachments, draw order, animations, and QA.
- `<object>_layered_review_grid.png`: human QA sheet with fixed cells, labels, pivot marks, and visible grid. Not loaded by gameplay.
- `<object>_layered_composite_preview.png`: optional assembled preview for visual review only.

## Atlas JSON Requirements

Every JSON atlas should declare:

- image filename
- atlas pixel dimensions
- frame rectangles
- source cell size
- sprite source offset
- pivot/anchor
- animation frame order
- animation timing
- loop/hold behavior

Layered JSON atlases must additionally declare:

- `pipeline`, e.g. `layered-object-v2`;
- `drawOrder`;
- `sprites` with explicit tight runtime `rect`, source/content size, and `pivotPx` or normalized `pivot`;
- optional `reviewCell` metadata only for the human review grid;
- `attachments`, including semantic anchors such as `weapon_pivot`, `muzzle_anchor`, `flag_anchor`, `lantern_anchor`, and `projectile_spawn` where applicable;
- `animations` that reference named layer frames instead of relying on baked full-object strips;
- runtime transforms, such as target-facing rotation, wind frame selection, flame loop, charge level, or recoil;
- base/body footprint lock, including the measured footprint used for QA.

The manifest is the source of truth. Review grids are visual QA artifacts and must not be required by the engine runtime. A fixed 512px grid can be generated for review, but production runtime should use compact packed rectangles unless a specific engine constraint requires fixed cells.

## Validation Gates

Before acceptance:

- PNG exists and opens.
- JSON exists and parses.
- PNG size is under 5 MB.
- Atlas contains one object family only.
- Frame names match naming rules.
- Baseline and pivot are stable.
- For layered atlases, every rotatable/animated layer has a declared pivot and attachment.
- For layered atlases, the composed preview matches the object footprint and does not reveal missing hidden base art.
- For layered atlases, runtime extraction uses tight rects from JSON; review grid cells are not treated as runtime rects.
- For layered atlases, review-only assembled previews are excluded from the runtime atlas.
- For layered atlases, projectile/impact/debris that belong to the object are included in the same object atlas unless intentionally shared and documented.
- No unintended pure-black object pixels remain.
- Quality gate scorecard is complete.
- Canon Asset comparison is complete.

## Acceptance Authority

This contract determines whether an asset can enter the engine. It does not approve art direction by itself. Final acceptance requires `../07_pipeline/quality-gate.md`, `../03_art/style-drift.md`, and any applicable Canon Asset checks.

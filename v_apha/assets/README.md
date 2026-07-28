# Asset Workspace

This directory is the only home for new visual and audio files. Do not place assets beside game code or inside documentation.

## Lifecycle

```text
source -> staging -> approved -> runtime
                    |          |
                    +-> review +-> game
```

- `source/references/`: external or internal visual references. Store provenance beside each reference.
- `source/editable/`: layered masters such as PSD, Aseprite, Krita, Blender source, or SVG working files.
- `staging/incoming/`: untouched exports from artists or generation tools.
- `staging/candidates/`: normalized candidates ready for review, grouped by asset family.
- `staging/prompts/`: generated per-object prompt copies; canonical prompt text remains in `docs/05_assets/`.
- `staging/rejected/`: rejected candidates retained only when useful for comparison.
- `approved/canon/`: explicitly approved visual references listed in the Canon Asset Registry.
- `approved/masters/`: approved high-quality object masters before runtime packing.
- `runtime/`: engine-ready sprites, atlases, audio, and fonts. The browser prototype loads only from here.
- `review/`: temporary contact sheets, galleries, captures, and scorecards.

## Promotion Rule

Never copy a generated image directly into `runtime/`. A file must pass the technical contract, style-drift review, and quality gate first. Promotion order:

1. Put the untouched file in `staging/incoming/`.
2. Normalize it into `staging/candidates/<family>/`.
3. Review it using `docs/07_pipeline/quality-gate.md`.
4. Preserve the accepted master in `approved/masters/<family>/`.
5. Export engine-ready files into `runtime/`.
6. Promote a separate copy to `approved/canon/` only by explicit canon decision.

## Families

Use the same family names throughout `candidates`, `masters`, and `runtime/sprites`:

`buildings`, `enemies`, `heroes`, `environment`, `ui`, `vfx`.

Use lowercase snake_case filenames. Never encode review status as `final`, `new`, or `latest`; review status belongs in the review record.

# Ether Frontier — v_beta (active)

This is the only active development workspace for Ether Frontier. The game visual
pipeline is being rebuilt from zero while preserving working gameplay mechanics.

## Start here

1. `AGENTS.md` — mandatory workspace and placement rules.
2. `docs/00_project/current-production-state.md` — current phase and next action.
3. `docs/00_project/source-of-truth.md` — canon priority.
4. `docs/README.md` — documentation map.
5. `assets/README.md` — asset lifecycle.

## Included

- `game/` — preserved working browser gameplay code and mechanics.
- `docs/` — canonical project vision, gameplay, lore, creative, art, audio,
  asset, engine and quality-pipeline documentation.
- `assets/staging/prompts/` — the clean layered-atlas restart master prompt.
- `scripts/` — generic reusable sprite preparation and packing tools.
- `assets/source/` — raw new generated sources and decomposed layers.
- `assets/staging/candidates/` — unapproved processed candidates.
- `assets/approved/` — approved masters and manifests.
- `assets/runtime/` — approved runtime atlases and sprites.
- `assets/review/` — human QA artifacts.
- `output/` — local validation output.
- `sites/` — local QA applications.

## Deliberately excluded

- all previous generated object art;
- old runtime atlases and sprites;
- old candidates and review images;
- archived assets;
- object-specific generators tied to rejected visuals;
- old QA sites and captured output;
- local virtual environments;
- API keys and `.env` files.

The browser prototype may show missing visuals until the first new approved
runtime batch is generated. Its gameplay mechanics and source code are preserved.

## Visual restart

Start with:

`assets/staging/prompts/restart_all_layered_sprite_atlases_clean_v1.md`

That prompt requires a new neutral material baseline before production begins on
the first gameplay object.

## Archive

The complete previous workspace is stored beside this directory in:

`../v_apha/`

It is a frozen archive, not a reference source. Do not inspect or copy its visual
assets into beta unless the user explicitly requests archive recovery.

# Ether Frontier v_beta — Working Rules

## Active root

`v_beta/` is the only active development root for Ether Frontier.

`../v_apha/` is a frozen historical archive. Do not read it for visual direction,
copy generated art from it, run its tools, or modify it unless the user explicitly
requests an archive recovery.

All new code, documentation, prompts, assets, QA pages, and validation output must
be created inside `v_beta/`.

## Start every task here

1. Read `docs/00_project/current-production-state.md`.
2. Read `docs/00_project/source-of-truth.md`.
3. Read the owning canonical document for the requested area.
4. For visual-object work, also read
   `assets/staging/prompts/restart_all_layered_sprite_atlases_clean_v2.md`.

Do not infer object design from another object. Each object must follow its own
description in `docs/05_assets/object-family-and-variation-spec-v5.md`,
`docs/05_assets/object-lore-material-overlay-v5.md` and
`docs/05_assets/asset-prompt-bible-v5.md`.

## Visual production lock

- Layered gameplay objects use true top-down orthographic 90°.
- Every moving or independently animated part is a separate cardboard layer.
- One object family per atlas.
- Runtime atlas and manifest are engine data; review grids and labels are QA only.
- An object cannot advance to runtime, and the next object cannot start, until the
  current object passes visual and technical validation.
- Approved assets are recorded in
  `docs/05_assets/canon-asset-registry.md`.

## File placement

- Game code: `game/`
- Canonical documentation: `docs/`
- Production prompts: `assets/staging/prompts/`
- Raw generated sources: `assets/source/`
- Unapproved candidates: `assets/staging/candidates/`
- Human QA artifacts: `assets/review/`
- Approved source/manifest records: `assets/approved/`
- Engine-ready files only: `assets/runtime/`
- Reusable tooling: `scripts/`
- Temporary validation output: `output/`
- Local QA apps: `sites/`
- Short-lived task notes and handoffs: `notes/`

Never place review grids, labels, pivot crosses, or assembled previews in
`assets/runtime/`.

Before changing layered-atlas tooling, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s scripts/tests -p 'test_*.py' -v
```

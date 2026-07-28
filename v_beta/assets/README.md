# Asset Workspace

Assets move in one direction:

`source → staging/candidates → review → approved → runtime`

- `source/objects/<object-id>/` — original generations and lossless layer sources.
- `source/shared/` — approved truly shared material components; never a shortcut
  for copying an object's unique weapon or identity.
- `staging/prompts/` — active production prompts.
- `staging/candidates/<object-id>/` — unapproved processed candidates.
- `review/objects/<object-id>/` — review grid, composite previews, validation report.
- `approved/canon/` — approved visual masters.
- `approved/manifests/` — approved source-of-truth manifests.
- `runtime/atlases/` — compact transparent packed atlases only.
- `runtime/sprites/` — other engine-ready sprite outputs only.

An asset may not skip a stage. Generated output is not canon until it passes the
quality gate and is registered in `docs/05_assets/canon-asset-registry.md`.


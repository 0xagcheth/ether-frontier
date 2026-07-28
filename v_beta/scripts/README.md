# Asset Scripts

- Top-level scripts extract prompts and prepare generated sprites, strips, and
  runtime packs.
- Scripts are reusable technical utilities. Their filenames do not grant approval
  to any asset or object family.

All project paths must be derived from `Path(__file__)`; do not add machine-specific absolute paths. Inputs belong in `assets/staging/`, approved masters in `assets/approved/`, and outputs consumed by the game in `assets/runtime/`.

Before using a script, verify that its input/output contract matches
`docs/05_assets/technical-asset-contract.md`. Old naming inside a generic script
must not override the active manifest schema.

## Layered atlas validation

Validate a preproduction contract:

```bash
python3 scripts/validate_layered_atlas.py \
  assets/staging/candidates/watchtower/watchtower_layered_manifest_template_v1.json \
  --mode template
```

Validate a filled runtime atlas and manifest:

```bash
python3 scripts/validate_layered_atlas.py \
  assets/runtime/atlases/watchtower_layered_manifest.json \
  --mode production
```

Production mode is fail-closed. It verifies the PNG, 5 MB limit, atlas
dimensions, expanded sprite entries, rect bounds and overlaps, alpha-tight
packing, pivots, master pivots, attachments, animation references, anchors,
master approval and QA approval.

## Layered atlas packing

List the exact required Watchtower input filenames:

```bash
python3 scripts/build_layered_atlas.py --inventory
```

Build after approved full-canvas transparent layers and approved geometry exist:

```bash
python3 scripts/build_layered_atlas.py \
  --geometry assets/approved/masters/watchtower_layer_geometry.json \
  --layers assets/approved/masters/watchtower_layers \
  --output-png assets/runtime/atlases/watchtower_layered_runtime.png \
  --output-manifest assets/runtime/atlases/watchtower_layered_manifest.json
```

The packer requires the complete inventory, rejects unexpected files, rejects
mixed source-canvas dimensions, requires explicit master pivots and anchors,
alpha-crops every layer, computes local pivots from approved master coordinates,
and produces deterministic padded power-of-two shelf packing. It leaves
`qa.validated` false until human artifacts pass.

Generate a draft geometry checklist only after the approved master dimensions
are known:

```bash
python3 scripts/build_layered_atlas.py \
  --write-geometry-template assets/staging/candidates/watchtower/watchtower_layer_geometry_draft.json \
  --master-width <approved-width> \
  --master-height <approved-height>
```

The generated file is deliberately `draft_geometry`, with null pivots/anchors
and `master.approved: false`; the runtime packer rejects it until completed and
approved.

## Layered QA artifacts

After packing, build the separate human review files:

```bash
python3 scripts/build_layered_review.py \
  assets/runtime/atlases/watchtower_layered_manifest.json \
  --review-grid assets/review/watchtower/watchtower_layered_review_grid.png \
  --composite assets/review/watchtower/watchtower_layered_composite_preview.png
```

This tool reads the real runtime atlas/manifest. It draws labels, grid lines and
pivot crosses only in the review grid, while the composite is reconstructed from
default-visible layers in master coordinates. It never edits the runtime atlas.

## Watchtower ImageGen intake

After ImageGen 2 returns a chroma-key projection master:

```bash
python3 scripts/prepare_watchtower_projection_master.py \
  /absolute/path/to/generated.png \
  --revision <new-revision>
```

The intake preserves the raw source under `assets/source/watchtower/`, invokes
the canonical ImageGen chroma-removal helper, writes the alpha candidate under
`assets/staging/candidates/watchtower/`, and creates a checksum/alpha/margin
report. It does not approve projection or style: the report leaves the manual
visual gate false.

Validate the ordered Watchtower ImageGen call plan:

```bash
python3 scripts/validate_source_call_plan.py \
  assets/staging/prompts/watchtower_source_call_plan_v1.json
```

The validator checks unique ordered dependencies, the human approval stop after
the projection master, ImageGen 2 ownership, unique output names and the
one-source-unit-per-call rule.

After visual review, promotion is controlled by:

```bash
python3 scripts/promote_watchtower_projection_master.py \
  assets/staging/candidates/watchtower/watchtower_projection_review_v<revision>.json
```

Start from
`assets/staging/candidates/watchtower/watchtower_projection_review_template_v1.json`.
Promotion requires every canon, visual and technical criterion to be `PASS`,
`decision.result: APPROVE`, explicit `userConfirmed`, matching intake/master
checksums and an unmodified project-local candidate. Pending review fails closed.

## Regression suite

Run the complete layered-pipeline regression suite:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s scripts/tests -p 'test_*.py' -v
```

The suite covers the 133-sprite inventory, production rejection of templates,
the fourteen-call approval gate, deterministic non-overlapping packing,
unapproved geometry defaults, review/runtime separation and rejection of a
pending visual review.

## Authoritative Watchtower status

Generate current machine-readable and human-readable gate status:

```bash
python3 scripts/watchtower_pipeline_status.py \
  --json output/watchtower_pipeline_status.json \
  --markdown output/watchtower_pipeline_status.md
```

Add `--fail-if-blocked` for CI. The reporter derives state from real source,
intake, approval, layer, atlas, QA and site files. It enforces sequential gates
and reports whether work on the next object is allowed.

# Documentation Rules

## Authority

`docs/` is authoritative. Historical drafts are kept outside the active project workspace.

When two documents appear to conflict, use this order:

1. The user's latest explicit decision
2. `00_project/source-of-truth.md`
3. `00_project/current-production-state.md`
4. The owning document listed in `00_project/active-document-map.md`
5. Approved Canon Assets in `05_assets/canon-asset-registry.md`

## One Responsibility Per Document

Each document owns one decision area. Do not duplicate rules across documents. Cross-link instead.

Examples:

- Active visual language lives in `03_art/master-visual-style.md`.
- Palette summary lives in `03_art/art-bible.md`.
- Atlas file constraints live in `05_assets/technical-asset-contract.md`.
- Per-object prompt wording lives in `05_assets/asset-prompt-bible-v4.md`.
- Approval scoring lives in `07_pipeline/quality-gate.md`.
- Approval flow lives in `07_pipeline/review-pipeline.md`.
- Visual reference canon lives in `05_assets/canon-asset-registry.md`.

## Change Process

Any future change to style, projection, faction identity, atlas format, or naming must update the owning document before assets or code are changed.

Every doc change should answer:

- What rule changed?
- Why did it change?
- Which assets/code are affected?
- Does it invalidate archived prompts or generated assets?

## AI Assistance

AI may draft, summarize, compare, and propose edits. AI must not silently change canon direction. Any AI-generated rule must be reviewed against `project-vision.md` and `art-bible.md`.

## Archive Policy

Do not keep superseded drafts, exported conversations, or compatibility copies in the active repository. Preserve history in version control or external project storage.

The adjacent `v_apha/` folder is external project storage for this purpose. It is
not an active documentation or visual reference source.

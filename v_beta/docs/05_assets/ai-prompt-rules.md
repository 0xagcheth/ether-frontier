# AI Prompt Rules

For full AI conduct, see `ai-behavior.md`. This file is the compact prompt-stack contract.

## Required Prompt Stack

Every AI asset generation must start from:

1. `../03_art/art-bible.md`
2. `../03_art/master-visual-style.md`
3. `../03_art/style-self-review.md`
4. `canon-asset-registry.md`
5. `../03_art/style-drift.md`
6. `technical-asset-contract.md`
7. `asset-prompt-bible.md`
8. The exact per-object prompt block

## Forbidden Prompt Drift

Do not introduce:

- 3D render language.
- full isometric, 3/4 side-view, perspective, tall-facade, full-doorway, staircase, or dominant vertical-wall language for ordinary gameplay assets.
- Smooth modern illustration language.
- Pixel-art language as the active style target.
- Studio or game imitation language.
- Generic undead or goblin factions for Lower City, Grey, Nav or machine units.
- Player amber as enemy magic.
- Deprecated Horde toxic-green as player tower identity.
- Pure black object pixels.
- Shared atlas output for unrelated objects.
- Ground discs, pedestals, or unrelated terrain under object sprites.

## Generation Output Requirements

Ask for one object at a time. New/regenerated gameplay objects should output a layered atlas candidate matching the owning object contract, not a whole-object baked strip by default.

For Layered Object Pipeline v2 the required deliverables are:

- compact transparent runtime atlas;
- JSON manifest with tight rects, pivots, attachments, draw order, animation clips, and runtime transforms;
- separate fixed-cell human review grid with labels and pivot marks;
- optional composed preview for review only.

Horizontal strips are legacy/export derivatives and should be requested only when a runtime compatibility task explicitly needs them.

If an AI tool cannot guarantee cell consistency, the result is a candidate only and must pass technical normalization before review.

## Review Requirement

AI-generated assets are never automatically canon. They must pass:

1. Technical validation.
2. Style drift check.
3. Quality gate scorecard.
4. Art-direction review.
5. Gameplay readability review.
6. Implementation smoke test.

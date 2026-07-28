# Source Of Truth

## Purpose

This document defines what wins when project documents, prompts, assets, or AI output disagree.

No future document, prompt, tool output, generated image, or code comment may override this hierarchy implicitly.

## Canon Order

The authority chain is:

1. `project-vision.md`
2. `../02_creative/creative-direction.md`
3. `../03_art/master-visual-style.md`
4. `../03_art/art-bible.md`
5. `../05_assets/technical-asset-contract.md`
6. `../05_assets/object-family-and-variation-spec-v4.md`
7. `../05_assets/restart-description-driven-object-pipeline-v3.md`
8. `../05_assets/modular-object-family-plan.md` (legacy reuse rules are superseded by v4)
9. `../05_assets/object-module-registry.json` (legacy schema; v4 wins on conflicts)
10. `../05_assets/asset-prompt-bible.md`
11. The approved object prompt extracted from the asset prompt bible
12. The current Canon Asset references in `../05_assets/canon-asset-registry.md`
13. Candidate generated asset
14. Runtime implementation

If a generated asset contradicts any higher source, the asset is wrong.

If a new document such as `enemy_bible_v2.md`, `sprite_rules_new.md`, or `artstyle_update.md` appears, it has no authority until this file and `documentation-rules.md` explicitly incorporate it.

## Canon Assets

Text rules are necessary but not sufficient. Approved visual references are stronger than interpretation.

A Canon Asset is an accepted reference asset used to judge future assets for:

- palette
- lighting
- pixel density
- silhouette readability
- material rendering
- scale
- outline treatment
- shadow language
- animation restraint

Canon Assets do not replace written rules. They make written rules measurable.

## Conflict Resolution

Use this sequence:

1. Identify the conflicting rule or output.
2. Locate the highest-ranking source that speaks to the issue.
3. Reject or revise lower-ranking material.
4. If the higher-ranking source is ambiguous, document the decision in the owning file.
5. Update prompts only after the canon decision is recorded.

## Non-Override Rule

AI output cannot establish canon. A generated image may become canon only after passing the quality gate and being listed in `../05_assets/canon-asset-registry.md`.

## Required Review Phrase

Every asset review must state:

```text
Canon source checked:
- Project Vision: PASS/FAIL
- Creative Direction: PASS/FAIL
- Master Visual Style: PASS/FAIL
- Art Bible: PASS/FAIL
- Technical Asset Contract: PASS/FAIL
- Asset Prompt Bible/Object Prompt: PASS/FAIL
- Canon Asset References: PASS/FAIL
```

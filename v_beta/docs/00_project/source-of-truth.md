# Source Of Truth

## Purpose

This document defines what wins when project documents, prompts, assets, or AI output disagree.

No future document, prompt, tool output, generated image, or code comment may override this hierarchy implicitly.

## Canon Order

The active authority chain is:

1. The user's latest explicit decision.
2. `project-vision.md`.
3. `current-production-state.md`.
4. `../03_art/world-visual-direction-review-draft-v1.md` for world appearance
   only.
5. `../03_art/hero-spas-character-visual-review-draft-v1.md` for Spas's
   character and appearance only.
6. `../01_design/hero-spas-passive-and-buildings-review-draft-v1.md` for
   Spas's passive and three unique buildings only.
7. `../03_art/heroes-velimudr-and-tara-character-visual-review-draft-v1.md` for
   Velimudr and Tara character and appearance only.
8. `../01_design/heroes-velimudr-and-tara-passives-buildings-review-draft-v1.md`
   for their passives and three unique buildings only.
9. `../02_creative/four-ages-campaign-synthesis-v1.md`.
10. `../02_creative/fourth-age-invention-of-antiquity-world-bible-v1.md`.
11. `../02_creative/third-age-antlan-and-fatta-world-bible-v1.md`.
12. `../02_creative/second-age-daariya-and-lelya-world-bible-v1.md`.
13. `../02_creative/first-cosmic-age-world-bible-v1.md`.
14. `../02_creative/andrboll-topic-adaptation-map-v1.md`.
15. `../02_creative/satirical-world-foundation-v1.md`.
16. `../02_creative/game-lore-bible-v6.md`, only where it does not contradict
   the satirical foundation.
17. `../01_design/gameplay-rules.md`.
18. `../01_design/game-system-and-lore-integration-v1.md`.
19. `../01_design/seven-circles-object-redesign-v1.md`.
20. `../02_creative/entity-mechanics-codex-v5.md`, runtime facts only where they do not contradict the redesign.
21. `../02_creative/faction-bible-v5.md`.
22. `../02_creative/campaign-v5.md`.
23. `../02_creative/character-bible-v5.md`.
24. `../02_creative/mission-briefings-and-dialogue-v3.md`.
25. `../02_creative/campaign-epilogues-v3.md`.
26. `../01_design/grey-transfer-mechanics-v2.md`.
27. `../02_creative/visual-cultural-source-map-v4.md`.
28. `../03_art/master-visual-style.md`.
29. `../03_art/art-bible.md`.
30. `../03_art/environment-bible.md`.
31. `../03_art/symbol-risk-register-v2.md`.
32. `../05_assets/asset-prompt-bible-v7.md`.
33. `../05_assets/prompt-lore-alignment-audit-v2.md`.
34. `../03_art/world-concept-art-prompt-bible-v2.md`, material and composition only.
35. `../05_assets/technical-asset-contract.md`.
36. Technical-only fragments of older family, overlay and registry documents,
    but never their object identity, ability, weapon or effect definitions.
37. A v7 per-object source-call plan approved after redesign.
38. Canon Asset references in `../05_assets/canon-asset-registry.md`, material
    and projection reference only until re-approved for v7 identity.
39. Candidate generated asset.
40. Runtime implementation.

Superseded v5/v4/v3 lore, campaign, character, entity, story, dialogue and
prompt documents are migration references only. They never override the active
chain above.

If a generated asset contradicts any higher source, the asset is wrong.

The v7 lore-first object framework supersedes weapon-led prompts inside the v6
package. The v6 lore formally supersedes Options A and B,
Kitezh-17, the blended Last-Outpost framing, Goblin Horde, Grimhold, Aeldrath
and generic Western medieval-fantasy identity in lower-ranked documents. The
active asset prompt bible and object specification have already been migrated;
older versions are archival technical history only.

Earlier long-form stories remain archival tone/reference material. Plot canon
is owned by `game-lore-bible-v6.md`, `campaign-v5.md`, current dialogue and
epilogues until a separately approved v6 long-form story is written.

For layered gameplay objects, true top-down orthographic 90° is mandatory.
Identity, ability, mechanisms and animation states come from
`seven-circles-object-redesign-v1.md` and `asset-prompt-bible-v7.md`.

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

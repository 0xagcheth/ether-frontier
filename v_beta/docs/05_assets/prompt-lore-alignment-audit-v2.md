# Ether Frontier — Prompt/Lore Alignment Audit v2

Status: **REDESIGNED — runtime implementation pending**  
Updated: 2026-07-26

## Finding

The v6 prompt chain retained crossbow, ballista, harpoon, cannon, mortar,
grapeshot, projectile and familiar hero-class logic from older directions.
The Seven Circles mostly changed names and surface materials.

## Correction

- Preserved: top-down projection, cardboard construction, separate children,
  stable pivots and animation-ready states.
- Replaced: roles, mechanisms, emitted effects, hero actions and upgrade logic.
- New mechanics source: `../01_design/seven-circles-object-redesign-v1.md`.
- New prompt source: `asset-prompt-bible-v7.md`.
- Combinations now join lore verbs rather than weapon families.
- Existing concept art is material/projection reference only.

## Blocked legacy inputs

- `watchtower_source_call_plan_v1.json`;
- identity sections of `watchtower-layer-contract-v4.md`;
- weapon-led entries in `object-family-and-variation-spec-v5.md`;
- genre-role entries in `production-prompt-catalog-v1.md`;
- source generation based on any of the above.

## Runtime mismatch

Current `game.js` still implements legacy damage, targeting, projectiles and
upgrade behaviour. Prompt correction does not silently change code. Runtime
mechanics require a separate migration before v7 objects become production
compatible.

## Validation gate

1. Brief names one Circle and one lore question.
2. Ability changes a relationship, not merely hit points.
3. Physical process communicates the ability without symbols.
4. Neutral, prepare, commit, resolve, interrupted, captured and destroyed
   states share compatible geometry.
5. No old weapon appears unless newly justified from lore.
6. Candidate concept art is used only for material/projection reference.

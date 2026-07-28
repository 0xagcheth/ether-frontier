# Review Pipeline

## Intake

Every new asset, animation, UI element, level, sound, or code change starts by identifying its owning document in `docs/`.

## Asset Flow

1. Confirm object contract.
2. Confirm relevant Canon Assets.
3. Generate or draw candidate.
4. Normalize/prepare source.
5. Build object atlas.
6. Run technical checks.
7. Run `quality-gate.md`.
8. Run `../03_art/style-drift.md`.
9. Review gameplay readability.
10. Export to `assets/runtime/` and integrate into `game/` only after acceptance.
11. Decide whether the asset is eligible for Canon Asset promotion.
12. Archive rejected or superseded candidates.

## Approval Roles

- Creative Director: world, faction, tone, naming.
- Art Director: visual identity, palette, silhouette, UI/VFX.
- Technical Art Director: atlas, animation, cutout, prompt contract.
- Principal Engineer: runtime integration, performance, maintainability.
- Game Designer: gameplay role, level readability, wave pressure.

## Rejection Conditions

Reject immediately if an asset:

- Looks 3D-rendered.
- Uses unrelated faction identity.
- Breaks the atlas-per-object rule.
- Exceeds 5 MB atlas size.
- Has unstable baseline or building body breathing.
- Cannot be read at gameplay scale.

## Required Review Output

Every visual asset review must include the scorecard from `quality-gate.md` and the comparison report from `../03_art/style-drift.md`.

If no relevant Canon Asset exists, the review must say:

```text
Canon reference missing. This candidate cannot become production-approved until a Canon Asset is selected or this candidate is explicitly promoted after full review.
```

## Archive Rules

Rejected candidates may be archived if useful for comparison. They must not be referenced by production manifests.

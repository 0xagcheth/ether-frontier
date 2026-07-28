# Performance And Optimization Rules

## Asset Budgets

- Object atlas PNG: maximum 5 MB.
- Atlas JSON: compact and deterministic.
- Avoid global atlases that grow with unrelated objects.
- Prefer trimmed frames with stable source-size metadata.

## Runtime Budgets

- Keep animation frame counts purposeful.
- Avoid DOM growth per projectile/effect beyond what is visible.
- Reuse atlas data rather than loading many redundant standalone images in gameplay.
- Cache-busting should be deliberate and documented.

## Current Debt

The legacy shared game atlas is larger than the production budget. Do not expand it as the long-term strategy. Migrate toward one atlas per visual object.

## Validation

Before accepting a content batch:

- Check atlas file sizes.
- Check frame count and dimensions.
- Check browser memory and render performance on the prototype map in `game/`.
- Check that animation viewers still load.

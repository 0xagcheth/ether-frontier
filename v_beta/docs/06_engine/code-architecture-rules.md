# Code Architecture Rules

## Current Runtime

The current prototype is a browser game shell:

- `game/index.html`
- `game/styles.css`
- `game/game.js`

The runtime holds game state, tower definitions, enemy behavior, rendering, animation style injection, projectiles, waves, and UI interactions in one prototype layer.

## Asset Pipeline Code

Pipeline scripts live in `scripts/`; specialized utilities live in `scripts/asset_tools/`:

- Prompt extraction.
- Generated asset cleanup.
- Black-key handling.
- Tower strip stabilization.
- Atlas packing.
- Review gallery generation.

## Boundary Rules

- Gameplay code should not define art-direction rules.
- Art-direction docs should not duplicate implementation constants.
- Asset pipeline scripts may enforce technical contracts from `05_assets/technical-asset-contract.md`.
- Viewer pages may inspect assets but should not become production manifests.

## Future Refactor Direction

When the prototype grows, separate:

- Game state and simulation.
- Rendering and animation.
- Asset loading and atlas lookup.
- UI/HUD.
- Data manifests for towers, enemies, waves, and levels.

## This Task

No game code was changed while creating this documentation system.

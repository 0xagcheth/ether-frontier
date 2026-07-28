# Ranger barbed bolt v1

Status: **canon — visual and technical gates passed**

## Identity

- ID: `ranger__projectile__barbed_bolt_v1`
- Owner: `ranger`
- Family: `fortress_ranged`
- Slot: `projectile`
- Runtime role: unique projectile spawned from `rapid_crossbow.muzzle_anchor`
- Candidate: `assets/staging/candidates/modules/ranger/ranger__projectile__barbed_bolt_v1_chroma.png`
- Forward axis: local `+X`

## Modular contract

Included:

- one straight lightweight wooden bolt shaft;
- one compact barbed dark-iron arrowhead;
- two forest-green paper fletching fins;
- exposed tan cardboard cut edge.

Excluded:

- crossbow and all parent modules;
- second projectile or loose ammunition;
- trail, muzzle flash, impact, glow and debris;
- labels, grid, pivot marker, shadow, motion blur, perspective and 3D render.

## Visual QA

- [x] Exactly one connected isolated projectile
- [x] Strict top-down orthographic projection
- [x] Straight horizontal local `+X` axis
- [x] Visually distinct from Watchtower simple bolt
- [x] Physical cardboard tabletop construction
- [x] No baked trail, impact, glow, weapon, or extra ammunition
- [x] Generous chroma padding and no clipping

## Generation

- Mode: built-in ImageGen
- Canvas: `1254 × 1254 px`
- Prompt intent: one fast Ranger projectile with green fletching and barbed tip, no animation effects or parent layers.

## Technical result

- Alpha: `assets/approved/canon/modules/ranger/ranger__projectile__barbed_bolt_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/ranger/ranger__projectile__barbed_bolt_v1.json`
- Tight rect: `1075 × 223 px`
- Trajectory pivot: `[537, 111] px`
- Tail spawn anchor: `[0, 111] px`
- Tip impact anchor: `[1074, 111] px`
- Runtime length: `0.23` of parent weapon
- Draw order: `40`
- Visible magenta spill: `0 px`
- Alpha size: `347,862 bytes` — under `5 MB`
- Muzzle-spawn composite: `assets/staging/reviews/modules/ranger/ranger__projectile__barbed_bolt_v1_muzzle_spawn_composite.png`
- Trajectory grid: `assets/staging/reviews/modules/ranger/ranger__projectile__barbed_bolt_v1_trajectory_review_grid.png`

## Gate

Barbed bolt promoted to canon after muzzle and rotated-trajectory validation. Projectile contains no baked trail, flash, impact, glow, or debris.

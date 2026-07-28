# Ranger rapid muzzle flash v1

Status: **canon — visual and technical gates passed**

## Identity

- ID: `ranger__muzzle_fx__rapid_flash_loop_v1`
- Owner: `ranger`
- Family: `fortress_ranged`
- Slot: `muzzle_fx`
- Runtime role: four-frame non-looping attack effect attached to `rapid_crossbow.muzzle_anchor`
- Candidate: `assets/staging/candidates/modules/ranger/ranger__muzzle_fx__rapid_flash_loop_v1_source_chroma.png`
- Forward axis: local `+X`

## Source-sheet structure

- Canvas: `1254 × 1254 px`
- Layout: four isolated animation groups in reading-order `2 × 2`
- Top-left: compact ignition star and short rays
- Top-right: long narrow amber spear flash
- Bottom-left: wider split paper flare with two green accent flecks
- Bottom-right: fading ochre fragments and small center ember
- No labels, grid lines, borders, or pivot markers

## Modular contract

Included:

- exactly four chronological paper/cardboard effect groups;
- shared empty attachment center;
- amber, gold and ochre paper with restrained green accent;
- non-realistic printed effect construction.

Excluded:

- weapon, projectile, bolt, magazine and optics;
- smoke, realistic fire, glow bloom or fifth group;
- text, labels, grid, pivot cross, shadow, perspective and 3D render.

## Visual QA

- [x] Four isolated groups in stable `2 × 2` structure
- [x] Clear ignition → expansion → split flare → fading fragments progression
- [x] Dominant attack frames face local `+X`
- [x] Flat physical paper/cardboard style
- [x] Sufficient chroma separation between all quadrants
- [x] No clipping or forbidden parent layers

## Generation

- Mode: built-in ImageGen
- Prompt intent: one unlabeled four-frame rapid-crossbow flash sheet with a stable attachment center and no baked weapon/projectile.

## Technical result

- Manifest: `assets/approved/canon/modules/ranger/ranger__muzzle_fx__rapid_flash_loop_v1.json`
- Runtime frames: four separate transparent PNG files
- Shared canvas: `477 × 272 px`
- Shared attachment pivot: `[78, 136] px`
- Timing: `45 / 55 / 65 / 85 ms`; total `250 ms`; non-looping
- Runtime scale: `0.17` of parent weapon length
- Draw order: `50`
- Runtime frame bytes: `202,595` — under `5 MB`
- Magenta spill by frame: `0 / 0 / 0 / 0 px`
- Review grid: `assets/staging/reviews/modules/ranger/ranger__muzzle_fx__rapid_flash_loop_v1_review_grid.png`
- Attack preview: `assets/staging/reviews/modules/ranger/ranger__muzzle_fx__rapid_flash_loop_v1_attack_preview.gif`

## Gate

Rapid muzzle flash promoted to canon after shared-pivot, despill, timing, and assembled muzzle validation.

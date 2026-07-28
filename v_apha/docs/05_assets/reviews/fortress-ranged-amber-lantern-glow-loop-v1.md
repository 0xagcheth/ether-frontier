# Fortress Ranged Amber Lantern Glow Loop v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_glow_loop_v1_chroma.png`

Module IDs: `fortress_ranged__ambient_child__amber_lantern_glow__frame_01..04`

Status: **canon animation module; composed animation pending user confirmation**

## Animation contract

- Family: `fortress_ranged`
- Parent: `fortress_ranged__ambient_child__amber_lantern_housing`
- Anchor: housing `glow_anchor`
- Exact frame count: `4`
- Order: low → rising → bright → settling
- Loop: independent idle loop
- Must not contain: housing, base, socket, weapon, flag, smoke, detached sparks, labels, grid lines, or pivot marks

## Source-sheet validation

- One built-in ImageGen request for the complete loop: PASS
- Strict implicit `2 × 2` layout: PASS
- Exactly four isolated components: PASS
- Uniform chroma background: PASS
- True top-down circular paper-token construction: PASS
- Cardboard/paper material read: PASS
- No baked housing or other parent layers: PASS
- No clipping or cell overlap: PASS
- Shared silhouette family and palette: PASS
- Frame-to-frame center drift: maximum `1 px`: PASS
- Extracted component sizes: all exactly `427 × 431 px`: PASS
- Large detached garbage pixels: none visible

## Generation record

- Mode: built-in ImageGen
- Canvas: `1254 × 1254 px`
- Chroma key sampled by extraction helper: `#fa03f9`
- Transparent pixels after provisional extraction: `992318 / 1572516`
- Partially transparent antialiasing pixels: `9999 / 1572516`

Final prompt summary: exactly four top-down amber printed-paper glow inserts in one unlabeled `2 × 2` source sheet; low/rising/bright/settling loop; identical centers and proportions; subtle brightness-only pulse; crisp cardboard cutouts on uniform magenta chroma; no housing, scenery, blur, realistic fire, shadows, labels, or grid lines.

## Next gate

## Prepared runtime frames

- Shared normalized canvas: `440 × 440 px`
- Shared content rect: `{ x: 6, y: 4, w: 427, h: 431 }`
- Shared pivot: `[220, 220] px` (`[0.5, 0.5]` normalized)
- Duration: `180 ms` per frame; `720 ms` complete loop
- Draw order: `21`, directly above the housing
- Runtime frame bytes: `1,289,118` total — PASS under `5 MB`
- Visible magenta spill: `0` pixels in every frame
- Frame luminance progression: `144.88 → 161.78 → 175.02 → 166.73`
- Runtime manifest: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_glow_loop_v1.json`

## Separate QA artifacts

- Human review grid with labels and pivot crosses: `assets/staging/reviews/modules/fortress_ranged/fortress_ranged__amber_lantern_glow_loop_v1_review_grid.png`
- Animated composed preview: `assets/staging/reviews/modules/fortress_ranged/fortress_ranged__amber_lantern_glow_loop_v1_composite.gif`
- Labels, slot borders, checkerboard, and pivot crosses are absent from runtime frames.

## Composed animation validation

- Glow fits inside the housing aperture: PASS at `0.31` of housing footprint
- Housing and parent footprint remain static: PASS
- Shared anchor prevents frame jitter: PASS
- Brightness progression is monotonic through frame 03 and settles in frame 04: PASS
- Loop reads without projection changes: PASS
- Active lantern semantic read: PASS

After user approval of the animated preview:

1. lock the complete `fortress_ranged` shared core package;
2. begin the first Watchtower-specific module: the light single crossbow;
3. keep its body, rotating weapon, projectile, and muzzle effect as separate layers.

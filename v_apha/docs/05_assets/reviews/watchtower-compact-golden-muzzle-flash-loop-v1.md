# Watchtower Compact Golden Muzzle Flash Loop v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__muzzle_fx__compact_golden_flash_loop_v1_chroma.png`

Module IDs: `watchtower__muzzle_fx__compact_golden_flash__frame_01..04`

Status: **canon animation module; composed attack pending user confirmation**

## Animation contract

- Object: `watchtower`
- Parent: `watchtower__active_addon__light_single_crossbow.muzzle_anchor`
- Slot: `muzzle_fx`
- Exact frame count: `4`
- Order: ignition → expansion → peak → fade
- Direction: local `+X`, extending right from a left-side attachment origin
- Playback: one-shot per attack
- Must not contain: crossbow, projectile, smoke, impact, base, labels, grid lines, or pivot marks

## Source-sheet validation

- One built-in ImageGen request for the complete successful loop: PASS
- Exactly four visually isolated flash components: PASS
- Clear implicit `2 × 2` reading order: PASS
- All flashes extend toward local `+X`: PASS
- Cardboard/paper effect construction: PASS
- Ignition/expansion/peak/fade size progression: PASS
- No baked weapon or projectile: PASS
- No detached sparks or garbage components: PASS
- No labels, borders, or drawn grid: PASS
- Uniform chroma background: PASS
- Raw slot-origin alignment: requires normalization
- Peak frame crosses the mathematical sheet midpoint by a few pixels but does not touch another component; split by connected component, not by a destructive hard quadrant crop

## Generation record

- Mode: built-in ImageGen
- Successful canvas: `1254 × 1254 px`
- Chroma key sampled by provisional extraction: `#f809f1`
- Two earlier built-in requests failed at the network layer before producing files

Final prompt summary: four separate top-down golden cardboard muzzle-flash wedges in one unlabeled `2 × 2` sheet; ignition/expansion/peak/fade sequence; every effect points right on `+X` from a left attachment origin; matte ochre/gold/cream paper with ink outlines and tan cut edge; uniform magenta chroma; no weapon, bolt, smoke, impact, blur, labels, grid, perspective, or 3D rendering.

## Next gate

## Prepared runtime frames

- Segmentation: four isolated connected components; no destructive quadrant cut
- Shared normalized canvas: `521 × 384 px`
- Shared left-center muzzle pivot: `[8, 192] px`
- Runtime scale: `0.20` of composed weapon length
- Composed maximum canvas: `156 × 115 px`
- Duration: `90 ms` per frame; `360 ms` complete one-shot
- Loop: `false`; hold last: `false`
- Draw order: `50`
- Runtime frame bytes: `428,742` total — PASS under `5 MB`
- Visible magenta spill: `0` pixels in every frame
- Runtime manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__muzzle_fx__compact_golden_flash_loop_v1.json`

## Separate QA artifacts

- Labeled review grid with muzzle-pivot crosses: `assets/staging/reviews/modules/fortress_ranged/watchtower__compact_golden_muzzle_flash_loop_v1_review_grid.png`
- Animated attack preview: `assets/staging/reviews/modules/fortress_ranged/watchtower__compact_golden_muzzle_flash_loop_v1_attack_preview.gif`
- Preview includes a `450 ms` blank reset hold after the four runtime frames; this pause is not part of the runtime animation manifest.
- Labels, checkerboard, and pivot crosses are absent from runtime frames.

## Composed attack validation

- Shared pivot remains locked to crossbow `muzzle_anchor`: PASS
- All frames inherit weapon rotation and local `+X`: PASS
- Ignition/expansion/peak/fade reads as a one-shot: PASS
- No frame jitter: PASS
- Peak frame remains inside a compact effect envelope: PASS
- Crossbow and base remain unchanged: PASS
- Projectile is not baked into the flash frames: PASS

After user approval of the animated attack preview:

1. lock the Watchtower firing-module package: crossbow, projectile, and muzzle flash;
2. generate the separate flag mount/pole as a flat top-down cardboard module;
3. only after its placement passes, generate the four-frame red pennant wind loop.

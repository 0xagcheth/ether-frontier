# Watchtower Range Pennant Wind Loop v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__ambient_child__range_pennant_wind_loop_v1_chroma.png`

Module IDs: `watchtower__ambient_child__range_pennant_wind__frame_01..04`

Status: **canon animation module; composed idle pending user confirmation**

## Animation contract

- Object: `watchtower`
- Parent: `watchtower__flag_mount__range_pennant_socket.cloth_anchor`
- Slot: `ambient_child`
- Exact frame count: `4`
- Order: upward ripple → straight → downward ripple → neutral return
- Direction: local `+X`, cloth extends right from a rigid left attachment tab
- Playback: independent looping idle animation
- Must not contain: mount, pole, base, weapon, lantern, labels, grid lines, detached scraps, or pivot marks

## Source-sheet validation

- One built-in ImageGen request for the complete loop: PASS
- Exactly four isolated connected components: PASS
- Clear implicit `2 × 2` reading order: PASS
- True top-down flat-paper construction: PASS
- No side-view hanging flag or upright pole: PASS
- All left attachment tabs remain rigid and readable: PASS
- All cloth frames extend toward local `+X`: PASS
- Consistent length: widths `574 / 578 / 574 / 576 px`: PASS
- Restrained wind contour changes: PASS
- Dark-red cardboard/paper material and tan cut edge: PASS
- No readable text or emblem: PASS
- No clipping, cell overlap, or detached garbage: PASS
- Raw origin drift is small and will be removed during shared-pivot normalization

## Generation record

- Mode: built-in ImageGen
- Canvas: `1254 × 1254 px`
- Chroma key sampled by provisional extraction: `#f903f9`
- Component bounds:
  - frame 01: `574 × 227 px`
  - frame 02: `578 × 214 px`
  - frame 03: `574 × 239 px`
  - frame 04: `576 × 213 px`

Final prompt summary: exactly four flat top-down dark-red cardboard pennant frames in one unlabeled `2 × 2` source sheet; rigid left tab, local `+X` extension, swallowtail right edge, restrained up/straight/down/neutral wind loop, tan cut edge; uniform magenta chroma; no mount, pole, parent layers, text, debris, perspective, shadows, or 3D cloth.

## Next gate

## Prepared runtime frames

- Segmentation: four isolated connected components
- Shared normalized canvas: `594 × 255 px`
- Shared left-center cloth pivot: `[8, 127] px`
- Base-relative scale: `0.22`
- Composed canvas size: `238 × 102 px`
- Parent cloth anchor in composed preview: `[456, 373] px`
- Duration: `180 ms` per frame; `720 ms` complete loop
- Loop: `true`
- Draw order: `16`, above the mount and below the weapon
- Runtime frame bytes: `849,982` total — PASS under `5 MB`
- Visible magenta spill: `0` pixels in every frame
- Runtime manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__ambient_child__range_pennant_wind_loop_v1.json`

## Separate QA artifacts

- Labeled review grid with cloth-pivot crosses: `assets/staging/reviews/modules/fortress_ranged/watchtower__range_pennant_wind_loop_v1_review_grid.png`
- Assembled idle preview: `assets/staging/reviews/modules/fortress_ranged/watchtower__range_pennant_wind_loop_v1_idle_preview.gif`
- Labels, checkerboard, and pivot crosses are absent from runtime frames.

## Composed idle validation

- Shared pivot remains locked to the mount `cloth_anchor`: PASS
- Rigid attachment tab does not move between frames: PASS
- Cloth extends consistently on local `+X`: PASS
- No frame jitter: PASS
- Up/straight/down/return loop reads clearly: PASS
- Base, mount, and weapon remain unchanged: PASS
- Pennant remains inside the object footprint at composed scale: PASS

After user approval of the animated idle preview:

1. lock the complete Watchtower intact-state layer package;
2. generate the destruction/debris kit as individually addressable cardboard pieces;
3. validate each piece, its pivot, and the assembled destroy animation before atlas packing.

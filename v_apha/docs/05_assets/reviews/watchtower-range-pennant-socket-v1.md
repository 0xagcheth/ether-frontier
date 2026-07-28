# Watchtower Range Pennant Socket v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/watchtower__flag_mount__range_pennant_socket_v1_chroma.png`

Module ID: `watchtower__flag_mount__range_pennant_socket`

Status: **canon module; composed placement pending user confirmation**

## Module contract

- Object: `watchtower`
- Family: `fortress_ranged`
- Slot: `flag_mount`
- Runtime behavior: static mount on the base; parent of the animated pennant cloth
- Local cloth direction: `+X`, toward the rectangular attachment slot
- Contains: low circular socket, short flat clamp/rail, rivets, center axle, cloth slot
- Must not contain: flag cloth, waving fabric, upright pole, base, weapon, lantern, labels, grid, or pivot cross

## Visual review

- True 90° top-down projection: PASS
- No side-view or upright-pole silhouette: PASS
- Flat socket and clamp lie parallel to image plane: PASS
- Clear local `+X` cloth attachment direction: PASS
- Rectangular child attachment slot is readable: PASS
- Cardboard/paper construction with exposed tan edge: PASS
- Wood/metal palette matches the Watchtower family: PASS
- One isolated component with clear chroma margin: PASS
- Internal axle and attachment openings remain separable for alpha extraction: PASS
- No flag cloth or parent layers baked in: PASS
- No clipping, cast shadow, or glossy 3D material: PASS

## Generation record

- Mode: built-in ImageGen
- Canvas: `1254 × 1254 px`
- Chroma key: `#ff00ff`

Final prompt summary: one low-profile top-down circular wood/metal pennant socket with a short flat +X clamping rail and rectangular cloth slot; separate die-cut cardboard construction; uniform magenta chroma; no flag fabric, upright pole, parent layers, labels, grid, perspective, shadows, or 3D rendering.

## Next gate

## Prepared runtime source

- Alpha layer: `assets/approved/canon/modules/fortress_ranged/watchtower__flag_mount__range_pennant_socket_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/watchtower__flag_mount__range_pennant_socket_v1.json`
- Tight rect: `1059 × 616 px`
- Socket/base pivot: `[308, 308] px`
- Transparent cloth-slot bbox: `[941, 234, 986, 395]`
- `cloth_anchor`: `[963, 314] px`, derived from the slot centroid
- Base position: `[0.24, 0.27]` normalized
- Scale relative to base footprint: `0.18`
- Composed size: `195 × 113 px`
- Draw order: `15`, below pennant, lantern, and weapon
- Alpha PNG size: approximately `957 KB`
- Visible magenta spill pixels: `0`

## Composed placement validation

- Upper-left platform placement: PASS
- Central socket clearance: PASS
- Entire mount remains inside the base footprint: PASS
- Cloth slot points toward local `+X`: PASS
- Mount remains readable at `0°/90°/180°/270°` weapon angles: PASS
- Weapon remains on the higher draw order when its envelope approaches the mount: PASS
- No clipping: PASS

Composite: `assets/staging/reviews/modules/fortress_ranged/watchtower__core_crossbow_range_pennant_socket_v1_composite.png`

Separate weapon-clearance grid: `assets/staging/reviews/modules/fortress_ranged/watchtower__range_pennant_socket_v1_weapon_clearance_grid.png`

After user approval of the placement:

1. lock the mount transform in the Watchtower assembly contract;
2. generate the complete four-frame red pennant wind loop in one source sheet;
3. normalize every cloth frame to the shared mount-side pivot and validate the assembled idle animation.

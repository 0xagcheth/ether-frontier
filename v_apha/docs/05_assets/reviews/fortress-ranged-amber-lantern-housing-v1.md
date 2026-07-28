# Fortress Ranged Amber Lantern Housing v1 Review

Candidate: `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_housing_v1_chroma.png`

Module ID: `fortress_ranged__ambient_child__amber_lantern_housing`

Status: **canon module; composed placement pending user confirmation**

## Module contract

- Family: `fortress_ranged`
- Shared by: Watchtower, Ranger, Tracker, Assassin
- Slot: `ambient_child`
- Contains: static physical lantern casing only
- Must receive later: separate amber glow/flame child frames
- Must not contain: base, socket, weapon, flag, glow, flame, VFX, labels, grid, or pivot marker

## Review

- True 90° top-down projection: PASS
- Flat cardboard tabletop construction: PASS
- Exposed tan outer and inner cut edges: PASS
- One isolated component with clean chroma margin: PASS
- Empty central aperture for animated glow: PASS
- No baked light, flame, or cast shadow: PASS
- Radial alignment and symmetry: PASS
- Semantic readability as a static lantern mounting at intended composed scale: PASS
- Semantic readability as an active lantern: pending first separate glow frame
- Visual distinction from the center socket: PASS, but the housing is deliberately more octagonal and ribbed

## Generation record

- Mode: built-in ImageGen
- Successful request: clean generation without image references after two reference-edit requests failed with network errors
- Canvas: `1254 × 1254 px`
- Chroma key: `#ff00ff`

Final prompt summary: one standalone static circular-octagonal lantern casing; exact overhead orthographic projection; dark blue-grey printed metal frame, warm wood insert, radial cage ribs, rivets, empty center aperture, exposed tan cardboard edges; uniform magenta chroma; no glow, flame, base, socket, weapon, flag, extra parts, perspective, shadow, labels, or 3D rendering.

## Prepared runtime source

- Alpha layer: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_housing_v1_alpha.png`
- Manifest: `assets/approved/canon/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_housing_v1.json`
- Tight rect: `1070 × 1067 px`
- Pivot: `[535, 533] px`
- Parent attachment: `base_token` at `[0.29, 0.72]` normalized
- Scale relative to base footprint: `0.18`
- Glow attachment: `glow_anchor` at housing center
- Draw order: `20`
- Central aperture transparency: PASS
- Visible magenta spill pixels: `0`

## Composed validation

- Base footprint stability: PASS
- Central weapon/socket clearance: PASS
- Housing remains inside the platform footprint: PASS
- Independent cardboard silhouette at composed scale: PASS
- No clipping: PASS
- Static housing reads as a compact mechanical lantern mount: PASS
- Active-lantern read: deferred until the separate amber glow child is composed

Review image: `assets/staging/reviews/modules/fortress_ranged/fortress_ranged__base_socket_lantern_housing_v1_review.png`

Transparent composite: `assets/staging/reviews/modules/fortress_ranged/fortress_ranged__base_socket_lantern_housing_v1_composite.png`

## Next gate

After user approval of the composed placement:

1. lock housing position and scale in the family assembly contract;
2. generate the complete four-frame amber glow loop in one consistent source strip;
3. normalize all glow frames to one scale and pivot;
4. compose the animation over this unchanged housing for visual QA.

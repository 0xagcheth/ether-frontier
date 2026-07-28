# Watchtower — Layered Runtime v2 Final Review

Status: **approved candidate — awaiting user confirmation**

## Deliverables

- Runtime atlas: `assets/approved/runtime/watchtower/watchtower_layered_runtime_v2.png`
- Source-of-truth manifest: `assets/approved/runtime/watchtower/watchtower_layered_manifest_v2.json`
- Human QA grid: `assets/staging/reviews/watchtower/watchtower_layered_review_grid_v2.png`
- Static composite preview: `assets/staging/reviews/watchtower/watchtower_layered_composite_preview_v2.png`
- Final destruction preview: `assets/staging/reviews/modules/fortress_ranged/watchtower__destroy_v1_final_preview.gif`

The production sources are intentionally modular rather than one overloaded source sheet. Their canonical chroma sheets and per-module manifests remain under `assets/approved/canon/modules/fortress_ranged/` and are enumerated by `sourceManifests` in the final manifest.

## Runtime atlas

- Object family: `fortress_ranged / watchtower` only
- Dimensions: `1024 × 1024 px`
- Format: transparent RGBA PNG
- File size: `979,759 bytes` — PASS under `5 MB`
- Runtime base footprint: `512 px`
- Sprite count: `31`
- Packing: tight trimmed rects with `4 px` separation
- Labels/grid/pivot crosses inside runtime: none
- Visible magenta spill: `0` pixels

## Included layers

- Base: stone/wood token
- Rotation: central socket and independently rotating crossbow
- Flag: mount plus four cloth frames
- Lantern: housing plus four glow frames
- Attack: four muzzle frames and separate projectile bolt
- Solid destruction: stone A/B/C, wood D, metal E
- Destruction effects: four dust frames and four spark frames

## Animation inventory

- `idle_flag`: 4 frames, looping
- `idle_lantern`: 4 frames, looping
- `attack`: 4 frames, one-shot
- `destroy_dust`: 4 frames, one-shot
- `destroy_sparks`: 4 frames, one-shot
- Aim rotation and projectile movement remain runtime transforms rather than baked frames
- Solid destruction pieces use independent physics records

## Manifest validation

- JSON parse: PASS
- Every atlas rect in bounds: PASS
- Atlas rect overlap: none
- Every moving layer has a pivot: PASS
- Attachments for object center, weapon socket, muzzle, flag, cloth, lantern, and glow: present
- Draw order: present
- Frame durations and loop/hold behavior: present
- Trim offsets and untrimmed runtime source sizes: present
- Base footprint remains stable across animations: PASS

## Visual validation

- True top-down/orthographic reading: PASS
- Matte cardboard/paper style: PASS
- Tan cut edges and ink outlines preserved at runtime scale: PASS
- No baked terrain, facade, side view, glossy 3D, or assembled animation frames: PASS
- Small glow, muzzle, spark, and projectile layers remain readable: PASS
- No clipping in runtime atlas or review grid: PASS

## Next gate

After user approval, wire this atlas and manifest into the Watchtower animation lab/site, demonstrate idle, aim, attack, projectile, and destroy behavior from atlas rects, then perform browser QA. Do not proceed to Ranger until that final in-site Watchtower validation passes.

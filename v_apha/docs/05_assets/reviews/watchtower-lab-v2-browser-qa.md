# Watchtower Atlas Lab v2 — Browser QA

Status: **passed — awaiting user in-browser confirmation**

## Runtime sources

- Atlas: `assets/approved/runtime/watchtower/watchtower_layered_runtime_v2.png`
- Manifest: `assets/approved/runtime/watchtower/watchtower_layered_manifest_v2.json`
- Site: `watchtower-lab/`
- Local URL: `http://127.0.0.1:4174/watchtower-lab/`

The renderer loads the single atlas plus its manifest. It does not load separately assembled Watchtower frames or the review grid.

## Implemented states

- `idle`: independently looping flag and lantern layers
- `aim`: crossbow rotation around its atlas pivot; base footprint remains fixed
- `attack`: muzzle frames at the manifest muzzle attachment plus a separate projectile
- `projectile`: repeated bolt travel along the current aim angle
- `destroy`: independent solid debris A/B/C/D/E, dust frames, and spark frames

## Runtime integration

- Sprite count reported by the page: `31`
- Atlas reported by text state: `watchtower_layered_runtime_v2.png`
- `bakedCompositeFrames`: `false`
- Child attachment points are derived from parent `sourceSize`, `pivotInSourcePx`, and normalized attachment positions
- Canvas: `720 × 720`, origin top-left, +X right, +Y down
- Deterministic hooks: `window.advanceTime(ms)` and `window.render_game_to_text()`

## Browser QA scenarios

- Idle composition and stable base: PASS
- Flag attachment and frame cycling: PASS
- Lantern housing/glow attachment: PASS
- Pointer/automatic aim rotation: PASS
- Early attack muzzle flash: PASS
- Projectile spawn/direction/travel: PASS
- Early destruction sparks above dust: PASS
- Mid destruction dust expansion and separate debris: PASS
- Late destruction debris drift/fade: PASS
- Canvas clipping during intact states: none
- Console errors: none reported

## Captures

- `output/web-game/watchtower-v2-idle/shot-0.png`
- `output/web-game/watchtower-v2-aim/shot-0.png`
- `output/web-game/watchtower-v2-attack-flash/shot-0.png`
- `output/web-game/watchtower-v2-attack-mid/shot-0.png`
- `output/web-game/watchtower-v2-destroy-sparks/shot-0.png`
- `output/web-game/watchtower-v2-destroy-burst/shot-0.png`
- `output/web-game/watchtower-v2-destroy-drift/shot-0.png`

## Final gate

After user confirmation in the browser, Watchtower becomes the locked baseline for Layered Object Pipeline v2. Only then may production proceed to the next object in the approved family order.

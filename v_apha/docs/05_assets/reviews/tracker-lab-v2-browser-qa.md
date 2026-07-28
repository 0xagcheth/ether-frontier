# Tracker Atlas Lab v2 — browser QA

Date: 2026-07-22
URL: `http://127.0.0.1:4174/watchtower-lab/?object=tracker`

## Result

- Lab loads `tracker_layered_manifest_v2.json` and `tracker_layered_runtime_v2.png` directly.
- Sprite count reported by runtime: `35`.
- Baked composite frames: false.
- Tested states: idle, aim, targeting, attack, projectile, impact, destroy.
- Targeting state exposes the current `targeting_rune_*` frame below `scan_optics_ring`.
- Scan ring rotation is independent while both ring and rune inherit weapon aim placement.
- Magazine remains attached to the long-range crossbow and inherits aim rotation.
- Crown and lantern remain static base children.
- Destroy detaches existing magazine, ring, crown and shared stone layers rather than using a baked destruction image.
- Automated browser client completed every state with exit code `0` and no reported console error.
- Screenshots and text states: `output/web-game/tracker-lab-*`.

Tracker is approved and the lab gate passes. Assassin production may begin.

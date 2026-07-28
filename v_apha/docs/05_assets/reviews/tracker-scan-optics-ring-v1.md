# Tracker scan optics ring v1 — visual candidate

Date: 2026-07-22

## Source

`assets/staging/candidates/modules/tracker/tracker__aim_child__scan_optics_ring_v1_chroma.png`

## Contract

- One standalone `aim_child` for Tracker.
- Exact overhead circular annulus, attached concentrically to the long-range-crossbow bearing.
- Independent runtime rotation around its own center.
- Dark printed metal, four brass tracker ticks, four symmetric mounting tabs, tan die-cut edge.
- Open center remains chroma and must become transparent after extraction.
- No weapon, platform, center socket, magazine, projectile, rune, glow, beam, text, grid, or shadow.

## Visual QA

- Source size: `1521 × 1034 px`.
- Subject bounds: `(404, 157)–(1108, 860)`.
- Safe margins: left `404 px`, top `157 px`, right `413 px`, bottom `174 px`.
- Canvas center matches the chroma key: pass; center hole is visually open.
- Circular top-down projection: pass.
- Connected cardboard component: pass.
- Clipping: none.
- Alpha extraction, pivot registration, weapon overlay and scan animation: complete and promoted to canon after continuation approval.

## Canon result

- Tight alpha: `702 × 701 px`.
- Pivot: `[351, 350]`.
- Center alpha: `0`; open center preserved.
- Runtime width: `0.25` of parent weapon width.
- Scan animation: continuous independent rotation at `42°/s`.
- Visible magenta spill: `0 px`.
- Four-angle local scan review: `0 / 22.5 / 45 / 67.5°` pass.

## Generation path

Built-in ImageGen with the approved Tracker long-range crossbow as material/projection reference. The first request failed at the backend network layer and produced no artifact; one built-in retry succeeded. No CLI or API fallback was used.

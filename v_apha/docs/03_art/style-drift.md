# Style Drift Check

## Purpose

AI-generated assets drift gradually. This document defines the mandatory drift check before any asset can be accepted.

An asset is rejected if it is beautiful but no longer belongs to Ether Frontier.

## Required Comparison Set

Before creating or accepting any visual asset, compare it against:

- the relevant Canon Asset for the same category, if one exists
- the nearest Canon Asset by material and scale
- the last 20 accepted assets in the same production lane, once that history exists
- `art-bible.md`
- `../05_assets/technical-asset-contract.md`

If fewer than 20 accepted assets exist, compare against all accepted Canon Assets plus all accepted assets in the lane.

## Drift Axes

Score each axis from 0 to 10:

| Axis | Reject If | Notes |
|---|---:|---|
| Camera / Projection | below 10 | Must stay near top-down with slight tilt: 85-90% top planes, 10-15% side thickness. Not full isometric, not 3/4 side-view, not perspective. |
| Palette | below 9 | Faction colors and material ramps must match. |
| Lighting | below 9 | Top-left lighting and shadow language must match canon. |
| Pixel Density | below 9 | No over-rendered micro-detail or under-detailed blobs. |
| Material Rendering | below 9 | Stone, wood, metal, cloth, skin, magic must match canon handling. |
| Outline Treatment | below 9 | No pure black object pixels, no modern anti-aliased contour. |
| Scale | below 10 | Object footprint and gameplay scale must match class. |
| Silhouette Readability | below 9 | Role must read at gameplay size. |
| Animation Restraint | below 10 for buildings | No body breathing or baseline jitter. |
| Faction Identity | below 10 | Horde, player, neutral, and UI identities must not mix incorrectly. |
| Layer Separation | below 10 for new/regenerated objects | Base/body, active part, ambient FX, attack FX, projectile/impact, and destroy FX must be separated where useful; baked full-object strips are legacy/export derivatives unless justified. |

## Automatic Rejection Language

Reject the prompt or asset if it uses or implies:

- slightly realistic
- realistic render
- hand painted
- digital illustration
- concept art style
- cinematic lighting
- 3D model
- octane
- blender
- smooth gradient
- painterly
- high-detail illustration
- realistic material
- soft bloom
- modern mobile game style
- vector icon style
- full isometric
- 3/4 side-view
- perspective camera

These words may appear only in a negative prompt or forbidden-style section.

## Drift Report Template

```text
Asset:
Compared against:
- Canon Asset 1:
- Canon Asset 2:
- Last accepted lane assets:

Scores:
- Camera / Projection:
- Palette:
- Lighting:
- Pixel Density:
- Material Rendering:
- Outline Treatment:
- Scale:
- Silhouette Readability:
- Animation Restraint:
- Faction Identity:
- Layer Separation:

Drift observed:
- 

Decision: ACCEPT / REVISE / REJECT
Required changes:
- 
```

## Decision Rule

Passing the style drift check does not approve an asset by itself. It only allows the asset to continue to the quality gate.

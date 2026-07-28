# Canon Asset Registry

## Purpose

This registry lists approved visual reference assets. Future generated or hand-authored assets must be compared against these references before acceptance.

Do not add an asset here because it is useful, current, live, or visually attractive. Add it only after it passes the full quality gate and is approved as a style reference.

## Canon Status Values

- `PROPOSED`: candidate reference under review.
- `CANON`: approved reference asset.
- `MISSING`: required reference slot with no current candidate.
- `DEPRECATED`: no longer authoritative, retained for history.
- `REJECTED`: evaluated and rejected as a reference.

## Required Canon Starter Set

The project should establish these 10-20 canon references before scaling asset production:

| Slot | Purpose | Status | Asset Path | Notes |
|---|---|---|---|---|
| Canon Cardboard Material | physical die-cut edge, matte print, stacked-layer construction | CANON | `assets/approved/canon/materials/cardboard_material_swatch_v1_chroma.png` | Approved 2026-07-21. Cross-family material reference; not a runtime sprite. |
| Canon Tree Oak | broadleaf foliage, trunk, shadow, scale | MISSING | `assets/approved/canon/environment/tree_oak.png` | Create and approve before environment batch production. |
| Canon Pine | conifer silhouette and dark foliage | MISSING | `assets/approved/canon/environment/tree_pine.png` | Create and approve before environment batch production. |
| Canon Rock | stone material and resource readability | MISSING | `assets/approved/canon/environment/rock_a.png` | Create and approve before environment batch production. |
| Canon Road / Path | ground value hierarchy | MISSING | `assets/approved/canon/environment/road_path.png` | Background reference, not a cutout sprite. |
| Canon Grass / Dirt | non-path terrain material | MISSING | `assets/approved/canon/environment/terrain_grass_dirt.png` | Approve gameplay-scale crops. |
| Canon Watchtower | base player tower style | MISSING | `assets/approved/canon/buildings/watchtower_idle.png` | First required building reference. |
| Canon Economy Building | noncombat building style | MISSING | `assets/approved/canon/buildings/sawmill_idle.png` | Required before economy-building batch. |
| Canon Magic Tower | captured magic / obelisk language | MISSING | `assets/approved/canon/buildings/obelisk_idle.png` | Required before magic-tower batch. |
| Canon Horde Runner | enemy body/scale/motion reference | MISSING | `assets/approved/canon/enemies/fast_walk_front.png` | Required before enemy batch production. |
| Canon Resource Icon | UI/resource icon scale | MISSING | `assets/approved/canon/ui/res_gold.png` | Required before HUD icon batch. |
| Canon UI Button | HUD material and interaction language | MISSING | TBD | Must be created or selected later. |
| Canon Hero | hero scale and player-character material | MISSING | TBD | Must be created or selected later. |
| Canon Projectile | projectile scale and glow discipline | MISSING | TBD | Must be selected per damage family. |
| Canon Impact | hit VFX scale and timing | MISSING | TBD | Must be selected per damage family. |

## Canon Promotion Requirements

An asset may become `CANON` only if:

- It passes `../07_pipeline/quality-gate.md`.
- It passes `../03_art/style-drift.md` with no axis below threshold.
- It is reviewed at gameplay scale and native scale.
- It has stable technical data: atlas, frame count, pivot, and naming.
- It has an owner and date.
- It has notes explaining what future assets should copy from it.

## Canon Entry Template

```text
Canon Name:
Status:
Asset Path:
Atlas Path:
JSON Path:
Owner:
Approved Date:
Category:
Use As Reference For:
Do Copy:
- 
Do Not Copy:
- 
Known Limitations:
- 
Review Score:
- Style:
- Lighting:
- Readability:
- Palette:
- Scale:
- Atlas:
- Engine Ready:
```

## Rule

If there is no Canon Asset for a category, the first production task is to create or nominate one. Large-scale generation should not proceed on text prompts alone.

## Canon Cardboard Material v1

Canon Name: Cardboard Material Swatch v1  
Status: CANON  
Asset Path: `assets/approved/canon/materials/cardboard_material_swatch_v1_chroma.png`  
Atlas Path: N/A — material reference, not runtime  
JSON Path: N/A  
Owner: Ether Frontier art pipeline  
Approved Date: 2026-07-21  
Category: Cross-family material reference  
Use As Reference For: all layered towers, buildings, resources, decor, and rigid cardboard modules  
Do Copy:
- exposed tan compressed-cardboard cut edges;
- matte fibrous printed face;
- shallow stacked cutout separation;
- simplified screen-printed material patterns;
- slightly imperfect physical die-cut contour.

Do Not Copy:
- the calibration disc composition;
- four-quadrant layout;
- geometric sample shapes;
- magenta chroma background into runtime pixels.

Known Limitations:
- Material-only reference; it establishes neither object silhouette nor gameplay scale.

Review Score:
- Style: PASS
- Lighting: PASS
- Readability: PASS
- Palette: PASS
- Scale: N/A
- Atlas: N/A
- Engine Ready: N/A

# Sprite Bible

## Responsibility

This document defines object-level sprite rules. Per-object prompt text lives in `../05_assets/asset-prompt-bible.md`.

## Sprite Classes

- Units: enemies, heroes, bosses.
- Towers: player combat buildings and support structures.
- Economy: sawmill, quarry, resource structures.
- Environment: trees, rocks, terrain props.
- UI sprites: icons, cards, buttons, resource glyphs.
- VFX sprites: projectiles, impacts, magic bursts.

## Object Atlas Rule

Every visual object must have its own sprite atlas.

- One object per atlas.
- PNG plus JSON.
- Maximum 5 MB per atlas.
- No unrelated objects in the same atlas.
- Projectiles and impacts may live with the owning object only when they are unique to that object.

The deleted shared demo atlas was legacy prototype debt and must not be recreated as the production model.

## Layered Object Pipeline v2

All new or regenerated gameplay objects should be authored as layered tabletop tokens, not as fully baked whole-object animation strips by default.

Each object remains one object family and one atlas, but the atlas contains named modular layers. The runtime composes those layers like a stacked paper model:

- `base_token`: locked footprint / cardboard platform / ground-facing body mass.
- `body_static`: non-moving structural silhouette, if separate from the base.
- `active_part`: rotatable weapon, lens, crystal, wheel, tool arm, or other gameplay-facing component.
- `ambient_fx`: flame, flag cloth, smoke, rune blink, glow, gear motion, liquid, sparks.
- `attack_fx`: charge, muzzle flash, recoil mark, impact start.
- `projectile`: owning-object projectile when unique.
- `impact`: owning-object hit effect when unique.
- `destroy_fx`: debris, collapse overlays, smoke, ruin fragments.

The old horizontal strips are still allowed as export/runtime derivatives, but they are no longer the preferred source of truth for buildings, towers, resources, and decor. The source of truth should be a layered atlas plus a manifest that declares pivots, attachments, draw order, and animation clips.

For moving units, the same principle applies where useful: keep rigid body parts, weapon arcs, projectiles, shields, capes, glows, and death debris separable when it improves smoothness or reduces duplicated pixels. Fully baked unit strips are acceptable only when layer separation would not improve runtime clarity.

## Runtime Packed Atlas + Human Review Grid

Layered objects use two atlas views:

- Runtime atlas: compact transparent PNG for the engine. It uses tight `rect` entries in JSON, not fixed empty 512px cells. This keeps files smaller and loading more efficient.
- Review grid: separate QA PNG for humans. It may use fixed cells, labels, grid lines, pivot crosses, and dark/checker backgrounds. It must never be required by runtime code.

Do not make the runtime atlas convenient for human inspection at the expense of engine efficiency. The manifest must make runtime extraction deterministic:

- every sprite has a precise `rect`;
- every sprite has `pivotPx` or normalized `pivot`;
- every sprite has a semantic layer name;
- review-only previews are excluded from the runtime atlas;
- large grouped effects, especially debris, should be split into independent sprites unless deliberately authored as one overlay.

Fixed-cell atlases are acceptable only for review, debugging, or early validation. Production runtime should prefer tight packed rectangles plus JSON.

## Layer Manifest Requirements

A layered object JSON must declare:

- atlas image filename and pixel size;
- explicit rectangle for every runtime layer/frame;
- optional review-grid cell only when documenting a human QA sheet;
- one named sprite entry per layer/frame;
- per-layer pivot, in normalized `[0..1]` coordinates;
- attachment points in both local pixels and semantic names;
- draw order from back to front;
- animation clips, frame order, frame duration, loop/hold behavior;
- runtime-controlled transforms, such as `rotate_to_target`, `wind_direction`, `flame_loop`, or `charge_amount`;
- body footprint lock and maximum accepted atlas file size.

Example required attachment names for a tower:

- `object_center`
- `weapon_pivot`
- `muzzle_anchor`
- `flag_anchor`
- `lantern_anchor`
- `projectile_spawn`

If a layer rotates, its pivot must be visible in the manifest and validated in preview. If a layer animates, the animation must not move the base/body anchor unless that motion is the explicit gameplay event.

## Cutout Rule

Source generations may use black as a cutout key. Final runtime assets should have transparent backgrounds where the pipeline expects transparency.

Object pixels must not contain pure black or near-black. Dark outlines should use deep green-grey, purple-grey, or blue-grey depending on faction/material.

## Scale And Silhouette

Sprites must remain readable at gameplay size. Primary role must be visible before internal detail.

Each object needs:

- Strict top-down readability.
- Stable canvas/cell dimensions across all actions.
- Stable anchor/baseline.
- Consistent scale across projections.
- Distinct silhouette against other objects in the same role.

For layered objects, the locked scale is measured on the composed base/body footprint, not on transient effects. Rotating weapons, flag cloth, flame, muzzle flashes, projectiles, and debris may extend beyond the body footprint only if the full atlas cell still has safe margins and the base pivot remains unchanged.

## Layered Object Baseline

No previous generated Watchtower or layered demo is active in `v_beta`.

The first new baseline must be created through
`assets/staging/prompts/restart_all_layered_sprite_atlases_clean_v1.md`, pass the
visual and technical gates, and be registered in the Canon Asset Registry before
another object begins. Until then, no image is a visual reference.

The manifest and technical asset contract define the reusable format. They do not
authorize copying the Watchtower silhouette, weapon, body, or decorative parts to
other objects.

## Source Material

Derived from `../05_assets/asset-prompt-bible.md` and the technical asset contract.

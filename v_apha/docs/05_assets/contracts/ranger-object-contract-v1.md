# Ranger / Garrison Ranger — Layered Object Contract v1

Status: **projection-master production**
Object ID: `ranger`
Family: `warden_ranged_lineage`
Pipeline: `layered-object-v2`

## Identity

Ranger is a visibly staffed/refitted hunter-green firing platform. It uses the Warden material language but does not reuse the Watchtower body, crossbow, flag, lamp, projectile, or debris art.

Readable identity:

1. irregular reinforced firing platform with hunter-green fittings;
2. rapid-volley crossbow with twin launch rails;
3. tall top-view fletched-bolt rack and separate magazine;
4. green-amber hunting optics;
5. small staffed-position markers represented as flat cardboard equipment/boot/seat tokens, never side-view people.

## Projection

- True top-down orthographic 90°.
- Every part lies in the board-parallel plane.
- No facade, upright personnel, side wall, tall perspective, isometric ellipse, horizon, or cinematic camera.
- Nominal height is represented by nested flat cardboard layers and tight contact shadows.

## Object-owned modules

- `ranger__base_body__garrison_platform`
- `ranger__mount_socket__rapid_bearing`
- `ranger__active_primary__rapid_crossbow`
- `ranger__ammo_child__bolt_magazine`
- `ranger__utility_child__fletched_bolt_rack`
- `ranger__optics_child__hunting_optics`
- `ranger__staff_marker__position_01..02`
- `ranger__ambient_child__optics_glint__frame_01..04`
- `ranger__ambient_child__rack_vibration__frame_01..04`
- `ranger__attack_release__green_amber_flash__frame_01..04`
- `ranger__projectile__long_fletched_bolt`
- `ranger__impact__hunting_hit__frame_01..04`
- independent platform, arrow-rack, magazine, optics, weapon, stone, wood and fitting debris
- `ranger__destroy_fx__dust__frame_01..04`
- `ranger__ruin_state__collapsed_garrison`

## Runtime behavior

- Base/body footprint remains pixel-static.
- Crossbow, magazine and hunting optics rotate as one aim group.
- Rack stays attached to the platform and only swaps vibration frames.
- Optics glint loops independently.
- Attack flash is one-shot and muzzle-aligned.
- Projectile points along velocity.
- Destroyed modules become independent bodies; ruin state replaces the intact platform.

## Must differ from Watchtower

- no broken-ring Watchtower body clone;
- no lightweight single crossbow;
- no red range pennant;
- no Watchtower square signal lamp;
- no simple short wooden bolt;
- no reuse of Watchtower debris.

## Projection-master gate

The assembled master must show one coherent Ranger platform only. No labels, grid, separated parts, animation variants, projectile, impact, debris, or review overlays. Decomposition begins only after visual approval.

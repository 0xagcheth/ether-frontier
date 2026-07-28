# Ether Frontier — Garrison Ranger Layered Object Contract

## Source of truth

Gameplay definition: `game/game.js`, `watchtowerSpecializations.infantry`.

- Name: Garrison Ranger.
- Role: anti-infantry.
- Attack: fast crossbow.
- Special system: ether hunting optics.
- Progression identity: Hunter's Mark, Execute, Chain Shot.
- Projectile family: physical crossbow bolts.

This object must not inherit Watchtower's silhouette or weapon. It may reuse only
the approved cardboard material language and compatible attachment conventions.

## Logic lock

- Weapon: compact rapid crossbow, not a ballista, cannon, firearm, or magic staff.
- Ammunition: short physical bolts held in a visible bolt magazine/rack.
- Release: mechanical string snap and recoil only.
- Projectile: separate barbed hunting bolt, aligned to velocity.
- Impact: embedded bolt plus compact paper/cardboard hit fragments.
- Forbidden attack FX: muzzle flame, gun smoke, shell casing, cannon blast,
  explosive fireball, energy beam.
- Targeting: separate ether hunting optic that rotates with or tracks the weapon.
- Hunter's Mark: separate subtle targeting/rune child layer, never baked into the
  base or projectile.

## Stable structure

1. `ranger__base_body__garrison_post`
   - stable top-down footprint;
   - squat reinforced cardboard garrison platform;
   - no weapon, optic, ammo, flag, projectile, or effect baked in.

2. `ranger__mount_socket__rapid_crossbow_bearing`
   - separate low circular bearing;
   - shares the base attachment anchor but keeps its own cardboard edge.

3. `ranger__mount_child__central_pivot_cap`
   - small independent axle cap centered inside the bearing;
   - remains a separate glued cardboard/metal layer.

4. `ranger__active_primary__rapid_crossbow`
   - compact wide-limbed hunting crossbow;
   - lighter and faster-looking than Watchtower's simple crossbow;
   - separate rotation pivot.

5. `ranger__aim_child__ether_hunting_optic`
   - separate lens/ring assembly;
   - attached to the weapon;
   - may rotate or pulse independently.

6. `ranger__ammo_child__bolt_magazine`
   - separate magazine/quiver of short bolts;
   - mounted near the crossbow without obscuring its silhouette.

7. `ranger__utility_child__bolt_rack`
   - separate platform-mounted reserve bolt rack;
   - visually communicates rapid anti-infantry fire.

8. `ranger__identity_child__hunter_trim`
   - restrained ranger marking made from cut paper/cardboard;
   - no readable letters or UI symbols.

## Animation and owned effects

- `optic_scan_01..04`: subtle lens/ring motion.
- `hunter_mark_01..04`: targeting mark animation.
- `crossbow_release_01..04`: mechanical release/recoil; no flame.
- `projectile_barbed_bolt`: standalone physical projectile.
- `impact_barbed_hit_01..04`: embedded-bolt/paper-chip hit.
- `destroy_piece_01..N`: independent wood, cardboard, metal-bearing, optic-glass,
  and bolt-rack debris.
- `destroy_dust_01..04`: matte cardboard/stone dust only.

## Visual direction

- True top-down orthographic tabletop read.
- Child-made cut-cardboard construction with slightly uneven cut edges.
- More cartoon-like than photoreal, while retaining believable corrugated
  cardboard thickness and matte paper texture.
- Crayon/painted markings restrained enough to preserve material readability.
- Slight dirt, abrasion, glue marks, and imperfect alignment.
- Every mounted element has a small local contact shadow that makes it read as a
  separately glued cardboard layer.
- No facade, side view, tall perspective, isometric camera, glossy 3D, plastic,
  baked terrain, labels, or text.

## Production sequence

Generate and validate modules separately at large readable scale:

1. base body;
2. bearing;
3. rapid crossbow;
4. hunting optic;
5. bolt magazine and reserve rack;
6. identity trim;
7. animation children;
8. projectile and impact;
9. destruction pieces and dust.

Only after all modules pass visual review:

1. remove chroma key into alpha;
2. calculate tight rects and pivots;
3. pack one compact Ranger-only runtime atlas;
4. author manifest JSON as source of truth;
5. render separate review grid and composite/animation proofs;
6. run size, clipping, pivot, attachment, style, and weapon-logic validation.

Do not begin Fortress Ballista until Ranger passes both visual and technical QA.

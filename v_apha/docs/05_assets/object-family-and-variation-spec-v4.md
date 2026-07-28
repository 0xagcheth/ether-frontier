# Ether Frontier — Object Families and Variation Specification v4

Status: **authoritative production specification**  
Date: 2026-07-22  
Scope: all layered towers and buildings

## 1. Purpose

Define the complete object system before restarting image generation.

The project does **not** build one generic tower and replace its weapon. It builds recognizable object-owned constructions using a common technical grammar. Two objects may share anchors, scale rules, materials, or genuinely identical hardware without sharing the same visible body.

This specification supersedes the reuse decisions in `modular-object-family-plan.md` and `object-module-registry.json` wherever they imply that upgrade lineage authorizes an identical base/body silhouette.

## 2. Non-negotiable visual rules

### 2.1 Projection

- Every structural sprite is true top-down orthographic 90°.
- No facade, side, rear, elevation, tall-tower, isometric, or cinematic perspective.
- A nominally vertical element must be redesigned as a readable plan-view cardboard footprint.
- Weapons rotate in the board plane and must be drawn from above.
- Flags are flat top-view cloth cutouts attached radially around a top-view mount; never side-view banners.
- Barrels, bows, lenses, lanterns, crystals, gears, tools, chains, braziers, shells, racks, and debris use the same top-view camera as their parent.

### 2.2 Physical cardboard construction

Every visible component, including animation and VFX components, is a separate physical tabletop piece:

- matte printed paper face;
- exposed tan die-cut cardboard edge;
- shallow stacked-card separation only;
- dark local-color ink edge, never pure-black comic outline;
- simplified printed stone, wood, cloth, metal, crystal, flame, smoke, rune, or magic pattern;
- no glossy 3D bevel, realistic transparency, volumetric smoke, realistic flame, or photoreal material.

Fire, smoke, glow, lightning, runes, poison, dust, and impacts are stylized die-cut paper effect tokens. They are not realistic particles painted over another layer.

### 2.3 Structure and motion

- `base_body` owns the locked footprint and never moves during idle or attack.
- Every moving or changing part is a child layer.
- A child animation changes only that child; it never redraws the complete object.
- Rotatable weapons, lenses, crystals, prisms, tools, barrels, and launchers have explicit pivots.
- Flags, flames, smoke, gears, runes, vines, birds, liquid, and glow have independent animation frames and anchors.
- Unique projectiles, impacts, and debris belong to their owning object package.
- Shared art is permitted only when the physical part is canonically the same object, not merely similar in purpose.

## 3. Reuse levels

| Level | Meaning | May be visually identical? | Examples |
|---|---|---:|---|
| `standard` | Technical convention only | No | scale, atlas schema, anchor names, cut-edge thickness |
| `material_kit` | Same printed material language | Texture language only | Warden stone, warm timber, paladin ivory |
| `hardware_interface` | Compatible mounting geometry | Only the hidden/neutral connector | socket diameter, rail spacing, rune receiver |
| `shared_module` | Literally the same physical produced part | Yes | an explicitly inherited ranger bolt or identical lantern token |
| `object_owned` | Defines identity or silhouette | No | body, primary mechanism, signature trim, signature FX |

Default classification is `object_owned`. A module becomes shared only when this document explicitly names it as shared.

## 4. Source-generation units

Never generate a complete atlas on one ImageGen sheet.

| Unit | Contents | Layout |
|---|---:|---|
| projection master | one assembled object used only to lock silhouette and attachment plan | one centered object |
| base/body | one static object-owned footprint | one centered module |
| static child | one child; at most two genuinely related variants | one module or 2 columns |
| animation family | frames of one child only | 2×2 for 4 frames; 3×2 for 6 frames |
| projectile | one projectile; trail generated separately | one centered module |
| impact/FX family | one effect animation only | 2×2 or 3×2 |
| debris material family | up to eight independent pieces of one material family | 4×2 |

Generated images contain no labels, grid, pivot marks, or assembled preview. Deterministic tooling adds those to the human QA grid.

## 5. Universal technical slots

- `base_body`
- `mount_socket`
- `active_primary`
- `active_secondary_*`
- `identity_trim_*`
- `ambient_child_*`
- `attack_charge_*`
- `attack_release_*`
- `projectile_*`
- `impact_*`
- `destroy_piece_*`
- `destroy_fx_*`
- `ruin_state`

Required anchors where applicable: `object_center`, `active_primary_pivot`, `secondary_anchor_*`, `ambient_anchor_*`, `muzzle_anchor`, `projectile_spawn`, `impact_center`, and `debris_origin_*`.

## 6. Family map

Families describe compatible art language and attachment conventions. They do not automatically authorize a shared body.

| Family | Objects | Shared scope |
|---|---|---|
| `warden_ranged_lineage` | watchtower, ranger, tracker, assassin | Warden materials and compatible ranged attachment vocabulary |
| `heavy_air_defense` | ballista, scorpion, hailstorm | reinforced materials, heavy swivel interface, heavy ammunition scale |
| `siege_artillery` | cannon, mortar, grapeshot | artillery materials, turntable/recoil interface, shell storage scale |
| `ritual_constructs` | obelisk, beacon, pal-ward, pal-censer, pal-reliquary, mage-frost, mage-tesla, mage-prism | ritual receiver geometry and faction material kits |
| `living_pathfinder` | palisade, hunt-snare, hunt-roost, hunt-hive | living wood, vines, rope, thorn and leaf material kits |
| `economy_worksites` | sawmill, quarry | worksite scale, storage connectors, pulley/tool attachment conventions |
| `strategic_unique` | castle, spawn-cave | global cardboard rules only |

## 7. Per-object identity contracts

### 7.1 Warden ranged lineage

#### `watchtower` — Warden's Post

- **Object-owned base/body:** compact circular stone lookout post; exposed tan edge; dedicated flag and lantern stations.
- **Primary:** one lightweight simple crossbow in exact plan view.
- **Secondary:** small central bearing, top-view range pennant mount, top-view lantern casing.
- **Animated children:** radial flag cloth, paper flame/glow, compact paper muzzle flash.
- **Projectile/impact:** simple wooden bolt; no inherited ranger bolt.
- **Destroy:** watch-post stone pieces, simple crossbow fragments, wood/cardboard chips.
- **May share:** Warden stone/wood material kit only.

#### `ranger` — Garrison Ranger

- **Object-owned base/body:** visibly staffed/refitted firing platform with hunter-green fittings; not the Watchtower body copied unchanged.
- **Primary:** rapid volley crossbow.
- **Secondary:** tall fletched-bolt rack, bolt magazine, hunting optics, staffed-position markers.
- **Animated children:** optics glint, rack vibration, magazine/limb snap, green-amber attack flash.
- **Projectile/impact:** long fletched ranger bolt and sharp hunting impact.
- **Destroy:** platform sections, spilled arrows, rack and optics fragments.
- **May share:** Warden material kit and compatible socket dimensions; establishes the ranger bolt as a possible explicit descendant module.

#### `tracker` — Crown Tracker

- **Object-owned base/body:** royal spotter construction with unmistakable rune-optics silhouette and regal-blue/rune-gold surface plan; not Ranger with a trim overlay.
- **Primary:** precision long-bolt launcher designed around the optics ring.
- **Secondary:** large rotating scan ring, royal range markers, crown trim.
- **Animated children:** optics scan, targeting rune, radial royal cloth markers.
- **Projectile/impact:** may inherit the ranger bolt only if scale and attachment validation pass; owns its targeting trail/impact.
- **Destroy:** broken optics ring, rune plates, royal cloth and launcher fragments.
- **May share:** ranger bolt by explicit reference; Warden material kit and socket standard.

#### `assassin` — Shadow Archer

- **Object-owned base/body:** low hooded/shrouded sniper perch with a broken dark silhouette; no circular Watchtower/Ranger body clone.
- **Primary:** single heavy sniper-ballista mechanism.
- **Secondary:** critical lens and concealed ammunition cradle.
- **Animated children:** radial shroud flaps, lens charge, restrained violet-amber critical spark.
- **Projectile/impact:** heavy sniper bolt and needle-sharp critical impact.
- **Destroy:** shroud pieces, dark timber, lens shards, heavy-bolt fragments.
- **May share:** Warden attachment vocabulary only; projectile is object-owned unless later explicitly approved.

### 7.2 Heavy air defense

#### `ballista` — Fortress Ballista

- **Object-owned base/body:** reinforced cold-stone/steel anti-air emplacement with heavy bolt storage integrated into its top silhouette.
- **Primary:** huge single heavy swivel ballista.
- **Secondary:** amber tracking lens, tension mount, heavy bolt rack.
- **Animated children:** lens tracking, limbs/string release, recoil slide.
- **Projectile/impact:** armored heavy bolt and metallic bolt-shatter impact.
- **May share:** establishes heavy swivel interface and heavy bolt family.

#### `scorpion` — Sky Scorpion

- **Object-owned base/body:** harpoon carriage balanced by a segmented scorpion-tail counterweight; tail silhouette must dominate recognition.
- **Primary:** ether harpoon launcher, not a normal ballista.
- **Secondary:** articulated counterweight tail and harpoon cradle.
- **Animated children:** tail sway, harpoon charge, violent recoil.
- **Projectile/impact:** may share ballista shaft scale, but owns ether harpoon head, trail, and execution impact.
- **May share:** heavy swivel interface and selected heavy-chassis hardware only.

#### `hailstorm` — Hailstorm Ballista

- **Object-owned base/body:** wide anti-swarm battery shaped around a fan rack and string drum.
- **Primary:** multi-bolt repeater fan.
- **Secondary:** fan-loaded rack, spinning string drum, bolt feed.
- **Animated children:** drum rotation, bolt settling, rapid volley flicker.
- **Projectile/impact:** unique spread of small bolts and swarm scatter impact.
- **May share:** heavy swivel interface and heavy material kit only.

### 7.3 Siege artillery

#### `cannon` — Field Cannon

- **Object-owned base/body:** ramshackle stone-and-timber recoil carriage.
- **Primary:** long alchemical cannon barrel.
- **Secondary:** breech chamber, recoil rails, fuse and shell cradle.
- **Animated children:** fuse ember, muzzle smoke token, barrel/carriage recoil.
- **Projectile/impact:** heated dark-bronze cannonball and amber debris-ring explosion.
- **May share:** artillery turntable interface and siege material kit.

#### `mortar` — Siege Mortar

- **Object-owned base/body:** compact armored shell platform built around a broad top footprint and heavy-shell stacks.
- **Primary:** short wide mortar mouth represented as a plan-view concentric tube, never a side-pointing pipe.
- **Secondary:** top-view elevation cradle, breech glow, shell racks.
- **Animated children:** vent smoke, breech glow, recoil marker, smoke ring.
- **Projectile/impact:** heavy shell and broad ground burst.
- **May share:** artillery turntable and shell-storage connector scale only.

#### `grapeshot` — Grapeshot Battery

- **Object-owned base/body:** wide synchronized battery whose silhouette follows a radial/fanned breech system.
- **Primary:** seven-barrel fan in plan view.
- **Secondary:** synchronized breech rack and pellet hoppers.
- **Animated children:** fuse embers, broad release flash, spread smoke.
- **Projectile/impact:** pellet fan and wide low scatter impact.
- **May share:** artillery turntable/recoil interface only.

### 7.4 Ritual constructs

#### `obelisk`

- **Body:** captured-void ritual receiver with gold rune bands; low plan-view monolith token, not a tall side-view crystal.
- **Active:** floating/rotating void shard footprint and lightning emitter.
- **Children:** rune pulse, hover offset marker, violet paper arcs.
- **Shot:** branching void bolt and arc-shatter impact.
- **Share:** fortress-captured-void material kit and ritual receiver interface.

#### `beacon`

- **Body:** bright sun-seal construct with a broad radial halo silhouette; never a side-view lighthouse.
- **Active:** solar lens and halo shutters.
- **Children:** lens pulse, top-view brazier flames, radial light rays.
- **Shot:** sun bolt and radiant halo impact.
- **Share:** ritual receiver interface only.

#### `pal_ward` — Sanctum Ward

- **Body:** low ivory/gold holy seal plate with four readable ward points.
- **Active:** rotating rune ring and hovering sigil token.
- **Children:** warm pulse rings and compact lower-body aura; no projectile.
- **Share:** paladin material kit and ritual receiver interface.

#### `pal_censer` — Censer Spire

- **Body:** radial holy censer construct designed from above, with four chain sockets.
- **Active:** four individual top-view censers/braziers.
- **Children:** chain swing arcs, flame tokens, incense-smoke paper curls.
- **Shot:** white-gold holy-fire comet and burn-pool impact.
- **Share:** paladin material kit; no body sharing with Pal Ward.

#### `pal_reliquary` — Reliquary Bastion

- **Body:** squat armored ivory/gold reliquary with shutter geometry.
- **Active:** smite emitter/hammer-of-light mechanism and relic crystal.
- **Children:** charge pulse, stained-glass shimmer, armor shutters.
- **Shot:** heavy light spear and white-gold stun detonation.
- **Share:** paladin material kit only.

#### `mage_frost` — Frost Conduit

- **Body:** obsidian-teal conduit receiver with a snowflake/crystal-cluster plan silhouette.
- **Active:** frost focus gem and rotating ice-crystal rings.
- **Children:** ring rotation, cyan pulse, paper frost-mist curls.
- **Shot:** spinning ice shard and frost slow-ring impact.
- **Share:** mage copper/gold rune kit and ritual interface.

#### `mage_tesla` — Storm Coil

- **Body:** copper-and-arcane-steel radial coil plate; no side-view Tesla spire.
- **Active:** ether orb held by top-view rune prongs.
- **Children:** coil rings, discrete cyan paper lightning arcs, orb charge.
- **Shot:** branching lightning token and chain-arc impact.
- **Share:** mage copper/gold rune kit and ritual interface.

#### `mage_prism` — Void Prism

- **Body:** short rune receiver with a large multi-facet prism footprint.
- **Active:** rotating prism plate, mana core, beam splitters.
- **Children:** facet glints and charge tokens.
- **Shot:** dense refracting orb/lance and large arcane shockwave.
- **Share:** mage rune kit and ritual interface only.

### 7.5 Living Pathfinder structures

#### `palisade`

- **Body:** reinforced living-wood wall footprint with unmistakable stake rhythm.
- **Active:** thorn-launch arm.
- **Children:** independent vines, thorns, green pulse.
- **Shot:** wooden thorn stake and splinter-vine impact.

#### `hunt_snare` — Bramble Snare

- **Body:** low camouflaged bramble ring and hidden trigger plate.
- **Active:** independent closure jaws/net-vines.
- **Children:** tripwire glow and individual leaves.
- **Attack:** closure frames and thorn burst; no projectile.

#### `hunt_roost` — Hawk's Roost

- **Body:** timber/rope marksman platform with radial green camo sections; must not become a Watchtower body.
- **Active:** heavy hunting longbow/ballista rig.
- **Secondary:** hawk token and ranging optics.
- **Children:** hawk wing/ruffle frames, optics glint, radial canvas movement.
- **Shot:** precision fletched bolt and sharp critical impact.

#### `hunt_hive` — Toxic Hive

- **Body:** gnarled stump/hive footprint with readable comb-cell clusters and poison reservoir.
- **Active:** toxin vents or glob launcher.
- **Children:** liquid surface, venom drips, spore tokens, comb glows.
- **Shot:** poison glob/spore cluster and lingering splash cloud.

Living objects may share rope, vine, thorn, leaf, sap, and splinter material kits. Their bodies and active mechanisms remain object-owned.

### 7.6 Economy worksites

#### `sawmill`

- **Body:** timber work-yard/hut roof footprint with log bed and storage zones.
- **Active:** saw wheel and belt/gears.
- **Children:** wheel rotation, belt frames, sawdust tokens, chimney-smoke curls.
- **Destroy:** roof/beam sections, logs, saw fragments.

#### `quarry`

- **Body:** open rock-pit footprint with cut-block stacks.
- **Active:** pick-arm derrick and pulley.
- **Children:** arm motion, pulley rotation, basket, dust tokens.
- **Destroy:** derrick pieces, block/rubble families, broken pulley.

Sawmill and Quarry may share neutral worksite connectors and generic rope/wood hardware only. They do not share the visible base/body.

### 7.7 Strategic unique objects

#### `castle` — Grimhold

- Entire footprint is object-owned: keep, rampart/roof sections, gate, seal crystal, banners, braziers, breach modules, ruin state, large debris families.
- No tower-family chassis reuse.
- Large scale does not permit a facade-dominant camera; top planes remain primary.

#### `spawn-cave` — Voidrift Spawn Cave

- Entire footprint is object-owned: jagged rim, void opening, vortex, veins, corruption drips, spawn flare, rock and void debris.
- No fortress or ritual chassis reuse.
- The cave mouth is a top-view opening/rim, not a front-facing arch entrance.

## 8. Approval order

1. Approve this document.
2. Approve universal cardboard material/cut-edge swatches for stone, wood, metal, cloth, flame/FX, crystal/magic, and organic material.
3. For Watchtower, approve one assembled top-view projection master only.
4. Generate and approve Watchtower modules one source unit at a time.
5. Assemble family core/addon packages only after visual approval establishes which modules are genuinely identical.
6. Continue one object at a time. Do not generate the next object before visual and technical approval of the current object.

## 9. Per-object documentation gate

Before ImageGen, every object receives a short object contract containing:

- identity sentence and silhouette test;
- object-owned base/body diagram;
- module inventory and ownership (`shared_module` or `object_owned`);
- top-view redesign notes for nominally vertical elements;
- anchors, pivots, draw order, and footprint;
- separate source-generation calls and layouts;
- animation ownership;
- projectile/impact/debris ownership;
- explicit `must differ from` list;
- visual and technical acceptance checklist.

No ImageGen prompt may introduce a module not present in the approved object contract.

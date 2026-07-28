# GRIMHOLD Asset Generation Manifest

Source prompt bible: `docs/05_assets/asset-prompt-bible.md`

## Output Roots

- Incoming tool exports: `assets/staging/incoming/`
- Normalized candidates: `assets/staging/candidates/<family>/`
- Approved masters: `assets/approved/masters/<family>/`
- Directional enemies: `assets/runtime/sprites/enemies/`
- Buildings: `assets/runtime/sprites/buildings/`
- Environment and resources: `assets/runtime/sprites/environment/`
- UI icons: `assets/runtime/sprites/ui/`
- Generated prompt working files: `assets/staging/prompts/`

## Generation Batches

### Batch 1 - Resources And Decor

- `tree_oak.png`
- `tree_oak_grow.png`
- `tree_pine.png`
- `tree_pine_grow.png`
- `rock_a.png`
- `rock_b.png`
- `rock_c.png`
- `rock_grow.png`
- `res_gold.png`
- `res_wood.png`
- `res_stone.png`
- `backgroud.png`

### Batch 2 - Base Buildings

- `watchtower_idle.png`, `watchtower_attack.png`, `watchtower_destroy.png`, `watchtower_projectile.png`
- `ranger_idle.png`, `ranger_attack.png`, `ranger_destroy.png`, `ranger_projectile.png`
- `tracker_idle.png`, `tracker_attack.png`, `tracker_destroy.png`
- `assassin_idle.png`, `assassin_attack.png`, `assassin_destroy.png`
- `ballista_idle.png`, `ballista_attack.png`, `ballista_destroy.png`, `ballista_projectile.png`, `ballista_impact.png`
- `scorpion_idle.png`, `scorpion_attack.png`, `scorpion_destroy.png`
- `hailstorm_idle.png`, `hailstorm_attack.png`, `hailstorm_destroy.png`, `hailstorm_projectile.png`, `hailstorm_impact.png`
- `cannon_idle.png`, `cannon_attack.png`, `cannon_destroy.png`, `cannon_projectile.png`, `cannon_impact.png`
- `mortar_idle.png`, `mortar_attack.png`, `mortar_destroy.png`, `mortar_projectile.png`, `mortar_impact.png`
- `grapeshot_idle.png`, `grapeshot_attack.png`, `grapeshot_destroy.png`, `grapeshot_projectile.png`, `grapeshot_impact.png`
- `palisade_idle.png`, `palisade_attack.png`, `palisade_destroy.png`, `palisade_projectile.png`, `palisade_impact.png`
- `obelisk_idle.png`, `obelisk_attack.png`, `obelisk_destroy.png`, `obelisk_projectile.png`, `obelisk_impact.png`
- `beacon_idle.png`, `beacon_attack.png`, `beacon_destroy.png`, `beacon_projectile.png`, `beacon_impact.png`
- `sawmill_idle.png`, `sawmill_destroy.png`
- `quarry_idle.png`, `quarry_destroy.png`
- `castle_static.png`, `castle_destroy.png`
- `spawn_cave_idle.png`, `spawn_cave_spawn.png`

### Batch 3 - Hero-Specific Buildings

- Paladin: `pal_ward`, `pal_censer`, `pal_reliquary`
- Mage: `mage_frost`, `mage_tesla`, `mage_prism`
- Hunter: `hunt_snare`, `hunt_roost`, `hunt_hive`

Each building uses `idle`, `attack` or support pulse/trigger, `destroy`, and projectile/impact files where specified.

### Batch 4 - Heroes

- `paladin`
- `mage`
- `hunter`

Actions: `spawn`, `walk`, `attack`, `death`, `summon` for each projection: `front`, `back`, `3qr`, `3ql`, `sider`, `sidel`.

Ranged hero projectiles:

- `mage_projectile_<projection>.png`
- `hunter_projectile_<projection>.png`

### Batch 5 - Early Enemies

- `fast`
- `warrior`
- `brute`
- `raider`
- `witch_doc`
- `slime`
- `air`
- `wraith`

Actions: `spawn`, `walk`, `attack`, `death`, `breach` for each projection.

Ranged projectiles:

- `witch_doc_projectile_<projection>.png`
- `air_projectile_<projection>.png`

### Batch 6 - Mid Enemies

- `scout`
- `berserker`
- `shield`
- `tunneler`
- `necro`
- `bomber`
- `spellbreak`
- `spider`

Ranged projectiles:

- `necro_projectile_<projection>.png`
- `bomber_projectile_<projection>.png`

### Batch 7 - Heavy Enemies

- `summoner`
- `machine`
- `iron_jug`
- `golem`
- `miniBossGround`

Ranged projectiles:

- `machine_projectile_<projection>.png`

### Batch 8 - Bosses

- `bossGround`
- `bossAir`
- `bossMachine`
- `dread_lord`
- `elder_dragon`

Ranged projectiles:

- `bossAir_projectile_<projection>.png`
- `bossMachine_projectile_<projection>.png`

Special:

- `elder_dragon_flyin.png`

## Shared Rules

- Use the master style prompt from the source prompt bible before every object prompt.
- Compare every generated candidate against `docs/05_assets/canon-asset-registry.md`.
- Run `docs/03_art/style-drift.md` and `docs/07_pipeline/quality-gate.md` before acceptance.
- Keep pure `#000000` only as the background key color.
- Do not use pure black or near-black on the object.
- New/regenerated gameplay objects use Layered Object Pipeline v2 by default: one object atlas PNG plus JSON manifest with separated base/body/active/ambient/attack/projectile/impact/destroy layers.
- Baked horizontal strips are allowed as runtime exports or legacy compatibility derivatives, but they should not replace the layered source of truth unless documented.
- Every baked animation export uses identical cells and a stable baseline.
- Moving units use six projections: `front`, `back`, `3qr`, `3ql`, `sider`, `sidel`.
- Buildings are single-direction top-down composed objects; their source atlas should be layered, with baked strips generated only when the runtime needs them.
- Animations must use at least 5 frames per strip unless the user explicitly requests a shorter engine-legacy variant.
- Every layered atlas must remain below 5 MB and contain only one object family.
- Every layered object must produce a compact transparent runtime atlas plus a separate human review grid.
- Runtime atlas extraction must be driven by tight JSON rects, pivots, and attachments. Do not require the engine to crop from a labeled review sheet.
- Rotating gameplay parts such as crossbows, cannon barrels, lenses, prisms, crystals, and tool arms must be separate layers with explicit pivots.
- Ambient elements such as flags, lantern flames, smoke, gears, saw wheels, runes, and crystals must animate as child layers without moving the locked base/body footprint.

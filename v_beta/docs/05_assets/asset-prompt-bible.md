# GRIMHOLD — Asset Generation Prompt Bible

> **LORE MIGRATION WARNING (2026-07-23):** Technical frame counts, runtime IDs,
> directions, cell sizes and action requirements in this file remain valid.
> Goblin Horde, Grimhold, Aeldrath, old hero/faction names, palettes and narrative
> subjects are deprecated. For all new work, identity and naming come from
> `../02_creative/object-renaming-map-v2.md`,
> `../02_creative/faction-bible-v2.md`,
> `../02_creative/visual-cultural-source-map-v2.md`, and
> `object-family-and-variation-spec-v4.md`. No prompt may paste a deprecated
> faction block from this file.
Prompt library for generating every game sprite for **GRIMHOLD / Ether Frontier** with an
image model (Midjourney / SDXL / DALL·E / Flux, etc.).

Read order:
1. `../03_art/master-visual-style.md` — active visual language.
2. `../03_art/art-bible.md` — global visual identity.
3. `technical-asset-contract.md` — file naming, atlas, size, and pipeline requirements.
4. **MASTER STYLE PROMPT** — paste before every per-object prompt.
5. **TECHNICAL CONTRACT** — exact file naming, frame counts, sizes the current prototype expects.
6. **PER-OBJECT PROMPTS** — one block per enemy / hero / tower / building.

> Documentation source of truth: `../README.md`. Creative direction: `../02_creative/creative-direction.md`.

> Canonical projection note: this project's camera is **NEAR TOP-DOWN WITH SLIGHT TILT**.
> Top planes dominate 85-90%; side faces are only 10-15% subtle thickness cues. Do not use full
> isometric, 3/4 side-view, perspective, side-scroller, forced-depth, tall-facade, full-doorway,
> staircase, or dominant vertical-wall camera language in new prompts for ordinary gameplay assets.

> Prompt output is never accepted by prompt compliance alone. Every candidate must pass
> `../03_art/style-drift.md`, `technical-asset-contract.md`, and `../07_pipeline/quality-gate.md`.

> Layered object note: new/regenerated gameplay objects should use **Layered Object Pipeline v2**.
> Prefer one object-specific compact runtime atlas plus JSON manifest with separated base/body/active/ambient/attack/projectile/impact/destroy layers. Also produce a separate human review grid. Baked horizontal strips are legacy/runtime export derivatives unless a task explicitly asks for the old strip format.

---

## 1. MASTER STYLE PROMPT

Paste this verbatim at the top of every asset prompt, then append the per-object block.

```
MASTER VISUAL STYLE:
This project does NOT imitate any existing game, studio, or franchise. It follows its own
artistic language. Every asset must belong to the same visual universe because it follows the
same rules of shape, material, color, light, and gameplay readability.

CORE PHILOSOPHY:
The world feels like an illustrated fantasy book brought to life: hand-crafted, iconic, clean,
readable, and designed for gameplay first. It is adapted from the discipline of traditional
hand-painted animation backgrounds and character design from late 1980s-1990s animated feature
films into a clean near top-down with slight tilt game art language. It is NOT realistic, NOT anime, NOT pixel art,
NOT a studio imitation, NOT a clone of any existing game, NOT AI glossy, and NOT concept art
rendering.

CAMERA / PROJECTION (CRITICAL):
NEAR TOP-DOWN WITH SLIGHT TILT. The camera is almost directly above the world with only a small
angled tilt to reveal volume. Top planes dominate: 85-90% roof/top/crown/upper-surface read.
Side faces are only 10-15% subtle thickness cues. NOT full isometric. NOT 3/4 side-view.
NOT perspective. NOT side-scroller. For ordinary gameplay assets: NO tall front facade, NO full
doorway, NO staircase, NO vertical wall dominating the asset. Every asset must work when moved
anywhere on the map: no baked environment, no baked terrain, no forced perspective.

SHAPE LANGUAGE:
Use large readable shapes and very few small details. Every object must be recognizable by pure
black silhouette. No visual noise and no unnecessary decoration.

MATERIAL LANGUAGE:
Materials matter more than texture. Stone feels heavy. Wood feels warm. Metal feels dense.
Leather feels soft. Fabric feels light. Gold feels precious. The material must be understood
before seeing any texture.

COLOR:
Use emotional colors, never photorealistic colors. Shadow colors are cool. Light colors are warm.
Stone is blue-gray. Wood is warm brown. Grass is blue-green instead of saturated green. Magic uses
accent colors. Every biome has a restrained palette.

LIGHT:
One main light source: top-left. Soft illustrated lighting only. No cinematic lighting, no dramatic
rim lights, no realistic GI, no glossy reflections. Volume is created through color transitions and
simplified forms.

LINEWORK:
Use soft illustrated outlines. Never thick comic outlines. Never black outlines. Use darker local
colors for edges. The image should feel hand-crafted, not vector-clean or AI-polished.

DETAIL:
Detail exists only where it improves readability. Never add detail because there is empty space.
Large forms dominate; small details support them.

PROPORTIONS:
Stylized heroic proportions. Buildings slightly oversized. Weapons slightly oversized. Trees have
large crowns. Roofs are visually important. Characters are readable at small size.

GAMEPLAY FIRST:
The player must instantly distinguish walkable, blocked, interactive, resource, enemy, friendly,
and objective. Everything must remain readable even when the screen is full.

NEVER DO:
NO realism. NO AI glossy look. NO concept art rendering. NO photobashing. NO painterly brush noise.
NO random texture overlays. NO procedural-looking assets. NO full isometric camera. NO 3/4 or perspective camera. NO cinematic
perspective. NO exaggerated depth. NO visual clutter. NO studio or game clone style.

FINAL TEST:
Every asset must pass these questions: Can it be recognized in pure black silhouette? Can it be
recognized at 64x64? Can it be moved anywhere on the map? Does it feel hand-crafted? Does it belong
to the same universe as every other asset? If any answer is NO, redesign the asset.

PROPORTION LOCK (CRITICAL):
For Layered Object Pipeline v2, the composed base/body footprint, gameplay scale, and main
pivot/anchor MUST stay stable across all actions. Child layers may animate, rotate, appear, or
disappear only through declared pivots, attachments, and runtime transforms.

For legacy strip exports and moving-unit strips, every strip for the same object MUST use the
IDENTICAL canvas size, cell size, object scale, and baseline anchor across ALL actions and ALL
projections. The object occupies the same pixel footprint and sits at the same vertical baseline
in every frame. DO NOT resize, rescale, reframe, or recompose the object between action strips.
This is essential: if proportions vary between strips, the engine cannot swap them cleanly and
the animation will jitter/jump.

BUILDING IDLE ANIMATION RULE (CRITICAL):
The solid STRUCTURE (stone walls, wood frame, metal casing) is COMPLETELY STATIC in every
idle frame — it does NOT breathe, pulse, scale, bob, or shift position. ONLY named physical
sub-elements may animate, and only in ways that are physically plausible:
  ALLOWED: flame/ember flicker (brazier, torch, censer), smoke/steam drift, spinning
           wheel/gear/drum/optics-ring, swaying banner/flag/chain/vine, rotating
           lens/crystal/prism, liquid bubbling in a vat, pulley/belt moving, pendulum/arm
           swinging, small arc/spark crackling between fixed conductors, rune/gem blinking.
  FORBIDDEN: the whole building scaling up-down ("breathing"), any solid masonry/wood/metal
             element shifting, a glow-pulse that covers the whole structure, "hovering" of
             a non-floating object. If a building has NO moving parts, idle = 1 static frame.
This rule applies equally to enemies, heroes, and decor: only physically motivated elements
on the object animate; the rigid body/silhouette is locked.

LAYERED OBJECT PIPELINE V2 (CRITICAL):
For all new or regenerated gameplay objects, prefer a modular layered atlas over a fully baked
whole-object animation strip. The object is assembled like a stacked cardboard board-game token:
base/body stays locked, while child layers provide life and gameplay direction.
- Separate the object into named layers where applicable:
  base_token, body_static, active_part, ambient_fx, attack_fx, projectile, impact, destroy_fx.
- Rotating gameplay parts must be separate layers with declared pivots:
  crossbow, cannon barrel, ballista arm, prism, lens, crystal, tool arm, shield, weapon.
- Ambient motion must be separate child animation:
  flag cloth wind frames, lantern/brazier flame, smoke, gears, saw wheel, pulley, rune blink,
  crystal shimmer, liquid bubble, sparks.
- Attack motion must use separate FX layers:
  charge, muzzle flash, recoil mark, projectile spawn, impact.
- The base/body footprint must remain stable across idle/attack/destroy. Effects may extend only
  within safe atlas margins.
- One object family per atlas. Put owner-specific projectile/impact/debris in the same object atlas.
- The final atlas must stay under 5 MB and must be accompanied by JSON declaring rectangles, pivots,
  attachments, draw order, animation clips, frame timing, loop/hold behavior, and runtime transforms.
- Deliver two views: a compact transparent runtime atlas for code, and a separate fixed-cell review
  grid for humans. The engine must read tight `rect` values from JSON, not crop from the review grid.
- Exclude assembled previews and labels from the runtime atlas. Previews and labels belong only in
  review artifacts.
- For cardboard tabletop objects, prefer TRUE TOP-DOWN ORTHOGRAPHIC 90° when readable: no facade,
  no rear view, no tall perspective tower, no cinematic angle.

PALETTE: desaturated stone greys as the structural base. Horde bodies read as green to
grey-green skin with scrap metal, bone, leather, and ochre/red war paint. Horde magic reads as
TOXIC GREEN ether (#6abf3f → #b6f06a), with restrained sickly purple only as a secondary hex
accent. Player towers/heroes read as warm AMBER/ORANGE torch glow (#b8761f → #ffb23f → #ffe06b).
Fortress stone is cold grey (#5a6472 → #aab2bd) with thin GOLD seal-crack lines (#ffe06b).
Use saturated accent colors ONLY for energy/eyes/runes, never for the whole body.

CUT-OUT RULE (CRITICAL):
- Background MUST be PURE solid black (#000000), flat, fully opaque, edge to edge.
- The OBJECT ITSELF must contain NO pure-black and NO near-black pixels anywhere — not in
  outlines, shadows, armor, void energy, gaps, or holes. The darkest pixel allowed ON the
  object is a deep desaturated purple-grey (#1c1726) or deep blue-grey (#181d28), never #000.
- This lets the asset be chroma-keyed / cut from the black background cleanly. Treat black as
  the "alpha" color. Outlines around the object = dark purple-grey, NOT black.
- No drop shadow cast onto the background. No ground disc, no vignette, no glow bleeding into
  the black field (keep glow tight inside the silhouette / within 2px of it).
- NO pedestal, foundation, circular base, soil patch, terrain tile, or object stand beneath
  any object. The object ends where its lowest pixel is — no decorative ground.

SHEET FORMAT:
Preferred for new/regenerated objects: output ONE object-specific layered sprite atlas with named
separated parts, plus JSON manifest. Source generations may be arranged in a clean grid, but the
production deliverable must be normalized into:
1. a compact transparent runtime atlas using tight JSON rectangles;
2. a separate human review grid with fixed cells, labels, and pivot marks.
Components must be isolated, fully visible, consistently scaled, and separated enough for clean
extraction/composition. Include no unrelated objects.

Legacy/export format when required by runtime compatibility: output ONE horizontal sprite strip =
a single row of N animation frames, left to right, evenly spaced, identical frame cell size,
transparent-intent black between/around frames. Each frame perfectly centered in its cell,
consistent ANCHOR baseline (the object's own lowest contact pixel — NOT a drawn ground line)
across all frames so the sprite does not jitter when played. No sub-pixel drift.

ANIMATION: minimum 5 frames per action (more is better — aim 5–7) so the loop is smooth.
Frame 1 = clean readable pose. Show clear in-between poses, not just two extremes. Loop or
hold-last as noted per action.

SILHOUETTE: instantly readable shape at small size. Distinct per unit. No tiny fiddly detail
that vanishes when downscaled.
```

---

## 2. TECHNICAL CONTRACT (engine-facing)

### 2.1 The 6 movement/facing directions

These are facing directions inside the near top-down with slight tilt camera. They are not alternate cameras.

| Suffix  | Facing | Description |
|---------|--------|-------------|
| `front` | down-screen / south | top-down unit facing the player side of the map |
| `back`  | up-screen / north | top-down unit facing the spawn side of the map |
| `3qr`   | down-right / southeast | top-down diagonal facing |
| `3ql`   | down-left / southwest | top-down diagonal facing |
| `sider` | right / east | top-down side-facing silhouette |
| `sidel` | left / west | top-down side-facing silhouette |

`sider`/`sidel` and `3qr`/`3ql` are mirror pairs in orientation but must be **separately drawn**
when gear, lighting, or silhouette is asymmetric. Same character, same scale, same baseline across all 6.

### 2.2 Actions

**Moving units (enemies, heroes, bosses)** — 5 actions × 6 projections:
- `spawn` — appear / emerge (plays once, then → walk)
- `walk` — locomotion loop (seamless cycle)
- `attack` — strike / cast (plays once per hit)
- `death` — die / dissolve (plays once, holds last frame)
- `breach` — attacking the player's wall/base (plays once/loops)

**Ranged units** additionally get `projectile` × 6 projections.

**Buildings / towers** — single-direction layered objects:
- `idle` — composed from locked base/body plus ambient child loops.
- `attack` — active part rotation/recoil plus attack FX once.
- `destroy` — debris/ruin overlays or generated collapse pieces, hold last where applicable.
- Attacking towers also get owner-scoped `projectile` and `impact` layers when unique.

Economy buildings (sawmill, quarry) and decor: `idle` + `destroy` only (+ `grow` for resources).

### 2.3 File naming

```
ENEMIES:    <unit>_<action>_<projection>.png      e.g.  warrior_walk_3qr.png
ENEMY PROJ: <unit>_projectile_<projection>.png    e.g.  air_projectile_sider.png
TOWERS:     <tower>_idle.png  <tower>_attack.png  <tower>_destroy.png
TOWER PROJ: <tower>_projectile.png   <tower>_impact.png
RESOURCES:  res_gold.png  res_wood.png  res_stone.png
DECOR:      tree_oak.png  tree_oak_grow.png  rock_a.png  rock_grow.png ...
```

Runtime folders: directional enemies → `assets/runtime/sprites/enemies/`; buildings → `assets/runtime/sprites/buildings/`; decor and terrain → `assets/runtime/sprites/environment/`. Candidates must remain under `assets/staging/candidates/` until approved.

### 2.4 Frame-cell sizes (per-frame square, sprite centered inside)

| Tier | Units | Cell |
|------|-------|------|
| Small | raider, witch_doc, air, necro | 72–80 px |
| Std | warrior, fast, slime, wraith, berserker, bomber, spellbreak, tunneler, scout | 88–96 px |
| Large | shield, spider, machine | 96–104 px |
| Heavy | brute, summoner, iron_jug, miniBoss | 120–144 px |
| Boss | golem, bossGround, bossAir, bossMachine, dread_lord | 144 px |
| Colossal | elder_dragon | 192 px |
| Buildings | all towers | layered runtime atlas, compact rects; composed gameplay footprint defined per object |
| Projectiles (enemy) | — | ~20–40 px |
| Projectiles (tower) | cannon 18 · obelisk 22 · beacon 18 · watchtower 20 · ranger 36 · mortar 20 px |

Per-action frame counts: target **5–7** for enemies (engine tolerates 4–8). Buildings use layered child loops/one-shot FX by default: ambient loops usually 4–6 frames, attack FX usually 4 frames, destroy debris/ruin pieces as needed.

---

## 3. PER-OBJECT PROMPTS

Each entry = paste MASTER STYLE PROMPT first, then the object block.
**Reminder per-prompt rule:** new/regenerated objects use layered runtime atlas + JSON manifest
by default. Legacy strips, when explicitly required, share the same canvas/cell size, camera,
scale, and baseline. No ground/pedestal/base beneath the object unless it is the object itself.

---

### 3.A ENEMIES

> **ENEMY FACTION THEME — THE GOBLIN HORDE (paste into every enemy prompt).**
> ALL enemies are GOBLINS / goblinoids of one invading horde — a scavenger warband, not undead
> and not abstract void-spawn. Keep one unified race look across the whole roster:
> - SKIN: warty green to grey-green (#3a5a2e → #7faa4d highlights), big pointed ears, hooked
>   noses, sharp underbite tusks/teeth, sinew + bone. Bigger bruisers = hobgoblin/ogre size,
>   greyer + more muscle. Skin shadow darkest = **#1c2a16 (deep green-grey, NEVER black)**.
> - GEAR: scavenged & mismatched — rusted scrap-iron plates, bone, leather straps, riveted junk,
>   tribal war-paint (ochre/red), torn clan banners. Improvised, asymmetric, "made from trash".
> - MAGIC / GLOW: the horde's shamans use TOXIC-GREEN ether (#6abf3f → #b6f06a), with a little
>   sickly VOID-PURPLE only as their dark hex accent — glow lives in eyes, runes, potions, orbs,
>   NEVER as the body color. Eyes glow sickly green or amber.
> - BEASTS & MACHINES of the horde (wargs, cave-bats, spiders, scrap-mechs, the captive wyrm) are
>   goblin-bred or goblin-built/piloted — tie each back to the horde (harness, war-paint, crew).
> - NO PURE BLACK / NO NEAR-BLACK anywhere on any enemy (cut-out rule): outlines = deep green-grey
>   or deep purple-grey, never #000. Background only is pure black.
> Loose clans (flavor): Wolf-pack (runners), Warband (melee), Sapper clan (diggers/bombers),
> Shaman cult (casters), Tinkerer clan (machines), Beast-riders (spiders/bats), Warlord court (bosses).

---

#### `fast` — Runners (Wolf-pack)

```
SUBJECT: a lean mangy WAR-WOLF (warg) of the goblin horde — the tribe's bred wolf-beast,
sprinting low. Grey-green matted fur, a scrap-iron spiked collar + tribal war-paint, sharp
fangs, sickly-green glowing eyes (darkest fur = #1c2a16, no pure black). Small fast agile
silhouette. 128px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all 5 action strips (spawn/walk/attack/death/breach) use identical 128px
cell, same scale, same baseline. Do not resize the hound between strips.

spawn  (5–6f): scrambles up over the lip of a dug trench/burrow, shakes off, drops onto all
               fours ready to run.
walk   (6f):   fast gallop cycle, legs blur-stepped, body bobbing, ears back.
attack (6f):   lunges forward, snapping jaws, head thrust then recoil.
death  (6f):   yelps, tumbles, crumples into a limp heap + a puff of dust, hold last frame.
breach (6f):   claws and bites repeatedly at an offscreen wall (lower-right), frantic.
PROJECTIONS: front=facing camera mid-run, back=tail toward us, 3qr/3ql=diagonal sprint,
             sider/sidel=full profile gallop.
```

#### `warrior` — Warriors (Wave 1, iso-redone)

```
SUBJECT: a GOBLIN foot-soldier of the horde — green-grey warty skin, pointed ears, snarling
tusked face, mismatched scavenged scrap-iron half-plate, tribal war-paint, a crude chipped
cleaver-sword + a battered scrap shield. Sickly-green eye-glow. 128px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all 5 action strips use identical 128px cell, same scale, same baseline.

spawn  (6f): scrambles up out of a dug trench, straightens, raises cleaver to ready stance.
walk   (6f): heavy march, shield forward, armor sway.
attack (6f): wind-up over shoulder → diagonal downward cleaver chop → recover.
death  (6f): snarls, staggers, armor buckles, collapses into a heap, hold last.
breach (6f): hammers shield + sword against the wall, shoulder-checks it.
PROJECTIONS: shield on unit's left arm consistent; sider shows sword arm to camera,
             sidel shows shield side to camera.
```

#### `brute` — Brutes (Rotting Tide, heavy)

```
SUBJECT: a hulking OGRE-BRUTE of the goblin horde — massive swollen muscle, hunched, green-grey
warty hide, jutting tusks, crude bone-and-scrap pauldrons, oversized fists, a spiked club or
bare knuckles. Massive top-heavy silhouette. 144px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 144px cell, same scale, same baseline.

spawn  (4f): heaves up, roars, pounds fists once.
walk   (6f): slow lumbering stomp, knuckle-drag, heavy side-to-side weight shift.
attack (4f): rears back → giant overhead double-fist slam.
death  (4f): topples backward like felled tree, kicking up a cloud of dust, hold last.
breach (4f): bashes wall with full body-slam shoulder charges.
PROJECTIONS: emphasize bulk; back view shows bone-spur pauldrons + hide prominently.
```

#### `raider` — Raiders (Iron Vanguard)

```
SUBJECT: a wiry GOBLIN brigand in scavenged leathers + a torn red clan sash, twin curved
daggers, green-grey skin, hooked nose, big ears, sickly-green eye-glow. Small 80px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 80px cell, same scale, same baseline.

spawn  (4f): darts out of cover into a low ready crouch.
walk   (6f): light bouncy jog, daggers reverse-gripped, head scanning.
attack (6–7f): rapid double-slash X cross, then a back-step.
death  (6f): clutches chest, spins, crumples + a puff of dust, hold last.
breach (4f): pries/jabs daggers into a resource crate/wall.
PROJECTIONS: keep red sash readable from every angle.
```

#### `witch_doc` — Witch Doctors (Forsaken Court, RANGED)

```
SUBJECT: a hunched GOBLIN witch-doctor/shaman in feather-and-bone fetish robes, an antlered
bone mask, green-grey skin, a skull-topped staff dripping toxic-green hex. 72px cell. Caster.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 72px cell, same scale, same baseline.

spawn  (5f): rises from bubbling hex puddle, mask tilts up.
walk   (6f): shuffling limp, staff as cane, robe sway.
attack (6f): raises staff, swirls hex orb, thrusts it forward (→projectile).
death  (6f): mask cracks, body crumples + a wisp of green hex-smoke escapes, hold last.
breach (5f): jabs staff and flings hex at the wall.
PROJECTILE (witch_doc_projectile_*, ~24px, 5f): a spinning sickly toxic-green hex skull/orb
            with a short comet trail, drawn per projection.
```

#### `slime` — Slimes (Void Spawn)

```
SUBJECT: a runaway GOBLIN ALCHEMICAL OOZE — a wobbling blob of toxic acid-green translucent
sludge (darker green core #1f2a16, NOT black) brewed by the horde's tinkerers, with goblin junk
half-dissolved inside (a cracked goblin helmet, a gnawed bone). 88px cell. No legs — it oozes.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 88px cell, same scale, same baseline.

spawn  (6f): drips down from above / wells up, wobbles into a domed blob.
walk   (5f): squash-and-stretch ooze crawl, surface ripples, core sloshes.
attack (5–6f): rears front up and flops/engulfs forward, splatter.
death  (6f): pops and spreads into a flat splat that fizzes away in green steam, hold last.
breach (5f): slams its mass against the wall, splashing.
PROJECTIONS: vary the suspended junk's angle + highlight per view so direction reads.
```

#### `air` — Flyers (air category, RANGED)

```
SUBJECT: a GOBLIN BAT-RIDER — a small whooping goblin clinging to a horde-bred leathery
cave-bat, grey-green bat wings + green-grey goblin skin, a scrap-iron riding harness, the
goblin clutching a spit-blowpipe. Perpetually airborne (float slightly high), green eye-glow.
80px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 80px cell, same scale, same baseline.

spawn  (5f): swoops down into frame, wings snap open into a hover.
walk   (5f): FLY loop, steady wing-flap, slight vertical bob.
attack (5–6f): swoops/dives forward, the goblin spits a green dart-bolt (→projectile), pulls up.
death  (7f): wing tears, bat + rider tumble spiraling downward, hold last.
breach (5f): claws and dives at wall top repeatedly.
PROJECTILE (air_projectile_*, ~20px, 5f): a small toxic-green spit-dart / energy bolt, teardrop
           with trail, per projection.
```

#### `wraith` — Wraiths (Forsaken Court, air/ghost)

```
SUBJECT: a GOBLIN HEX-WISP — a tattered spirit conjured by the horde's shamans: a ghostly
goblin-skull wrapped in ragged green spirit-smoke, no legs (trailing smoke tail), two cold
sickly-green pinpoint eyes, skeletal goblin hands. Pale grey-green, semi-transparent. 88px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
      smoke tail trails behind/below.
PROPORTION LOCK: all action strips use identical 88px cell, same scale, same baseline.

spawn  (5f): condenses from wisp of smoke into the hooded form.
walk   (6f): hovering drift, robe and smoke-tail undulating.
attack (4–5f): lunges forward with a clawing spectral hand swipe.
death  (6f): unravels into shredded smoke ribbons, hold last as faint wisp.
breach (4f): phases partway into the wall, clawing through.
PROJECTIONS: feathered dithered edges. Tail trails opposite to facing.
```

#### `scout` — Scouts (recon skirmisher)

```
SUBJECT: a lean GOBLIN scout in a light hood + leather wraps, a short recurve bow or a blowpipe,
green-grey skin, big ears, a grey-green clan cloak, sickly-green eye-glow. 88px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 88px cell, same scale, same baseline.

spawn  (5f): drops from shadow-rift into low ready crouch.
walk   (5f): light fast skirmishing jog, cloak fluttering.
attack (6f): quick darting strike — bow-snap or javelin-jab — then nimble step back.
death  (6f): spins, crumples + a puff of dust + a fluttering torn cloak, hold last.
breach (5f): jabs/looses rapidly at wall while bobbing.
PROJECTIONS: keep cloak + hood as the read; sider/sidel show longest skirmish stride.
```

#### `berserker` — Berserkers (Iron Vanguard, fast melee)

```
SUBJECT: a frenzied bare-chested GOBLIN/hobgoblin berserker, green-grey muscle, dual rusted
hand-axes, bone-spiked pauldrons, war-paint, frothing, hunched aggressive lean. 88px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 88px cell, same scale, same baseline.

spawn  (5–6f): smashes up through ground, throws head back in silent roar, axes up.
walk   (5f): aggressive fast stomping charge, axes swinging at sides.
attack (5–6f): whirlwind — both axes cross-chop in a spinning flurry.
death  (6f): over-swings, loses balance, topples in a burst of sparks + dust, hold last.
breach (5f): berserk hacking both axes into the wall, no rhythm, frantic.
```

#### `shield` — Shield Bearers (Iron Vanguard, tank)

```
SUBJECT: a heavily armored GOBLIN/hobgoblin juggernaut behind a massive scrap tower shield
(tribal-rune painted), a short stabbing spear, green-grey skin, thick riveted scrap plate. 96px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
      FRONT projection = mostly the giant shield face toward camera; BACK = armored back + rim.
PROPORTION LOCK: all action strips use identical 96px cell, same scale, same baseline.

spawn  (5f): plants tower shield down, braces behind it.
walk   (6f): slow shielded advance, shield leading, short steps.
attack (5f): jabs spear out past shield edge, retracts.
death  (6–7f): shield drops/shatters, body folds, tribal runes flare and die, hold last.
breach (5f): rams tower shield bodily into the wall.
PROJECTIONS: sider/sidel = shield in profile, spear arm visible.
```

#### `tunneler` — Tunnelers (burrower)

```
SUBJECT: a GOBLIN SAPPER/digger with huge clawed digging gauntlets, a drill-pick snout-helm,
dirt-caked scrap plate, green-grey skin, sickly-green glowing eyes. 92px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 92px cell, same scale, same baseline.

spawn  (5f): bursts up out of a dirt mound in a spray of soil + dust (debris is motion FX only).
walk   (6f): low scuttling waddle, claws swinging, dirt trailing.
attack (6f): swipes both drill-claws in an X, then a snout headbutt.
death  (6f): collapses, half-sinks into a crumbling hole, hold last.
breach (5f): drills/claws into wall base, boring motion, debris flying.
```

#### `necro` — Necromancers (Forsaken Court, RANGED)

```
SUBJECT: a gaunt GOBLIN bone-shaman in a hooded ragged death-robe, green-grey skin, a floating
sickly-green soul-orb, little scrap-bone fetishes + a raised bone-goblin hinted at his feet.
80px cell. Caster posture.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 80px cell, same scale, same baseline.

spawn  (5f): rises amid ring of green grave-fog, orb ignites.
walk   (6f): slow gliding stride, robe trailing, orb orbiting one hand.
attack (5–6f): raises both arms, channels and hurls a necrotic energy bolt (→projectile).
death  (6f): orb shatters, robe collapses empty, soul escapes upward, hold last.
breach (5f): channels destructive necrosis into the wall, hands outstretched.
PROJECTILE (necro_projectile_*, ~24px, 5–6f): a clustered sickly-green skull-bolt / soul-wisp
           with trailing embers, per projection.
```

#### `bomber` — Balloon Bombers (air, RANGED)

```
SUBJECT: a cackling GOBLIN BOMBARDIER riding a patched balloon of stitched hide (sickly-green
gas membrane), green-grey skin, clutching a lit scrap-iron bomb with a green-sparking fuse.
88px cell. Airborne.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 88px cell, same scale, same baseline.

spawn  (5f): balloon inflates from nothing, gremlin pops up grinning.
walk   (6f): bobbing drift, balloon wobble, legs dangling, bomb swinging.
attack (6–7f): winds up and lobs bomb downward (→projectile), balloon recoils up.
death  (7f): balloon pops, goblin plummets, mid-air bomb-burst of orange-green flame, hold last.
breach (5f): drifts to wall and drops bombs onto it.
PROJECTILE (bomber_projectile_*, ~28px, 5f): a round dark grey-iron scrap bomb (NOT black,
           darkest #20242e) with a green-sparking fuse + arc trail, per projection.
```

#### `spellbreak` — Spellbreakers (Forsaken Court, anti-magic melee)

```
SUBJECT: a hulking armored GOBLIN/hobgoblin rune-breaker wrapped in rune-suppressing chains,
green-grey skin, hefting a crude glaive that nullifies magic (desaturated anti-glow zone around
it). Scrap steel + glowing tribal runes (darkest #1c2a16, no pure black). 88px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 88px cell, same scale, same baseline.

spawn  (5f): chains snap taut as it forms, glaive spun into guard.
walk   (5f): measured advance, glaive across body, chains swaying.
attack (6f): wide sweeping glaive arc, desaturating shimmer trailing the blade.
death  (6f): chains burst, runes go dark, body crumbles, hold last.
breach (5f): chops glaive into the wall, prying chains around it.
```

#### `spider` — Spider Riders (Void Spawn)

```
SUBJECT: a giant cave-SPIDER mount with a tiny GOBLIN rider + spear/lance on its back. Dark
mottled green-grey abdomen with a painted tribal-rune brand, 8 spindly legs, dripping mandibles.
104px cell. Wide low silhouette.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 104px cell, same scale, same baseline.

spawn  (5f): drops down on a glowing thread, legs splay to stance.
walk   (5f): scuttling 8-leg cycle, abdomen bobbing, rider jostling.
attack (5f): rears front legs + rider stabs lance forward, mandible snap.
death  (6f): legs curl inward, abdomen bursts green ichor, rider topples, hold last.
breach (5f): legs grip wall, mandibles + lance jab at it.
PROJECTIONS: legs must read distinctly per angle; back shows the abdomen rune-brand.
```

#### `summoner` — Summoners (Forsaken Court, heavy caster)

```
SUBJECT: a tall regal GOBLIN WARLOCK / shaman-king in ornate crowned fetish-robes, green-grey
skin, twin floating ritual braziers, an open bone spell-tome, green warp-portals at the hem that
spit goblin reinforcements. 120px cell. Imposing, slow.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 120px cell, same scale, same baseline.

spawn  (6f): a summoning circle blooms, the priest descends into it, braziers ignite.
walk   (5f): slow imperious glide, robes and braziers trailing, tome floating ahead.
attack (7f): spreads arms wide, opens a small green warp-portal that disgorges goblin motes.
death  (6f): crown cracks, braziers fall, robe collapses as portals implode, hold last.
breach (5f): opens a green rift against the wall, channeling it apart.
```

#### `machine` — Machines (machine category, RANGED)

```
SUBJECT: a clattering GOBLIN WAR-CONTRAPTION — a piloted scrap-mech of riveted bronze-and-iron
junk with a goblin tinkerer visible at the controls, an exposed glowing green furnace-core in the
chest, piston legs, an arm-mounted scrap-cannon. Warm rust + sickly-green core. 104px cell.
Darkest steel = #20242e (NOT pure black).
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 104px cell, same scale, same baseline.

spawn  (6f): assembles/clanks online, core ignites, steam vents, arm-cannon racks.
walk   (6f): heavy piston march, gear rotation, exhaust puffs, core glow pulse.
attack (4–6f): arm-cannon recoils firing an ether shell (→projectile), steam burst.
death  (6f): core overloads, plates blow off, sparks + green flame, slumps, hold last.
breach (5f): drives a piston-fist / drill into the wall.
PROJECTILE (machine_projectile_*, ~28px, 5f): a glowing scrap artillery shell, bronze casing +
           green energy trail, per projection.
```

#### `iron_jug` — Iron Juggernauts (machine, super-tank)

```
SUBJECT: a colossal GOBLIN-built siege-juggernaut, riveted scrap slab armor, a battering-ram
prow, two glowing green furnace eyes, goblin crew clinging to it. 120px cell. Moving wall.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 120px cell, same scale, same baseline.

spawn  (6f): unfolds from compacted transport-block to full height, furnaces light.
walk   (6f): ponderous two-step stomp, smoke stacks puffing.
attack (5–6f): rams prow forward like a piston, recoil shudder.
death  (6f): seizes, furnaces blow out, armor sloughs, collapses into smoking heap, hold last.
breach (3–4f): drives battering-ram prow straight through the wall.
```

#### `golem` — Stack Golems (Void Spawn, boss-tier)

```
SUBJECT: a towering GOBLIN SCRAP-GOLEM — a lurching construct of bolted-together junk, scrap-metal
slabs and cage-cores lashed around a captured glowing green ether-crystal heart by the horde's
tinkerers, glowing seams, fused-scrap fists. 144px cell. Hulking, ramshackle.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
      simultaneously; the levitating gaps between slabs read clearly.
PROPORTION LOCK: all action strips use identical 144px cell, same scale, same baseline.

spawn  (5f): slabs fly together from scattered rubble and lock into the standing tower.
walk   (6f): slabs counter-rotate as it strides, levitating gaps pulsing.
attack (5–6f): one arm-slab swings a massive crushing hook.
death  (7f): green seams snap, scrap scatters and falls, hold last on settling rubble.
breach (3–4f): slams a scrap-fist clean through the wall.
PROJECTIONS: emphasize the bolted-junk mass + green core glow; rigid, lurching per angle.
```

---

### 3.B BOSSES & MINI-BOSSES

#### `miniBossGround` — Warlord Vanguard

```
SUBJECT: an elite GOBLIN WARLORD-CAPTAIN (hobgoblin-sized) in spiked scrap-and-bone warlord
plate, green-grey skin, a great two-handed cleaver, a tattered horde banner-cape, a single
horned/tusked helm. Commanding. 120px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 120px cell, same scale, same baseline.

spawn  (5–6f): plants cleaver, banner unfurls, raises a fist.
walk   (5f): confident heavy march, cleaver shouldered, cape billowing.
attack (5–7f): big two-handed cleaver swing, ground-shaking follow-through.
death  (6f): drops to one knee, banner falls, armor cracks with green war-fire, hold last.
breach (4–5f): two-hand overhead cleaver chops into the wall.
```

#### `bossGround` — Boss: Warlord

```
SUBJECT: the GREAT GOBLIN WARLORD (horde war-king) — a massive armored hobgoblin, green-grey
hide, oversized cleaver + scrap shield, a crown of horns and tusks, a cape of chains and skulls,
a glowing green tribal war-totem on the chest. 144px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 144px cell, same scale, same baseline.

spawn  (6f): erupts in a pillar of green war-fire, lands in a crouch, rises with a roar.
walk   (6f): earth-shaking stride, cape and chains swaying.
attack (5–6f): overhead cleaver smash → optional shield-bash combo.
death  (4–6f): dramatic stagger, totem cracks blazing green, body detonates in a burst,
              hold last on smoking crater pose.
breach (1–2f): single devastating wall-shattering blow.
```

#### `bossAir` — Boss: Sky Terror (RANGED)

```
SUBJECT: an enormous WYVERN / great cave-bat unleashed by the horde — vast tattered wings, a
barbed tail, a beaked maw, a goblin war-harness + a strapped-on goblin beast-master, a sickly-
green storm crackling around it. 144px cell. Always airborne.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 144px cell, same scale, same baseline.

spawn  (4–5f): descends from above out of a green storm, wings flare into hover.
walk   (4–5f): powerful slow wing-beat hover loop, tail sway.
attack (2–3f): rears, throat glows, exhales a green blast (→projectile). (Few frames, punchy.)
death  (5–7f): wing shreds, spirals down trailing storm, crashes, hold last.
breach: dives and rakes wall/base with talons.
PROJECTILE (bossAir_projectile_*, ~40px, 5f): a crackling green storm-orb / lightning lance with
           branching arcs, per projection.
```

#### `bossMachine` — Boss: Siege Engine (RANGED)

```
SUBJECT: a gigantic GOBLIN GRAND SIEGE-ENGINE — a junk-fortress on legs, multiple scrap-cannon
barrels, a furnace heart, smokestacks, scrap-tech plating, a swarming goblin crew. 144px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 144px cell, same scale, same baseline.

spawn  (4–5f): unfolds/deploys from travel mode, barrels rack, furnaces ignite.
walk   (1–4f): slow grinding crawl, treads/legs churning, smoke.
attack (3–4f): main cannon recoils firing a huge shell (→projectile), muzzle flash.
death  (5–7f): cascading internal explosions, barrels blow off, collapses, hold last.
breach (5f): rams chassis / fires point-blank into base.
PROJECTILE (bossMachine_projectile_*, ~40px, 5f): a heavy mortar shell, glowing green core,
           thick smoke trail, per projection.
```

#### `dread_lord` — Dread Warlord (penultimate boss)

```
SUBJECT: the DREAD GOBLIN WARLORD — a towering hobgoblin death-king draped in a flowing bone-
and-rag cloak, green-grey gaunt skin, a floating crown of skull-shards, a soul-reaping
greatscythe, orbiting goblin death-spirits (hex-wisps). 144px cell. Elegant + terrifying.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips use identical 144px cell, same scale, same baseline.

spawn  (6–7f): materializes from vortex of screaming spirits, crown assembles, scythe forms.
walk   (6–7f): hovering regal glide, cloak and spirits trailing, scythe at rest.
attack (4–6f): sweeping scythe reap, a crescent of green soul-energy following the arc.
death  (7–8f): crown shatters shard by shard, spirits scatter, body unravels, hold last.
breach (4–6f): scythe-reaps the wall, spirits swarming through.
```

#### `elder_dragon` — Elder Dragon (final boss, 192px)

```
SUBJECT: the horde's captive ELDER WYRM — a vast ancient dragon the goblins have chained and
unleashed as their doomsday beast. Dark green-charcoal scales (#1d2416 darkest, NEVER black),
molten amber-green cracks between scales, enormous wings, a horned skull, a glowing green core
throat, goblin war-chains + lashed siege-howdahs/crew across its back. 192px cell. Largest asset.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
      the angled near top-down with slight tilt view. Wings spread show top surface + front edge.
PROPORTION LOCK: ALL action strips + all 6 projections use identical 192px cell.

flyin  (3f, single dir): soars in from the horizon, growing larger, wings spread.
spawn  (4f per dir): lands/coils, wings furl, head rears with a roar.
walk   (4–6f): immense four-legged prowl OR wing-assisted hover-stride.
attack (1–4f): rears, throat-core flares, unleashes a green-fire breath cone.
death  (4–6f): collapses, wings crumple, scale-cracks blaze then go out, dissolves, hold last.
breach (2–4f): bites/claws the base, or breath-blasts it.
PROJECTIONS: back = full dorsal wing span + spine ridge; sides = profile head + tail.
```

---

### 3.C HEROES

> Each hero needs: `spawn` / `walk` / `attack` / `death` / `summon`, all × 6 projections.
> Ranged heroes (Hunter, Mage) also get `projectile`. Heroes = WARM amber/gold, NOT void-purple.
> File naming: `paladin_<action>_<projection>.png`, `mage_…`, `hunter_…`.

#### `paladin` — Paladin (Order of Light · melee tank/support)

```
SUBJECT: a noble armored knight — polished steel plate in light blue-grey (#3a4458→#cdd6e2,
NEVER pure black), white-and-gold tabard with radiant cross/sun sigil, winged great-helm,
longsword + holy kite shield glowing warm gold. 96–128px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips × 6 projections use identical cell, same scale, same baseline.

spawn  (5–6f): descends in a shaft of gold light, shield raised, helm-crest flaring.
walk   (6f): proud steady armored march, tabard/cape sway, shield forward.
attack (6f): overhead or diagonal sword cleave with gold light-trail, shield braced.
death  (6f): staggers, shield drops, gold light gutters then bursts gently upward, hold last.
summon (5–6f): plants sword/shield, raises a hand → a dome/ring of golden shields blooms out.
PROJECTIONS: cross/sun sigil + glowing kite shield visible from all 6 angles.
```

#### `mage` — Mage (Ether Circle · ranged caster)

```
SUBJECT: a robed arcanist in deep teal-and-violet star-robes with gold trim, wide pointed hat
or circlet, rune-staff topped with a floating ETHER CRYSTAL glowing cyan-amber, orbiting
spell-glyphs. NOT corrupted — cool cyan/teal magic. 96–120px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips × 6 projections use identical cell, same scale, same baseline.

spawn  (5–6f): a glyph-circle spins up beneath, mage fades in, staff-crystal ignites.
walk   (6f): gliding near-hovering stride, robe and glyphs trailing, crystal pulsing.
attack (6f): raises staff, gathers swirling ether orb and casts it forward (→projectile).
death  (6f): crystal cracks, robes collapse as ether disperses in cyan sparks, hold last.
summon (6f): both arms wide, staff overhead → a large ether nova / slow-field glyph expands out.
PROJECTILE (mage_projectile_*, ~24px, 5f × 6 proj): swirling cyan-amber ether orb / arcane
           bolt with sparkling trail, trail pointing opposite to travel per projection.
```

#### `hunter` — Hunter (Pathfinders · ranged skirmisher)

```
SUBJECT: an agile ranger in weathered green-and-leather forest garb, hood, amber-gold accents,
recurve longbow or repeating crossbow, quiver of bright arrows. Light and poised. 96–104px cell.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: all action strips × 6 projections use identical cell, same scale, same baseline.

spawn  (5–6f): drops in from a roll / steps out of green-amber light, draws and nocks an arrow.
walk   (6f): light confident skirmisher's stride, cloak fluttering.
attack (6f): draws bow fully and looses an arrow (→projectile), quick recovery + re-nock.
death  (6f): spins and falls to a knee, bow dropping, warm amber ember rises, hold last.
summon (5–6f): plants a foot, raises bow overhead, fires signal-volley → amber rally-burst.
PROJECTILE (hunter_projectile_*, ~36px, 5f × 6 proj): long fletched arrow with amber-glowing
           tip and fast streak, drawn per projection so it points along travel.
```

---

### 3.D TOWERS & BUILDINGS

> Buildings: single-direction layered object atlas. Runtime = compact transparent atlas with tight JSON rects. Human QA = separate fixed-cell review grid.
> Actions: idle child loops, attack one-shot FX, destroy debris/ruin pieces.
> VIEW: TRUE TOP-DOWN ORTHOGRAPHIC preferred for cardboard tabletop tokens; near top-down slight tilt only when readability requires it. No facade/tall tower read.
> PROPORTION LOCK: composed base/body footprint stays stable across all actions; child FX may extend only inside safe margins.

#### `watchtower` — Warden's Post  [+projectile]

```
SUBJECT: cardboard tabletop Watchtower token: circular stone platform with tan exposed cardboard
edge, central wooden/metal rotation socket, separate rotatable crossbow, separate flag pole,
red wind flag cloth, separate lantern body/flame, projectile bolt, muzzle flash, debris.
VIEW: TRUE TOP-DOWN ORTHOGRAPHIC 90° preferred. No side/facade/rear/tall tower read.
LAYER CONTRACT:
- base_stone_token: static locked footprint.
- central_socket: static or subtle rotation detail.
- crossbow_rotatable: separate active part, rotates to target at runtime.
- flag_pole: static pole/base.
- flag_cloth_wind_01..04: wind loop, attaches to flag pole.
- lantern_body: static.
- lantern_flame_01..04: flame loop, attaches to lantern body.
- muzzle_flash_01..04: one-shot attack FX at crossbow muzzle.
- projectile_bolt: separate projectile, rotates along trajectory.
- destroy_debris_01..N: individual debris pieces for destroy/physics.
OUTPUT: compact transparent runtime atlas + JSON manifest + separate review grid.
DESTROY: individual stone/wood/cardboard debris pieces, optional ruin overlay, no single huge grouped strip unless documented.
PROJECTILE: separate `projectile_bolt` layer with pivot and trajectory rotation.
```

#### `ranger` — Garrison Ranger  [+projectile]

```
SUBJECT: watchtower refitted — taller fletched-arrow rack, green-amber hunting optics lens,
manned firing platform. Same stone tower body, hunter-green accents.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): optics lens glints (1px highlight shifts), arrows in rack quiver slightly,
             platform/tower body is pixel-static.
attack  (4f): rapid crossbow volley snap, green-amber flash.
destroy (5f): platform collapses, arrows spill, hold last.
PROJECTILE (ranger_projectile.png, 36px): longer fletched bolt, fast streak, optics-green tip.
```

#### `tracker` — Crown Tracker  [uses ranger projectile]

```
SUBJECT: ranger upgraded — tall spotter's spire with a big rune-optics ring and royal banners.
Amber + regal blue accents.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): optics ring slowly rotates/scans, banners sway.
attack  (4f): precise long bolt fires with bright trailing flash.
destroy (5f): spire topples, ring shatters, hold last.
```

#### `assassin` — Shadow Archer

```
SUBJECT: ranger upgraded toward stealth-crit — a darkened shrouded perch, single heavy
sniper-ballista bolt, faint violet-amber crit shimmer. Low hooded silhouette.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): fabric shrouds drift (hem pixels shift), the bolt tip crit-glow brightens
             frame-by-frame as it charges — perch body is pixel-static.
attack  (4f): one heavy bolt fires with a sharp crit-spark.
destroy (5f): perch caves in, hold last.
```

#### `ballista` — Fortress Ballista  [+projectile +impact]

```
SUBJECT: a converted watchtower mounting a huge anti-air ballista on a swivel, ether-lens
sight, heavy bolt rack. Cold stone + steel + amber lens.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): swivel arm tracks the sky slowly, lens glows.
attack  (4f): ballista arm snaps forward, string twang, bolt away.
destroy (5f): arm cracks off, tower buckles, hold last.
PROJECTILE (ballista_projectile.png, ~40px strip): heavy steel bolt, fast, faint amber trail.
IMPACT (ballista_impact.png): sharp metallic spark-burst + bolt-shatter.
```

#### `scorpion` — Sky Scorpion  [uses ballista projectile/impact]

```
SUBJECT: ballista upgraded to a massive single-shot harpoon-launcher with scorpion-tail
counterweight, ether-harpoon glowing amber.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): tail-counterweight sways, harpoon hums.
attack  (4f): violent harpoon launch, big recoil.
destroy (5f): arm snaps and whips down, hold last.
```

#### `hailstorm` — Hailstorm Ballista  [+projectile +impact]

```
SUBJECT: ballista upgraded to a multi-bolt repeater rack (anti-swarm), fan of small bolts,
spinning string-drum.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): drum slowly spins, bolts settle in rack.
attack  (4f): spread of small bolts flits out, rapid flicker.
destroy (5f): rack disintegrates, bolts scatter, hold last.
```

#### `cannon` — Field Cannon  [+projectile +impact]

```
SUBJECT: an improvised siege cannon on a stone-and-timber carriage, alchemical-shell muzzle,
amber powder-glow. Volatile, slightly ramshackle.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): smoke drifts from muzzle (wisp pixels shift), fuse-ember flickers — carriage
             and barrel are pixel-static, no rocking or settling.
attack  (4f): big muzzle-flash boom, carriage recoils back, smoke cloud.
destroy (5f): barrel bursts, carriage splinters, hold last as smoking wreck.
PROJECTILE (cannon_projectile.png, 18px): round dark-bronze cannonball (#2a2118, NOT black)
           with faint amber heat-glow + smoke wisp.
IMPACT (cannon_impact.png): orange-amber splash explosion + debris ring.
```

#### `mortar` — Siege Mortar  [+projectile +impact]

```
SUBJECT: cannon upgraded to stubby high-angle mortar, thick reinforced tube pointed up,
heavy armor-piercing shells stacked beside.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): tube vents smoke, a shell glows in the breech.
attack  (4f): deep lobbed-shot blast, heavy recoil downward, smoke ring.
destroy (5f): tube cracks and slumps, hold last.
PROJECTILE (mortar_projectile.png, 20px): heavy arcing shell, dark-bronze, amber core.
IMPACT: large amber ground-burst.
```

#### `grapeshot` — Grapeshot Battery  [+projectile +impact]

```
SUBJECT: cannon upgraded to wide multi-barrel scattergun battery, fanned barrels.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): barrels glow with fuse-embers, slight smoke.
attack  (4f): wide fan muzzle-flash, all barrels boom, big smoke spread.
destroy (5f): barrel-cluster blows apart, hold last.
PROJECTILE: spray of small amber pellets; IMPACT: wide low scatter-burst.
```

#### `palisade` — Palisade  [+projectile +impact]

```
SUBJECT: a bristling defensive wall-stake emplacement — sharpened thorn-logs + ballista
spikes, living-wood green-amber, vines.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): vines and thorns subtly sway, green glow pulses.
attack  (4f): thorn-spikes shoot out / stake fires, green flash.
destroy (5f): stakes snap and frame collapses, hold last.
PROJECTILE (palisade_projectile.png): sharp wooden thorn-spike, green-tipped.
IMPACT (palisade_impact.png): green thorn-burst / splinter spray.
```

#### `obelisk` — Obelisk (captured void, anti-machine)  [+projectile +impact]

```
SUBJECT: a tall floating rune-obelisk of captured void energy — levitating dark-violet crystal
monolith, gold-rune bands, arc of purple lightning at the tip. Darkest pixel #1c1726, no
pure black. (Purple is allowed here — it's captured void, still allied.)
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): crystal hovers and bobs, runes pulse, arcs crackle.
attack  (4f): violet lightning-bolt lances from the tip, blinding flash.
destroy (5f): crystal cracks, energy implodes/scatters, hold last.
PROJECTILE (obelisk_projectile.png, 22px): crackling violet energy bolt with branching arcs.
IMPACT (obelisk_impact.png): purple electric burst / arc-shatter.
```

#### `beacon` — Beacon (sun tower, anti-air)  [+projectile +impact]

```
SUBJECT: a tall lighthouse-like beacon topped with a radiant gold sun-lens / brazier,
holy warm light, anti-air focus. The brightest, warmest structure.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): sun-lens pulses warm gold, light rays shimmer, brazier flickers.
attack  (4f): focused gold light-beam/flare lances upward, bright bloom.
destroy (5f): lens cracks, light gutters, tower collapses, hold last.
PROJECTILE (beacon_projectile.png, 18px): radiant gold light-mote / sun-bolt with bright comet.
IMPACT (beacon_impact.png): warm gold flash-burst / radiant ring.
```

#### `sawmill` — Sawmill (wood economy)  [idle + destroy]

```
SUBJECT: a small timber sawmill hut with a spinning saw wheel, log piles, green roof.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: idle/destroy use identical cell.

idle    (5f): saw-wheel rotates, sawdust puffs, chimney smoke.
destroy (5f): wheel splinters, hut caves in, logs spill, hold last.
```

#### `quarry` — Quarry (stone economy)  [idle + destroy]

```
SUBJECT: a small stone-cutting quarry rig — a pick-arm derrick over a rock pit, cut-stone
blocks stacked, grey.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: idle/destroy use identical cell.

idle    (5f): pick-arm chips the rock, dust puffs, a pulley turns.
destroy (5f): derrick collapses, rocks tumble into pit, hold last.
```

#### `castle` — The Fortress / Grimhold (player base)

```
SUBJECT: the great fortress keep — cold grey stone ramparts, gold seal-crack lines through
the walls, amber-lit gatehouse, tattered Warden banners, central seal-crystal spire. ~139×120.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.

static  (1f or gentle 5f idle): banners sway, seal-crystal pulses gold, brazier flicker.
destroy (9–10f): walls breach section by section, seal-crystal cracks and erupts, gatehouse
        collapses — hold last on smoking ruin.
```

#### `spawn_cave` — Voidrift Spawn Cave (enemy portal)

```
SUBJECT: a jagged cave-mouth / void-rift where enemies emerge — dark rock arch, swirling
purple Voidrift portal inside, dripping corruption, glowing violet veins. ~318px wide strip.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.

idle    (5–6f): portal swirls slowly, purple energy churns, veins pulse, drips fall.
spawn   (anim): portal flares bright and bulges as a silhouette pushes out, energy ripple.
```

---

### 3.E PROJECTILES (summary)

**Enemy (×6 projections each):** `air`, `bomber`, `witch_doc`, `necro`, `machine`,
`bossAir`, `bossMachine`. Trail always points opposite to travel direction per projection.

**Tower (single dir):** `watchtower`(20px) `ranger`(36px) `ballista`(40px) `cannon`(18px)
`mortar`(20px) `obelisk`(22px) `beacon`(18px) `palisade` `hailstorm`. Plus `*_impact` for
`ballista`/`cannon`/`obelisk`/`beacon`/`palisade`.

```
PROJECTILE STYLE: tiny but readable energy/ammo sprite, 3–5 frame spin or flicker loop.
Bright core + 1–2px dithered glow + short motion streak. Pure black background, NO pure-black
on the projectile. Color matches owner (amber=player, void-purple=enemy, gold=beacon,
green=palisade). VIEW: near top-down with slight tilt trajectory angle per projection.
```

---

### 3.F RESOURCES & DECOR

> near top-down with slight tilt camera, Grimhold palette, pure-black background,
> NO pure-black on object, NO ground/base/pedestal/soil-patch beneath the object.

#### `tree_oak` — Oak (wood node)

```
SUBJECT: a single gnarled old oak in near top-down with slight tilt view — large sculptural canopy mass,
visible trunk at the center/lower break, dark muted forest-green (#2f4a2e → #5f8a4d),
top-left warm highlight on canopy top, a few restrained accent leaves. NOT a realistic foliage
blob, NOT a front-facing portrait. The near top-down silhouette must identify the tree type immediately.
Darkest pixel = #182414. Single frame. No ground, no soil patch, no base ring beneath the trunk.
```

#### `tree_oak_grow` — Oak growth strip

```
SUBJECT: a 4–6 frame horizontal GROW strip of the oak in near top-down with slight tilt view. Frame 1 =
a tiny sapling sprout visible from the top-down silhouette angle (small trunk stub + tiny canopy dome),
growing taller and fuller each frame, final frame = the full `tree_oak`. The near top-down with slight tilt
angle is consistent across ALL frames — no shifting between 3/2 isometric and side-view. Same
baseline + center across all frames. Same palette, black background, cut-out rule.
PROPORTION LOCK: every frame uses the same cell size as `tree_oak` — the sapling is just
small/centered within that cell, not a smaller canvas.
```

#### `tree_pine` — Pine (wood node, variant)

```
SUBJECT: a single tall conifer in near top-down with slight tilt view — straight dark trunk visible from
the angled crown break, a layered conical canopy above, deep blue-green needles (#243d33 → #4f7a5e),
top-left warm highlight, the cone shape reads from the near top-down silhouette and stacked crown masses.
Darkest pixel = #14201a. Single frame. No ground/soil beneath.
```

#### `tree_pine_grow` — Pine growth strip

```
SUBJECT: a 4–6 frame horizontal GROW strip of the pine in near top-down with slight tilt view. Frame 1 =
a small needle-sprout (tiny trunk + first conical layer visible at the top-down silhouette angle), each
frame taller with more conical layers, final frame = full `tree_pine`. Consistent near top-down with slight tilt
camera across all frames. Consistent baseline + center, same palette, black background.
PROPORTION LOCK: every frame uses the same cell size as `tree_pine`.
```

#### `rock_a` / `rock_b` / `rock_c` — Stone deposits (3 variants)

```
SUBJECT: boulder clusters in near top-down with slight tilt view — weathered cold grey stone
(#4a525e → #aab2bd), chiseled flat top facets, faint amber ore-vein glints. The overhead
silhouette and top planes must make each rock readable. Three silhouettes:
  rock_a = a low wide cluster of 3–4 rounded boulders,
  rock_b = a single tall jagged spire-rock,
  rock_c = a flatter cracked slab with rubble.
Each a single frame, black background, darkest pixel = #1a1e26 (no pure black).
No ground-patch or soil ring beneath the rocks.
```

#### `rock_grow` — Stone growth strip

```
SUBJECT: a 4–6 frame GROW strip of a stone deposit re-forming in near top-down with slight tilt view.
Frame 1 = a few small pebbles visible at the top-down silhouette angle, accreting into a full boulder
cluster (`rock_a` shape) by the final frame. Same near top-down with slight tilt angle all frames. Same
baseline/center. Grey palette, black background.
PROPORTION LOCK: every frame uses the same cell size as `rock_a`.
```

#### `res_gold` — Gold resource icon

```
SUBJECT: a small pickup/UI icon in near top-down with slight tilt — a tidy stack of glowing gold coins
viewed from slightly above-and-to-the-side (the top-down silhouette angle makes the coin faces and the
stack height both visible). Warm amber glint (#b8761f → #ffe06b), 1px dithered shine.
Reads instantly at ~24px in the HUD. Black background, NO pure-black on the icon. Single frame.
```

#### `res_wood` — Wood resource icon

```
SUBJECT: a small pickup/UI icon in near top-down with slight tilt — a bundle of cut logs viewed from
slightly above-and-to-the-side (both the end-grain rings and the log length visible). Warm
brown (#5a3a1f → #9c6b3a), a touch of green bark. Same cell scale as res_gold. Single frame.
```

#### `res_stone` — Stone resource icon

```
SUBJECT: a small pickup/UI icon in near top-down with slight tilt — a neat stack of grey cut-stone blocks
with chiseled top edges and faint amber ore-glint. The top silhouette reads as stacked stone.
(#5a6472 → #aab2bd). Same cell scale as res_gold and res_wood. Single frame.
```

#### `backgroud` — Battlefield terrain (the map itself)

```
SUBJECT: the full Grimhold battlefield ground, top-down-iso, as ONE opaque scene (this is the
ONLY asset that does NOT use the cut-out rule — it fills the frame, no black-key). Cracked grey
flagstone enemy paths winding down the map, dark mossy earth and dead grass between, void-tainted
purple-cracked patches near the top spawn caves, warm torch-lit stone and gold seal-glow near the
fortress at the bottom. Muted, grim, cohesive with all sprites. Keep the walkable paths clearly
lighter/distinct from buildable ground so enemy lanes read. SNES 16-bit texture, subtle 1px
dithering, no modern smooth gradients.
```

---

### 3.G HERO-SPECIFIC SPECIAL BUILDINGS

> 9 unique buildings — 3 per hero. Use Layered Object Pipeline v2: compact runtime atlas + JSON manifest + separate review grid.
> VIEW: NEAR TOP-DOWN WITH SLIGHT TILT for all — roof/top silhouette is primary; subtle wall thickness is visible.
> PROPORTION LOCK: composed base/body footprint remains stable across actions; child layers animate independently.

| Hero | id | Name | Role | dmg | range | rate | cost | cap |
|------|----|------|------|-----|-------|------|------|-----|
| **Paladin** | `pal_ward` | Sanctum Ward | Support aura | 0 | 92 | — | 180 | 4 |
| | `pal_censer` | Censer Spire | Holy AoE / DoT | 20 | 100 | 1.0 | 240 | 4 |
| | `pal_reliquary` | Reliquary Bastion | Heavy smite | 60 | 120 | 1.8 | 300 | 3 |
| **Mage** | `mage_frost` | Frost Conduit | Control / slow | 12 | 110 | 0.9 | 200 | 5 |
| | `mage_tesla` | Storm Coil | Chain lightning | 28 | 120 | 1.1 | 260 | 4 |
| | `mage_prism` | Void Prism | Arcane nuke / AoE | 70 | 100 | 2.0 | 320 | 3 |
| **Hunter** | `hunt_snare` | Bramble Snare | Ground trap | 8 | cell | trigger | 150 | 5 |
| | `hunt_roost` | Hawk's Roost | Precision / crit | 50 | 170 | 1.3 | 240 | 4 |
| | `hunt_hive` | Toxic Hive | Poison / swarm | 14 | 115 | 0.85 | 220 | 4 |

#### `pal_ward` — Sanctum Ward  [idle + pulse + destroy, no projectile]

```
SUBJECT: a low holy shrine-pylon — a pale marble + gold-trim column BODY topped with a slowly
rotating ring of golden seal-runes and a hovering radiant sigil-stone, a soft warm dome/aura of
light hugging its lower body (a glow EFFECT, NOT a ground disc/base). Light blue-grey stone +
warm gold glow (#ffe06b). Darkest #1a1e26.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/pulse/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): rune-ring rotates (the ring itself spins, column body is static), sigil-stone
             slowly bobs up-down (it's a floating gem — physically justified), a faint warm
             glow emanates from the lower-body runes — NO whole-structure scale or breathing.
pulse   (4f, as "attack"): dome flares outward in expanding gold aura ring, then settles.
destroy (5f): rune-ring shatters, sigil cracks, dome collapses inward, hold last.
```

#### `pal_censer` — Censer Spire  [+projectile +impact]

```
SUBJECT: a tall thin holy spire — a gothic stone column hung with swinging golden censers/
braziers dripping blessed flame, a sun-cross finial on top, chains and incense smoke.
Radiant orange-gold fire, white-gold core.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): censers swing gently, embers drift, smoke curls.
attack  (4f): censers swing wide and fling a blob of holy fire (→projectile), flare.
destroy (5f): spire cracks, censers fall scattering burning embers, hold last.
PROJECTILE (pal_censer_projectile.png, ~20px): small comet of white-gold holy fire + ember trail.
IMPACT (pal_censer_impact.png): radiant gold flame-burst (the burn pool).
```

#### `pal_reliquary` — Reliquary Bastion  [+projectile +impact]

```
SUBJECT: a squat fortified holy bastion — heavy armored reliquary-turret of gold-banded white
stone, a great hammer-of-light / smite-cannon mounted on top, stained-glass facets glowing,
a relic-crystal charging between shots.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): relic-crystal pulses brighter as it charges, stained glass shimmers.
attack  (4f): smite-cannon discharges a thick descending bolt of gold light, big recoil + flash.
destroy (5f): bastion buckles, relic-crystal cracks and erupts light, hold last.
PROJECTILE (pal_reliquary_projectile.png, ~22px): heavy radiant smite-bolt / falling light-spear.
IMPACT (pal_reliquary_impact.png): big white-gold holy detonation + stun-ring sparkle.
```

#### `mage_frost` — Frost Conduit  [+projectile +impact]

```
SUBJECT: a slender Ether-Circle conduit — a polished obsidian-teal pillar wrapped in floating
ICE-CRYSTAL rings and frost-runes, hovering pale-cyan focus gem, faint frost mist. Cool
teal-cyan (#1f5560→#9fe6ef) + gold rune trim. NOT void-purple.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): crystal rings rotate, focus gem pulses cyan, frost mist drifts.
attack  (4f): gem snaps and fires a shard of frost-energy (→projectile), chill flash.
destroy (5f): crystal rings shatter into ice-shards, pillar cracks, hold last.
PROJECTILE (mage_frost_projectile.png, ~22px): spinning pale-cyan ice shard / frost orb.
IMPACT (mage_frost_impact.png): cyan frost-burst with radiating slow-rings + ice crystals.
```

#### `mage_tesla` — Storm Coil  [+projectile +impact]

```
SUBJECT: an arcane tesla-spire — a tall coil-pillar of banded copper-and-arcane-steel, a
crackling ETHER ORB cradled in rune-prongs at the top, arcs of cyan-white lightning.
Cyan-white energy (#bfeaff) + warm copper (#b8761f) + gold runes.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): small cyan-white arcs flicker between the fixed prong-tips (arcs appear/fade),
             the floating orb glows steadily — the coil column and prongs are pixel-static.
attack  (4f): orb discharges a forking lightning bolt (→projectile), bright strobe flash.
destroy (5f): coil shorts out in shower of sparks, orb implodes, hold last.
PROJECTILE (mage_tesla_projectile.png, ~22px): jagged branching lightning bolt, cyan-white core.
IMPACT (mage_tesla_impact.png): electric arc-burst with jump-arcs leaping to sides.
```

#### `mage_prism` — Void Prism  [+projectile +impact]

```
SUBJECT: a floating arcane PRISM — a large levitating multi-facet crystal (deep amethyst-teal,
darkest #241a33, NOT black) cradled above a short rune-inscribed arcane column (the tower body,
NOT a ground pedestal/base), refracting arcane light, gathering a bright mana-core between shots.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
column's lowest pixel is the anchor; NO ground/soil/disc beneath it.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): prism slowly rotates and refracts, mana-core brightens.
attack  (4f): prism flares blinding and unleashes wide arcane blast, big bloom.
destroy (5f): prism fractures along facets, mana implodes, shards scatter, hold last.
PROJECTILE (mage_prism_projectile.png, ~24px): dense refracting arcane orb / energy lance,
           cyan-violet, heavy glow (moves slowly, hits hard).
IMPACT (mage_prism_impact.png): large arcane shockwave detonation, wide ring, armor-shatter spark.
```

#### `hunt_snare` — Bramble Snare  [idle + trigger + destroy, no projectile]

```
SUBJECT: a Pathfinder ground TRAP — a ring of camouflaged thorn-vines and a hidden barbed
snare around a faint green tripwire-glow. Low to the ground — the near top-down with slight tilt view shows
the top of the vine ring AND the slight side thickness of the trap mechanism. Earthy green-brown
(#2f4a2e→#7a9c4d) + amber tripwire glints.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/trigger/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): individual vine leaves stir (2–3 leaf-pixels shift position), the tripwire-
             glow blinks on/off — the thorn-stakes and ground ring are pixel-static.
trigger (4f, as "attack"): thorny brambles SNAP up violently, then retract — fast, snappy.
destroy (5f): snare withers and vines blacken-to-grey and crumble, hold last.
TRIGGER FX (hunt_snare_impact.png): burst of thorns + green snare-runes + bleed-spatter.
```

#### `hunt_roost` — Hawk's Roost  [+projectile +impact]

```
SUBJECT: a tall Pathfinder marksman's roost — a timber-and-rope watch-perch with draped green
camo-canvas, a mounted heavy hunting-ballista / longbow rig, a perched HAWK companion and
ranging optics. Weathered wood + green canvas + amber optics.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): hawk shifts and ruffles, optics scan/glint, canvas sways.
attack  (4f): rig looses a single precise long-range bolt with amber crit-flash, hawk flares wings.
destroy (5f): perch collapses, canvas tears, hawk flies off, hold last.
PROJECTILE (hunt_roost_projectile.png, ~36px): long fletched precision arrow/bolt, amber tip.
IMPACT (hunt_roost_impact.png): sharp amber crit-spark / pierce-burst.
```

#### `hunt_hive` — Toxic Hive  [+projectile +impact]

```
SUBJECT: a Pathfinder alchemist's TOXIC HIVE — a gnarled hollow stump/hive rig dripping sickly
green venom, clustered wasp-comb cells, a bubbling poison vat at its base, faint green spore-haze.
Sickly green-yellow (#3a5a1f→#9bc24a) venom + brown wood. Allied-green, NOT enemy-purple.
VIEW: NEAR TOP-DOWN WITH SLIGHT TILT — 85-90% top planes, 10-15% subtle side thickness; no tall facade.
PROPORTION LOCK: composed base/body footprint remains stable across idle/attack/destroy; runtime uses layered rects and pivots, not a 48×64 strip cell.

idle    (5f): vat surface bubbles (liquid pixels shift), venom drips fall from the hive,
             spore particles drift upward, individual comb cells blink faintly (not all
             at once) — the stump/hive body is pixel-static.
attack  (4f): hive lobs a glob of venom / releases spore-burst (→projectile).
destroy (5f): hive collapses, vat spills, spores disperse, hold last.
PROJECTILE (hunt_hive_projectile.png, ~24px): arcing green venom glob / spore-cluster.
IMPACT (hunt_hive_impact.png): green poison splash-cloud that lingers a beat.
```

---

## 4. GENERATION CHECKLIST (per asset)

- [ ] MASTER STYLE PROMPT pasted first, then the object block.
- [ ] Background matches pipeline stage: imagegen source may use flat #ff00ff chroma-key; final runtime atlas is transparent. NO pure-black anywhere ON the object.
- [ ] **TOP-DOWN READ** — cardboard tabletop objects prefer true top-down orthographic 90°. Near top-down slight tilt is allowed only when readability requires it. NOT full isometric. NOT 3/4 side-view. NOT side-scroller. NOT forced perspective.
- [ ] **PROPORTION LOCK** — composed base/body footprint, pivot, and gameplay scale stay stable across all actions. Child layers animate independently.
- [ ] Layered objects: compact transparent runtime atlas + JSON tight rects + separate review grid. Legacy strip exports only when explicitly required.
- [ ] Correct projection facing (front/back/3qr/3ql/sider/sidel) — 6 files for moving units.
- [ ] Correct palette (warm amber = player, toxic green = Horde magic, grey stone = structure).
- [ ] No pedestal, no soil patch, no ground disc, no base ring beneath any object.
- [ ] Silhouette readable + distinct at small size.
- [ ] Projectile + impact generated for ranged owners.
- [ ] File named to the §2.3 convention, dropped in the right folder.

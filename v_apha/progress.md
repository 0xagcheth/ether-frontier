Original prompt: Создать production-ready Sprite Atlas для 2D-игры Ether Frontier, продолжать объекты по манифесту и показывать их на сайте с анимацией.

## Completed

- Goblin spearman animation lab uses 384px runtime atlases.
- Batch 1 environment masters/runtime assets: oak, pine, rock A/B/C, gold, wood, stone, battlefield.
- Runtime normalization: centered 384px cells, 255px target extent, clipping QA.
- Sprite Lab environment library added with live 8-frame growth previews.
- Browser QA passed for hero unit view and environment library at 1280×720.
- Environment overlay shows all 8 assets without clipping; deterministic text state and time-step hooks are available.
- Watchtower master and production runtime complete: idle 5f, attack 4f, destroy 5f, projectile.
- Watchtower automated QA: locked intact extent 255px, projectile 82px, no clipped frames.
- Sprite Lab building preview added; idle and attack browser QA passed.
- Ranger master and runtime complete: idle 5f, attack 4f, destroy 5f, projectile.
- Ranger QA: intact body locked to 255px; detached attack projectile does not affect body scale; no clipping.
- Building Lab selector now switches between Watchtower and Ranger; Ranger browser QA passed.
- Tracker master and runtime complete: idle 5f, attack 4f, destroy 5f; reuses ranger projectile.
- Tracker attack normalization locks the massive stone ring independently from connected/detached bolt effects.
- Building Lab now switches across Watchtower, Ranger and Tracker; Tracker idle browser QA passed.
- Assassin master/runtime complete: idle 5f, attack 4f, destroy 5f; no standalone projectile per manifest.
- Assassin QA: 255px locked idle body, stable attack silhouette, no clipped frames.
- Building Lab now switches across four completed towers; Assassin idle browser QA passed.
- Ballista master/runtime complete: idle 5f, attack 4f, destroy 5f, projectile and impact.
- Ballista QA: 255px locked platform, 146px projectile, 112px impact, no clipping.
- Building Lab now switches across five completed towers; Ballista idle browser QA passed.
- Scorpion master/runtime complete: idle 5f, attack 4f, destroy 5f; reuses Ballista projectile and impact.
- Scorpion QA: 255px locked intact body, 146px projectile, 112px impact, no clipped frames.
- Building Lab now switches across six completed towers; Scorpion idle browser QA passed at 1280×720.
- Hailstorm master/runtime complete: idle 5f, attack 4f, destroy 5f, volley projectile and impact.
- Hailstorm QA: 255px locked intact body, 118px projectile/impact, no clipped frames.
- Building Lab now switches across seven completed towers; Hailstorm idle browser QA passed at 1280×720.
- Field Cannon master/runtime complete: idle 5f, attack 4f, destroy 5f, heated cannonball and debris-ring impact.
- Cannon QA: 255px locked intact body, 96px projectile, 128px impact, no clipped frames.
- Building Lab now switches across eight completed towers; Cannon idle browser QA passed at 1280×720.
- Siege Mortar master/runtime complete: idle 5f, attack 4f, destroy 5f, arcing shell and broad ground-burst impact.
- Mortar QA: 255px locked intact body, 104px projectile, 132px impact, no clipped frames.
- Building Lab now switches across nine completed towers; Mortar idle browser QA passed at 1280×720.
- Grapeshot Battery master/runtime complete: idle 5f, attack 4f, destroy 5f, pellet fan and wide scatter impact.
- Grapeshot QA: 255px locked intact body, 124px projectile, 140px impact, no clipped frames.
- Building Lab now switches across ten completed towers; Grapeshot idle browser QA passed at 1280×720.
- Living Palisade master/runtime complete: idle 5f, attack 4f, destroy 5f, thorn projectile and splinter-vine impact.
- Palisade QA: idle locked to 255px, attack 261–270px including launch effects, projectile 120px, impact 128px, no clipped frames.
- Source-sheet divider cleanup now detects and removes long internal near-white separators without erasing local flashes.
- Building Lab now switches across eleven completed towers; Palisade idle browser QA passed at 1280×720.
- Obelisk HD master generated and saved; animation/source strips remain to build.
- Void Obelisk production set complete: idle 5f, attack 4f, destroy 5f, violet lightning projectile and arc-shatter impact.
- Obelisk QA: idle locked to 255px; attack 255–270px including arcs; destroy safely contracts after a 279px fragment burst; projectile 112px; impact 136px; no clipped frames.
- Green chroma-key VFX sources now use the alpha-source preference path; transparent projectile/impact outputs were visually verified.
- Building Lab now switches across twelve completed towers; Obelisk idle browser QA passed at 1280×720 with no reported console errors.
- Sun Beacon production set complete: idle 5f, attack 4f, destroy 5f, sun-bolt projectile and radiant-ring impact.
- Beacon QA: idle locked to 255px; attack 255–266px with fully contained short lance; destroy 252–256px; projectile 92px; impact 132px; no clipped frames.
- Building chroma extraction can now preserve white highlights, preventing transparent holes in bright attack/projectile/impact cores.
- Building Lab now switches across thirteen completed towers; selector has a bounded scroll region so animation controls remain visible at 1280×720.
- Beacon idle browser QA passed at 1280×720 with no reported console errors.
- Economic-building runtime support added: attack strips/actions are optional, while idle/destroy remain production-normalized.
- Sprite Lab action controls now support per-object availability and visually disable unsupported actions.
- Existing Beacon runtime and browser preview were regression-tested after the optional-action changes.
- Timber Sawmill cardboard master generated with built-in ImageGen and saved into workspace.
- Sawmill source/runtime complete: idle 5f and destroy 5f, no attack/projectile/impact.
- Sawmill QA: idle locked to 255px across all frames; destroy contracts 255/255/235/223/212px; no clipped frames; magenta-key fringe cleaned.
- Building Lab now switches across fourteen completed buildings/towers; Sawmill idle and destroy browser QA passed at 1280x720 with no console errors.
- Building Lab vertical layout tightened so long selected names remain visible at 1280x720.
- Stone Quarry runtime verified and re-cleaned: idle 250-255px, destroy 233-255px, no clipped frames, magenta-key remnants removed.
- Building Lab now switches across fifteen completed buildings/towers; Quarry destroy browser QA passed at 1280x720 with no console errors.
- Grimhold Castle runtime verified and re-cleaned: idle 254-255px; destroy 197-255px across 10 frames; no clipped frames; magenta-key remnants removed.
- Building Lab now switches across sixteen completed buildings/towers; Castle idle and 10-frame destroy browser QA passed at 1280x720 with no console errors.
- Voidrift Spawn Cave runtime verified: idle 254-255px, spawn 255px across all frames, no clipped frames.
- Building Lab now switches across seventeen completed objects; Spawn Cave spawn browser QA passed at 1280x720 with no console errors.
- Building Lab action controls now include SPAWN and support per-object action frame/duration overrides.
- Hero-specific runtime audit completed for available candidates.
- Integrated Paladin Ward, Paladin Censer, Paladin Reliquary, Mage Frost, Mage Tesla and Hunter Snare after rebuilding with chroma-fringe cleanup.
- QA for those six: no clipped frames; magenta-key remnants removed; browser QA passed for Pal Ward pulse and attack actions on Pal Censer, Pal Reliquary, Mage Frost, Mage Tesla and Hunt Snare at 1280x720 with no console errors.
- Building Lab now switches across twenty-three completed objects; action controls include PULSE and use a compact grid layout.
- Style reset restarted from Watchtower after comparing against the supplied concept, resource tokens and Goblin Spearman.
- Watchtower v3 rebuilt as a true top-down / orthographic cardboard board-token crossbow post, replacing the older tilted/tall tower reads.
- Current Watchtower QA: idle [255,255,255,255,255], attack [256,256,256,256], destroy [255,255,227,224,233], projectile [82], no clipped frames, magenta-key remnants removed, browser QA passed for attack and destroy.
- Sprite Lab now cache-busts building runtime PNGs with BUILDING_ASSET_VERSION=27 so corrected atlases replace stale browser images.
- Layered Object Pipeline v2 documented as the new default visual/source pipeline: one object-specific atlas PNG + JSON manifest, separated base/body/active/ambient/attack/projectile/impact/destroy layers, explicit pivots/attachments/draw order/runtime transforms, under 5 MB.
- Watchtower layered demo created for user validation: `assets/sprite-atlases/watchtower/layered-demo/watchtower_layered_demo_atlas.png`, review grid, composite preview, and manifest. Demo atlas is 1024x1280 RGBA and ~59 KB, with all demo layers in one PNG.
- Watchtower layered ImageGen v1 created from built-in imagegen: `assets/sprite-atlases/watchtower/layered-imagegen-v1/watchtower_layered_imagegen_v1_chroma.png`, alpha atlas, review rect overlay, and manifest. Alpha atlas is 1536x1024 RGBA, ~1.4 MB, under 5 MB. Style matches the confirmed top-down cardboard board-token baseline. Known issue: imagegen produced 3 strong muzzle flash frames instead of requested 4, and production packing still needs fixed-grid normalization.
- Watchtower layered ImageGen v1 was repacked into a code-friendly fixed 512px grid: `assets/sprite-atlases/watchtower/layered-imagegen-v1/packed-grid/watchtower_layered_imagegen_v1_packed_512.png` plus manifest/review. Runtime atlas is 2048x4096 RGBA, 4x8 cells, ~1.35 MB, under 5 MB. Each runtime sprite is isolated in one transparent cell; assembled preview is excluded; debris is split into `destroy_debris_01..14`.
- Final production atlas decision documented: runtime must use a compact transparent packed atlas with tight JSON rects/pivots/attachments; fixed-cell grids, labels, pivot crosses and assembled previews are human review artifacts only and must not be loaded by gameplay.
- New-window restart prompt prepared at `assets/staging/prompts/restart_layered_generation_from_watchtower.md`; it starts generation from Watchtower and blocks continuing to Ranger until Watchtower layered format is approved.

## Current

- Full visual reset requested on 2026-07-21. Deleted all 926 raster images except the three background files whose paths contain `background`/`backgroud`. All prior atlases, sources, previews, generated assets and browser QA screenshots are gone. The old sites/manifests/scripts may remain as code/history but reference deleted visuals and are not valid runtime sources.
- Restart strategy: generate one assembled Watchtower projection master first, exact 90-degree overhead, approve its spatial construction, then decompose that same approved master into named per-animation runtime layers. ImageGen eventually succeeded after repeated backend network failures. First post-reset visual is `assets/source/watchtower/watchtower_projection_master_v1_chroma.png` (1254x1254, ~2.49 MB): circular top-down platform, central socket/crossbow, flat rim pennant and round top-view lantern. Await user approval before layer decomposition.
- Watchtower layer decomposition generated as a fresh source sheet after reference-edit endpoint failures: `assets/source/watchtower/watchtower_layered_source_v1_chroma.png`. It contains a clean base, socket, top-down crossbow, mount, four pennants, top-view lantern housing, four glow frames, four muzzle flashes, projectile and ten independent debris pieces. Extracted into 28 named layer PNGs plus compact runtime atlas and manifest under `assets/runtime/atlases/watchtower/`; no baked composite frames.
- User stopped visual production and requested a documented modular architecture first. Draft created at `docs/05_assets/modular-object-family-plan.md` with projection/cardboard rules, source-sheet limits, family-core + object-addon runtime architecture, seven building families, shared modules, per-object differences, production order, naming, and quality gates. Machine-readable registry at `docs/05_assets/object-module-registry.json` validates 7 families and 26 unique objects. No further image generation should occur until the draft/open decisions are approved.
- User approved continuing the modular plan. `modular-object-family-plan.md` and `object-module-registry.json` are now approved and incorporated into `docs/00_project/source-of-truth.md`. First planned visual gate generated: `assets/staging/candidates/materials/cardboard_material_swatch_v1_chroma.png`, a non-gameplay top-down physical cardboard calibration specimen. Review recorded at `docs/05_assets/reviews/cardboard-material-swatch-v1.md`; candidate passes material/projection checks and awaits user confirmation before canon registration and `fortress_ranged` chassis generation.
- User approved continuing. Cardboard Material Swatch v1 promoted to CANON at `assets/approved/canon/materials/cardboard_material_swatch_v1_chroma.png` and registered in `canon-asset-registry.md`. Next gated module generated: `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__base_token__round_light_v1_chroma.png`. It is a neutral top-down cardboard base shared by Watchtower/Ranger/Tracker/Assassin with no socket or object-specific addons. Review: `docs/05_assets/reviews/fortress-ranged-base-round-light-v1.md`. Await user approval before alpha extraction and center-socket generation.
- User approved the fortress_ranged base. It is now a CANON module under `assets/approved/canon/modules/fortress_ranged/` with chroma source, transparent tight cutout, and JSON metadata. Validated size 1064x1082, pivot [532,541], locked footprint 1082px, zero magenta-spill pixels. Two built-in ImageGen attempts for the next module `fortress_ranged__center_socket__light_bearing` failed with backend network errors; no socket candidate was created and later modules remain blocked by the gate.
- Retried ImageGen successfully and created `fortress_ranged__center_socket__light_bearing` candidate at `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__center_socket__light_bearing_v1_chroma.png`. It is a standalone true-top-down circular cardboard wood/metal bearing with six rivets and a center axle opening, containing no base or weapon. Review recorded at `docs/05_assets/reviews/fortress-ranged-center-socket-light-bearing-v1.md`. Await user approval before alpha extraction, base+socket proportion preview, and lantern housing generation.

## TODO

- Watchtower Layered Object Pipeline v2 approved-candidate generated in `assets/sprite-atlases/watchtower/layered-v2-candidate/`: new built-in ImageGen chroma source, alpha source, compact 1536px-wide runtime atlas, schema-v2 manifest, separate review grid and composite preview. Runtime contains 27 tight sprites (including nine independent debris pieces) and is under 5 MB. Fourth muzzle-flash frame is an explicitly documented fading hold derived from ImageGen frame 03 because the source sheet returned three flash silhouettes. Await user visual approval; do not continue to Ranger until approved.
- Watchtower v2 layers assembled into the established 384px animation contract at `assets/sprite-atlases/watchtower/layered-runtime-384/`: idle 5f, attack 4f, destroy 5f, projectile 1f, plus per-action strips, a combined 1920x1536 atlas and manifest. Atlas is ~610 KB; every frame has transparent safety margins and the intact base footprint is locked to 255px.
- New manifest-driven `watchtower-lab/` site previews all four actions from the combined atlas, includes frame timeline/buttons, Space pause/play, F fullscreen, `render_game_to_text`, and deterministic `advanceTime`. Browser QA passed for idle, attack, destroy hold-last and projectile; screenshots/states saved under `output/web-game/watchtower-layered-*` with no reported console errors.
- User rejected the baked Watchtower composite because side-view flag/lantern layers violated the overhead camera and spatial assembly was arbitrary. The baked `layered-runtime-384` output is superseded and must not be used.
- Corrected Watchtower runtime v3 created at `assets/sprite-atlases/watchtower/layered-runtime-v3/`. It reuses only valid top-down source parts, discards the side-view flag/lantern source layers, replaces them with flat radial pennant/socket and concentric top-view lantern layers, and exposes named sprites plus `layersByAction`-style full frame compositions. No baked composite frames are stored. `watchtower-lab/` now renders directly from anchors/layers in the v3 manifest; pointer aiming rotates only the crossbow/attack FX. Browser QA passed for idle, attack and destroy with explicit visible-layer state.
- Repair/regenerate `mage-prism`, `hunt-roost`, and `hunt-hive` before exposing them in Sprite Lab.
- Treat `fast` as an enemy/unit pipeline task, not a building-lab object, because it has no building `manifest.json`.
## 2026-07-21 — fortress_ranged center socket prepared

- Promoted `fortress_ranged__center_socket__light_bearing_v1` to the canon module package.
- Extracted transparent tight rect: `1023 × 1051 px`; pivot `[511, 525]`.
- Added manifest with attachment `base_token.center`, draw order `10`, and parent-footprint scale `0.34`.
- Technical QA: zero visible magenta spill, no source clipping, stable centered attachment.
- Built separate transparent composite and checkerboard review image for `base + socket`.
- Gate: waiting for user confirmation of composed proportions before generating the amber lantern housing.
## 2026-07-21 — fortress_ranged amber lantern housing candidate

- Generated `fortress_ranged__ambient_child__amber_lantern_housing_v1` with built-in ImageGen.
- Two reference-image requests failed at the network layer; a clean generation request succeeded without changing model/API mode.
- Saved the project candidate at `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__ambient_child__amber_lantern_housing_v1_chroma.png`.
- Visual QA passes top-down projection, cardboard construction, isolation, symmetry, empty glow aperture, and no baked VFX.
- Gate: waiting for user confirmation before alpha extraction, composed scale validation, and glow-frame generation.
## 2026-07-22 — fortress_ranged lantern housing prepared

- Extracted the approved housing with the standard chroma-removal helper and promoted it to the canon module package.
- Tight rect: `1070 × 1067 px`; pivot `[535, 533]`; zero visible magenta spill.
- Added a transparent center `glow_anchor`, parent position `[0.29, 0.72]`, scale `0.18`, and draw order `20`.
- Built transparent and checkerboard composites for `base + socket + lantern housing`.
- Placement QA passes footprint, center-socket clearance, cardboard separation, projection, and clipping checks.
- Gate: waiting for composed-placement confirmation before generating the four-frame amber glow strip.
## 2026-07-22 — fortress_ranged amber lantern glow source loop

- Generated all four amber glow frames in one built-in ImageGen source-sheet request.
- Saved chroma and provisional alpha sheets under `assets/staging/candidates/modules/fortress_ranged/`.
- Source validation: exact `2 × 2` layout, four isolated frames, identical `427 × 431 px` component bounds, maximum center drift `1 px`, no clipping or baked housing.
- Gate: waiting for user confirmation before splitting, normalizing, manifesting, and composing the animated lantern.
## 2026-07-22 — fortress_ranged amber lantern glow normalized

- Split and normalized four approved glow frames to a shared `440 × 440` canvas and pivot `[220, 220]`.
- Created the canon animation manifest with `180 ms` frame timing, housing `glow_anchor`, scale `0.31`, and draw order `21`.
- Runtime frames total `1,289,118` bytes and contain zero visible magenta spill.
- Created a separate labeled review grid and a `base + socket + housing + animated glow` GIF preview.
- Composed QA passes fit, footprint stability, anchor stability, luminance progression, projection, and active-lantern readability.
- Gate: waiting for animation confirmation before generating the Watchtower-specific crossbow.
## 2026-07-22 — Watchtower light crossbow candidate

- Locked the approved `fortress_ranged` shared core through the animated lantern glow layer.
- Generated the first Watchtower-specific module: `watchtower__active_addon__light_single_crossbow_v1`.
- Candidate passes top-down projection, +X firing axis, cardboard construction, central mounting aperture, muzzle readability, isolation, and no-baked-projectile/FX checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/watchtower__active_addon__light_single_crossbow_v1_chroma.png`.
- Gate: waiting for user confirmation before alpha extraction, pivot/muzzle measurement, and composed rotation-envelope validation.
## 2026-07-22 — Watchtower crossbow prepared and rotation-tested

- Extracted and promoted the approved crossbow to the canon module package.
- Tight rect: `1316 × 896 px`; alpha file approximately `675 KB`; zero visible magenta spill.
- Derived pivot `[648, 447]` from the enclosed axle aperture and muzzle anchor `[1315, 447]` from the +X weapon tip.
- Composed scale is `0.72` of base footprint (`779 × 530 px`).
- Full rotation envelope radius is `396 px` versus `541 px` base radius: PASS.
- Built transparent assembled preview and separate `0°/90°/180°/270°` rotation QA grid.
- Gate: waiting for composed rotation confirmation before generating the simple bolt projectile.
## 2026-07-22 — Watchtower simple bolt candidate

- Generated `watchtower__projectile__simple_bolt_v1` with built-in ImageGen.
- Candidate passes top-down projection, exact +X orientation, cardboard construction, axis symmetry, projectile isolation, and no-baked-trail/impact checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/watchtower__projectile__simple_bolt_v1_chroma.png` (`1774 × 887 px`).
- Gate: waiting for user confirmation before alpha extraction, trajectory/spawn anchors, and composed flight validation.
## 2026-07-22 — Watchtower simple bolt prepared

- Extracted and promoted the approved bolt to the canon module package.
- Tight rect: `1553 × 263 px`; alpha file approximately `412 KB`; zero visible magenta spill.
- Added center trajectory pivot `[776, 131]`, tail spawn anchor `[0, 131]`, and tip impact anchor `[1552, 131]`.
- Composed game size is `203 × 34 px`, equal to `0.26` of the composed weapon length.
- Built muzzle-spawn composite and separate `+X/+45°/-45°` trajectory QA grid.
- QA passes muzzle alignment, rotation stability, projection, clipping, and game-scale readability.
- Gate: waiting for trajectory confirmation before generating the four-frame compact muzzle flash.
## 2026-07-22 — Watchtower compact muzzle flash source sheet

- Generated a four-frame compact golden muzzle-flash source sheet with built-in ImageGen after two network-level failures.
- Saved chroma and provisional alpha sheets under `assets/staging/candidates/modules/fortress_ranged/`.
- Visual QA passes frame count, +X direction, cardboard effect construction, one-shot size progression, isolation, and no-baked-weapon/projectile checks.
- Raw origins need normalization; the peak component slightly crosses the mathematical sheet midpoint, so production splitting must use isolated connected components rather than hard quadrant crops.
- Gate: waiting for user confirmation before component segmentation, shared-pivot normalization, manifesting, and animated attack composition.
## 2026-07-22 — Watchtower muzzle flash normalized

- Segmented the approved source sheet into exactly four connected components without quadrant clipping.
- Normalized frames to a shared `521 × 384` canvas and left-center pivot `[8, 192]`.
- Added one-shot manifest timing: `90 ms × 4`, `loop: false`, draw order `50`, scale `0.20` of weapon length.
- Runtime frames total `428,742` bytes and contain zero visible magenta spill.
- Created a separate labeled QA grid and animated attack preview with a review-only blank reset hold.
- Composed QA passes muzzle lock, +X inheritance, frame stability, one-shot progression, compact envelope, and layer separation.
- Gate: waiting for attack-preview confirmation before generating the separate Watchtower flag mount/pole.
## 2026-07-22 — Watchtower range pennant socket candidate

- Locked the Watchtower firing package after muzzle-flash validation.
- Generated `watchtower__flag_mount__range_pennant_socket_v1` with built-in ImageGen.
- Candidate passes true top-down projection, flat cardboard construction, +X cloth-slot readability, layer isolation, internal-hole preservation, and no-upright-pole checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/watchtower__flag_mount__range_pennant_socket_v1_chroma.png` (`1254 × 1254 px`).
- Gate: waiting for user confirmation before alpha extraction, mount/cloth anchors, and composed placement validation.
## 2026-07-22 — Watchtower range pennant socket prepared

- Extracted and promoted the approved pennant socket to the canon module package.
- Tight rect: `1059 × 616 px`; pivot `[308, 308]`; alpha file approximately `957 KB`; zero visible magenta spill.
- Preserved the transparent cloth slot and derived `cloth_anchor` `[963, 314]` from its centroid.
- Placed the mount at `[0.24, 0.27]` of the base with scale `0.18` and draw order `15`.
- Built transparent composite and separate four-angle weapon-clearance grid.
- QA passes footprint, center clearance, +X orientation, draw-order behavior, readability, and clipping checks.
- Gate: waiting for placement confirmation before generating the four-frame red pennant wind loop.
## 2026-07-22 — Watchtower red range pennant source loop

- Generated all four range-pennant wind frames in one built-in ImageGen source-sheet request.
- Saved chroma and provisional alpha sheets under `assets/staging/candidates/modules/fortress_ranged/`.
- Source QA found exactly four isolated components with consistent widths `574/578/574/576 px` and no clipping, overlap, or detached scraps.
- Frames pass true top-down flat-paper projection, rigid left-tab, +X direction, dark-red cardboard material, and restrained wind-loop checks.
- Gate: waiting for user confirmation before component splitting, shared-pivot normalization, manifesting, and assembled idle animation preview.
## 2026-07-22 — Watchtower range pennant wind loop normalized

- Segmented and normalized the four approved pennant frames to a shared `594 × 255` canvas and pivot `[8, 127]`.
- Created the canon looping manifest with `180 ms × 4`, scale `0.22` of base footprint, and draw order `16`.
- Runtime frames total `849,982` bytes and contain zero visible magenta spill.
- Created a separate labeled QA grid and assembled four-frame idle GIF.
- Composed QA passes cloth-anchor lock, rigid tab stability, +X orientation, jitter, loop readability, layer separation, and footprint checks.
- Gate: waiting for idle-preview confirmation before generating individually addressable destruction/debris pieces.
## 2026-07-22 — fortress_ranged stone debris chunk A candidate

- Began the destruction kit with one file per physical debris object.
- Rejected the first ImageGen result before project import because it was a large multi-stone platform sector.
- Generated and saved the corrected single connected `fortress_ranged__debris__stone_rim_chunk_a_v1` candidate.
- Candidate passes top-down, single-component, rim-brick geometry, cardboard material, isolation, no-neighboring-masonry, and no-detached-chip checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_a_v1_chroma.png` (`1635 × 962 px`).
- Gate: waiting for confirmation before alpha/pivot preparation and the second individual debris piece.
## 2026-07-22 — fortress_ranged stone debris chunk A prepared

- Extracted and promoted the approved single stone fragment to the canon module package.
- Tight rect: `1195 × 640 px`; center-of-mass pivot `[602, 299]`; zero visible magenta spill.
- Set runtime scale `0.14` of base footprint (`151 × 81 px`) and verified it against one intact rim stone.
- Added independent medium-mass destroy defaults for radial velocity, spin, drag, and lifetime.
- Alpha file is `1,473,554` bytes and passes the `5 MB` limit.
- Gate: waiting for runtime-scale confirmation before generating individual `stone_rim_chunk_b`.

## 2026-07-22 — fortress_ranged stone debris chunk B candidate

- Accepted the runtime scale of stone debris chunk A and advanced to the second individually addressable debris module.
- Rejected the first ImageGen attempt before project import because it was a large curved platform/ring sector.
- Generated the corrected `fortress_ranged__debris__stone_rim_chunk_b_v1` as exactly one compact, connected, near-square loose fragment.
- Candidate passes true top-down projection, flat cardboard construction, silhouette differentiation from chunk A, isolation, no-detached-chip, no-platform, and no-clipping checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__debris__stone_rim_chunk_b_v1_chroma.png` (`1254 × 1254 px`, approximately `1.3 MB`).
- Gate: waiting for visual confirmation before alpha extraction, tight rect/pivot preparation, scale comparison, and canon promotion.

## 2026-07-22 — fortress_ranged stone debris chunk B prepared

- Extracted the approved candidate to alpha and removed the compressed magenta edge fringe.
- Promoted `fortress_ranged__debris__stone_rim_chunk_b_v1` to the canonical module package.
- Tight rect: `541 × 612 px`; alpha-weighted center-of-mass pivot: `[268, 277]`; visible magenta spill: `0`.
- Runtime scale is `0.115` of the base footprint (`124 × 140 px`); alpha PNG is `681,030` bytes and passes the `5 MB` limit.
- Added independent medium-small destruction physics and draw order `61` to the manifest.
- Built a separate A/B scale-and-pivot review; the two modules retain distinct silhouettes and consistent physical stone scale.
- Gate: waiting for A/B runtime-pair confirmation before generating the next individual destruction element.

## 2026-07-22 — fortress_ranged stone core chunk C candidate

- Locked the approved A/B runtime pair and advanced to a third independently addressable debris silhouette.
- Generated `fortress_ranged__debris__stone_core_chunk_c_v1` with built-in ImageGen.
- Candidate is exactly one connected inner-stone cardboard shard with no curved rim geometry, making it structurally distinct from chunks A and B.
- Visual QA passes strict top-down projection, flat cardboard construction, isolation, silhouette differentiation, no-detached-piece, no-platform, and no-clipping checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/fortress_ranged__debris__stone_core_chunk_c_v1_chroma.png` (`1254 × 1254 px`, approximately `1.2 MB`).
- Gate: waiting for visual confirmation before alpha extraction, pivot/scale preparation, and A/B/C runtime comparison.

## 2026-07-22 — fortress_ranged stone core chunk C prepared

- Extracted and promoted the approved `fortress_ranged__debris__stone_core_chunk_c_v1` candidate to the canonical module package.
- Tight rect: `535 × 622 px`; alpha-weighted center-of-mass pivot: `[259, 316]`; visible magenta spill: `0`.
- Runtime scale is `0.095` of the base footprint (`103 × 120 px`); alpha PNG is `595,574` bytes and passes the `5 MB` limit.
- Added small-mass destruction physics and draw order `62` to the manifest.
- Built the separate A/B/C runtime scale-and-pivot review; all three pieces remain distinct and use a coherent physical stone/cardboard scale.
- Gate: waiting for A/B/C kit confirmation before adding the next destruction layer with a different material or animation role.

## 2026-07-22 — Watchtower crossbow arm shard D candidate

- Locked the approved A/B/C shared stone destruction kit.
- Advanced to a different material and owner-specific role: `watchtower__debris__crossbow_arm_shard_d_v1`.
- Generated exactly one connected wooden crossbow-limb fragment with an integrated metal binding and one splintered broken end using built-in ImageGen.
- Candidate passes strict top-down projection, flat cardboard construction, wood/stone differentiation, isolation, no-complete-weapon, no-detached-splinter, and no-clipping checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/watchtower__debris__crossbow_arm_shard_d_v1_chroma.png` (`1254 × 1254 px`, approximately `1.2 MB`).
- Gate: waiting for visual confirmation before alpha extraction, crossbow-relative scaling, pivot preparation, and weapon/debris comparison.

## 2026-07-22 — Watchtower crossbow arm shard D prepared

- Extracted and promoted the approved wooden arm fragment to the canonical Watchtower module package.
- Tight rect: `845 × 314 px`; alpha-weighted center-of-mass pivot: `[424, 167]`; visible magenta spill: `0`.
- Scaled the fragment to `0.36` of the canonical crossbow length, producing a `280 × 104 px` runtime layer against the `779 × 530 px` weapon.
- Alpha PNG is `516,556` bytes and passes the `5 MB` limit.
- Added owner-rotation inheritance, light-wood destruction physics, and draw order `64` to the manifest.
- Built a separate crossbow/debris scale-and-pivot review; the fragment reads as one broken limb segment rather than a second complete weapon.
- Gate: waiting for weapon-relative scale confirmation before adding a smaller hardware/effect destruction layer.

## 2026-07-22 — Watchtower crossbow axle bracket E candidate

- Locked the approved weapon-relative scale of wooden arm shard D.
- Generated `watchtower__debris__crossbow_axle_bracket_e_v1` as a separate small metal destruction layer using built-in ImageGen.
- Candidate is exactly one connected broken C-shaped axle collar with an open inner cutout, two integrated rivets, and one fractured side.
- Visual QA passes strict top-down projection, flat cardboard construction, open-hole readability, metal/wood/stone differentiation, isolation, and no-clipping checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/watchtower__debris__crossbow_axle_bracket_e_v1_chroma.png` (`1254 × 1254 px`, approximately `1.2 MB`).
- Gate: waiting for visual confirmation before alpha extraction, hole validation, axle-relative scaling, pivot preparation, and hardware comparison.

## 2026-07-22 — Watchtower crossbow axle bracket E prepared

- Extracted and promoted the approved metal axle fragment to the canonical Watchtower module package.
- Tight rect: `495 × 606 px`; alpha-weighted material pivot: `[231, 302]`; visible magenta spill: `0`.
- Verified the open center after alpha conversion (`center alpha: 0`) and excluded it from the center-of-mass calculation.
- Scaled the bracket to `0.14` of the canonical crossbow length, producing a `109 × 133 px` runtime layer against the `779 × 530 px` weapon.
- Alpha PNG is `556,461` bytes and passes the `5 MB` limit.
- Added owner-rotation inheritance, fast-spinning light-metal destruction physics, and draw order `65`.
- Built a separate crossbow/hardware scale-and-pivot review; the bracket remains readable at axle scale and clearly subordinate to the weapon.
- Gate: waiting for axle-relative scale confirmation before generating a short-lived destruction effect layer.

## 2026-07-22 — Watchtower stone dust burst source sheet

- Locked the approved axle-relative scale of metal bracket E.
- Generated the complete four-frame `watchtower__destroy_fx__stone_dust_burst_v1` sequence in one built-in ImageGen request.
- Source sheet contains exactly four isolated 2×2 animation groups: compact dust rosette, widening broken ring, thinner expanded ring, and faint dispersed wisps.
- Visual QA passes stable center, readable one-shot progression, flat paper/cardboard construction, true top-down presentation, slot isolation, no-realistic-smoke, and no-clipping checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/watchtower__destroy_fx__stone_dust_burst_v1_source_chroma.png` (`1254 × 1254 px`, approximately `1.2 MB`).
- Gate: waiting for visual confirmation before alpha extraction, four-frame normalization, timing manifest, and assembled destruction preview.

## 2026-07-22 — Watchtower stone dust burst normalized

- Split the approved 2×2 source sheet into four alpha frames while preserving each quadrant's generated effect center.
- Normalized all frames to a shared `627 × 627 px` canvas and pivot `[313, 313]`.
- Added a non-looping `490 ms` manifest sequence with timing `85 / 105 / 125 / 175 ms`, scale `0.76` of the base footprint, and draw order `70`.
- Runtime frames total `1,316,958` bytes and contain zero visible magenta spill.
- Created a separate labeled QA grid; runtime files contain no labels, grid, or pivot markers.
- Built an assembled destruction GIF combining the intact Watchtower, dust sequence, stone debris A/B/C, wooden shard D, and metal bracket E as independent layers.
- Gate: waiting for assembled destruction confirmation before deciding whether a separate spark one-shot is necessary and before final family atlas packing.

## 2026-07-22 — Watchtower metal spark burst source sheet

- Confirmed that the destruction package benefits from a separate short metal-impact accent for axle bracket E.
- Generated the complete four-frame `watchtower__destroy_fx__metal_spark_burst_v1` sequence in one built-in ImageGen request.
- Source sheet contains exactly four isolated 2×2 groups with a stable empty center: compact rays, long expanded rays, shorter amber fragments with flecks, and distant fading remnants.
- Visual QA passes outward progression, paper/cardboard construction, no-glow treatment, slot isolation, true top-down presentation, and no-clipping checks.
- Saved at `assets/staging/candidates/modules/fortress_ranged/watchtower__destroy_fx__metal_spark_burst_v1_source_chroma.png` (`1254 × 1254 px`, approximately `1.0 MB`).
- Gate: waiting for visual confirmation before alpha extraction, shared-center normalization, timing manifest, QA grid, and final assembled destruction preview.

## 2026-07-22 — Watchtower metal spark burst normalized

- Split the approved spark source sheet into four alpha frames on a shared `627 × 627 px` canvas and center pivot `[313, 313]`.
- Added a fast non-looping manifest sequence with timing `55 / 65 / 75 / 95 ms`, total duration `290 ms`, scale `0.34` of crossbow length, and draw order `71`.
- Runtime frames total `1,086,692` bytes and contain zero visible magenta spill.
- Created a separate labeled QA grid; runtime frames contain no labels, grid, pivot markers, or glow bloom.
- Built the final destruction GIF by compositing sparks above the existing independent dust and debris layers.
- Gate: waiting for final destroy-preview confirmation before freezing the Watchtower animation inventory and packing the compact runtime atlas.

## 2026-07-22 — Watchtower layered runtime atlas v2 packed

- Froze the approved Watchtower inventory at 31 independently addressable runtime sprites.
- Downscaled from canonical alpha sources using a locked `512 px` base footprint and existing manifest scale relationships.
- Trimmed every runtime sprite and retained source sizes, trim offsets, pivots, attachments, draw order, animation timing, and destruction physics in the source-of-truth manifest.
- Packed all sprites into one transparent `1024 × 1024 px` Watchtower-family atlas with `4 px` separation.
- Runtime atlas is `979,759` bytes and passes the `5 MB` limit.
- Final audit passes JSON parsing, 31/31 rects in bounds, zero rect overlap, RGBA transparency, and zero visible magenta spill.
- Runtime atlas contains no labels, grid, pivot crosses, or assembled previews.
- Created a separate 31-cell labeled review grid and a separate static composite preview.
- Status: `approved candidate`; waiting for user confirmation before wiring the atlas/manifest into the Watchtower animation site and running browser QA.

## 2026-07-22 — Watchtower Atlas Lab v2 integrated and browser-tested

- Replaced the superseded `layered-runtime-v3` Watchtower Lab renderer with a direct consumer of `assets/approved/runtime/watchtower/watchtower_layered_runtime_v2.png` and its schema-v2 manifest.
- Site now assembles all object states from atlas rects, pivots, trim/source-space metadata, normalized attachments, and runtime transforms; no baked composite frames are loaded.
- Added five interactive states: idle, aim, attack, projectile, and destroy.
- Aim rotates only the crossbow; muzzle/projectile inherit its attachment and angle; flag and lantern animate independently; destruction uses five solid debris layers plus dust and sparks.
- Added deterministic `advanceTime(ms)` and concise `render_game_to_text()` state for automated QA.
- Updated the lab interface around a dominant 720px canvas, restrained technical controls, runtime metadata, pointer aiming, pause, reset, and fullscreen shortcuts.
- Playwright client scenarios passed for idle, aim, early/late attack, projectile visibility, early/mid/late destruction, and state reporting.
- Visually inspected every generated QA capture; no clipping or attachment failures found and no console-error artifacts were emitted.
- Local site is running at `http://127.0.0.1:4174/watchtower-lab/`.
- Gate: waiting for user in-browser confirmation before locking Watchtower as the baseline and starting the next object.

## 2026-07-22 — Watchtower baseline locked; Ranger generation started

- User approved continuing after the Watchtower Atlas Lab browser gate, so Watchtower is now the locked Layered Object Pipeline v2 baseline.
- Advanced to Ranger, the next object in the approved family-first production order.
- Ranger inherits the `fortress_ranged` base, center socket, lantern/glow, and shared stone debris kit.
- Ranger-specific contract remains: rapid crossbow, separate bolt magazine, separate arrow rack, separate hunting optics, separate ranger trim, and ranger bolt.
- Began with `ranger__active_primary__rapid_crossbow_v1`, explicitly excluding magazine, optics, arrows, rack, trim, base, and lantern from the primary module.
- Both the full built-in ImageGen request and the required simplified retry failed with backend network errors before producing an image.
- No Ranger candidate or partial asset was saved, and no fallback model/API was used.
- Gate: retry the same built-in ImageGen rapid-crossbow request when the backend is available; all later Ranger modules remain blocked behind its visual approval.

## 2026-07-22 — Ranger rapid crossbow visual candidate

- Retried the blocked built-in ImageGen step and successfully generated `ranger__active_primary__rapid_crossbow_v1`.
- Candidate is one connected, strict-top-down cardboard rapid crossbow with central axle hub and +X twin launch rail.
- Magazine, optics, bolts/projectile, arrow rack, Ranger trim, base, lantern, flag, and effects remain excluded for independent child layers.
- Visual QA passes projection, cardboard construction, isolation, attachment readability, Watchtower differentiation, and no-clipping checks.
- Saved at `assets/staging/candidates/modules/ranger/ranger__active_primary__rapid_crossbow_v1_chroma.png` (`1254 × 1254 px`, approximately `1.4 MB`).
- Gate: waiting for visual confirmation before alpha extraction, axle/muzzle derivation, inherited-base rotation review, and canon promotion.

## 2026-07-22 — Watchtower animation HTML revalidated before Ranger continuation

- Kept the Watchtower Atlas Lab as a direct runtime consumer of the approved schema-v2 manifest and compact atlas; no baked composite animation frames were introduced.
- Restarted the local project server at `http://127.0.0.1:4174/watchtower-lab/` and exercised `idle`, `aim`, `attack`, `projectile`, and `destroy` through the required browser-game QA client.
- Captured and visually inspected a control frame for every state under `output/watchtower-animation-qa/`.
- Confirmed stable base footprint, independent crossbow rotation, inherited muzzle/projectile alignment, independent flag and lantern animation, and layered destruction debris/effects.
- Browser QA completed without console errors; the interactive page is open for user review.
- Gate: pause Ranger production until the user has reviewed the Watchtower animations.

## 2026-07-22 — Ranger rapid crossbow promoted; bolt magazine visual candidate

- Converted the approved rapid crossbow to transparent alpha and cropped it to a `931 × 844 px` tight rect.
- Locked the center axle pivot at `[462, 431] px` and local `+X` muzzle attachment at `[930, 431] px`.
- Added its canon module manifest under `assets/approved/canon/modules/ranger/`, including magazine, optics, parent, and muzzle attachment contracts.
- Validated the weapon at `0 / 90 / 180 / 270` degrees on the inherited fortress base/socket/lantern core.
- Rotation envelope is `362 px` inside the inherited `541 px` base radius; no clipping and zero visible magenta spill.
- Promoted `ranger__active_primary__rapid_crossbow_v1` to canon.
- Generated `ranger__ammo_child__bolt_magazine_v1` as one separate strict-top-down cardboard cassette with a central mounting aperture and no visible ammunition or parent layers.
- Saved the visual candidate at `assets/staging/candidates/modules/ranger/ranger__ammo_child__bolt_magazine_v1_chroma.png` (`1254 × 1254 px`).
- Gate: wait for bolt-magazine visual confirmation before alpha extraction, scale/drawOrder validation, and crossbow composite.

## 2026-07-22 — Ranger bolt magazine promoted; empty arrow rack candidate

- Extracted the magazine to a `1059 × 466 px` tight alpha rect with zero visible magenta spill and preserved its transparent center opening.
- The first center-underlay assembly made the magazine unreadable; technical QA caught this before canon promotion.
- Moved the weapon magazine socket to local `x=0.66`, rotated the cassette `90°`, reduced it to `0.18` of weapon width, and assigned draw order `31` above the rail.
- Four-angle assembly QA now keeps the magazine readable without obscuring the weapon pivot, limbs, string, or muzzle.
- Promoted `ranger__ammo_child__bolt_magazine_v1` to canon.
- Generated `ranger__utility_child__arrow_rack_v1` as one empty strict-top-down crescent-shaped cardboard rack with five slots and no baked ammunition.
- Saved at `assets/staging/candidates/modules/ranger/ranger__utility_child__arrow_rack_v1_chroma.png` (`1254 × 1254 px`).
- Gate: wait for arrow-rack visual confirmation before alpha extraction and platform-clearance validation.

## 2026-07-22 — Ranger arrow rack promoted; hunting optics candidate

- Extracted the empty arrow rack to a `948 × 409 px` tight alpha rect with zero visible magenta spill.
- Initial rack position `[0.5, 0.205]` failed clearance with overlap counts `863 / 5246 / 110 / 4676 px`; canon status was blocked.
- Moved the rack to the northern inner rim at `[0.5, 0.12]` and reduced it to `0.19` of the inherited base footprint.
- Repeated the four-angle audit and achieved `0 / 0 / 0 / 0 px` overlap with the rotating crossbow-plus-magazine group.
- Promoted `ranger__utility_child__arrow_rack_v1` to canon as a static draw-order-15 child.
- Generated `ranger__aim_child__hunting_optics_v1` as one separate strict-top-down cardboard sight with a printed amber lens, mounting clamps, and adjustment wheel.
- Saved at `assets/staging/candidates/modules/ranger/ranger__aim_child__hunting_optics_v1_chroma.png` (`1254 × 1254 px`).
- Gate: wait for hunting-optics visual confirmation before alpha extraction and weapon assembly validation.

## 2026-07-22 — Ranger hunting optics promoted; identity trim candidate

- Extracted hunting optics to a `918 × 393 px` tight alpha rect with zero visible magenta spill.
- Attached the sight to `rapid_crossbow.optics_socket` at `0.27` of parent weapon width and draw order `32`.
- Four-angle assembled QA passes with optics, magazine, and weapon rotating as one group while remaining independently addressable layers.
- Promoted `ranger__aim_child__hunting_optics_v1` to canon.
- Generated `ranger__identity_child__ranger_trim_v1` as one connected strict-top-down cardboard platform medallion with a compass-arrow and leaf motif.
- Saved at `assets/staging/candidates/modules/ranger/ranger__identity_child__ranger_trim_v1_chroma.png` (`1254 × 1254 px`).
- Gate: wait for Ranger trim visual confirmation before alpha extraction and full-platform clearance validation.

## 2026-07-22 — Ranger identity trim promoted; barbed bolt candidate

- Extracted Ranger trim to a `708 × 857 px` tight alpha rect with zero visible magenta spill.
- Mounted it as a static draw-order-16 child at south-east rim position `[0.79, 0.79]`, opposite the inherited lower-left lantern and separate from the northern rack.
- Full crossbow, magazine, and optics rotation audit passes with `0 / 0 / 0 / 0 px` trim overlap.
- Promoted `ranger__identity_child__ranger_trim_v1` to canon.
- Generated `ranger__projectile__barbed_bolt_v1` as one strict-top-down `+X` cardboard projectile with green fletching and a barbed iron tip.
- Trail, muzzle flash, impact, glow, debris, weapon, and extra ammunition remain excluded as independent layers.
- Saved at `assets/staging/candidates/modules/ranger/ranger__projectile__barbed_bolt_v1_chroma.png` (`1254 × 1254 px`).
- Gate: wait for barbed-bolt visual confirmation before alpha extraction and muzzle/trajectory validation.

## 2026-07-22 — Ranger barbed bolt promoted; core unique module inventory complete

- Extracted the Ranger bolt to a `1075 × 223 px` tight alpha rect with zero visible magenta spill.
- Locked trajectory pivot `[537, 111]`, tail spawn `[0, 111]`, tip impact `[1074, 111]`, and local `+X` forward axis.
- Scaled the projectile to `0.23` of parent weapon length and aligned its tail exactly to `rapid_crossbow.muzzle_anchor`.
- Muzzle-spawn composite and `0 / 45 / 90 / 180°` trajectory grid pass orientation and attachment checks.
- Promoted `ranger__projectile__barbed_bolt_v1` to canon.
- Ranger now has canon unique modules for rapid crossbow, bolt magazine, arrow rack, hunting optics, identity trim, and barbed bolt, plus inherited fortress base/socket/lantern/shared stone debris.
- Next gate: document Ranger animation inventory, separate reusable fortress effects from Ranger-specific effects, then generate only the missing owner-specific layers before atlas packing.

## 2026-07-22 — Ranger animation inventory locked

- Documented Ranger's complete runtime layer and animation contract in `docs/05_assets/ranger-animation-inventory-v1.md`.
- Reuse is limited to the inherited fortress base, socket, lantern loop, stone debris, dust, and metal spark destruction accent.
- Aim rotates the crossbow, magazine, and optics as one hierarchy while retaining independently addressable sprites.
- Destroy reuses existing Ranger children themselves as detachable debris rather than duplicating magazine, optics, rack, or trim artwork.
- Identified exactly two missing owner-specific effects before atlas packing: four-frame rapid muzzle flash and four-frame barbed-bolt impact.
- Gate: generate and validate `ranger__muzzle_fx__rapid_flash_loop_v1` next; impact remains blocked behind it.

## 2026-07-22 — Ranger rapid muzzle flash visual candidate

- Generated `ranger__muzzle_fx__rapid_flash_loop_v1` as one unlabeled built-in ImageGen `2 × 2` source sheet.
- Sheet contains exactly four isolated groups in reading order: ignition star, narrow spear flash, wider split flare with green flecks, and fading fragments.
- Dominant firing frames face local `+X`; weapon, projectile, smoke, realistic flame, glow bloom, labels, grid, and pivot marks remain excluded.
- Visual QA passes quadrant isolation, paper/cardboard construction, chronological progression, generous chroma margins, and no clipping.
- Saved at `assets/staging/candidates/modules/ranger/ranger__muzzle_fx__rapid_flash_loop_v1_source_chroma.png` (`1254 × 1254 px`).
- Gate: wait for visual confirmation before alpha splitting, shared-pivot normalization, attack timing, and muzzle composite.

## 2026-07-22 — Ranger rapid muzzle flash promoted

- Split the approved `2 × 2` sheet by fixed quadrants so disconnected paper flecks remain part of their intended frames.
- Normalized four runtime frames to a shared `477 × 272 px` canvas and attachment pivot `[78, 136]`.
- Locked non-looping rapid timings `45 / 55 / 65 / 85 ms`, total `250 ms`, scale `0.17` of weapon length, and draw order `50`.
- Initial audit found magenta fringe; strengthened the effect-specific despill pass and repeated extraction.
- Final runtime spill is `0 / 0 / 0 / 0 px`; four frames total `202,595` bytes.
- Review grid and assembled attack GIF pass visual attachment and progression checks.
- Promoted `ranger__muzzle_fx__rapid_flash_loop_v1` to canon.
- Gate: generate the final missing Ranger-owned effect, `ranger__impact_fx__barbed_hit_v1`.

## 2026-07-22 — Ranger barbed impact generation blocked by ImageGen network

- Started the final missing Ranger-owned effect as an unlabeled four-frame `2 × 2` source sheet with a stable empty impact center.
- The full built-in ImageGen request failed with a backend network error before producing any image.
- Retried once through the same built-in ImageGen path with a shorter prompt; the retry also failed with a backend network error after extended processing.
- No impact candidate, partial source, or placeholder was saved, and no CLI/API/model fallback was used.
- Existing rapid muzzle flash remains canon and validated; Ranger atlas packing remains blocked only by `ranger__impact_fx__barbed_hit_v1`.
- Gate: retry built-in ImageGen when the backend is available, or use the CLI fallback only after explicit user approval and local `OPENAI_API_KEY` configuration.

## 2026-07-22 — Ranger barbed impact visual candidate generated

- Retried `ranger__impact_fx__barbed_hit_v1` through the built-in ImageGen path after the earlier network failures.
- Successful source contains exactly four isolated `2 × 2` groups: compact contact burst, wider angular burst, expanded broken shard ring, and sparse fade.
- Every group preserves a stable empty center; bolt, weapon, target, blood, smoke, fire, glow, realistic explosion, labels, grid, and pivot marks remain excluded.
- Visual QA passes quadrant isolation, chronological outward progression, paper/cardboard material, generous chroma margins, and no clipping.
- Saved at `assets/staging/candidates/modules/ranger/ranger__impact_fx__barbed_hit_v1_source_chroma.png` (`1254 × 1254 px`).
- Gate: wait for visual confirmation before alpha splitting, shared-center normalization, timing, and contact preview.

## 2026-07-22 — Ranger barbed impact promoted; atlas inventory complete

- Split the approved impact sheet by fixed quadrants and preserved each quadrant center as the common contact pivot `[313, 313]` on `627 × 627 px` canvases.
- Removed chroma and magenta fringe; final spill is `0 / 0 / 0 / 0 px`.
- Locked non-looping timings `55 / 70 / 90 / 120 ms`, total `335 ms`, scale `0.72` of projectile length, and draw order `55`.
- Four runtime frames total `1,216,374` bytes and remain below the per-family size threshold before compact atlas downscaling.
- Separate review grid and bolt-tip contact GIF pass visual progression and attachment checks.
- Promoted `ranger__impact_fx__barbed_hit_v1` to canon.
- Ranger animation inventory is now complete; no missing owner-specific layers remain.
- Gate: pack one compact transparent Ranger runtime atlas, create the schema-v2 source-of-truth manifest, separate review grid, composite preview, and technical audit.

## 2026-07-22 — Ranger layered runtime v2 packed and validated

- Packed all 32 inherited and Ranger-owned layers into one transparent `1024 × 1024 px` family atlas.
- Runtime atlas is `992,457 bytes`, safely below the `5 MB` limit.
- Created the schema-v2 manifest with tight rects, pivots, source sizes, trim offsets, draw order, nine attachments, runtime transforms, and five animation clips.
- Reused the approved fortress base, socket, lantern loop, stone debris, dust, and sparks; kept every Ranger-specific module independently addressable.
- Removed 582 residual chroma-edge pixels during runtime packing; final magenta spill is `0 px`.
- Automated audit passes: all rects in bounds, zero rect overlaps, no runtime labels, stable `512 px` base footprint.
- Created a separate 32-layer human QA grid and assembled true-top-down composite preview.
- Review record: `docs/05_assets/reviews/ranger-layered-runtime-v2-final.md`.
- Gate: wait for human visual confirmation of Ranger before updating the animation lab or starting the next object.

## 2026-07-22 — Ranger approved and integrated into the Layered Object Lab

- User approval received through the continuation gate; Ranger runtime status is locked as approved.
- Extended `watchtower-lab/` into a two-object manifest-driven lab with Watchtower and Ranger selectors.
- Ranger actions exposed from atlas rects and attachments: idle, aim, attack, projectile, impact, and destroy.
- Browser-game QA passed for all six Ranger states with `32` manifest sprites and no baked composite frames.
- Verified magazine and optics inherit weapon rotation while rack, trim, and lantern remain base children.
- Verified Ranger destruction detaches existing child layers rather than introducing duplicate baked debris art.
- Tracker is next in the documented family-first order.
- Added `docs/05_assets/tracker-module-contract-v1.md`; first gated asset is the standalone long-range crossbow projection master.

## 2026-07-22 — Tracker long-range crossbow visual candidate

- Generated the first Tracker-owned module through built-in ImageGen using the approved Ranger rapid crossbow only as a family/material reference.
- Replaced the compact rapid-fire silhouette with a longer precision rail and long narrow limbs while retaining the exact top-down cardboard construction and centered bearing.
- Initial output had insufficient horizontal safety margin and was not selected for production.
- Performed one targeted framing edit without changing the weapon design.
- Selected candidate is `1521 × 1034 px` with safe margins `261 / 158 / 194 / 165 px` and no clipping.
- Review: `docs/05_assets/reviews/tracker-long-range-crossbow-v1.md`.
- Gate: wait for visual confirmation before chroma-to-alpha extraction, pivot registration, scaling against the inherited base, and scan-ring generation.

## 2026-07-22 — Tracker crossbow promoted; scan optics ring candidate

- Continuation approval accepted for the Tracker long-range crossbow.
- Extracted a tight `1064 × 709 px` alpha layer with zero visible magenta spill.
- Locked authored bearing pivot `[498, 358]`, muzzle `[1063, 358]`, local `+X` axis, and runtime scale `0.78` of the inherited fortress footprint.
- Four-angle rotation audit passes: `449 px` envelope remains inside the `541 px` base radius.
- Promoted `tracker__active_primary__long_range_crossbow_v1` to canon with manifest, inherited-core composite and review grid.
- Generated `tracker__aim_child__scan_optics_ring_v1` as a separate connected overhead cardboard annulus with an open chroma center.
- Ring source has safe margins `404 / 157 / 413 / 174 px`, no clipping, and a verified chroma center hole.
- First built-in ring generation failed due to a backend network error; one built-in retry succeeded. No fallback path was used.
- Gate: wait for scan-ring visual confirmation before alpha extraction, concentric pivot registration, overlay/rotation QA, and crown-trim generation.

## 2026-07-22 — Tracker scan ring promoted; pivot corrected; crown trim candidate

- Continuation approval accepted for the Tracker scan ring.
- Initial weapon overlay exposed an authored-pivot error: the framing edit centered the full silhouette, not the mechanical bearing.
- Corrected the crossbow pivot from `[498, 358]` to the visible bearing at `[352, 358]` and reduced runtime scale from `0.78` to `0.74`.
- Rebuilt the crossbow canon manifest and QA: corrected `536 px` rotation envelope remains inside the `541 px` base radius.
- Extracted scan ring to tight `702 × 701 px` alpha with pivot `[351, 350]`, center alpha `0`, and magenta spill `0`.
- Independent local rotation review at `0 / 22.5 / 45 / 67.5°` now remains concentric with the corrected bearing.
- Promoted `tracker__aim_child__scan_optics_ring_v1` to canon with continuous `42°/s` scan rotation.
- Generated `tracker__identity_child__crown_trim_v1` as a separate flat crown-and-compass cardboard medallion.
- Crown source has safe margins `229 / 253 / 229 / 301 px`, no clipping, and no baked parent or targeting effect.
- Gate: wait for crown-trim visual confirmation before alpha extraction, static base placement, full rotation-clearance QA, and targeting-rune generation.

## 2026-07-22 — Tracker crown trim promoted; targeting rune blocked by ImageGen network

- Continuation approval accepted for the Tracker crown trim.
- Extracted a tight `792 × 698 px` alpha layer with pivot `[396, 349]`, zero visible magenta spill, and runtime size `114 × 100 px`.
- Corrected review placement to use `center + (normalized - 0.5) × footprint`; the earlier canvas-normalized preview incorrectly placed the trim outside the rim and was rejected.
- Final static position `[0.79, 0.79]` sits inside the inherited base footprint.
- Full rotating group (long-range crossbow, inherited magazine, scan ring) has `0 / 0 / 0 / 0 px` crown overlap at `0 / 90 / 180 / 270°`.
- Promoted `tracker__identity_child__crown_trim_v1` to canon.
- Started the final Tracker-owned targeting-rune four-frame source through built-in ImageGen.
- Reference-edit generation failed twice at the backend network layer; a third built-in generation without an image reference also failed at the generation endpoint.
- No rune source, placeholder, programmatic substitute, CLI output, or partial artifact was saved.
- Gate: retry built-in ImageGen when its backend is available. CLI `gpt-image-1.5` fallback remains disallowed without explicit user confirmation and local `OPENAI_API_KEY` configuration.

## 2026-07-22 — Tracker targeting rune built-in retry still blocked

- Retried the missing four-frame targeting-rune source through a fresh built-in ImageGen generation without image references.
- The generation endpoint again failed at the backend network layer after extended processing and returned no image.
- No source file, partial frame, placeholder, or synthetic substitute was created.
- Tracker canon remains intact through crossbow, scan ring, inherited magazine/projectile, and crown trim.
- Further progress requires either a later successful built-in retry or explicit user authorization for the CLI transparency fallback with a locally configured `OPENAI_API_KEY`.

## 2026-07-22 — Tracker targeting rune generated and normalized

- A later built-in ImageGen retry succeeded; no CLI fallback was used.
- Generated exactly four isolated targeting-rune states on one unlabeled `2 × 2` chroma source sheet.
- ImageGen swapped the two lower states relative to requested reading order; runtime order was explicitly remapped to `TL → TR → BR(lock) → BL(fade)`.
- Split the source into four independently addressable tight alpha frames with shared `627 × 627 px` source footprint and pivot `[313, 313]`.
- Locked timings `180 / 180 / 240 / 220 ms`, total `820 ms`, looping.
- Final magenta spill is `0 / 0 / 0 / 0 px`.
- Initial assembled preview placed the paper rune above and visually obscured the metal scan ring; corrected draw order to weapon `30`, rune `31`, scan ring `32`.
- Final weapon preview keeps the animated rune and independently rotating metal ring simultaneously readable.
- Tracker unique inventory is complete: long-range crossbow, inherited Ranger magazine/bolt, scan optics ring, crown trim, and targeting rune loop.
- Gate: wait for rune-loop visual confirmation before packing the compact Tracker runtime atlas and schema-v2 manifest.

## 2026-07-22 — Tracker layered runtime v2 packed and validated

- Continuation approval accepted for the targeting-rune loop and complete Tracker inventory.
- Packed `35` inherited and Tracker-owned sprites into one transparent `1024 × 1024 px` Tracker-family atlas.
- Runtime atlas is `1,033,305 bytes`, safely below the `5 MB` limit.
- Created the schema-v2 source-of-truth manifest with tight rects, pivots, source sizes, trim offsets, draw order, eight attachments, runtime transforms and six animation clips.
- Preserved the corrected long-range-crossbow bearing pivot and distinct transforms for weapon aim, magazine inheritance, targeting-rune animation and independent scan-ring rotation.
- Runtime layer order keeps weapon `30`, targeting rune `31`, scan ring `32`, and magazine `33` independently readable.
- Automated audit passes: all rects in bounds, zero rect overlaps, zero magenta spill, no runtime labels, stable `512 px` base footprint.
- Created a separate 35-layer QA grid and assembled true-top-down composite preview.
- Review record: `docs/05_assets/reviews/tracker-layered-runtime-v2-final.md`.
- Gate: wait for human confirmation before setting Tracker to approved, integrating it into the animation lab, or starting Assassin.

## 2026-07-22 — Tracker approved and integrated into the Layered Object Lab

- User continuation confirmed the Tracker final candidate; manifest and reproducible packer now emit `approved` status.
- Added Tracker as object `03` in `watchtower-lab/` with idle, aim, targeting, attack, projectile, impact and destroy controls.
- Browser-game QA passed all seven states with `35` runtime sprites and no baked composite frames.
- Verified targeting rune below independently rotating metal scan ring, inherited magazine transform, projectile flight, impact and child-layer destruction.
- Browser QA record: `docs/05_assets/reviews/tracker-lab-v2-browser-qa.md`.
- Tracker is closed; Assassin is next in the documented Ranger-derived order.
- Added `docs/05_assets/assassin-module-contract-v1.md`; first gated module is the standalone sniper crossbow.

## 2026-07-22 — Assassin sniper crossbow visual candidate

- Started Assassin only after Tracker runtime and browser gates passed.
- Built-in reference-edit generation failed at the backend network layer; one built-in text-only retry succeeded without CLI fallback.
- Generated one isolated Assassin sniper crossbow in exact overhead projection with local `+X` muzzle, centered bearing, long enclosed rail, swept limbs and dark violet/amber cardboard treatment.
- Source is `1254 × 1254 px` with safe margins `83 / 197 / 78 / 199 px` and no clipping.
- Base, critical lens, charge, projectile, shrouded rim insert, release FX and all review markings remain excluded.
- Review: `docs/05_assets/reviews/assassin-sniper-crossbow-v1.md`.
- Gate: wait for visual confirmation before alpha extraction, authored-bearing pivot registration, inherited-base rotation QA and shrouded-rim generation.

## 2026-07-22 — Full tower visual branch rejected; description-driven v3 restart

- User rejected the Watchtower/Ranger/Tracker/Assassin branch because repeated crossbow-platform reuse erased the distinct tower descriptions.
- Stopped Assassin immediately; its candidate and every generated image package from the rejected fortress-ranged branch are no longer canon.
- Moved the rejected Watchtower/Ranger/Tracker/Assassin generated assets into the recoverable archive `assets/_archive/crossbow-family-reset-2026-07-22/`.
- Battlefield background and unrelated project images were explicitly preserved.
- Confirmed from `asset-prompt-bible.md` that Watchtower itself is crossbow-based, while later families use heavy ballistae, harpoons, repeater fans, cannons, mortars, multi-barrel grapeshot, magic crystals/lenses, living wood, and economy mechanisms.
- The failure was structural: Ranger must read as a manned firing platform, Tracker as a royal spotter spire, Assassin as a shrouded perch, rather than sharing one near-identical token body.
- Added the new source-of-truth matrix and reuse rules in `docs/05_assets/restart-description-driven-object-pipeline-v3.md`.
- Gate: generate a fresh assembled Watchtower / Warden's Post projection master from the original description only. Do not reuse any archived visual.

## 2026-07-22 — Watchtower v3 master generation blocked by ImageGen network

- Reset `watchtower-lab/` to a background-only restart screen so it no longer requests or displays archived runtime atlases.
- Started a fresh Watchtower assembled projection master with no archived image references.
- New contract emphasizes Warden's Post architecture: distinctive stone parapet, wood working deck, access/hardware detail, small central simple crossbow, separate flag and lantern stations.
- The first built-in generation and one shorter built-in retry both failed at the generation backend network layer before returning an image.
- No old asset was restored, no placeholder was created, and no CLI/API fallback was used.
- Gate remains the same: obtain and visually approve the fresh Watchtower projection master before generating any individual layer.

## 2026-07-22 — Fresh Watchtower v3 Warden's Post master generated

- A new built-in ImageGen request succeeded without any archived image reference.
- Generated a description-driven assembled Watchtower master dominated by the Warden's Post architecture: varied stone parapet, wood working deck, access notches, hatches, rope equipment, flag station and top-view lantern station.
- Kept exactly one small simple crossbow on the center bearing, as required by the original Watchtower description; it no longer defines the complete platform silhouette.
- Saved the `1254 × 1254 px` chroma source under `assets/source/watchtower-v3/`.
- Removed chroma locally to a separate alpha review: all four corners alpha `0`, visible magenta spill `0 px`, no clipping.
- Safe source margins are `82 / 88 / 82 / 102 px`.
- The visible loaded bolt is explicitly marked for separation during layer production; it must not remain baked into the final weapon layer.
- Review: `docs/05_assets/reviews/watchtower-v3-wardens-post-projection-master.md`.
- Gate: wait for human approval of the new master before generating base/body, socket, crossbow, flag, lantern and animation child layers.

## 2026-07-22 — Watchtower v3 master rejected for excessive realism

- User rejected the fresh Warden's Post master because realistic stone, wood, metal and rope rendering overpowered the cardboard tabletop style.
- Marked the master review as rejected; it must not be decomposed or used as a visual-style reference.
- Locked the correction: chunky die-cut silhouettes, broad flat printed colors, coarse halftone, imperfect ink registration, thick illustrated outlines, obvious tan corrugated edges, and at least 70–80% less micro-detail/material realism.
- Attempted one built-in reference edit and two fresh built-in generations with the corrected punchboard specification.
- All three requests failed at ImageGen backend network endpoints before producing an image.
- No replacement candidate, placeholder or CLI fallback was created.
- Gate: retry a fresh non-realistic cardboard Watchtower master when built-in ImageGen is available.

## 2026-07-22 — Watchtower v4 cardboard master ready for visual gate

- A fresh built-in ImageGen generation succeeded without using the rejected realistic master as a visual reference.
- The new candidate uses an unmistakable punchboard language: chunky die-cut silhouette, thick black ink outlines, coarse halftone, restricted printed palette and a visible tan cardboard edge.
- Preserved the original Watchtower / Warden's Post identity: stone parapet, radial timber deck, two access breaks, one small simple central crossbow, red flag and amber lantern.
- Saved both chroma source and locally cleaned alpha review under `assets/source/watchtower-v3/` with explicit object/version names.
- Alpha review is `1254 × 1254 px`, `2,466,505 bytes`, has fully transparent corners, safe margins `112 / 94 / 98 / 113 px`, and no clipping.
- Review: `docs/05_assets/reviews/watchtower-v4-cardboard-projection-master.md`.
- Gate: wait for explicit human approval before producing the separate base, socket, weapon, projectile, flag, lantern and FX cardboard layers.

## 2026-07-22 — Watchtower v4 rejected as over-simplified; supplied diorama reference adopted

- User rejected v4 because it reduced the object to an overly simple flat punchboard token.
- Adopted the supplied battlefield image as the explicit visual reference for v5: premium handcrafted paper diorama, many individually cut pieces, 2–4 stacked cardboard layers, visible fiber edges, muted printed textures and restrained contact shadows.
- Locked the balance for v5: richer construction and material depth than v4, but no return to photorealistic stone/wood/metal and no loss of the exact overhead projection.
- Attempted two built-in reference-guided generations; both failed at the ImageGen edit network endpoint before returning an image.
- No CLI fallback, substitute placeholder or reuse of rejected masters was performed.
- Gate: retry the same reference-guided v5 generation when the built-in endpoint is available; layers remain blocked until the assembled master passes human review.

# Watchtower / Ветровой дозор — Layer Contract v4

> **SUPERSEDED / DO NOT GENERATE (2026-07-26).** Crossbow-based identity is
> removed. A new Wind Route Table contract must be derived from
> `seven-circles-object-redesign-v1.md` and `asset-prompt-bible-v7.md`.

Status: **archival decomposition contract**  
Updated: 2026-07-24  
Runtime ID: `watchtower` (`fire` alias)  
Object family: `wind_ranged`

V4 replaces Watchtower lore and ownership from v3. The former projection is
technical history, not an approved geometry master. Pixel coordinates remain
unset until the new Seven-Circles projection master passes visual approval.

## 1. Required assembled identity

- compact low circular lookout, never a tall tower;
- twenty independent cold-grey stone-card parapet tiles;
- exactly two opposite access notches;
- eight radial dark timber-card deck sectors;
- balanced lightweight crossbow on a layered central bearing;
- four copper bearing-fastening arcs;
- burgundy signal cloth, small amber lantern;
- rack with four bolts and one empty fifth slot;
- faded sky-blue repair card with a broken three-bend wind path.

The crossbow is the strongest functional accent but remains smaller and lighter
than the Ballista family.

## 2. Coordinates and extraction

The approved alpha-clean projection master establishes immutable
`masterWidth × masterHeight`. Every structural edit retains its canvas, scale,
rotation and position.

1. Validate 1:1 compositing against the master.
2. Extract layers in master coordinates.
3. Compute tight alpha rectangles.
4. Record pivots/attachments in master and local rect coordinates.
5. Pack only tight rects into the runtime atlas.

No independently recentered child may be approximately scaled back into place.
Complex mechanisms use one coherent geometry master and matching state edits.

## 3. Draw-order ranges

| Range | Group |
|---|---|
| 0–9 | footprint and foundation |
| 10–29 | fixed deck |
| 30–59 | parapet |
| 60–79 | deck attachments |
| 80–109 | bearing |
| 110–149 | rotating crossbow |
| 150–179 | cloth, lantern and reserve |
| 180–219 | projectile and impact |
| 220–299 | destruction |

Contact shadows belong to upper children. Painted shading cannot invent a
height step absent from the layer hierarchy.

## 4. Stable structure

| Layer ID | Parent | Draw order |
|---|---|---:|
| `footprint_shadow_card` | `stable_base` | 0 |
| `foundation_ring_card` | `stable_base` | 5 |
| `deck_underlay_card` | `stable_base` | 10 |
| `deck_sector_01..08` | `deck_stack` | 12–19 |
| `parapet_support_ring` | `stable_base` | 30 |
| `parapet_stone_01..20` | `parapet_stack` | 32–51 |
| `access_notch_lip_a` | `parapet_stack` | 52 |
| `access_notch_lip_b` | `parapet_stack` | 53 |
| `repair_staple_01..02` | `parapet_stack` | 54–55 |
| `wind_repair_card` | `deck_stack` | 62 |

Forbidden: archive mark, inventory plate, Kitezh route, laboratory enamel,
pseudo-rune and faction logo.

## 5. Bearing

| Layer ID | Draw order |
|---|---:|
| `bearing_lower_washer` | 80 |
| `bearing_fastening_arc_01..04` | 82–85 |
| `bearing_upper_washer` | 88 |
| `bearing_socket` | 90 |
| `bearing_contact_shadow` | 91 |

The arcs are structural copper cards, not circuitry or a symbol.
`active_primary_pivot` is the rotation origin and parent origin of
`crossbow_group`.

## 6. Crossbow

All parts come from one coherent crossbow master. Tense and released states are
matching edits of that geometry.

| Layer ID | Draw order |
|---|---:|
| `crossbow_group_shadow` | 110 |
| `crossbow_body_lower` | 112 |
| `crossbow_body_upper` | 114 |
| `crossbow_rear_cap` | 116 |
| `crossbow_trigger_block` | 118 |
| `crossbow_left_arm_lower` | 120 |
| `crossbow_left_arm_upper` | 122 |
| `crossbow_right_arm_lower` | 124 |
| `crossbow_right_arm_upper` | 126 |
| `crossbow_fastener_01..04` | 128–131 |
| `crossbow_string_tense` | 134 |
| `crossbow_string_release_01..02` | 135–136 |
| `crossbow_recoil_overlay_01..03` | 138–140 |
| `loaded_bolt` | 142 |
| `projectile_bolt` | transient |

Anchors: `bolt_nock_anchor`, `bolt_muzzle_anchor`, `string_left_anchor`,
`string_right_anchor`, `trigger_anchor`.

## 7. Secondary children

Signal cloth:

- `signal_cloth_mount_lower`, `signal_cloth_mount_cap`;
- `signal_cloth_01..04`;
- pivot `signal_cloth_hinge`.

Lantern:

- `lantern_mount_pad`, `lantern_body_lower`, `lantern_copper_frame`;
- `lantern_window`, `lantern_flame_01..04`, `lantern_glow_01..04`.

Bolt reserve:

- `bolt_rack_lower`, `bolt_rack_upper`;
- `reserve_bolt_01..04`, `reserve_slot_empty`.

No inventory ticks. Flame and glow remain independent from the lantern body.

## 8. Animations

| Animation | Sequence |
|---|---|
| `idle` | fixed base; subtle cloth and lantern loops |
| `aim` | bearing/crossbow rotate; tense string and bolt visible |
| `fire` | hide loaded bolt → release 1–2 → spawn projectile → recoil 1–3 |
| `recover` | return recoil → tense string → restore loaded bolt |
| `hit` | no base scale/rotation; optional short code-driven tint/offset |
| `disabled` | stop weapon; reduce cloth/flame cadence |
| `destroy` | detach named construction pieces; dust follows |

The atlas stores child states, not preassembled object frames.

## 9. Owned effects and debris

- `projectile_bolt`;
- `impact_01..04`;
- `debris_stone_01..05`, `chip_stone_01..06`;
- `debris_deck_01..04`, `splinter_wood_01..06`;
- debris for body, left arm, right arm and trigger;
- debris for cloth, lantern stack and four reserve bolts;
- `destroy_dust_01..05`.

## 10. Manifest

Required:

- `schemaVersion`, `objectId`, `familyId`, `atlas`, `atlasSizeBytes`;
- layer `rect`, `sourceSize`, `pivot`, `masterPivot`, `parent`, `attachment`,
  `drawOrder`, `defaultVisible`;
- master/local anchors;
- animation duration, loop and visibility/transform tracks;
- stable collision/selection footprint;
- projectile spawn and impact ownership;
- runtime versus QA classification.

The loader cannot infer pivots from rect centers.

## 11. Deliverables

Production:

1. ImageGen 2 source sheets;
2. alpha-clean masters;
3. tight transparent layer PNGs;
4. compact transparent runtime atlas ≤ 5 MB;
5. manifest JSON.

Separate human QA:

6. labelled review grid;
7. assembled composite;
8. animation HTML/site using the real atlas and manifest;
9. validation report.

QA labels, grid, crosses and previews never enter the runtime atlas.

## 12. Gates

Visual:

- true top-down, low footprint, no facade;
- premium punchboard rather than realism or glossy 3D;
- twenty stones, two notches and eight deck sectors readable;
- balanced crossbow, separate complete child cutouts;
- sparse Seven-Circles accents, no legacy marks;
- no clipping across all extents.

Technical:

- sources composite 1:1;
- rects tight, in bounds and non-overlapping;
- pivots/attachments reproduce the approved composite;
- footprint fixed during idle/aim/fire;
- animation references resolve;
- projectile starts at `bolt_muzzle_anchor`;
- atlas contains no QA pixels and stays ≤ 5 MB;
- browser proof uses production atlas/manifest without fallback sprites.

Current state: **READY FOR IMAGEGEN PROJECTION MASTER**. Decomposition waits for
user approval; packing waits for composite validation.

Preproduction manifest:
`../../assets/staging/candidates/watchtower/watchtower_layered_manifest_template_v1.json`.

Validator: `../../scripts/validate_layered_atlas.py`.

Deterministic packer: `../../scripts/build_layered_atlas.py`. It consumes
approved full-master-canvas layer PNGs and explicit geometry; it never derives
pivots from sprite centers.

QA builder: `../../scripts/build_layered_review.py`. It reconstructs the
composite from the real atlas and manifest and keeps labels/grid/pivot crosses
inside the separate review grid.

ImageGen intake: `../../scripts/prepare_watchtower_projection_master.py`. It
preserves the source, invokes the canonical chroma-to-alpha helper and records
checksums, alpha statistics, margins and the still-unapproved manual visual gate.

Ordered generation plan:
`../../assets/staging/prompts/watchtower_source_call_plan_v1.json`.
It separates the projection master, coherent structural/mechanism edits,
animation children, projectile/impact and material-specific debris into
fourteen gated ImageGen 2 calls.

Visual approval template:
`../../assets/staging/candidates/watchtower/watchtower_projection_review_template_v1.json`.
Promotion tool: `../../scripts/promote_watchtower_projection_master.py`.
It requires explicit user confirmation, all PASS criteria and matching
candidate/intake checksums before copying anything into approved masters.

Gate reporter: `../../scripts/watchtower_pipeline_status.py`. Its status is
derived from actual pipeline artifacts; `mayStartNextObject` becomes true only
after every gate passes.

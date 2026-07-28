# Watchtower Layer Contract v3

> **SUPERSEDED.** Its approved-reference claim belongs to the pre-Option-C
> Watchtower. Use `watchtower-layer-contract-v4.md`.

Updated: 2026-07-24

Status: **authoritative high-granularity decomposition contract**

Approved projection reference:
`assets/staging/candidates/watchtower/watchtower_projection_master_v4_alpha.png`

Projection master v5 is rejected and must not influence layer geometry.

V3 replaces Layer Contract v2. The goal is visible tabletop depth assembled from
many independent flat cardboard pieces, never simulated facade perspective.

## 1. Shared coordinate system

Every structural source uses the master 1254 × 1254 canvas. ImageGen removes
unrelated components without centering, resizing, rotating or translating the
retained part.

All full-canvas sources are validated by 1:1 compositing. Only then are they
cropped into tight runtime rectangles.

## 2. Depth grammar

Each visible height step must be a real runtime layer:

1. footprint shadow card;
2. foundation card;
3. deck underlay;
4. printed deck sectors;
5. parapet support ring;
6. independent parapet stones;
7. attachment pads;
8. bearing washers;
9. weapon subparts;
10. animated overlays and FX.

No shading may invent a height step that has no corresponding layer. Contact
shadows are compact and belong to the upper child. The manifest records `z`,
`pivot`, `attachment`, `drawOrder` and optional animation ownership.

## 3. Stable base stack

| Layer ID | Function |
|---|---|
| `footprint_shadow_card` | compact soft footprint shadow |
| `foundation_ring_card` | lowest solid-board circular foundation |
| `deck_underlay_card` | dark inset support below printed deck |
| `deck_sector_01..08` | eight radial printed timber wedges |
| `deck_archive_mark` | separate faded Kitezh-17 inspection-print card |
| `parapet_support_ring` | dark support visible under stone pieces |
| `parapet_stone_01..20` | individually named stone punchboard tiles |
| `access_notch_lip_a` | upper access-notch reinforcement |
| `access_notch_lip_b` | lower access-notch reinforcement |
| `repair_staple_01` | first oxidized-copper repair |
| `repair_staple_02` | second oxidized-copper repair |

The twenty stones retain a stable assembled footprint during normal play but
detach independently during destruction.

## 4. Central mount stack

| Layer ID | Function |
|---|---|
| `bearing_lower_washer` | broad dark bearing base |
| `bearing_copper_route_01..04` | separate printed copper arc cards |
| `bearing_upper_washer` | smaller raised rotating plate |
| `bearing_socket` | central axle cap |
| `bearing_shadow` | compact rotating child shadow |

The crossbow group attaches to `active_primary_pivot` on `bearing_socket`.

## 5. Crossbow construction

| Layer ID | Function |
|---|---|
| `crossbow_body_lower` | lower guide/body card |
| `crossbow_body_upper` | brighter upper guide card |
| `crossbow_rear_cap` | rear loading cap |
| `crossbow_trigger_block` | readable copper trigger housing |
| `crossbow_left_arm_lower` | left arm support card |
| `crossbow_left_arm_upper` | left printed arm face |
| `crossbow_right_arm_lower` | right arm support card |
| `crossbow_right_arm_upper` | right printed arm face |
| `crossbow_fastener_01..04` | independent copper fastening plates |
| `crossbow_string_tense` | idle/aim string |
| `crossbow_string_release_01..02` | release deformation |
| `crossbow_recoil_overlay_01..03` | short mechanism recoil |
| `loaded_bolt` | bolt visible before release |
| `projectile_bolt` | owner-specific flying bolt |

The whole crossbow rotates as one parent group, while its children animate
locally.

## 6. Secondary modules

| Layer ID | Function |
|---|---|
| `flag_mount_lower` | lower circular cloth attachment card |
| `flag_mount_cap` | raised ochre cap |
| `signal_cloth_01..04` | four cardboard deformation states |
| `lantern_mount_pad` | deck attachment card |
| `lantern_body_lower` | dark lantern backing |
| `lantern_copper_frame` | raised copper outline |
| `lantern_enamel_repair` | blue-grey repair plate |
| `lantern_window` | amber paper window |
| `lantern_flame_01..04` | paper flame animation |
| `lantern_glow_01..04` | translucent glow animation |
| `bolt_rack_lower` | rack backing card |
| `bolt_rack_upper` | raised slot face |
| `reserve_bolt_01..04` | four separately addressable bolts |
| `reserve_slot_empty` | readable empty fifth slot |
| `inventory_tick_01..05` | separate faded ochre count marks |

## 7. Attack, impact and destruction

| Layer ID | Function |
|---|---|
| `attack_flash_01..03` | paper muzzle flash |
| `impact_01..04` | wood/stone paper-chip impact |
| `debris_stone_01..05` | selected detached parapet pieces |
| `debris_deck_01..04` | detached deck wedges |
| `debris_crossbow_body` | broken guide |
| `debris_crossbow_left_arm` | detached left arm |
| `debris_crossbow_right_arm` | detached right arm |
| `debris_trigger` | detached trigger card |
| `debris_signal_cloth` | detached cloth |
| `debris_lantern_01..03` | separated lantern stack |
| `debris_bolt_01..04` | scattered reserve bolts |
| `splinter_wood_01..06` | small cardboard wood splinters |
| `chip_stone_01..06` | small cardboard stone chips |
| `destroy_dust_01..05` | settling paper/cardboard dust |

## 8. Required parent hierarchy

```text
watchtower
├── stable_base
│   ├── footprint/foundation
│   ├── deck_stack
│   └── parapet_stack
├── bearing_group
│   └── crossbow_group
│       ├── body_stack
│       ├── left_arm_stack
│       ├── right_arm_stack
│       ├── string_animation
│       └── loaded_bolt
├── signal_cloth_group
├── lantern_group
├── bolt_reserve_group
└── fx_group
```

## 9. Assembly acceptance

- no manual scale or rotation correction during composite;
- depth reads from overlapping cardboard edges and contact shadows;
- the primary weapon remains the largest and most saturated functional accent;
- every visually raised construction step maps to a manifest layer;
- normal animation keeps the stable footprint unchanged;
- destruction can detach visible construction pieces without inventing debris;
- the compact runtime atlas remains below 5 MB;
- review grid, labels, pivots and composite never enter the runtime atlas.

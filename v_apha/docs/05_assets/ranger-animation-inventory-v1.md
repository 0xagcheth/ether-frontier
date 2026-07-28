# Ranger animation inventory v1

Status: **complete; ready for runtime atlas packing**

## Layer ownership

### Inherited `fortress_ranged` layers

- `base_stone_token` — stable footprint
- `central_socket` — static weapon bearing
- `lantern_body` — static ambient child
- `lantern_flame_01..04` — shared `180 ms` idle loop
- `stone_debris_a/b/c` — shared destruction debris
- `destroy_dust_01..04` — shared stone-base destruction effect
- `destroy_sparks_01..04` — shared metal destruction accent

### Ranger canon layers

- `rapid_crossbow` — rotates around inherited weapon socket
- `bolt_magazine` — child of weapon, local `90°`, inherits rotation
- `hunting_optics` — child of weapon, inherits rotation
- `arrow_rack` — static northern-rim child
- `ranger_trim` — static south-east identity child
- `barbed_bolt` — projectile spawned by tail at muzzle anchor

### Ranger-owned effect layers

- `ranger__muzzle_fx__rapid_flash_loop_v1` — four compact fast frames, canon
- `ranger__impact_fx__barbed_hit_v1` — four non-looping paper/metal impact frames, canon

## Runtime clips

| Clip | Layers | Behavior |
|---|---|---|
| `idle` | shared lantern frames | loop; base and all Ranger children remain static |
| `aim` | crossbow + magazine + optics | runtime rotation around `weaponSocket`; footprint, rack, trim, and lantern fixed |
| `attack` | rotating weapon group + rapid muzzle frames | short non-looping flash; intended repeated cadence is controlled by gameplay, not baked into atlas |
| `projectile` | barbed bolt | spawn tail at muzzle; translate and rotate along trajectory |
| `impact` | missing barbed-hit frames | non-looping owner-specific effect at bolt tip/contact point |
| `destroy` | shared stone debris/dust/sparks plus existing Ranger child layers | magazine, optics, rack, trim and complete weapon become independently simulated debris; no baked composite destruction frame |

## Destroy reuse decision

The existing Ranger child sprites already satisfy independent debris rendering. Runtime destruction will detach and simulate them directly. New duplicate debris art is not required for magazine, optics, rack, or trim. Shared base-stone debris and dust remain valid because Ranger inherits the same platform construction.

## Atlas gate

Both Ranger-owned effects have passed visual and technical validation. Pack inherited layers and Ranger-owned layers into one Ranger-family runtime atlas, preserving their source manifest references and keeping the result under `5 MB`.

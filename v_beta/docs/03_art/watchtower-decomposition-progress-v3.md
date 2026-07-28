# Watchtower Decomposition Progress v3

Updated: 2026-07-24

Status: **in progress**

## Current source groups

- `watchtower_structural_base_master_v1`
  - clean foundation, deck and twenty-stone parapet;
  - all movable and secondary modules removed;
  - exact v4 footprint retained.
- `watchtower_bearing_group_v1`
  - complete reconstructed washer and copper-route stack;
  - visually valid, pending master-bound normalization.
- `watchtower_crossbow_group_v2`
  - complete reconstructed crossbow construction;
  - one forward steel-blue bolt tip;
  - incorrect double-ended v1 bolt rejected;
  - pending master-bound normalization and sublayer extraction.
- `watchtower_crossbow_body_stack_v1`
  - complete reconstructed lower/upper guide, rear cap, trigger housing and body
    fasteners without arms, string or projectile.
- `watchtower_crossbow_arm_stacks_v1`
  - paired but physically separated left/right arm stacks with end clamps.
- `watchtower_loaded_bolt_v1`
  - one forward steel-blue tip, dark shaft and rear wooden fletching;
  - intentionally generated oversize for clean source detail and pending
    master-bound normalization.
- `watchtower_crossbow_string_tense_v1`
  - complete drawn V-shaped string with two endpoints and central nock;
  - pending rotation/scale normalization to the arm endpoints.
- `watchtower_crossbow_string_release_v1`
  - shallow released state with a small asymmetric vibration bend;
  - independent animation overlay, not baked into the weapon.

## Structural extraction

- eight independently cropped deck sectors;
- twenty parapet-stone candidates detected from their closed grey-blue printed
  faces rather than cut with equal arbitrary angles;
- each output has a tight rectangle, master-relative pivot and draw order;
- `deck_full_reference` is QA-only and explicitly excluded from runtime;
- fragment manifest:
  `structural_layers/watchtower_structural_layers_v3.fragment.json`;
- separate labelled QA grid:
  `watchtower_structural_review_grid_v3.jpg`.

The first equal-angle stone extraction was rejected because some masks crossed
tile boundaries. The active extraction derives angular boundaries from the
twenty detected stone-face centroids.

## Bearing extraction

- normalized bearing diameter: 500 source pixels;
- `bearing_lower_washer`;
- `bearing_upper_washer`;
- `bearing_socket`;
- `bearing_copper_route_01..04`;
- all seven candidates have tight rects, center-relative pivots, attachment and
  draw order in:
  `bearing_layers/watchtower_bearing_layers_v3.fragment.json`.

## Crossbow normalization

Status: **REJECTED**

The body, arm and bolt sources came from independent ImageGen reconstructions.
Although each source is visually usable in isolation, they do not share one
mechanical geometry:

- arm roots do not meet one common mounting axis;
- body width and arm-stack scale describe different weapon variants;
- the loaded bolt is too large for the reconstructed guide;
- deterministic offsets can hide gaps but cannot repair incompatible design.

`watchtower_crossbow_composite_v3.png` and its fragment manifest are QA history
only and must not enter the runtime atlas.

Replacement rule: normalize the coherent
`watchtower_crossbow_group_v2_alpha.png` once, then extract every runtime child
from that one normalized construction. Independently generated body/arm/bolt
sources may supply hidden texture patches only; they cannot define geometry.

## Coherent crossbow replacement v4

- `watchtower_crossbow_coherent_master_v4.png` fixes one shared loaded geometry;
- `watchtower_crossbow_unstrung_master_v1` removes only the string and bolt and
  restores the guide/arm surfaces beneath them;
- the unstrung source is normalized to the coherent 540 × 529 weapon bounds;
- left arm, right arm and body stack are extracted from that single normalized
  raster;
- their active composite is:
  `watchtower_crossbow_unstrung_composite_v4.png`;
- their replacement manifest is:
  `crossbow_layers_v4/watchtower_crossbow_layers_v4.fragment.json`.

The previous `crossbow_layers` directory remains rejected QA history.

## Normalization rule

ImageGen isolation may preserve orientation while changing the part's internal
scale. Therefore:

1. placement and target bounds come from projection master v4;
2. generated isolated sources provide complete occluded geometry and print;
3. normalization is deterministic and recorded;
4. the 1:1 composite must match v4 before tight cropping;
5. no arbitrary visual hand-fitting is allowed.

## Next extraction

1. create the lower foundation and parapet-support cards;
2. normalize the coherent crossbow group to the v4 weapon bounds;
3. extract left/right arms, body, loaded bolt and taut string from that one
   normalized geometry;
4. map the released string to the same endpoints;
5. generate the recoil overlay family;
6. generate the cloth, lantern and reserve modules;
7. build the first high-granularity 1:1 composite.

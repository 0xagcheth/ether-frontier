# Environment Bible

## Battlefield Direction

The battlefield is a readable medieval fortress approach: stone lanes, dark earth, dead grass, moss, ruins, torch warmth, and seal glow near Grimhold.

## Terrain Hierarchy

1. Enemy paths must be clearest.
2. Buildable ground must be distinct from paths.
3. Resources must be identifiable but secondary.
4. Decoration must never obscure gameplay state.

## Background Exception

The full battlefield background is the only visual asset that may ignore the sprite cutout rule. It fills the scene and should not use black-key transparency.

## Resource Nodes

Trees and rocks must look harvestable, not like passive decoration. Growth states should preserve object identity and footprint.

## Perspective

Terrain supports near top-down with slight tilt readability. Individual objects are designed from overhead first; side faces are only subtle thickness cues. The map must not become a 3D diorama or forced-perspective board.

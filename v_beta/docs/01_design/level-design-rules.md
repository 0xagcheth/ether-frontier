# Level Design Rules

## Map Readability

Paths must read before decoration. The player should identify enemy lanes, buildable zones, blocked cells, resources, and the fortress direction within one second.

## Camera And Board

Levels use a 2D orthographic top-down board with painterly/pixel perspective cues. Do not introduce a 3D camera, true isometric-map grid, or side-scroller framing.

## Lane Rules

- Paths should have clear value contrast against buildable terrain.
- Curves and chokepoints should support tower strategy, not obscure enemy motion.
- Multi-lane levels must reveal lane intent before the wave starts.
- Flying enemies may bypass ground lanes, but their shadow/altitude language must stay readable.

## Resource Placement

Trees, stone, gold, and other harvest nodes should create meaningful build tradeoffs. Resource nodes must not hide tower footprints or path boundaries.

## Wave Pacing

Early levels teach one new pressure at a time. Later levels may combine pressures, but every spike needs preview information.

Boss waves should be spectacle moments with reduced visual clutter from lesser enemies unless the boss design depends on summons.

## Source Material

Distilled from market research, current grid/path behavior, and the project vision.

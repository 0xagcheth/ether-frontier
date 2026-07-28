# Master Visual Style

## Principle

Ether Frontier does not imitate any existing game, studio, or franchise.

The project follows its own artistic language. Every asset must belong to the same visual universe because it follows the same design rules, not because it copies a reference.

## Core Philosophy

The world feels like an illustrated fantasy book brought to life.

It is:

- hand-crafted
- iconic
- clean
- readable
- designed for gameplay first
- simplified from traditional illustration into top-down game assets

It is not:

- realistic
- anime
- pixel art
- a studio imitation
- a clone of any existing game
- AI glossy
- concept art rendering

The useful inspiration is the production discipline of traditional hand-painted animation backgrounds and character design from late 1980s-1990s animated feature films, adapted into a clean near top-down with slight tilt game art language.

## Camera

NEAR TOP-DOWN WITH SLIGHT TILT.

Not full isometric. Not 3/4 view. Not side-view. Not perspective.

The camera is almost directly above the world, with only a small angled tilt to reveal volume.

Top planes must dominate: roughly 85-90% roof/top/crown/upper-surface read, with only 10-15% side thickness. Side faces are subtle thickness cues, not facades.

No ordinary gameplay object may show a tall front facade, full doorway, staircase, or vertical wall dominating the asset. Those features belong only to deliberate large structures such as castles, and even there top-plane readability must remain primary.

No asset may depend on baked terrain or forced perspective to read correctly.

Every object must be movable anywhere on the map without breaking the camera read.

For cardboard tabletop tokens and layered object atlases, prefer true top-down orthographic 90° when the object can still read clearly. The confirmed Watchtower baseline uses this stricter top-down read: the platform, weapon, flag, lantern, and other child layers are seen from above as board-game pieces, not as facades or rear/side views.

Layered objects must not use camera tilt to fake animation. Motion comes from composited child layers: rotating weapons, wind-driven fabric, flames, gears, glows, projectiles, and debris.

## World

The world feels ancient. Every object has history.

- Castles look centuries old.
- Trees feel alive.
- Weapons feel legendary.
- Resources feel valuable.
- Nothing feels generic.

## Shape Language

Large readable shapes dominate.

Every object must be identifiable by silhouette alone. If color is removed, the object should still read.

Use very few small details. No visual noise. No decoration that does not improve readability, identity, or material clarity.

## Materials

Materials are more important than texture.

- Stone feels heavy.
- Wood feels warm.
- Metal feels dense.
- Leather feels soft.
- Fabric feels light.
- Gold feels precious.

The material must be understood before the viewer notices texture.

## Color

Use emotional colors, not photorealistic colors.

- Shadows are cool.
- Lights are warm.
- Stone is blue-gray.
- Wood is warm brown.
- Grass is blue-green instead of saturated green.
- Magic uses accent colors.
- Each biome has a restrained palette.

## Light

One main light source: top-left.

Lighting is soft and illustrated. No cinematic lighting, dramatic rim lights, realistic GI, glossy reflections, or physically rendered materials.

Volume is created through color transitions and simplified forms.

## Linework

Use soft illustrated outlines. Never use thick comic outlines or black outlines.

Edges use darker local colors. The illustration should feel hand-made, not vector-clean or AI-polished.

## Detail

Detail exists only where it improves readability.

Never add detail because there is empty space. Large forms dominate; small details support them.

## Proportions

Proportions are stylized and heroic:

- Buildings are slightly oversized.
- Weapons are slightly oversized.
- Trees have large crowns.
- Roofs are visually important.
- Characters are readable at small size.

## Characters

Characters are designed like animation heroes:

- not realistic humans
- not anime
- not caricatures
- strong silhouette
- readable costume
- large iconic equipment
- simple faces
- maximum personality with minimum detail

## Environment

The environment is decorative like a classic illustrated fairy tale, but gameplay remains first.

Everything has rhythm and balance. Nature is stylized. Nothing should feel procedural.

## Buildings

Buildings use storybook architecture:

- readable roofs
- large entrances
- simple windows
- strong silhouettes
- no tiny bricks
- no tiny roof tiles
- no micro-detail

## Trees

Trees are sculptural:

- large crown masses
- visible trunk
- readable canopy
- unique silhouette per tree type
- never realistic foliage

## Gameplay First

The player must instantly distinguish:

- walkable
- blocked
- interactive
- resource
- enemy
- friendly
- objective

Everything must remain readable when the screen is full.

## Reference Policy

References describe why something works, not what to copy.

The artistic philosophy may learn from broad craft principles:

- traditional late 1980s-1990s hand-painted animation process
- illustrated fantasy books
- classic game readability
- large readable RTS shape language
- atmospheric restraint
- heroic material design

without copying a studio, franchise, or specific title.

## Never Do

- no realism
- no AI glossy look
- no concept art rendering
- no photobashing
- no painterly brush noise
- no random texture overlays
- no procedural-looking assets
- no 3/4 or perspective camera
- no cinematic perspective
- no exaggerated depth
- no visual clutter

## Final Test

Every asset must answer YES to all questions:

- Can it be recognized in pure black silhouette?
- Can it be recognized at 64x64?
- Can it be moved anywhere on the map?
- Does it feel hand-crafted?
- Does it belong to the same universe as every other asset?

If any answer is NO, redesign the asset.

# Style Self Review

## Purpose

This is the pre-finish review every visual asset must pass before it can enter the formal quality gate.

The goal is not beauty. The goal is timeless readability.

## Reject If It Looks Like

- AI generated
- glossy
- over-rendered
- concept art
- semi-realistic
- mobile game
- generic fantasy
- specific studio clone
- specific game clone
- anime
- painterly
- realistic
- procedural
- vector-clean
- textureless plastic or foam
- noisy texture overlay

## Increase

- silhouette clarity
- shape simplicity
- material readability
- correct camera-mode readability; exact 90° top-down for runtime objects
- hand-crafted feeling
- iconic design
- emotional color
- warm/cool light discipline
- gameplay readability

## Reduce

- micro-detail
- texture noise
- baked shadows tied to one terrain
- decorative clutter
- rim lighting
- glossy highlights
- realistic material simulation
- perspective depth
- side-face dependence

## Required Self-Review Output

```text
Asset:
Looks AI-generated: YES/NO
Looks glossy: YES/NO
Looks over-rendered: YES/NO
Looks like concept art: YES/NO
Looks semi-realistic: YES/NO
Looks generic fantasy: YES/NO
Looks like a clone: YES/NO
Top-down readable: YES/NO
Camera mode appropriate to asset class: YES/NO
Silhouette readable: YES/NO
Material readable: YES/NO
Cardboard fibers visible through print: YES/NO
Looks like plastic/foam/vector fill: YES/NO
Hand-crafted feeling: YES/NO

Decision: PASS / REVISE / REJECT
Required simplifications:
-
```

Any YES in the first seven checks requires REVISE or REJECT.

For layered cardboard objects, `Cardboard fibers visible through print: NO` or
`Looks like plastic/foam/vector fill: YES` is also an automatic REVISE/REJECT.
For runtime objects, any camera result other than true top-down orthographic 90°
is an automatic REJECT.

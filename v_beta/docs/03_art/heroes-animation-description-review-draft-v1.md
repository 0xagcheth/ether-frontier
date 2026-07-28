# Ether Frontier — Hero Animation Description Review Draft v1

Status: **review draft; text only; not canon**  
Updated: 2026-07-27

## 1. Scope

This document describes animation for:

- Spas;
- Velimudr;
- Tara.

It contains no drawings, generated images, prompts, atlas files or numerical
timings approved for runtime.

It does not describe the animation of their nine unique buildings. Those remain
a later review stage.

## 2. Shared animation rule

The heroes are field specialists who can defend themselves, not conventional
combat units.

Their movement and actions must show:

- observation;
- physical work with real instruments;
- preparation before an effect;
- visible completion or withdrawal;
- fatigue and interruption;
- return of every detached object to its owner.

Every hero receives one ordinary attack with a unique physical instrument,
range, silhouette and secondary effect. No hero receives a generic sword swing,
generic projectile, spell cast, victory pose or glowing power-up animation.

## 3. Projection and direction

Gameplay animation uses exact top-down orthographic 90-degree projection and
premium layered cardboard construction.

Each hero requires six directional sets:

- front/down;
- back/up;
- three-quarter right;
- three-quarter left;
- side right;
- side left.

Mirroring is allowed only for the body locomotion layer. Asymmetric equipment
must retain its real side:

- Spas's Three-Moon Measure remains on his left;
- Velimudr's comparison table remains on his left and shoulder cloth on his
  right;
- Tara's half-mantle remains on her left and Returned-Ground Frame on her right.

## 4. Shared state family

Every hero requires:

1. `arrive` — enters the field or unfolds from the Last Knot;
2. `idle_primary` — readable neutral loop;
3. `idle_secondary` — rare character-specific loop;
4. `walk` — ordinary field movement;
5. `hurry` — movement toward a threatened building or cell;
6. `attack` — unique repeatable self-defence action;
7. `observe` — reads the current condition;
8. `prepare` — sets up the defining instrument;
9. `work` — performs the character-specific non-combat action;
10. `resolve` — records the result and retrieves loose pieces;
11. `interrupted` — action stops without generic knockback;
12. `hit` — restrained physical reaction if the hero can be affected;
13. `exhausted` — visible limit after extended work;
14. `return` — goes back to the Last Knot;
15. `defeat` — withdraws or becomes unable to work, never graphic death.

## 5. Cardboard construction rule

Each hero is assembled from separate gameplay layers:

- body and legs;
- head and hair;
- principal garment shape;
- defining instrument;
- small record or material pieces;
- owner shadow;
- character-specific emitted pieces.

The base body footprint stays stable. Arms, tools, cards, cords, vessels and
frames may move beyond it but must return or remain explicitly in the world.

# Part I — Spas

## 6. Animation identity

Spas's animation language is **weight, measurement and reluctant decision**.

He moves slowly until a forecast becomes actionable. Then his movement becomes
direct and economical. He never gestures like a prophet receiving revelation.

His defining moving elements are:

- three unequal rings of the Three-Moon Measure;
- central Midgard plumb;
- six forecast leaves;
- ochre evacuation cord;
- four plates of the stone mantle.

## 7. Spas — `arrive`

Spas does not appear in a flash.

1. The ochre evacuation cord emerges from the Last Knot.
2. Three unequal lunar rings slide along it in folded form.
3. Spas follows, holding the central plumb low to the ground.
4. He seats both feet, checks the direction of the cord and locks the Measure
   against his left shoulder.
5. The four mantle plates settle one after another rather than simultaneously.

The final frame must match `idle_primary` exactly.

## 8. Spas — `idle_primary`

A slow asymmetrical inspection loop:

1. Spas checks the small Lelya ring.
2. He shifts the central plumb by a small amount.
3. The large Fatta ring responds later than expected.
4. He looks down at one forecast leaf.
5. He returns the leaf without changing its confidence tab.

The body barely moves. Most life comes from the instrument's imperfect balance.

## 9. Spas — `idle_secondary`

Rare loop showing doubt:

1. Spas begins to write a date on a forecast leaf.
2. He pauses.
3. He checks which calendar edge is attached.
4. He turns the leaf over and leaves the date blank.

This loop should occur infrequently so the gesture remains meaningful.

## 10. Spas — `walk`

- broad deliberate four-step cycle;
- shoulders remain steady under the stone mantle;
- lunar rings lag slightly behind the body;
- the plumb swings with diminishing amplitude;
- six forecast leaves move independently but do not flutter like loose paper;
- evacuation cord remains secured around the right forearm.

Spas must feel heavy and experienced, not slow because of age.

## 11. Spas — `hurry`

- torso leans only slightly;
- right hand secures the evacuation cord;
- left shoulder lowers to stabilise the Measure;
- stride length increases rather than becoming a run;
- mantle plates knock once against their separate fasteners;
- final step plants firmly without a skid.

## 11A. Spas — `attack`: Shard of Lelya

Spas directs a small retained fragment of destroyed Lelya. The fragment changes
its effective weight, strikes one enemy at medium range and briefly makes the
target heavier, slowing its movement. The attack connects Spas directly to the
destruction of Lelya and the old technology of gravity and orbital control.

1. Spas turns the small Lelya ring of the Three-Moon Measure toward the target.
2. A dark fragment separates from its physical cradle inside that ring.
3. The Fatta ring shifts in the opposite direction as a visible counterweight.
4. The fragment accelerates close to the ground, without a luminous trail.
5. On impact, the target's layered body compresses toward its ground pin and its
   next steps become visibly heavy.
6. Spas reverses the ring alignment; the fragment returns and locks into its
   cradle before he can attack again.

The attack is gravitational technology later described as lunar priestcraft,
not a generic magical missile.

## 12. Spas — `observe`

Used for wave forecast and inspection of a threatened location.

1. Spas lowers the Midgard plumb onto the cell.
2. He unfolds the three rings in sequence: Mesyats, Fatta, Lelya.
3. Each ring settles at a different angle.
4. He places two forecast leaves beside the reading.
5. If they disagree, he keeps both visible.
6. He marks the result reliable, disputed or unknown with a separate tab.

No celestial light enters the rings.

## 13. Spas — `prepare`

Used when a forecasted danger becomes imminent.

1. He releases the evacuation cord from his forearm.
2. The cord is fixed to the ground with one small stone weight.
3. He rotates the Lelya ring toward the threatened Road.
4. The other two rings remain independent reference points.
5. One mineral-red warning leaf is moved to the front of the Measure.

The pose must clearly show that Spas is ready to act but has not yet ordered
movement.

## 14. Spas — `work`

Spas commits to the forecast:

1. He pulls the evacuation cord through both hands.
2. The cord extends toward the threatened cell or building.
3. Three forecast leaves align temporarily along it.
4. The stone mantle opens slightly at its deliberate rear gap.
5. Spas seats the plumb and holds the route steady until the action completes.

The animation represents issuing an accountable route, not casting a line of
magic.

## 15. Spas — `resolve`

### Correct forecast

- the red warning leaf turns to its recorded side;
- the cord is retrieved in ordered loops;
- one mantle plate lifts and settles, showing released tension;
- Spas stores the confirmed leaf separately from unresolved leaves.

### Disputed or incomplete result

- the cord returns normally;
- the leaf remains outside the main stack;
- Spas does not perform a success gesture.

## 16. Spas — `interrupted`, `hit`, `exhausted`

### Interrupted

The plumb is displaced, one lunar ring folds incorrectly and the cord loses
tension. Spas catches the ring before it strikes the ground and withdraws the
warning leaf.

### Hit

One mantle plate shifts outward and absorbs the visible motion. Spas steps once
to restore balance. No flash, recoil launch or weapon reaction.

### Exhausted

He lowers the Three-Moon Measure onto its own supports, removes the mantle's
front weight and sits beside—not upon—the forecast leaves. The instrument
continues a very small unstable motion.

## 17. Spas — `return` and `defeat`

### Return

Spas retrieves the evacuation cord from the farthest point inward, closes the
lunar rings, returns all six leaves and walks back along the cord. The cord is
the final element absorbed by the Knot.

### Defeat

The Measure can no longer hold alignment. Spas closes it manually, removes the
red warning leaf and leaves the field carrying the instrument with both hands.
He is not killed or transformed into debris.

# Part II — Velimudr

## 18. Animation identity

Velimudr's animation language is **comparison, interruption of certainty and
visible revision**.

He never waves text like magical authority. His gestures are small, exact and
sometimes impatient.

Defining moving elements:

- folding Table of Three Versions;
- asymmetric indigo shoulder cloth;
- revision clips;
- speaker-present token;
- unfinished wooden board.

## 19. Velimudr — `arrive`

1. The unfinished board slides from the Knot first.
2. Velimudr follows with the triangular table folded under his left arm.
3. He places the speaker-present token on the ground before fully entering.
4. The indigo shoulder cloth unfolds into its asymmetrical position.
5. He checks that the token remains visible and enters `idle_primary`.

## 20. Velimudr — `idle_primary`

1. He opens one side of the triangular table.
2. Reads a line.
3. Opens the second side and compares the edge lengths.
4. Attaches a small copper clip between the versions.
5. Notices the clip implies more agreement than exists and removes it.

The loop ends with all three versions still separate.

## 21. Velimudr — `idle_secondary`

Velimudr discovers ink transferred to his cheek:

1. touches the cheek;
2. examines the stained finger;
3. checks which writing plate supplied the colour;
4. records the accidental transfer on a tiny scrap;
5. returns to work without cleaning it immediately.

This is restrained character humour, not slapstick.

## 22. Velimudr — `walk`

- measured uneven rhythm caused by the left-leg injury;
- triangular table remains tight against the left side;
- shoulder cloth moves as one heavy working surface, not a cape;
- revision clips respond with small delayed rotations;
- unfinished board stays vertical behind the belt;
- free right hand remains ready to steady loose records.

## 23. Velimudr — `hurry`

Velimudr does not run cleanly:

- folds the table only halfway;
- uses its closed edge briefly as support;
- protects the unfinished board with his right forearm;
- takes two short steps followed by one longer compensating step;
- arrives irritated by the physical interruption, not frightened.

## 23A. Velimudr — `attack`: Spoken Word

Velimudr reads a short operational formula reconstructed from the damaged
boards attributed to him. A narrow material line of text reaches the enemy,
crosses out one of its active properties and lowers its defence for a short
time. The direct damage is light, but later allied attacks become stronger.

1. Velimudr selects one small board from the damaged early version, not from the
   confident public edition.
2. He places the speaker-present token against his throat and speaks the formula.
3. A narrow printed strip feeds physically from the board across the ground.
4. The strip reaches the enemy and brackets one visible armour or body layer.
5. That layer shifts out of alignment rather than vanishing.
6. The strip differs slightly on successive attacks, showing that no final
   authoritative wording exists.
7. When the weakening ends, the strip breaks at its perforations and returns as
   loose record pieces for Velimudr to collect.

The effect uses the setting's operational language that can alter reality. It
must resemble a dangerous textual procedure, not a wizard's glowing spell.

## 24. Velimudr — `observe`

1. Places the speaker-present token nearest the observed object.
2. Opens the source side of the table.
3. Opens the public-edition side.
4. Leaves the correction side closed at first.
5. Checks the owner and date attachments.
6. Only then opens the correction side.

The order communicates that correction follows inspection rather than replacing
the source immediately.

## 25. Velimudr — `prepare`

1. The triangular table unfolds on three unequal supports.
2. Velimudr selects one revision clip but does not attach it.
3. The shoulder cloth spreads into a secondary work surface.
4. The unfinished board is placed beside the three versions.
5. He rotates the speaker-present token toward the current witness.

## 26. Velimudr — `work`

1. Velimudr takes a strip from the affected object or record.
2. Places it successively beside all three versions.
3. Rejects one tempting but incorrect attachment.
4. Uses a distinct clip to bind the strip to its actual source.
5. Keeps the correction physically detachable.

No letters fly through the air. The visible action is material attribution.

## 27. Velimudr — `resolve`

### Successful attribution

- returns the source to its owner;
- places the correction beside it rather than over it;
- closes the public-edition side last;
- retrieves the speaker-present token.

### Unresolved attribution

- removes all clips;
- leaves the strip on the unfinished board;
- turns the empty final section toward the camera.

## 28. Velimudr — `interrupted`, `hit`, `exhausted`

### Interrupted

One table support collapses. Velimudr catches the source side first, allowing
the public edition to close. He visibly checks that no loose page has been
mistaken for a final result.

### Hit

The shoulder cloth folds over the work surface. One clip detaches and Velimudr
follows it with his eyes before restoring his stance.

### Exhausted

He sits on the closed table frame, removes his reading plates and rubs the
bridge of his nose. The unfinished board remains propped upright beside him.

## 29. Velimudr — `return` and `defeat`

### Return

He closes the correction, public and source sides in reverse working order,
collects every clip, retrieves the speaker token and carries the unfinished
board into the Knot last.

### Defeat

Velimudr cannot determine ownership of the active record. He removes every clip,
places all versions in a neutral stack and withdraws without declaring a final
reading.

# Part III — Tara

## 30. Animation identity

Tara's animation language is **testing, pressure transfer and deliberate
restoration**.

Her motion is low, grounded and physically strong. Nothing grows instantly
around her and she never performs nature magic.

Defining moving elements:

- four-bed Returned-Ground Frame;
- three Covenant vessels;
- dark-turquoise half-mantle;
- Lelya-glass separation tool;
- owner-coloured seed packets.

## 31. Tara — `arrive`

1. The square Returned-Ground Frame emerges flat from the Knot.
2. Tara steps into its open centre and lifts it onto her right side.
3. Three Covenant vessels follow separately and lock onto her pressure belt.
4. The turquoise half-mantle unfolds from the left shoulder.
5. She tests the ground with one wide-soled boot before assuming `idle_primary`.

## 32. Tara — `idle_primary`

1. Tara removes a small soil sample from the pressure belt.
2. Compares it with one bed of the folded Frame.
3. Checks the surface-water vessel.
4. Checks the Lower Passage vessel separately.
5. Returns the sample without mixing either vessel.

Her idle communicates caution, not serenity with nature.

## 33. Tara — `idle_secondary`

1. A seed packet begins slipping from the right hip.
2. Tara catches it with the shortened fingers of her left hand.
3. Checks the owner-colour tab.
4. Restores it to a different, more secure attachment.
5. Tests the knot twice before releasing it.

## 34. Tara — `walk`

- compact strong four-step gait;
- wide soles seat fully before weight transfer;
- Returned-Ground Frame remains vertical on the right;
- half-mantle moves low and heavy, never like a cape;
- three vessels swing with different fill weights;
- seed packets remain distinct and do not merge into one colourful mass.

## 35. Tara — `hurry`

- lowers body centre;
- secures all three vessels with left forearm;
- carries the square Frame horizontally like a field stretcher;
- takes short fast steps that avoid unstable ground seams;
- final arrival includes a deliberate weight test before work begins.

## 35A. Tara — `attack`: Perun's Arrow

Tara releases a short directed electrical discharge through a surviving Solar
Covenant conductor. It deals high damage at short-to-medium range and may jump
once to the nearest second enemy with reduced force. Later chronicles present
the discharge as proof that Tara is Perun's daughter; the secure layer records
it as inherited Covenant technology.

1. Tara draws the metal conductor from beside the three Covenant vessels.
2. She touches its lower contact to the ground before raising the upper contact.
3. A compact charge passes from ground through the conductor, never through her
   unprotected body.
4. Tara aims with her open hand and releases one angular mineral-blue discharge.
5. The first target's cardboard layers separate for one sharp frame.
6. If a second target is close enough, a thinner branch crosses to it.
7. Tara grounds the remaining charge and returns the conductor to its holder.

The attack is compact and technical: no storm cloud, divine apparition or
continuous fantasy lightning beam.

## 36. Tara — `observe`

1. Tara places the square Frame flat across the selected cell.
2. Opens the four beds independently.
3. Presses the pressure-stone bed first.
4. Samples flood residue.
5. Opens the living-soil bed only after the first two readings.
6. Places one seed packet in its owner-marked corner without opening it.

## 37. Tara — `prepare`

1. The half-mantle spreads on the ground as a moisture surface.
2. Three Covenant vessels are placed on separate corners.
3. Tara removes the Lelya-glass tool from its ceramic case.
4. The fourth Frame bed remains open for contaminated material.
5. She braces the frame with both wide-soled boots.

## 38. Tara — `work`

1. Tara separates one damaged material layer with the lunar-glass tool.
2. Moves it to the residue bed.
3. Pours small samples from two vessels into separate channels.
4. Opens an exchange only after comparing both flows.
5. Seats a recovery organism or seed packet in the living bed.
6. Applies weight through the pressure belt to settle the repaired layer.

The action is physical restoration with visible owners and costs.

## 39. Tara — `resolve`

### Stable result

- closes residue and pressure beds first;
- returns unused water to its original vessel;
- attaches a visible repair tab to the cell;
- retrieves every unopened seed packet.

### Unsafe result

- leaves the Frame around the cell as a warning boundary;
- seals all seed packets;
- marks the cell unavailable rather than forcing restoration.

## 40. Tara — `interrupted`, `hit`, `exhausted`

### Interrupted

One vessel tips but does not empty. Tara catches it against the pressure belt,
closes all exchange channels and removes the living material before withdrawing.

### Hit

The square Frame turns outward to protect the vessels. Tara takes one low step
back and checks the black Lelya-glass burn on her left side.

### Exhausted

She sits on the closed Frame, removes the pressure belt and places the three
vessels in front of her according to remaining weight. The half-mantle remains
spread beneath them to catch leakage.

## 41. Tara — `return` and `defeat`

### Return

Tara closes each Frame bed, returns every sample, locks the three vessels and
retrieves the half-mantle from the ground. She carries any unresolved material
into the Knot rather than leaving it unnamed.

### Defeat

The selected ground cannot safely hold restoration. Tara seals the four-bed
Frame around the damaged sample, marks the location closed and withdraws. She
does not collapse, die or cause the land to wither theatrically.

# Part IV — Comparison and production limits

## 42. Rhythm comparison

| Hero | Movement rhythm | Main preparation shape | Work rhythm | Failure behaviour |
|---|---|---|---|---|
| Spas | heavy, direct, measured | three unequal rings and long cord | align, announce, hold route | closes forecast and withdraws authority |
| Velimudr | uneven, precise, interrupted | imperfect triangle and separate versions | compare, reject, attach context | removes all clips and leaves unknown |
| Tara | low, strong, terrain-aware | divided square and three vessels | test, separate, exchange, settle | seals unsafe ground rather than forcing repair |

### Ordinary attack comparison

| Hero | Attack | Range | Impact | Secondary effect | Dominant silhouette |
|---|---|---|---|---|---|
| Spas | Shard of Lelya | medium | medium | briefly increases enemy weight and slows it | small dark fragment between unequal lunar rings and target |
| Velimudr | Spoken Word | long | light | temporarily lowers defence | narrow material text strip bracketing one target layer |
| Tara | Perun's Arrow | short-medium | high | one weaker jump to a nearby enemy | grounded conductor and compact angular discharge |

## 43. Animation separation tests

The animation sets pass only if:

- Spas is recognisable without colour by rings and cord;
- Velimudr is recognisable without colour by triangle, board and clips;
- Tara is recognisable without colour by square Frame, belt and vessels;
- none performs the same generic casting gesture;
- all three ordinary attacks remain distinguishable in silhouette, range and
  secondary effect;
- no detached piece disappears without return, damage or recorded placement;
- successful actions are quieter than fantasy victory animations;
- interruption differs from defeat;
- narrative reality remains monumental and material, while gameplay sprites use
  the approved cardboard representation.

## 44. Review decisions

1. Approve the shared non-combat animation state family?
2. Approve Spas's animation language based on lunar measurement and evacuation
   cord?
3. Approve Velimudr's animation language based on comparison, revision clips
   and the unfinished board?
4. Approve Tara's animation language based on testing, Covenant vessels and
   physical ground restoration?
5. Attack set approved in direction on 2026-07-27: Spas's slowing Shard of
   Lelya, Velimudr's defence-reducing Spoken Word and Tara's chaining Perun's
   Arrow. Exact numerical balance remains unapproved.

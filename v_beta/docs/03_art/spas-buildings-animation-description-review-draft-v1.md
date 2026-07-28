# Ether Frontier — Spas Buildings Animation Description Review Draft v1

Status: **canonical animation direction; approved 2026-07-27**  
Updated: 2026-07-27

## 1. Scope

This document describes animation only for Spas's three approved buildings:

1. Warning Stone;
2. Riphean Passage Yard;
3. Observatory of Three Moons.

It contains no generated art, prompt text, atlas layout, frame counts or final
timings. Velimudr's and Tara's buildings are outside this approved scope.

## 2. Shared presentation

- exact top-down orthographic 90-degree gameplay projection;
- monumental in-world stone mechanisms translated into layered matte cardboard;
- the base footprint never rotates, bounces or changes scale;
- moving rings, plates, wedges, rollers, cords and record leaves are separate
  child layers;
- every change of state is shown by a physical object changing position;
- no runes, magical aura, hologram, portal, generic energy dome or unexplained
  glow;
- readiness, activation, exhaustion and reset must be readable without colour.

## 3. Shared state family

Each building uses only the states relevant to its function:

- `place` — assembly on the selected cell;
- `idle` — neutral state with no stored action;
- `configure` — the player assigns its current responsibility;
- `prepared` — forecast allows the building to begin ready;
- `trigger` — committed gameplay action;
- `resolve` — pieces settle and the result becomes readable;
- `spent` or `occupied` — cannot repeat the action yet;
- `wrong` or `disputed` — evidence is insufficient or incorrect;
- `reset` — between-wave restoration;
- `upgrade` — added physical capacity;
- `damage` — functional layers loosen or crack;
- `destroy` — controlled material failure, not an explosion.

# Part I — Warning Stone

## 4. Animation identity

The Warning Stone communicates **one named danger, one interruption, one spent
answer**.

Its moving parts are:

- three unequal lunar groove inserts;
- one removable mineral-red danger plate;
- four pressure wedges facing neighbouring cells;
- one inner listening weight beneath the top plate.

The Stone never attacks continuously and never behaves like a turret.

## 5. `place`

1. A low pale foundation layer seats into the selected cell.
2. Four pressure wedges slide outward one at a time and stop at different local
   seams rather than forming perfect symmetry.
3. The main warning block settles onto the foundation.
4. Three lunar inserts are pressed into their unequal grooves.
5. The red danger plate remains face down until configuration.

The completed object must feel embedded in the road margin rather than dropped
onto it.

## 6. `idle`

The inner listening weight makes one restrained movement every few seconds.
Only the nearest pressure wedge responds. The other wedges remain still.

This loop shows that the Stone listens locally. It must not pulse in a regular
magical rhythm.

## 7. `configure`

The player selects one of four dangers. The same red plate is physically seated
in one of four differently shaped positions:

- raid: plate aligned toward the protected building attachment;
- Grey capture: plate crosses the owner-facing wedge;
- tunnelling: plate seats over the central pressure slot;
- summoning or copied route: plate bridges two outward wedges.

The building does not change colour or grow a new icon-only effect. Its chosen
responsibility is readable from the plate's position.

### Detection — Hidden Passage

Independently of the selected one-use danger, the four pressure wedges compare
road disturbance with the three lunar grooves. An invisible enemy crossing the
Stone's small listening radius becomes revealed to nearby towers for a short
interval.

- this detection deals no damage and does not spend the red danger plate;
- repeated invisible enemies must each cross the listening radius;
- the Stone does not reveal the whole Road or the entire wave;
- a revealed trace is shown by one wedge pointing to a displaced lunar insert;
- the function applies to ground, air or otherwise hidden movement only when its
  route produces a declared pressure or bearing mismatch.

## 8. `prepared`

If Spas correctly forecast the Road:

1. the relevant wedge is already depressed before the wave starts;
2. the inner weight rests against that wedge rather than at centre;
3. the red plate is raised by one cardboard layer;
4. the other three wedges remain available as evidence but do not animate.

Prepared state is tension held in a physical mechanism, not a glow.

## 9. `trigger`

When the named hostile action begins within range:

1. the corresponding pressure wedge snaps inward;
2. the inner weight strikes the underside of the warning block;
3. the three lunar inserts shift out of alignment in a short sequence;
4. the red plate flips from its named side to its spent side;
5. a low physical interruption line travels through ground seams toward the
   enemy group;
6. the enemy's prepared attachment opens or drops before its action resolves;
7. nearby friendly buildings show their own shortened preparation response.

There is no damage projectile. The Stone interrupts preparation and leaves the
enemy group visibly recovering.

## 10. `spent` and wrong forecast

### Spent

- red plate lies face down in the centre;
- inner weight hangs below its working height;
- all four wedges remain extended but unresponsive;
- lunar inserts stay slightly misaligned until the next wave.

### Wrong forecast

If an unselected danger passes through the area, only the physically relevant
wedge moves. The red plate and inner weight do not answer. This small failed
reading must be visible, but the Stone performs no dramatic failure animation.

## 11. `reset`, `upgrade`, `damage`, `destroy`

### Reset

Between waves, the inner weight rises, lunar inserts return in reverse order and
the red plate becomes available for a new named danger.

### Upgrade

- level 2 adds an outer set of smaller listening wedges;
- level 3 adds a second plate socket, while only one inner weight remains.

The upgrade must never imply two interruptions in one wave.

### Damage and destroy

Damage loosens one wedge and cracks one lunar insert. Destruction drops the main
block onto its foundation, ejects the spent plate a short distance and leaves
the embedded wedges behind. Nothing explodes.

# Part II — Riphean Passage Yard

## 12. Animation identity

The Yard communicates **registration, difficult removal, stored responsibility
and costly return**.

Its moving parts are:

- receiving recess;
- departure recess;
- four heavy stone rollers;
- multiple ochre route strips;
- owner and level plates borrowed from the registered building;
- reserve clamps showing whether the Yard is empty or occupied.

It is a migration platform, not a portal or railway station.

## 13. `place` and `idle`

### Place

1. Two unequal platform halves slide together across the cell.
2. Four rollers are inserted from alternating sides.
3. Receiving and departure recesses open and close once to prove separation.
4. Ochre route strips are laid manually between the recesses.
5. Reserve clamps remain open, showing that no building is registered.

### Idle

One roller turns only enough to take slack from a route strip. Empty clamps make
the unoccupied state readable from above.

## 14. `register`

1. One ochre strip extends physically from the Yard toward the selected friendly
   building.
2. The registered building releases a duplicate owner plate and level plate.
3. Both plates travel along the strip and lock into separate Yard sockets.
4. The receiving recess rotates toward the registered footprint.
5. Reserve clamps close halfway but remain visibly empty.

Registration does not move, copy or shrink the protected building.

## 15. Voluntary evacuation

1. The Yard's four rollers begin turning in an uneven heavy sequence.
2. The route strip becomes taut between Yard and ward.
3. The ward stops functioning and returns loose active parts to neutral.
4. Its owner, level and surviving functional layers detach in a controlled order.
5. Those layers travel as flat labelled pieces along the route strip.
6. The original cell retains its damaged foundation and departure scar.
7. The pieces enter the receiving recess and settle into the reserve clamps.
8. The Yard closes around them and changes to `occupied`.

The building is not miniaturised into a glowing token. Its identity is preserved
as a visible stack of owned layers.

## 16. Emergency evacuation

Emergency activation uses the same physical process with less preparation:

- all four rollers engage at once and slip under load;
- the route strip pulls at an unstable angle;
- damaged pieces arrive out of order;
- one reserve clamp closes late;
- the departure scar is wider;
- the stored stack remains visibly damaged.

This communicates that the building was saved from total loss but not restored.

## 17. Interrupted evacuation

If a raid interrupts voluntary evacuation:

1. the route strip loses tension;
2. layers already detached stop between the two owners;
3. the Yard reverses its rollers;
4. surviving pieces return to the ward in reverse order;
5. any damage taken during the attempt remains visible.

No layer disappears simply because the transfer failed.

## 18. `occupied` and re-binding

### Occupied

- reserve clamps hold a compact but recognisable stack;
- owner and level plates remain visible in separate sockets;
- route strips wrap around the storage recess;
- rollers are locked by different physical wedges.

### Re-binding after the wave

1. The player selects a valid opened cell.
2. A new ochre route is laid from the departure recess to that cell.
3. Owner plate travels first and fixes the new footprint.
4. Foundation and surviving functional layers follow in their recorded order.
5. Damage layers remain attached.
6. The level plate arrives last and locks only after the re-binding cost is paid.
7. The Yard opens its reserve clamps and returns to empty state.

The old cell keeps its departure scar for the required full wave.

## 19. `upgrade`, `damage`, `destroy`

### Upgrade

- level 2 adds broader roller sleeves and a second route-strip drum;
- level 3 adds one narrow witness-layer rack beside the main reserve, not a
  second building bay.

### Damage and destroy

Damage chips roller edges and loosens a route strip without erasing stored
identity. If an empty Yard is destroyed, its platform halves separate and the
rollers settle into their sockets. If an occupied Yard can be destroyed by the
final rules, the stored owned layers must be deposited visibly on the cell for
recovery; they may never vanish in debris.

# Part III — Observatory of Three Moons

## 20. Animation identity

The Observatory communicates **six independent observations becoming a
temporary, revisable plan**.

Its moving parts are:

- large Fatta ring;
- small dense Lelya ring;
- silver Mesyats arc;
- central Midgard plumb;
- six non-identical record leaves in separate sockets;
- six physical input paths from neighbouring building families.

The rings never spin continuously like a fantasy orrery.

## 21. `place` and neutral `idle`

### Place

1. A low circular platform is assembled from four unequal Daariyan sections.
2. The Midgard plumb is fixed at the actual centre.
3. Fatta, Lelya and Mesyats elements are installed separately.
4. Six record leaves enter six visibly different sockets.
5. All input paths end before the platform until evidence is supplied.

### Idle

Only one celestial element moves during an idle loop. The plumb answers with a
small delayed correction. Record leaves remain physically independent.

## 22. Receiving observations

Each distinct nearby building family sends one differently constructed evidence
piece along its own input path. The six accepted types remain visually separate:

1. Road direction — forked route piece;
2. ground pressure — weighted wedge;
3. owner or provenance — owner plate;
4. copied transmission — duplicated strip with visible join;
5. incomplete name — open-ended attachment;
6. captured machine layer — foreign plate still fixed to its original base.

Repeated evidence from the same family enters the same socket and does not open
a new one.

## 23. `prepared`

When Spas's passive correctly identifies the Road:

- the relevant input path is already connected;
- one record leaf rests face up;
- the Midgard plumb leans slightly toward that Road;
- the three lunar elements remain uncommitted until independent evidence arrives.

## 24. Three-source convergence

1. Three different evidence sockets close in their own rhythms.
2. Their record leaves move beside the central plumb without stacking.
3. The three lunar elements align briefly, each at a different angle.
4. One physical route plan unfolds from the platform toward nearby buildings.
5. Those buildings enter preparation earlier.
6. After their next committed action, the plan retracts and the three leaves
   return to their original sockets.

The Observatory provides coordination, not damage or a universal buff aura.

## 25. Five- or six-source interruption

1. Five distinct sockets close; the sixth may remain visibly unresolved.
2. The Midgard plumb drops one layer into its commitment recess.
3. All agreeing leaves form an incomplete ring around it.
4. At the moment the hostile special action commits, the physical plan line
   reaches its imposed attachment.
5. That attachment is held open or detached before completing its action.
6. The exposed layer remains beside its owner long enough for other buildings
   to answer it.
7. All lunar elements separate immediately after the interruption.

There is no blast, stun dome or automatic destruction of the enemy.

## 26. False consensus and disputed forecast

If most inputs come from identical or Grey-captured sources:

1. duplicated pieces arrive at several sockets;
2. their identical joins become visible;
3. the Lelya ring attempts to align before the other two elements;
4. the Midgard plumb refuses to enter its commitment recess;
5. a mineral-red disputed leaf is placed across, but not inside, the central
   arrangement;
6. all preparation and interruption effects are withheld.

The animation rewards refusal to commit. It must not look like a malfunction.

## 27. `resolve`, `reset`, `upgrade`

### Resolve and reset

Evidence returns to its supplying building family in reverse order. The plan
line retracts, the plumb rises and all six sockets reopen. No record leaf merges
with another.

### Upgrade

- level 2 adds distinct bearing supports that allow agreement from three sources;
- level 3 deepens the commitment recess and adds two exposed-layer holding arms
  required for five/six-source interruption.

No upgrade adds a weapon, telescope barrel or additional moon.

## 28. `damage` and `destroy`

Damage shifts one ring off its reference mark and cracks one empty socket. The
Observatory remains readable as impaired rather than simply darker.

On destruction:

1. the Midgard plumb drops into the platform;
2. the small Lelya ring separates first;
3. Fatta ring opens at one repaired joint;
4. Mesyats arc settles across two platform sections;
5. all six record leaves remain individually visible around the ruin.

## 29. Separation test

The three buildings pass only if their active silhouettes cannot be confused:

- Warning Stone: one low block, inward wedge and flipping danger plate;
- Passage Yard: long route strip, four rollers and stored owned layers;
- Observatory: three unequal celestial elements and six independent evidence
  paths.

## 30. Review decisions

1. Approve the Warning Stone as a one-use physical warning mechanism?
2. Approve the Passage Yard evacuation as visible transfer of owned layers,
   without portal or miniaturisation?
3. Approve the Observatory convergence as physical comparison of six evidence
   types?
4. Should any of the three building animations be simplified before timing and
   atlas planning?

# Ether Frontier — World, Heroes, Buildings and Enemies Production Bible v1

Status: **rejected draft; not canon and not a production source**  
Updated: 2026-07-26

## 1. Purpose

This rejected draft attempted to define the external appearance, abilities and
animation families of the world, three playable heroes, seven core buildings,
twenty standard enemy handles and six bosses.

It was rejected because it combined too many approval stages. Nothing in this
file supersedes an approved source. It may be mined only after the user reviews
the corresponding subject separately.

No image generation is authorised by this document alone. Each family must
later receive a separate source-call prompt and atlas plan.

## 2. Non-negotiable presentation

- gameplay assets use exact true top-down orthographic 90-degree projection;
- premium smooth solid punchboard and matte printed paper, never corrugated;
- every moving child has a complete die-cut perimeter and its own attachment;
- silhouettes remain readable at mobile scale;
- no facade, horizon, isometric tilt or cinematic perspective in runtime art;
- no generic medieval weapons, spell crystals, fantasy classes or glossy
  science-fiction machinery;
- no pseudo-runes, copied sacred signs, supremacist symbols or racial coding;
- damage changes assembly state: it never merely adds a red glow;
- captured state adds removable Grey layers without recolouring the source
  object into an unrelated design.

## 3. Material logic of the world

The world is not scenery painted beneath sprites. It is a layered historical
machine whose materials show who built, repaired, renamed and buried each
part.

### Primary layers

| Layer | Material | Meaning | Motion |
|---|---|---|---|
| living ground | green fibre card, bark paper, felt moisture | growth and obligation | breath, swell, regrow |
| pressure ground | blue-grey stone card, chalk seams | load and earlier routes | settle, crack, reseat |
| Road | warm ochre paper strips | currently recognised passage | flex, fork, close |
| water route | dark turquoise and silver-paper channels | exchange and older passage | fill, divide, drain |
| witness layer | ivory cards with visible handwriting differences | attributed memory | attach, dispute, return |
| cosmic layer | dark indigo nested discs and metallic route strips | Moon Cards and Golden Path | rotate, align, shear |
| Grey correction | ash-lilac duplicate plates | imposed sameness | copy, cover, erase, peel |

## 4. The Last Knot battlefield

### Overall silhouette

One vertical handmade game board with two northern entry mouths, two Roads that
join and separate, and a low circular Knot near the lower centre. The board is
asymmetrical because every historical repair follows a different cause.

### Historical strata

1. serpent pressure channels below the visible surface;
2. Daariyan orientation bed;
3. Antlan copper-water repairs;
4. later timber and stone settlements;
5. modern Road cards;
6. temporary Grey correction plates.

The strata must not look like one civilisation's decorative theme.

### Board animation states

- `board_neutral`: quiet fibre movement, slow water glint, stable Roads;
- `road_forecast`: next fork lifts one edge and exposes its bearing tab;
- `pulse_open`: entry mouth separates into layered interval cards;
- `road_split`: second Road unfolds without changing the underlying board;
- `dual_pressure`: both routes flex independently, never mirror perfectly;
- `grey_capture`: pale plates spread only along recognised connections;
- `revocation`: owner tabs retract, stopping capture propagation;
- `board_damage_1..3`: name tabs disappear and seams widen;
- `board_failure`: Roads lose distinction and flatten into one pale strip;
- `board_restored`: differences return; scars remain visible.

## 5. World regions for narrative concepts

### Daariya

Circular polar continent cut by four water-pressure routes. White is used only
for snow and blank material, never racial purity. Settlements are low ring
assemblies, climate terraces and route docks. Three moons have distinct card
mechanisms and periods.

Animation language: orbital drift, water balance, slow pressure breathing,
evacuation strips extending south, moon layers shearing during Lelya's fall.

### Asgard Iriysky

Accumulated civic exchange at two waterways: date wheels, landing court,
markets and inspection tables. No golden imperial palace and no generic
pseudo-Slavic temple skyline.

Animation language: bridges rotate between calendars; courier tabs arrive;
founding dates disagree visibly without the city collapsing.

### Lelya

Small inhabited utility moon: reservoir rings, worker chambers, continuity
eggs and a central passage anchor. It must appear valuable and lived-in before
militarisation.

Animation language: reservoir circulation, civilian lights, quarantine plates,
conflicting command layers, final spatial separation rather than explosion.

### Antlan

Seven asymmetric island rings joined by copper memory channels, tide locks and
floating witness courts. It is neither Greek Atlantis nor crystal fantasy.

Animation language: tides pass between rings, testimony cards circulate,
emergency gates override civic routes, rings fail sequentially during drowning.

### Fatta

Scarred imported moon built from Deya material and thirteen route stations.
It appears repaired many times, with no perfect radial symmetry.

Animation language: counterweight motion, three conflicting command plates,
anchor strain, layer separation and partial loss into Interworld.

### Mara's Limit

Finished edges, winter fibre, berry-black absence and closure thread. It is not
a gothic death realm. Nothing loops here.

Animation language: slow closure, clean severance, material return and complete
stillness.

### Peklo and Grey Interval

Too many incompatible spaces compressed into too little card depth. Repeated
layers almost align but expose small gaps. Avoid hell imagery.

Animation language: copy, offset, search for a stable outline, temporarily
inhabit it, detach when provenance is restored.

## 6. Universal animation contract

### Buildings

Every building family requires:

- `neutral`, minimum 4-frame living loop;
- `listen`, 3–5 frames;
- `prepare`, 4–6 frames;
- `commit`, 4–8 frames;
- `resolve`, 3–6 frames;
- `interrupted`, 2–4 frames plus hold;
- `captured`, neutral loop with owner tab absent and Grey overlays separate;
- `revoked`, function children returned but base intact;
- `destroyed`, 6–10 frames of material-specific separation;
- optional directional child rotations stored as manifest transforms.

### Heroes

Every hero requires six plan-view directions where bodily orientation matters:

- `manifest`, `idle`, `move`, `listen`, `prepare`, `commit`, `resolve`,
  `interrupted`, `exhausted`, `return_to_knot`;
- no baked shadow movement that changes footprint;
- held tools and emitted pieces remain separate layers;
- hero never uses a generic repeated melee attack as primary action.

### Enemies

Every standard enemy requires:

- `emerge`, `move`, `route_turn`, `ability_prepare`, `ability_commit`,
  `ability_resolve`, `hit`, `layer_lost`, `interrupted`, `breach`, `release`;
- six plan-view directions for ground or directional air movement;
- owner/imposed layers separated for units that may be freed;
- `release` replaces generic death where the carrier survives categorisation;
- destructive death is reserved for forms that cannot be safely unbound.

## 7. Hero — Borislav, Keeper of Revocable Accord

### Readable identity

Broad, low centre of gravity, warm ochre-red field coat and three oversized
copper Answer plates carried on separate shoulder rails. His alignment mallet
is a practical seating tool, not a war hammer. No knight armour or shield.

### Personality

Decisive, dependable and tempted to confuse agreement with obedience. He looks
like someone who physically joins a crew's work rather than commands from a
throne.

### Primary ability — Threefold Answer

Borislav lends one plate to each of three different nearby Circle objects. If
all three independently reach `prepare`, their plates align and cancel one
hostile committed action. If one object is captured, Borislav revokes the
other plates before the Editor can copy the agreement.

### Passive — Accountable Service

Completed waves return a small extra Zlato payment only when no borrowed plate
was lost. This replaces an unconditional command-income fantasy.

### Animation family

- `manifest`: three copper plates arrive first; Borislav locks into them;
- `idle`: checks plate cords in a slow unequal sequence;
- `move`: broad four-step cycle, plates lag independently;
- `listen`: seats mallet head against ground and feels synchronisation;
- `lend_left/right/front`: removes and slides one plate toward its socket;
- `prepare`: braces empty shoulder rails and pulls return cords taut;
- `commit`: three remote cords snap into one triangular answer;
- `resolve`: interruption tab releases; plates recoil separately;
- `revoke`: cuts alignment with mallet handle, returns all plates early;
- `interrupted`: one cord tangles; he manually frees it;
- `exhausted`: shoulders lowered, all plate sockets empty;
- `return_to_knot`: folds rails inward and is pulled into the Answer ring.

## 8. Hero — Ayana, Reader of Compared Layers

### Readable identity

Tall but compact indigo field coat with large hinged comparison windows,
ivory provenance cards and water-silver measuring strips. Her hands remain
visible. No staff, wizard robe, spellbook or floating crystal.

### Personality

Precise, curious and initially convinced that enough measurement can eliminate
interpretation. Her warmth appears when she admits a limit clearly.

### Primary ability — Field of Sources

Ayana opens a comparison field. Every copied movement step must reveal its
source layer before continuing, delaying Grey carriers. Captured objects expose
their original owner layer for selection and possible release.

### Passive — Measured Yield

Worksites produce more only while their origin and return dates remain attached.
Grey-captured or provenance-less worksites receive no bonus.

### Animation family

- `manifest`: four comparison windows unfold around an empty centre;
- `idle`: sorts cards, occasionally returns one to an earlier position;
- `move`: windows fold close to body; silver strips trail with mild delay;
- `listen`: places two non-identical samples side by side;
- `prepare`: opens windows in opposing pairs, never one magical radial bloom;
- `commit`: source strips extend from field to selected copied steps;
- `select_layer`: lifts one imposed plate and pins the original below;
- `dispute`: rotates a confidence tab from known to disputed;
- `resolve`: strips roll back and cards retain new attribution;
- `interrupted`: one window closes on the wrong layer; Ayana reopens it;
- `exhausted`: sits inside the folded frame, continuing to annotate;
- `return_to_knot`: windows stack into one attributed packet.

## 9. Hero — Amba, Keeper of Witnessed Passage

### Readable identity

Lean pine-and-berry route worker with witness pegs, flexible path ribbons and a
curved tension tool used to seat them. No bow, quiver, animal trophy or hunter
costume.

### Personality

Economical and observant. She distrusts central maps but learns that a local
route still owes a public account to everyone it affects.

### Primary ability — Witnessed Detour

Amba lays a temporary route across damaged cells. Each crossing unit reveals
the obligation that brought it to the Road: debt, copied instruction, missing
name or voluntary oath. The revealed obligation lets the matching Circle
interact more effectively.

### Passive — First Footprint

The first object bound on a newly opened cell gains a temporary route witness,
not bonus damage. If sold or captured, the witness returns to Amba.

### Animation family

- `manifest`: pegs strike separately, then ribbon draws her outline between;
- `idle`: tests tension and reads dust orientation;
- `move`: short quick steps; peg bundle remains on its own pivot;
- `listen`: lays one loose ribbon and watches its curve;
- `prepare`: seats first and second pegs with curved tool;
- `commit`: runs ribbon through the path, changing direction at each witness;
- `crossing_reveal`: obligation tab flips from underside of ribbon;
- `retrieve`: releases pegs in reverse order and rolls ribbon by hand;
- `interrupted`: broken peg leaves a visible scar tab;
- `exhausted`: kneels beside empty peg loops;
- `return_to_knot`: retrieves final route instead of disappearing abruptly.

## 10. Building — Wind Route Table (`watchtower`)

Silhouette: low asymmetric table, four unequal vanes, removable fork card and
long tension ribbons. Sky-blue and silver accents over a quiet stone base.

Ability: samples the next movement choice and rotates a temporary route fork,
redirecting or delaying a limited group. It affects decisions, not health.

Revocation: the fork returns when its witnessed group passes or provenance is
lost.

Key animations: vane sampling; independent bearing search; fork lift; 45/90/180
degree fork rotation; route-tab handoff; ribbon tension; resolved return;
captured identical-vane loop; ribbon snap destruction.

Forbidden: crossbow, bolt, targeting reticle, ammunition or attack recoil.

## 11. Building — Root Return Nursery (`sawmill`)

Silhouette: open graft table around a living cell, three large root loops, seed
cards, felt moisture pad and permanent scar ledger.

Ability: restores an exhausted resource cell or grows a temporary binding root
across one Road segment. Regrown material retains a visible graft scar and
cannot be duplicated as pristine.

Revocation: temporary root withdraws after its obligation is satisfied.

Key animations: seed selection; moisture fill; root extension in separate
segments; take-hold squeeze; scar recording; gradual five-stage regrowth;
root release; dry interrupted state; Grey copy producing root without scar;
fibre separation destruction.

Forbidden: saw, mill, logs, frost, thorn ammunition or industrial harvesting.

## 12. Building — Stone Load Chorus (`quarry`)

Silhouette: broad open ring of non-identical slabs, three counterweights,
visible load cords and low pressure seats.

Ability: anchors a cell and redistributes load from a heavy or captured carrier
until one detachable layer becomes exposed. It does not shoot or mine.

Revocation: releasing the anchor returns stored pressure to the ground slowly.

Key animations: slab listening; sequential weight lift; cords tension by load
direction; ring settle; pressure transfer; target layer lift; overload crack;
manual reseat; captured equal-weight deadlock; slab-and-cord separation.

Forbidden: quarry pit, derrick, lightning, boulder attack or artillery.

## 13. Building — Water Exchange Weir (`palisade`)

Silhouette: shallow open-centre channels, two exchange cups, silver flow strips
and paired return gates. Dark turquoise, river blue and pearl grey.

Ability: divides movement into a delayed step and a returned step. It may also
wash one imposed layer from a nearby friendly object into a recoverable holding
cup.

Revocation: water drains and all held layers must be returned or attributed.

Key animations: channel fill; cup counterbalance; gate choice; flow division;
delayed-step hold; washed-layer float; return pour; drying loop; captured
one-way flow; channel delamination destruction.

Forbidden: wall, stakes, thorns, poison, ice or projectile trap.

## 14. Building — Name Witness Table (`obelisk`)

Silhouette: low indigo-ivory table around a conspicuous absent centre,
non-identical provenance tabs, owner sockets, dispute clips and one long
revocation thread.

Ability: identifies who owns an action, prevents duplication and releases a
captured object after two independent witnesses agree.

Revocation: any owner may pull the thread; the granted action ends instead of
passing to a copier.

Key animations: tab arrival; handwriting comparison; owner socket test;
dispute clips oppose; witness agreement; owner tab return; full revocation;
captured absent owner plus pale substitute; thread cut; orderly table breakup.

Forbidden: monument, magic obelisk, void bolt, rune stone or archive stamp.

## 15. Building — Sun Comparison Measure (`beacon`)

Silhouette: low amber surface with four independent shutters, large colour
samples, exposure cards and peel tabs.

Ability: reveals the separation between original colour/material and imposed
Grey directive. Temporarily restores one overwritten function.

Revocation: shutters close before exposure burns a provisional reading into the
object.

Key animations: shutter sequence; sample alignment; warm exposure sweep;
directive edge lift; peel and fold; original-colour return; overexposure
warning; captured shutters opening identically; amber-card separation.

Forbidden: lighthouse, holy shrine, anti-air beam, solar projectile or crystal.

## 16. Building — Thunder Answer Drum (`cannon` branch handle)

Silhouette: low ring of differently sized contact drums, timed clappers and
three removable copper bridges. Burgundy, copper and storm blue.

Ability: stores contributions from different Circles. When timings align, it
interrupts one hostile committed action. Repetition from identical copied
sources never counts as independent agreement.

Revocation: removing any bridge cancels the stored answer safely.

Key animations: individual contribution taps; bridge placement; asynchronous
clapper search; shared strike; interruption token release; copper cooling;
failed false consensus; bridge revoke; captured metronomic loop; ring opening
and bridge fall destruction.

Forbidden: cannon, barrel, shell, explosion, lightning strike or solitary
trigger.

## 17. Enemy material families

### Lower Passage

Warm clay, water-dark fibre, shed-scale treaty cards and pressure stone. Damage
reveals obligations and house colours; it never reveals a generic reptile body
beneath clothing.

### Nav

Translucent smoke paper, oxidised green edges, torn name scraps and absent
centres. Movement looks unfinished rather than ghostly floating.

### Grey correction

Pale lilac, ash, cold cyan and repeated white closures. All apparent uniformity
comes from added directive pieces over varied carriers.

### Captured machines

Warm colourful civic chassis visibly survives beneath removable pale command
plates. Their release animation restores function ownership rather than merely
changing team colour.

## 18. Standard enemy roster

Each row owns a distinct relationship, ability, silhouette and animation hook.

| ID / name | Appearance and silhouette | Ability | Signature animations |
|---|---|---|---|
| `fast` Depth Runner | tiny clay route body, four long pressure-feelers and one debt tab | reads weak load seams and accelerates through an unanchored fork | feelers sample; low sprint; debt tab reveal; stumble when Stone reseats route |
| `warrior` Scale Retainer | compact two-layer carrier with one large coloured oath plate | shares route stability with the next retainer while plates match | oath plate lock; paired march; plate disagreement; voluntary release |
| `brute` Clay Bearer | broad stacked clay masses around flexible timber brace | carries accumulated pressure, resisting redirection until load is exposed | weight gather; brace compress; heavy settle; outer mass shed rather than rage |
| `raider` Name Hook | narrow asymmetric body with oversized separate hook and blank tab roll | leaves Road briefly to remove owner tabs from buildings | hook unfold; roadside lunge; tab pull; roll storage; dropped-tab recovery |
| `witch_doc` Grey Instructor | visibly local carrier under a fan of identical pale lesson cards | copies one nearby imposed category onto another unit | observe; select card; duplicate; attach; cards scatter when Sun exposes source |
| `slime` Nav Dew | shallow translucent pools connected by incomplete edge strips | occupies gaps between steps and slows return of revoked pieces | droplets seek outline; pool join; cling; owner name condenses; clean evaporation release |
| `berserker` Red Crest | lean carrier whose oath crest adds layers as commands repeat | gains speed when the same order is issued again; weakens when orders differ | crest stack; forced sprint; conflicting-order wobble; crest peel |
| `shield` Shell Keeper | small route keeper under one huge independent pressure shell | takes load for units behind it until Stone redirects the obligation | shell lower; group shelter; pressure cracks; body steps free after shell release |
| `tunneler` Pressure Digger | flat wedge silhouette, paired digging cards and soil cap | enters an existing lower route and emerges beside a named structure | seam listen; cards alternate; cap closes; underground marker; debris-ring emergence |
| `necro` Caller of Missing Names | open-centre witness frame pulling torn Nav tabs on threads | assigns a convenient false name to an unfinished form, summoning it to Road | thread cast; name approximation; form assemble; false tab cut by Name Table |
| `bomber` Grey Vessel | folded pale air carrier around detachable sealed correction packet | delivers a directive packet to a building; does not use explosive ordnance | wings refold for turns; packet arm; dive; plate spread; empty vessel unfold-release |
| `spellbreak` Answer Silencer | broken copper response ring carried horizontally | desynchronises nearby Circle contributions by inserting one repeated false beat | listen; false clapper extend; mute pulse as paper compression; ring fracture |
| `spider` Thread Rider | eight independent pressure legs around ownerless spool | connects two structures so capture on one propagates to the other | alternating four-leg gait; spool rotate; bridge thread lay; thread sever recoil |
| `summoner` Interval Opener | mobile rectangular tear frame with folded blank cards inside | opens a brief copied route that emits one carrier shell | frame plant; corners pull apart; blank fold emerges; route snaps closed |
| `golem` Barrow Form | mound of non-identical witness stones around an empty name socket | absorbs detached historical layers and becomes heavier but less steerable | stone collect; socket remain empty; gait reseat; overload collapse; stones return to sites |
| `air` Winged Scale Scout | warm-clay plan-view glider with two independent membrane cards | follows old sky bearings that ignore current ground forks | wing flex; tail bearing read; bank via layer rotation; landing oath reveal |
| `wraith` Unremembered | absent centre surrounded by drifting name scraps and two direction fins | crosses toward the strongest unused name and steals it to complete itself | scraps orbit; name sense; rapid glide; temporary centre form; Mara closure |
| `scout` Empty-Sky Observer *(planned)* | tiny ash carrier with one off-centre lens and erased route card | marks the least witnessed path for later Grey copies | lens sweep; card erase; mark drop; observed-by-Sun lens shutter |
| `machine` Captured Craft | colourful Antlan/Daariyan civic chassis beneath one pale owner plate | performs its old useful operation as a forced raid against current owner | original idle under plate; directive clamp; tool misuse; plate lift; owner restart |
| `iron_jug` Directive Shell | thick walking shell made from many identical blank plates around hidden chassis | replaces lost outer plates with nearby copied layers until Name revokes supply | plate march; damaged plate eject; copy receive; inner chassis glimpse; total shell unstack |

## 19. Standard enemy release rules

- Lower Passage units may retreat, renegotiate or shed an imposed oath.
- Nav forms may complete, return a borrowed name or pass to Mara.
- Grey operators lose coherence when their repeated source is exposed.
- captured machines retain a recoverable chassis unless explicitly destroyed
  by overload;
- no freed unit instantly becomes a permanent player soldier by colour swap;
- each `release` state has a distinct owner-return piece for codex readability.

## 20. Boss — Voivode of the Red Plate (`miniBossGround`)

Silhouette: broad Lower Passage commander with one enormous red oath plate,
three contradictory treaty leaves and a compact pressure staff used for route
signals, not combat.

Ability: cycles between three debt readings. Each reading protects a different
escort relationship. The correct counter is to expose contradictions, forcing
the plate to detach between readings.

Animation phases: treaty leaves rotate; oath plate locks; signal staff seats;
escort formation tightens; contradiction clips appear; plate tears at stitch;
unarmoured parley hold; destructive release only if obligation is ignored.

## 21. Boss — Prince of the Lower Covenant (`bossGround`)

Silhouette: massive pressure armour assembled from distinct Naga, Deep Scale
and Fleet contract layers around a visibly smaller mediator body.

Ability: opens the suppressed second Road and transfers damage/load into the
old underground covenant. Overuse wakes deeper infrastructure.

Animation phases: pressure map unfold; armour layers settle by house; second
Road lift; debt transfer cords; omitted clause reveal; universal lizard overlay
peel; mediator emerges; armour returns to separate owners.

## 22. Boss — Three-Command Keeper of Fatta (`bossAir`)

Silhouette: orbital plan-view keeper with three independent command heads,
unequal wing-counterweights and a scarred Fatta centre plate.

Ability: executes League, Keeper and continental commands. Each grants a useful
movement correction; simultaneous commitment creates a catastrophic dash and
route shear.

Animation phases: heads wake separately; each reads its card; one/two-command
stable orbits; three-command strain; counterweights oppose; Fatta plate crack;
command bridges interrupted; keeper disengages into three accountable records.

## 23. Boss — Engine of the Empty Name (`bossMachine`)

Silhouette: absent central hub surrounded by recognisable but ownerless pieces
copied from all seven buildings. No single weapon or face.

Ability phases:

1. copies one valid function;
2. removes its provenance and cost;
3. applies it universally;
4. labels resistant objects as enemies;
5. attempts to merge both Roads.

Animation phases: empty hub measures; child copy arrives; owner socket seals;
seven fragments orbit; universal alignment becomes unnaturally symmetrical;
Road merge strips extend; player revocation pulls fragments away; hub collapses
because nothing owns its centre.

## 24. Boss — Grey Conductor (`dread_lord`)

Silhouette: restrained, almost ordinary carrier surrounded by separate editing
tools—quotation arms, confidence clamps, category bridges and a pale chorus of
duplicate cards. It must not resemble a racialised alien sovereign.

Ability: assembles an authoritative command entirely from true quotations whose
original contexts disagree. Units obey because every fragment is authentic.

Animation phases: collect quotation; crop edges; remove authors; align chorus;
conduct repeated sentence; source cards restored out of sequence; carrier
revealed as replaceable; distributed voice dissipates.

## 25. Boss — Awakened World Serpent (`elder_dragon`)

Silhouette: enormous segmented plan-view pressure-and-water infrastructure,
each body section built in a different historical material. It is not a winged
dragon and not inherently hostile.

Ability: responds to accumulated subterranean load by crossing both Roads and
reseating whole board sections. Towers on ignored debt cells become unstable;
honoured covenant cells remain safe.

Animation phases: underground segment shadows; sequential surface emergence;
water-route flex; old repair layers awaken; board-scale coil; load discharge;
covenant recognition; segments return below leaving changed terrain seams.

## 26. Boss production scale rules

- bosses may exceed a normal cell but keep exact top-down footprint metadata;
- every phase change swaps or moves physical children, never only colour;
- boss weak points are relationship pieces: oath, clause, command bridge,
  owner socket, quotation crop or load debt;
- all boss source art must show neutral, each phase, interrupted, resolved and
  destroyed/released states separately;
- no boss may visually imply that an entire fictional people is biologically
  monstrous.

## 27. Effect ownership

| Effect | Owner atlas | Physical form |
|---|---|---|
| route redirection | Wind Table | fork card and tension ribbon |
| regrowth | Root Nursery | segmented root and scar tab |
| exposed load | Stone Chorus | lifted layer and load cord |
| delayed/returned step | Water Weir | silver flow strip and exchange cup |
| provenance return | Name Table | owner tab and revocation thread |
| directive exposure | Sun Measure | shutter light card and peel tab |
| interruption | Thunder Drum | copper bridge and answer token |
| Grey capture | capturing enemy | pale directive overlay |
| Nav completion | affected Nav unit | returned-name or closure piece |
| serpent pressure | Lower Passage unit | dust, water and debt card |

No generic shared magic VFX library may replace these owner-specific pieces.

## 28. Concept-art separation

Future generation must be split into separate calls and review families:

1. world regions and battlefield;
2. Borislav;
3. Ayana;
4. Amba;
5. one call per building family;
6. one call per standard enemy family or carefully bounded unit;
7. one call per boss.

Never request heroes, enemies and buildings on one sheet. Never ask one image
to establish both narrative perspective art and exact runtime projection.

## 29. Acceptance checklist

An object is ready for prompt extraction only when:

- its lore action precedes appearance;
- ability changes a relationship, not merely health;
- silhouette differs from every other family;
- every moving child has an owner and pivot;
- neutral, prepare, commit, resolve, interrupted, captured and release/destroy
  states are described;
- exact 90-degree gameplay projection is preserved;
- forbidden inherited shapes are explicit;
- faction material does not encode real race or religion;
- the animation can be expressed in one-object-family atlas under 5 MB.

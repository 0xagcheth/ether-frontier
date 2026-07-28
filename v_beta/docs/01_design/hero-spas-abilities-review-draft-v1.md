# Ether Frontier — Hero Review Draft: Spas Abilities v1

Status: **rejected draft; not canon**  
Updated: 2026-07-26

## Review scope

This rejected draft used the wrong hero structure: several active abilities and
a hero resource. The approved project pattern is one passive ability and three
hero-specific buildings. Nothing in this file is a production source.

Already approved and unchanged:

- Spas is a title, not a personal name;
- age 55–60;
- Daariyan lunar surveyor and Keeper of Imminent Passage;
- four-part stone mantle;
- Three-Moon Measure;
- central flaw: a correct forecast tempts him to decide for others.

This draft does not approve animation, visual effects, numerical balance,
runtime implementation or concept-art prompts.

## 1. Gameplay role

**Spas is a forecast and evacuation hero.**

He does not deal direct damage. His value comes from:

- revealing danger before it becomes fully visible;
- preparing one part of the battlefield for a predicted event;
- saving a building from an announced loss;
- creating an organised retreat when the defence line fails;
- distinguishing a confident prediction from certain knowledge.

He is strongest for a player who reads the next wave and prepares early. He is
weaker when summoned only after enemies have already reached the Knot.

## 2. Unique resource — Trust

Spas uses **Trust**, shown as six separate forecast leaves attached to the
Three-Moon Measure.

- maximum: 6 Trust;
- begins each wave with 3;
- gains 1 when an announced forecast proves correct;
- loses 2 when a marked danger does not occur within its predicted interval;
- cannot spend Trust that has not been earned;
- Trust never represents mystical energy—it represents how many communities
  are willing to act on his next warning.

At zero Trust, Spas remains present but cannot order evacuation. He can rebuild
Trust by making smaller verifiable forecasts.

### Why this matters

The mechanic expresses his character conflict. Being correct grants real
authority, but authority is limited, measurable and revocable.

## 3. Passive ability — Measure of Three Moons

Before each wave, Spas reveals three pieces of information:

1. the first active Road;
2. the dominant relationship of the wave—pressure, copied directive, missing
   name or captured machine;
3. one uncertain warning that may or may not occur.

The third warning is explicitly marked with confidence:

- probable;
- disputed;
- unknown.

The player may **accept** or **decline** the uncertain warning.

### Accept

- one affected zone is marked in advance;
- relevant structures prepare faster if the event occurs;
- Spas gains Trust when correct;
- Spas loses Trust when wrong.

### Decline

- no bonus or penalty;
- the forecast remains in the archive as unresolved rather than false.

### Design purpose

The player uses uncertainty instead of merely uncovering a perfect enemy list.
Spas is informative without becoming an automatic solution.

## 4. Active ability — Warning Stone

Cost: 1 Trust.

The player places one temporary **Warning Stone** on a buildable cell or Road
segment before the next enemy group arrives.

For a short preparation interval, the Stone listens for the predicted event.

If the event occurs inside its area:

- nearby buildings immediately revoke exposed owner pieces before capture;
- the first hostile raid, forced movement or directive attachment is cancelled;
- the Stone records the event and returns 1 Trust.

If a different event occurs:

- the Stone does nothing;
- it remains as evidence of an incorrect local forecast;
- spent Trust is not returned.

### Restrictions

- only one Warning Stone may exist at a time;
- it cannot cancel direct ordinary movement or damage;
- it must name the expected event when placed;
- changing the expected event requires removing the Stone and spending Trust
  again.

### Character meaning

Spas protects through early, specific warning—not through a universal shield.

## 5. Active ability — Evacuation Cord

Cost: 2 Trust.

The player connects one threatened building to one valid empty cell within a
limited route distance.

For a short interval, the building prepares to move. During preparation:

- it stops performing its normal function;
- its owner and upgrade layers remain attached;
- it may still be interrupted by a raid.

If preparation completes:

- the building is rebound on the chosen cell;
- its level and ownership are preserved;
- no sell refund or rebuilding cost is triggered;
- the original cell receives a visible departure scar and cannot be reused
  immediately.

If interrupted:

- the building stays on its original cell;
- 1 of the 2 spent Trust is returned;
- it does not suffer automatic destruction.

### Restrictions

- the destination must already be legitimately opened;
- the ability cannot move the Last Knot, resource source or Road;
- captured buildings must first recover their owner;
- only one building may be in evacuation at a time;
- moving a building does not cleanse damage or reset cooldowns.

### Character meaning

This is the defining active ability. Spas saves what can still be moved, but
evacuation has time, opportunity and land costs.

## 6. Active ability — Six Disagreeing Models

Cost: no Trust; once per wave.

Spas asks up to six nearby sources to evaluate one selected enemy group or
incoming event. Each source contributes a different type of observation:

- route;
- load;
- transmission;
- material layer;
- owner;
- return state.

The ability becomes stronger through **different** sources, not repeated copies.

### One or two sources

The group receives a provisional relationship label. No control effect occurs.

### Three or four sources

One imposed layer is exposed and becomes interactable by the appropriate
building.

### Five or six sources

The selected hostile committed action is interrupted. The enemy itself is not
automatically destroyed.

### False consensus rule

Two identical or Grey-copied sources count as one. If all selected sources
derive from the same owner, the ability produces a confident but non-binding
forecast and grants no interruption.

### Character meaning

Spas is strongest when independent disagreement converges on one practical
conclusion.

## 7. Ultimate ability — The Great Passage

Cost: all current Trust, minimum 4.

The player draws one temporary passage from a threatened section of the board
toward the Last Knot or another safe junction.

For its duration:

- friendly owner pieces and released witnesses travel through it first;
- one building connected by Evacuation Cord completes its relocation faster;
- hostile units cannot enter unless their route obligation genuinely leads
  through the same passage;
- units falsely sharing a copied route are separated and delayed;
- any Bearing Name that would be erased during the passage is instead removed
  from the active Knot and placed in a recoverable evacuation reserve.

The Great Passage does not kill enemies or make the base invulnerable. It
changes what can be saved from an otherwise successful breach.

### End cost

When the Passage closes:

- Spas's Trust falls to zero;
- he cannot issue another evacuation order during the same wave;
- every evacuated Bearing Name must be returned through later successful wave
  completion;
- the route leaves a temporary scar that blocks immediate construction.

### Character meaning

This is not triumphant mass control. Spas spends all accumulated authority to
save people and records, then must earn trust again without claiming the rescue
proved every part of his forecast.

## 8. Ability relationship

The intended loop is:

1. **Measure of Three Moons** proposes a danger;
2. the player accepts or declines uncertainty;
3. **Warning Stone** protects the predicted location;
4. **Six Disagreeing Models** verifies the actual hostile relationship;
5. **Evacuation Cord** moves one irreplaceable structure before failure;
6. **The Great Passage** preserves part of the defence during a major breach;
7. Spas loses accumulated authority and must earn it again.

No ability is a reskinned attack, freeze, shield dome or healing spell.

## 9. Strengths

- exceptional preparation before complex waves;
- protects developed buildings from raids and capture;
- allows limited repositioning without rebuilding from zero;
- preserves some value during an otherwise damaging breach;
- rewards mixed Circle construction and independent information sources;
- expresses the Daariya evacuation directly through gameplay.

## 10. Weaknesses

- no direct damage;
- weak when Trust is low;
- incorrect predictions have lasting cost;
- evacuation temporarily disables the moved building;
- cannot save closed or illegitimate cells;
- ultimate recovers from failure rather than guaranteeing victory;
- requires more player attention than a passive combat hero.

## 11. Explicit exclusions

- no prophecy as perfect revelation;
- no time stop, rewind or global freeze;
- no meteor, moon strike or solar weapon;
- no generic shield charges;
- no healing aura;
- no direct melee or ranged attack;
- no automatic evacuation without player-selected origin and destination;
- no reward for treating a disputed warning as certain;
- no racial or lineage-based bonus.

## 12. Review decisions required

1. Does **Trust** fit Spas, or is it unnecessary complexity?
2. Keep **Measure of Three Moons** as a forecast containing one uncertain item?
3. Keep **Warning Stone** as specific protection against a predicted event?
4. Keep **Evacuation Cord** as his defining building-relocation ability?
5. Keep **Six Disagreeing Models**, or reduce Spas to a simpler ability set?
6. Does **The Great Passage** work as an ultimate, despite not dealing damage?

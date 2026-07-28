# Ether Frontier — Hero: Spas Passive and Buildings v1

Status: **canonical hero kit; attack revision approved 2026-07-27**  
Updated: 2026-07-27

## Approved scope

This document canonically defines exactly:

- one unique passive ability for Spas;
- one ordinary personal attack for Spas;
- three unique buildings unlocked by choosing Spas.

It does not approve animations, numerical balance, runtime code or
concept-art prompts.

Project-wide hero rule confirmed during approval: unique buildings do not have
to deal direct damage. According to the character, they may attack, strengthen
friendly structures, slow or weaken enemies, control routes, change economy or
preserve investments.

## 1. Hero structure

Choosing Spas changes the player's method of defence through preparation and
preservation.

Spas has:

- no separate active ability bar;
- no personal Trust resource;
- one repeatable lore-grounded attack, Shard of Lelya;
- one always-active forecast passive;
- three buildings purchased and placed through the normal construction system.

The three buildings form a clear progression:

1. detect the danger;
2. preserve what the danger would destroy;
3. coordinate the whole defence around a verified forecast.

## 2. Passive — Measure of Three Moons

Before every wave, Spas's Three-Moon Measure reveals:

- which Road receives the first enemy group;
- the first three enemy formations in their real order;
- one special action expected during the wave: raid, capture, summoning,
  tunnelling or false-route transition.

The special-action prediction carries one of three confidence states:

- **reliable** — confirmed by several independent records;
- **disputed** — supported by one record and contradicted by another;
- **unknown** — the Measure detects an anomaly but cannot classify it.

### Mechanical benefit

The player receives five additional seconds of preparation before the wave.

If the player places at least one Spas building on the correctly predicted
Road, that building begins the wave already prepared rather than starting from
its neutral state.

### Limitation

The passive does not reveal the entire wave, exact timings, enemy health or
boss phases. A disputed prediction may be incomplete. An unknown prediction is
allowed to remain unknown.

### Identity

This passive makes Spas valuable before the enemy appears. It does not function
as supernatural omniscience.

## 2A. Ordinary attack — Shard of Lelya

Spas directs a small retained fragment of destroyed Lelya through the small
Lelya ring of his Three-Moon Measure. The fragment briefly changes its effective
weight, strikes one enemy at medium range and returns to its physical cradle.

### Mechanical identity

- medium range;
- moderate direct damage to one target;
- briefly increases the target's effective weight and slows its movement;
- repeatable only after the fragment has returned to the Measure.

The large Fatta ring moves as a visible counterweight during release. The
attack therefore reads as recovered gravitational technology from the Lelya
catastrophe, later retold as lunar priestcraft. It is not a beam, thrown spell
or generic ranged weapon.

### Limitation

The attack does not reveal enemies, interrupt special actions, affect a group
or replace Spas's forecast role. Exact damage, range, slow strength and cadence
remain numerical-balance decisions.

## 3. Building I — Warning Stone

Hero handle: `spas_warning_stone`  
Tier: early / inexpensive  
Placement: empty cell adjacent to a Road  
Limit: 3

### Purpose

Local protection against one specifically announced hostile action.

### Appearance concept

A low piece of pale Daariyan warning stone seated in the ground. Its top holds
three unequal lunar grooves and one removable mineral-red danger plate. Four
small pressure wedges point toward neighbouring cells.

It is a practical road instrument, not a runestone, shrine or defensive wall.

### Ability — Early Warning

When placed, the player selects one danger:

- raid against a building;
- Grey capture or owner removal;
- tunnelling emergence;
- summoning or copied-route opening.

The first selected action occurring within range is interrupted before its
effect resolves.

The involved enemy group loses its prepared action and moves more slowly for a
short recovery interval. Nearby friendly buildings prepare their next answer
against that group faster.

After triggering, the red danger plate becomes spent. The Stone resets between
waves, not repeatedly during the same wave.

### Wrong forecast

If another type of danger enters the area, the Stone does nothing. It does not
deal damage or block the Road.

### Upgrade direction

- Level 1: protects its own cell and immediate neighbours;
- Level 2: larger listening radius;
- Level 3: may name two different dangers, but still interrupts only one action
  per wave.

### Gameplay identity

Cheap local control that rewards reading the forecast: it cancels one correctly
named action, disrupts that group and accelerates the local response.

## 4. Building II — Riphean Passage Yard

Hero handle: `spas_passage_yard`  
Tier: middle / moderate cost  
Placement: opened buildable cell, not directly on Road  
Limit: 2

### Purpose

Evacuates one threatened friendly building without pretending that relocation
is free or instantaneous.

### Appearance concept

A broad low stone transit platform patterned after the migration route along
the Riphean Mountains. It has one receiving recess, one departure recess,
ochre route strips and four heavy stone rollers. No portal, glowing teleport
ring or railway machinery.

### Ability — Remove from the Fall

The Yard may register one friendly building within range as its **ward**.

When the registered building is about to be destroyed or fully captured:

- its owner, level and surviving functional layers are removed from the board;
- the original footprint becomes a damaged departure scar;
- the building enters the Yard's evacuation reserve;
- after the wave, the player may place it on any valid opened cell for a
  reduced re-binding cost.

### Cost of evacuation

- the building stops functioning immediately;
- damage is preserved;
- re-binding is not free;
- the abandoned cell remains unavailable for one full wave;
- only one building may be stored in each Yard;
- the Last Knot, Roads, resource deposits and another Passage Yard cannot be
  evacuated.

### Manual use

The player may order evacuation before critical danger. Voluntary evacuation
takes several seconds and may be interrupted by a raid. Emergency evacuation
is automatic but returns the building with greater retained damage.

### Upgrade direction

- Level 1: one registered building, high re-binding cost;
- Level 2: faster voluntary evacuation and lower cost;
- Level 3: stores one building plus one detached owner or witness layer.

### Gameplay identity

This is Spas's defining structure. It converts a total loss into an expensive,
delayed recovery rather than granting invulnerability.

## 5. Building III — Observatory of Three Moons

Hero handle: `spas_three_moon_observatory`  
Tier: late / expensive  
Placement: large clear footprint with sight of at least one Road  
Limit: 1

### Purpose

Turns several independent observations into one temporary battlefield plan.

### Appearance concept

A monumental but low Daariyan observation platform translated into a gameplay
object. Three unequal stone-and-metal orbital rings surround a central Midgard
plumb. Six non-identical record leaves occupy separate sockets around the
platform.

It is not a telescope tower, magical orrery, laser device or temple.

### Ability — Convergence of Six Models

The Observatory listens to six types of battlefield evidence:

1. Road direction;
2. ground pressure;
3. owner or provenance;
4. copied transmission;
5. incomplete name;
6. captured machine layer.

Different nearby building families supply different observations. Repeated
copies of the same family count only once.

When three different observations agree:

- the next special enemy action in range is revealed before preparation;
- nearby buildings receive enough notice to enter their prepared state early;
- those buildings acquire affected targets sooner and recover from their next
  committed action faster.

When five or six different observations agree:

- the revealed hostile action is interrupted at commitment;
- imposed layers involved in that action remain exposed briefly for other
  buildings to answer;
- the enemy itself is not automatically destroyed.

### False consensus

If most observations come from identical or Grey-captured sources, the
Observatory refuses to commit. It displays a disputed forecast instead of
producing an effect.

### Upgrade direction

- Level 1: requires four distinct observations for early preparation;
- Level 2: requires three;
- Level 3: unlocks the five/six-source interruption.

### Gameplay identity

Expensive late-game coordination. Its strength depends on a diverse defence,
not on filling the map with one optimal tower. It strengthens surrounding
buildings rather than dealing direct damage.

## 6. How the three buildings work together

### Before the wave

**Measure of Three Moons** shows the likely first Road and special danger.

### Local preparation

The player places or configures a **Warning Stone** near the expected event.

### Preservation

A valuable structure on the threatened side is registered with the **Riphean
Passage Yard**.

### Late-game verification

The **Observatory of Three Moons** compares different building observations and
prevents one verified large hostile action.

The kit therefore does not contain three versions of a shield:

- Warning Stone protects one event;
- Passage Yard preserves one investment after failure;
- Observatory coordinates a diverse defence.

## 7. Intended strengths

- more preparation information;
- strong defence against raids, capture, tunnelling and summoning;
- protects expensive developed buildings from permanent loss;
- rewards varied construction;
- converts catastrophic mistakes into recoverable setbacks;
- strongly reflects Spas and the evacuation from Daariya.

## 8. Intended weaknesses

- none of the buildings deals direct damage;
- wrong Warning Stone configuration wastes its wave;
- Passage Yard temporarily removes a useful building;
- Observatory requires several different supporting structures;
- heavy investment in preservation may leave insufficient ordinary defence;
- weak against simple mass movement without special actions.

## 9. Functional profile

| Element | Primary effect | Secondary effect |
|---|---|---|
| Measure of Three Moons | information and preparation time | pre-prepares correctly positioned Spas buildings |
| Shard of Lelya | moderate damage to one enemy | briefly increases effective weight and slows movement |
| Warning Stone | interrupts one predicted special action | briefly slows that group and accelerates nearby friendly preparation |
| Riphean Passage Yard | preserves one threatened building | enables delayed discounted re-binding elsewhere |
| Observatory of Three Moons | verifies and interrupts complex actions | strengthens preparation and recovery of diverse nearby buildings |

Spas supplies limited single-target direct damage. His three unique buildings
remain non-damaging and instead control enemy tempo and improve the reliability
of the surrounding defence.

## 10. Explicit exclusions

- no active hero ability or personal resource meter;
- no generic melee swing or unrelated conventional projectile;
- no global shield;
- no time stop or rewind;
- no moon beam, falling moon, area bombardment or automatic gravitational kill;
- no automatic free relocation;
- no three buildings that perform the same protection role;
- no inherited Paladin, Mage or Hunter structures from the alpha lore;
- no racial or lineage bonuses.

## 11. Approval result

Approved:

- Measure of Three Moons as Spas's single passive;
- Shard of Lelya as Spas's ordinary personal attack;
- Warning Stone as the first unique building;
- Riphean Passage Yard as the second and defining building;
- Observatory of Three Moons as the expensive third building;
- no direct-damage requirement for unique hero buildings;
- future hero buildings receive attack, strengthening, slowing, weakening,
  control, economy or preservation only where appropriate to that character.

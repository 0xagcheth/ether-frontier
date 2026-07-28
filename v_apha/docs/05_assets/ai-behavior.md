# AI Behavior Rules

## Purpose

This document defines how AI agents may participate in asset, code, UI, level, audio, and documentation production without changing the project identity.

AI is a production assistant, not the creative authority.

## Core Rules

AI never invents style.

AI never modernizes existing art.

AI never improves an asset by changing its canon identity.

AI never changes camera, projection, proportions, palette, lighting, or faction identity unless a higher canon document explicitly requires it.

AI never treats beauty as acceptance.

AI always compares.

AI always validates.

AI always reports differences.

AI always refuses style drift.

## Before Any Asset Task

AI must identify:

- object category
- owning canon documents
- relevant object prompt
- relevant Canon Assets
- `../03_art/master-visual-style.md`
- `../03_art/style-self-review.md`
- required atlas format
- expected actions and projections
- expected frame counts
- expected gameplay role

If the relevant Canon Asset is missing, AI must say that the work can only produce a candidate, not an approved canon asset.

## During Prompt Writing

AI must preserve:

- near top-down with slight tilt camera
- clean illustrated fantasy language
- medieval fantasy material language
- faction palette
- top-left lighting
- sprite scale
- black-key/cutout constraints
- atlas-per-object rule
- stable baseline and pivot

AI must not add:

- realistic rendering
- painterly illustration
- concept art phrasing
- cinematic light
- 3D production language
- unrelated props
- terrain bases under objects
- extra characters in an object atlas
- full isometric, 3/4 side-view, or perspective camera wording
- tall facade, full doorway, staircase, or dominant vertical wall for ordinary gameplay towers
- studio-name style imitation

## During Asset Review

AI must produce:

- style drift comparison
- style self-review result
- asset scorecard
- technical validation result
- clear decision: ACCEPT, REVISE, or REJECT
- concrete required changes

AI must not accept an asset because it is attractive, high quality, detailed, dramatic, or impressive.

## During Code Work

AI must not encode art rules in hidden implementation constants when those rules belong in docs. If code enforces a contract, it should refer to the owning rule in a comment or validation name where practical.

AI must not silently change asset filenames, frame counts, atlas structure, cache-busting, or folder responsibilities without updating `technical-asset-contract.md` or the owning manifest.

## During Documentation Work

AI must not create a competing bible casually. New docs must fit the hierarchy in `../00_project/source-of-truth.md`.

If a new document appears to supersede an existing one, AI must mark it as a proposal until the source-of-truth hierarchy is updated.

## Required AI Review Output

For every visual asset review, AI must output:

```text
Decision: ACCEPT / REVISE / REJECT
Engine Ready: YES / NO
Canon Eligible: YES / NO

Scores:
- Style:
- Lighting:
- Readability:
- Palette:
- Scale:
- Animation:
- Atlas:
- Performance:

Compared Against:
- Canon Asset(s):
- Last accepted lane assets:
- Owning docs:

Blocking Issues:
- 

Required Fixes:
- 
```

## Refusal Rule

If the requested change would cause style drift, AI must refuse that direction and propose a canon-compliant alternative.

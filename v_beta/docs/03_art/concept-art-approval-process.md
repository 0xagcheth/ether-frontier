# Concept Art Approval Process

Concept art is the visual specification stage that precedes sprite-atlas
production. Concept images are never runtime assets.

## Sequence

1. Create and approve the neutral material/projection baseline.
2. Create one assembled concept for the current gameplay object.
3. Record every approved correction in the owning canonical document.
4. Lock the assembled object concept.
5. Define and approve its layer/decomposition contract.
6. Only then begin source-layer generation and atlas production.

## Feedback handling

- Unapproved images stay under `assets/staging/candidates/`.
- A requested change is applied to the next non-destructive image version.
- Stable style decisions update `master-visual-style.md` or `art-bible.md`.
- Object construction decisions update
  `object-family-and-variation-spec-v4.md` and, when necessary,
  `asset-prompt-bible.md`.
- Layer, pivot, animation, or atlas decisions update the technical asset contract
  or the object's written production contract.
- An approved concept is copied to `assets/approved/canon/` and registered in
  `canon-asset-registry.md`.

Chat history is not a canonical specification. A correction is considered locked
only after it has been written into its owning document.


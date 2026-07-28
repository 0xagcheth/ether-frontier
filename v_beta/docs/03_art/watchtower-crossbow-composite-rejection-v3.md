# Watchtower Crossbow Composite v3 — Rejection

Updated: 2026-07-24

Status: **REJECTED**

## Visible faults

1. The left and right arms do not share a believable common mount.
2. The body and arms have different scale and curvature conventions.
3. The independently generated bolt is too large for the guide.
4. Attachment offsets produce overlap but not a valid mechanism.
5. The missing string makes the structural mismatch even more obvious.

## Root cause

The composite combined three separately redesigned ImageGen subassemblies.
Independent generation is appropriate for texture exploration, but not for
geometry that must physically connect.

## Corrective pipeline

1. Use `watchtower_crossbow_group_v2_alpha.png` as the single geometry source.
2. Normalize the whole weapon once against projection master v4.
3. Segment children from the normalized whole.
4. Use generated isolated sources only to restore occluded print/edge areas.
5. Validate the weapon alone before placing it on the tower.

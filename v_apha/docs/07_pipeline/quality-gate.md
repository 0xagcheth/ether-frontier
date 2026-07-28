# Quality Gate

## Purpose

The quality gate is the mandatory acceptance system for every asset, animation, UI element, level, sound, and code change.

Nothing is accepted because it looks beautiful. Work is accepted only when it passes the required gates.

## Asset Gate Flow

```text
Candidate Asset
↓
Canon Source Check
↓
Style Self Review
↓
Style Drift Check
↓
Style Review
↓
Scale Review
↓
Atlas Review
↓
Animation Review
↓
Gameplay Review
↓
Performance Review
↓
Accept / Revise / Reject
```

## Required Decision Labels

- `ACCEPT`: all blocking gates passed.
- `REVISE`: asset is directionally valid but has fixable issues.
- `REJECT`: asset violates canon, style, engine contract, or gameplay readability.

## Asset Scorecard

Each reviewed visual asset receives scores:

| Category | Minimum | Blocking |
|---|---:|---|
| Style | 9/10 | Yes |
| Lighting | 9/10 | Yes |
| Readability | 9/10 | Yes |
| Palette | 9/10 | Yes |
| Scale | 10/10 | Yes |
| Proportions | 10/10 | Yes |
| Animation | 9/10, or 10/10 for building body lock | Yes |
| Atlas | 10/10 | Yes |
| Engine Ready | YES | Yes |
| Gameplay Fit | 9/10 | Yes |
| Performance | PASS | Yes |

Any blocking category below the minimum means the asset cannot be accepted.

## Style Review

Pass only if:

- The asset matches the Art Bible.
- The asset passes `../03_art/style-self-review.md`.
- It matches the relevant Canon Assets.
- It does not introduce realism, modern rendering, painterly style, or 3D language.
- Faction color language is correct.
- Pixel density matches nearby accepted assets.

## Scale Review

Pass only if:

- Gameplay footprint matches class.
- Cell size matches contract.
- Pivot and baseline are stable.
- The object reads at gameplay scale.
- It does not overpower smaller or larger classes incorrectly.

## Atlas Review

Pass only if:

- Atlas is PNG plus JSON.
- PNG is under 5 MB.
- Atlas contains one visual object only.
- Frame names match naming convention.
- JSON frame rectangles, pivots, offsets, and animations are valid.
- No unrelated projectiles, props, terrain, or UI elements are included.

## Animation Review

Pass only if:

- Required actions exist.
- Required projections exist.
- Frame count matches contract.
- Unit motion has readable anticipation, action, recovery, or loop.
- Buildings keep solid structure static during idle.
- No baseline jitter or scale crawl exists.

## Gameplay Review

Pass only if:

- Role is readable before detail.
- Enemy/tower/resource/UI function is clear at game scale.
- VFX does not hide tactical state.
- Player and enemy ownership cannot be confused.

## Performance Review

Pass only if:

- Atlas size is within budget.
- Frame count is justified.
- Runtime loading path is known.
- No avoidable oversized source files are introduced into production paths.

## Review Record Template

```text
Asset:
Reviewer:
Date:
Owning Docs:
Canon Assets Compared:

Scores:
- Master Visual Style: PASS/FAIL
- Style: /10
- Lighting: /10
- Readability: /10
- Palette: /10
- Scale: /10
- Proportions: /10
- Animation: /10
- Atlas: /10
- Gameplay Fit: /10
- Performance: PASS/FAIL
- Engine Ready: YES/NO

Blocking Failures:
- 

Decision: ACCEPT / REVISE / REJECT
Canon Eligible: YES / NO
Required Fixes:
- 
```

## Canon Promotion

An accepted asset is not automatically a Canon Asset. Canon promotion requires a second explicit decision and an entry in `../05_assets/canon-asset-registry.md`.

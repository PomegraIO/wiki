---
title: "Three-Stage Dividend Discount Model"
description: "A refinement of the two-stage DDM that adds a transitional growth phase between high-growth and stable-growth periods."
keywords:
  - dividend discount model
  - three-stage growth
  - transitional growth
  - H-model
  - dividend valuation
image: "/svg/valuation.svg"
---

*The **three-stage dividend discount model** extends the [two-stage dividend discount model](/two-stage-dividend-discount-model/) by inserting a bridging period in which growth gradually declines from the initial rapid rate to the terminal stable rate. Rather than an abrupt handoff from, say, 20% growth to 3%, the three-stage model lets growth taper smoothly through an intermediate zone—a pattern closer to how real companies typically mature.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Three-Stage Dividend Discount Model — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation concepts." />

<div class="wiki-infobox-caption">High growth, then gradual decline, then stability.</div>

|   |   |
|---|---|
| **What it is** | Equity valuation with explicit high-growth, transitional, and stable-growth periods |
| **Also called** | Three-stage growth model, H-model (in some variants), multi-stage DDM |
| **Key refinement** | Growth rate declines linearly (or otherwise) from Stage 1 to Stage 3 |
| **Core inputs** | Initial dividend, high-growth rate and duration, transitional-growth parameters, terminal growth rate, [discount rate](/discount-rate/) |
| **Theoretical edge** | More realistic trajectory of corporate maturation |
| **Practical tradeoff** | More complex calculation and more assumptions to validate |

</aside>

## The intuition behind three stages

The [two-stage model](/two-stage-dividend-discount-model/) is elegant: growth for *n* years, then perpetual stability. But real companies rarely flip a switch at Year n and settle into a fixed growth rate. A technology firm might sustain 18% growth for three years, then gradually decelerate as the market saturates and competition intensifies, reaching 4% stable growth by Year 8. The three-stage model captures this deceleration explicitly.

Instead of assuming:
- Years 1–5: 15% growth
- Years 6+: 3% growth

The three-stage model assumes:
- Years 1–3: 15% growth (high growth)
- Years 4–6: 15% declining linearly to 3% (transition)
- Years 7+: 3% growth (stable growth)

This is not just cosmetic. The smoother path tends to produce a fairer valuation because it avoids the artificial cliff at the transition point. It also often better matches the observed dividend behaviour of mature companies.

## How the three-stage model is structured

The calculation breaks into three parts:

**Stage 1 (High Growth):** Explicit forecasts for years 1 through n1, with constant growth rate g1. Each dividend is discounted back to present value:

PV(Stage 1) = Σ [D0 × (1 + g1)^t / (1 + r)^t] for t = 1 to n1

**Stage 2 (Transitional Growth):** Dividends grow at a declining rate from g1 down to g2, typically over n2 years (often 2–4 years). The most common assumption is *linear decline*:

Growth in year t = g1 − (g1 − g2) × (t − n1) / n2

This means growth steps down smoothly. For example, if g1 = 15%, g2 = 3%, and the transition lasts 3 years:
- Year 4: 15% − (15% − 3%) × 1/3 = 11%
- Year 5: 15% − (15% − 3%) × 2/3 = 7%
- Year 6: 15% − (15% − 3%) × 3/3 = 3%

Each interim dividend is forecast and discounted:

PV(Stage 2) = Σ [D(t−1) × (1 + g_t) / (1 + r)^t] for t = n1+1 to n1+n2

where g_t is the year-specific transitional growth rate.

**Stage 3 (Terminal/Stable Growth):** From year n1+n2+1 onward, dividends grow at constant rate g2 forever. Terminal value is computed using the perpetuity formula, applied to the last dividend from Stage 2:

Terminal Value = [D(n1+n2) × (1 + g2)] / (r − g2)

Discount this back to present:

PV(Stage 3) = Terminal Value / (1 + r)^(n1 + n2)

**Total Fair Value = PV(Stage 1) + PV(Stage 2) + PV(Stage 3)**

## A worked example

Assume the same company as before: current dividend 2.00, [cost of equity](/cost-of-equity/) 10%. But now:
- Stage 1 (3 years): 15% growth
- Stage 2 (3 years): growth declines from 15% to 3%
- Stage 3 (perpetuity): 3% growth

**Stage 1** (Years 1–3, flat 15% growth):
- Year 1: 2.00 × 1.15 / 1.10 = 2.09
- Year 2: 2.00 × 1.15² / 1.10² = 2.30
- Year 3: 2.00 × 1.15³ / 1.10³ = 2.53
- **PV(Stage 1) = 6.92**

**Stage 2** (Years 4–6, declining 15% to 3%):
- Year 4: dividend = 2.53 × 1.11 / 1.10⁴ = 1.73 (11% growth in year 4)
- Year 5: dividend = 2.81 × 1.07 / 1.10⁵ = 1.74 (7% growth in year 5)
- Year 6: dividend = 3.01 × 1.03 / 1.10⁶ = 1.70 (3% growth in year 6)
- **PV(Stage 2) = 5.17**

**Stage 3** (Terminal):
- Year 7 dividend: 3.01 × 1.03 × 1.03 = 3.20
- Terminal Value = 3.20 / (0.10 − 0.03) = 45.71
- PV(Stage 3) = 45.71 / 1.10⁶ = 25.79

**Fair Value = 6.92 + 5.17 + 25.79 = 37.88 per share**

Contrast this with the two-stage model from the prior article (40.56 per share). The three-stage valuation is slightly lower because the transition zone caps Stage 1 growth more realistically—you do not assume 15% growth as long, so near-term cash is smaller.

## Linear versus non-linear transition

The example above assumes *linear* decline in growth—a common simplification that is tractable and defensible. Some practitioners use alternative transition curves:

- **Exponential decay:** Growth declines faster initially, then flattens. Mathematically:
  g_t = g2 + (g1 − g2) × e^(−k × (t − n1))

- **Quadratic or spline:** Growth follows a smoother polynomial path.

The choice matters most when the transition is long (4+ years). For shorter transitions (2–3 years), linearity is usually sufficient and far easier to explain to stakeholders.

## When three stages beat two

The three-stage model is worth the added complexity when:

1. **Long businesses lifecycles are evident.** A utility transitioning from a regulated monopoly to a competitive market might spend 3–5 years in transition, not jump instantly.

2. **Dividend history shows gradual deceleration.** If past data shows growth declining year by year, the three-stage model captures this pattern better.

3. **Multiple scenarios are being explored.** Building one well-specified three-stage model is easier than running many two-stage models with varying assumptions about when the transition happens.

4. **Precision is needed for close valuation calls.** If a stock is near fair value on a two-stage model, the three-stage view might tip the decision.

Three-stage models are popular in regulated industries (utilities, telecoms), where growth transitions are predictable, and in M&A analysis, where the acquirer can forecast a multi-year integration and normalization.

## The "H-model" shortcut

For practitioners seeking a closed-form solution, the H-model (named for its shape) approximates a three-stage model with a mathematical shorthand. It assumes growth declines linearly over a half-life H, simplifying the calculation:

Value ≈ D0 × (1 + g2) / (r − g2) + D0 × H × (g1 − g2) / (r − g2)

This trades some accuracy for speed and is useful in bulk screening, but bespoke three-stage calculations are preferred when a specific valuation matters.

## Common pitfalls

**Overstaying in Stage 1:** Analysts often assume high growth lasts longer than reasonable. Quarterly earnings calls and industry reports should inform realistic Stage 1 duration—not wishful thinking.

**Transition too fast:** A three-year deceleration from 20% to 3% is almost never observed in practice. Five to seven years is more typical for large-cap companies.

**Terminal growth above GDP:** Stage 3 growth should rarely exceed 4–5% for developed-market companies. Assuming 6–8% indefinite growth is a red flag that the analyst is overvaluing.

**Ignoring regime change:** If competitive dynamics shift dramatically (new entrant, regulation, technology disruption), the entire three-stage structure must be re-examined. Models are tools, not prophecy.

## Three-stage versus two-stage trade-off

The two-stage model is simpler, faster, and good enough for most equity research. The three-stage model is more theoretically satisfying and often more accurate for companies with visible maturation paths. The choice depends on available data, the confidence in forecasts, and whether the marginal precision justifies the added complexity.

For academic research and textbook examples, three-stage models showcase the full toolkit. For practising analysts, many use two-stage for speed and reserve three-stage for situations where the transition phase materially affects the valuation.

## See also

<div class="wiki-seealso">

### Closely related

- [Two-stage dividend discount model](/two-stage-dividend-discount-model/) — the simplified cousin
- [Dividend discount model](/dividend-discount-model/) — the foundational one-stage framework
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the broader DCF approach
- [Terminal value](/terminal-value/) — how to value the perpetual cash beyond explicit forecasts
- [Cost of equity](/cost-of-equity/) — the discount rate used in all DDM calculations
- [Dividend](/dividend/) — the cash the model projects

### Wider context

- Valuation — the broader practice of pricing equity
- [Relative valuation](/relative-valuation/) — comparing firms using multiples like [price-to-earnings-ratio](/price-to-earnings-ratio/)
- [Value investing](/value-investing/) — the philosophy that marries intrinsic valuation with price
- [Business cycle](/business-cycle/) — the real-world maturation pattern that three-stage models attempt to capture

</div>

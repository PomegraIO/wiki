---
title: "What Happens in the DDM When Dividend Growth Exceeds the Discount Rate"
description: "When dividend growth (g) equals or exceeds the discount rate (r) in the Gordon Growth Model, the formula produces nonsensical results. Multi-stage models and explicit forecast periods solve the problem."
keywords:
  - dividend discount model
  - dividend growth exceeds discount rate
  - gordon growth model
  - ddm valuation problem
image: "/svg/valuation.svg"
---

*The Gordon Growth Model, the simplest form of the [dividend discount model](/dividend-discount-model/), assumes a company pays dividends forever at a steadily increasing rate. When the long-term dividend growth rate (g) approaches or exceeds the discount rate (r), the formula breaks down mathematically, producing infinite or negative valuations that contradict reality. This boundary case reveals both the model's elegant simplicity and its limitations, forcing practitioners to deploy multi-stage models and explicit forecast periods.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DDM When Dividend Growth Exceeds Discount Rate — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">An impossible assumption exposed by algebra forces refinement toward multi-stage reality.</div>

|   |   |
|---|---|
| **The formula problem** | When g ≥ r, the denominator (r − g) becomes zero or negative, yielding infinite or negative values |
| **Real cause** | The model assumes eternal growth at a constant rate; unsustainable over infinite time |
| **Practical solutions** | Two-stage DDM; three-stage DDM; explicit forecast period followed by terminal value |
| **Industry standard** | Most analysts use 5–10 year explicit forecasts, then apply terminal assumptions |
| **Why it matters** | Forces disciplined judgment about when growth normalizes |

</aside>

## The formula at its breaking point

The Gordon Growth Model (one-stage [dividend discount model](/dividend-discount-model/)) states:

**P₀ = D₁ / (r − g)**

where:
- P₀ is the present value (intrinsic price).
- D₁ is next year's expected dividend.
- r is the [discount rate](/discount-rate/) (required return).
- g is the perpetual dividend growth rate.

This formula is beautifully simple and works well when g is meaningfully lower than r. A stock with a 5% dividend growth rate and a 10% discount rate yields a clean valuation.

But suppose a company is growing dividends at 9% and investors require 10% return. The denominator shrinks to 1%, inflating value. If growth reaches 10%, the denominator is zero—the formula crashes. If growth exceeds 10%, the denominator is negative, implying negative stock value, which is nonsensical.

Mathematically, the model demands g < r always. Economically, that constraint is often violated, particularly for young, thriving companies.

## Why the assumption breaks

The root cause is the model's assumption that a company will grow dividends at rate g forever. Over infinite time, even a 1% perpetual growth rate—compounding uninterrupted—will eventually produce dividends larger than the entire global economy, which is impossible.

Real companies follow a lifecycle:
1. **High growth phase** (5–15 years): Invest heavily, distribute modest or no dividends, growth rate > r.
2. **Transition phase** (years 15–25): Growth slows, dividend payout rises.
3. **Mature phase** (perpetuity): Growth stabilizes near GDP growth (~2–3%), r > g again.

A young, rapidly growing tech company might have a 20% dividend growth rate. Assuming that rate indefinitely is fantasy. Yet the one-stage Gordon model forces exactly that assumption, leading to breakdown when g creeps near r.

## The two-stage solution

The two-stage DDM splits the timeline:

**Stage 1 (explicit forecast, years 1–5 or 1–10):**
- Assume the company grows at the high rate g₁ (which can exceed r).
- Calculate the present value of dividends explicitly, year by year.
- Sum these year-by-year values.

**Stage 2 (terminal value):**
- Assume at the end of year N, growth slows to a sustainable, perpetual rate g₂ (where g₂ < r, often 2–3%).
- Use Gordon's formula with g₂ to calculate terminal value: **Terminal Value = D(N+1) / (r − g₂)**.
- Discount that terminal value back to present.

**Example:**
A stock pays $1.00 annual dividend. Growth is expected at 15% for the next 5 years, then 3% forever. Required return is 10%.

| Year | Dividend | Present Value (discounted at 10%) |
|------|----------|-----|
| 1 | $1.15 | $1.05 |
| 2 | $1.32 | $1.09 |
| 3 | $1.52 | $1.14 |
| 4 | $1.75 | $1.19 |
| 5 | $2.01 | $1.25 |
| **PV of stage 1** | | **$5.72** |

**Terminal Value (year 5):**
- Dividend in year 6: $2.01 × 1.03 = $2.07
- Terminal Value at year 5: $2.07 / (0.10 − 0.03) = $29.57
- PV of Terminal Value: $29.57 / (1.10)⁵ = $18.35

**Total intrinsic value: $5.72 + $18.35 = $24.07 per share**

The two-stage model sidesteps the mathematical trap: you explicitly forecast high growth where it's plausible, then impose normalcy.

## The three-stage refinement

For companies with a prolonged transition, analysts add a third stage:

**Stage 1:** High growth (15% for 5 years).
**Stage 2:** Decline toward maturity (15% → 8% over years 6–10).
**Stage 3:** Terminal maturity (3% perpetual growth).

Each stage uses different assumptions. Stage 1 dividends are calculated year-by-year. Stage 2 can use a linearly declining growth schedule or specific forecasts. Stage 3 uses Gordon's formula with the mature-phase growth rate.

Three-stage models are common in practice and reflect reality better, though they demand more judgment about when transitions occur and how fast growth normalizes.

## Avoiding the trap: disciplined assumptions

The practical lesson is not to avoid the one-stage model—it remains useful for mature, slow-growth companies. Instead, practitioners must be discipline about assumptions:

**Red flag:** If your long-term growth assumption is ≥ the discount rate, you are implicitly assuming the company will eventually exceed the economy's growth. Ask why: Is the company taking market share permanently? Inventing new products forever? Usually, the answer is no.

**Adjustment:** Set the perpetual growth rate to realistic equilibrium—often the long-run GDP growth rate (2–3% in developed economies) plus a small industry premium. Be explicit about it.

**Time horizon honesty:** If a company genuinely has 8 years of 15% growth ahead, say so. Forecast those 8 years explicitly, then apply a normal terminal rate. This approach forces you to commit to a timeline, making assumptions transparent and testable.

## Why this matters to valuations

The difference between a one-stage and two-stage model can be enormous. Using Gordon's formula with g = 12% and r = 10% yields an infinite valuation. Switching to a two-stage model with 12% growth for 5 years, then 3% forever, yields a finite, rational value. Investors who rely on the one-stage model without checking its validity can produce wildly optimistic valuations.

Conversely, analysts sometimes force the one-stage model on fast-growing companies, implicitly penalizing them for not being mature. A two-stage model respects reality: high growth is possible, but not forever. Valuation becomes more realistic.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend discount model](/dividend-discount-model/) — the full family of valuation approaches
- [Dividend payout ratio](/dividend-payout-ratio/) — determines reinvestment and future growth capacity
- [Discount rate](/discount-rate/) — the hurdle rate that separates value from excess claims
- [Intrinsic value](/intrinsic-value/) — the goal of DDM and competitor models
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — earnings-based cousin using identical logic

### Wider context

- [Terminal value](/terminal-value/) — the challenge all multi-stage models face
- [Business cycle](/business-cycle/) — macroeconomic context that shapes long-term growth
- [Earnings per share](/earnings-per-share/) — often grows faster than dividends, complicating assumptions
- [Relative valuation](/relative-valuation/) — alternative approach that bypasses perpetuity assumptions

</div>

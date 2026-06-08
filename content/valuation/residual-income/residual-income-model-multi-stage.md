---
title: "Multi-Stage Residual Income Model Explained"
description: "How to split residual income valuation into distinct growth phases—high-growth and mature—with worked example and step-by-step methodology."
keywords:
  - multi-stage residual income model
  - two-stage residual income model
  - high-growth RI model
  - residual income valuation phases
image: /svg/valuation.svg
---

*A **multi-stage residual income model** divides the forecast into distinct periods—a high-growth stage where the firm earns above-market returns, and a mature stage where growth and returns converge toward industry norms. This structure is more realistic than a single-stage perpetual-growth model and allows the analyst to reflect the firm's actual competitive trajectory.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Multi-Stage Residual Income Model — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Forecast growth and returns separately; they rarely move in lockstep.</div>

|   |   |
|---|---|
| **Typical structure** | High-growth stage (5–10 years), mature stage (perpetuity) |
| **Key difference** | Each stage has its own earnings growth rate, ROE, and cost of equity assumptions |
| **High-growth period** | Higher ROE, excess residual income, often reinvestment of all earnings |
| **Mature period** | ROE converges toward cost of equity; steady-state growth equals dividend growth |
| **Terminal value** | Calculated at the boundary between stages |
| **Valuation** | Book Value₀ + PV(Stage 1 RIs) + PV(Stage 2 terminal value) |

</aside>

## Why split the forecast into stages

A single-stage residual income model—applying one set of assumptions about earnings growth, return on equity, and cost of equity to perpetuity—rarely reflects business reality. Most companies go through phases:

- **High-growth years (startup, breakout product, market expansion)**: The firm invests heavily, earns returns well above the cost of equity, and reinvests all profits.
- **Mature years (market saturation, steady cash generation)**: Growth slows, competitive returns approach the cost of equity, and the firm pays dividends or buys back shares.

A multi-stage model captures this by forecasting these periods separately, then stitching them together into a single intrinsic value.

## The two-stage model structure

The most common version has two stages:

1. **Explicit high-growth stage**: Years 1–N (often 5–10 years). Analyst projects earnings, calculates residual income, and discounts each year's RI back to present.
2. **Terminal (mature) stage**: Years N+1 to perpetuity. Assumes steady-state growth and ROE convergence. Terminal value is calculated at year N and discounted back.

**Formula**:

Intrinsic Value = Book Value₀ + Σ PV(RI_t) [t=1 to N] + PV(Terminal Value at year N)

## High-growth stage assumptions

During the high-growth stage, you project:

**Earnings growth**: Often higher than GDP (5–15% or more for early-stage tech, lower for mature cyclicals). This may vary year-by-year as the firm scales.

**Return on equity (ROE)**: Above the cost of equity, reflecting the firm's competitive advantages. Example: Cost of equity = 8%, expected ROE = 12–15% for a high-growth tech firm.

**Reinvestment rate**: Often 100% (all earnings retained), since the firm is growing and not yet paying dividends.

**Book value growth**: Driven by retained earnings. If earnings = $100M and ROE = 10%, and all earnings are retained, book value grows by $100M (assuming no distributions).

**Residual income each year**:
RI_t = Earnings_t − (Book Value_{t-1} × Cost of Equity)

## Mature-stage assumptions

At the boundary into the mature stage (say, year 10), assumptions shift:

**Earnings growth**: Slows to long-term sustainable rate, often aligned with nominal GDP growth (2–3.5%). May also reflect competitive equilibrium in the industry.

**Return on equity**: Converges toward the cost of equity. If cost of equity = 8%, mature-stage ROE might be 8–9%. The spread (ROE − Cost of Equity) shrinks, making residual income small.

**Payout ratio**: May shift to a dividend-paying policy. If mature earnings = $200M, and the payout ratio is 60%, dividends = $120M and retained earnings = $80M.

**Terminal residual income**: Once ROE = Cost of Equity, RI = 0 (no excess return). But if ROE stays slightly above cost of equity (say, 1–2 percentage points), modest RI persists in perpetuity.

## Numeric example: a two-stage model

Let's value a consumer software firm:

**Current state**:
- Book Value = $100M
- Cost of Equity = 9%

**Stage 1 (High-growth, years 1–5)**:

| Year | Earnings | Beginning Book Value | RI = Earnings − (BV × 9%) |
|---|---|---|---|
| 1 | $12M | $100M | $12M − $9M = $3M |
| 2 | $16M | $112M | $16M − $10.1M = $5.9M |
| 3 | $22M | $128M | $22M − $11.5M = $10.5M |
| 4 | $28M | $150M | $28M − $13.5M = $14.5M |
| 5 | $34M | $178M | $34M − $16M = $18M |

(Assumes all earnings retained; book value grows by annual earnings.)

**PV of Stage 1 RIs** (discounted at 9% cost of equity):
$3M / 1.09 + $5.9M / 1.09² + $10.5M / 1.09³ + $14.5M / 1.09⁴ + $18M / 1.09⁵
= $2.75M + $4.97M + $8.11M + $10.28M + $11.69M = **$37.8M**

**Stage 2 (Mature, year 6 onward)**:

Assume:
- Beginning book value (year 6) = $212M (year 5 BV + year 5 earnings)
- Earnings growth = 2.5% in perpetuity
- ROE = 9% (equals cost of equity, so steady-state RI = 0)
- All earnings paid out as dividends (no further reinvestment)

Since ROE = Cost of Equity, residual income = $0 forever.

Terminal Value (at end of year 5) = Book Value at year 6 = $212M

(Alternatively, if you assume ROE = 9.5% and 2.5% growth in perpetuity, terminal RI would be Earnings_6 − Charge = (212M × 9.5% × 1.025) − (212M × 9%) = $20.7M − $19.1M = $1.6M, and Terminal Value = $1.6M × 1.025 / (0.09 − 0.025) = $29.8M. This captures slight ongoing excess return.)

For simplicity, assume Terminal Value = $212M.

**PV of Terminal Value** (discounted back 5 years at 9%):
$212M / 1.09⁵ = $137.8M

**Total intrinsic value**:
Book Value₀ + PV(Stage 1 RIs) + PV(Terminal Value)
= $100M + $37.8M + $137.8M = **$275.6M**

If there are 10M shares outstanding, per-share intrinsic value ≈ $27.56.

## When to use three or more stages

For some firms, two stages oversimplify. A three-stage model might split:
1. High-growth (years 1–5): ROE 12%, earnings growth 15%
2. Transition (years 6–10): ROE 10%, earnings growth 8%
3. Mature (year 11+): ROE 9%, earnings growth 2.5%

This is common for biotech (early success phases in different drugs) or retail (expansion, then consolidation, then maturity). The added complexity is justified if the business drivers genuinely change at different milestones.

## Common pitfalls in multi-stage modeling

**Too-optimistic high-growth assumption**: Projecting 20% earnings growth for 10 years strains credibility unless the firm is genuinely early-stage and has proven market traction. Most high-growth phases last 5–7 years.

**Inconsistent ROE and growth**: If you project 15% earnings growth but only 10% ROE, the implicit payout ratio becomes negative (impossible). Ensure that Growth = Retention Rate × ROE.

**Forgetting to converge ROE**: The biggest mistake is projecting a permanently elevated ROE. Competitive forces drive ROE toward cost of equity over time. Explicitly model the path (a gradual decline from 12% to 9%) rather than a sudden jump.

**Terminal value as an afterthought**: Many analysts spend 80% of effort on explicit forecasts and 20% on terminal value, then are shocked when terminal value is 60% of intrinsic value. Stress-test terminal assumptions.

## Integration with book value adjustments

If you've made [book value adjustments](/book-value-adjustments-residual-income/) (e.g., capitalizing R&D or adding back goodwill), start Book Value₀ with the adjusted figure. The stages then project forward from that base.

## See also

<div class="wiki-seealso">

### Closely related

- [Continuing Residual Income and Terminal Value](/continuing-residual-income-terminal-value/) — How to model the transition to steady-state in stage two
- [Book Value Adjustments for Residual Income Valuation](/book-value-adjustments-residual-income/) — The starting point before forecasting either stage
- [Residual Income Model with Negative Book Value](/residual-income-model-negative-book-value/) — Handling weak starting positions in multi-stage models

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Two-stage DCF uses the same logic with free cash flow
- [Return on Equity](/return-on-equity/) — The driver of residual income in both stages
- [Cost of Equity](/cost-of-equity/) — Sets the hurdle rate above which returns are "residual"
- Competitive Advantage — The basis for expecting ROE to exceed cost of equity in stage one

</div>

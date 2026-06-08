---
title: "Multi-Stage Dividend Discount Model Explained With an Example"
description: "A step-by-step walkthrough of the multi-stage dividend discount model with numerical examples, showing how to forecast near-term dividends and apply stable-growth terminal value."
keywords:
  - multi stage dividend discount model example
  - two stage ddm valuation
  - dividend forecasting terminal value
  - h-model dividends
  - stable growth valuation
image: /svg/valuation.svg
---

*The **multi-stage Dividend Discount Model** replaces the [Gordon Growth Model](/gordon-growth-model-assumptions/)'s single perpetual-growth assumption with explicit forecasts of dividends for 5–10 years, then applies a stable-growth terminal value to the remainder. A worked example shows how dividends evolve through stages, how to discount each stage back to today, and where the valuation is sensitive.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Multi-Stage DDM — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Forecast dividends in detail, then collapse the tail to a perpetuity.</div>

|   |   |
|---|---|
| **Stages** | Typically 2–3: high growth, moderate growth, stable |
| **Explicit period** | Year 1–5 or 1–10 forecasts with dividend detail |
| **Terminal value** | Gordon Model applied to year N+1 stable dividend |
| **Value** | PV of explicit dividends + PV of terminal value |
| **Payout assumption** | Tied to [sustainable growth rate](/sustainable-growth-rate-dividend-valuation/) in each stage |
| **Strength** | Captures realistic growth arcs; less sensitive than Gordon |
| **Complexity** | Requires more forecasts and judgment about transitions |

</aside>

## The Multi-Stage Logic

The [single-stage Gordon Growth Model](/gordon-growth-model-assumptions/) assumes dividends grow at a constant rate forever. Real companies do not. A high-growth software firm might expand dividends 15% annually for five years, decelerate to 8% for the next five years, then settle into 3–4% perpetual growth.

The multi-stage model respects this reality. It splits the future into explicit stages:
- **Stage 1:** High or above-average growth, dividends forecast year by year.
- **Stage 2:** Moderate growth, dividends forecast explicitly or as a bridge.
- **Stage 3:** Perpetual stable growth, valued as a terminal value (using perpetuity).

The firm's value is the sum of:
1. Present value of all Stage 1 dividends
2. Present value of all Stage 2 dividends
3. Present value of the terminal value

## A Worked Example: MidCap Industrial Inc.

Let's value a dividend-paying industrial firm with the following setup:

**Current fundamentals:**
- Current dividend (D₀): $2.00 per share
- Payout ratio: 35%
- Implied EPS: $5.71
- Return on equity (ROE): 14%
- Discount rate (cost of equity): 10%
- Current stock price: $50

**Stage 1 (Years 1–5): High-Growth Period**
- Dividend growth rate: 12% annually
- Rationale: The firm is expanding market share and capacity at above-GDP rates. ROE remains strong at 14%; payout stays at 35%. Sustainable growth = 14% × 65% = 9.1%, so 12% external growth assumptions are slightly above sustainable, implying modest external financing—realistic for a firm in expansion.

**Stage 2 (Year 6–10): Transition Period**
- Growth rate: 8% annually (midpoint between high and stable)
- Payout ratio: 40% (slight increase as reinvestment needs moderate)
- Rationale: Market maturation slows organic expansion. Competition and regulation compress margins slightly, lowering ROE to 12%. Sustainable growth = 12% × 60% = 7.2%; assumed 8% is near sustainable, requiring some external capital.

**Stage 3 (Year 11+): Perpetual Stable Growth**
- Growth rate: 4% annually
- Payout ratio: 50%
- ROE: 10%
- Rationale: Firm is now mature, competing in a slow-growth market. Sustainable growth = 10% × 50% = 5%, so 4% assumed growth is below sustainable. The firm retains more than it needs to grow, allowing for share buybacks or debt repayment.

## Stage 1 Dividend Forecast (Years 1–5)

Starting with D₀ = $2.00, grow at 12% per year:

| Year | Dividend | Discount factor (10%) | Present value |
|------|----------|---|---|
| 1 | $2.00 × 1.12 = $2.24 | 1 / 1.10 = 0.909 | $2.24 × 0.909 = $2.04 |
| 2 | $2.24 × 1.12 = $2.51 | 1 / 1.10² = 0.826 | $2.51 × 0.826 = $2.07 |
| 3 | $2.51 × 1.12 = $2.81 | 1 / 1.10³ = 0.751 | $2.81 × 0.751 = $2.11 |
| 4 | $2.81 × 1.12 = $3.15 | 1 / 1.10⁴ = 0.683 | $3.15 × 0.683 = $2.15 |
| 5 | $3.15 × 1.12 = $3.53 | 1 / 1.10⁵ = 0.621 | $3.53 × 0.621 = $2.19 |
| **Total PV Stage 1** | | | **$10.56** |

## Stage 2 Dividend Forecast (Years 6–10)

Starting from Year 5 dividend of $3.53, grow at 8% per year:

| Year | Dividend | Discount factor (10%) | Present value |
|------|----------|---|---|
| 6 | $3.53 × 1.08 = $3.81 | 1 / 1.10⁶ = 0.564 | $3.81 × 0.564 = $2.15 |
| 7 | $3.81 × 1.08 = $4.12 | 1 / 1.10⁷ = 0.513 | $4.12 × 0.513 = $2.11 |
| 8 | $4.12 × 1.08 = $4.45 | 1 / 1.10⁸ = 0.467 | $4.45 × 0.467 = $2.08 |
| 9 | $4.45 × 1.08 = $4.81 | 1 / 1.10⁹ = 0.424 | $4.81 × 0.424 = $2.04 |
| 10 | $4.81 × 1.08 = $5.19 | 1 / 1.10¹⁰ = 0.386 | $5.19 × 0.386 = $2.00 |
| **Total PV Stage 2** | | | **$10.38** |

## Terminal Value (Year 11+)

At the end of Year 10, we have a dividend of $5.19 per share. In Year 11, it grows to:

**D₁₁ = $5.19 × 1.04 = $5.40**

Using the [Gordon Growth Model](/gordon-growth-model-assumptions/) with stable-growth assumptions (g = 4%, r = 10%):

**Terminal Value = D₁₁ / (r − g) = $5.40 / (0.10 − 0.04) = $5.40 / 0.06 = $90.00**

This is the value at the end of Year 10. Discounting back to today:

**PV of Terminal Value = $90.00 / 1.10¹⁰ = $90.00 / 2.594 = $34.71**

## Total Valuation

**Intrinsic Value = PV(Stage 1) + PV(Stage 2) + PV(Terminal Value)**
**= $10.56 + $10.38 + $34.71 = $55.65 per share**

The current price is $50, suggesting the stock is undervalued by about 11%. An analyst might use this to support a buy recommendation, or as the start of a deeper investigation into whether the growth and payout assumptions are realistic.

## Sensitivity Analysis: Where Does Value Come From?

Terminal value represents $34.71 / $55.65 = **62% of intrinsic value**. This is typical and highlights the model's sensitivity to long-term assumptions.

Let's test how sensitive the valuation is to the terminal growth rate:

| Terminal Growth | Terminal Value (Year 10) | PV Terminal | Total Value | % Change |
|---|---|---|---|---|
| 3.0% | $5.40 / 0.07 = $77.14 | $29.73 | $50.67 | −9% |
| **4.0%** | **$5.40 / 0.06 = $90.00** | **$34.71** | **$55.65** | **—** |
| 5.0% | $5.40 / 0.05 = $108.00 | $41.65 | $62.59 | +13% |

A mere 1% change in perpetual growth swings the valuation by ±9–13%. This illustrates why the terminal assumption must be defensible. If the analyst assumes 5% perpetual growth but the economy is structurally limited to 2–3%, the overvaluation is severe.

## Stage Transitions and Judgment Calls

The growth rates in each stage are judgment calls. In practice, analysts might use:
- **Market guidance:** If management guides near-term growth, use that as Stage 1.
- **Industry comparables:** Compare growth assumptions to peers at similar lifecycle stages.
- **Historical performance:** Projects trend growth, adjusted for expected changes.
- **Fundamental constraints:** Ensure payout and ROE are consistent with [sustainable growth rate](/sustainable-growth-rate-dividend-valuation/).

In this example, Stage 1 at 12% is above the firm's 9.1% sustainable rate, implying modest external capital use. This is reasonable if the analyst believes the firm can profitably deploy external capital. If not, reduce the Stage 1 growth or increase the payout ratio to make the forecast self-funded.

## Two-Stage vs. Three-Stage Models

Many analysts use a simpler **two-stage model**: explicit forecast for 5 years, then perpetual growth thereafter. This saves one stage's worth of judgment, though it risks understating the transition period.

A three-stage model (as above) is more realistic but requires more forecast detail. The choice depends on confidence in the transition. For a cyclical firm entering a downturn, three stages help. For a stable utility, two suffice.

## When Forecasts Diverge from Market

If a multi-stage DDM yields $55.65 but the market price is $40, several explanations apply:

1. **Market is right:** Your growth or payout assumptions are optimistic.
2. **Hidden risk:** Competitive or regulatory threats not priced into the discount rate.
3. **Market timing:** The stock is genuinely cheap, and the market will eventually reprice it.
4. **Dividend risk:** The market doubts the sustainability of the forecast dividends.

Run sensitivity analysis. If the valuation is still $45+ even under conservative Stage 1 growth (8% instead of 12%), the stock likely has margin of safety. If any reasonable assumptions yield $40 or less, trust the market.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — The foundational framework
- [Gordon Growth Model Assumptions and Limitations](/gordon-growth-model-assumptions/) — Single-stage perpetuity logic
- [Sustainable Growth Rate in Dividend Valuation](/sustainable-growth-rate-dividend-valuation/) — Ensuring payout and growth align
- [Applying the Dividend Discount Model to Non-Dividend Stocks](/dividend-discount-model-non-dividend-stocks/) — Hypothetical dividends and forecasting
- [Terminal Value](/terminal-value/) — Theory behind perpetuity calculations
- [Dividend Distribution](/dividend-distribution/) — Forecasting payout and growth

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Broader DCF framework
- [Cost of Equity](/cost-of-equity/) — The discount rate input
- [Return on Equity](/return-on-equity/) — Driver of sustainable growth
- [Intrinsic Value](/intrinsic-value/) — What valuation models seek to estimate

</div>

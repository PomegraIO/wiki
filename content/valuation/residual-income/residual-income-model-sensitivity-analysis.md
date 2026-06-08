---
title: "Sensitivity Analysis in Residual Income Models"
description: "Demonstrates how changes to cost of equity, ROE fade rate, and terminal assumptions compound into large intrinsic value swings in residual income valuation."
keywords:
  - residual income model sensitivity analysis
  - residual income valuation sensitivity
  - rie model assumptions impact
  - residual income model terminal value
  - residual income model cost of equity
image: /svg/valuation.svg
---

*The **residual income model** is mathematically elegant but fragile: a 1% shift in [cost of equity](/cost-of-equity/) or a change in how quickly [ROE](/return-on-equity/) mean-reverts to cost of capital can swing intrinsic value by 20–40%. Sensitivity analysis exposes these vulnerabilities and reveals which assumptions are load-bearing.*

<div class="wiki-hatnote">

This article assumes familiarity with [residual income valuation](/discounted-cash-flow-valuation/) mechanics: book value, excess returns, and perpetuity formulas. For foundational concepts, see the [discounted cash flow](/discounted-cash-flow-valuation/) and [return on equity](/return-on-equity/) entries.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">RIM Sensitivity — core levers</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation topics." />

<div class="wiki-infobox-caption">Small parameter tweaks produce outsized value swings in residual income models.</div>

|   |   |
|---|---|
| **Model driver** | Sensitivity (typical ±1 change) |
| Cost of equity (ke) | ±15–25% swing in intrinsic value per 1% change |
| ROE fade rate | ±10–20% swing per year of fade acceleration |
| Terminal ROE assumption | ±20–30% swing depending on forecast period length |
| Terminal growth rate | ±5–10% swing per 0.5% increase in perpetuity growth |
| Initial book value | Mechanical impact; less economically loaded than ke or ROE |

</aside>

## The anatomy of residual income model fragility

The residual income model (RIM) values equity as the sum of three components:

1. **Current book value** (the balance sheet starting point)
2. **Present value of forecast-period excess returns** (explicitly projected years, e.g., 5–10 years)
3. **Present value of terminal-period excess returns** (perpetuity or perpetual growth, beyond the forecast)

The formula:

**Intrinsic Value = Book Value₀ + Σ[RI_t / (1 + ke)^t] + [Terminal RI / (ke − g)] / (1 + ke)^n**

Where:
- RI_t = Residual Income in year t = (ROE_t − ke) × Book Value_t−1
- ke = Cost of equity (discount rate)
- g = Terminal growth rate
- n = End of forecast period

The problem: the model's output is hypersensitive to three deeply uncertain inputs: the cost of equity, the fade trajectory of ROE, and the terminal ROE level. Small errors in any of these propagate through both the forecast period and the terminal value, and terminal value often represents 60–80% of total intrinsic value.

## Worked example: a base-case build

**Company:** Stable industrial manufacturer
**Current Book Value (2025):** $50 per share
**Forecast period:** 5 years (2026–2030)
**Terminal assumption:** ROE fades to cost of equity by year 6, held constant thereafter

**Base-case parameters:**
- Cost of equity: 9%
- Forecast-period ROE: starts at 14%, fades linearly to 9% by year 6
- Terminal growth: 2% (long-run GDP growth)
- Book value growth: 6% annually (earnings retained)

**Forecast-period residual income:**

| Year | Book Value | ROE | Net Income | RI = (ROE − ke) × BV₋₁ | PV Factor | PV of RI |
|------|------------|-----|------------|------------------------|-----------|----------|
| 2026 | $53.00 | 14.0% | $7.42 | (0.140 − 0.09) × 50.00 = $2.50 | 0.9174 | $2.29 |
| 2027 | $56.18 | 12.8% | $7.19 | (0.128 − 0.09) × 53.00 = $2.01 | 0.8417 | $1.69 |
| 2028 | $59.55 | 11.6% | $6.91 | (0.116 − 0.09) × 56.18 = $1.46 | 0.7722 | $1.13 |
| 2029 | $63.12 | 10.4% | $6.56 | (0.104 − 0.09) × 59.55 = $0.83 | 0.7084 | $0.59 |
| 2030 | $66.90 | 9.2% | $6.15 | (0.092 − 0.09) × 63.12 = $0.13 | 0.6499 | $0.08 |
| **Total PV forecast-period RI** | | | | | | **$5.78** |

**Terminal value** (at end of 2030, discounted back to 2025):

Starting book value in year 6 = $66.90 × 1.06 = $70.91

At terminal, ROE = ke = 9%, so residual income = 0. But the model assumes growth, so perpetuity is:

**Terminal RI (year 6) = 0** (because ROE = ke)

However, this is a nuance: under the Gordon growth model formulation, if growth > 0 and ROE = ke, the terminal value contribution is still zero in steady state. Some practitioners use a different assumption: ROE stays above ke in perpetuity. Let's recalculate assuming **terminal ROE = 11%** (a 200 basis-point spread above ke):

Terminal RI (year 6) = (0.11 − 0.09) × $70.91 = $1.42

PV of terminal perpetuity = [$1.42 / (0.09 − 0.02)] / (1.09)^5 = [$1.42 / 0.07] / 1.5386 = $20.29 / 1.5386 = **$13.18**

**Intrinsic Value = $50.00 + $5.78 + $13.18 = $68.96 per share**

This is the base case. Now we stress-test the key assumptions.

## Sensitivity to cost of equity

Increasing ke from 9% to 10% (a 100 basis-point increase):

| Component | Change | New Value |
|-----------|--------|-----------|
| PV of forecast RI (discount rate increases) | −$1.02 | $4.76 |
| PV of terminal RI (higher discount rate + denominator grows) | −$3.14 | $10.04 |
| **Total intrinsic value** | | **$64.80** |
| Change from base case | −$4.16 | −6.0% |

Decreasing ke to 8%:

| Component | Change | New Value |
|-----------|--------|-----------|
| PV of forecast RI | +$1.45 | $7.23 |
| PV of terminal RI (lower denominator, stronger terminal RI growth) | +$4.89 | $18.07 |
| **Total intrinsic value** | | **$75.30** |
| Change from base case | +$6.34 | +9.2% |

**Lesson:** A 100 basis-point swing in cost of equity produces a −6% to +9% range around the base case. The effect is asymmetric because lower ke increases both the present value factor and the perpetuity denominator denominator, amplifying the sensitivity. For a stock trading at $70, this narrows the range to $64.80–$75.30 — a material band of uncertainty.

## Sensitivity to terminal ROE and fade rate

In the base case, terminal ROE = 11%. Let's test:

**Terminal ROE = 9% (fades completely to cost of equity):**
- Terminal RI = 0
- PV of terminal RI = 0
- **Intrinsic Value = $50.00 + $5.78 + $0 = $55.78** (−19% from base)

**Terminal ROE = 13% (assumes sustained competitive advantage):**
- Terminal RI (year 6) = (0.13 − 0.09) × $70.91 = $2.84
- PV of terminal RI = [$2.84 / 0.07] / 1.5386 = **$26.36**
- **Intrinsic Value = $50.00 + $5.78 + $26.36 = $82.14** (+19% from base)

This −19% to +19% swing underscores the critical role of terminal assumptions. Terminal value dominates long-term valuations, and small differences in assumed competitive advantage drive massive swings in intrinsic value. A company trading at $70 could theoretically be worth $55–$82 depending on whether you assume mean reversion to cost of capital or sustained outperformance.

## Sensitivity to fade rate (speed of ROE mean-reversion)

In the base case, ROE fades linearly over 5 forecast years. What if fade is faster?

**Fast fade (3 years):** ROE declines 14% → 9% in 3 years instead of 5.

Forecast-period RI shrinks (fewer years of high RI):
- **PV of forecast RI = ~$4.20** (down from $5.78)
- Terminal value is unchanged (same terminal ROE)
- **Intrinsic Value ≈ $50 + $4.20 + $13.18 = $67.38** (−2% from base)

**Slow fade (10 years):** Extend forecast to 10 years; ROE declines more gradually.

More years of above-cost-of-capital returns:
- **PV of forecast RI = ~$8.50** (up from $5.78)
- Terminal value slightly lower (later discount factor)
- **Intrinsic Value ≈ $50 + $8.50 + $11.80 = $70.30** (+2% from base)

A 7-year swing in fade timing moves intrinsic value roughly ±2%. The impact is smaller than cost-of-equity sensitivity because it affects only the forecast period, not the perpetuity denominator.

## Multi-variable sensitivity table

In practice, analysts build a matrix testing multiple assumptions simultaneously. Example 2D table: **Cost of equity vs. Terminal ROE**

| ke ↓ / Terminal ROE → | 9% | 11% | 13% |
|----------------------|-----|-----|-----|
| **8%** | $69.00 | $77.15 | $85.30 |
| **9% (base)** | $55.78 | $68.96 | $82.14 |
| **10%** | $48.50 | $64.80 | $81.10 |

Reading across the base row (ke = 9%):
- Downside (terminal ROE = cost of equity): $55.78 (−19%)
- Base case (terminal ROE = 11%): $68.96
- Upside (terminal ROE = 13%): $82.14 (+19%)

An analyst might define a fair-value range using conservative, base, and optimistic cases:
- **Conservative:** ke = 9.5%, Terminal ROE = 9% → ~$52
- **Base:** ke = 9%, Terminal ROE = 11% → ~$69
- **Optimistic:** ke = 8.5%, Terminal ROE = 12% → ~$77

This bracketing approach acknowledges the model's intrinsic uncertainty rather than false precision.

## Why sensitivity matters

The residual income model is theoretically appealing: it cleanly decomposes value into book value, forecast excess returns, and terminal excess returns. But its output depends critically on unreliable estimates:

- **Cost of equity** is not directly observable; [CAPM](/capital-asset-pricing-model/) estimates vary by 1–2% depending on risk-free rate, beta, and market risk premium assumptions.
- **Terminal ROE** is a pure forecast, often 5–20+ years out. Market conditions, competition, and technological disruption are unknowable.
- **Fade rate** is a modeler's judgment call with no empirical anchor.

Sensitivity analysis is not a defect of the model; it is essential discipline. It forces the analyst to identify which assumptions move the needle and to justify them with conviction. A valuation that is insensitive to reasonable changes in key assumptions is either the result of lucky offsetting errors or a sign that the model has been overfit to the current price.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the parent framework for residual income models
- [Cost of Equity](/cost-of-equity/) — how to estimate the discount rate and its role in sensitivity
- [Return on Equity](/return-on-equity/) — understanding profitability and mean reversion
- [Terminal Value](/enterprise-value/) — methods for valuing cash flows beyond the forecast period
- [Deriving Equity Value Per Share from a Multiples Analysis](/equity-value-per-share-from-multiples/) — alternative valuation method for comparison

### Wider context

- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — framework for deriving cost of equity
- [Balance Sheet](/balance-sheet/) — source of book value inputs
- [Earnings Quality](/earnings-quality/) — evaluating reliability of ROE projections
- [Intrinsic Value](/fair-value/) — the target of all valuation analysis

</div>
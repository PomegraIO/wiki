---
title: "Single-Stage Residual Income Model: Example and Formula"
description: "Worked example of the simplified constant-growth RI formula, showing each input and how intrinsic value derives from book value and perpetual excess returns."
keywords:
  - single stage residual income model
  - residual income model example
  - constant growth residual income
  - residual income valuation formula
  - perpetual growth valuation
---

*The **single-stage residual income model** is the simplest version of residual income valuation. It assumes a firm will sustain a constant level of residual income (or grow it at a constant rate) indefinitely, then discounts that to a present value and adds it to current book value. A worked example shows how each input flows into the formula, making the logic transparent and revealing which assumptions drive the valuation most.*

## The single-stage formula

The perpetual-growth residual income model is:

$$V_0 = BV_0 + \frac{RI_1}{r_e - g}$$

where:
- **V₀** = intrinsic value per share today
- **BV₀** = book value of equity per share
- **RI₁** = expected residual income per share in the next year
- **r_e** = cost of equity (the required return)
- **g** = perpetual growth rate of residual income

Residual income itself is:

$$RI = (ROE - r_e) \times BV$$

The model says: *intrinsic value equals the book value shareholders already have, plus the present value of all future excess returns.*

If a firm earns exactly its cost of equity (ROE = r_e), then RI = 0, and intrinsic value equals book value. If it earns more (ROE > r_e), value is created. If it earns less, value is destroyed.

## Worked example: A stable utility

Consider a regulated electric utility with stable cash flows and predictable growth.

**Given data:**
- Current book value of equity: $1,000 million
- Number of shares outstanding: 100 million
- Book value per share: $10
- Expected net income next year: $120 million
- Cost of equity (estimated via CAPM): 8%
- Perpetual growth rate (assumed): 3% (aligned with GDP growth)

**Step 1: Calculate expected ROE**

Expected ROE = Expected NI ÷ BV₀ = $120M ÷ $1,000M = 12%

**Step 2: Calculate residual income in year 1**

RI₁ (total) = (ROE − r_e) × BV₀ = (12% − 8%) × $1,000M = $40 million

RI₁ per share = $40M ÷ 100M shares = $0.40 per share

**Step 3: Calculate present value of perpetual residual income**

PV(RI) = RI₁ ÷ (r_e − g) = $40M ÷ (8% − 3%) = $40M ÷ 5% = $800 million

Or on a per-share basis:
PV(RI) per share = $0.40 ÷ (8% − 3%) = $0.40 ÷ 5% = $8.00 per share

**Step 4: Add to book value to get intrinsic value**

V₀ = BV₀ + PV(RI) = $1,000M + $800M = $1,800 million total

Or per share:
V₀ = $10 + $8 = **$18 per share**

**Interpretation:** The utility's intrinsic value is $18 per share, compared to a current book value of $10. The $8 premium reflects the present value of the utility's ability to earn a 4 percentage-point spread (ROE − cost of equity) indefinitely. If the stock trades at $18, it is fairly valued. If it trades at $15, it is undervalued. If it trades at $20, it is overvalued.

## Sensitivity to key assumptions

The valuation is highly sensitive to three inputs: cost of equity, growth rate, and the ROE spread.

### Sensitivity to cost of equity

Cost of equity is often the most uncertain input. Let's rerun the example with different assumptions:

| r_e | PV(RI) per share | V₀ per share | P/B ratio |
|-----|------------------|--------------|-----------|
| 7%  | $13.33           | $23.33       | 2.33×     |
| 8%  | $8.00            | $18.00       | 1.80×     |
| 9%  | $5.71            | $15.71       | 1.57×     |
| 10% | $4.44            | $14.44       | 1.44×     |

A 1 percentage-point rise in cost of equity shrinks the intrinsic value by 13–20%. This makes sense: if shareholders' required return rises, future excess returns are discounted more heavily. In a rising-rate environment, residual income models deflate sharply.

### Sensitivity to growth rate

Growth rate feeds the denominator. A higher growth rate raises intrinsic value because residual income is expected to persist longer and compound.

| g | r_e − g | PV(RI) per share | V₀ per share |
|---|---------|------------------|--------------|
| 1% | 7% | $5.71 | $15.71 |
| 2% | 6% | $6.67 | $16.67 |
| 3% | 5% | $8.00 | $18.00 |
| 4% | 4% | $10.00 | $20.00 |
| 5% | 3% | $13.33 | $23.33 |

A 2 percentage-point rise in perpetual growth (from 3% to 5%) lifts intrinsic value by $5.33 per share, a 30% increase. This illustrates the model's sensitivity to long-term growth assumptions. Small errors in growth can swing the valuation significantly.

### Sensitivity to the ROE spread

The width of the ROE-minus-cost-of-equity spread drives the magnitude of residual income.

| Expected ROE | ROE − r_e | RI₁ per share | V₀ per share |
|--------------|-----------|---------------|--------------|
| 10%          | 2%        | $0.20         | $14.00       |
| 11%          | 3%        | $0.30         | $16.00       |
| 12%          | 4%        | $0.40         | $18.00       |
| 13%          | 5%        | $0.50         | $20.00       |

A 1 percentage-point widening of the spread (from 3% to 4%) adds $2 per share of value. This is why competitive advantage and pricing power matter so much in residual income valuation: they determine the sustainable spread.

## Sanity-checking with price-to-book

In the worked example, intrinsic value of $18 per share on book value of $10 yields a price-to-book ratio of 1.8×. Is this reasonable?

For a stable utility with 4 percentage-points of excess return, a P/B of 1.8× is plausible. Growth stocks with 8–10 percentage-point spreads might justify P/B ratios of 3×–5×. Value stocks with 1–2 percentage-point spreads might trade at 1.2×–1.4×. The model output should align with intuition and peer multiples.

If the RI model yields a P/B of 0.5× for a stable business with a positive spread, something is wrong with the assumptions (too-high cost of equity, too-low growth rate, or an incorrectly stated book value).

## When the perpetual-growth assumption breaks down

The single-stage model assumes the ROE and growth rate are both constant forever. This is rarely true in practice:

- **High-growth companies** (biotech, early-stage tech) likely see higher ROE and growth early, then a decline as the firm matures and competition intensifies. A single-stage model overstates their value.
- **Cyclical firms** (airlines, autos) have ROE and growth that vary dramatically with the economic cycle. Assuming a perpetual average spreads the risks but obscures the timing.
- **Regulatory transitions** can shift ROE (new regulations, rate caps, subsidies changes). A single stage can't capture a step change.

For these firms, a **two-stage or three-stage model** is more appropriate: forecast explicit years of higher growth and ROE, then assume a mature perpetual level. But those models are more complex and require more assumption-setting.

## Relationship to net present value of growth

A useful reframing: the residual income model can be thought of as net present value of growth (NPVG) plus the current book value.

$$V_0 = BV_0 + NPVG$$

where NPVG is the present value of all growth in earnings above the cost of capital. This perspective clarifies why book value is the anchor: it represents the value if the firm earns exactly its cost of capital (zero excess growth). Value is created by growth that exceeds the cost of capital.

## Building a sensitivity table for presentations

When presenting a residual income valuation, a two-way sensitivity table is standard. For the utility example:

| Cost of Equity ↓ / Growth → | 2% | 3% | 4% | 5% |
|---|---|---|---|---|
| 7% | $20.00 | $26.67 | $40.00 | $80.00 |
| 8% | $16.67 | $18.00 | $20.00 | $23.33 |
| 9% | $14.29 | $15.71 | $17.14 | $19.23 |
| 10% | $12.50 | $13.33 | $14.29 | $15.56 |

Each cell is the intrinsic value per share. This table shows the valuation across a plausible range of cost-of-equity and growth assumptions. A reader can see both the base-case estimate and how value shifts if assumptions change. The table should highlight the base case (8% cost of equity, 3% growth, yielding $18 per share) so the point estimate is clear amid the sensitivity.

## Common mistakes in single-stage application

1. **Confusing book value growth with residual income growth.** If book equity grows because the firm retains earnings, the model should reflect that explicitly in later years, not assume perpetual flat RI. A true perpetual-growth model requires an assumption about how much of earnings is retained and reinvested.

2. **Using current earnings instead of sustainable earnings.** If the firm is in a cyclical peak year, next-year earnings may be lower. Use a normalized or forward estimate, not a historical average that may embody outdated conditions.

3. **Forgetting that g should not exceed the long-term growth of the broader economy.** A firm cannot grow 8% forever in a 3% economy—it would eventually become larger than the world. g should be anchored to realistic long-term drivers (GDP growth, demographic growth, market-share assumptions).

4. **Ignoring the cost of equity calculation.** If the cost-of-equity estimate is off by 1–2 percentage points (plausible, given estimation error in beta or risk premiums), the valuation can swing 20–30%. Sensitivity analysis is not optional.

## See also

<div class="wiki-seealso">

### Closely related

- [ROE Minus Cost of Equity: The Value-Creation Spread](/roe-minus-cost-of-equity-spread/) — The driver of residual income in this model.
- [Residual Income Model for Financial Firms](/residual-income-model-financial-firms/) — How banks and insurers use the RI framework.
- [Residual Income Model for Intangible-Heavy Firms](/residual-income-model-intangible-heavy-firms/) — Adjustments needed before applying the basic formula.
- [Cost of Equity](/cost-of-equity/) — Estimating r_e, the denominator in the model.
- [Return on Equity](/return-on-equity/) — The numerator; critical to get right.
- Book Value — The anchor of the valuation.
- [Intrinsic Value](/intrinsic-value/) — The target the model estimates.
- [Price-to-Book Ratio](/price-to-book-ratio/) — The valuation multiple implied by the RI model output.

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Alternative valuation method; similar in spirit but different mechanics.
- Net Present Value — The foundation of discounted-value thinking.
- [Relative Valuation](/relative-valuation/) — Comparing firms on multiples instead of absolute value.

</div>
---
title: "Damodaran's Intrinsic Value Method Explained"
description: "Aswath Damodaran's discounted cash flow framework for estimating intrinsic value, with step-by-step projections, growth stages, and discount rate selection."
keywords:
  - damodaran intrinsic value method
  - discounted cash flow valuation
  - intrinsic value calculation
  - terminal value
  - free cash flow projection
image: /svg/people.svg
---

*The **Damodaran intrinsic value method** is a step-by-step discounted cash flow framework that projects a company's future free cash flows, applies a risk-adjusted discount rate, and sums those flows to arrive at a present-day value. Aswath Damodaran, a NYU Stern finance professor, has systematized this approach across thousands of valuations and teaching cases, making it one of the most widely adopted frameworks in investment education and practice.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Damodaran's Method — key facts</div>

<img src="/svg/people.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A systematic DCF framework anchored in explicit growth assumptions and risk-adjusted discount rates.</div>

|   |   |
|---|---|
| **Core inputs** | Free cash flow projections, growth rates, [discount rate](/cost-of-equity/) |
| **Time horizon** | Explicit forecast (5–10 years) + terminal value |
| **Discount rate** | [Weighted average cost of capital](/cost-of-debt/) (WACC) or cost of equity |
| **Key output** | Present value of firm or equity value per share |
| **Strengths** | Transparent, adjustable for scenario, grounded in cash flows |
| **Challenges** | Terminal value dominance, growth rate sensitivity |

</aside>

## The Three-Stage Framework

Damodaran's method divides a company's future into three distinct periods. The **high-growth stage** spans years 1–5 (or sometimes 1–10), when the company reinvests heavily to sustain above-market growth. Free cash flow typically remains modest because growth requires capital spending. The explicit forecast period is where you make your boldest, most defensible assumptions.

The **transition stage** begins when the company matures. Growth rates decline toward the long-term economy rate. Capital intensity may improve, and the [free cash flow](/free-cash-flow/) finally accelerates relative to growth. This bridge period, often 5–10 years, reflects a realistic path from high growth to stability.

The **stable-growth stage** arrives when the company becomes a long-term perpetuity, growing at roughly the GDP growth rate (2–3% for developed economies). Here, reinvestment settles into a steady ratio of earnings, and the bulk of [free cash flow](/free-cash-flow/) can theoretically be distributed.

## Estimating Free Cash Flow

Damodaran insists on starting with operating cash flows and subtracting necessary capital expenditures. Many practitioners mistakenly use earnings or [EBITDA](/ebitda/); Damodaran pushes for precision: what cash leaves the business to sustain or grow operations?

The formula is straightforward:

**Free Cash Flow = Operating Cash Flow − Capital Expenditures + Non-Operating Income**

(Or, working from net income: add back [depreciation](/depreciation/) and non-cash charges, subtract taxes and changes in working capital, then subtract capex.)

For high-growth companies, Damodaran emphasizes that **reinvestment rate** matters enormously. If a company grows at 30% annually, reinvestment is heavy. As growth slows to 3%, reinvestment drops sharply. Failing to model this transition makes early valuations unrealistic.

## The Discount Rate: WACC and Beyond

The discount rate determines how far into the future your cash flows carry weight. A 1% increase in the discount rate can slash valuation by 20–40% if cash flows extend far ahead.

Damodaran advocates using the [weighted average cost of capital](/cost-of-debt/) (WACC) when valuing the entire firm:

**WACC = (E / V) × Cost of Equity + (D / V) × Cost of Debt × (1 − Tax Rate)**

where E and D are market values of equity and debt, and V is the total.

For [cost of equity](/cost-of-equity/), he typically applies the [Capital Asset Pricing Model](/capital-asset-pricing-model/) (CAPM):

**Cost of Equity = Risk-Free Rate + Beta × Market Risk Premium**

A key Damodaran principle: use a **risk-free rate** that matches your cash flow currency and stage (e.g., 10-year Treasury for a 10-year explicit forecast). Mismatch the tenor, and your discount rate will be wrong. The **beta** should reflect the company's actual leverage and business risk, not a sector average. And the **market risk premium**—historically around 5–6% in the U.S.—should be consistent with your assumptions about long-term returns.

## Terminal Value: The Elephant in the Room

In most cases, the [terminal value](/intrinsic-value/) (the value of all cash flows beyond the explicit forecast period) comprises 60–80% of the total valuation. A small change in terminal assumptions can swing the entire answer.

Damodaran typically applies either a **perpetuity growth model** or a **multiple-based exit**. The perpetuity approach:

**Terminal Value = FCF in Year N × (1 + g) / (WACC − g)**

where g is the stable-growth rate. Here, credibility depends entirely on assuming g ≤ long-term GDP growth. If you assume 5% terminal growth in a 2.5% GDP economy, your valuation is fantasy.

The alternative—assuming an exit multiple of, say, 12× EBITDA in year 5—ties valuation to market sentiment at a single point. It's simpler but no less assumption-heavy.

## Sensitivity and Scenario Analysis

Because intrinsic value is so sensitive to a handful of inputs, Damodaran counsels building sensitivity tables. Hold the discount rate constant and vary the terminal growth rate by ±0.5%; note how valuation shifts. Hold growth constant and vary WACC by ±1%. These tables expose which assumptions matter most and where your confidence should end.

Damodaran also endorses scenario analysis: build a base case (realistic, mid-point), an upside case (higher growth, lower risk), and a downside case. Assign probabilities and compute an expected value. This disciplined approach beats single-point forecasts and forces intellectual honesty about the range of plausible outcomes.

## Common Pitfalls

**Circular reasoning**: Using the market stock price as a discount rate or comparing present value to market price without acknowledging the gap is the market's disagreement with your assumptions, not a sign your math is wrong.

**Perpetual high growth**: Assuming 15% growth forever is contradiction. If a company grows faster than the economy forever, it eventually dwarfs the entire market. Damodaran drills this point: stable-stage growth must be defensible at economy-wide scale.

**Ignoring working capital**: A fast-growing retailer building inventory or a SaaS firm offering free trials may show impressive earnings but bleed cash. Damodaran's framework forces you to model this drag.

**Mismatched currencies**: Projecting growth in one currency, then discounting at a rate from another, introduces hidden currency risk. Keep everything consistent.

## Extensions for Multistage Scenarios

Damodaran has adapted his framework for distressed firms (negative earnings, burning cash), cyclic businesses (where normalized earnings differ from any single year), and high-growth disruptors. The logic remains: project the cash flows you believe, discount them at a rate that matches the risk, sum them. The frame is flexible; the discipline is not.

For startups or turnarounds with no positive cash flow yet, the method shifts: value the path to profitability using scenario-weighted outcomes, or value the business at a stable-growth exit and work backward. Either way, you're making explicit forecasts about when and how the company reaches cash-generating maturity.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — foundational concept behind Damodaran's method
- [Cost of equity](/cost-of-equity/) — a key input in WACC and the discount rate
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — framework for estimating cost of equity
- [Free cash flow](/free-cash-flow/) — the actual cash flows being projected
- [Terminal value](/intrinsic-value/) — the dominant component in most DCF valuations
- [Sensitivity analysis valuation](/sensitivity-analysis-valuation/) — testing valuation robustness

### Wider context

- [Intrinsic value](/intrinsic-value/) — the philosophical target of valuation
- [Relative valuation](/relative-valuation/) — alternative approach using multiples
- [Value investing](/value-investing/) — discipline that applies DCF frameworks
- Aswath Damodaran — the thinker and educator behind this method

</div>

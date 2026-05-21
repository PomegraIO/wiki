---
title: "Discounted Cash Flow Valuation"
description: "A valuation method that calculates a company's intrinsic value by projecting its future free cash flows and discounting them back to the present using a risk-adjusted rate."
keywords:
  - DCF
  - valuation
  - discounted cash flow
  - intrinsic value
  - free cash flow
image: "/svg/valuation.svg"
---

*The **discounted cash flow (DCF)** model is the most theoretically rigorous valuation method in finance. It projects a company's future cash flows, discounts each one back to today using a rate that reflects the risk of those cash flows, and sums them to arrive at an intrinsic value. The method rests on a single principle: a dollar earned tomorrow is worth less than a dollar earned today.*

## How DCF works in principle

A DCF model answers the question: what should I pay today for a stream of cash flows I expect to receive in the future? The answer depends on three things: the amount and timing of those cash flows, the riskiness of receiving them, and what else you could do with your money (the opportunity cost).

The formula is straightforward. Take a projected cash flow in year one, divide it by (1 + discount rate), then do the same for year two using (1 + discount rate) squared, and so on for every year in the forecast period. Sum all the discounted cash flows, plus a terminal value—an estimate of what all cash flows beyond the explicit forecast period are worth—and that sum is the company's intrinsic value.

The discount rate, called the weighted average cost of capital, is the rate of return an investor could earn on an equally risky investment elsewhere. If your DCF suggests the stock is worth $100 per share and it trades at $50, you have a $50-per-share margin of safety. If it trades at $150, the market is pricing in expectations of cash flows or growth that exceed your forecast.

## The three building blocks

Every DCF model has the same structure, differing only in complexity:

**Explicit forecast period.** Most models project free cash flows for 5 to 10 years explicitly. This is the period you have the most confidence in—you know the industry, you can assess competitive position, and you have a reasonable view of the cost of capital. The longer the period, the harder it becomes to estimate with conviction.

**Terminal value.** Beyond year ten (or five, depending on your horizon), you collapse all remaining cash flows into a single number: the terminal value. This number is almost always enormous because perpetuity yields a large present value even at a modest growth rate. Most of the value in any DCF comes from terminal value, which is why small changes in perpetual growth assumptions swing valuations wildly. [Perpetuity growth terminal value](/perpetuity-growth-terminal-value/) is the most common terminal-value approach.

**Discount rate.** This is your required return on the investment, adjusted for risk. For an equity investor, this is the [weighted average cost of capital](/weighted-average-cost-of-capital/), which blends the [cost of equity](/cost-of-equity/) and [cost of debt](/cost-of-debt/). For a debt investor, it is a credit-appropriate discount rate. A higher discount rate yields a lower present value; a lower rate yields a higher one.

## Two classical variants

**Unlevered DCF** values the entire enterprise by projecting its free cash flow to the firm—cash generated before debt holders and equity holders take their cuts. You discount at the [weighted average cost of capital](/weighted-average-cost-of-capital/), then subtract net debt to arrive at equity value. This is the canonical approach.

**Levered DCF** projects free cash flow to equity holders directly, already subtracting debt payments and the cost of debt. You discount at the [cost of equity](/cost-of-equity/) alone. This is less common, less stable (the [cost of equity](/cost-of-equity/) can fluctuate as leverage changes), and requires explicit modeling of debt paydown.

For most valuation work, the unlevered approach is cleaner.

## Why DCF dominates in practice

A DCF model forces discipline. You cannot hand-wave; you must choose assumptions about growth, margins, capital expenditure, working capital, tax rates, and terminal value. Those assumptions become visible and contestable. If two analysts differ on value, a DCF conversation exposes exactly where they disagree.

The method also scales. A simple DCF for a software business—projecting 20% growth, 40% EBITDA margins, stable capex, and a 10% discount rate—takes minutes. A detailed DCF for a regulated utility, with dozens of regions, aging assets, and regulatory capex schedules, takes weeks.

## The perpetual tension: forecast accuracy

A DCF's accuracy rests entirely on forecast accuracy, and forecasts decay rapidly. A five-year forecast of cash flow for a stable business is often defensible; a ten-year forecast is a best guess; a perpetual growth assumption is closer to theology than arithmetic. 

This is why the method works best on [mature businesses](/going-concern-valuation/) with predictable earnings and capital needs: utilities, [bonds](/bond/), toll roads, railroads. It works poorly on high-growth startups with unpredictable inflection points or on businesses in disruption where competitive advantage is uncertain. For those, scenario analysis, [real options](/real-options-valuation/), or a [football field](/football-field-valuation/) of valuations is more honest.

## See also

<div class="wiki-seealso">

### Closely related

- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation/) — the most common DCF variant
- [Free cash flow to equity valuation](/free-cash-flow-to-equity-valuation/) — the levered variant
- [Terminal value](/terminal-value/) — the hardest part to estimate
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value/) — the canonical terminal assumption
- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — the discount rate
- [Two-stage DCF](/two-stage-dcf/) — the simplest time-variant
- [Three-stage DCF](/three-stage-dcf/) — explicit ramp to steady state

### Alternatives and complements

- [Multiples valuation](/multiples-valuation/) — faster, market-based, often a sanity check
- [Comparable company analysis](/comparable-company-analysis/) — what multiples does the peer set trade at
- [Scenario valuation](/scenario-valuation/) — explicit bear, base, bull cases
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — which assumptions move the needle
- [Residual income model](/residual-income-model/) — a theoretical alternative

### Inputs

- [Cost of equity](/cost-of-equity/) — a key discount rate component
- [Cost of debt](/cost-of-debt/) — the other component
- [Capital asset pricing model](/capital-asset-pricing-model/) — how to estimate cost of equity
- [Equity risk premium](/equity-risk-premium/) — a key CAPM input

</div>

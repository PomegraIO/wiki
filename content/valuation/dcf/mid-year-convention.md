---
title: "Mid-Year Convention"
description: "A DCF timing adjustment that assumes cash flows arrive at period midpoints, reducing end-of-year bias in valuations."
keywords:
  - mid-year convention
  - dcf adjustments
  - cash flow timing
  - discount-rate application
  - valuation bias
image: /svg/valuation.svg
---

*The **mid-year convention** is a refinement in discounted cash flow analysis that assumes operating cash flows arrive at the midpoint of each period rather than at year-end, reducing a systematic undervaluation of firms with strong, early-period cash generation.*

## Why the end-of-year assumption distorts valuation

Standard DCF models discount cash flows as if they all arrive on 31 December: a year-1 cash flow of £100 at a 10% discount rate becomes £100 ÷ 1.10 = £90.91. In reality, most operating cash flows distribute continuously throughout the year. A business collecting revenue monthly generates half its annual cash in the first six months. Waiting to discount the full year's cash until year-end understates the present value of those early inflows.

The practical effect is material. A firm generating £1 million per year over a decade, discounted at 10%, yields £6.144 million under the standard end-of-year assumption. The same flows discounted at midpoints yield £6.446 million—a 4.9% uplift. For cyclical businesses or those heavily weighted to early-period collection, this gap can swing a valuation decision.

## How the adjustment works

The mid-year convention applies a half-period adjustment factor to the discount rate. If cash flows are assumed to arrive halfway through the year, they face one additional half-year of discounting compared to a flow arriving at the period start, but one less half-year than a flow arriving at year-end.

The adjustment is straightforward: multiply the standard discount factor by the square root of (1 + discount rate). For a 10% rate, this adjustment factor is √1.10 = 1.0488. In practice:

- **Standard DCF**: Year 1 cash flow ÷ (1 + r)¹
- **Mid-year convention**: Year 1 cash flow ÷ [(1 + r)^0.5 × (1 + r)¹]

The net effect is that mid-year cash flows discount back by an additional half-year of the discount rate, correcting the systematic upward bias of assuming all cash arrives at year-end.

## When to use it

The mid-year convention is most appropriate for operating cash flow forecasts—[operating profit](/ebitda/) adjusted for [capital expenditures](/investment-company-act-of-1940/), working capital changes, and taxes. It assumes these flows distribute relatively evenly across the period. Companies with seasonal patterns or lumpy [capital spending](/cap-rate/) may require more tailored adjustments.

The convention is less relevant when valuing streams of discrete events: a bond [coupon payment](/coupon-payment/) scheduled for a specific date should be discounted to that date, not the period midpoint. Similarly, one-time [dividends](/dividend/) or large acquisition proceeds are better timed explicitly.

In academic valuations and textbook examples, the mid-year convention is standard. In commercial practice, investment banks and equity research teams use it unevenly—some apply it consistently, others reserve it for more rigorous engagements, and many omit it entirely when the discount rate is below 5% (making the distortion negligible). It is most common in real estate and [REIT](/real-estate-investment-trust/) valuation, where property income streams are genuinely continuous.

## The relationship to stub periods

If a company's valuation date falls between fiscal year-ends—say, 30 June when the fiscal year closes 31 December—the first forecast period is shorter than a full year. This **stub period** must be handled separately from the mid-year convention. A stub period adjustment typically assumes cash flows are discounted to their actual date, while subsequent full years can use the mid-year convention. The two techniques are complementary; both correct different timing biases.

## Choosing between simplifications

The mid-year convention is more defensible than the end-of-year assumption but introduces a small layer of complexity. If the model uses a long explicit forecast horizon (five years or more) followed by a [terminal value](/discounted-cash-flow-valuation/), the mid-year adjustment applies only to the explicit period; terminal value is typically discounted to the end of the final forecast year, then brought back to the valuation date.

Sensitivity analysis on the assumption is rarely needed—the impact on fair value is usually 2–5%—but when a valuation is tight or a company is highly cyclical, testing the effect is worthwhile. Most commercial models let users toggle the adjustment on or off, making it a one-line comparison.

## See also

<div class="wiki-seealso">

### Closely related

- [Stub Period Adjustment](/stub-period-dcf/) — handling partial fiscal years in DCF models
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the foundational DCF method
- [Fade Rate in DCF Forecasting](/fade-rate-dcf/) — managing forecast decay toward steady state
- [Reinvestment Rate](/reinvestment-rate-dcf/) — the capital reinvestment assumption underpinning growth
- [Discount Rate](/discount-rate/) — the denominator driving present value calculations
- [Terminal Value](/discounted-cash-flow-valuation/) — perpetuity assumptions beyond the explicit forecast

### Wider context

- [Cost of Equity](/cost-of-equity/) — the discount rate for equity cash flows
- [Time Value](/time-value/) — why cash today beats cash later
- [Present Value](/discounted-cash-flow-valuation/) — the mathematics of time-discounted returns

</div>

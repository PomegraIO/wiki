---
title: "Two-Stage DCF"
description: "A simplified discounted cash flow model with an explicit forecast period of high growth followed by a single terminal value assuming stable perpetual growth."
keywords:
  - two-stage DCF
  - two-stage model
  - explicit forecast
  - terminal value
  - perpetual growth
image: "/svg/valuation.svg"
---

*A **two-stage DCF** is the most practical variant of the [discounted cash flow](/discounted-cash-flow-valuation/) model. It divides time into two eras: an explicit forecast period of 5 to 10 years, during which you project cash flows in detail, and a terminal value representing all cash flows from that point onward, grown at a perpetual rate. This simplicity makes it the workhorse of equity research.*

## The structure

Year one through year N—typically 5, 7, or 10—you project free cash flows explicitly. You consider the industry, the company's competitive position, its capital intensity, its tax burden, and market dynamics. These flows are often volatile; a cloud software company might grow at 30% one year and 20% the next.

At year N plus one, you assume the company reaches a steady state and grows forever at a rate you specify. This terminal value is calculated as: free cash flow in year N plus one, times (1 + perpetual growth rate), divided by (discount rate minus perpetual growth rate). The discount rate must exceed the growth rate, or the formula yields infinity.

Sum the present value of all explicit-year cash flows, add the present value of the terminal value, and you have intrinsic equity value.

## Why two stages work

**Honest about uncertainty.** You explicitly forecast only what you believe you can see. Years 6–10 are harder to predict than year 1; making that boundary visible is more honest than burying ten years of wild guesses in an implicit terminal value.

**Scalable to the business.** A maturing SaaS company might use a 7-year explicit forecast and then assume 3% perpetual growth—reasonable for a 25x revenue multiple company. A startup might use 5 years and then assume 2%, or no terminal value at all if the cash-generation assumption is too heroic.

**Separates growth from value.** The explicit forecast captures the unique, near-term growth opportunity. The terminal value captures the baseline business value once the company has matured. This forces you to think clearly about what you're really paying for.

## The terminal value trap

The two-stage model inherits the [DCF](/discounted-cash-flow-valuation/) model's most dangerous assumption: the perpetual growth rate. If you assume 3% instead of 2%, and the discount rate is 10%, the terminal value nearly doubles. The method is therefore highly sensitive to the terminal assumption.

Professional practice uses several guardrails. The perpetual growth rate should not exceed the long-term GDP growth rate of the country where the company operates—for a mature US business, 2–3% is the ceiling. Many analysts instead use an [exit multiple terminal value](/exit-multiple-terminal-value/), projecting year-N EBITDA or earnings, multiplying by a multiple, and discounting that, which sometimes feels less arbitrary.

Another check: calculate the terminal value as a percent of the total intrinsic value. If it exceeds 70–80%, your valuation rests too heavily on an untestable assumption. If it exceeds 90%, the explicit forecast is almost irrelevant; you're really just guessing perpetuity.

## The explicit forecast: practical detail

The explicit period requires projection of seven to ten inputs: revenue, EBITDA or NOPAT, capex, changes in working capital, tax rates, and sometimes incremental maintenance capex. For a mature business, many of these stabilize by year 3 or 4. For a growth business, revenue might ramp for five years, margins expand by year six, and capex intensity peaks then declines.

The depth depends on available information and analytical conviction. A bank analyst modeling a regional lender needs to project loan growth, charge-offs, net interest margins, and operating leverage. A retail analyst modeling a mature apparel company might simply assume revenue flatness and stable margins.

The most common mistake: overcomplicating the explicit forecast with excessive detail, then applying a hand-wavy terminal assumption. The opposite error—a detailed terminal assumption and lazy explicit forecasts—is less common but equally flawed.

## Common variants

**Revenue-based forecasts** start with a top-line projection, then layer margin assumptions, capex, and tax rates. This works well when revenue growth is the primary driver of value.

**EBITDA-based forecasts** begin with an earnings projection, then calculate cash flow by adding back depreciation, subtracting capex, and adjusting for working capital. This works when margins are stable and you have conviction about profitability.

**Return-on-invested-capital (ROIC) based forecasts** assume the company reinvests earnings at a specific return and grows at (ROIC × reinvestment rate). This approach ties valuation directly to the economics of the business and is growing in popularity.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the parent model
- [Three-stage DCF](/three-stage-dcf/) — an explicit transition period for declining growth
- [Terminal value](/terminal-value/) — the hardest assumption
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value/) — the canonical approach
- [Exit multiple terminal value](/exit-multiple-terminal-value/) — an alternative endpoint
- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation/) — the typical cash-flow metric

### Inputs and decisions

- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — the discount rate
- [Cost of equity](/cost-of-equity/) — equity component of discount rate
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — which assumptions drive value
- [Football field valuation](/football-field-valuation/) — presenting a range of outcomes

### Reality checks

- [Comparable company analysis](/comparable-company-analysis/) — implied multiples from the DCF
- [Multiples valuation](/multiples-valuation/) — market-based sanity check
- [Scenario valuation](/scenario-valuation/) — bear, base, bull cases

</div>

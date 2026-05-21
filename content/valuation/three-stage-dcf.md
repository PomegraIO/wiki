---
title: "Three-Stage DCF"
description: "An extended discounted cash flow model that explicitly models a transition period where growth rate declines from a high initial rate to a stable perpetual rate."
keywords:
  - three-stage DCF
  - three-stage model
  - declining growth
  - transition period
  - valuation
image: "/svg/valuation.svg"
---

*A **three-stage DCF** is a refinement of the [two-stage model](/two-stage-dcf) that acknowledges an intermediate reality: most businesses do not leap from high growth to stable growth instantly. Instead, they pass through a transition period—five, ten, or fifteen years—where growth rate declines gradually. A three-stage model makes this decay explicit.*

## The three eras

**High-growth stage.** Years 1–5, 7, or even 10, depending on the business. The company enjoys clear competitive advantages, an addressable market that is itself growing rapidly, or investments that are still ramping. Cash flows expand at a double-digit or higher rate. This stage is firm-specific; each company has a unique window.

**Transition stage.** Years 6–15 or 8–20, depending on when the analyst believes mature-company dynamics will take hold. During this period, growth declines explicitly—perhaps 20% in year 6, 18% in year 7, 15% in year 8, dropping by two percentage points annually until reaching the perpetual rate. This stage forces you to decide when and how quickly advantage erodes.

**Terminal stage.** Year 16 onward, or whatever comes after transition ends. Growth is now perpetual and modest—2–4% for developed-market companies. Cash flows are stable; competitive positioning is assumed unchanged. This stage collapses into a single terminal value.

## When three stages are necessary

**Growth companies with clear fading.** A SaaS company growing 50% today will not grow at 50% forever. A two-stage model that assumes it grows 40% for seven years, then drops to 3% in perpetuity, is jarring and unrealistic. A three-stage model that declines 40% to 38% to 35% to 30% over the first four years, then to 20%, then to 3%, is more credible.

**Capital-intensive businesses in a new market.** Renewable energy, infrastructure, or emerging-market telecom companies often have high growth phases supported by heavy capex, then lower growth once the build-out is complete and the business becomes cash-generative. Three stages capture this rhythm.

**Declining businesses.** A company losing market share or facing disruption might show negative or near-zero growth in perpetuity, after an intermediate period of declining revenues. Three stages can model the descent explicitly.

## Building the transition period

The explicit model of declining growth requires one additional assumption beyond the two-stage model: how fast does growth decline? 

One approach is linear: if high-growth-stage growth is 30% and perpetual growth is 3%, and the transition is ten years, decline by 2.7 percentage points each year. Another is to model specific inflection points—perhaps capex drops in year 6, reducing reinvestment needs and allowing cash flow to decelerate naturally.

The most analytically honest approach is to tie the decline to fundamentals: the disappearance of a specific competitive advantage, the maturation of a market, the need to reinvest at lower returns. If you can articulate why growth should decline, the model becomes a coherent forecast, not a curve-fitting exercise.

## The calculation

The present value of the three-stage valuation is the sum of:

1. Present value of all explicit free cash flows in the high-growth stage
2. Present value of all free cash flows in the transition stage (each discounted at the appropriate year's factor)
3. Present value of the terminal value (calculated from the final year of transition, then discounted back to today)

The mathematics are identical to two-stage; the only difference is that you have more explicit years and a richer growth narrative.

## Pitfalls

**Over-specifying transitions.** If you model 15 years of declining growth, you are making 15 independent forecast assumptions. Confidence decays with each one. A seven-year explicit period—three high-growth, four transition—is often a reasonable compromise.

**Burying the terminal assumption.** Even with an explicit transition, the terminal value usually dominates the valuation. Three stages can encourage overconfidence that you have answered the hard question when you have merely deferred it.

**Path dependence.** The shape of the transition—linear decline, accelerating decline, S-curve decline—matters to the valuation. Without strong conviction, the choice can feel arbitrary.

Many practitioners use three-stage modeling as a sensitivity-check on two-stage valuations: "If I model a 5-year transition instead of assuming instant maturity, does the valuation change materially?" If it does, you know terminal assumptions are fragile. If it does not, the two-stage model is probably robust enough.

## See also

<div class="wiki-seealso">

### Closely related

- [Two-stage DCF](/two-stage-dcf) — the simpler variant
- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — the parent method
- [Terminal value](/terminal-value) — still the key assumption
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value) — the perpetual-growth endpoint
- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation) — the typical metric

### Analysis and sensitivity

- [Sensitivity analysis](/sensitivity-analysis-valuation) — how growth assumptions move value
- [Scenario valuation](/scenario-valuation) — discrete cases instead of curves
- [Football field valuation](/football-field-valuation) — presenting ranges
- [Reverse DCF](/reverse-dcf) — working backward from market price

### Inputs

- [Weighted average cost of capital](/weighted-average-cost-of-capital) — the discount rate
- [Cost of equity](/cost-of-equity) — the key component for equity
- [Market risk premium](/market-risk-premium) — used in cost of equity

</div>

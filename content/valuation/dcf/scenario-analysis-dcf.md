---
title: "DCF Scenario Analysis"
description: "Running bull, base, and bear case DCF models with assigned probability weights to arrive at a probability-weighted fair value."
keywords:
  - scenario analysis
  - base case valuation
  - bull case
  - bear case
  - probability weighting
  - expected value
image: "/svg/valuation.svg"
---

*A **DCF scenario analysis** builds separate, internally consistent [discounted-cash-flow-valuations](/discounted-cash-flow-valuation/) for a company's bull, base, and bear cases, assigns a probability weight to each, and calculates an expected value. Unlike [sensitivity analysis](/sensitivity-analysis-valuation/), which tweaks one variable at a time, scenario analysis holds multiple assumptions constant within each case and weights them coherently.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DCF Scenario Analysis — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Three stories, one probability-weighted verdict.</div>

|   |   |
|---|---|
| **What it is** | Weighted average of multiple DCF models under different assumptions |
| **Also called** | Scenario weighting, case-based valuation, probabilistic DCF |
| **Typical scenarios** | Bull (upside), Base (most likely), Bear (downside) |
| **Probability split** | Often 20%/60%/20% or 25%/50%/25%, adjusted per situation |
| **Output** | Single expected-value price target incorporating range |
| **Differs from** | [Monte Carlo](/monte-carlo-dcf/), which samples distributions randomly |

</aside>

## Why three cases matter more than one

A single-case DCF model is a forecast dressed as certainty. It assumes you nailed the revenue trajectory, margin outlook, capex needs, and terminal growth all at once. Reality is messier. A new competitor could emerge, crushing margins. A regulatory tailwind could lift volumes. The company might execute flawlessly or stumble.

Scenario analysis forces you to articulate **three internally consistent futures**. In the bull case, market share expands, operating leverage kicks in, and return on capital compounds. In the bear case, a competitor cuts prices, the company defends share by sacrificing margin, and growth stalls. The base case sits between: the company grows steadily with some headwinds and tailwinds offsetting. Each scenario is not "what if margin drops 1%" but "in a world where X, Y, and Z all happen together, the valuation is …"

By assigning probabilities—say, 20% bull, 60% base, 20% bear—you're not claiming to know the future, but you're saying: "I've thought through the odds, and here's my expected value." This is far more honest than "$147.32 is the price target" in a single base case.

## Building the three scenarios

**The base case** should reflect consensus expectations and the company's own guidance, with modest adjustments where you have an edge. Revenue grows at the company's long-term sustainable rate (sometimes the industry median). Operating margins improve slightly as the company matures but face incremental cost inflation. Capex stays near historical norms as a percentage of revenue. The [discount-rate](/discount-rate/) uses your best estimate of the [weighted-average-cost-of-capital](/cost-of-debt/). This is the "nobody-is-surprised" future.

**The bull case** assumes your best-case thesis plays out. Perhaps you believe the company is gaining market share faster than consensus recognises, or a new product will restore growth. Margins expand thanks to operating leverage, not because costs magically drop. The capex intensity might drop as the business matures. The discount rate might fall if equity risk premium compresses or beta declines with stability. The terminal growth rate might inch higher, but stays reasonable (no "8% forever" nonsense for a saturated business). The upside is not a fever dream—it is the thesis the market hasn't priced.

**The bear case** is not catastrophe but a credible downside. A competitor takes share. Regulatory changes impose costs. Margin pressure persists. Capex must rise to defend position. The discount rate rises—either because rates spike or because market volatility increases the equity risk premium. Growth disappoints and the company shrinks modestly or plateaus. Again, this is plausible, not apocalyptic. If the bear case assumes the company goes bankrupt, it doesn't belong in a valuation range for an ongoing concern.

Most practitioners assign **probabilities that sum to 100%**: 20% / 60% / 20% is a classic split—slightly weighted toward the base, but acknowledging symmetric tail risk. Some use 25% / 50% / 25% to give more weight to extremes. Your own conviction shapes it. If you are very confident in management and the thesis, maybe 15% / 70% / 15%. If uncertainty is high, 30% / 40% / 30%.

## Calculating the expected value

Each scenario produces a DCF valuation per share:

- Bull case: $190
- Base case: $130
- Bear case: $85

With 20% / 60% / 20% weights:

Expected value = (0.20 × $190) + (0.60 × $130) + (0.20 × $85) = $38 + $78 + $17 = $133

Your price target is $133 per share. This number now embeds your view of the full distribution of outcomes without claiming false precision.

## How scenario analysis differs from Monte Carlo

A [Monte Carlo simulation](/monte-carlo-dcf/) randomly draws thousands of times from probability distributions for each input. Scenario analysis instead builds three discrete, narrative-driven cases. Which is better?

Monte Carlo is more statistically rigorous if your assumptions are truly independent random variables. It reveals tail behaviour and confidence intervals automatically.

Scenario analysis is more intuitive for communicators and forces narrative discipline. You must tell a coherent story: "In the bull case, *because* the market grows and the company captures 60% of new volume, *therefore* margins expand and capex intensity drops." The linkages are explicit, not buried in a correlation matrix. And there's no false precision—no one pretends to know the standard deviation of Q3 2027 EBITDA margin.

In practice, many investors combine both. Run a scenario DCF for your base, bull, and bear narratives. Then sanity-check the range against a Monte Carlo sensitivity test. If they disagree wildly, you've learned something worth investigating.

## Stress-testing scenarios against history

A sound bear case is not pessimism but realism about downside. One way to calibrate: look at the company's worst year in the past decade. What happened to revenue, margins, capex, growth expectations? Did they decline 20%, 40%, 60%? Your bear case should be in the realm of historical precedent, not unimaginable catastrophe.

Similarly, check whether your bull case has ever been achieved. If you're assuming 15% [return-on-equity](/return-on-equity/) forever but the company has never exceeded 12%, you may be too optimistic, or you may have identified genuine operational upside. Either way, the comparison forces discipline.

## Refining probabilities as time passes

Scenario weights are not written in stone. As new information arrives—earnings beats, competitive moves, regulatory clarity—your confidence in each case should shift. A quarter of strong margin beats might upgrade the bull probability from 20% to 30%. A disappointing guidance cut might flip the base and bear. This is not flip-flopping; it is learning.

Some investors periodically recalibrate their scenarios and update their price targets. Others set three-year targets under each scenario and then quarterly update probabilities, letting the expected value creep. Either way, scenario analysis becomes a living framework, not a one-time calculation.

## See also

<div class="wiki-seealso">

### Closely related

- [Monte Carlo DCF Simulation](/monte-carlo-dcf/) — probabilistic alternative using repeated random sampling
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the DCF foundation applied three times
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — testing single-variable impacts within a case
- [Discount Rate](/discount-rate/) — differs across scenarios and shapes valuation materially
- [Terminal Growth Rate](/yield-to-maturity/) — often a key lever across scenarios

### Wider context

- Valuation — conceptual overview of pricing methods
- [Price Target](/price-to-earnings-ratio/) — outcome of scenario analysis and other models
- Risk Management — why multiple scenarios strengthen investment decisions
- Expected Value — philosophical foundation of probability weighting

</div>

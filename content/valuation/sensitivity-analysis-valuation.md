---
title: "Sensitivity Analysis (Valuation)"
description: "A technique that shows how valuation results change when key assumptions (growth, margins, discount rate, terminal value) are varied, revealing which assumptions most impact value."
keywords:
  - sensitivity analysis
  - assumption sensitivity
  - valuation risk
  - tornado chart
  - one-way table
image: "https://picsum.photos/seed/sensitivity-analysis-valuation/900/600"
---

*A **sensitivity analysis** in valuation asks: if my assumption about growth is wrong by 1%, how much does the valuation change? What if discount rate is wrong? Which assumptions move the needle on value the most? It is an essential part of any rigorous DCF or multiples analysis, exposing which assumptions are fragile and which are robust.*

## Basic structure

**Pick a key assumption.** Discount rate, perpetual growth, EBITDA margin, revenue growth, capex intensity.

**Vary it over a range.** Growth from 2% to 5% in 1% increments. Discount rate from 8% to 12%.

**Recalculate valuation at each point.** For each variation, rebuild the DCF and calculate intrinsic value.

**Tabulate or chart.** Show how value changes with the assumption.

## One-way sensitivity table

The simplest form is a one-way table varying one assumption:

| Perpetual growth | Intrinsic value per share |
|---|---|
| 1% | 30 |
| 2% | 40 |
| 3% | 55 |
| 4% | 80 |
| 5% | 130 |

This shows that value is very sensitive to perpetual growth—a 2 percentage point swing yields 100 dollars of value change. If growth is uncertain, the valuation is fragile.

## Two-way sensitivity table

More complex: vary two assumptions simultaneously.

Rows: discount rate (8%, 9%, 10%, 11%, 12%)
Columns: perpetual growth (2%, 3%, 4%, 5%)
Cells: intrinsic value

| WACC \ Growth | 2% | 3% | 4% | 5% |
|---|---|---|---|---|
| 8% | 70 | 100 | 160 | 300 |
| 9% | 55 | 75 | 110 | 180 |
| 10% | 45 | 60 | 85 | 130 |
| 11% | 38 | 50 | 68 | 105 |
| 12% | 33 | 42 | 58 | 85 |

This shows that value depends critically on the combination of discount rate and growth. If both are uncertain, value ranges from 33 to 300—a 9x spread.

## Tornado chart

A graphical sensitivity analysis showing which assumptions have the largest impact on valuation.

For each key assumption, calculate the valuation impact if it swings from low to high:

- Perpetual growth from 2% to 4%: value changes from 40 to 80 (40-point range)
- Discount rate from 8% to 12%: value changes from 70 to 30 (40-point range)
- EBITDA margin from 15% to 25%: value changes from 50 to 65 (15-point range)

Sort by range (largest first). The chart looks like a tornado because the longer bars are at the top.

A tornado chart immediately shows which assumptions matter most. If perpetual growth and discount rate each swing value by 40 points but margins only by 15 points, you should focus your effort on validating growth and discount rate.

## When sensitivity is high vs. low

**High sensitivity.** The valuation is fragile. Small assumption errors cause large valuation errors. These are typically terminal-value assumptions (perpetual growth, discount rate).

**Low sensitivity.** The valuation is robust. Reasonable assumption variations don't move value much. These are typically near-term assumptions (year-1 revenue, year-3 margin).

## Practical implications

**High sensitivity → more caution.** If value is 50 dollars but highly sensitive to growth assumptions, and you are unsure about growth, the valuation is unreliable. Use a wider margin of safety or seek more information before committing capital.

**Low sensitivity → more confidence.** If value is 50 dollars and robust to most assumption variations, you can be more confident in the 50-dollar estimate.

**Identifies key value drivers.** Sensitivity analysis shows what you really need to research and validate. If the valuation hangs on perpetual growth, go find evidence about competitive position, market trends, and management capital allocation to assess whether the growth assumption is credible.

## Limitations of sensitivity analysis

**Linear assumption, but relationships might not be.** If you assume margins improve 1% per year, reaching 25%, but actually the industry is consolidating and will commoditize, the linear assumption is wrong.

**Doesn't capture correlations.** In reality, if growth is high, margins often face pressure (competition intensifies). Sensitivity analysis assumes these move independently. [Monte Carlo](/monte-carlo-valuation) is better for correlations.

**Multiple assumptions can't fail simultaneously.** A true disaster case might involve simultaneous failure of growth, margins, and cost of capital. Sensitivity analysis doesn't easily model this. [Scenario analysis](/scenario-valuation) does.

## Best practice

**Run a one-way table.** Identify which assumptions are most sensitive.

**Run a two-way table** for the two most sensitive assumptions. This shows their joint impact.

**Consider a tornado chart** to visualize which assumptions matter most.

**Understand the correlations.** Explicitly note if assumptions move together or independently.

**Bound the assumptions reasonably.** Don't test perpetual growth from -50% to +50%; test realistic ranges (1–5% for a developed-economy company).

**Sense-check the range.** If sensitivity shows value from 10 to 100 dollars and the stock trades at 40, the wide range suggests valuation is uncertain—acknowledge this in your conclusion.

## Presentation to non-technical audiences

Rather than raw sensitivity tables, you can present as:

- "Our base case value is 50 dollars."
- "If growth is 1% instead of 3%, value is 40 dollars."
- "If growth is 5% instead of 3%, value is 65 dollars."
- "The valuation is sensitive to growth assumptions and less sensitive to near-term margins."

This is simpler and clearer than a table.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — what is being analyzed
- [Terminal value](/terminal-value) — usually most sensitive
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value) — the fragile assumption
- [Weighted average cost of capital](/weighted-average-cost-of-capital) — another sensitive input

### Alternative uncertainty approaches

- [Monte-Carlo valuation](/monte-carlo-valuation) — continuous distributions
- [Scenario valuation](/scenario-valuation) — discrete cases
- [Football field valuation](/football-field-valuation) — ranges and ranges

### Communication

- Tornado chart — visual sensitivity
- Waterfall chart — showing contribution to value

</div>

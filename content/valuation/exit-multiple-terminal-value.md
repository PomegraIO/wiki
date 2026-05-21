---
title: "Exit Multiple Terminal Value"
description: "A terminal value approach that projects year-N EBITDA or earnings and applies an assumed exit multiple, offering an alternative to perpetual growth formulas."
keywords:
  - exit multiple
  - terminal value
  - exit assumption
  - multiples terminal value
  - valuation endpoint
image: "https://picsum.photos/seed/exit-multiple-terminal-value/900/600"
---

*An **exit multiple terminal value** values a company's cash flows beyond the explicit forecast period by assuming the company will be sold (or valued) at a given multiple of year-N earnings or EBITDA. Instead of using a [perpetuity growth formula](/perpetuity-growth-terminal-value), you project year 10 EBITDA (say, 100 million), assume it will trade at 10x EBITDA on exit (1 billion), and discount that 1 billion back to today. This approach feels more grounded in market reality and is often preferred by practitioners.*

## The logic

**Perpetuity growth approach:** Year-10 EBITDA × (1 + g) / (WACC - g) → Terminal value

**Exit multiple approach:** Year-10 EBITDA × Exit multiple → Terminal value

Both yield a single lump-sum value for years 11 onward. The exit multiple approach is often simpler and more intuitive.

## Example

A company has:
- Year 10 projected EBITDA: 100 million
- Assumed exit multiple: 10x EBITDA
- WACC: 10%

Terminal value = 100 million × 10 = 1 billion (in year 10 dollars)

PV of terminal value = 1 billion / (1.10)^10 = 386 million

If explicit-period (years 1–10) cash flows are worth 400 million, total enterprise value is 786 million.

## Why exit multiples can be better than perpetuity

**Observable market multiples.** You can look at the current market and see what multiples peers trade at. An 10–12x EBITDA multiple is market-observed. Perpetual growth of 3% is a guess.

**Incorporates market realities.** If you expect the company to be sold (in a strategic scenario) or valued by a financial buyer, the exit multiple is what you'd actually get.

**Avoids the growth-rate debate.** Instead of arguing about perpetual growth, you argue about reasonable exit multiples (8x or 12x?), which is easier.

**Captures market cycle.** If you are building a 10-year model and expect exit in year 10, using today's multiples might be appropriate, or you might adjust for cycle expectations.

## Challenges

**What multiple is appropriate?**

The exit multiple must be defensible. Is 10x reasonable for this company and industry? If peers trade at 12–15x, why would the exit be only 10x?

Some practitioners use "average" or "normalized" multiples (what the company might trade at through a cycle) rather than current multiples (which might be elevated or depressed).

**Exit multiple vs. perpetual growth are linked.**

An exit multiple of 10x EBITDA on year-10 EBITDA of 100 million, discounted at 10% for 10 years, implies a specific perpetual growth rate. Conversely, a perpetuity formula with specific growth and discount rates implies a terminal multiple.

The two approaches should be reconciled: if you use 10x multiple and 3% perpetual growth, are they consistent?

**Explicit forecasts matter more.**

The exit multiple applies to year-10 EBITDA. If year-10 EBITDA is much higher or lower than today, the exit multiple matters enormously. Small errors in forecasting year-10 EBITDA are magnified.

## Reconciling exit multiple with perpetuity growth

To check if an exit multiple is consistent with a growth assumption:

Terminal value = EBITDA (year N+1) / (WACC - g)

Rearranging: Multiple = (1 + g) / (WACC - g)

If WACC is 10% and perpetual growth is 3%:
Multiple = 1.03 / (0.10 - 0.03) = 1.03 / 0.07 = 14.7x

So a 10x multiple implies perpetual growth of:
10 = (1 + g) / (0.10 - g)
10 × (0.10 - g) = 1 + g
1 - 10g = 1 + g
11g = 0
g = 0%

A 10x multiple at 10% WACC implies zero perpetual growth. An 8x multiple implies negative growth.

This shows that exit multiples often embed lower growth assumptions than might be realistic. If you use a 10x multiple, you should verify that zero perpetual growth is defensible (company matures and stops growing).

## Choosing exit multiples

**Current market multiples.** Look at peers today. If they trade at 10–12x, a 10x exit is reasonable if you don't expect mean reversion or multiple expansion.

**Normalized or through-cycle multiples.** If the industry is currently in a boom (elevated multiples), assume exit at normalized multiples (lower). If in a trough, assume higher exit multiples.

**Discount to peers.** If your company is smaller or riskier than peers, apply a discount. If better positioned, apply a premium.

**Sector/size benchmarks.** Large-cap software companies trade at 25–30x EBITDA; smaller regional software companies at 8–12x. Match the appropriate peer group.

## Sensitivity to exit multiple

Like [perpetuity growth](/perpetuity-growth-terminal-value), terminal value (and thus total valuation) is highly sensitive to exit multiple assumptions.

A change from 10x to 12x EBITDA increases terminal value by 20%. A change to 8x decreases it by 20%.

Running sensitivity on exit multiple is essential. Show valuation at 8x, 10x, and 12x to reveal the range.

## When exit multiples are most useful

**M&A scenarios.** If you are modeling the value assuming the company is acquired in year 10, an exit multiple is the appropriate terminal assumption.

**PE-backed companies.** Private equity models often use exit multiples (the fund plans to sell in years 4–7 at an assumed multiple).

**Short-to-medium forecasts.** If you are modeling 7 years explicitly, a year-7 exit multiple is concrete and easier to justify than perpetual growth.

**Peer comparison.** If you have multiples for all peers, applying those multiples to your target's projected EBITDA is intuitive.

## See also

<div class="wiki-seealso">

### Closely related

- [Terminal value](/terminal-value) — the endpoint being calculated
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value) — the alternative
- [Multiples valuation](/multiples-valuation) — the source of exit multiples
- [Gordon growth model](/gordon-growth-model) — the formula being replaced

### Valuation frameworks

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — uses terminal value
- [Two-stage DCF](/two-stage-dcf) — explicit period plus terminal
- [Comparable company analysis](/comparable-company-analysis) — source of multiple benchmarks

### Integration and testing

- [Sensitivity analysis](/sensitivity-analysis-valuation) — exit-multiple sensitivity
- [Football field valuation](/football-field-valuation) — combining approaches
- [Scenario valuation](/scenario-valuation) — different exit scenarios

</div>

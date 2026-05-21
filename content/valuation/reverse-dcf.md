---
title: "Reverse DCF"
description: "A valuation technique that works backward from a stock's market price to determine the implied assumptions—growth rate, terminal value, or discount rate—embedded in that price."
keywords:
  - reverse DCF
  - implied assumptions
  - market expectations
  - backward engineering
  - valuation check
image: "/svg/valuation.svg"
---

*A **reverse DCF** takes the market price of a stock and asks: what assumptions would justify this price in a DCF model? If the implied growth is impossibly high, the stock is probably overvalued. If the implied growth is lower than you expect, the stock is probably undervalued. It is a powerful sanity check and sentiment indicator.*

## The concept

A standard DCF goes: forecast cash flows → discount to present → get intrinsic value → compare to market price.

A reverse DCF goes: market price is given → solve for the implied growth rate, discount rate, or terminal value that justifies it.

This is algebraically straightforward but requires some setup. A simple case is the [implied growth rate](/implied-growth-rate) from a [Gordon growth model](/gordon-growth-model). More complex versions involve multi-stage DCFs where you solve for a missing parameter.

## Building a reverse DCF

**Step 1: Establish current market price.** Use enterprise value if you are working at the firm level; use equity value if you are valuing equity.

**Step 2: Set up a DCF template.** But leave one variable blank—the variable you will solve for. Usually, it is terminal growth rate.

**Step 3: Specify all other assumptions.** Explicit-period growth, margins, capex, working capital, discount rate. Use forecasts from consensus, your own analysis, or conservative assumptions.

**Step 4: Solve for the blank variable.** Use algebra or trial-and-error (goal seek in Excel) to find what growth rate, discount rate, etc. makes the DCF value equal the market price.

**Step 5: Evaluate.** Is the implied assumption reasonable? If implied growth is 8% and the industry grows at 2%, the stock is expensive (the market is betting on market-share gain or disruption).

## Example

A software company trades at 10 billion in enterprise value. Consensus expects:
- Explicit-period revenue growth: 15% annually for 5 years
- EBITDA margin: 20% by year 5
- Capex and working capital: steady-state
- WACC: 9%

Build a standard DCF with these assumptions. Ignore terminal value for now. The sum of five years of discounted EBITDA might be 2 billion. So terminal value must be 8 billion for total value to be 10 billion.

Working backward: What perpetual growth rate yields a terminal value of 8 billion?

Year-5 EBITDA = 1 billion (rough estimate from revenue and margin).
Terminal value = EBITDA × (1 + g) / (WACC - g) = 1 × (1 + g) / (0.09 - g)

Setting this equal to 8 billion:
1 × (1 + g) / (0.09 - g) = 8
(1 + g) = 8 × (0.09 - g)
1 + g = 0.72 - 8g
9g = -0.28
g = -3.1%

A negative perpetual growth rate? That means the market is pricing in that the business will shrink forever after year 5. That seems wrong. More likely, the market is pricing in either higher growth (disagreement with consensus), or the stock is overvalued.

Let's try assuming 3% perpetual growth (reasonable for a mature software company):

Terminal value = 1 × 1.03 / (0.09 - 0.03) = 1.03 / 0.06 = 17.17 billion

But explicit-period value is only 2 billion, total would be 19.17 billion—much higher than the 10 billion market price.

This suggests the market is pricing in either lower growth, higher cost of capital, or lower margins than consensus expects.

## Applications

**Identifying overvalued sectors.** Calculate implied growth for all stocks in the S&P 500. If growth stocks are implying 8% perpetual growth while the economy grows 2%, the sector is likely overvalued as a whole.

**Spotting value opportunities.** If a company is implying 1% growth but you believe it will grow at 5%, it is undervalued.

**Monitoring sentiment shifts.** If implied growth drops from 5% to 3% without fundamental changes, the market has become pessimistic—possibly a buying opportunity.

**Explaining stock moves.** After a 20% price drop with no earnings misses, what changed? Maybe the market repriced its growth expectations (higher growth implied before the drop, lower after).

**Comparing valuations across peers.** Implied growth for Company A is 4%; for Company B (similar business) it is 6%. Why the difference? Does it reflect real differences, or is one a buy and the other a sell?

## Key assumption to solve for

**Terminal growth rate.** Most common. Solve for the implied perpetual growth given market price, explicit-period forecasts, and WACC.

**WACC / cost of equity.** Given a market price and growth assumptions, what cost of capital is implied? If implied cost is lower than your estimate, the market thinks the stock is less risky than you do.

**Explicit-period growth.** Given a market price and terminal assumptions, what growth rate during the explicit forecast period is implied?

**EBITDA margin.** Given price and growth/discount assumptions, what steady-state margin is implied?

## Interpretation caveats

**The market is not always right.** If implied growth is implausibly high, it doesn't mean the stock will crash tomorrow. It means the market is pricing in aggressive optimism. That optimism might be justified by a product launch, or it might be hype.

**Implied assumptions are not forecasts.** The market is pricing in a consensus of thousands of traders, many of whom have different time horizons and information sets. The implied growth is what the market is willing to pay for, not necessarily the expected outcome.

**The model is only as good as its inputs.** If you use wrong explicit-period assumptions, the implied terminal growth will be wrong.

## When reverse DCF is most useful

**High-visibility companies with stable forecasts.** If consensus is tight on explicit-period growth (everyone agrees 10%), reverse DCF's implied terminal growth is meaningful.

**Monitoring sentiment.** Track implied growth over time. Big shifts are real signals even if they are not perfect forecasts.

**Deciding between two good companies.** Both meet your criteria, but one has implied growth of 3%, the other 5%. The lower-growth one might be the better value.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — the parent model
- [Implied growth rate](/implied-growth-rate) — one specific application
- [Terminal value](/terminal-value) — usually what is being solved for
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value) — the terminal assumption type

### Analysis context

- Market expectations — what reverse DCF reveals
- Sentiment — the emotional component of market price
- Valuation multiple — related metric
- Price-to-book · Price-to-earnings — related multiples

### Integration and testing

- [Sensitivity analysis](/sensitivity-analysis-valuation) — which assumptions drive value
- [Football field valuation](/football-field-valuation) — scenarios and ranges
- [Scenario valuation](/scenario-valuation) — discrete cases

</div>

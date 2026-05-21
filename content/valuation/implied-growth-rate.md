---
title: "Implied Growth Rate"
description: "The perpetual growth rate that a valuation model implies, working backward from a market price or given enterprise value."
keywords:
  - implied growth
  - reverse engineering
  - perpetual growth
  - growth assumptions
  - valuation
image: "/svg/valuation.svg"
---

*An **implied growth rate** is the perpetual growth rate embedded in a current market price. If a stock trades at 50 dollars and you know the company's free cash flow, cost of capital, and current earnings, you can solve for the growth rate the market is pricing in. This backward-engineered growth rate reveals market expectations and helps identify if a stock is over- or underpriced relative to consensus.*

## The logic

Instead of forecasting growth and deriving a valuation, you start with the market price and derive the growth rate. This forces you to ask: "What assumptions would make this price right?"

If the implied growth is 5% and you believe growth will be 2%, the stock is overvalued. If the implied growth is 2% and you believe growth will be 5%, the stock is undervalued.

## Using the Gordon growth formula

Start with the [Gordon growth model](/gordon-growth-model):

Intrinsic value = FCF × (1 + g) / (r minus g)

Rearrange to solve for g:

g = (r × Value minus FCF) / (Value plus FCF)

Or approximately:

g = (r minus FCF / Value)

Where r is cost of capital and Value is the current market price (or enterprise value).

**Example.** A company has:
- FCF = 100 million
- Enterprise value = 1,000 million
- Cost of capital (WACC) = 10%

FCF yield = 100 / 1,000 = 10%

This yield equals cost of capital, so the implied growth rate is roughly 0% (no growth priced in). Any growth above 0% is upside; any growth below 0% is downside.

Another example:
- FCF = 100 million
- Enterprise value = 1,500 million
- Cost of capital = 10%

FCF yield = 6.67%

Using the formula: g = 10% minus 6.67% = 3.33%

The market is pricing in 3.33% perpetual growth.

## Interpretation

**Implied growth vs. consensus.** If consensus expects 5% growth and the implied rate is 3.33%, the stock is overpriced relative to consensus. If consensus expects 2%, the stock is underpriced.

**Implied growth vs. reality.** If you believe the company can grow at 5% for the next 10 years then 2% forever (a three-stage assumption), and the implied rate is 3.33%, is that reasonable? Probably yes—3.33% is a weighted average of the high and low growth rates.

**Sanity check.** Implied growth should not exceed long-term GDP growth (2–3% for developed markets). If it does, either the company is gaining market share forever (rare), or the market is irrationally optimistic.

## Application

**Valuation check.** Build a DCF with your own growth assumptions. Calculate what growth rate your valuation implies. Compare to the market's implied rate. If yours is much higher, you're assuming more aggressive growth than the market; verify this is defensible.

**Identifying overvalued sectors.** Calculate implied growth for all stocks in a sector. If growth stocks are implying 8% perpetual growth while the industry grows 3%, the sector is likely overvalued.

**Spotting value opportunities.** If a company has implied growth of 1% but you believe it will grow at 5%, it is undervalued.

**Monitoring market sentiment.** Track implied growth rates over time. If implied growth for a stock drops from 4% to 2%, the market has become more pessimistic, and the stock has de-rated (lower multiple) even if fundamentals are unchanged.

## The issue: terminal value dominance

Implied growth calculations are most reliable when perpetuity assumptions are important to valuation—i.e., when terminal value is a large portion of total value. For most mature companies, this is true.

For high-growth companies, terminal value might be only 20–30% of value; the implied growth from perpetuity is less meaningful.

## Multistage models

For a company you expect will grow at 20% for 5 years then 3% forever, the implied growth from the Gordon formula is a weighted blend—maybe 8%. This implied growth is useful because it summarizes the expected growth path.

## Reverse DCF

A "reverse DCF" calculation is essentially finding the implied growth rate from market price. It is a powerful tool for:

1. **Sanity-checking your own DCF.** If your DCF implies higher growth than the market, examine why.

2. **Benchmarking against consensus.** Wall Street consensus forecasts growth at 5%; market implies 3%. What will happen if consensus is right?

3. **Identifying changes in sentiment.** If implied growth drops sharply while fundamentals are stable, the market has become pessimistic—possibly a buying opportunity if you disagree.

## See also

<div class="wiki-seealso">

### Closely related

- [Reverse DCF](/reverse-dcf) — the broader concept
- [Gordon growth model](/gordon-growth-model) — the formula used
- [Terminal value](/terminal-value) — what implied growth determines
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value) — the specific terminal approach

### Growth and expectations

- Expected growth — what the market assumes
- Consensus growth forecast — compare to Wall Street
- Growth rate — the underlying metric

### Valuation context

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — uses explicit growth assumptions
- [Sensitivity analysis](/sensitivity-analysis-valuation) — growth sensitivity
- [Football field valuation](/football-field-valuation) — ranges of growth assumptions
- [Scenario valuation](/scenario-valuation) — discrete growth cases

</div>

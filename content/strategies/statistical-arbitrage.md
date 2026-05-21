---
title: "Statistical arbitrage"
description: "Statistical arbitrage is a quantitative strategy of identifying statistical mispricings across multiple stocks or baskets, then taking offsetting positions to capture the mean reversion."
keywords:
  - statistical arbitrage
  - stat arb
  - statistical mispricing
  - mean reversion
  - quantitative arbitrage
  - basket trading
image: "https://picsum.photos/seed/statistical-arbitrage/900/600"
---

*Statistical arbitrage (stat-arb) is a quantitative investment strategy of identifying statistical mispricings among multiple [stocks](/stock/) or assets — using regression models, correlation analysis, or other statistical techniques — then establishing offsetting long and short positions to exploit those mispricings while hedging market risk.*

<div class="wiki-hatnote">

For pairs trading, see [pairs trading](/pairs-trading/). For merger arbitrage, see [merger arbitrage](/merger-arbitrage/). For broader quantitative methods, see [quantitative investing](/quantitative-investing/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Statistical arbitrage — key facts</div>

<img src="https://picsum.photos/seed/statistical-arbitrage/900/600" alt="A basket of stocks identified as statistically mispriced relative to a model" />

<div class="wiki-infobox-caption">Stat-arb strategies identify statistical patterns and exploit them via neutral portfolios.</div>

|   |   |
|---|---|
| **Core idea** | Identify statistical mispricings; create hedged baskets |
| **Market exposure** | Market-neutral; beta ~0 |
| **Scale** | Often involves 20–200+ stocks |
| **Technology** | High; requires models and automated execution |
| **Holding period** | Days to months; until convergence |
| **Return profile** | Consistent but modest (2–8% annually) |
| **Risk** | Model breaks; correlations change; execution slippage |

</aside>

## How statistical arbitrage works

A stat-arb model:

1. **Identifies factors.** Constructs a regression or factor model predicting [stock](/stock/) returns based on characteristics (valuation, momentum, quality, etc.).
2. **Ranks stocks.** Scores all stocks in the universe (e.g., S&P 500) based on the model.
3. **Creates baskets.** Long the highest-scoring stocks (predicted to outperform) and short the lowest-scoring stocks (predicted to underperform).
4. **Sizes positions.** Constructs the long and short baskets with equal gross exposure, ensuring [market risk](/beta/) is neutral.
5. **Monitors and rebalances.** Updates scores regularly, trimming losers, adding winners.

**Example:** A model predicts that stocks with low debt-to-equity ratios and high profitability will outperform for the next month. The strategy:

- **Long:** 20 high-quality, low-leverage stocks, $100 million combined.
- **Short:** 20 low-quality, high-leverage stocks, $100 million combined.
- **Expected return:** If the model is right, the long basket outperforms the short basket, capturing the 50–200 basis point spread.
- **Market exposure:** Zero, since longs and shorts are equal.

## Advantages

- **Market-neutral returns.** Immune to [bull](/bull-market/) or [bear market](/bear-market/) moves; returns depend only on factor performance.
- **Diversification.** Many baskets (50+ stocks) dilute single-stock risk.
- **Systematic and scalable.** Rules-based; can be applied to thousands of stocks mechanically.
- **Multiple factor bets.** A sophisticated stat-arb model can have exposure to value, momentum, quality, and other factors simultaneously.

## Challenges

1. **Model risk.** If the model breaks (factors stop working, relationships change), losses can accelerate.
2. **Crowding.** As more hedge funds use the same factors, mispricings narrow, reducing returns.
3. **Execution costs.** Long 20 stocks and short 20 stocks = 40 transactions. Costs compound.
4. **Correlation breakdowns.** Assumed correlations among stocks may break, especially in crises.
5. **Tail risk.** Models trained on normal data often underestimate crash risk. A sharp market reversal can cause model-wide losses.

## Historical returns

Stat-arb strategies historically delivered 3–8% annualized returns with 5–10% volatility (lower than the broader market). However, as of the 2010s, returns have compressed due to crowding — more capital chasing the same factors.

## See also

<div class="wiki-seealso">

### Closely related

- [Pairs trading](/pairs-trading/) — two-leg stat-arb
- [Quantitative investing](/quantitative-investing/) — broader quant methodology
- [Factor investing](/factor-investing/) — factor-based strategy
- [Systematic investing](/systematic-investing/) — rules-based discipline
- [Merger arbitrage](/merger-arbitrage/) — related arbitrage strategy

### Wider context

- [Stock](/stock/) — the underlying instruments
- [Correlation](/beta/) — the relationship metric
- [Beta](/beta/) — market exposure metric
- [Hedge fund](/hedge-fund/) — typical venue for stat-arb

</div>

---
title: "Cross-Sectional Momentum vs Time-Series Momentum"
description: "Cross-sectional momentum ranks assets against each other (buy best performers); time-series momentum trades an asset against its own history (buy if above trend). Each generates different risk profiles."
keywords:
  - cross sectional momentum vs time series momentum
  - cross-sectional momentum
  - time-series momentum
  - momentum strategy
  - relative momentum
image: "/svg/strategies.svg"
---

*A **cross-sectional momentum** strategy ranks assets against each other and buys the strongest performers; **time-series momentum** buys an asset if it is trading above its own historical average. These are structurally different approaches that produce distinct portfolio characteristics and often negatively correlated returns.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Sectional vs Time-Series Momentum — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for strategies." />

<div class="wiki-infobox-caption">Relative ranking versus absolute trend.</div>

|   |   |
|---|---|
| **Cross-sectional** | Long best performers, short worst performers; market-neutral structure possible |
| **Time-series** | Long if price > trend, short if price < trend; long-biased unless hedged |
| **Timing signal** | Cross-sectional: past 12 months relative return; Time-series: 12-month moving average |
| **Market exposure** | Cross-sectional: hedgeable; Time-series: systematic to broad markets |
| **Crisis behavior** | Cross-sectional: reversal risk, crowded trades; Time-series: whipsaw on trend breaks |
| **Correlations** | Often negative; provide diversification when combined |
| **Asset class** | Stocks typical for cross-sectional; works across all liquid markets for time-series |
| **Implementation cost** | Cross-sectional: turnover can be high; Time-series: lower churn if held long |

</aside>

## Cross-Sectional Momentum: Ranking Within a Universe

**Cross-sectional momentum** looks at a group of assets—say, 500 stocks—and ranks them by recent performance. It buys the top 10% and shorts (or avoids) the bottom 10%, betting that relative strength persists. The signal is *relative*: a stock that gained 30% is attractive not because 30% is a "good" absolute return, but because it beat 90% of its peers.

This approach is sometimes called "relative momentum" or "residual momentum." It answers the question: Which assets are outperforming their peers?

**Example**: In January, you measure the return of the S&P 500 stocks over the prior 12 months. Microsoft gained 45%, Amazon gained 20%, and Golds Sachs fell 5%. You go long the top quintile (Microsoft, Apple, Nvidia, and others) and short or underweight the bottom quintile (GS and peers). The bet is not that these stocks will keep rising in absolute terms; it is that the outperformers will continue beating the underperformers.

Cross-sectional momentum works because of behavioral factors: investors extrapolate trends, momentum traders pile in, and supply-and-demand imbalances persist. It also naturally lends itself to market-neutral structures (equal long and short), which can reduce [systemic-risk](/systemic-risk/) exposure.

## Time-Series Momentum: Trading Against Trend

**Time-series momentum** (also called "absolute momentum") compares an asset's current price to its own historical average—typically a 12-month moving average. If the price is above the average, the asset is said to have positive momentum; you buy or hold. If it drops below, you exit or short.

The signal is *absolute* and historical, not relative to other assets. It answers: Is this asset trending up or down?

**Example**: The S&P 500 is trading at 5,400. Its 12-month average is 5,100. The signal is bullish; you own or increase exposure to the index. Six months later, the S&P 500 has fallen to 4,800—below the moving average. The signal turns bearish; you exit or go to cash. Meanwhile, an individual stock (say, Tesla) may be soaring at the same moment; time-series momentum doesn't care what Tesla is doing—only whether the S&P 500 is above or below its own trend.

Time-series momentum is by nature long-biased for markets in an uptrend. During bull markets, it captures sustained rallies. During bear markets, it exits early and sits in cash or holds short positions.

## Why They Produce Different Returns

Cross-sectional and time-series momentum measure *different market conditions* and often produce uncorrelated or even negatively correlated returns.

**Scenario 1: Broad market rally with rotation**
- The S&P 500 rises 20% over 12 months; every stock is up.
- Time-series momentum is deeply long; the signal is clear positive.
- Cross-sectional momentum, however, sees that all stocks moved together. Ranking them reveals only tiny differences; the strategy is close to market-weight or sideways.
- Time-series thrives; cross-sectional is flat.

**Scenario 2: Market decline with uneven losses**
- The S&P 500 falls 15%; some sectors (tech) fall 30%, others (utilities) fall 5%.
- Time-series momentum exits equities as the price falls below the moving average; the portfolio is in cash or short.
- Cross-sectional momentum is still long utilities (outperformer) and short tech (underperformer); it may be profitable despite the overall decline.
- Time-series avoids losses; cross-sectional captures relative strength.

**Scenario 3: Momentum reversal**
- Stocks that were the best performers for 12 months suddenly begin to underperform; the market is rotating.
- Cross-sectional momentum is still long yesterday's winners and short yesterday's losers. It gets hammered as the leadership changes.
- Time-series momentum, because it looks at absolute trends, is less affected by relative rank changes; if the broad market is still up, it remains long.
- Cross-sectional suffers reversal loss; time-series is resilient.

Empirically, academic research shows correlation between the two strategies ranges from -0.3 to 0.3 depending on the period and asset class. They are often diversifying; holding both can reduce [idiosyncratic-risk](/idiosyncratic-risk/) in a portfolio.

## Implementation and Rebalancing

**Cross-sectional momentum** requires frequent rebalancing. If you rank assets every month, the portfolio turns over significantly. A stock that was top-ranked one month may drop to the middle quintile the next and be sold. This creates trading costs, taxes (in taxable accounts), and slippage.

However, cross-sectional momentum is also naturally suited to liquid markets with tight [bid-ask-spreads](/bid-ask-spread/). Stocks, indices, currencies, and commodity futures are all candidates.

**Time-series momentum** can have lower turnover if you use a wide moving average (e.g., 12 months) and hold for extended periods. Entry and exit signals are less frequent. Transaction costs are often lower. But time-series momentum is also vulnerable to "whipsaws"—false signals when prices briefly cross the moving average and then reverse.

## Asset Class Generality

Cross-sectional momentum is most natural for stocks, where you have a large, homogeneous universe to rank. Applying it to a small number of assets (e.g., five major commodities) reduces diversification and increases idiosyncratic noise.

Time-series momentum generalizes across asset classes. You can apply it to stocks, bonds, currencies, commodities, or cryptocurrencies independently. A systematic time-series momentum strategy might hold long equity [index-funds](/index-fund/), long commodity [futures](/futures-contract/), and long government bonds whenever each asset class is above its moving average. This approach is sometimes called "global tactical asset allocation" and has appealed to institutional investors for its simplicity and [diversification](/diversification/).

## Risk and Performance During Crises

During a sudden market shock—a credit freeze, a geopolitical event—both strategies can suffer:

- **Cross-sectional** faces "crowding" risk. If many investors are using the same ranking system, they all exit the same stocks at once, exacerbating the decline. The "best performing" stock may collapse if sentiment shifts sharply.
- **Time-series** faces "whipsaw" risk. As a crash destroys the moving average signal, the strategy exits (correctly). But if there is a violent rebound, the strategy re-enters (also correct) but may miss the first 20% of the rally due to signal lag.

Empirically, both strategies have survived and profited in various market environments, but neither is crisis-proof. A diversified [hedge-fund](/hedge-fund/) or [quantitative](/algorithmic-trading/) program might hold both to balance the risks.

## Combining Cross-Sectional and Time-Series

A sophisticated investor might use both signals together: go long the best-ranked stocks *only if* they are also above their own moving averages. Or, hold a cross-sectional long/short portfolio *only when* the broad market is in a positive time-series trend.

These hybrids attempt to harness the relative-strength capture of cross-sectional momentum while filtering for broad market health from the time-series signal. The result is often lower turnover, fewer false signals, and better risk-adjusted returns than either strategy alone.

## See also

<div class="wiki-seealso">

### Closely related

- [Momentum investing](/momentum-investing/) — foundational strategy; encompasses both styles
- [Moving average](/moving-average/) — the trend-following tool used in time-series momentum
- [Market cycle](/market-cycle/) — why momentum strategies are profitable in trending markets
- [Trend following](/trend-following/) — broader class of time-series momentum strategies
- [Bid-ask spread](/bid-ask-spread/) — execution cost that matters more for high-turnover cross-sectional strategies
- [Diversification](/diversification/) — how combining strategies reduces risk
- [Algorithmic trading](/algorithmic-trading/) — systematic implementation of momentum signals

### Wider context

- [Hedge fund](/hedge-fund/) — typical institutional deployer of both momentum styles
- [Factor investing](/factor-investing/) — momentum as one factor in multi-factor portfolios
- [Index fund](/index-fund/) — passive alternative; often outperformed by momentum in ranging markets
- Behavioral finance — psychological basis for momentum premiums
- [Business cycle](/business-cycle/) — broader context for when momentum thrives or fails

</div>

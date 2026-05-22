---
title: "Positive Volume Index"
description: "A technical indicator that isolates price movement on days when trading volume increases, used to identify trend direction and investor conviction."
keywords:
  - volume analysis
  - technical indicators
  - market breadth
  - trend confirmation
---

*The **Positive Volume Index** (PVI) is a technical indicator that tracks cumulative price changes on days when trading volume *increases* compared to the previous day. The logic is that rising volume often accompanies genuine trend moves driven by informed investors, while declining volume suggests weak, speculative moves.*

<aside class="wiki-infobox">

| Component | Definition |
|---|---|
| Calculation | Accumulate price changes on up-volume days; ignore down-volume days |
| Interpretation | Rising PVI = uptrend on increasing volume (conviction) |
| Comparison | Negative Volume Index (NVI) tracks down-volume days |
| Range | No fixed range; plotted as cumulative index |
| Typical Usage | Trend confirmation; divergence warnings |
| Signal | PVI crossing above moving average often signals strength |

</aside>

## Core concept: Volume as a vote

The Positive Volume Index is based on the idea that volume reflects investor participation and conviction. When investors buy with increasing volume, they're voting for higher prices with their money—the move is backed by genuine interest. When prices rise on declining volume, fewer investors are participating; the move is fragile and may reverse.

The PVI construction is simple: on days when volume is higher than the previous day, record the percentage price change and add it to the cumulative index. On days when volume declines, ignore the price change and hold the PVI at its prior level. The result is an index that rises only when price moves occur on increasing volume, filtering out low-conviction moves.

If the market rises 1% on a low-volume day, the PVI doesn't change. If the market rises 0.5% on a high-volume day, the PVI increases by 0.5%. Over weeks and months, the PVI trajectory reflects high-volume price moves and can diverge sharply from the actual market index.

## Detecting trend strength and divergence

A rising PVI suggests that uptrends are backed by conviction—rising volume on rallies. A falling or stagnant PVI during a market rally suggests few investors are participating; retail selling or profit-taking may be offsetting institutional buying. This is a red flag for a potential reversal.

Similarly, when the market is in a downtrend and the PVI is rising (because volume is increasing despite prices falling), it signals that selling is heavy and conviction is high. The downtrend is likely to persist.

A divergence occurs when prices make a new high but the PVI doesn't, or vice versa. For example, if the S&P 500 rallies to a new all-time high but the PVI is below its prior peak, it suggests the rally is occurring on lower-volume days. This divergence often precedes a pullback or reversal, as the move lacks sufficient participation.

## Comparing PVI to the Negative Volume Index (NVI)

The Negative Volume Index (NVI) does the opposite: it accumulates price changes on days when volume *declines*. The NVI and PVI together paint a complete picture of price movements across volume regimes.

- A rising PVI + rising NVI suggests that both high-volume and low-volume days are up; the market is in a strong uptrend.
- A rising PVI + falling NVI suggests that up-volume days are rising but down-volume days are falling; an uptrend is intact but weakening on low participation.
- A falling PVI + rising NVI suggests that up-volume days are down but down-volume days are up; a bearish signal, as the most active participation is bearish.

Traders often use the PVI-to-NVI ratio or comparison to assess overall market health. Some technical analysts prefer NVI for longer-term trend identification, arguing that markets peak on high volume (capitulation) and bottom on low volume (disinterest).

## PVI moving averages and crossover signals

The PVI itself is volatile on a day-to-day basis; traders smooth it with a moving average (typically 255-day, a market year). When the PVI crosses above its moving average, it's a buy signal: the high-volume trend is accelerating upward. When the PVI falls below its moving average, it's a sell signal: high-volume moves are turning down.

A 255-day moving average of the PVI is a long-term trend filter. The average itself can be viewed as the "equilibrium" level; deviations above or below signal strength or weakness in the high-volume component of price action.

During strong bull markets, the PVI climbs steadily above its moving average. During bear markets, it falls below and remains depressed. During sideways, choppy markets, the PVI oscillates around its moving average, generating whipsaws.

## Limitations and caveats

The PVI assumes that high volume is always "good" and reflects informed participation. But this isn't always true. Panic selling can occur on very high volume; it's emotional, not informed. Similarly, a low-volume rally can be driven by retail optimism unconnected to fundamental value.

Additionally, the PVI is not a complete picture of market sentiment. A more comprehensive analysis includes [breadth indicators](/wiki/market-breadth-advances-declines/) (how many stocks are rising), [internal strength indices](/wiki/internal-strength-index/), and [price patterns](/wiki/candlestick-pattern/). The PVI is one tool among many.

Another limitation: the PVI is backward-looking. It's a *confirmation* indicator—it confirms that high-volume moves occurred—not a prediction tool. A rising PVI doesn't guarantee future gains; it documents that past gains were on heavy volume, which is a positive, but past does not always predict future.

## Practical application and screening

A trader using the PVI might screen for stocks where the PVI is rising above its 255-day moving average while the [price](/wiki/price-discovery/) is also above its key moving averages (e.g., 50-day, 200-day). This suggests a multi-timeframe uptrend confirmed by volume. A short setup might be a stock where the price is rising but the PVI is falling—a warning of weak participation.

Institutional investors use volume-weighted analyses (of which PVI is a simple version) to assess whether their own large trades are moving markets (market impact). If they buy 1 million shares and the PVI surges, their trade is moving the market with conviction. If volume is light, their trade might be moving the market artificially, and they'd expect reversal once they stop buying.

## Relationship to other volume indicators

The PVI is one of many volume-based technical indicators. The [on-balance volume (OBV)](/wiki/obv-on-balance-volume/) is similar but simpler: add volume on up days, subtract on down days, and plot the cumulative result. The [accumulation/distribution line](/wiki/accumulation-distribution-line/) combines volume and price action to assess whether a stock is accumulating (buying) or distributing (selling) at each price level.

The [Chaikin oscillator](/wiki/chaikin-oscillator/) and [money flow index](/wiki/money-flow-index/) incorporate volume and price to assess momentum. Each has strengths: the PVI is simple and clear, while others incorporate more price-volume nuance. A thorough technical analyst might use multiple indicators to triangulate a signal.

<div class="wiki-seealso">

### Closely related
- [On-Balance Volume](/wiki/obv-on-balance-volume/) — cumulative volume indicator aligned with price direction
- [Accumulation/Distribution Line](/wiki/accumulation-distribution-line/) — indicator combining volume and price
- [Market Breadth](/wiki/market-breadth-advances-declines/) — number of rising vs. falling stocks
- [Volume Participation Order](/wiki/volume-participation-order/) — execution algorithm adjusting to market volume

### Wider context
- [Technical Analysis](/wiki/technical-analysis/) — price and volume pattern analysis
- [Momentum Investing](/wiki/momentum-investing/) — buying recent winners based on price trends
- [Candlestick Pattern](/wiki/candlestick-pattern/) — price action charts showing open, high, low, close
- [Moving Average](/wiki/moving-average/) — smoothed price trend

</div>

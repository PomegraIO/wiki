---
title: "On-Balance Volume (OBV) Indicator"
description: "On-balance volume (OBV) is a technical indicator that accumulates volume on up days and subtracts it on down days to confirm price trends or signal divergence."
keywords:
  - on-balance volume indicator
  - obv technical analysis
  - volume accumulation indicator
  - price volume confirmation
  - volume divergence
image: /svg/technical-analysis.svg
---

*The **on-balance volume** (OBV) indicator is a running cumulative total of volume that rises on days when price closes higher and falls on days when price closes lower. By tracking whether volume is flowing into or out of a security, OBV helps traders confirm whether a price trend has real conviction behind it or whether a divergence suggests a reversal is brewing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">On-Balance Volume — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Volume accumulates when smart money is committed.</div>

|   |   |
|---|---|
| **What it measures** | Cumulative volume weighted by price direction |
| **Calculation** | Add volume on up days, subtract on down days |
| **Signal** | Rising OBV confirms uptrend; falling OBV confirms downtrend |
| **Key insight** | Divergence between price and OBV suggests weakness or reversal |
| **Time window** | Any timeframe; daily and weekly are most common |
| **Interpretation** | Trend strength, confirmation, and reversal warnings |

</aside>

## How OBV is calculated

On-balance volume starts with a simple logic: if the market closed higher than the previous day, all of that day's volume is considered positive (buying volume) and is added to the running total. If it closed lower, that volume is considered negative (selling volume) and is subtracted. If it closes unchanged, the prior total remains unchanged.

For example, suppose an OBV started at zero. Day 1: price rises on 1,000 shares; OBV = +1,000. Day 2: price falls on 1,500 shares; OBV = 1,000 − 1,500 = −500. Day 3: price rises on 2,000 shares; OBV = −500 + 2,000 = +1,500. The line zigzags up and down, reflecting the net flow of volume. A rising OBV line signals that volume is clustering on up days; a falling line signals clustering on down days.

OBV is elegantly crude. It ignores the *magnitude* of the price move—a $0.01 gain counts the same as a $5 gain. This is intentional: the indicator prioritizes *direction* and volume weight, not percentage change. It also assumes that volume on a given day represents the true conviction of buyers or sellers, which is often (but not always) true.

## Confirming trends with OBV

The primary use of OBV is **trend confirmation**. When price and OBV both rise, the uptrend is healthy; volume is flowing to buyers, which suggests the trend has legs. Conversely, if price rises but OBV falls, buyers are losing interest and volume is drying up despite the price gain—a warning sign that the uptrend may stall.

This is particularly useful in the early stages of a breakout from a [chart pattern](//) or from a key support or resistance level. If price breaks out on light OBV, the move may be false or short-lived. A breakout accompanied by rising OBV and heavy volume is much more likely to persist. Many traders use OBV as a secondary confirmation filter: they don't act on a price signal unless OBV backs it up.

The same logic applies to downtrends. A falling price paired with falling OBV (rising negative volume) confirms that sellers are in control. A falling price with rising OBV is incongruent and hints that the downside move lacks conviction.

## Detecting divergence and reversal risk

The most powerful use of OBV is spotting **divergence**—when price and OBV move in opposite directions. For example, price rises to a new high, but OBV fails to reach a new high or even declines. This divergence signals that the price move is not backed by volume, suggesting the uptrend may be running out of gas.

Bullish divergence occurs when price falls to a new low but OBV does not; this suggests selling pressure is waning and a reversal upward could be near. Bearish divergence occurs when price rises to a new high but OBV does not; this warns that the upside move lacks follow-through.

Divergence is not a guaranteed reversal signal—the trend can persist for a long time despite divergence. But it does raise the probability that a trend change is coming, making it a valuable warning to tighten [stop-loss](//) orders or reduce exposure.

## OBV and accumulation/distribution phases

Market participants use OBV to infer whether large institutions or "smart money" are accumulating or distributing a position. Rising OBV in the absence of price gains suggests quiet accumulation—large buyers stepping in without pushing prices dramatically higher. Falling OBV as price holds steady or rises slightly can signal distribution—large holders gradually offloading without crashing the price.

A prolonged period of rising OBV followed by a price breakout is taken as confirmation that the accumulation phase has ended and a move is imminent. Similarly, falling OBV before a price collapse can hint that distribution is complete and downside is coming.

## Limitations and practical use

OBV has notable blind spots. It treats all volume equally, ignoring the fact that some days' volume may be driven by news, short-covering, or other one-off events unrelated to structural buying or selling interest. A stock might gap down on bad earnings, generating heavy selling volume, but then recover the next week—in this case, the heavy down-day volume doesn't accurately reflect the true intent of market participants.

OBV is also slow to react to sudden news or sentiment shifts. If insiders know bad news is coming and gradually offload, OBV will show falling volume, but the price may not drop until the news breaks—at which point OBV finally confirms what astute observers already knew.

For these reasons, OBV is best used alongside other indicators and [price structure](/). A divergence between price and OBV is more compelling if it occurs near a key support or resistance level. A rising OBV confirming an uptrend is more useful if the trend is already established and visible in the price chart.

## OBV on different timeframes

OBV can be applied to any timeframe, but longer-term perspectives (daily, weekly) tend to be more reliable. Intraday OBV (minute or hourly) is noisy and heavily influenced by the natural chop of day trading. Weekly OBV is cleaner and better reflects institutional participation. A trader using a daily chart might look for OBV to align with price over weeks; a day trader might use OBV to confirm intraday momentum over hours or minutes.

The choice of timeframe depends on the holding period and the noise tolerance. Longer-term investors care about weekly or monthly OBV; short-term traders need to filter intraday noise and may prefer volume-weighted price or other order-flow metrics.

## See also

<div class="wiki-seealso">

### Closely related

- [Volume](//) — the raw data underlying on-balance volume
- [Accumulation distribution](//) — a related volume indicator that weights price within the bar
- [Price volume confirmation](//) — the principle that trends need volume backing
- [Momentum](//) — price-based indicators that OBV complements
- [Divergence](//) — when price and indicator move opposite directions

### Wider context

- [Bollinger Band Squeeze: What It Signals](/bollinger-band-squeeze/) — volatility and breakout signals
- [Head and Shoulders Pattern: The Neckline Explained](/head-and-shoulders-neckline/) — pattern confirmation with volume
- [Measured Move in Chart Patterns](/measured-move-chart-pattern/) — projecting breakout targets
- [Technical analysis](//) — the broader framework for price and volume interpretation
- [Market maker trading](/market-maker-trading/) — how institutional volume flows through markets

</div>

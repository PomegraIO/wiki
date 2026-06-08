---
title: "Commodity Channel Index"
description: "A momentum oscillator that measures how far a security's price has moved from its statistical mean, used to identify cyclical turning points."
keywords:
  - commodity channel index
  - cci oscillator
  - technical analysis
  - price momentum
  - cyclical reversal
image: "/svg/technical-analysis.svg"
---

*The **Commodity Channel Index (CCI)** measures the deviation of a security's price from its statistical average, expressed as a ratio of that deviation to the security's typical variation. By flagging when price has strayed far from its mean—either sharply high or sharply low—CCI identifies potential cyclical turning points where mean reversion becomes likely.*

## The formula and what it reveals

CCI compares the current price to a moving average of itself, then normalizes that distance by the security's average deviation. The formula is straightforward: subtract the simple moving average from the typical price (the mean of high, low, and close), then divide by 0.015 times the mean absolute deviation. The result is a dimensionless oscillator that hovers around zero.

When CCI is high (above +100), price has risen far above its recent average. When CCI is low (below −100), price has fallen far below its average. Traders interpret extreme readings—readings beyond ±100 or ±200, depending on strategy—as signals that price has overextended and may be due to revert. CCI values between +100 and −100 represent ordinary range-bound trading where reversion pressure is mild.

## Why normalization matters

The normalization step is what makes CCI useful across different securities and timeframes. A [volatility](/volatility-smile/) measure that does not normalize (like raw standard deviation) inflates for highly volatile stocks and shrinks for stable ones, making cross-comparison misleading. By dividing the deviation by typical deviation, CCI scales itself to each security's natural behaviour. An extreme CCI reading on a utility stock carries the same interpretive weight as an extreme reading on a technology stock, even though the technology stock's price swings are much larger in absolute terms.

This property also allows traders to apply the same threshold settings (e.g., ±100) to any asset class—equities, commodities, currencies, futures. It is one reason CCI gained early adoption among futures and commodity traders before spreading to equity markets.

## Cyclical turning points versus trending markets

CCI was designed for cyclical, range-bound markets. In a sideways-moving market where price oscillates between support and resistance, CCI's extreme readings align well with reversals. When the oscillator spikes above +200 near a local top, the subsequent pullback often brings CCI back toward zero and price back down.

However, CCI performs poorly during strong [trending](/market-timing/) markets. In a sharp uptrend, CCI can remain elevated for weeks, signalling "overbought" conditions that never materialize in an actual reversal. A trader using only CCI in a trending market will suffer repeated false signals—selling short at CCI = +150, only to watch the trend accelerate. This is why experienced traders filter CCI signals through a separate [trend filter](/market-risk/), such as a longer-period moving average, before acting on them.

## Divergence and confirmation

CCI, like other momentum oscillators, is most potent when price and CCI diverge. If price reaches a new high but CCI fails to reach a prior high, that negative divergence warns that momentum is weakening even as price climbs. Sellers may be gradually withdrawing support, a hint that the uptrend is fragile. Similarly, if price falls to a new low but CCI bounces above its prior low, bullish divergence suggests that the downside pressure is abating.

Divergence alone is not a trade. Rather, it is a frame that raises the odds that a reversal is brewing. The trader then waits for confirmation—perhaps a break of a support or resistance level, a moving average crossover, or a candlestick reversal pattern—before committing capital.

## CCI in combination with other indicators

CCI works well alongside [rate of change](/roc-rate-of-change/) and [true strength index](/tsi-true-strength-index/), both of which measure momentum but in subtly different ways. [ROC](/roc-rate-of-change/) is simple and responsive; [TSI](/tsi-true-strength-index/) is smoother and noise-resistant. By combining two or three momentum tools, a trader can cross-check signals and reduce false positives. A short setup might require CCI > +150 AND ROC in decline AND TSI showing negative divergence, a confluence that raises conviction.

Some traders also pair CCI with moving average or band-based reversal systems. The premise is that CCI flags extremes while the bands define the structure within which the extremes occur. A price touching the upper band with CCI > +200 is a stronger sell signal than CCI > +200 alone.

## Period selection and sensitivity

The standard CCI period is 20, but traders adjust it based on the timeframe and asset. A day trader using a 1-minute chart might use CCI(5) to catch very short-term extremes; a swing trader using a daily chart might use CCI(20) or CCI(40) for broader, less noisy signals. The longer the period, the fewer and larger the oscillations; the shorter the period, the more responsive and volatile the indicator becomes.

Sensitivity tuning is always a trade-off. A very sensitive CCI (short period) catches turning points quickly but generates many false signals. A less sensitive CCI (longer period) filters noise but may arrive late to the move. Backtesting on historical price data helps a trader find the setting that works best for their strategy and risk tolerance.

## See also

<div class="wiki-seealso">

### Closely related

- [Rate of Change Indicator](/roc-rate-of-change/) — Simple percentage momentum over a fixed lookback
- [True Strength Index](/tsi-true-strength-index/) — A double-smoothed momentum oscillator with less noise
- [Volatility Smile](/volatility-smile/) — Statistical behaviour of price swings that CCI implicitly measures
- [Market Timing](/market-timing/) — The challenge of entering and exiting positions, where CCI signals assist

### Wider context

- Technical Analysis — The study of price patterns and indicators
- [Algorithmic Trading](/algorithmic-trading/) — Automated systems that often embed CCI rules
- [Price Discovery](/price-discovery/) — The mechanism by which fair value emerges, which CCI exploits
- Support and Resistance — Key price levels that CCI extremes often reverse from
- [Sentiment Analysis](/market-risk/) — Interpretation of investor mood alongside technical indicators

</div>

---
title: "Stochastic Oscillator"
description: "A momentum indicator that measures where a security's price falls within its recent range to identify overbought and oversold conditions."
keywords:
  - stochastic oscillator
  - momentum indicator
  - overbought oversold
  - price range
---

*The **stochastic oscillator** is a [momentum indicator](/wiki/momentum-factor/) that compares a security's closing price to its recent price range (typically 14 periods) to gauge whether the security is overbought or oversold, helping traders identify potential reversals.*

The stochastic oscillator produces two lines: **%K** (the fast line) and **%D** (a moving average of %K, the signal line). %K is calculated as: `(Close – Low) / (High – Low) × 100`, where High and Low are the 14-period highs and lows. The result ranges from 0 to 100. If a stock closes at $105 and its 14-day range is $100–$110, %K = (105–100)/(110–100) × 100 = 50. If the stock is near the top of its range, %K approaches 100 (overbought); if near the bottom, %K approaches 0 (oversold).

The stochastic oscillator is grounded in the observation that during an uptrend, prices *tend to close near the high of the range*, and during a downtrend, near the low. A reading above 80 (overbought) or below 20 (oversold) is flagged as potentially unsustainable, inviting mean reversion or reversal traders.

<aside class="wiki-infobox">

| Parameter | Detail |
|---|---|
| **Period** | 14 days (default; adjusted for longer/shorter timeframes) |
| **Oversold threshold** | Below 20 (or 30 in some variants) |
| **Overbought threshold** | Above 80 (or 70 in some variants) |
| **%K** | Raw fast oscillator (0–100) |
| **%D** | 3-period SMA of %K (signal line) |
| **Signal** | Crossover of %K and %D |
| **Efficiency** | Best in range-bound, choppy markets |
| **Weaknesses** | Lag in trending markets; false signals |

</aside>

## Interpretation and trading signals

Traders use the stochastic oscillator in several ways:

1. **Overbought/oversold extremes**: A reading above 80 suggests the security is overbought (supply may overwhelm demand soon, triggering a pullback). Below 20 suggests oversold (demand may rebound). However, extremes can persist—a stock can be "overbought" for weeks in a strong uptrend, so extremes alone are not reliable sell/buy signals.

2. **Divergence**: If the price hits a new 14-day high but the stochastic oscillator fails to break 80, a **bearish divergence** is flagged—the momentum is weakening even as price pushes higher, potentially a reversal signal. **Bullish divergence** occurs when price hits a new low but %K stays above 20—momentum is not following price down.

3. **Crossovers**: When %K crosses above %D, some traders treat this as a bullish signal (momentum accelerating upward). A %K cross *below* %D is a bearish signal.

4. **Extreme crossovers in extremes**: The most reliable signal is a %K/%D crossover that occurs *while both are in overbought or oversold territory*. For instance, both lines are above 80, then %K crosses below %D—a strong reversal signal in context.

## Slow stochastic vs. fast stochastic

The classic stochastic (fast) uses the raw %K and a 3-period SMA as %D. A **slow stochastic** smooths %K with a 3-period SMA before plotting, reducing whipsaw but adding lag. Traders in choppy markets prefer the fast stochastic (more signals); trend followers prefer the slow stochastic (fewer false alarms).

## Limitations and context-dependency

The stochastic oscillator shines in range-bound, choppy markets. In a strong trending market, a stock can remain "overbought" (above 80) for months, and traders blindly shorting overbought readings incur losses. Conversely, the stochastic lags price movements—it is a **lagging indicator**, updating only after the price has already moved. A sudden gap up bypasses the stochastic entirely.

False signals are common. The indicator performs best when combined with other tools: price support/resistance levels, [moving averages](/wiki/moving-average/), [volume](/wiki/volume-rate-of-change/), and broader market context. A stochastic oversold signal paired with a gap support level and high volume reversal bar is more reliable than oversold alone.

## Comparison to other momentum indicators

The stochastic oscillator is similar to the **[RSI (Relative Strength Index)](/wiki/rsi-relative-strength/)**, which compares up-days to down-days over a period. Both measure momentum and flag extremes, but the stochastic uses a price-range calculation while RSI uses price changes. The stochastic is typically more whipsaw-prone (more signals) but catches turning points faster. RSI is smoother but may lag.

The [MACD](/wiki/macd-indicator/) (moving average convergence divergence) and [Momentum](/wiki/momentum-investing/) (simply price change over a period) are other momentum tools. The stochastic's range-based approach makes it particularly useful for [swing trading](/wiki/swing-trading/) and identifying **mean reversion** opportunities—it assumes prices oscillate within ranges, not trend indefinitely.

## Practical example

A trader is swing-trading Apple stock in a range of $150–$160 (mid-range, $155). Over 14 days, the stock has traded $148–$162. Apple closes at $161 (near the high). %K = (161–148)/(162–148) × 100 ≈ 93, triggering overbought. The trader anticipates a pullback to $156–$157 and shorts on weakness. If Apple falls to $156, the stochastic oscillator normalizes (now around 50), and the trade profits. This is exactly the use case the stochastic was designed for: range-bound markets where extremes predict mean reversion.

<div class="wiki-seealso">

### Closely related
- [RSI Relative Strength](/wiki/rsi-relative-strength/) — momentum oscillator using price changes
- [MACD Indicator](/wiki/macd-indicator/) — momentum using moving average divergence
- [Momentum Investing](/wiki/momentum-investing/) — price-trend following strategy
- [Overbought Oversold](/wiki/overbought-oversold/) — condition the oscillator flags

### Wider context
- [Technical Analysis](/wiki/technical-analysis/) — broader framework for price patterns
- [Swing Trading](/wiki/swing-trading/) — primary use case for stochastic
- [Mean Reversion](/wiki/mean-reversion-investing/) — theoretical driver of reversals
- [Volume Rate of Change](/wiki/volume-rate-of-change/) — complementary volume-based indicator

</div>

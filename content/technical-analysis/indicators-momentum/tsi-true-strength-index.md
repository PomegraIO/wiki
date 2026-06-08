---
title: "True Strength Index"
description: "A double-smoothed momentum oscillator that reduces price noise while preserving the direction of the underlying trend."
keywords:
  - true strength index
  - tsi indicator
  - momentum oscillator
  - double smoothing
  - technical analysis
image: "/svg/technical-analysis.svg"
---

*The **True Strength Index (TSI)** is a momentum oscillator that applies two successive exponential moving averages to the rate of change of price, dramatically reducing noise whilst preserving the signal of trend. The double smoothing allows traders to spot sustained momentum shifts with fewer false signals than simpler indicators.*

## The construction: momentum, smoothed twice

TSI begins with the [rate of change](/roc-rate-of-change/) of price over a short period (typically 1 period, making it simply the price change from one bar to the next). That raw change is then smoothed with a long exponential moving average (typically 25 periods), then smoothed again with a shorter exponential moving average (typically 13 periods). The two-step smoothing is the key innovation.

Why smooth twice? A single exponential moving average flattens the data but lags. Double smoothing applies the lag twice, which feels like a disadvantage, but it creates a peculiar property: the indicator becomes exquisitely sensitive to *changes* in trend direction even as it ignores short-term noise. A trader sees the broad momentum shift without being whipsawed by daily or intraday chop.

The result oscillates around zero, ranging typically from +100 to −100 on a percentage scale. Positive readings indicate upward momentum; negative readings indicate downward momentum. Readings near zero suggest directionless, low-conviction trading.

## Why double smoothing beats single smoothing

Consider a single exponential moving average of momentum. It smooths noise but inherently lags the actual shift in momentum. If price momentum accelerates sharply upward, a single EMA will take many bars to fully reflect that acceleration, arriving late to the signal.

TSI's two-step smoothing paradoxically improves timeliness because the *second* smoothing is applied to an already-smoothed series. The first smoothing strips high-frequency noise (one-bar jitter). The second smoothing then emphasizes the *derivative*—the rate of change of the smoothed momentum. When momentum shifts, that derivative spikes sharply, and TSI reacts. The indicator becomes responsive to turning points while remaining insensitive to noise.

This property is why TSI is favored in choppy, range-bound markets where noise would trigger false signals in simpler momentum tools like [ROC](/roc-rate-of-change/).

## Reading TSI signals and divergences

A basic TSI trade is simple: go long when TSI crosses above zero, go short when it crosses below. This filters out sideways noise (where TSI hovers near zero) and captures trending moves. Many traders add a signal line—a 7- or 9-period EMA of TSI itself—and look for crossovers of TSI above or below that line, a refinement that delays entry but raises confidence.

Divergence is TSI's most potent use. If price reaches a new high but TSI fails to reach a new high, that negative divergence warns that upward momentum is faltering. Sellers are quietly accumulating, a precursor to reversal. The low-conviction divergence becomes high-conviction when price then breaks a support level or TSI crosses below zero.

## Filtering true trends from choppy noise

TSI excels in markets that cycle between trending and sideways phases. During a trending phase, TSI makes large, decisive moves and remains on one side of zero for many bars. A trader riding that trend with TSI as confirmation enjoys many consecutive winning bars. When the trend exhausts and the market enters a choppy range, TSI oscillates near zero and generates whipsaws if used mechanically.

The solution is to add a separate filter—a longer-period moving average or an ADX-style trend strength measure—to tell the trader whether the market is trending or choppy. In choppy regimes, a trader ignores TSI crosses and waits for a clear break; in trending regimes, they take TSI crosses more seriously. This two-layer approach (TSI for momentum, ADX for regime) cuts losses in sideways markets significantly.

## Parameter tuning and timeframe dependency

The standard TSI parameters are 25 for the long EMA and 13 for the short EMA, with a 7-period signal line. These defaults are often right for daily charts and swing trading. For faster timeframes (hourly or 4-hour), traders shorten the parameters: 15 and 8 with a 5-period signal. For slower timeframes (weekly), they lengthen: 35 and 20 with a 9-period signal.

The ratio between the long and short EMA matters more than the absolute values. A 2:1 or 3:1 ratio (long to short) preserves the double-smoothing character. Too-short parameters make TSI respond like [ROC](/roc-rate-of-change/), defeating the purpose of smoothing. Too-long parameters make it so sluggish that entries come late in the move.

## TSI versus Commodity Channel Index and Rate of Change

[CCI](/cci-commodity-channel-index/) measures deviation from a moving average; [ROC](/roc-rate-of-change/) measures simple percentage change. TSI measures the rate of change of smoothed momentum. The three take different angles on the same question: "Is the market accelerating or decelerating?"

On a calm, trending market, all three often agree. But in choppy markets, CCI and ROC generate many false signals while TSI remains relatively quiet, reducing whipsaws. Conversely, TSI lags the initial move because of its double smoothing; a trader using ROC alone might catch the first 1% of an uptrend before TSI confirms.

Many skilled traders run all three together, trusting a signal only when two or three agree. A long entry might require TSI > 0 AND ROC > +2%, a confluence that raises odds meaningfully.

## Practical entry and exit rules

A simple TSI system is:
- Enter long when TSI crosses above its signal line while both are above zero.
- Enter short when TSI crosses below its signal line while both are below zero.
- Exit when TSI crosses back below (longs) or above (shorts) the signal line.
- Tighten stops if TSI begins to diverge from price.

This rule set is mechanical but disciplined, removing emotion from trading. Over dozens of trades, the rule should produce more winners than losers in markets with clear, multi-week trends; in choppy, range-bound markets, it will struggle.

## See also

<div class="wiki-seealso">

### Closely related

- [Rate of Change Indicator](/roc-rate-of-change/) — Simple momentum without smoothing
- [Commodity Channel Index](/cci-commodity-channel-index/) — A normalized deviation oscillator
- Bollinger Band — Moving-average based bands that pair well with TSI
- [Price Discovery](/price-discovery/) — How markets establish fair value, exploited by momentum trades
- Support and Resistance — Price levels where TSI reversals often occur

### Wider context

- Technical Analysis — The study of price patterns and indicators
- [Algorithmic Trading](/algorithmic-trading/) — Automated strategies often embed TSI rules
- [Market Timing](/market-timing/) — The challenge of entries and exits that TSI helps address
- [Volatility Smile](/volatility-smile/) — Statistical behaviour of price movement
- [Trend](/bull-market/) — The directional bias that TSI helps identify and ride

</div>

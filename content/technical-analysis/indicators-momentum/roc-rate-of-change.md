---
title: "Rate of Change Indicator"
description: "A momentum oscillator that expresses price movement as a percentage change over a fixed lookback period, revealing the pace of gains or losses."
keywords:
  - rate of change
  - roc indicator
  - momentum oscillator
  - price velocity
  - technical analysis
image: "/svg/technical-analysis.svg"
---

*The **Rate of Change (ROC) indicator** measures how much a security's price has changed in percentage terms over a fixed number of periods, capturing the velocity of price movement. By expressing momentum as a simple percentage gain or loss, ROC tells traders whether the market is accelerating, decelerating, or reversing direction.*

## The formula and straightforward interpretation

ROC subtracts the closing price N periods ago from today's close, then divides by the price N periods ago and multiplies by 100. The result is a percentage. If a stock closed at 100 yesterday and 110 today, the ROC(1) is +10%. If it closed at 100 ten days ago and 110 today, the ROC(10) is +10%. The period choice (1, 10, 12, 20, or others) determines sensitivity—shorter periods catch quick moves; longer periods smooth out noise.

ROC oscillates around zero. Positive readings mean price is higher than it was N periods ago; negative readings mean it is lower. The magnitude reveals the pace. A ROC of +5% in 20 periods is a slow, steady climb; a ROC of +5% in 5 periods is a sharp spike. High positive ROC readings suggest strong upward momentum; deep negative readings suggest strong selling pressure.

## Acceleration and deceleration as warning signs

ROC's power lies in revealing *changes* in momentum, not just momentum itself. A stock climbing steadily with ROC at +3% each day is healthy. But if ROC begins to fall—from +3% to +2% to +1% to 0%—price is still rising, but acceleration has shifted to deceleration. This cooling of momentum often precedes a full reversal. A trader watching ROC can exit an uptrend early, before the price stops rising altogether.

Similarly, in a downtrend, a falling ROC (becoming more negative) shows accelerating selling. But if ROC begins to rise from −5% toward −3% toward −1%, the downside pressure is easing. That is typically when contrarian buyers step in, before price bottoms.

## Why percentage, not absolute price change

Using percentage change instead of dollar change standardizes the measurement across different securities. A stock advancing from $10 to $12 (+$2) looks modest in absolute terms, but it is a +20% gain—significant momentum. A stock advancing from $100 to $101 (+$1) looks large in absolute terms, but it is only +1% gain—weak momentum. ROC strips away the nominal price and reveals the true rate at which the business value (or speculative value) is growing or shrinking. This makes ROC comparable across different stocks, markets, and eras.

## ROC with divergence to spot weakening trends

ROC reveals divergences that warn of trend reversals. If price reaches a new high but ROC fails to reach a new high, that bearish divergence signals that upward momentum has deteriorated. The price is being pushed higher by fewer, weaker buyers. The reverse is true for downtrends: a lower low in price combined with a higher low in ROC (less negative ROC) warns that selling pressure is evaporating.

Divergence alone does not guarantee a reversal. But it is a shift in the probabilities, and combined with other signals—a break of a support level, a reversal candle, or a moving average crossover—divergence turns a suspicion into actionable conviction.

## Period selection shapes the trade

ROC(12) and ROC(20) are popular on daily charts for swing trading; they balance responsiveness and noise suppression. On a 4-hour or hourly chart, traders often use ROC(5) or ROC(10). The longer the period, the smoother and less responsive ROC becomes, but the fewer false signals it generates. The shorter the period, the noisier and more responsive, catching fast moves but also minor vibrations.

A trader choosing a period should consider their holding time. A day trader holding for minutes uses a very short ROC; a position trader holding for weeks uses a longer ROC. Backtesting on historical data helps reveal which period minimizes whipsaws while capturing the magnitude of moves relevant to the strategy.

## ROC as a filter for trending systems

Many trend-following systems use a simple rule: "go long if ROC is positive, go short if ROC is negative." The system ignores the magnitude and treats ROC as a directional gate. This reduces the number of trades during sideways markets (where ROC hovers near zero) and accepts most of the trades during trends (where ROC is clearly positive or clearly negative). The approach is crude but effective for reducing losses in choppy, mean-reverting ranges.

A refinement is to set a threshold, e.g., "go long only if ROC > +2%," which filters out weak uptrends and captures only those with clear momentum. This raises selectivity and can improve the [win rate](/value-investing/) at the cost of fewer entries.

## Comparison with other momentum tools

ROC differs from [Commodity Channel Index](/cci-commodity-channel-index/) in that CCI normalizes deviation from a moving average, while ROC simply expresses the percentage change. ROC is simpler and more transparent; CCI is more statistically refined. [True Strength Index](/tsi-true-strength-index/) is a smoothed, double-differentiated version of momentum that filters more noise but lags ROC. The three tools often agree on the direction of momentum but diverge on timing. Using two or all three together reduces the odds of a false signal.

## See also

<div class="wiki-seealso">

### Closely related

- [Commodity Channel Index](/cci-commodity-channel-index/) — Another momentum oscillator based on mean deviation
- [True Strength Index](/tsi-true-strength-index/) — A double-smoothed momentum indicator with reduced noise
- [Price Discovery](/price-discovery/) — How markets establish fair value over time
- Support and Resistance — Levels where momentum often stalls or reverses
- [Market Timing](/market-timing/) — The challenge of entering and exiting, where momentum helps

### Wider context

- Technical Analysis — The field of price pattern and indicator interpretation
- [Algorithmic Trading](/algorithmic-trading/) — Automated systems that often encode ROC rules
- [Volatility Smile](/volatility-smile/) — Statistical measure of price swings that underlies momentum
- [Trend](/bull-market/) — The directional bias that ROC helps identify and exploit
- [Value Investing](/value-investing/) — A fundamental approach that can be complemented by momentum signals

</div>

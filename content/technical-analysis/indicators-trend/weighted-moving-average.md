---
title: "Weighted Moving Average"
description: "A moving average that applies linearly increasing weights to recent bars, making it more responsive to current price than a simple or exponential alternative."
keywords:
  - weighted moving average formula
  - wma technical analysis
  - linear weighting moving average
  - price responsiveness indicator
image: "/svg/technical-analysis.svg"
---

*The **Weighted Moving Average** (WMA) is a trend-following indicator that applies steadily increasing weights to the most recent price bars whilst suppressing older values. Unlike the unweighted [simple moving average](/simple-moving-average/), the WMA reacts faster to recent price changes, making it useful for traders who need faster trend confirmation without the jerky responsiveness of short-period averages.*

## Why weight recent bars?

A simple moving average adds all prices equally. A 20-bar SMA gives the first bar and the most recent bar the same influence. This creates lag because the oldest bar still contributes 5% of the total weight. In trending markets, yesterday's price is more relevant than twenty bars ago, yet the SMA treats them identically.

The weighted moving average solves this by assigning weights: the oldest bar in the window gets weight 1, the next bar gets weight 2, and so on until the most recent bar gets weight 20. The sum of prices is then divided by the sum of all weights (1 + 2 + 3 + … + 20 = 210), not by the count of bars. This linear weighting makes the WMA "lean" toward recent action.

The result is mathematically simple but behaviorally powerful: a WMA will rise faster in uptrends and fall faster in downtrends than an SMA of the same period. It turns sooner when price reverses. This responsiveness appeals to swing traders and intermediate timeframe analysts.

## The calculation

For a 5-bar WMA, suppose prices are 100, 102, 101, 103, 104:

- Weighted sum: (100 × 1) + (102 × 2) + (101 × 3) + (103 × 4) + (104 × 5) = 100 + 204 + 303 + 412 + 520 = 1,539
- Sum of weights: 1 + 2 + 3 + 4 + 5 = 15
- WMA = 1,539 ÷ 15 = 102.6

The unweighted 5-bar SMA would be (100 + 102 + 101 + 103 + 104) ÷ 5 = 102. The WMA at 102.6 is slightly higher, pulled up by the recent bars (103, 104). If prices had declined at the end, the WMA would have dropped below the SMA, faster and further.

This weighting scheme is linear: each bar's coefficient increases by 1. Other variations exist—quadratic weighting (1, 4, 9, 16, 25) or exponential weighting—but linear WMA is the standard.

## Responsiveness and lag reduction

The WMA's lag is measurably shorter than an SMA. In a strong uptrend, a 20-bar WMA will be above a 20-bar SMA because the WMA has already pulled forward by recent strength. Conversely, in decline, the WMA falls below the SMA first, signalling exhaustion sooner.

This lag advantage comes at a cost: false signals. In range-bound or choppy markets, the WMA's eagerness to follow recent bars can trigger whipsaws. A brief rally pushes the WMA up; a single reversal bar pulls it down, often triggering premature exit signals. Traders using WMA must accept that their entries and exits will be faster but occasionally premature.

Compared to an [exponential moving average](/exponential-moving-average/) (EMA) at the same period, the WMA is slightly laggier. The EMA decays older values exponentially (exponential decay), so it leans even more heavily toward the most recent bar. However, the difference is small, and the WMA is computationally simpler—no recursive formula needed.

## WMA in trading strategy

Many traders use WMA as a baseline trend filter rather than a standalone signal. A position is only entered long if price is above the WMA and the WMA is rising. Exits occur when price closes below the WMA, or when the WMA flattens or turns down. This simple rule captures swing trends whilst avoiding choppy countertrend trades.

Cross-overs also feature in WMA strategy. A short-period WMA (e.g., 9-bar) crossing above a longer-period WMA (e.g., 20-bar) can signal an emerging uptrend. The reverse signals weakness. Because the WMA is responsive, these crosses occur earlier in the move than they would with SMAs, which can improve entry timing on early trend days.

WMA is particularly effective on timeframes where bars are frequent enough to form distinct swings (hourly, 4-hour, daily). On minute or tick charts, the noise floor is too high; false crosses multiply. On weekly or monthly charts, the WMA's responsiveness advantage diminishes because structural moves span so many bars that even an SMA is timely enough.

## Combining WMA with other tools

WMA alone does not eliminate false signals. To filter entries and exits, traders combine WMA with momentum oscillators. For example, buy only when:
- Price is above the WMA,
- WMA is rising, and
- RSI is above 40 (avoiding extreme oversold, which often precedes reversals).

Or pair WMA with [Bollinger Bands](/bollinger-bands/) or Average True Range: trade only when volatility is moderating (bands tightening) and the WMA is clearly directional. These overlays reduce whipsaws from false WMA crosses.

Some strategies layer two WMAs: a fast (9-period) for tactical moves and a slow (20-period) for strategic direction. Trades are taken when the fast is above the slow and price is above the fast; they're closed when the fast drops below the slow or price closes below either. This two-tier approach captures intermediate swings within longer trends.

## Historical and practical use

The weighted moving average is one of the oldest adaptive averages, predating computer charting. Traders calculated it by hand, maintaining a running tally of weighted prices. It gained popularity in the 1990s with digital charting platforms because the computation became trivial. Today, it remains a staple in technical analysis, though it often appears alongside or beneath exponential moving averages on most charting tools.

The WMA's simplicity—linear weighting, immediate calculation, no parameter tuning beyond the period—makes it approachable for new traders. Yet it is sophisticated enough to serve in multi-indicator systems. It also serves as the foundational building block for more complex averages: the [Hull Moving Average](/hull-moving-average/) stacks WMAs at different periods to reduce lag further, and other adaptive averages inherit the WMA's core weighting logic.

## WMA versus alternatives

The simple moving average remains the most widely understood baseline. If a trader is unsure which average to use, the SMA is a safe default because its lag is well-known and consistent. The WMA is the next step for traders who find the SMA too slow.

The exponential moving average is the third rung. It lags slightly less than the WMA but demands fractional parameters (the smoothing constant alpha) that can be harder to tune. Many traders prefer WMA's straightforward period-based tuning.

Longer-period WMAs can approximate the smoothness of longer-period EMAs with less lag, making them useful for traders who need to hold positions across multiple timeframes. A 40-period WMA might provide similar volatility filtration to a 60-period EMA but turn slightly sooner.

## See also

<div class="wiki-seealso">

### Closely related

- [Simple Moving Average](/simple-moving-average/) — Unweighted baseline; the WMA improves upon
- [Exponential Moving Average](/exponential-moving-average/) — Exponential decay alternative; slightly less lag but more complex
- [Hull Moving Average](/hull-moving-average/) — Stacks WMAs to reduce lag further
- [Triple Exponential Moving Average](/triple-exponential-moving-average/) — Alternative lag-reduction using stacked exponential layers
- [Adaptive Moving Average](/adaptive-moving-average/) — Dynamic speed adjustment based on market conditions

### Wider context

- Technical Analysis — Discipline within which moving averages operate
- [Trend Following](/trend-following/) — Core strategy WMA supports
- Price Action — How recent bars inform WMA direction
- Moving Average Convergence Divergence — Indicator comparing fast and slow moving averages

</div>

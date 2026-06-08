---
title: "Hull Moving Average"
description: "An adaptive moving average developed by Alan Hull that reduces lag and improves responsiveness through weighted sublayer construction."
keywords:
  - moving average lag reduction
  - hull moving average formula
  - technical analysis indicators
  - trend following smoothing
image: "/svg/technical-analysis.svg"
---

*The **Hull Moving Average** (HMA) is a trend-following indicator that combines multiple weighted moving averages at different periods to eliminate lag whilst maintaining smoothness. Developed by Alan Hull, the HMA reweights sublayers using the square root of the lookback period, creating a faster-responding baseline than traditional exponential or simple moving averages at equivalent lengths.*

## The lag problem in moving averages

Any moving average, by definition, lags. It trails price action because it averages historical data—the further back you look to smooth noise, the further behind current price you sit. Traditional approaches accept this tradeoff: longer averages capture trend better but arrive late; shorter ones snap to recent ticks but noise-twitch during choppy consolidation. Traders face a hard choice: responsiveness or reliability.

The Hull Moving Average sidesteps this by stacking multiple weighted averages at different periods and then reweighting them. The formula uses a weighted moving average (WMA) at half the user-specified period and a WMA at the full period, then applies another WMA to their difference. The result is reapplied as a [weighted moving average](/weighted-moving-average/) over a period equal to the integer square root of the lookback. This double-weighting architecture pulls the average forward without sacrificing the smoothness that longer lookbacks provide.

## How the construction works

The HMA typically uses three layers. If you specify a 20-period HMA:

- Compute a WMA over 10 periods (half the lookback).
- Compute a WMA over 20 periods (the full lookback).
- Subtract the 20-period from the 10-period result. This difference highlights the acceleration—where recent prices diverge from the longer baseline.
- Apply a WMA to this difference series using a period of √20 ≈ 4.5 (rounded to 5).

The subtraction step creates a momentum-like derivative. By weighting that momentum overlay, the HMA pulls the final average toward the latest price action without overshooting. The square-root period in the final layer is the elegant constraint: it's short enough to be responsive but long enough to filter one-bar noise.

The construction can be extended: some traders stack four or five layers, each reweighting the residuals, to chase even tighter lag. The tradeoff is complexity and increased whipsaw risk during ranging markets.

## Responsiveness without whip

The key appeal of HMA is its balance. Compared to a 20-period simple moving average (SMA) or exponential moving average (EMA), the HMA of the same lookback will touch price reversals sooner. It turns uptrend confirmations faster and abandons failing rallies with less delay. This faster reaction time makes it attractive for swing traders and position traders who must catch trend changes early.

Yet the HMA does not snap to every bar's close the way a short-period average would. The initial WMA construction already applies linear weighting, suppressing erratic single-bar spikes. The final square-root reweighting stage compounds that smoothing. The result is an average that feels "tight" around price without jigging—it hugs a genuine trend but ignores feints.

In ranging or choppy markets, this responsiveness can be a liability. The HMA will cross above and below price multiple times as sentiment oscillates, triggering false breakout signals. Traders often combine HMA with momentum filters (such as moving-average ribbon distance or momentum oscillators) to reduce whipsaws.

## Comparing moving averages

An EMA at the same period decays older values exponentially, smoothing erratically but arriving at trend turns only slightly later than HMA. The computational overhead of EMA is lower—a single recursive formula—whereas HMA requires three separate moving-average calculations. For real-time charting platforms, the difference is negligible; for backtesting large datasets, it accumulates.

The simple moving average (SMA) at the same period will lag the HMA noticeably because it weights all bars equally. An SMA 20 pulls an equal amount from all 20 bars; an HMA 20 front-loads the recent bars via the WMA sub-layers. This makes HMA useful for traders who want SMA's interpretability but EMA's snap.

Weighted moving averages themselves (linear weighting) are a natural intermediate. A WMA 20 will lead an SMA 20 but trail an HMA 20 because the HMA's stacked construction extracts and amplifies the recent-price acceleration signal.

## In practice

HMA works best on intraday charts (1-hour, 4-hour) and daily timeframes where trend reversals occur over several bars. On minute charts, the noise floor is too high; the HMA's responsiveness becomes a curse, generating whipsaws. On weekly or monthly charts, even the HMA's speed advantage shrinks because structural trend moves unfold over many bars anyway.

Traders often use HMA in combination with other indicators. A typical setup pairs HMA with RSI or MACD to filter entries: only go long when HMA is rising and momentum oscillators agree, only short when HMA is falling and momentum confirms. This layering reduces false signals from HMA's solo responsiveness.

Some traders watch HMA slope or apply acceleration filters—if HMA flattens whilst price rises, trend is likely exhausted. Others watch for crossovers: HMA 9 crossing above HMA 20 as a buy signal, the reverse as a sell. These are heuristics, not guaranteed rules, but they exploit the HMA's responsiveness to capture turning points more reliably than longer-period simple or exponential averages.

## Speed versus stability

The core tension in HMA design is speed versus stability. By using a square-root-period final layer, Hull chose a middle ground: responsive enough to catch real trend turns early, stable enough to ignore noise and single-bar reversals. Traders who want even more speed can reduce the square-root multiplier (use a linear or smaller square-root scale). Those who want more stability can extend the final WMA period or stack additional reweighting layers.

The HMA is not a silver bullet. It reduces lag, but lag reduction always comes at the cost of increased whipsaw risk in ranging markets. It is best used as a component in a multi-indicator system rather than a standalone entry or exit rule.

## See also

<div class="wiki-seealso">

### Closely related

- [Weighted Moving Average](/weighted-moving-average/) — Linear weighting approach that powers HMA's sub-layers
- [Exponential Moving Average](/exponential-moving-average/) — Recursive smoothing that decays older bars; slightly laggier but lower-overhead alternative
- [Simple Moving Average](/simple-moving-average/) — Unweighted baseline; the lag HMA seeks to reduce
- [Triple Exponential Moving Average](/triple-exponential-moving-average/) — Alternative lag-reduction scheme using stacked exponential layers
- [Adaptive Moving Average](/adaptive-moving-average/) — Dynamic smoothing speed based on market efficiency ratio

### Wider context

- Technical Analysis — Framework within which moving averages operate
- [Trend Following](/trend-following/) — Trading approach HMA supports with faster turn signals
- Momentum — The force HMA's subtraction layer attempts to capture
- Moving Average Convergence Divergence — Related indicator pairing fast and slow averages

</div>

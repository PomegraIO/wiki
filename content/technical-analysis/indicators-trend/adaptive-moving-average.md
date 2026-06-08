---
title: "Adaptive Moving Average"
description: "A moving average that dynamically adjusts its smoothing speed based on the market's efficiency ratio, responding faster in trending markets and slower in choppy conditions."
keywords:
  - adaptive moving average kama
  - kaufman adaptive moving average
  - dynamic smoothing indicator
  - efficiency ratio technical analysis
image: "/svg/technical-analysis.svg"
---

*The **Adaptive Moving Average** (KAMA, or Kaufman Adaptive Moving Average) is a trend-following indicator that adjusts its responsiveness dynamically based on how efficiently price is moving. Developed by Perry Kaufman, KAMA measures the ratio of directional movement to overall price change, slowing when price is choppy and accelerating when price is trending smoothly—solving the problem of fixed-period averages.*

## The fundamental problem with fixed periods

A standard moving average uses a fixed period. A 20-bar EMA always has the same responsiveness; it treats choppy, sideways markets the same as trending markets. In consolidation, this leads to whipsaws: the average crosses above and below price repeatedly, triggering false breakout signals. In smooth uptrends, the same period is slow to respond; entries arrive late.

An ideal average would shift shape based on market conditions: slower (longer period) when price is random, faster (shorter period) when price trends. Kaufman's insight was to quantify this condition using an efficiency ratio and embed it into the smoothing constant itself.

## The efficiency ratio

The efficiency ratio (ER) compares the direction of price movement to the total distance travelled. Over the lookback period:

- **Change** = absolute value of (close today − close N bars ago)
- **Volatility** = sum of absolute bar-to-bar changes over N bars
- **ER** = Change ÷ Volatility, ranging from 0 to 1

If price rises steadily upward, change equals volatility (all movement is directional), so ER approaches 1. If price oscillates—up one bar, down the next, sideways—change is small but volatility is high, so ER approaches 0.

This ratio is elegant. It captures "trending-ness" without subjective parameters. ER near 1 signals a trend; ER near 0 signals choppy consolidation.

## Dynamic smoothing constant

The KAMA formula uses ER to scale the exponential smoothing constant. The smoothing constant (alpha) normally depends on the lookback period. For EMA, alpha = 2 ÷ (period + 1). Kaufman modifies this:

- Define a fastest smoothing constant: alpha_fast = 2 ÷ (2 + 1) = 0.667 (equivalent to a 2-bar EMA).
- Define a slowest smoothing constant: alpha_slow = 2 ÷ (longest period + 1), often 30 bars, yielding about 0.0625.
- Scale between them: alpha_scaled = ER × (alpha_fast − alpha_slow) + alpha_slow.

The KAMA is then computed as a standard EMA, but with this dynamic alpha:

KAMA = KAMA_previous + alpha_scaled × (price − KAMA_previous)

When ER is high (trending), alpha_scaled approaches alpha_fast (0.667), making KAMA snap to price like a 2-bar EMA. When ER is low (choppy), alpha_scaled approaches alpha_slow (0.0625), making KAMA smooth like a 30-bar EMA. The transition is continuous and automatic.

## Adaptive response in practice

In a strong uptrend where every bar closes higher, ER is near 1. KAMA accelerates, rising quickly with price. Entries triggered on KAMA crossovers or proximity to price occur early in the move.

When price enters consolidation, ER collapses. KAMA downshifts to slow smoothing, flattening out. The false crosses that plague fixed-period averages in ranging markets are suppressed. KAMA becomes sticky, reducing whipsaws.

As the trend resumes, ER climbs again. KAMA automatically speeds up, catching the breakout sooner than fixed-period alternatives. This self-adjusting behaviour is why KAMA appeals to traders: it adapts to market conditions without manual tuning.

## Comparing to fixed alternatives

A 20-bar [exponential moving average](/exponential-moving-average/) is the closest fixed-period analog. In trending markets, KAMA (running at alpha_fast ≈ 0.667) is far faster, turning weeks earlier. In choppy markets, KAMA (at alpha_slow ≈ 0.0625) is far smoother, avoiding false crosses.

The tradeoff is that KAMA introduces two additional parameters: the ER lookback (often 2 or 5 bars) and the slowest-period definition (often 20 or 30 bars). These require testing and tuning. A trader using a standard EMA can plug in "period 20" and move on; KAMA demands consideration of how efficiently price must move to be considered "trending."

The [Hull Moving Average](/hull-moving-average/) and [Triple Exponential Moving Average](/triple-exponential-moving-average/) achieve lag reduction through mathematical layering (weighting or stacking). KAMA achieves it through dynamic period adjustment. All three operate on the same frontier: faster response in trends, lower whipsaw in ranges.

## Tuning KAMA

The ER lookback controls how recent the efficiency assessment is. A 2-bar ER is myopic; it reacts aggressively to single-bar reversals. A 5-bar ER is more stable. A 10-bar ER captures structural trends but misses short-term swings.

The slowest-period parameter defines how conservative KAMA becomes in choppy conditions. A 30-bar slowest period makes KAMA extremely smooth in choppy markets (like a 30-bar EMA), but it also stalls trend recovery when volatility drops. A 20-bar slowest period is more balanced. Traders select this based on their target holding period: swing traders favour faster slowest periods (15–20); position traders favour slower (30–50).

The fastest period is usually fixed at 2 bars and rarely adjusted. Some traders extend it to 3 or 4 bars if KAMA whips too much during strong trends, though this sacrifices some of the speed advantage.

## In trend-following strategy

KAMA is used as the core trend filter in many algorithmic strategies. The rule is simple: go long when price is above KAMA and KAMA is rising; go short when price is below KAMA and KAMA is falling; exit the opposite signal. Because KAMA adjusts to market efficiency, this single rule captures most intermediate swings without the parameter-optimization burden of fixed-period averages.

Some traders layer multiple KAMA periods. A 9-period KAMA (ER on 2 bars) and a 20-period KAMA (ER on 5 bars) can define fast and slow trends. Trades are taken when the fast KAMA is in the same direction as the slow KAMA and price agrees with both. This reduces false signals from short-term noise.

KAMA works particularly well on daily and weekly charts where structural trends are pronounced and parameter selection is less sensitive. On minute charts, the efficiency ratio becomes too granular; one or two bars of reversal noise can flip the ER from 1.0 to 0.5, causing KAMA to whip between fast and slow modes. On intraday charts (1-hour, 4-hour), KAMA is effective if tuned for that timeframe's typical swing length.

## Combining with confirmation indicators

KAMA alone, like any moving average, can generate false signals. Pairing KAMA with momentum-based indicators strengthens the approach. For example:

- Buy only when price is above KAMA, KAMA is rising, and RSI is above 50.
- Sell when price falls below KAMA or RSI falls below 40.

Or use KAMA with Volume: entries on KAMA breaks are more reliable when volume is rising. This layering converts KAMA from a directional filter into part of a multi-indicator system.

Some traders use KAMA's slope as a signal. A KAMA that is rising but flattening suggests the trend is weakening; a KAMA that is flat and then suddenly steep suggests an emerging trend. These are heuristics, but they exploit KAMA's adaptive nature to anticipate changes in efficiency.

## Limitations and nuance

KAMA assumes that trending markets deserve faster response and choppy markets deserve slower response. This is often true, but not always. During panic-driven selloffs, the market is both highly directional (high ER) and highly volatile. KAMA accelerates, which is good for early exits, but it can also increase whipsaw risk if the panic reverses suddenly.

In grinding, low-volatility consolidations, ER is low, and KAMA slows. Yet boring sideways markets sometimes break explosively. KAMA's slowness during the consolidation means entry signals lag when the breakout occurs. Traders must accept this tradeoff: smoothness in chop for speed in trends.

Parameter selection is non-trivial. A KAMA tuned for 4-hour charts may not work on daily charts; efficiency ratios behave differently across timeframes. Backtesting and live validation are essential. This is true of all adaptive indicators, but KAMA's dynamic nature makes it more sensitive to parameter drift.

## See also

<div class="wiki-seealso">

### Closely related

- [Exponential Moving Average](/exponential-moving-average/) — Fixed-period baseline; KAMA adapts this using efficiency ratio
- [Hull Moving Average](/hull-moving-average/) — Stacked weighted construction; alternative lag-reduction approach
- [Triple Exponential Moving Average](/triple-exponential-moving-average/) — Stacked exponential layers; similar responsiveness goals
- [Weighted Moving Average](/weighted-moving-average/) — Linear-weighting alternative; does not adapt
- Average True Range — Volatility measure often paired with KAMA for confirmation

### Wider context

- Technical Analysis — Framework within which KAMA operates
- [Trend Following](/trend-following/) — Core strategy KAMA supports
- Volatility — Factor KAMA indirectly measures via efficiency ratio
- Momentum — Force KAMA aims to capture in trending markets
- Moving Average Convergence Divergence — Related dual-EMA indicator

</div>

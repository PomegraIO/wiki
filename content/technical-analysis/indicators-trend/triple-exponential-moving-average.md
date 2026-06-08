---
title: "Triple Exponential Moving Average"
description: "A moving average that applies three successive exponential smoothing layers to minimise lag whilst preserving trend clarity, reducing noise compared to single EMA smoothing."
keywords:
  - triple exponential moving average
  - tema technical indicator
  - lag reduction exponential
  - trend confirmation indicator
image: "/svg/technical-analysis.svg"
---

*The **Triple Exponential Moving Average** (TEMA) is a trend-following indicator that reduces lag by compounding three exponential smoothing passes at the same period. Developed to capture trend turns faster than a standard [exponential moving average](/exponential-moving-average/), TEMA uses the difference between single, double, and triple EMA layers to extract and amplify the acceleration signal whilst suppressing noise.*

## The lag problem in exponential averages

An exponential moving average decays older bars exponentially, weighting recent bars heavily. It is faster than a simple moving average but still lags. In a sharp uptrend, the EMA trails price by a fixed delay—roughly one-quarter of the lookback period. For a 20-bar EMA in a steep move, you wait 5 bars for the average to fully respond, missing the early portion of the trend.

Traders could use a shorter EMA to reduce lag, but short averages snap to noise. A 5-bar EMA is responsive but whips around with every bar; a 20-bar EMA is smoother but late. TEMA sidesteps this choice by stacking three exponential layers, extracting and reapplying the acceleration signal to pull the average forward without sacrificing smoothness.

## Three layers of exponential smoothing

The TEMA formula uses three successive exponential moving averages, all at the same user-specified period. If the period is 20:

1. Compute the first EMA (EMA1) over 20 bars.
2. Compute the second EMA (EMA2) as an EMA of EMA1.
3. Compute the third EMA (EMA3) as an EMA of EMA2.

Then combine them: TEMA = (3 × EMA1) − (3 × EMA2) + EMA3.

This formula is elegant. The three-times weighting of EMA1 (the base) pulls the average toward recent price. Subtracting three times EMA2 (the "slowest" layer) removes inertia. Adding back EMA3 (the slowest layer applied twice) eliminates whipsaw. The result is an average that reacts faster without overshooting.

## How the layers interact

Think of EMA2 as the trend if it were even more lagged than EMA1. Subtracting it highlights how much the base trend has accelerated away from the over-smoothed version. By adding back EMA3, we dampen that acceleration slightly, preventing the TEMA from spiking on single-bar anomalies.

Visually, TEMA appears as a line that hugs price more tightly than an EMA but without the jitter of a short-period average. In a clear uptrend, the TEMA rises smoothly with price, turning up before the standard EMA and falling before it during corrections. In choppy markets, the layers cancel out some of the noise, but not all—the TEMA can still whip around during ranging action.

The period parameter matters enormously. A 20-period TEMA responds faster than a 20-period EMA but behaves like a 5-to-8-bar EMA in terms of jitter. Traders sometimes use longer TEMA periods (30, 50) to recover smoothness, then gain speed by shortening it again. The point is to dial in the right balance for your timeframe and trading style.

## Comparing to other lag-reduction methods

The [Hull Moving Average](/hull-moving-average/) also reduces lag but uses linear weighting instead of exponential decay. HMA is arguably more elegant conceptually (a single formula using weighted sub-layers) whilst TEMA is more computationally straightforward if you already have an EMA function available.

In practice, HMA and TEMA are close cousins. A 20-bar HMA and a 20-bar TEMA will lag nearly identically, usually within half a bar. The choice between them is often stylistic: HMA practitioners like its weighted construction; TEMA practitioners appreciate the pure exponential decay aesthetics.

The [weighted moving average](/weighted-moving-average/) (WMA) is simpler than both but lags slightly more. A standard [exponential moving average](/exponential-moving-average/) lags noticeably more. Short-period simple moving averages are fast but noisy.

## Practical trading use

TEMA is best used as a trend confirmation filter or swing target rather than a standalone signal generator. A common pattern:
- Go long when price closes above the TEMA and the TEMA is rising.
- Exit when price closes below the TEMA or the TEMA turns down.

This rule keeps traders aligned with the intermediate trend captured by TEMA's period. Because TEMA responds faster, the exit comes earlier in a drawdown, protecting capital before large retracements.

Some traders layer two TEMA periods: a fast (9-bar) and a slow (20-bar). The fast TEMA is used for tactical entry and exit; the slow TEMA defines strategic direction. Trades are taken when the fast is above the slow and price is above both; they are closed when the fast drops below the slow. This nested approach balances responsiveness with stability.

TEMA is particularly effective on intraday charts (1-hour, 4-hour) where trend swings are pronounced and price reversals occur over a handful of bars. On minute charts, even TEMA's lag-reduction advantage is insufficient; the noise floor dominates. On weekly or monthly charts, standard EMAs are usually sufficient because structural trends are slow enough to be captured without urgency.

## The smoothness-responsiveness frontier

All moving averages exist on a spectrum. Longer periods are smoother but slower; shorter periods are responsive but jumpy. TEMA and HMA are attempts to break this tradeoff by using mathematical tricks—layering and reweighting—to push the frontier closer to "fast and smooth."

The cost is complexity. TEMA requires computing three EMAs; HMA requires three WMAs and a square-root calculation. On modern systems, this overhead is negligible, but conceptually, these averages are harder to explain and trust than a simple EMA. Traders new to TEMA should not expect it to work without testing on their specific market and timeframe.

TEMA also inherits the EMA's parameter sensitivity. The smoothing constant (alpha) for an EMA of period 20 is defined as 2 ÷ (20 + 1). Adjust the period slightly—say, 19 instead of 20—and the responsiveness changes noticeably. TEMA compounds this: small period changes produce large behavioural shifts across three layers. Traders must be disciplined about period selection.

## Combining TEMA with other indicators

TEMA alone generates false signals in choppy markets. To improve reliability, combine TEMA with a momentum oscillator. For example:
- Buy when price is above TEMA, TEMA is rising, and MACD is positive.
- Sell when price falls below TEMA or MACD turns negative.

Or pair TEMA with ATR (Average True Range): trade only when volatility is stable or declining, signalling reduced noise and clearer trend direction. This layering dramatically reduces whipsaws from TEMA's solo responsiveness.

Some mean-reversion traders use TEMA in reverse: they trade against it. When price touches TEMA from above or below, momentum often reverses, offering short-term countertrend opportunity. This approach requires tight stops and careful risk management but can capture mean-reversion trades that breakout traders miss.

## See also

<div class="wiki-seealso">

### Closely related

- [Exponential Moving Average](/exponential-moving-average/) — Single-layer exponential baseline; TEMA improves upon this
- [Weighted Moving Average](/weighted-moving-average/) — Linear-weighting alternative to exponential decay
- [Hull Moving Average](/hull-moving-average/) — Stacked weighted construction; similar lag-reduction goal as TEMA
- [Adaptive Moving Average](/adaptive-moving-average/) — Dynamic smoothing speed based on market efficiency
- [Simple Moving Average](/simple-moving-average/) — Unweighted baseline; more lagged than any adaptive variant

### Wider context

- Technical Analysis — Framework within which TEMA operates
- [Trend Following](/trend-following/) — Core strategy TEMA supports
- Moving Average Convergence Divergence — Related dual-EMA indicator
- Momentum — Force TEMA's layering attempts to capture
- Volatility — Often paired with TEMA for entry and exit filtering

</div>

---
title: "EWMA Volatility Model Explained"
description: "Learn the EWMA volatility model—exponential weighting, how lambda is chosen, how it compares to simple historical volatility, and its role in risk measurement."
keywords:
  - ewma volatility model
  - exponentially weighted moving average volatility
  - ewma lambda decay factor
  - ewma vs historical volatility
  - variance estimation
image: "/svg/risk.svg"
---

*The **EWMA (exponentially weighted moving average) volatility model** estimates variance by assigning higher weight to recent returns and lower weight to older ones, with weights declining exponentially. Instead of treating all observations equally (as [rolling window](/rolling-window-volatility-estimation/) estimation does), EWMA lets recent market stress immediately raise the estimate without waiting for historical calm to exit a window. The model is tuned by a single decay parameter, lambda, typically set between 0.94 and 0.99. It is widely used in risk systems, option pricing, and regulatory frameworks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">EWMA Volatility — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Exponential weighting lets recent data dominate without arbitrary window cutoffs.</div>

|   |   |
|---|---|
| **Update formula** | σ²_t = λ × σ²_{t-1} + (1−λ) × r²_{t-1} |
| **Decay parameter (lambda)** | 0.94–0.99; larger = more inertia, slower response |
| **Typical values** | Daily: λ=0.94; weekly: λ=0.97; monthly: λ=0.99 |
| **vs. [rolling window](/rolling-window-volatility-estimation/)** | Smoother transitions; no cliff when old data exits |
| **vs. simple history** | Responsive to regime change; ignores very old data |
| **Use** | [VaR](/value-at-risk/) models, option pricing, risk dashboards, Basel frameworks |

</aside>

## The Core Formula and Intuition

The EWMA recursion is elegantly simple:

σ²_t = λ × σ²_{t-1} + (1 − λ) × r²_{t-1}

On each day t, the variance estimate is a blend: a fraction λ of yesterday's variance estimate plus a fraction (1 − λ) of today's squared return. The squared return r²_{t-1} measures how volatile the market was on the prior day. If the prior day was calm, r² is small and pushes the estimate down. If it was turbulent, r² is large and pushes the estimate up.

The decay parameter λ determines how much history is baked into the estimate. If λ = 0.99, yesterday's estimate gets 99% weight, and today's squared return gets only 1%. The estimate changes slowly, suitable for stable periods. If λ = 0.94, yesterday's estimate gets 94% weight, and today's shock gets 6%—the estimate reacts faster to new information.

The recursion can be expanded to show the effective history. Rearranging reveals that today's variance estimate is a weighted sum of all past squared returns, with weights declining exponentially:

σ²_t = (1 − λ) × [r²_{t-1} + λ × r²_{t-2} + λ² × r²_{t-3} + …]

The weight on return t−1 is (1 − λ); on return t−2, it is (1 − λ) × λ; on return t−3, it is (1 − λ) × λ². Each older return receives a smaller weight, decaying by a factor of λ.

## Choosing Lambda

The decay parameter λ must be calibrated, but no universal "correct" answer exists. The choice depends on the asset, market regime, and decision horizon.

**Daily equity indices** typically use λ = 0.94. A shock on day 1 receives 6% weight; by day 10, that shock's weight has fallen to 0.6%. By day 20, it is negligible. This means the model responds to a week or two of market stress but gradually forgets shocks older than a month. The [Federal Reserve](/federal-reserve/) and banks often use 0.94 for daily [value-at-risk](/value-at-risk/) calculations.

**Weekly or longer horizons** employ higher λ, such as 0.97 or 0.99, to slow the decay and give more weight to the longer-term regime. A hedge fund using weekly returns might set λ = 0.97, so a shock remains influential for months.

**Empirical calibration** compares past EWMA estimates to realized volatility over a test period, choosing λ to minimize prediction error. If you have two years of daily data, you might compute EWMA variance estimates for the first year at various lambda values, then measure which lambda predicted realized volatility best in the second year. This approach is labor-intensive but yields an optimal λ for the specific asset and market regime.

**Regime-dependent tuning** is common in practice. Use λ = 0.94 in normal times, but during crises, switch to λ = 0.92 or lower to make the model more responsive. This is a manual override, requiring judgment about when a true regime shift has begun.

## Advantages Over Historical Volatility

Simple [historical volatility](/historical-volatility/)—the standard deviation of the last n days—treats all days equally. A 60-day rolling window assigns the same weight to day 1 and day 60. EWMA avoids this cliff.

When a volatile day exits a rolling window, rolling volatility can drop sharply even if markets remain stressed. EWMA decays gradually, so the shock's influence fades smoothly rather than vanishing abruptly. This continuity is preferable for dynamic risk management, where sudden jumps in risk estimates can trigger unwarranted trading or hedging.

EWMA also responds faster to regime change. During a market spike, the rolling window takes days to fully incorporate elevated volatility (if the spike is on day 61, the rolling 60-day window ignores it until older data exits). EWMA responds immediately on day 1 of the spike, because the squared return on day 1 enters the formula at (1 − λ) weight directly.

## Comparison to Rolling Windows

A [rolling window](/rolling-window-volatility-estimation/) volatility using a 60-day window implicitly weights the last 60 days equally and drops older data entirely. EWMA weights data exponentially with no hard cutoff. In calm conditions, both methods produce similar results. During stress, they diverge.

Consider a market with sustained elevated volatility for 20 days. A rolling 60-day window will gradually incorporate these days as older calm days exit, causing volatility to rise smoothly. EWMA will spike upward immediately on day 1 of stress because each new large squared return receives direct weight. As days 2–20 of stress arrive, EWMA remains elevated. Once stress ends on day 21, rolling volatility remains high for the next 40 days (until stressed returns exit the window), while EWMA begins to decay immediately.

This means EWMA leads in detection (faster to rise) but rolls back more quickly once stress passes. The choice depends on whether you prioritize early warning (EWMA) or confirmation (rolling window).

## Variance vs. Volatility

Note that the EWMA recursion above updates the *variance* σ², not the volatility σ. Volatility is the square root of variance:

σ_t = √(σ²_t)

Some systems update variance directly, others update volatility and square it for variance. The two approaches are equivalent if done consistently. Most academic and regulatory frameworks update variance for computational ease, then report volatility as its square root.

## Limitations and Practical Considerations

EWMA assumes returns are i.i.d. (independent and identically distributed), an assumption that breaks during regime change. If volatility suddenly jumps (e.g., after a central bank shock), EWMA will eventually catch up, but the transition may lag slightly behind the true regime shift. Models like GARCH attempt to capture time-varying volatility more explicitly.

EWMA also ignores **autocorrelation**. If returns cluster (positive autocorrelation) or mean-revert (negative autocorrelation), a simple variance estimate cannot capture the full picture of risk.

Another limitation is **mean reversion**. If an EWMA-based [VaR](/value-at-risk/) estimate spikes but volatility subsequently falls sharply, the model can underestimate how quickly risk declines. This is less of a problem than lagging upside, but it matters for stop-loss triggers and [risk limits](/risk-horizon-holding-period-var/).

## Use in Regulatory Frameworks

The Basel Committee recommends EWMA-based variance estimates for internal [value-at-risk](/value-at-risk/) models, with λ = 0.94 for daily data. This standardization ensures banks calculate risk consistently and comparably. [Regulators](/office-of-the-comptroller-of-the-currency/) then scale one-day VaR to ten-day VaR using the [square root of time rule](/annualizing-volatility-square-root-of-time/), and EWMA variance provides the input to that scaling.

The JP Morgan RiskMetrics system, published in the 1990s, popularized EWMA as the standard for risk measurement and made 0.94 the de facto default for daily volatility. Despite the subsequent development of more sophisticated models, EWMA remains the primary benchmark in most institutional risk systems.

## When to Use EWMA

Use EWMA when you need responsive volatility estimates that react smoothly to regime change without artificial cliffs. It is ideal for [option pricing](/option-premium/), dynamic [hedging](/derivatives-hedging/), and intraday risk monitoring. For strategic [asset allocation](/asset-allocation/) or long-horizon decisions, simpler measures like annual or quarterly [rolling window](/rolling-window-volatility-estimation/) estimates often suffice. Combine EWMA with [stress testing](/stress-testing/) and [scenario analysis](/stress-testing/) to capture tail behavior that no single volatility model can convey.

## See also

<div class="wiki-seealso">

### Closely related

- [Rolling window volatility estimation](/rolling-window-volatility-estimation/) — Equally-weighted alternative to EWMA
- [Annualizing volatility using square root of time](/annualizing-volatility-square-root-of-time/) — Scaling variance across horizons
- [Risk horizon and holding period in VaR](/risk-horizon-holding-period-var/) — Regulatory scaling of risk estimates
- [Value at risk](/value-at-risk/) — Risk metric using volatility estimates
- [Volatility smile](/volatility-smile/) — How implied volatility varies; EWMA is one calibration approach
- [Historical volatility](/historical-volatility/) — Backward-looking volatility from realized returns

### Wider context

- [Market risk](/market-risk/) — Portfolio losses from adverse price movement
- [Stress testing](/stress-testing/) — Forward-looking tail risk assessment
- [Asset allocation](/asset-allocation/) — Portfolio construction using volatility and correlation
- [Derivatives hedging](/derivatives-hedging/) — Using volatility estimates to manage exposure
- [Sharpe ratio](/sharpe-ratio/) — Risk-adjusted performance metric

</div>

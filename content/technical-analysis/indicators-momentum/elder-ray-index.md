---
title: "Elder Ray Index"
description: "A momentum indicator that separates buyer power from seller power relative to an exponential moving average, revealing force imbalances."
keywords:
  - elder ray index
  - bull power bear power
  - momentum indicator
  - technical analysis
  - force asymmetry
image: /svg/technical-analysis.svg
---

*The **Elder Ray Index**, created by Alexander Elder, splits market force into two explicit components: Bull Power and Bear Power. Bull Power measures how far the high extends above an exponential moving average; Bear Power measures how far the low drops below it. Rather than blending these opposing forces into a single oscillator, Elder Ray keeps them separate, allowing traders to see exactly which participants—buyers or sellers—are in control.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Elder Ray Index — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Two-component momentum: buyer force and seller force rendered visible.</div>

|   |   |
|---|---|
| **What it is** | Bull Power = High − 13-EMA; Bear Power = Low − 13-EMA |
| **Also called** | Elder-Ray oscillator; Force index variant |
| **Standard period** | 13-period exponential moving average |
| **Range** | No fixed bounds; oscillates around zero |
| **Bull signal** | Rising Bull Power; Bear Power weak or negative |
| **Bear signal** | Rising Bear Power magnitude (increasingly negative); Bull Power weak or zero |
| **Primary use** | Identifying trend reversals; divergence analysis |

</aside>

## The two-component model: clarity through separation

Rather than averaging or offsetting buyer and seller momentum, Elder Ray makes both visible at once. The **Bull Power** line is calculated as the period's high minus the 13-period EMA. A Bull Power reading of +1.5 means buyers pushed the price 1.5 units above the moving average trend. A reading of +0.1 means they barely budged the market above the MA.

The **Bear Power** line is the period's low minus the 13-period EMA. Here, context inverts: a Bear Power reading of −2.0 means sellers drove price 2.0 units below the moving average—significant downside force. A reading of −0.3 means sellers were weak.

This separation illuminates force imbalance. In a healthy uptrend, Bull Power is rising and positive while Bear Power hovers near zero or slightly negative. In a reversal, Bull Power begins to falter (smaller highs relative to the EMA) while Bear Power strengthens in magnitude (larger negative moves). A trader watching both lines simultaneously captures the story ordinary momentum oscillators smooth over.

## The 13-period exponential moving average as anchor

Elder Ray anchors both components to a 13-period EMA. This choice is pragmatic: 13 bars is short enough to reflect recent trend yet stable enough to avoid whipsaw. The EMA acts as a dynamic fulcrum—a moving baseline that adjusts to current price momentum. When price is rallying strongly, the EMA itself rises; Bull Power then measures excess above that rising baseline, not an arbitrary fixed point.

The EMA's exponential weighting gives recent bars more influence, making it responsive without being jittery. Traders who prefer faster reaction use shorter periods (10-EMA); those seeking stability prefer longer ones (20-EMA). The adjustment is straightforward and does not change the logic.

## Reading convergence and divergence

The most actionable Elder Ray signal is **divergence**. Suppose a stock makes a new 52-week high. In a genuine bull move, Bull Power should also reach new heights (relative to the EMA). If instead Bull Power fails to exceed its prior peak while price does, buyers are losing force—a classic bearish divergence warning.

The inverse applies to Bear Power. If a stock plunges to a new low and Bear Power simultaneously reaches a new extreme (most negative), sellers maintain intensity. But if the low is new while Bear Power is weaker (less negative) than before, selling pressure is exhausted despite lower price—a bullish warning that bears have shot their ammunition.

**Convergence**—when both Bull Power and Bear Power are rising together—is less common and typically marks early-stage reversals. A market where both buyer and seller force is increasing is transitional; one side will eventually dominate.

## Trend confirmation and exhaustion

In established uptrends, Bull Power should remain positive and increasing on each rally attempt. When Bull Power begins to shrink or turns negative on a higher price close, the trend is weakening. This is not a reversal signal yet, but a deterioration flag—useful for tightening stops or reducing position size.

Similarly, in downtrends, Bear Power should remain negative and intensifying on each new low. When Bear Power weakens (becomes less negative) even as price makes lower lows, the downtrend is losing momentum. Traders using [coppock-curve](/coppock-curve/) or longer-term indicators to identify major reversals often watch Elder Ray for intra-trend confirmation.

## Comparison with single-line oscillators

The RSI and [stochastic-rsi](/stochastic-rsi/) blend overbought pressure and oversold pressure into a single value. Elder Ray refuses to blend; it insists you look at both. This is pedagogically cleaner but requires more attention from the trader—you must mentally integrate two lines rather than reading one.

The [PPO](/ppo-percentage-price-oscillator/) normalizes momentum as a percentage for cross-asset comparison. Elder Ray is absolute and instrument-specific; a +2.0 Bull Power on a $10 stock is not directly comparable to +2.0 Bull Power on a $300 stock. For single-instrument trend analysis, this specificity is an advantage. For portfolio momentum scanning, it is a liability.

## Practical application in swing trading

Many swing traders use Elder Ray as a second opinion when [price-discovery](/price-discovery/) signals are ambiguous. If price has broken above resistance but Bull Power is declining, the breakout is suspect. Conversely, if price is still trading below resistance but Bull Power is visibly rising and Bear Power weakening, a breakout may be imminent.

The indicator shines in choppy markets where price oscillates around the EMA. Reading the two lines tells you whether chop is buyer-driven or seller-driven. A market oscillating upward (higher highs, higher lows) with Bull Power rising is a consolidating uptrend. A market with same-level highs but falling Bull Power is a weakening uptrend and a candidate for tactical shorts.

## See also

<div class="wiki-seealso">

### Closely related

- [Force Index](/force-index/) — Momentum weighted by volume; another component-based approach
- RSI (Relative Strength Index) — Combines overbought and oversold into single oscillator
- [Stochastic RSI](/stochastic-rsi/) — A faster momentum oscillator for extreme readings
- [PPO (Percentage Price Oscillator)](/ppo-percentage-price-oscillator/) — Momentum normalized for cross-asset comparison
- [Exponential Moving Average](/exponential-moving-average/) — The EMA anchor underlying Bull and Bear Power

### Wider context

- Technical analysis — Broader practice of chart-based trading
- Momentum — Conceptual foundation of all force-based oscillators
- Divergence (technical analysis) — The most reliable signal from Elder Ray
- Trend reversal — Market structure change that Elder Ray helps identify

</div>

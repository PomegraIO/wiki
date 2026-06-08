---
title: "Stochastic RSI"
description: "A momentum oscillator that applies stochastic smoothing to RSI values, creating faster overbought/oversold signals than the RSI alone."
keywords:
  - stochastic rsi
  - momentum oscillator
  - overbought oversold signals
  - technical analysis
  - rsi derivative
image: /svg/technical-analysis.svg
---

*The **Stochastic RSI** applies the stochastic oscillator formula to RSI values rather than price itself, producing a more reactive and bounded overbought/oversold measure. Where the RSI softens extremes through smoothing, the Stochastic RSI heightens sensitivity to momentum shifts within the RSI itself, making it particularly useful for traders seeking earlier entry and exit signals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stochastic RSI — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">RSI pushed through a stochastic lens to catch faster momentum turns.</div>

|   |   |
|---|---|
| **What it is** | Stochastic of RSI: (RSI − Lowest RSI) ÷ (Highest RSI − Lowest RSI) × 100 |
| **Also called** | Fast stochastic of momentum; Stoch-RSI |
| **Standard lookback** | 14 periods for both RSI and stochastic window |
| **Range** | 0 to 100 (bounded oscillator) |
| **Overbought threshold** | Typically 80 or higher |
| **Oversold threshold** | Typically 20 or lower |
| **Primary signal** | Extreme crossovers; divergence with price |

</aside>

## The formula: nested momentum smoothing

The Stochastic RSI performs two layers of transformation. First, it calculates a standard 14-period RSI, which itself incorporates smoothing via its internal gain and loss averaging. Then it applies the stochastic formula to those RSI values:

Find the highest RSI value over the last 14 periods and the lowest RSI value over the same window. Subtract the lowest from the current RSI, divide by the range (highest minus lowest), and multiply by 100. The result: a reading between 0 and 100 that reflects where today's RSI sits within its recent range.

Many platforms also offer a **Stoch-RSI K line** (the main stochastic output) and **D line** (a 3-period moving average of K), mirroring the dual-line convention of standard stochastic oscillators.

## Why apply stochastic to RSI?

The RSI itself is already smoothed—its internal calculation averages gains and losses over multiple bars. For traders seeking earlier signals, this smoothing can feel sluggish. The Stochastic RSI adds reactivity by asking: "Where within its recent range is the RSI right now?" A Stochastic RSI of 95 means the RSI is near the top of its recent band, suggesting momentum is extreme relative to the past two weeks. A reading of 5 means RSI is near its low—potential oversold extreme.

This dual-layer approach achieves what single-layer oscillators cannot: simultaneously stable overbought/oversold zones (the 0-100 bounds) and higher sensitivity to momentum exhaustion within those zones.

## Reading overbought and oversold

Traders conventionally interpret Stochastic RSI above 80 as overbought and below 20 as oversold. However, these thresholds are flexible—some strategies use 70 and 30, others 90 and 10, depending on market volatility and timeframe.

Overbought does not mean "sell immediately." In a strong uptrend, the Stochastic RSI can remain above 80 for extended periods. The signal strengthens when overbought readings *diverge* from price—for example, the index makes fresh highs while Stochastic RSI fails to reach 80, suggesting momentum is weakening despite higher prices. This divergence often precedes pullback or consolidation.

Oversold readings work similarly in the downside. A Stochastic RSI below 20 paired with lower price lows but no new Stochastic RSI lows is a classic bearish exhaustion signal and can trigger bounce-trading strategies.

## K and D line crossovers

The K line (raw Stochastic RSI) and D line (smoothed K) create secondary signals through their interaction. When K crosses above the D line, momentum is accelerating upward; when K crosses below D, it is accelerating downward. These crossovers often trigger scalpers and swing traders, especially near extreme zones (above 80 or below 20).

The challenge: K/D crossovers generate noise in choppy markets. A crossover may precede a two-bar move rather than a sustained trend. Pairing K/D signals with [price-discovery](/price-discovery/) confirmation—a break of a recent swing high or low—filters false signals.

## Constraints and interpretation

The Stochastic RSI is not boundless like the [PPO](/ppo-percentage-price-oscillator/) or MACD. Its 0-100 range creates a structural constraint: readings below 0 or above 100 cannot occur. This constraint is a feature when used correctly, but it also means the indicator can plateau at extremes during very strong moves, reducing its ability to show further momentum divergence.

The indicator is most reliable on intermediate timeframes (daily, 4-hour) where a 14-period window captures meaningful highs and lows. On 1-minute charts, the lookback is too short and noise dominates. On weekly charts, it can be too slow.

Another limitation: the Stochastic RSI is derived from the RSI, which is itself derived from price. This dual derivation means the indicator lags price by definition. It is better suited to confirming trend changes than predicting them.

## Comparison with other momentum measures

Versus the raw RSI, the Stochastic RSI is faster but noisier. The RSI remains in overbought (above 70) longer during trends; the Stochastic RSI whipsaws in and out more frequently.

Versus the [Coppock Curve](/coppock-curve/), which is designed for long-term reversals, the Stochastic RSI is a short to intermediate-term tactical tool. The Coppock is a buy-once signal; Stochastic RSI generates frequent crossovers suited to active trading.

Versus the [PPO](/ppo-percentage-price-oscillator/), which normalizes momentum for cross-asset comparison, the Stochastic RSI is instrument-specific but more sensitive to overbought/oversold extremes.

## See also

<div class="wiki-seealso">

### Closely related

- RSI (Relative Strength Index) — The momentum foundation upon which Stochastic RSI is built
- [Stochastic Oscillator](/stochastic-oscillator/) — The stochastic formula applied directly to price
- [PPO (Percentage Price Oscillator)](/ppo-percentage-price-oscillator/) — Another momentum indicator normalized for cross-instrument comparison
- MACD — Absolute-value momentum oscillator used alongside Stochastic RSI
- [Elder Ray Index](/elder-ray-index/) — Separates buyer and seller power using a different approach

### Wider context

- Momentum — The conceptual foundation of all oscillators
- Overbought and oversold — The interpretation framework for bounded oscillators
- Technical analysis — Broader discipline of chart-based trading
- Divergence (technical analysis) — One of the most reliable signals from Stochastic RSI

</div>

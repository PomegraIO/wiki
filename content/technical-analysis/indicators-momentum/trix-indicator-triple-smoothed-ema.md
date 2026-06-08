---
title: "TRIX Indicator: Triple-Smoothed EMA Momentum"
description: "TRIX indicator uses triple exponential smoothing to filter noise and reveal momentum trends with fewer false crossovers than standard oscillators."
keywords:
  - trix indicator triple smoothed ema
  - trix momentum indicator
  - triple exponential smoothing
  - price momentum oscillators
  - technical analysis indicators
image: "/svg/technical-analysis.svg"
---

*The **TRIX indicator** applies three layers of exponential smoothing to price data, creating a momentum line that cuts through market noise and reduces the whipsaw from faster oscillators. By measuring the percentage change in a triple-smoothed moving average, TRIX isolates genuine trend shifts and is favored by swing traders who want fewer false signals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TRIX — Key Facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A momentum tool that smooths away noise through three passes of exponential averaging.</div>

|   |   |
|---|---|
| **Full name** | Triple Exponential Moving Average (TRIX) |
| **Type** | Momentum oscillator |
| **Primary use** | Identify trend direction and crossover signals |
| **Default period** | 15-day or longer |
| **Signal line** | 9-period EMA of TRIX value |
| **Strength** | Fewer false crossovers than single-smoothed averages |
| **Weakness** | Lagging; slower to react to fresh reversal |

</aside>

## What TRIX Does

TRIX calculates momentum by applying three successive exponential moving averages to closing prices, then measuring the percentage change between the current and prior smoothed value. The formula works in stages: first EMA smooths price, the second EMA smooths that result, and the third EMA smooths the second. The final step computes the rate of change (ROC) of this triple-smoothed line.

The three-pass smoothing removes the jittery noise that plagues single-pass momentum indicators, leaving behind genuine trend momentum. A TRIX reading above zero signals upward momentum; below zero signals downward momentum. The steeper the angle of the TRIX line, the stronger the momentum shift.

## How the Triple Smoothing Filters Noise

Exponential smoothing weights recent prices more heavily than older prices, but it still lags. Apply it once and you get a smoother line; apply it twice and the lag increases but noise drops further. The third pass is the key insight: it attenuates the whipsaw oscillations that plague oscillators like the raw Rate of Change or even a simple [momentum indicator](/momentum-indicator-for-swing-trading/), making TRIX suitable for identifying genuine breakouts without flinching at every minor wiggle.

Consider a price that spikes up 2% on a single bar, then reverses. A fast oscillator flags that as momentum change. A single-smoothed EMA still reacts. TRIX, being triple-smoothed, barely registers the blip. This is why swing traders often prefer TRIX when they want to ride multi-day trends without being shaken out by intra-day volatility.

The trade-off is lag. TRIX turns later than raw price action, so catching the very start of a move is harder. The benefit—avoiding false whipsaws and catching only the meaty part of a trend—often outweighs that cost for position traders working on daily or weekly charts.

## Signal-Line Crossovers

TRIX's primary trade signal is a crossover between the TRIX line itself and a 9-period EMA of TRIX, called the signal line. A bullish signal occurs when TRIX crosses above its signal line; a bearish signal when it crosses below. Because both lines are already heavily smoothed, these crossovers carry more conviction than crossovers in faster oscillators.

A bullish TRIX crossover often appears several bars into a recovery or uptrend, confirming that momentum is accelerating. Similarly, a bearish crossover signals that upward momentum is fading and reversals may follow. These crossovers work best on daily or weekly timeframes, where noise is proportionally smaller and trend windows are longer.

Traders often combine TRIX crossovers with other context: if TRIX crosses above its signal line while the price is above a key moving average, the signal is stronger. Conversely, a crossover near support or resistance that fails to hold is a warning sign that the signal was premature.

## When to Adjust the Period

The standard TRIX period is 15 days, which suits daily charts and swing trades of 5–15 bars. Shorter timeframes (hourly or 4-hour charts) benefit from shorter periods—9 or 12 days—because the faster the timeframe, the less relative noise three passes of smoothing can absorb before lag becomes problematic.

Longer-term traders (position traders, weekly charts) may increase the period to 21 or 30 days. A longer period means even less noise and even more lag, so TRIX becomes a confirmation tool rather than an entry signal. Higher periods also mean that trends must be sustained longer before TRIX catches them, reducing false signals further but requiring patience.

The signal-line EMA is almost always 9 periods, but some traders extend it to 12 or 15 if they want fewer crossovers overall. Testing on your specific market and timeframe matters: a parameter that works perfectly on daily euro futures may misbehave on intraday equities.

## Comparing TRIX to [MACD](/how-to-read-macd-crossover/)

Both TRIX and [MACD](/how-to-read-macd-crossover/) measure momentum through multiple moving averages and use signal-line crossovers as buy/sell cues. The key difference: MACD uses two exponential moving averages (a 12-period and 26-period) and plots their difference, while TRIX uses three exponential smoothing passes on price itself, then the rate of change.

TRIX is smoother and lags further, so it triggers fewer false crossovers but enters trends later. MACD is snappier and will catch earlier movement, but at the cost of occasional whipsaws. In choppy, range-bound markets, TRIX's extra smoothing is an advantage. In trending, low-noise environments, MACD's faster response can extract more profit.

Some traders use both: MACD for entry confirmation (once MACD points upward, the trend is confirmed) and TRIX for exit timing (waiting for TRIX to roll over signals that momentum is truly spent, not just pausing).

## Common Misreadings and Pitfalls

One frequent error is treating every TRIX crossover as a trade signal, regardless of market regime. A crossover in a narrow range is far less reliable than the same crossover during a breakout. Always check whether price is above resistance or below support; context matters more than the indicator alone.

Another mistake is chasing TRIX signals that arrive far into a move. Because TRIX lags, it often signals momentum well after price has already run 5–10%. Traders who jump in on those late signals are often caught when the move exhausts. Use TRIX as a trend-confirmation tool, not as a leading indicator.

Some traders fail to adjust the period for the timeframe. Running a 15-period TRIX on a 15-minute chart produces so much lag that the signal arrives after the move is over. Shorter timeframes need shorter periods; longer timeframes can tolerate longer periods.

## See also

<div class="wiki-seealso">

### Closely related

- [How to Read a MACD Crossover](/how-to-read-macd-crossover/) — Signal-line crossovers and trend context interpretation
- [Detrended Price Oscillator vs MACD](/detrended-price-oscillator-vs-macd/) — Comparing trend-following vs. detrended oscillators
- [Momentum Indicators for Swing Trading](/momentum-indicator-for-swing-trading/) — Which oscillators work best for multi-day trades
- [Moving Average](/moving-average/) — Foundation concepts behind exponential smoothing
- Technical Analysis — Overview of price and momentum tools

### Wider context

- [Volatility Smile](/volatility-smile/) — Understanding implied volatility surface
- [Algorithmic Trading](/algorithmic-trading/) — Systematic use of indicators in trading systems
- Risk Management — Position sizing and stop-loss rules alongside technical signals

</div>
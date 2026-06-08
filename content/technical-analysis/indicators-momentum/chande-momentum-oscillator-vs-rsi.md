---
title: "Chande Momentum Oscillator vs RSI: Key Differences"
description: "How CMO uses raw up/down price changes while RSI smooths them, creating different overbought/oversold signals on the same chart."
keywords:
  - chande momentum oscillator vs rsi
  - cmo vs rsi differences
  - rsi technical indicator
  - momentum oscillators
  - overbought oversold signals
  - technical analysis comparison
image: /svg/technical-analysis.svg
---

*The **Chande Momentum Oscillator** (CMO) and the **Relative Strength Index** (RSI) are both momentum indicators that measure overbought and oversold conditions, but CMO responds directly to raw price changes while RSI dampens them with an exponential moving average, causing the two to diverge significantly during trends and reversals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CMO vs RSI — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Two oscillators, one formula, two philosophies on smoothing.</div>

|   |   |
|---|---|
| **CMO basis** | Raw sum of up days minus sum of down days over N periods |
| **RSI basis** | Average gains divided by average losses, smoothed and normalized |
| **Scale** | CMO: –100 to +100; RSI: 0 to 100 |
| **Responsiveness** | CMO faster, noisier; RSI slower, more stable |
| **Overbought** | CMO >100 (impossible due to raw calculation); RSI >70 is standard |
| **Oversold** | CMO <–100 (impossible); RSI <30 is standard |
| **Signal lag** | RSI lags CMO by several bars in sharp reversals |

</aside>

## The Two Formulas: From Same Idea to Different Results

Both oscillators start with the same concept: measure the strength of upward price moves versus downward moves over a lookback period (typically 14 bars).

### The Chande Momentum Oscillator Formula

CMO is the simpler formula:

```
CMO = ((Sum of Up Days - Sum of Down Days) / (Sum of Up Days + Sum of Down Days)) × 100
```

Where:
- **Up Days**: Sum of all positive price closes minus the prior close.
- **Down Days**: Sum of the absolute value of all negative price closes minus the prior close.

The result ranges from –100 (all down days) to +100 (all up days).

### The RSI Formula

RSI is more elaborate:

```
RS = (Average Gain over N periods) / (Average Loss over N periods)
RSI = 100 - (100 / (1 + RS))
```

The key difference: RSI uses an **exponential moving average** of gains and losses, not a simple sum. This exponential smoothing means that each new bar's price change is weighted alongside a decaying memory of prior bars' changes. The default period is 14.

## Why the Formulas Matter: Smoothing and Lag

RSI's exponential smoothing makes it slower to respond than CMO. When a stock suddenly surges after a downtrend, CMO jumps instantly toward +100 because the recent up days dominate the raw sums. RSI rises more gradually because its exponential moving average still carries the weight of the prior down days for several bars.

This creates a lag—RSI "lags behind" in sharp reversals. Traders who rely on RSI crossing the 70 overbought level may be late to a reversal that CMO signals several bars earlier.

Conversely, RSI's lag can be an advantage during choppy, whipsaw markets: fewer false signals, less noise.

## Signal Divergences: When CMO and RSI Disagree

Consider a stock that gaps up hard on earnings:

- **Bar 1**: Price opens +5%, closes +4.5% above the prior close.
- **CMO** sees an enormous up move (+4.5); with a 14-bar lookback, the sum of up moves shoots higher and CMO jumps to 80–90+ on a single bar.
- **RSI** rises, but more modestly, to perhaps 65–75. The exponential average is still tempered by the prior 13 bars of history.

Later in a sustained downtrend:

- Over 10 bars, the price falls steadily –0.5% per bar (total –5%).
- **RSI** may still read 50–60 because the exponential moving average has "memory" of the prior rally.
- **CMO** drops sharply toward –80 or lower because recent down days dominate the raw sum.

These divergences are not errors. They reflect fundamentally different assumptions about how much weight to give recent price action versus recent history.

## Overbought and Oversold Thresholds

Traders use these thresholds:

**RSI**
- **Overbought**: RSI > 70
- **Oversold**: RSI < 30
- These thresholds are nearly universal; RSI cannot exceed 100.

**CMO**
- **Overbought**: CMO > 50 (some use 80 or 90)
- **Oversold**: CMO < –50 (some use –80 or –90)
- CMO can theoretically exceed 70 or 80 without hitting the scale limit, so thresholds are trader-defined.

Because RSI's scale is fixed (0–100) and bounded by its exponential smoothing, the 70/30 thresholds are well-established and cross many charts. CMO, being more volatile, often requires trader-specific calibration.

## Which Indicator Leads in Reversals?

Empirically, CMO tends to lead RSI in spotting reversal extremes. When a stock bottoms after a sharp fall, CMO usually reaches its lowest point and begins climbing before RSI does. A trader using CMO alone might exit a short position one to three bars ahead of someone using RSI alone.

However, this earliness comes with a cost: more whipsaws and false reversals. RSI's lag is a feature, not a bug—it filters out some noise.

## Combining CMO and RSI for Confirmation

Many traders use both oscillators together:

- **Buy signal**: CMO crosses above –50 AND RSI crosses above 30. This filters out false CMO bounces.
- **Sell signal**: CMO crosses below +50 AND RSI crosses below 70. This confirms a reversal with two independent measures.

The combination leverages CMO's responsiveness and RSI's stability, reducing whipsaws.

## Practical Application Comparison

| Scenario | CMO Advantage | RSI Advantage |
|----------|---|---|
| **Fast reversals after gaps** | Signals earlier | Avoids false whips |
| **Choppy, ranging market** | Overshoots, noisy | Stable, cleaner signals |
| **Sustained trend** | Reaches extremes faster | Stays in overbought/sold longer |
| **Trend confirmation** | Quick but unreliable alone | Slow but reliable |

## Common Pitfalls

- **Over-reliance on one**: Using only CMO (or only RSI) in isolation often leads to early or late exits.
- **Threshold confusion**: Assuming CMO's 50 is equivalent to RSI's 70 (it is not; they are on different scales and have different statistical distributions).
- **Ignoring price**: No oscillator is a substitute for [support and resistance](/support-and-resistance/) or volume confirmation. A stock can be RSI > 70 and keep rising for weeks.
- **Period mismatch**: Changing the lookback period from 14 to 7 or 21 alters both oscillators but in different ways; test before trading.

## See also

<div class="wiki-seealso">

### Closely related

- RSI — the foundational momentum oscillator
- [Momentum investing](/momentum-investing/) — the broader strategy of riding trends
- Overbought and oversold — the signal interpretation both indicators provide
- [Support and resistance](/support-and-resistance/) — price levels that interact with momentum extremes
- Divergence — when oscillators diverge from price, signaling reversals
- [Moving average](/moving-average/) — the smoothing technique underlying RSI

### Wider context

- Technical analysis — the broader discipline using price and volume patterns
- [Market timing](/market-timing/) — using indicators to enter and exit trades
- Volume — the confirmation signal that complements oscillator extremes
- [Volatility smile](/volatility-smile/) — how volatility changes with price extremes
- [Trend-following](/trend-following/) — the strategy both indicators aim to time

</div>

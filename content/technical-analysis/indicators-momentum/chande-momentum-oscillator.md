---
title: "Chande Momentum Oscillator"
description: "An unbounded momentum indicator comparing net up-day versus down-day closes without smoothing."
keywords:
  - chande momentum oscillator
  - momentum indicator
  - tushar chande
  - unbounded oscillator
  - technical analysis
image: "/svg/technical-analysis.svg"
---

*The **Chande Momentum Oscillator** (CMO) is an unsmoothed momentum indicator that measures the difference between the sum of up-closes and the sum of down-closes over a given period, then normalizes the result to a bounded scale of –100 to +100. Developed by technician Tushar Chande in 1994, the CMO strips away exponential smoothing to show raw buying versus selling pressure without lag.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Chande Momentum Oscillator — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">A direct, unsmoothed tally of up-days versus down-days to capture momentum with no lag.</div>

|   |   |
|---|---|
| **What it is** | Unbounded momentum oscillator ranging –100 to +100 |
| **Creator** | Tushar Chande (1994) |
| **Formula** | (Sum of up-closes − Sum of down-closes) ÷ (Sum of all closes) × 100 |
| **Lookback period** | Typically 9 or 14 periods |
| **No smoothing** | Raw calculation; responds immediately |
| **Overbought/Oversold** | > +50 / < –50 (roughly) |
| **Best for** | Identifying extreme momentum shifts |
| **Strength** | Zero lag; responsive to turning points |
| **Limitation** | Whippy in choppy markets; needs filters |

</aside>

## Why unsmoothed momentum matters

Most momentum indicators apply exponential moving averages or other smoothing to dampen noise and create cleaner signals. The trade-off: smoothing introduces lag. By the time a smoothed oscillator confirms a reversal, price has already moved significantly. Chande's approach inverts this thinking: measure the raw daily net change directly, with no averaging whatsoever, and let traders see the truth instantaneously.

The CMO tallies every up-close day and every down-close day in the lookback period, then compares their sums. If buying dominates, the oscillator spikes positive; if selling dominates, it crashes negative. This directness—combined with a simple normalization formula—yields an indicator that *responds to momentum shifts on the exact bar they occur*, not two or three bars later.

## The formula: net buying versus net selling

The calculation is straightforward. Over a given number of periods (typically 9 or 14), sum all the closes that are higher than the previous close. Call this **U** (up-closes). Sum all the closes that are lower than the previous close. Call this **D** (down-closes). Then:

**CMO = (U − D) ÷ (U + D) × 100**

This ratio is normalized to a range of –100 to +100. A CMO of +70 means that up-closes outnumber down-closes by a 70:30 margin; a reading of –70 means the reverse. A reading near zero indicates balanced buying and selling—neither side winning.

Because no smoothing is applied, the CMO can swing wildly from one bar to the next if a strong reversal bar appears. This volatility is intentional; it captures moments when sentiment genuinely shifts. Traders who dislike lag embrace this rawness; those who prefer steady signals may find the CMO too twitchy.

## Reading extremes and reversals

The CMO enters overbought territory above +50 and oversold below –50, though these thresholds are softer than the 70/30 levels of bounded oscillators like RSI. Extreme readings (above +80 or below –80) are rare and often signal capitulation or euphoria—moments when the current trend has run too hard, too fast, and exhaustion may be near.

However, **extreme readings do not always mean reversal is imminent**. In a strong uptrend, the CMO can camp above +60 for weeks, climbing higher as the momentum accelerates. Relying purely on overbought/oversold crossovers leads to whipsaws. Instead, many traders watch for *divergences*—when price makes a new high but CMO fails to, or vice versa—as a sign that the current move is losing conviction.

## The unsmoothed edge and its costs

The CMO's lack of smoothing gives it an edge in detecting turning points the instant they happen. A sharp reversal bar will show up immediately as an oscillator spike in the opposite direction. Experienced scalpers and swing traders use this responsiveness to time exits tightly, exiting the moment momentum rolls over rather than waiting for a slower indicator to confirm.

The cost: noise. In choppy, range-bound markets where prices bounce around without a clear trend, the CMO whipsaws constantly, generating false reversal signals. A one-bar counter-trend spike can trigger a spike in the oscillator that resolves instantly. Traders often pair the CMO with a trend filter (a moving average or ADX) or only trade signals when volatility is elevated and directional conviction is clear.

## Adjusting the lookback period

The default 9-period CMO captures short-cycle momentum, making it sensitive to intraday and 1-hour-bar reversals. A 14-period setting smooths slightly and suits daily charts and 4-hour swings. Longer periods (20, 25) reduce false signals but sacrifice some responsiveness.

Backtesting different periods on your timeframe and asset class is crucial. A CMO tuned for equities index futures (where liquidity is high and trends are sustained) may whip around uselessly on a thinly traded individual stock or crypto pair with gap-prone opens.

## When CMO shines and when it stumbles

The CMO excels in the first 5–10 bars of a trend reversal, when momentum is genuinely flipping. If you scan a chart, the CMO will flash the turn before price has moved far. This makes it valuable for mean-reversion strategies that buy oversold and sell overbought within a tight, defined risk window.

The CMO stumbles in sustained, powerful trends. If an asset is rallying hard, the CMO will stay extremely positive for days, offering no exit signal until the trend is nearly exhausted. It also struggles with gaps: a gapped open in one direction can produce an extreme oscillator reading that overstates the true buying or selling pressure, creating false reversal trades.

## Combining with other momentum tools

Many professional traders use the CMO as a *confirmation* layer rather than a standalone system. A setup might be: price shows a chart pattern reversal (e.g., a double-top), *and* the CMO is printing overbought, *and* volume is declining. The layering of signals raises the probability of a successful trade.

Pairing the CMO with an exponential moving average (EMA) or ADX trend filter prevents you from fading strong trends. Trading CMO oversold signals only when the price is above a 50-period EMA, for instance, keeps you on the long side of the dominant trend while capturing short-term overshoots.

Some traders also combine the CMO with RSI or the Stochastic oscillator, since all three measure momentum differently. If all three agree, the signal is robust; if they diverge, it often means the move is weak and likely to fail.

## See also

<div class="wiki-seealso">

### Closely related

- RSI — smoothed momentum oscillator using up-closes and down-closes
- Stochastic oscillator — momentum based on price position within a range
- MACD — trend momentum using exponential moving average divergence
- Ultimate oscillator — multi-timeframe momentum combining three buying-pressure ratios
- Momentum — rate-of-change concept and unsmoothed velocity measures
- Overbought and oversold — extreme oscillator readings and reversal probability

### Wider context

- Technical analysis — price and volume pattern recognition
- Divergence — price-momentum divergence as a reversal signal
- Mean reversion — trading around overbought/oversold extremes
- Trend confirmation — using indicators to validate directional moves
- Volatility — price swings and market regime detection

</div>

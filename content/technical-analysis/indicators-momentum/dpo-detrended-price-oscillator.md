---
title: "Detrended Price Oscillator"
description: "An oscillator that strips the dominant trend from price to expose short-cycle overbought and oversold conditions."
keywords:
  - detrended price oscillator
  - dpo
  - trend removal
  - overbought oversold
  - technical analysis
  - oscillator
image: "/svg/technical-analysis.svg"
---

*The **Detrended Price Oscillator** (DPO) is a trend-removal tool that displaces a moving average backward to isolate the short-term price fluctuations hidden beneath a dominant uptrend or downtrend. Rather than measuring momentum directly, the DPO shows what price would be doing *if the trend were not there*, making overbought and oversold conditions visible within a larger directional move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Detrended Price Oscillator — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Strip away the trend line to see short-cycle tops and bottoms.</div>

|   |   |
|---|---|
| **What it is** | Price minus displaced moving average |
| **Formula** | Close − SMA shifted backward |
| **Displacement** | Half the moving average period + 1 |
| **Typical SMA length** | 20 or 50 periods |
| **No bounded scale** | Unbounded; varies by asset and timeframe |
| **Best for** | Identifying cycle tops/bottoms within trends |
| **Strength** | Isolates short-cycle reversals in sustained moves |
| **Limitation** | Lag and backward displacement; difficult to trade in real time |

</aside>

## Why stripping the trend reveals hidden cycles

In a powerful uptrend, price climbs steadily, taking out new highs every few bars. A traditional momentum oscillator reads overbought for weeks, useless as a reversal signal. Yet within that uptrend, price does cycle: it pulls back 5%, then rallies, then pulls back again. These short-term reversals offer tactical entries and exits, but they are invisible when trend dominates.

The DPO solves this by *removing the trend line itself*. It calculates a simple moving average, shifts it backward in time, then subtracts it from the current price. What remains is the oscillation around the trend—the up-and-down wiggles separated from the long-term slope. In a strong uptrend, the DPO will oscillate above and below zero, making it clear when price is overdone relative to its short cycle, even though the overall trend remains intact.

## How the displacement works

The DPO formula is simple: **DPO = Close − SMA(displaced backward)**. The displacement is typically **(half the SMA period) + 1**. For a 20-period moving average, you shift it back 11 bars. For a 50-period MA, you shift back 26 bars.

This backward shift is unconventional and purposeful. A standard moving average lags price by its own length. A 20-period SMA sits about 10 bars behind the current price. By shifting the SMA back further—to a point roughly at the midpoint of its calculation window—the DPO aligns the trend with historical price, letting you see *current* price relative to a trend that is already confirmed and finalized, not one that is still forming.

The result is an oscillator with a peculiar property: it looks backward rather than forward. You cannot trade the DPO in real time the way you would trade RSI or MACD, because you need historical data to displace the MA. Instead, you use the DPO as a *cycle identifier*—a way to spot recurring peaks and troughs so you can anticipate when the next reversal is likely.

## Reading peaks and troughs for cycle prediction

The DPO oscillates above and below a zero line. Peaks (highs in the DPO) correspond to moments when price is furthest *above* its trend. Troughs (lows in the DPO) correspond to moments when price is furthest *below* its trend. In a sustained uptrend, the DPO will reach repeated peaks spaced maybe 10–20 bars apart—and those peaks mark tactical sell zones.

For example, in a 50-period trend, the DPO might spike up every 12–15 bars. If you chart those peaks, you notice a rhythm. Once you spot the cycle, you can project forward: *if the next peak is due in 3 days, I will watch for a short-term pullback there*. This is how the DPO reveals hidden cycles that traditional oscillators miss.

## When to use DPO versus standard momentum indicators

The DPO is not a real-time trading tool. Because of its backward displacement, the current bar's DPO reading is less reliable than a bar from 10 bars ago. Traders who need instant, actionable signals—scalpers, for instance—cannot rely on it.

Instead, the DPO shines for:

- **Swing traders** analyzing daily or 4-hour charts to identify likely pullback zones within a trend
- **Trend traders** spotting when a pullback is exhausted and buying the bounce
- **Cycle analysts** detecting repeating patterns and projecting future turning points
- **Multi-timeframe traders** using the daily-chart DPO to identify zone support on an intraday chart

For these uses, the DPO's backward look is an asset. You are trying to understand the structure of a move you are already inside, not predict the future on the next tick.

## Adjusting the moving average length

The standard 20-period DPO suits intraday trading and swing strategies with 2–5 day holding periods. A 50-period DPO smooths deeper cycles and works better on daily or weekly charts. Longer MAs (100, 200) reveal very slow cycles useful for position traders holding weeks or months.

Shorter MAs (9, 14) expose faster wiggles, useful if you are trading 1-hour bars and looking for 30–60 minute reversals. The art is matching the DPO period to your holding period: use a DPO that shows cycles about 2–3 times longer than your typical trade duration.

Backtesting on your own data is essential. A DPO that shows clear, repeating cycles on an equity may produce noise on the same timeframe for a volatile crypto asset. The calculation is identical, but the underlying price behaviour and volatility regime differ, shifting what cycle length is "real" versus random noise.

## The lag problem and how traders work around it

The DPO's displacement creates an inherent lag. The most recent bar's reading is not yet meaningful; only bars from 10–20 bars ago give you clean signals. This means you are making trading decisions based on patterns that are already half-formed in real time.

To work around this, experienced traders use the DPO in tandem with a real-time oscillator like RSI or stochastic. The DPO identifies zones; the real-time oscillator confirms entry. For instance: the DPO shows a cycle peak 2 bars away (historical), and you expect a pullback in 2 days. When price reaches that zone, RSI spikes overbought. Now you short. This layering lets you use the DPO's cycle insight without sacrificing entry precision.

## DPO for spotting cyclical trends

Beyond trade entries, the DPO reveals whether price is truly trending or just choppy. In a genuine trend, the DPO produces regular, repeating peaks and troughs. In a ranging market, peaks and troughs are erratic and scattered. Spotting this rhythm tells you whether to trade for reversal (in a range) or trend (in a cycle).

Some analysts use DPO peaks to divide a trend into legs. If each DPO peak corresponds to a pullback, then each pullback-to-peak rally is one "leg" of the trend. Counting legs tells you how mature a trend is and roughly how much room it has left before exhaustion.

## See also

<div class="wiki-seealso">

### Closely related

- Moving average — trend line that DPO displacements are based on
- RSI — real-time momentum oscillator; often paired with DPO for entry confirmation
- Stochastic oscillator — momentum gauge for overbought/oversold entries
- MACD — trend momentum using moving average convergence and divergence
- Momentum — rate of change; cycle-based vs. raw momentum
- Cycle analysis — identifying repeating price patterns and their period

### Wider context

- Technical analysis — price and volume pattern recognition
- Trend — sustained directional moves and their structure
- Pullback — temporary reversals within a larger trend
- Support and resistance — price zones where pullbacks often reverse
- Volatility — price swings and their predictability

</div>

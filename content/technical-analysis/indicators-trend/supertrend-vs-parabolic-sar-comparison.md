---
title: "Supertrend vs Parabolic SAR: Key Differences"
seo_title: "Supertrend vs Parabolic SAR: Which Trailing Stop to Use"
description: "Supertrend adapts stop distance to volatility via ATR; Parabolic SAR tightens on a fixed acceleration factor. Whipsaw rates, timeframes, and best uses."
keywords:
  - supertrend vs parabolic sar
  - supertrend trailing stop
  - parabolic sar indicator
  - volatility-adjusted stops
  - trend exit signals
  - atr-based stops
---

*The **Supertrend vs Parabolic SAR** comparison highlights two popular trailing-stop indicators with fundamentally different mechanisms. Supertrend adapts its stop distance to current [volatility](/volatility-smile/) via ATR, while Parabolic SAR uses a fixed acceleration rate that increases linearly. The choice depends on your market structure and whether you want volatility-responsive exits or mechanical consistency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Supertrend and Parabolic SAR — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Two trailing-stop systems with opposing approaches to stop adaptation.</div>

|   |   |
|---|---|
| **Stop mechanism** | Supertrend: ATR × multiplier; SAR: fixed acceleration factor |
| **Volatility response** | Supertrend adapts in real time; SAR climbs steadily |
| **Acceleration range** | Supertrend: 1.0–3.0 ATR typical; SAR: 0.02–0.20 (AF) |
| **Whipsaw rate** | Supertrend: lower (wider stops); SAR: higher (tighter stops) |
| **Trend confirmation** | Both can serve as directional filters |
| **Setup period** | Supertrend: 10 periods typical; SAR: continuous |
| **Best timeframe** | Supertrend: 4H, daily, weekly; SAR: 1H and above |

</aside>

## How Supertrend works

**Supertrend** is an ATR-based indicator that positions a dynamic stop above (in downtrends) or below (in uptrends) price. The formula is:

- **Uptrend stop** = HL/2 − (ATR × multiplier)  
- **Downtrend stop** = HL/2 + (ATR × multiplier)

where HL/2 is the high-low midpoint over the lookback period (typically 10 bars), and the multiplier (usually 3.0) scales the ATR output.

The result is a stop that widens automatically when volatility rises and tightens when volatility falls. In a calm uptrend, the stop sits close to price; in a choppy uptrend, it sits further away. This adaptation is Supertrend's defining feature.

When price closes on the opposite side of the Supertrend line, the trend flips. The indicator then switches to calculating the opposite-direction stop and waits for the price to close through it again.

## How Parabolic SAR works

**Parabolic SAR** (Stop and Reverse) uses a fixed **acceleration factor** (AF) that increases at discrete increments, not continuously. The SAR calculation is:

- SAR(t+1) = SAR(t) + AF × (Extreme Point − SAR(t))

The SAR moves closer to price each bar by a small fixed increment (the AF, starting at 0.02). When a new extreme high or low is made during the trend, the AF increments by another 0.02 (capped at 0.20). This creates a staircase effect: the SAR does not jump around, but climbs steadily toward price.

If price reverses and closes beyond the SAR, the stop flips to the opposite side. The AF resets to 0.02 and the process begins again in the new direction.

## Volatility responsiveness: the core difference

The fundamental **Supertrend vs Parabolic SAR** distinction is volatility adaptation. In a low-volatility uptrend:

- **Supertrend** tightens the stop close to price (lower ATR means a smaller multiplier offset).
- **Parabolic SAR** crawls toward price at the same fixed AF rate (0.02 per bar, +0.02 per extreme).

When volatility spikes (e.g., sudden news):

- **Supertrend** immediately widens the stop (higher ATR pulls the stop further away).
- **Parabolic SAR** continues its mechanical climb, unaware of the volatility surge.

This means **Supertrend gives traders more breathing room during volatile corrections**, reducing whipsaws. **Parabolic SAR can exit strong trends prematurely** if volatility jumps, because the SAR was calculated on the assumption of constant AF progression.

## Whipsaw frequency and false exits

In choppy, sideways markets, both indicators produce whipsaws. However:

- **Supertrend whipsaws** are typically fewer because the ATR is higher (reflecting chop), so the stop is wider. The indicator sits on the sidelines more often.
- **Parabolic SAR whipsaws** are more frequent because the AF keeps creeping upward regardless of market structure. A SAR in a consolidation can flip direction multiple times in a handful of bars.

On a 1-hour chart during a choppy Asian session, Supertrend might give 1–2 false signals. Parabolic SAR might give 5–6. This is why many traders reserve SAR for higher timeframes (daily and above) where trends are more durable.

## Trend confirmation and directional filtering

Both indicators double as **trend filters**:

- Price above Supertrend = uptrend (buy bias).
- Price below Supertrend = downtrend (sell bias).
- SAR below price = uptrend.
- SAR above price = downtrend.

Some traders use Supertrend as a [moving average](/moving-average/) replacement: only take longs when price is above the line, only shorts when below. Supertrend's wider spacing makes this a gentler filter than a 20 or 50-period EMA.

Parabolic SAR fills a similar role, but its tighter, more mechanical nature can produce false directional signals during consolidations. A SAR flip from below to above price (reversing the trend signal) during a range can be a trap.

## Practical trade setup: stop placement

**Supertrend approach:**
- Enter long when price closes above Supertrend (confirmed by some momentum check).
- Protective stop = Supertrend line (recalculated each bar).
- Exit if price closes below Supertrend.

**Parabolic SAR approach:**
- Enter long when SAR flips from above to below price.
- Protective stop = SAR line (moves up by AF each bar).
- Exit if price touches or closes below SAR.

In practice, **Supertrend stops are wider** (often 2–5% below entry), while **SAR stops are tighter** (often 1–3% below entry in low-volatility environments). This trade-off: tighter SAR stops mean faster exits and smaller losses, but also higher false-exit rate; wider Supertrend stops absorb volatility but cost more per stopped-out trade.

## Sensitivity and parameter tuning

**Supertrend** sensitivity is controlled by the **ATR period** and **multiplier**:
- Shorter ATR (7 bars) + lower multiplier (1.5) = tighter, more sensitive stops.
- Longer ATR (14 bars) + higher multiplier (3.0) = looser, less sensitive stops.

**Parabolic SAR** sensitivity is controlled by the **acceleration factor increments and maximum AF**:
- Lower starting AF (0.01) + lower max (0.10) = slower progression, looser stops.
- Higher starting AF (0.05) + higher max (0.30) = faster progression, tighter stops.

Default Supertrend settings (period 10, multiplier 3) suit daily and 4-hour charts. For 1-hour, many traders drop to period 7 or multiplier 2.0. Default SAR (AF start 0.02, max 0.20) suits daily and higher; for 1-hour, some traders raise max AF to 0.30 to accelerate exits.

## When to use Supertrend

- **Volatile markets** where you want stops to widen and contract with price movement.
- **Longer timeframes** (4H, daily, weekly) where the indicator's lag is acceptable.
- **Trend-following strategies** that prioritize staying in a trade over catching exact turns.
- **Risk management** where you want adaptive stops tied to realized volatility.

## When to use Parabolic SAR

- **Mechanical traders** who prefer deterministic, non-adaptive stops.
- **Mean-reversion strategies** where you want to exit countertrend moves quickly.
- **Short-term timeframes** (1H and above) if you tune AF to avoid excessive whipsaws.
- **Simple systems** where you want a single, familiar indicator without parameter complexity.

## Combining both for confirmation

Some traders plot both on the same chart as a **confirmation filter**. A signal is stronger if both Supertrend and SAR agree on direction. For example:

- Long bias if price > Supertrend AND SAR is below price.
- Exit if price closes below Supertrend OR closes below SAR (whichever is tighter).

This hybrid approach reduces false signals by requiring two independent mechanisms to align before trading. The trade-off is that you miss some early entries, but you also skip many whipsaws.

## See also

<div class="wiki-seealso">

### Closely related

- ATR indicator — Foundation for Supertrend calculation
- [Moving average](/moving-average/) — Alternative trend confirmation
- [Parabolic SAR](/parabolic-sar/) — Detailed mechanics of stop-and-reverse
- [DMI Plus and Minus](/dmi-plus-minus-directional-movement/) — Complementary directional signals

### Wider context

- [Trend-following](/trend-following/) — Strategy class both serve
- [Volatility smile](/volatility-smile/) — Market regime context
- [Support and resistance](/support-and-resistance/) — Price levels for stop placement
- [Position sizing](/position-sizing/) — Risk allocation with ATR-based stops

</div>

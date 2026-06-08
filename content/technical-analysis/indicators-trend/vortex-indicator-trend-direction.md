---
title: "Vortex Indicator for Trend Direction"
description: "Vortex indicator for trend direction: measures directional movement using high/low ranges to identify trends earlier and faster than traditional moving average crossovers."
keywords:
  - vortex indicator trend direction
  - VI+ VI- lines technical analysis
  - directional movement indicator
  - trend identification
image: /svg/technical-analysis.svg
---

*The **vortex indicator for trend direction** (VI+ and VI-) measures directional movement by comparing positive and negative high-low ranges over a lookback window, offering faster trend identification than moving averages alone. When VI+ is above VI- and climbing, uptrends are confirmed; when VI- leads, downtrends dominate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vortex Indicator — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two oscillating lines measuring directional strength over recent periods.</div>

|   |   |
|---|---|
| **VI+** | Positive directional movement; rising = uptrend strength |
| **VI-** | Negative directional movement; rising = downtrend strength |
| **Lookback period** | 14 days (default); 10 or 20 also common |
| **Range** | 0 to 2+; no fixed upper bound |
| **Crossover signal** | VI+ above VI- = bullish; VI- above VI+ = bearish |
| **Trend confirmation** | VI+ > 1.0 and climbing confirms uptrend conviction |
| **Speed vs MA** | Faster than golden cross; less lag on entries |

</aside>

## How the calculation works

The vortex indicator measures two directional components: upward movement and downward movement. On each bar, the indicator looks at the range from the high to the prior high (positive vortex movement) and from the low to the prior low (negative vortex movement). Over a rolling window—typically 14 days—it sums these movements and divides by the total true range (the widest range across the current high-low, prior close, or other reference points).

VI+ equals the sum of positive directional ranges divided by true range. VI- equals the sum of negative ranges divided by the same denominator. When upward movement dominates, VI+ climbs and VI- falls, creating visual separation on the chart. When downward movement dominates, the reverse occurs.

## Why this matters for trend identification

The vortex indicator responds to *sequence and direction*, not just magnitude. A stock can move down but do so in small, choppy increments (low directionality); another can move sideways in wide swings (directionality without trend). The vortex captures the *consistency* of directional movement, which is what separates a real trend from random noise.

This makes it faster than a [moving average](/moving-average/) crossover. A moving average is a lagging tool—it updates every bar and requires a full crossover period before declaring a trend. The vortex begins signaling directional strength within a few bars of a trend start because it only needs directional momentum to build, not a full 50- or 200-bar lookback.

## Reading VI+ and VI- crossovers

The most straightforward vortex signal is a crossover. When VI+ rises above VI-, it suggests upside momentum is emerging. Traders often wait for this crossover AND for VI+ to remain above VI- for a few subsequent bars to confirm the signal has staying power.

A VI- above VI+ signals downtrend dominance. If VI- is also above 1.0 and climbing, the downtrend is in full force. A crossover back below VI+ signals weakening downside pressure and a potential bottom.

The indicator also gives a *strength* signal independent of crossovers. If VI+ is at 1.5 and VI- is at 0.6, the uptrend is not just active but muscular—directional movement is strong and one-sided. An uptrend where VI+ climbs to 2.0+ on rising volume is far more reliable than one where VI+ stays below 0.9.

## Comparing to moving average strategies

A [golden cross](/golden-cross-vs-death-cross/) takes weeks or months to form because it requires two long moving averages to align. The vortex gives a signal within days of a trend start. In volatile markets, this speed advantage can capture 5–10% of a move that a golden cross would miss entirely.

However, the vortex is more sensitive to whipsaws in choppy, range-bound markets. A brief spike in directional movement can trigger a VI+ cross above VI- only for the trend to fail hours or days later. Golden crosses, by contrast, rarely trigger unless there is already significant momentum building.

Many traders use both: the vortex as an *early warning* that a trend may be starting, and [moving average](/moving-average/) confirmation as a *conviction check* that the move is real.

## Timeframe and lookback choices

The default 14-period lookback works well on daily charts for swing traders capturing moves of days to weeks. On weekly charts, a 14-week vortex captures longer-term institutional flows. On intraday charts, a 14-bar lookback (whether 5-minute or hourly bars) is also used but generates more false signals because intraday noise distorts directionality.

Some traders shorten to 10 or 8 periods for faster, more responsive signals in volatile markets. Others stretch to 20+ for smoother, fewer false-positive signals. The trade-off is always speed versus reliability.

## Volume context

Like any trend indicator, the vortex is strongest when paired with volume confirmation. A VI+ crossover above VI- on heavy volume—especially if volume exceeds the average—suggests real accumulation driving the move. The same crossover on declining volume is suspect and more likely to fail.

Traders often overlay volume bars beneath the vortex or watch for volume spikes coinciding with VI+ or VI- crossovers. This combination of directional movement and participation raises conviction significantly.

## Practical applications

Swing traders use the vortex to identify the *start* of a new trend, then enter on a pullback once VI+ is established above VI-. This approach captures more of a trend than waiting for a moving average crossover.

Trend-following systems often set alerts when VI+ is above VI- and above a threshold (like 1.0 or 1.2), treating sustained high readings as permission to increase position size. Conversely, a drop in VI+ below 0.8 while still above VI- may signal weakening trend strength and a time to exit or reduce exposure.

Mean reversion traders flip the logic: when VI+ or VI- spike to extreme levels (above 1.8–2.0), they often fade the move, betting that directional extremes are unsustainable.

## Limitations

The vortex is not a trend predictor; it is a trend *detector*. It works well only after a trend has begun. In a market that is about to turn but hasn't yet, the vortex offers no edge and can give false crossovers.

It is also purely directional. It does not measure the *magnitude* of price change, only the consistency of movement. A stock can have high VI+ while moving sideways as long as the up-moves are consistent, leading traders to mistake directionality for strength.

Finally, the indicator is smooth and can lag slightly on very rapid reversals. A sharp reversal on heavy volume may catch the vortex off-guard, resulting in a delayed signal relative to the actual pivot.

## See also

<div class="wiki-seealso">

### Closely related

- [Moving Average](/moving-average/) — traditional trend baseline that vortex often confirms
- [Average Directional Index (ADX) Explained](/average-directional-index-adx-explained/) — another directional strength measure
- [Trend Following](/trend-following/) — the strategy that benefits most from vortex signals
- Volume — how to validate vortex signals
- [Aroon Indicator: How It Works](/aroon-indicator-how-it-works/) — alternative directional indicator using time since high/low

### Wider context

- [Bull Market](/bull-market/) — what sustained high VI+ signals
- [Bear Market](/bear-market/) — what sustained high VI- signals
- [Volatility Smile](/volatility-smile/) — how uncertainty affects directional clarity
- [Market Timing](/market-timing/) — risk of over-relying on any single signal

</div>

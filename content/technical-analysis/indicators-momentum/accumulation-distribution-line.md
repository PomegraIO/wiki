---
title: "Accumulation/Distribution Line"
description: "Volume-weighted price location indicator measuring whether volume is concentrated during up or down moves."
keywords:
  - accumulation distribution
  - volume indicator
  - money flow
  - technical analysis
  - price action
---

*The **Accumulation/Distribution Line** (A/D Line) is a technical indicator that combines [volume](/wiki/volume-rate-of-change/) and price to measure whether money is flowing *into* a security (accumulation) or *out of* it (distribution). A rising A/D line during price advances confirms buying strength; a rising A/D during price declines suggests hidden accumulation.*

<aside class="wiki-infobox">

| Metric | Interpretation |
|---|---|
| **Rising A/D + Rising Price** | Bullish (accumulation confirmed) |
| **Falling A/D + Rising Price** | Bearish divergence (distribution during rally) |
| **Rising A/D + Falling Price** | Bullish divergence (accumulation during decline) |
| **Falling A/D + Falling Price** | Bearish (distribution confirmed) |
| **Volume extremes** | Volume on up days vs. down days shows conviction |
| **Signal line** | Simple moving average of A/D for trend confirmation |
| **Momentum use** | Can diverge from price before reversals |

</aside>

## The formula

The A/D Line is calculated as:

```
Money Flow Multiplier = (Close − Low) − (High − Close) / (High − Low)
Money Flow Volume = Money Flow Multiplier × Volume
A/D Line = Cumulative sum of Money Flow Volume
```

**Step-by-step:**

1. **Position in range** — where did the close sit within the day's high-low range?
   - Close = High: multiplier = 1 (entire day was accumulation)
   - Close = Low: multiplier = −1 (entire day was distribution)
   - Close = midpoint: multiplier = 0 (neutral)

2. **Scale by volume** — multiply the multiplier by the volume (high volume exaggerates the effect).

3. **Cumulative** — A/D Line is a running total; it only goes up, down, or flat (never resets daily).

## Intuition: volume-weighted price location

The A/D Line asks: **On days when price rose, how much volume was there? And on days when price fell, how much volume was there?**

**Bullish signal:**
- Price rallies on high volume (strong accumulation), or
- Price declines on low volume (weak distribution)
- A/D Line rises, confirming the move

**Bearish signal:**
- Price rallies on low volume (weak accumulation, possibly distribution in disguise), or
- Price falls on high volume (strong distribution)
- A/D Line falls or lags price, suggesting trouble ahead

## Example: accumulation-distribution divergence

A stock rises from $100 to $110 over a month:

**Scenario 1 (bullish):**
- Weeks 1–3: price up on high volume; A/D Line rises strongly
- Week 4: price stalls; A/D Line levels off
- **Interpretation**: Strong accumulation early; now exhausted. Likely consolidation, then higher

**Scenario 2 (bearish divergence):**
- Week 1: price up on low volume; A/D Line barely rises
- Week 2–3: price up on declining volume; A/D Line rises minimally
- Week 4: price up on tiny volume; A/D Line flat or declining
- **Interpretation**: Weak accumulation despite price rise. Distribution is happening; rally is vulnerable. Reversal likely.

In Scenario 2, the A/D Line "diverges" from price—price is up but A/D is flat/down. This is a classic warning sign.

## A/D vs. [on-balance volume](/wiki/obv-on-balance-volume/)

The A/D Line and [On-Balance Volume](/wiki/obv-on-balance-volume/) (OBV) are similar but distinct:

| Metric | A/D Line | OBV |
|---|---|---|
| **Calculation** | Position in range × volume | All up volume added; all down volume subtracted |
| **Edge case** | If close = midpoint, no net signal | Every bar is +vol (up) or −vol (down) |
| **Sensitivity** | Rewards closes at extremes of range | All-or-nothing: up or down |
| **Divergence** | Can flag distribution even in sideways markets | Cleaner for trend confirmation |

Both serve the same purpose: confirm whether volume is accumulating or distributing. A/D is more nuanced about *where* in the range the close is.

## Use in [trend](/wiki/trendline/) confirmation

A rising A/D Line during an uptrend confirms the trend is healthy. A declining A/D during an uptrend warns the trend may be weakening. Many technical traders use A/D as a secondary filter:

- **Entry** — buy a [breakout](/wiki/breakout-trading/) only if A/D Line is rising (not falling)
- **Exit** — if A/D turns down while price is still up, exit the position (take profit)
- **Fade a move** — if A/D is down while price is up, fade (bet on reversal)

## Divergence trading

The most powerful use of A/D is **divergence**:

**Bullish divergence:**
- Price makes a lower low, but A/D Line makes a higher low
- Interpretation: Despite weakness, accumulation is happening; bounce is likely
- Action: **Buy** (or cover short)

**Bearish divergence:**
- Price makes a higher high, but A/D Line makes a lower high
- Interpretation: Despite strength, distribution is happening; decline is likely
- Action: **Sell** (or take profits)

These divergences often precede significant reversals, giving traders a 3–7 day lead time on larger moves.

## Limitations and false signals

1. **Lagging indicator** — A/D is cumulative, so it is slower to reverse than price. A fast reversal may not show up immediately.

2. **Gap risk** — A/D doesn't account for [overnight gaps](/wiki/overnight-gap/) or gaps at market open. If a stock gaps up on low volume, A/D still shows accumulation (close near high), even though no intraday buying occurred.

3. **False divergences** — divergences can fail. A stock in a strong uptrend may have A/D divergences (distribution) but still rally for weeks. Divergences work best at **cycle extremes** (local tops/bottoms), not in the middle of trends.

4. **Sector and timeframe dependent** — some sectors or timeframes (e.g., [penny stocks](/wiki/penny-stocks-investor/)) see high false-positive divergences. A/D works better on liquid, established equities.

## Integration with other indicators

Most traders use A/D alongside:

- **[Price action](/wiki/price-discovery/)** — is the stock making higher highs and higher lows (uptrend)?
- **Moving averages** — is price above or below key MAs?
- **[Momentum indicators](/wiki/momentum-factor/)** ([RSI](/wiki/rsi-relative-strength/), [MACD](/wiki/macd-indicator/)) — is momentum diverging too?
- **[Volume profile](/wiki/volume-profile-support/)** — where is most volume historically?

A divergence on A/D that is *not* confirmed by other indicators is weaker.

## A/D Line and [market breadth](/wiki/market-breadth-advances-declines/)

For broader indices (S&P 500, Russell 2000), the A/D Line (summed across all stocks in the index) is a **breadth indicator**. A rising A/D breadth with a rising price index confirms the move. A falling A/D breadth with rising price signals ** breadth divergence**—not all stocks are participating, and the rally is fragile.

<div class="wiki-seealso">

### Closely related
- [Accumulation/distribution](/wiki/accumulation-distribution/) — the concept (brief entry)
- [On-balance volume (OBV)](/wiki/obv-on-balance-volume/) — similar volume indicator
- [Volume rate of change](/wiki/volume-rate-of-change/) — pure volume momentum
- [Chaikin oscillator](/wiki/chaikin-oscillator/) — derivative of A/D Line
- Technical analysis — broader framework

### Wider context
- [Momentum indicator](/wiki/momentum-factor/) — category of indicators
- [Price action](/wiki/price-discovery/) — qualitative complement to A/D
- [Divergence](/wiki/disposition-effect/) — concept in technical analysis
- [Market breadth](/wiki/market-breadth-advances-declines/) — A/D applied to indices
- [Volume profile support](/wiki/volume-profile-support/) — where volume clusters

</div>

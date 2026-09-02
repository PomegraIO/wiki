---
title: "Money Flow Index"
description: "A volume-weighted momentum indicator that measures the strength of buying and selling pressure, combining relative strength concepts with trading volume."
keywords:
  - momentum indicator
  - volume analysis
  - rsi variant
  - overbought oversold
  - technical analysis
  - market pressure
---

*The [Relative Strength Index](/wiki/rsi-relative-strength/) measures price momentum, while [volume](/wiki/volume-breadth-divergence/) tells you the conviction behind a move. The **Money Flow Index** (MFI) marries the two: it applies RSI logic to money (price times volume), not just price. A stock can rally on weak volume (unconvincing) or on strong volume (genuine). The MFI separates one from the other.*

<div class="wiki-hatnote">Also known as the volume-weighted RSI. It ranges from 0 to 100, just like the RSI, but incorporates transaction value instead of price alone.</div>

<aside class="wiki-infobox">

| Feature | Detail |
|---------|--------|
| **Formula base** | Typical price × volume = money flow |
| **Time period** | Usually 14 days (like RSI) |
| **Range** | 0–100 |
| **Overbought threshold** | Typically >80 |
| **Oversold threshold** | Typically <20 |
| **Signal type** | Momentum and divergence |
| **Volume dependency** | Essential; useless without volume data |

</aside>

## Construction: price and volume combined

The MFI starts by calculating "typical price" for each bar: (High + Low + Close) / 3. This is then multiplied by volume to get "money flow" for that period. A bar with high typical price and massive volume represents powerful buying (or selling).

The MFI then sums positive money flows (periods where typical price rises) over a lookback window (typically 14 days) and compares them to negative money flows (periods where typical price falls):

MFI = 100 − [100 / (1 + Money Flow Ratio)]

Where Money Flow Ratio = Positive Money Flow / Negative Money Flow.

A ratio of 2.0 (twice as much buying pressure as selling pressure) yields an MFI of 67. A ratio of 0.5 (half as much buying pressure as selling) yields an MFI of 33.

## Overbought and oversold signals

Like the [RSI](/wiki/rsi-relative-strength/), an MFI above 80 is considered overbought—too many buyers at once, likely to reverse. An MFI below 20 is oversold—too many sellers, likely to bounce. Many traders use these thresholds as entry signals: a stock that drops to MFI 15 is a buy candidate; one that surges to MFI 85 is a short candidate.

However, in strong trending markets, overbought/oversold signals are traps. A stock trending upward can stay above 80 for weeks, and shorting on that signal alone will lose money. Context matters.

## Divergences: momentum vs. price

The power of the MFI lies in divergences. If a stock makes a new high but the MFI fails to make a new high (lower high in MFI while price is higher), the rally is losing momentum—fewer dollars are flowing in. This divergence often precedes a pullback.

Conversely, if a stock makes a new low but the MFI bounces (higher low in MFI while price is lower), selling pressure is weakening—the market is exhausted. This bullish divergence often precedes a reversal.

These divergences are more reliable than the overbought/oversold levels alone because they reveal a mismatch between price action and buying/selling conviction.

## Volume profile and market regime

The MFI is most useful in liquid assets (stocks, large-cap ETFs, major indices) where volume is consistent and meaningful. In thinly traded securities, a single large order can spike volume artificially, creating a false MFI signal.

In crypto and small-cap stocks where volume can be manipulated or sporadic, the MFI is less reliable. Large market participants can paint the tape (trade with themselves to create volume illusions), distorting the MFI.

## Comparison to RSI and OBV

The [RSI](/wiki/rsi-relative-strength/) ignores volume entirely—a 1% price move on 1 million shares and 100 shares have the same impact. The [On Balance Volume](/wiki/obv-on-balance-volume/) (OBV) includes all volume but assigns it uniformly (up or down) without regard to magnitude of price move. The MFI splits the difference: it weights volume by the magnitude of the price move.

For mean-reversion traders (looking for extremes to reverse), the MFI's volume weighting is often better than RSI alone. For trend-followers, OBV or the MFI may outperform RSI.

## Practical trading rules

A typical MFI strategy might look like:
1. **Entry:** Wait for MFI >80 followed by a drop below 80 (sell signal releases). Short-term traders take short positions.
2. **Confirmation:** Check that volume on the reversal bar exceeds recent average. Weak volume weakens the signal.
3. **Exit:** Cover shorts if MFI drops to 30 or lower (capitulation) or if the stock closes above the signal bar's high.

Alternatively, for mean-reversion dip-buyers:
1. Wait for MFI to drop below 20 (exhaustion).
2. Buy on bounce above that level with volume confirmation.
3. Exit if MFI returns above 50 or on a reversal bar close.

## Divergence analysis: a deeper read

The most advanced MFI traders focus exclusively on divergences, ignoring the absolute level. They ask: "Is the MFI making higher highs as price makes higher highs?" If not, the uptrend is weakening. Momentum divergences precede price reversals by 5–20 bars—enough lead time to exit before the crash.

This is more robust than overbought/oversold levels because it captures the *direction of momentum change*, not just its extremeness.

## Limitations and cautions

The MFI is backward-looking. It tells you what has already happened (buying dominated for the past 14 days) but is mute on what happens next. In a market regime shift (a gap open on news), the MFI can be misleading.

Also, the MFI assumes that volume data is accurate. In stock markets, exchange-reported volume is reliable. In crypto markets, where many exchanges are unregulated and wash-trading is common, reported volume is often fiction.

The MFI is also sensitive to the lookback period. A 14-period MFI is standard, but a 7-period MFI will be choppier (more overbought/oversold touches), while a 21-period MFI is smoother but slower to turn.

<div class="wiki-seealso">

### Closely related
- [RSI / Relative Strength Index](/wiki/rsi-relative-strength/) — Price-only momentum, which MFI improves on
- [On-Balance Volume](/wiki/obv-on-balance-volume/) — Alternative volume indicator
- [Volume](/wiki/volume-breadth-divergence/) — The raw ingredient
- [Chaikin Oscillator](/wiki/chaikin-oscillator/) — Another volume-momentum hybrid

### Wider context
- Technical Analysis — Category of price/volume pattern analysis
- [Momentum Investing](/wiki/momentum-investing/) — Strategy that uses these signals
- [Mean Reversion](/wiki/mean-reversion-investing/) — Strategy MFI helps identify extremes for
- [Trading Signals](/wiki/breakout-trading/) — How indicators become actionable trades

</div>
---
title: "Chaikin Money Flow vs Money Flow Index: Which to Use"
description: "How CMF and MFI differ despite their names—construction, scale, and signals—and when to apply each volume-weighted indicator."
keywords:
  - chaikin money flow vs money flow index
  - chaikin money flow indicator
  - money flow index mfi
  - volume weighted sentiment indicators
image: "/svg/technical-analysis.svg"
---

*The **Chaikin Money Flow vs Money Flow Index** is a tale of similar-sounding names concealing different formulas. Both are volume-weighted sentiment indicators that combine price and volume to measure the strength of buying or selling pressure. But they diverge in construction, scale, and interpretation—and choosing the wrong one can lead to false signals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CMF and MFI — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Same idea, different math; CMF is unbounded, MFI oscillates 0–100.</div>

|   |   |
|---|---|
| **Chaikin Money Flow (CMF)** | Accumulation/Distribution line smoothed by volume; unbounded scale (can exceed ±1) |
| **Money Flow Index (MFI)** | RSI applied to money flow; oscillates 0–100, similar to RSI |
| **Construction** | CMF: price location × volume; MFI: positive/negative money flow ratio |
| **Signal** | CMF: positive/negative momentum and divergences; MFI: overbought (>80) / oversold (<20) |
| **Time period** | CMF: 20 or 21 days typical; MFI: 14 days typical (RSI-like) |
| **Use case** | CMF: trend confirmation, divergence trading; MFI: mean-reversion, extreme conditions |

</aside>

## The shared DNA: money flow and volume

Both the **Chaikin Money Flow** and **Money Flow Index** start from the same concept: volume-weighted price analysis. They ask, "Is buying pressure or selling pressure dominant today, and how strong is it?"

The key insight is that volume matters. A stock closing near its high on 10 million shares is more significant than a stock closing near its high on 100,000 shares. These indicators weight price strength by volume, creating a measure of "where the money is flowing."

From there, however, the two diverge sharply.

## Chaikin Money Flow: the accumulation distribution approach

**Chaikin Money Flow** (CMF) is the smoothed version of the Accumulation/Distribution (A/D) line. The A/D line calculates, for each bar:

Money Flow Multiplier = ((Close – Low) – (High – Close)) / (High – Low)

This number ranges from –1 (close at low) to +1 (close at high). The reasoning is intuitive: if a stock closes near the high, buyers are pushing the price up (multiplier near +1). If it closes near the low, sellers are winning (multiplier near –1).

Then multiply by volume: if close is near the high and volume is heavy, positive money flow accumulates. If close is near the low and volume is heavy, negative money flow (distribution) accumulates.

The A/D line cumulates these daily values into a running total. The CMF then smooths this cumulative line with a moving average (typically 20 or 21 days), creating a momentum indicator.

**CMF scale is unbounded.** It can exceed +1 or drop below –1, especially when volume is very heavy or very light. A CMF reading of +0.5 is moderately bullish; –0.5 is moderately bearish. Readings above +0.7 or below –0.7 are strong signals.

The interpretation is directional: positive CMF indicates accumulation (buyers in control); negative CMF indicates distribution (sellers in control). A crossover of CMF from negative to positive (or sustained positive CMF rising) suggests bullish momentum. Conversely, a divergence—price making a new high but CMF declining—signals weakening buying pressure and potential reversal.

## Money Flow Index: the RSI of volume

**Money Flow Index** (MFI) takes a different path. It borrows the RSI (Relative Strength Index) formula and applies it to money flow instead of price changes.

First, calculate "Typical Price" for each bar: (High + Low + Close) / 3.

Then calculate "Raw Money Flow" for each bar: Typical Price × Volume.

Now comes the RSI-like step: classify each day's raw money flow as positive (if the typical price rose from the previous day) or negative (if it fell). Sum the positive money flows over 14 days and the negative money flows separately.

Finally, apply the RSI formula:

MFI = 100 – (100 / (1 + (Positive Money Flow Sum / Negative Money Flow Sum)))

The result oscillates between 0 and 100, just like RSI. An MFI above 80 is overbought (strong buying exhaustion); below 20 is oversold (strong selling exhaustion).

**MFI scale is bounded 0–100**, making interpretation straightforward: high readings mean money is flooding in, low readings mean it is draining out.

## The practical differences: when to use each

Consider how these indicators behave in the same market move.

Suppose a stock rises from $100 to $110 over three weeks on moderate-to-heavy volume. During this time:

- **CMF** will be steadily positive (most bars close in the upper half of their range with volume increasing). CMF itself will be rising, moving from perhaps 0 to +0.4 or +0.5. The rising CMF confirms the uptrend.

- **MFI** will be rising toward the overbought zone (80+). As the stock approaches $110 and days pass where MFI stays above 80, the indicator is flagging that money flow (relative to recent history) is elevated.

A trader using CMF might stay long as long as CMF is positive and rising. But a trader using MFI at 85 might start trimming, expecting a pullback or consolidation.

**Use CMF for trend confirmation and divergence trading.** If a stock is making new highs but CMF is declining, that divergence suggests the uptrend is losing steam. CMF's unbounded nature means you are tracking the absolute strength of accumulation.

**Use MFI for mean-reversion and overbought/oversold signals.** When MFI spikes above 80 on breakout news, reversion traders bet on pullback. When MFI crashes below 20 on panic selling, contrarian traders spot opportunities.

## Comparing signals in a reversal scenario

Imagine a stock rallies hard for 10 days, closing near the high each day, then sells off sharply on a negative earnings miss.

On the reversal day:
- **CMF** flips negative immediately (the bar closes low; high volume on the down day tips the multiplier negative). CMF drops sharply. A trader watching CMF sees the accumulation reversed into distribution—a clear warning.

- **MFI** reaches 90 during the rally (overbought), then falls below 80 on the reversal day, but may not drop to oversold immediately (it is a 14-day oscillator, not a single-bar reading). MFI is slower to reverse and takes longer to signal "oversold."

This difference matters. CMF gives you fresh momentum every bar; MFI smooths and compares to a 14-day window. CMF is more reactive; MFI is more of a medium-term oscillator.

## Common pitfalls and divergence trading

Both indicators are prone to false signals in choppy, range-bound markets. High volume on a small price move can spike MFI or CMF without any meaningful momentum. Gaps and limit-move days can distort both.

A real edge comes from **divergences**: when price makes a new high (or low) but the indicator makes a lower high (or higher low). This suggests momentum is fading.

- **CMF divergence**: Stock rallies to a new 52-week high, but CMF is lower than it was at the prior high. Sellers are resisting; accumulation is weaker. This is a caution flag.

- **MFI divergence**: Stock rallies to new high, but MFI is in the 60s (not above 80 as before). Money flow is not as intense. Again, a warning that the move is losing conviction.

Both indicators excel at spotting these divergences, but they use different scales. Learning to read both prevents over-reliance on a single signal.

## Which to use: a framework

- **For trend traders**: Use CMF. Its directional nature and ability to measure absolute accumulation fit a trend-following approach. Pair it with moving averages or trend lines.

- **For swing traders and mean-reversion players**: Use MFI. The overbought/oversold levels (80/20) provide mechanical entry and exit signals. MFI is purpose-built for oscillating markets.

- **For divergence spotting**: Use both. CMF shows momentum divergence; MFI shows intensity divergence. A pattern appearing on both is more robust.

- **For confirmation**: Combine either indicator with volume itself. An MFI spike to 90 on light volume is weaker than the same reading on heavy volume. CMF rising on declining volume is a yellow flag.

## See also

<div class="wiki-seealso">

### Closely related

- Volume — the foundation of both CMF and MFI
- [Accumulation Distribution](/accumulation-distribution/) — the base line that CMF smooths
- RSI — the oscillator formula that MFI adapts
- Overbought Oversold — the MFI-centric concept
- Divergence — the pattern both indicators excel at spotting
- Money Flow — the concept underlying both indicators

### Wider context

- Technical Analysis — the discipline both indicators serve
- Momentum Indicators — the broader family of indicators
- [Support and Resistance](/support-and-resistance/) — price levels MFI overbought/oversold often occur at
- [Trend Following](/trend-following/) — the strategy CMF is well-suited for

</div>

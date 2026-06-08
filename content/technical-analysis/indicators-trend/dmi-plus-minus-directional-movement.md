---
title: "DMI Plus and Minus: Reading Directional Movement"
description: "The +DI and −DI lines measure trend strength and direction. Learn how their crossovers signal shifts and why filtering with ADX prevents false signals."
keywords:
  - dmi plus minus directional movement indicator
  - di lines adx
  - directional movement index
  - trend direction indicator
  - adx di crossover
  - positive negative di
---

*The **DMI plus and minus directional movement** indicator splits trend direction into two lines: +DI (positive directional indicator) and −DI (negative directional indicator). Their crossovers mark momentum reversals, but using them without an ADX filter generates excessive false signals in choppy, range-bound markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DMI +DI and −DI — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Two directional lines measuring uptrend and downtrend momentum separately.</div>

|   |   |
|---|---|
| **What they measure** | Strength of upward movement (+DI) and downward movement (−DI) |
| **Calculation** | Ratio of directional movement over true range, smoothed over 14 periods |
| **Typical period** | 14 bars (configurable) |
| **Best use case** | Confirming trend direction when ADX is rising |
| **Key weakness** | Generates whipsaws in sideways markets without ADX filter |
| **Crossover signal** | +DI above −DI = uptrend; −DI above +DI = downtrend |

</aside>

## How +DI and −DI are calculated

The **DMI plus and minus directional movement** indicator begins by measuring directional movement itself. Each bar's upward movement is the distance from yesterday's low to today's high (if positive). Downward movement is yesterday's high minus today's low (if positive). Only one directional move counts per bar—never both.

These raw directional values are then summed over the chosen period (usually 14 bars) and divided by the **true range** sum, which captures the full price range including gaps. The result is normalized to a 0–100 scale. Higher +DI means recent bars are pushing higher; higher −DI means recent bars are pushing lower. When both are low, price is consolidating.

The actual formula uses smoothing (Wilder's exponential moving average) to prevent erratic spikes. A 14-period setting is standard, but traders often adjust to 7 or 21 depending on timeframe sensitivity.

## +DI and −DI crossovers: what they signal

A **crossover** occurs when one line crosses above the other. Traditionally:

- **+DI crosses above −DI** → bullish signal (uptrend beginning or strengthening)
- **−DI crosses above +DI** → bearish signal (downtrend beginning or strengthening)

These crossovers can be clean and decisive in trending markets. A +DI breakout above −DI that holds for several bars often precedes a move. However, many traders find standalone crossovers are unreliable—especially when both DI lines are low (below 25). This is where the crossover can whip back and forth without meaningful price movement.

The visual advantage of +DI and −DI is that they separate bullish and bearish force, making the handoff clearer than a single oscillator. Traders can also spot divergences: if price makes a new low but −DI doesn't, it hints at weakening downward momentum.

## Why ADX filtering is essential

The **ADX (Average Directional Index)** is not a direction line itself; it measures trend *strength* on a 0–100 scale. It rises when one DI line pulls decisively away from the other and falls when the DI lines converge.

Using +DI and −DI crossovers in isolation produces numerous false signals in range-bound markets. Two DI lines bouncing at similar levels (e.g., both oscillating between 20 and 30) will cross repeatedly, each one triggering a trade that reverses almost immediately.

The professional approach is to **trade +DI/−DI crossovers only when ADX is above a threshold**—commonly 25 or 30. This rule filters out chop and focuses on crossovers that coincide with genuine directional strength. A rising ADX alongside a DI crossover is far more reliable than the crossover alone.

Many platforms allow alerts when "+DI crosses above −DI AND ADX > 25," eliminating manual chart scanning. Without that second condition, even the sharpest trader accumulates losses in consolidations.

## Interpreting high and low DI values

When **+DI is well above −DI** (e.g., +DI at 35, −DI at 15), the uptrend is dominant and unambiguous. Price is likely rallying. Conversely, when −DI dominates, the downtrend has the upper hand.

When **both DI lines are high** (e.g., +DI at 40, −DI at 35), the market is strongly directional but the dominance is narrow. This can precede a reversal—the weaker line may be about to cross below the stronger one. Experienced traders watch for this narrowing as a warning.

When **both DI lines are low** (below 20), the market is consolidating or moving sideways. Neither buyers nor sellers have clear control. Crossovers in this regime are noise and should be ignored unless ADX is rising sharply.

## Practical limitations

**Lag from smoothing:** The 14-period exponential smoothing built into +DI and −DI introduces delay. The indicator confirms a trend but rarely catches the exact turning point. Early-period bar reactions often move faster than the DI lines can register.

**No overbought/oversold bounds:** Unlike RSI or Stochastics, +DI and −DI do not have absolute extreme levels. A +DI reading of 50 is very strong, but a +DI of 45 is not necessarily "overbought"—it depends on context and volatility.

**Choppy behavior on lower timeframes:** On 1-minute or 5-minute charts, +DI and −DI can whip erratically unless ADX is exceptionally high. Most traders reserve the DMI for 4-hour, daily, or weekly charts where trends are more durable.

**Not suited for mean-reversion:** The indicator is directional by design. If your strategy thrives on reverting to the mean, a pure trend-following signal like +DI/−DI crossovers will fight you constantly.

## Combining DMI with other indicators

Many trend traders pair +DI/−DI with [price-to-earnings-ratio](/price-to-earnings-ratio/) or moving averages to confirm that price is also in alignment. For example, if +DI crosses above −DI but price is below its 200-period [moving-average](/moving-average/), the signal is weaker.

Another pairing is the [Bollinger Bands](/bollinger-bands/) (if your platform has them): a DI crossover near the upper or lower band carries more conviction than one in the middle. Some traders also use volume confirmation—a DI crossover on light volume is often false.

The MACD (if available) can serve as a secondary momentum check. If +DI crosses above −DI but MACD has not crossed its signal line, the move may be incomplete.

## When to override a DI crossover

Even with ADX filtering, certain contexts warrant caution:

- **Large gap against the crossover direction:** If +DI crosses above −DI but the open gaps below yesterday's close, momentum may be contested.
- **Rejection from a key level:** A DI crossover that immediately hits an old resistance and bounces back suggests the crossover was a feint.
- **End of major news event:** Crossovers in the 10-minute bar immediately after earnings or central bank decisions are often traps as volatility normalizes.

## See also

<div class="wiki-seealso">

### Closely related

- ADX indicator — Measures trend strength to filter DMI crossovers
- [Moving average](/moving-average/) — Baseline directional confirmation
- [Bollinger Bands](/bollinger-bands/) — Volatility context for DI moves
- MACD — Secondary momentum confirmation

### Wider context

- [Trend-following](/trend-following/) — The strategy class DMI serves
- [Support and resistance](/support-and-resistance/) — Price levels to combine with DI signals
- [Volatility smile](/volatility-smile/) — Market regime context
- [Supertrend vs Parabolic SAR](/supertrend-vs-parabolic-sar-comparison/) — Alternative trailing-stop approaches

</div>

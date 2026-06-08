---
title: "How to Calculate the Advance-Decline Line"
description: "Step-by-step process for calculating the advance-decline line from daily advances and declines, with a worked numeric example."
keywords:
  - advance-decline line calculation
  - a-d line cumulative
  - market breadth indicator
  - daily advances declines
  - technical analysis breadth
  - cumulative advance decline
image: /svg/technical-analysis.svg
---

*The **advance-decline line** is a running total of the cumulative difference between the number of stocks that rose and fell on a given day, reset at the start of each trading period. To calculate it, you subtract daily declines from daily advances and add the result to the previous day's total.*

## What the Advance-Decline Line Measures

The advance-decline line, often called the A-D line, is a momentum gauge that tracks whether more stocks are climbing than falling within a broad index. Unlike price-weighted averages, which can be lifted by a few heavy hitters, the A-D line counts raw participation: every stock that closes above its previous close counts as an advance; every one that closes below counts as a decline. Unchanged stocks are typically ignored.

The line's strength lies in its ability to reveal hidden divergences. An index may reach new highs while fewer and fewer stocks are participating—a signal that breadth is weakening even as prices appear robust. This disconnect often foreshadows reversals.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Advance-Decline Line — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A cumulative daily tally of net advances minus declines, used to assess the breadth of market moves.</div>

|   |   |
|---|---|
| **Calculation** | Prior A-D total + (today's advances − today's declines) |
| **Reset period** | Optional; often weekly, monthly, or per market cycle |
| **Data source** | Daily advances and declines from an exchange (NASDAQ, NYSE) |
| **Strength** | Captures participation breadth independent of price movements |
| **Weakness** | Lags price indices; heavily influenced by highly liquid names |
| **Use case** | Detect bullish or bearish divergences; assess underlying momentum |

</aside>

## The Basic Formula

The advance-decline line formula is straightforward:

**A-D Line(today) = A-D Line(yesterday) + (Advances − Declines)**

The result is always a single cumulative number. Because it includes all prior days, the A-D line should generally trend upward in a bull market and downward in a bear market—but that is not guaranteed. The absolute value has no meaning; only the direction and slope matter.

## Step-by-Step Calculation with a Worked Example

Imagine you are tracking the advance-decline line for a fictional market starting Monday. Here is the data:

| Day | Advances | Declines | Net (Adv − Decl) | A-D Line |
|---|---|---|---|---|
| Start (prior) | — | — | — | 0 |
| Monday | 250 | 150 | +100 | 100 |
| Tuesday | 200 | 180 | +20 | 120 |
| Wednesday | 160 | 240 | −80 | 40 |
| Thursday | 220 | 170 | +50 | 90 |
| Friday | 310 | 140 | +170 | 260 |

**Monday calculation:**
- Advances: 250, Declines: 150
- Net: 250 − 150 = +100
- A-D Line: 0 + 100 = **100**

**Tuesday calculation:**
- Advances: 200, Declines: 180
- Net: 200 − 180 = +20
- A-D Line: 100 + 20 = **120**

**Wednesday calculation:**
- Advances: 160, Declines: 240
- Net: 160 − 240 = −80
- A-D Line: 120 + (−80) = **40**

Notice that on Wednesday, even though the prior A-D line was positive, more stocks declined than advanced. The line moved down, pulling the cumulative total lower. This is where breadth weakness becomes visible.

**Thursday and Friday** continue the same logic, with Thursday adding 50 and Friday adding 170, ending the week at 260.

## Charting and Interpretation

Once calculated, the A-D line is charted over time, usually against a price index (like the [S&P 500 Index](/sp-500-index/)) on the same graph or in a separate pane. Technicians look for three patterns:

**Confirmation.** Both the index and the A-D line trend higher. This suggests broad, sustainable buying.

**Positive divergence.** The index is flat or falling, but the A-D line rises. Early buyers are accumulating beneath the surface, sometimes preceding a reversal higher.

**Negative divergence.** The index is rising, but the A-D line is flat or falling. Fewer stocks are participating, a warning that the rally may weaken.

A negative divergence is often considered more predictive of a top than a positive divergence is of a bottom—selling often hits suddenly, while recovery builds more gradually.

## Data Sources and the Role of Exchanges

The daily advances and declines figures come from stock exchanges themselves. The [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) each publish their own data, reflecting the stocks traded on their respective platforms. Some technicians calculate a single A-D line for one exchange; others blend multiple exchanges or create sector-specific A-D lines.

Because the NYSE and NASDAQ have different listings and liquidity, their A-D lines can diverge. A narrowing NYSE A-D line alongside a rising NASDAQ A-D line might indicate that blue-chip participation is weaker even as growth and tech names are leading.

## Reset Conventions

The A-D line is cumulative, so it never truly "resets"—it simply keeps adding and subtracting. However, some analysts choose to restart the counter at the beginning of a new market cycle (a major bottom) or at calendar points (a new year). This is a stylistic choice and does not change the calculation method.

The advantage of a reset is cleaner visual comparison across different market regimes. The disadvantage is loss of longer-term context. Most professional technicians do not reset and read the line as a continuous record.

## Limitations

The A-D line counts every stock equally, regardless of [market capitalization](/market-capitalization/) or trading volume. A penny stock counts the same as Apple. In practice, this means the A-D line can look strong even when most of the market's value is concentrating in a small number of megacap names—and vice versa.

Additionally, the A-D line is a lagging indicator. It reflects what already happened yesterday; it does not predict tomorrow. Many traders use it to confirm existing [trend](/trend-following/) or warn of hidden weakness, rather than as a standalone signal.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Capitalization](/market-capitalization/) — why share count matters less than dollar volume
- Technical Analysis — the parent discipline of breadth measurement
- [Support and Resistance](/support-and-resistance/) — complementary price-level concepts in charting
- [Moving Average](/moving-average/) — smoothing techniques applied to A-D lines
- Market Breadth — the broader concept of participatory strength
- [Trend Following](/trend-following/) — how breadth confirms directional conviction

### Wider context

- [Stock Market](/stock-market/) — the venue generating the raw advance-decline data
- [Market Cycle](/market-cycle/) — the phases within which breadth patterns emerge
- [Momentum Investing](/momentum-investing/) — a strategy sometimes informed by breadth indicators
- [Price Discovery](/price-discovery/) — how individual stock moves aggregate into market signals

</div>

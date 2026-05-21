---
title: "Point-and-figure chart"
description: "A point-and-figure chart displays price movement as a grid of X's (upward) and O's (downward), eliminating time and focusing on price reversals at specific levels."
keywords:
  - point-and-figure
  - p&f
  - technical analysis
  - price-based chart
  - x's and o's
image: "/svg/technical-analysis.svg"
---

*A **point-and-figure chart** (or **P&F chart**) displays price movement as a two-dimensional grid where X's represent upward price moves and O's represent downward moves. Each column of X's or O's represents a single up or down movement; a new column starts only when price reverses by a specified amount. Time is irrelevant; the chart focuses entirely on price levels and reversals. Point-and-figure charts are prized for identifying support, resistance, [breakouts](/technical-analysis/channel-pattern), and clean chart patterns. They are one of the oldest technical analysis tools, dating back to the 1800s.*

<div class="wiki-hatnote">

For time-based charts, see [candlestick chart](/technical-analysis/candlestick-chart). Other price-based alternatives include [renko](/technical-analysis/renko-chart) and [kagi](/technical-analysis/kagi-chart) charts.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Point-and-figure chart — key facts</div>

<img src="/svg/technical-analysis.svg" alt="A point-and-figure grid with X's and O's showing price movement" />

<div class="wiki-infobox-caption">Point-and-figure grid: X's up, O's down; time absent; reversals trigger new columns; patterns are geometrically clear.</div>

|   |   |
|---|---|
| **Grid structure** | Rows = price levels; columns = reversals |
| **X's** | Represent upward price moves |
| **O's** | Represent downward price moves |
| **Box size** | Fixed price increment (e.g., $1, 5¢) |
| **Reversal amount** | Trigger for new column (e.g., 3 boxes) |
| **Time axis** | Absent; irrelevant to chart |
| **Support/resistance** | Extremely clear at horizontal levels |
| **Patterns** | Head-and-shoulders, triangles, etc. appear geometrically |
| **Advantage** | Noise elimination, support/resistance clarity, patterns |
| **Disadvantage** | Unusual appearance, difficult for real-time trading |

</aside>

## How point-and-figure charts work

The chart is arranged as a grid. Each row represents a price level (e.g., $100, $101, $102). Each column represents a movement in one direction. As price rises, X's are placed in a column from bottom to top, one X per box size (e.g., one X per $1 move). When price reverses downward by the reversal amount (e.g., 3 boxes = $3), the chart stops the X column and starts a new column of O's.

The process continues: when price rises again by the reversal amount, the O column stops and a new X column begins.

## Box size and reversal amount

Two parameters define a P&F chart:

**Box size** is the price increment per row. A $1 box size means each row represents $1 of price movement. A $0.10 box size creates a more granular chart.

**Reversal amount** is the trigger for switching columns. A three-box reversal means price must move 3 × box size in the opposite direction to start a new column. Using a $1 box and 3-box reversal, price must move $3 to trigger a reversal.

Larger box sizes and reversal amounts create simpler, noisier-filtered charts. Smaller values create more granular information.

## Support and resistance on P&F charts

Point-and-figure charts excel at showing support and resistance. When X's cluster at the same price level (all in the same row), that level is obviously supported—the price has bounced there multiple times. Similarly, a level where multiple O columns start is clearly resistance—price has repeatedly failed to break above it.

This clarity is one of P&F's greatest strengths: support and resistance jump out geometrically.

## Patterns on point-and-figure charts

Point-and-figure charts naturally form recognizable patterns:

- **Double bottom:** Two columns of O's reaching the same low, followed by a column of X's that breaks above prior highs. Bullish.
- **Double top:** Two columns of X's reaching the same high, followed by a column of O's that breaks below prior lows. Bearish.
- **Head and shoulders:** A tall column of X's (head), flanked by shorter columns (shoulders). Bearish.
- **Triangle:** Columns of alternating X's and O's that converge to a point, then break out. 

These patterns emerge geometrically from the grid structure and are often cited as evidence of P&F's power.

## Advantages of point-and-figure charts

**Extreme noise reduction:** Only significant price reversals matter. Intraday chop, small bounces, and minor fluctuations are invisible.

**Clear support and resistance:** Levels where price has tested multiple times appear as obvious horizontal lines of X's or O's.

**Clean chart patterns:** Triangles, head-and-shoulders, double tops/bottoms, and other patterns appear more geometrically pure than on candlestick charts.

**No time distortion:** Because time is absent, a fast market that moves $5 in a day and a slow market that takes a month to move $5 appear identically on the chart—only the price matters.

## Disadvantages of point-and-figure charts

**Unfamiliar to most traders:** Candlesticks are now the default. Point-and-figure charts look alien to those trained on candlesticks, creating a learning curve.

**Real-time trading difficulty:** Like renko and kagi, P&F charts are difficult for live trading. A column might not change for hours or days if a reversal has not been triggered.

**Parameter selection:** Box size and reversal amount are arbitrary. Different choices produce different charts and signals.

**Limited popularity in modern platforms:** While P&F is available on major platforms, it is less featured and less widely discussed than candlesticks.

**Hidden intraday volatility:** A single X or O can represent significant intraday price swings, but that detail is hidden.

## Parameter selection

Choosing box size and reversal amount requires judgment:

- **Stocks under $10:** $0.25 or $0.50 box size; three-box reversal.
- **Stocks $10–$100:** $1 box size; three-box reversal.
- **Stocks over $100:** $2–$5 box size; three-box reversal.
- **Forex or commodities:** Percentage-based or ATR-based sizing.

The goal is a chart that shows clear trends and patterns without excessive noise.

## Point-and-figure versus candlesticks

| Aspect | Candlestick | Point-and-figure |
|--------|-------------|------------------|
| Time axis | Present | Absent |
| Data points | Four (OHLC) | Price levels only |
| Patterns | Defined by candle shape | Geometric on grid |
| Support/resistance | Inferred from clustering | Obvious from grid clustering |
| Noise | Present (real-time) | Filtered by reversal amount |
| Real-time trading | Excellent | Poor |
| Learning curve | Moderate | Steep |

## Historical use and modern perspective

Point-and-figure charts were standard before candlesticks became popular. Professional traders 50+ years ago relied on P&F charts. Modern practitioners often view them as a specialist tool—excellent for certain purposes (identifying support/resistance, patterns) but less suitable for real-time decision-making than candlesticks.

## Real-world use

A trader might:
1. Use a P&F chart (with $1 box, 3-box reversal) to identify major support at $95 and resistance at $110.
2. Switch to a daily candlestick chart to wait for price to approach $95, then look for a bullish pattern ([hammer](/technical-analysis/hammer-candle), [doji](/technical-analysis/doji), etc.) to enter long.
3. Use the P&F chart to identify the $110 resistance level as a profit target.

## Academic perspective

Point-and-figure charts have minimal academic study. While some early research referenced them, modern academic technical analysis literature almost exclusively focuses on candlesticks. This lack of research does not mean P&F is ineffective; it reflects academia's relative disinterest in practical trading tools that are not easily quantifiable.

## See also

<div class="wiki-seealso">

### Price-based charts

- [Renko chart](/technical-analysis/renko-chart) — fixed-size bricks, similar philosophy
- [Kagi chart](/technical-analysis/kagi-chart) — thin/thick lines based on reversals
- [Candlestick chart](/technical-analysis/candlestick-chart) — time-based alternative
- [Line chart](/technical-analysis/line-chart) — closes only

### Analysis concepts

- [Support and resistance](/technical-analysis/support-and-resistance) — especially clear on P&F
- [Head-and-shoulders](/technical-analysis/head-and-shoulders) — classic pattern visible on P&F
- [Double-top](/technical-analysis/double-top) and [double-bottom](/technical-analysis/double-bottom) — geometric patterns on P&F

</div>

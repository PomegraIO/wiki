---
title: "Renko chart"
description: "A renko chart displays price movement as uniform-sized rectangular bricks, eliminating the time axis and focusing purely on price changes of a specified magnitude."
keywords:
  - renko
  - brick chart
  - technical analysis
  - price-based chart
  - volatility
image: "/svg/technical-analysis.svg"
---

*A **renko chart** is a price-based charting method that displays price movement as uniform rectangular "bricks." Each brick represents a fixed price increment (e.g., $1, $5, or 2% depending on the security). A new brick is drawn only when price moves by at least that amount; time plays no role in the chart. The result is a highly filtered view of price action that removes intraday noise and focuses purely on significant price moves. The name comes from the Japanese word "renga," meaning brick. Renko charts are favored by traders seeking to filter out chop and identify clean support, resistance, and trend.*

<div class="wiki-hatnote">

For time-based charts, see [candlestick chart](/candlestick-chart/). Other price-based alternatives include [kagi charts](/kagi-chart/) and [point-and-figure charts](/point-and-figure-chart/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Renko chart — key facts</div>

<img src="/svg/technical-analysis.svg" alt="A renko chart showing uniform rectangular bricks of green and red" />

<div class="wiki-infobox-caption">Renko bricks: uniform size, pure price focus, no time axis—ideal for filtering noise.</div>

|   |   |
|---|---|
| **Basis** | Price movement, not time |
| **Brick size** | Fixed increment (dollar, percentage, ATR) |
| **Brick colour** | Green = up move, red = down move |
| **New brick requirement** | Price must move by brick size |
| **Time axis** | Absent; irrelevant to the chart |
| **High/low detail** | Not explicitly shown; only close position |
| **Advantage** | Noise reduction, clear trends, clear support/resistance |
| **Disadvantage** | Difficulty with live trading; no real-time view |
| **Best for** | Identifying clean trends, support/resistance zones |
| **Poor for** | Timing entries with precision; real-time decisions |

</aside>

## How renko bricks form

In a renko chart, the trader specifies a brick size—for example, $2 per brick. As price moves, a new brick is drawn only when the price moves by at least $2. If the price is at $100 and rises to $101.50, no new brick appears; the move is too small. When price reaches $102, a new brick appears at that level. If price then falls to $100.50, no brick appears in the opposite direction (a $2 move is needed). Only when price drops to $98 does a down brick appear.

The result is a chart that shows only "significant" moves—moves larger than the brick size—and ignores everything smaller. This dramatically simplifies the chart and removes chop.

## Advantages of renko charts

**Noise elimination:** The fixed brick size acts as a filter. Minor retracements, whipsaws, and choppy intraday moves are invisible. A renko chart shows only the "meat" of the move.

**Clear trends:** Because small moves are filtered out, trends become obvious. An extended uptrend appears as a tall column of green bricks with no red interspersed; a downtrend appears as a tall column of red. This clarity makes trends unmistakable.

**Support and resistance:** Once a price level has been tested multiple times (multiple bricks bouncing off a level), it becomes obvious support or resistance. Renko charts make these levels jump out visually because they cluster at key prices.

**Removes timing ambiguity:** Because time is absent, a renko chart sidesteps the question "Which timeframe should I use?"—a perennial source of confusion in traditional charts. The brick size is the only variable.

## Disadvantages of renko charts

**No real-time information:** Renko charts are difficult to use for live trading decisions. Because a new brick only appears when the brick size is reached, a trader watching prices move might not see a new brick for hours or even days. A 1% brick size on a slow stock might mean a new brick appears once a week.

**Hidden volatility within bricks:** While a brick shows that price moved by the brick size, it does not show whether price reached that level and immediately reversed, or whether it moved smoothly. The intraday volatility is hidden.

**Difficulty with precise entry and exit:** Traditional candlesticks and time-based charts allow precise entry and exit timing—"sell when the close is above this level." Renko charts, with their discrete brick structure, offer less flexibility for precision.

**Brick size selection is arbitrary:** The choice of brick size—$1, $5, 2%, ATR-based—is subjective. Different brick sizes produce different charts and signals. There is no "correct" brick size.

**Gap and open prices ignored:** Renko charts focus on the close (or in some implementations, the high and low). Opens are ignored, and gaps between time periods are not visible.

## Brick size selection

The brick size is the most critical parameter. Too small, and the renko chart becomes almost as cluttered as a candlestick chart. Too large, and important moves are missed. Common approaches:

- **Fixed dollar amounts:** $1, $5, $10 for stocks; 50 pips for forex. The amount depends on the volatility of the security.
- **Percentage:** 2%, 5%, or 10%. This adjusts automatically as the stock's price level changes.
- **ATR-based:** Use the average true range as the brick size, so it adapts to volatility.
- **Intuitive observation:** Set the brick size so that the chart looks "right"—showing clear trends without too much noise.

## Renko compared to other price-based charts

**Point-and-figure:** Point-and-figure is another price-based chart, but it uses a two-dimensional X's-and-O's grid. Both renko and P&F eliminate time, but the visual presentation differs dramatically.

**Kagi:** Kagi charts use thin and thick lines based on price reversals, not fixed increments like renko. Kagi is more responsive to reversals than renko, which uses fixed brick sizes.

## Common uses for renko charts

**Identifying clean support and resistance:** When multiple bricks cluster at a price level, that level becomes an obvious support or resistance. This is easier to see on renko than on candlesticks.

**Swing trading:** Some swing traders use renko to identify multi-brick trends and trade them, using time-based charts to time the precise entry and exit.

**Removing noise for long-term analysis:** An investor examining a stock over years can use renko to see the long-term trend without the noise of daily fluctuations.

**Combining with time-based charts:** A trader might use a renko chart to identify major support, resistance, and trend, then switch to a candlestick chart to time the entry and exit.

## Renko and gaps

In traditional time-based charts, a gap (price opening far from the prior close) is visible as a jump in the chart. In renko charts, there is no open price, so gaps are not explicitly shown. However, if an overnight gap causes the price to skip over a renko brick level, that level is simply skipped—not shown on the chart.

## Real-world application

A trader might:
1. Use a renko chart (with a 2% brick size) to identify that a stock is in a strong uptrend and key support is at $50.
2. Switch to a daily candlestick chart to time an entry near $50, looking for a hammer or other bullish reversal.
3. Use a renko chart again to identify when the uptrend is broken (a series of red bricks), signaling an exit.

## Academic perspective

Renko charts are rarely studied in academic literature. They are a practitioner tool, popular among active traders but not part of formal academic research on technical analysis. Their effectiveness depends heavily on brick size selection and the assumption that price moves larger than the brick size are "significant"—an assumption not rigorously tested.

## See also

<div class="wiki-seealso">

### Price-based charts

- [Point-and-figure chart](/point-and-figure-chart/) — X's and O's, price-based
- [Kagi chart](/kagi-chart/) — thin/thick lines based on reversals
- [Candlestick chart](/candlestick-chart/) — time-based alternative
- [Line chart](/line-chart/) — closes only

### Analysis concepts

- [Support and resistance](/support-and-resistance/) — key levels visible on renko
- [Trendline](/trendline/) — trends easier to identify
- [Volume](/on-balance-volume/) — not directly shown on renko

</div>

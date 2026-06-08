---
title: "Volume-Weighted Moving Average vs VWAP: Key Differences"
description: "Volume-weighted moving average and VWAP both weight price by volume, but differ in reset frequency, calculation span, and ideal use cases for trend versus intraday trading."
keywords:
  - volume weighted moving average vs vwap
  - vwma vs vwap
  - volume-weighted indicators
  - technical analysis volume
  - trend-following indicators
  - intraday benchmarking
  - moving average comparison
image: /svg/technical-analysis.svg
---

*Both **volume-weighted moving average** (VWMA) and **VWAP** (volume-weighted average price) use volume to weight price, but they reset at different intervals and serve distinct purposes: VWMA tracks longer-term trend momentum, while VWAP acts as an intraday benchmark that resets each day.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VWMA vs VWAP — Key Facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two volume-weighted tools with different reset windows and trader use cases.</div>

|   |   |
|---|---|
| **VWMA reset window** | Runs across user-selected lookback (typically 10–50 periods) |
| **VWAP reset window** | Resets to zero at market open each trading day |
| **Calculation span** | VWMA: rolling; VWAP: cumulative from day's open |
| **Primary use** | VWMA: trend identification; VWAP: intraday entry/exit reference |
| **Applicable timeframes** | VWMA: any; VWAP: intraday (1-min, 5-min, 15-min, hourly) |
| **Reset trigger** | VWMA: lookback period expires; VWAP: new trading day begins |

</aside>

## How VWMA and VWAP Differ in Construction

VWMA and VWAP are mathematically distinct. VWMA takes a rolling window—say, the last 20 candles—and weights each candle's closing price by its volume, then divides the sum of weighted prices by the sum of volumes. As new candles arrive, the oldest candle rolls off the window, and the calculation refreshes.

VWAP, by contrast, accumulates from the market open. It sums the product of typical price (high + low + close) ÷ 3 and volume from the first trade of the day through the current moment, then divides by cumulative volume since open. The denominator never resets until the market closes.

This structural difference means VWMA can climb, fall, or flatline across any lookback you choose. VWAP always starts fresh each morning, so it converges toward the day's open as volume accumulates.

## When VWMA Suits Trend-Following

VWMA is a trend indicator. Traders use it to identify sustained directional moves over days or weeks. Because it uses a rolling window (often 10 to 50 periods), it's sensitive enough to catch trend changes while smoothing out small noise. A price crossing above VWMA suggests upside momentum building; a cross below suggests weakening.

VWMA works on any timeframe—daily, 4-hour, 1-hour, or intraday. Its advantage is flexibility: you can adjust the lookback period to match your holding horizon. Swing traders often use a 20-period VWMA on a 1-hour chart; position traders might use 50 on the daily.

Because VWMA carries forward from day to day, it captures multi-day, multi-week trends. It does not reset at market open, so it integrates information across sessions.

## When VWAP Acts as an Intraday Benchmark

VWAP is built for intraday traders and institutional execution. Its appeal is clear: it answers "what has the volume-weighted fair price been *today*?" If you buy at a price above VWAP, you've overpaid relative to the day's balance of volume. If you buy below, you've gotten a bargain.

Institutional traders use VWAP as an arrival price benchmark. If they execute a large order and achieve an average price close to VWAP, they've executed efficiently—they didn't move the market against themselves more than the day's natural flow would suggest.

Intraday swing traders use VWAP as dynamic support and resistance. A stock rising above VWAP early in the day often holds that territory through lunch and into the close if buying is genuine. A sharp drop below VWAP can signal capitulation or panic selling.

Because VWAP resets every day, it is most useful on shorter timeframes (1-minute, 5-minute, 15-minute) where the single-day window is meaningful. On a daily chart, VWAP is far less practical—it becomes a single point per day, which is hard to read as a trend.

## Practical Differences in Application

Suppose a stock opens at $50 and spends the morning trading between $49.50 and $50.50. By noon, VWAP might sit at $50.10, reflecting the morning's volume. VWMA, if set to a 20-period (say, hourly) lookback, might sit at $50.30 if the last 20 hours included heavier volume at $50.50.

Later that afternoon, the stock rallies to $52. VWAP climbs toward $51 (new highs were reached; cumulative price shifts up). VWMA also rises but may lag or lead depending on whether that afternoon rally included larger volume than bars in the 20-period window.

A trader using VWAP for intraday entry might wait for a retest of VWAP at $51, then enter a long if support holds. A trader using VWMA for a swing trade might buy the break above the 20-hour VWMA, signaling momentum.

## Which Indicator Wins?

Neither. They solve different problems. VWMA answers "is this stock trending up or down based on multi-period volume weighting?" VWAP answers "where is today's fair price, and am I above or below it?"

A trader might use both. Use VWMA to identify an uptrend; use VWAP to time the intraday entry within that trend. If price is above the 50-period VWMA on the daily, the intermediate trend is up. Then, on a 5-minute chart, wait for a dip to VWAP as a pullback entry.

The key is intention. If you hold positions for days or weeks, VWMA guides trend. If you're scaling in and out during a single session, VWAP calibrates fair value.

## Common Pitfalls

Do not compare a 5-minute VWAP to a daily VWMA on the same chart—they operate at wildly different scales. A 5-minute VWAP resets 78 times a day (once per trading session). A daily VWMA spans weeks of data.

Do not assume VWAP support is universal. On low-volume days, VWAP can sit in the middle of the range all day, offering little insight. On high-volume reversals, VWAP can jump sharply, rendering yesterday's level irrelevant.

Do not use VWMA as a hard entry signal on longer timeframes without confirming volume divergence or other structure. A price crossing VWMA is a *suggestion* of trend, not a trade.

## See also

<div class="wiki-seealso">

### Closely related

- [Moving Average](/moving-average/) — foundational smoothing tool and trend baseline
- [Volume](/stock-market/) — why volume matters to price validation
- [Support and Resistance](/support-and-resistance/) — how traders use price levels
- [Historical Volatility](/historical-volatility/) — volatility context for entry setup
- [Price Discovery](/price-discovery/) — how volume and price interact to establish value

### Wider context

- Technical Analysis — candlesticks, patterns, and momentum
- [Algorithmic Trading](/algorithmic-trading/) — how machines exploit price and volume
- [Market Maker Trading](/market-maker-trading/) — institutional execution and fair value
- [Execution Risk](/execution-risk/) — slippage and impact of order size

</div>

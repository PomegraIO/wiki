---
title: "Moving Average"
description: "Simple and exponential moving averages that smooth price data and serve as dynamic trend references and support/resistance levels."
keywords:
  - moving average
  - simple moving average
  - exponential moving average
  - trend smoothing
  - support and resistance
  - price momentum
image: "/svg/technical-analysis.svg"
---

*A **Moving Average** is a smoothing calculation that reduces the noise in price data by averaging the close (or other metric) over a rolling window of N bars or periods. The two main variants are the simple moving average (SMA), which weights all periods equally, and the exponential moving average (EMA), which weights recent data more heavily. Moving averages serve dual purposes: they filter out short-term volatility to reveal the underlying trend, and they often act as dynamic support and resistance levels that markets respect repeatedly.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Moving Average — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Lagging indicator that smooths price noise and identifies trend direction.</div>

|   |   |
|---|---|
| **What it is** | A rolling average of price over a fixed number of periods |
| **Also called** | SMA (simple), EMA (exponential), weighted moving average (WMA) |
| **Simple formula** | Sum of closing prices over N periods, divided by N |
| **Exponential formula** | Current price × weighting factor + previous EMA × (1 − factor) |
| **Common periods** | 20, 50, 100, 200 (daily); 9, 21 (intraday) |
| **Primary use** | Identify trend direction; mark support and resistance |
| **Lag characteristic** | SMA lags more than EMA; longer periods lag more than shorter ones |

</aside>

## Simple moving average (SMA)

The simple moving average is the most basic form: add up the closing prices of the last N periods and divide by N. A 20-day SMA averages the close over the past 20 trading days. A 50-day SMA looks back 50 days. Each time a new day closes, the oldest day drops out of the calculation and the newest is added, creating a moving window.

The beauty of SMA is simplicity and transparency. A trader can intuitively understand that a 50-day SMA at 120 means the average price over the past 50 days is 120. If the current price is 130, the stock is trading above its average. If it's 110, it's trading below. The level often acts as a support or resistance: when price falls toward the 50-day SMA, buyers frequently step in, and when price rises toward it from below, sellers appear.

The downside is lag. Because SMA weights all periods equally, a sharp price spike 40 days ago contributes as much to today's average as yesterday's close. This means the SMA can significantly lag the actual trend, especially over longer lookback periods.

## Exponential moving average (EMA)

The exponential moving average assigns greater weight to recent prices and progressively less weight to older data. The calculation is slightly more complex: multiply today's close by a weighting factor, then add the previous EMA value multiplied by (1 − the weighting factor). The result is that an EMA "hugs" current price more closely than an SMA of the same length.

For a 50-day EMA, the weighting factor is 2 ÷ (50 + 1) ≈ 0.0392. This means today's close gets weight 3.92%, and the previous EMA gets 96.08%. Over many days, the cumulative effect is that prices from 5–15 days ago carry the most influence, while older data fades exponentially.

Traders often prefer EMA over SMA for trend-following, because it turns faster and less often whipsaws when price reverses sharply. The cost is that EMA is harder to compute mentally and less intuitive to understand.

## Crossovers and trend signals

A moving-average crossover occurs when a faster (shorter-period) average crosses above or below a slower (longer-period) average. A classic example is the 50-day MA crossing above the 200-day MA—called a [golden cross](/golden-cross-death-cross/)—which is widely viewed as a bullish signal marking the start of a new uptrend. Conversely, when the 50-day crosses below the 200-day—a [death cross](/golden-cross-death-cross/)—it is often interpreted as a bearish reversal.

These crossovers are among the few technical analysis signals with historical credibility in academic literature. Studies show that 50/200 crossover strategies, particularly in equity indices, have captured more than random performance, though transaction costs and [slippage](/slippage/) often erase the edge in real trading.

Shorter-period crossovers (e.g., 9-day vs. 21-day) generate more frequent signals and suit swing traders and day traders. Longer-period crossovers are slower and better suited to position traders and [value investors](/value-investing/) confirming a new regime.

## Support, resistance, and bounce zones

Beyond crossovers, moving averages often function as support in uptrends and resistance in downtrends. In a strong uptrend, price may dip to kiss the 50-day or 100-day SMA, find support, and bounce. In a downtrend, price may rally into the 50-day MA and fail, offering a short entry. This behaviour is sometimes attributed to algorithmic trading (many systems have buy/sell rules anchored to moving averages), sometimes to the cluster of mechanical stop losses placed just above or below the line, and sometimes simply to human psychology—traders watch the same levels and trade accordingly.

The effect is real but not universal. In choppy, trendless markets, moving averages whipsaw constantly and provide little edge. In strong trending markets, they can be remarkably reliable. The practical value depends on [volatility](/historical-volatility/) and whether a genuine trend exists.

## Choosing period length and weighting

There is no single "correct" moving-average period. Traders select periods based on their time horizon and the asset class. Day traders might use 9-, 20-, and 50-period EMAs on a 5-minute chart. Swing traders often use 10-, 20-, and 50-day EMAs. Longer-term investors focus on 50-, 100-, and 200-day SMAs. For exotic instruments like [futures contracts](/futures-contract/) or [cryptocurrency](/cryptocurrency-exchange/), trader convention varies widely.

The period choice should match the market you're trading. A 50-day MA is nearly meaningless on a 5-minute chart (it covers only a few hours of trading); a 9-period EMA on a weekly chart is too short to filter real noise. Overfitting to historical data—choosing the exact period that worked best in the past—is a common pitfall that fails in live trading.

## Combining multiple moving averages

Many traders layer multiple moving averages to filter signals and reduce whipsaws. A simple system might buy when price closes above the 20-day SMA *and* the 20-day closes above the 50-day, and the 50-day is above the 200-day. This triple-confirmation reduces false breakouts but also delays entry, allowing fast moves to pass before the signal triggers.

[Elliott Wave Theory](/elliott-wave-theory/) and [Fibonacci retracement](/fibonacci-retracement/) practitioners often use moving averages to validate wave reversals. If price completes a five-wave impulse and corrects, a trader might short only after price breaks below a key moving average, signalling the corrective structure is complete and a new impulse is underway.

## The lag reality

The critical limitation of moving averages is that they are inherently backward-looking. By definition, a 50-day MA reflects what has already happened over the past 50 days. It cannot predict the next bar. On days when the market reverses sharply—earnings surprises, central bank announcements, [credit events](/credit-event-sovereign/)—moving averages are often late, having already registered the old trend when the new one has just begun. This lag is the price paid for the filtering benefit.

Professional traders treat moving averages as one layer in a multi-factor decision, not as an oracle. They use them to confirm trend direction, to set stop losses, and to stage entries and exits—but always in conjunction with momentum indicators, price action, and fundamental catalysts.

## See also

<div class="wiki-seealso">

### Closely related

- [Golden Cross and Death Cross](/golden-cross-death-cross/) — 50-day and 200-day moving-average crossovers signalling trend shifts
- [Elliott Wave Theory](/elliott-wave-theory/) — wave patterns often validated by moving-average breakouts
- [Fibonacci Retracement](/fibonacci-retracement/) — pullback levels frequently combined with moving averages for confluence
- Technical Analysis — the discipline of chart-based price forecasting
- [Support and Resistance](/support-and-resistance/) — price levels where moving averages often align

### Wider context

- [Price Discovery](/price-discovery/) — the mechanism moving averages attempt to smooth and clarify
- Momentum Indicators — complementary tools measuring rate of change
- [Volatility Smile](/volatility-smile/) — another model of price behaviour
- [Stock Market](/stock-market/) — primary venue for moving-average applications

</div>

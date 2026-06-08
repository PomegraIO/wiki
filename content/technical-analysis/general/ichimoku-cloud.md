---
title: "Ichimoku Cloud"
description: "How the five Ichimoku lines encode support, resistance, momentum, and trend direction in a single overlay."
keywords:
  - ichimoku cloud
  - ichimoku indicator
  - technical analysis
  - support resistance
  - trend confirmation
image: "/svg/technical-analysis.svg"
---

*The **Ichimoku Cloud** (from Japanese "ichimoku kinko hyo," meaning "one glance at balance chart") is a comprehensive technical analysis framework combining five lines—Tenkan, Kijun, Senkou A, Senkou B, and Chikou—to display support, resistance, trend direction, and momentum in a single visual overlay. Developed in the 1960s by Japanese journalist Goichi Hosoda, it remains popular among swing and position traders for identifying trade-ready price levels with a single glance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ichimoku Cloud — five-line trend and support system</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis and price patterns." />

<div class="wiki-infobox-caption">A complete framework encoding trend, momentum, and support in layered lines and a colored cloud band.</div>

|   |   |
|---|---|
| **Components** | Five moving averages (Tenkan, Kijun, Senkou A, Senkou B) and a lagging line (Chikou). |
| **Primary signal** | Price above the cloud = uptrend; price below = downtrend; inside cloud = no clear trend. |
| **Momentum indicator** | Tenkan above Kijun = rising momentum; Tenkan below Kijun = falling momentum. |
| **Cloud definition** | Senkou A and B form the cloud; thickness and slope indicate trend strength. |
| **Lagging confirmation** | Chikou Span confirms trend if it closes above price; signals strength if price closes above it. |
| **Timeframe** | Best applied to 4-hour and daily charts; unreliable on 1-minute bars. |

</aside>

## The five components

**Tenkan Line** (conversion line): the average of the 9-period high and 9-period low. It captures short-term momentum and is the most reactive of the five lines. When Tenkan rises above Kijun, momentum is shifting upward; when it falls below, downward momentum emerges.

**Kijun Line** (base line): the average of the 26-period high and 26-period low. It represents the mid-point of the medium-term range and acts as dynamic support or resistance. A price that closes above Kijun in an uptrend often finds support at Kijun on pullbacks; a price that closes below Kijun in a downtrend faces resistance when trying to bounce.

**Senkou A** (leading span A): the average of Tenkan and Kijun, plotted 26 periods ahead into the future. This forward-plotting creates a self-fulfilling element—traders who expect Senkou A to be resistance often place sell orders there, reinforcing its effect.

**Senkou B** (leading span B): the average of the 52-period high and 52-period low, also plotted 26 periods ahead. It is slower and represents the longer-term trend. The region between Senkou A and Senkou B is shaded as a "cloud" (kumo). When Senkou A is above Senkou B, the cloud is green (bullish); when Senkou A is below Senkou B, the cloud is red (bearish).

**Chikou Span** (lagging span): the current close, plotted 26 periods *in the past*. This backward-looking line is the only one not forward-projected. It creates a visual confirmation mechanism: if Chikou closes above price (i.e., the line is above the candles), it confirms an uptrend; if Chikou falls below price, it confirms a downtrend. A Chikou that flattens or reverses predicts a potential trend change.

## Signal generation and trade mechanics

A basic Ichimoku signal fires when price crosses a line. In an uptrend, price above the cloud signals a buy signal (confirmed if Tenkan is above Kijun and Chikou is above price). A trader enters long at the close of that candle or sets a buy stop above the cloud's top edge. The Kijun line becomes the first stop loss; if price closes below Kijun, the signal is negated.

In a downtrend, the inverse applies: price below the cloud with Tenkan below Kijun signals a short entry; the Kijun becomes the stop loss.

The strength of the signal depends on how thick the cloud is. A thin cloud means Senkou A and Senkou B are nearly touching—tight consensus on trend direction and strong support/resistance. A thick cloud suggests disagreement between short-term and long-term momentum and weaker signal reliability. Traders often skip trades when the cloud is very thick or when price is within it, waiting instead for a clearer signal.

## Momentum and trend confirmation

The Ichimoku framework treats momentum and trend as distinct. Price can be in a strong uptrend but with weak momentum (Tenkan below Kijun). This divergence suggests fatigue; a pullback may be imminent, or the trend may be rolling over. Conversely, Tenkan can cross above Kijun while price remains in a downtrend—early warning that momentum is shifting and a reversal is brewing.

Professional traders use this layering to refine entries. They might wait for price to remain above the cloud for at least 3–5 candles (confirming trend) and for Tenkan to rise above Kijun (confirming momentum) before entering a long position. This dual confirmation reduces false entries.

The Chikou Span, lagging by definition, is used differently. Since it reflects past price relative to current price, traders watch it as a leading indicator *in reverse*: where Chikou is heading tells you where price will be. If Chikou is rising and approaching price from below, price is likely to continue higher (because the lagging line is "catching up"). If Chikou is falling and moving away from price, weakness is building.

## Advantages and limitations

Ichimoku's greatest strength is its all-in-one design. Traders don't need to overlay multiple indicators; support, resistance, momentum, and trend are all visible in one glance. It is also entirely mechanical—no subjective parameterization—and the fixed periods (9, 26, 52) have been tested across thousands of assets and decades.

The framework performs exceptionally well on 4-hour and daily timeframes. On these larger charts, the cloud smooths out noise and becomes a reliable boundary between bull and bear regimes.

However, Ichimoku breaks down on very short timeframes. On a 1-minute chart, the cloud is so jagged and the signals so frequent that many are false. Ichimoku is also a trend-following system; it excels in strong trends but can whipsaw in choppy, range-bound markets. A trader who buys every time price touches the cloud will suffer drawdowns during sideways trading. The forward-projection of Senkou A and B, while useful, also means the indicator lags real price discovery; by the time price breaks out of the cloud, the move may already be partially priced in.

Finally, Ichimoku requires discipline. New traders often over-trade every signal, treating every Tenkan-Kijun cross as a certain entry. Professional traders use Ichimoku to identify *zones* of high-probability trading, not automatic trades, and they combine it with price action, volume confirmation, and broader market context.

## Evolution in modern markets

Ichimoku was designed for the Japanese equity markets in the 1960s and has since spread globally. Crypto traders, forex traders, and equity swing traders across markets use it. However, some argue that modern electronic markets—with algorithmic trading, 24/7 sessions, and enormous intraday volatility—have changed the underlying dynamics Ichimoku exploits. A 26-period lag that was meaningful in slower markets may be less useful in today's fast-moving environments.

That said, the framework's flexibility allows for period adjustments. Traders on very short timeframes sometimes use Ichimoku with 5-period, 10-period, and 20-period averages instead of the traditional 9-26-52. This "faster" Ichimoku retains the structure but reacts quicker, though at the cost of more noise.

## See also

<div class="wiki-seealso">

### Closely related

- [Dow theory](/dow-theory/) — foundational principles of trend identification and multi-asset confirmation
- Technical analysis — interpreting price and volume to forecast direction
- Support and resistance — price levels where supply and demand concentrate
- [Heikin-ashi chart](/heikin-ashi-chart/) — smoothed candlestick display that filters short-term noise
- [Moving average](/moving-average/) — lagging indicator that averages prices over time to show trend

### Wider context

- [Price discovery](/price-discovery/) — mechanism by which supply and demand converge on fair value
- [Momentum](/momentum-investing/) — investing based on recent outperformance or price trends
- Swing trading — holding trades over days or weeks based on technical signals
- [Volatility](/volatility-smile/) — degree of price fluctuation; high volatility increases Ichimoku whipsaws

</div>

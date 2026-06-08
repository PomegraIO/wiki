---
title: "Bollinger Bands"
description: "A volatility envelope around a moving average that tightens in low-volatility periods and widens during high volatility, marking support and resistance dynamically."
keywords:
  - Bollinger Bands
  - volatility bands
  - standard deviation envelope
  - trend channels
  - mean reversion
  - volatility indicator
image: "/svg/technical-analysis.svg"
---

*A **Bollinger Band** is a pair of dynamic envelopes that sit a fixed number of [standard deviations](/price-to-sales-ratio/) above and below a moving average. As volatility rises, the bands widen; when volatility falls, they contract. Traders use the bands as adaptive support and resistance levels, and when price touches an outer band, it often signals a potential reversal—making Bollinger Bands one of the most versatile trend-channel tools in technical analysis.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bollinger Bands — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Volatility-adaptive trend channels built from moving-average deviations.</div>

|   |   |
|---|---|
| **What it is** | Upper and lower bands positioned 2 standard deviations from a 20-period moving average |
| **Core formula** | Band = Moving Average ± (2 × Standard Deviation of price) |
| **Default settings** | 20-period MA, 2 standard deviations |
| **Strengths** | Adapts to changing volatility, clear visual channels, multiple trade signals |
| **Weaknesses** | Whipsaws in strong trends, lag-based, does not predict moves |
| **Named after** | John Bollinger, who popularized the tool in the 1980s |

</aside>

## Why standard deviations capture volatility better than fixed price bands

A fixed-width price band (e.g., "mark support 5 points below the MA") assumes markets behave consistently. They do not. During calm, low-volatility periods, price might never touch a 5-point band; the band sits uselessly wide. During panic selling, a 5-point band can be pierced dozens of times in a day, rendering it meaningless as a reversal signal.

Bollinger Bands solve this by using standard deviation—a measure of how far price typically strays from the [moving average](/exponential-moving-average/). In calm markets, standard deviation shrinks, and the bands tighten. In turbulent markets, standard deviation balloons, and the bands widen automatically. The bands thus become a faithful mirror of market behaviour, rescaling themselves to match the regime.

The default Bollinger Band calculation uses a 20-period simple moving average and plots the upper band two standard deviations above it, and the lower band two standard deviations below. Historically, about 95% of all price bars fall within two standard deviations of the mean. This means price touching the outer bands is genuinely rare—which makes it genuinely interesting to traders.

## The volatility squeeze and mean reversion

One of the most potent Bollinger Band signals is the "squeeze"—a period when the bands collapse inward because volatility has evaporated. Traders read a squeeze as a charge building. Price is coiling, preparing for a directional breakout. The narrower the bands, the sharper the expected move.

When the squeeze breaks, price typically bursts through one of the bands with conviction. Pairs traders and mean-reversion specialists watch for squeezes, then position ahead of the expected volatility spike. They expect price to reverse sharply once it reaches the expanded outer band—a classic mean-reversion play.

Conversely, traders sometimes fade the breakout from a squeeze. Price might burst through the outer band on low-conviction volume, only to snap back to the moving average. This is where the bands shine as dynamic support/resistance: they adapt to the volatility regime, so they're more likely to hold during mean-reversion periods than a fixed price level.

## Bollinger Bands as trend-channel markers

In a healthy [uptrend](/bull-market/), price walks along the upper band like a highway guardrail, occasionally touching or slightly exceeding it, then backing off toward the moving average. The [exponential moving average](/exponential-moving-average/) in the middle acts as a dynamic support floor. A trader holding a long position can ride the trend as long as price stays above the moving average and the upper band remains stable.

When price touches the lower band during an uptrend, it often represents a minor pullback within a larger move. Aggressive traders view this as a buy-the-dip opportunity. Conservative traders use the lower-band touch as a stop-loss trigger, exiting if the MA is breached downward.

Conversely, in a downtrend, price hugs the lower band, and the moving average acts as dynamic resistance. A trader holding a short position watches for price to stay below the MA and touch the lower band repeatedly. A touch of the upper band signals a minor bounce; a breach above the MA warns that the downtrend is weakening.

## The squeeze as a volatility predictor

Financial markets exhibit volatility clustering: calm periods are followed by volatile periods, and vice versa. Bollinger Bands capture this implicitly. A very narrow band (a squeeze) statistically precedes an expansion. Traders can quantify the squeeze by measuring the percentage distance between the bands, then acting when that metric falls below a historical threshold.

Some traders trade the squeeze and expand mechanically. They buy when a squeeze is detected, holding until the bands expand significantly; they sell when bands contract to another squeeze threshold. This mean-reversion logic has shown modest edge in ranging markets, though it fails dramatically during sustained trending moves where price just keeps accelerating through the outer bands.

## Mixing Bollinger Bands with other indicators

Stand-alone, Bollinger Bands are vulnerable to whipsaws. Price can touch an outer band multiple times in quick succession, generating false reversal signals. Professional traders filter these signals by combining bands with momentum indicators like RSI or MACD, or by requiring bands to show specific geometric patterns (bands should widen for two or more bars, not just once).

Another approach: use [exponential moving averages](/exponential-moving-average/) instead of the default simple moving average. A 20-period EMA is more responsive to recent price, and bands around an EMA tighten and expand faster, which suits intraday traders who want quicker signals.

A three-band setup (bands at 1, 2, and 3 standard deviations) offers more granularity. Price touching the middle band (1 std dev) might signal a minor reversal; touching the outer band (2 std dev) is more significant; touching the extreme (3 std dev) is a shock. This layering reduces whipsaws for discretionary traders willing to use judgment.

## When Bollinger Bands fail

In a strong, one-directional trend, price can ride the outer band for weeks without ever reverting to the moving average. Traders expecting mean reversion get stopped out. The bands are working perfectly—they're expanding to match the high volatility of the trend—but they're not signalling reversals because the trend is still in force.

Similarly, during a gap-open after overnight news, price can jump beyond the bands without ever trading through them in real time. The bands adjust in the next bar, but the trader is already caught off guard.

The tool also assumes a normal distribution of returns, which is violated during market crashes and liquidity events. These events, though rare, are precisely when traders most need their tools to work—and Bollinger Bands, like most volatility measures, can fail spectacularly in extreme moves.

## Customising band width for your timeframe

The standard 20/2 (20-period MA, 2 standard deviations) works well for daily and weekly charts where you're tracking intermediate trends. For intraday 5-minute or 15-minute charts, traders often reduce the period to 10 or 12, keeping the 2 standard-deviation width. For longer monthly or quarterly trends, extending to a 50-period MA can make sense.

The 2 standard-deviation width is nearly universal because it captures about 95% of normal price movement. Tightening to 1 standard deviation makes the bands more sensitive (they hit more often, generating more signals but also more false ones). Widening to 3 standard deviations makes them almost never hit, so they're used mainly as extreme-move markers rather than tactical trade signals.

## See also

<div class="wiki-seealso">

### Closely related

- [Exponential Moving Average](/exponential-moving-average/) — The moving-average core around which Bollinger Bands are constructed
- [Parabolic SAR](/parabolic-sar/) — Another tool for trailing stops and trend exhaustion within established trends
- [Moving Average Crossover](/moving-average-crossover/) — A complementary trend-entry signal that can be validated by band position
- [Volatility Smile](/volatility-smile/) — The broader concept of volatility clustering that Bollinger Bands exploit

### Wider context

- [Market Timing](/market-timing/) — The goal of entering and exiting trades at optimal moments
- [Mean Reversion](/bull-market/) — The assumption underlying Bollinger Band mean-reversion trades
- [Price Discovery](/price-discovery/) — The underlying mechanism that bands track
- [Risk Management](/concentration-risk/) — Using bands as dynamic stop-loss levels

</div>

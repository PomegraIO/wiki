---
title: "Force Index"
description: "An indicator that combines price movement and trading volume to measure the strength of buying and selling pressure in a market."
keywords:
  - force index indicator
  - volume-based momentum
  - elder force index
  - price volume pressure
  - buying selling strength
image: "/svg/technical-analysis.svg"
---

*The **Force Index** is a technical indicator that fuses price change with trading volume to quantify the intensity of buying or selling pressure. Developed by Alexander Elder, it isolates volume spikes that coincide with meaningful price moves, filtering out volume that merely marks time. Traders use it to confirm momentum shifts and spot divergences between price and underlying buyer-seller conviction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Force Index — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">An Elder indicator that weighs volume by price momentum.</div>

|   |   |
|---|---|
| **What it is** | A momentum oscillator combining [price change](/stock/) and [volume](/volume-price-trend/) into a single force reading |
| **Created by** | Alexander Elder, 1986 |
| **Also called** | Elder Force Index, EFI |
| **Calculation** | Raw: (Close – Prior Close) × Volume; typically smoothed with a moving average |
| **Interpretation** | Positive force = buyer pressure; negative = seller pressure; divergence signals weakening moves |
| **Time horizon** | Intraday to swing trading |

</aside>

## The core idea: volume with direction

The Force Index answers a question traditional [volume](/volume-price-trend/) cannot: *which moves have real conviction behind them?* A million shares traded in a flat day means almost nothing. A million shares traded alongside a sharp price surge means everything. Elder's insight was simple but powerful—multiply volume by the magnitude of the price change, then let the sign (positive or negative) tell you whether buyers or sellers won.

The raw formula is straightforward:

Raw Force = (Close – Previous Close) × Volume

A close higher than yesterday's yields a positive force; a lower close yields a negative force. Large price jumps generate large force figures, small nudges generate small ones. This elegantly captures the trader's intuition: volume packed into a decisive move signals conviction, while volume spread across a dull session signals nothing.

## Smoothing the signal

Most traders apply a moving average to raw Force Index values—typically 13 periods for short-term moves or 50 periods for longer trends. Smoothing removes day-to-day noise while preserving the underlying direction and magnitude of buying or selling pressure. This turns a jagged line into a readable oscillator that oscillates above and below zero, with positive peaks indicating strong bullish phases and negative troughs indicating strong bearish ones.

The crossover of Force Index above or below zero, or the crossing of its moving average, often signals a shift in momentum direction. A rising Force line accompanied by a rising price confirms the move has fuel. A rising price paired with a *falling* Force line suggests the buyer pressure is evaporating—a classic divergence warning that the move is running out of steam.

## Spotting buyer and seller exhaustion

Force Index excels at revealing when a [bear market](/bear-market/) or [bull market](/bull-market/) rally lacks real conviction. Picture a stock bouncing upward on heavy volume, then continuing upward on light volume as Force Index rolls over. The price is climbing, but the sellers are stepping back, not the buyers are pushing forward. This divergence—higher price, weaker force—often precedes a pullback or reversal.

Conversely, a sharp decline on falling Force Index can signal capitulation is near. Sellers have sold all they intend to; volume dries up, and the downward force collapses toward zero. Many traders read this as a potential bottom, a moment when despair has subsided and conviction to keep selling has vanished.

## Strengths and real limitations

Force Index performs well in directional, trending markets where volume spikes tend to align with real momentum. Stocks and futures with clear volume patterns often produce readable Force signals, and the indicator's simplicity makes it easy to spot divergences at a glance.

However, Force Index struggles in choppy, range-bound markets where volume is abundant but price merely oscillates. It also has no inherent ability to distinguish between institutional accumulation and retail panic, both of which can generate large forces in opposite directions. And it relies entirely on closing price—it ignores intraday movement, which occasionally masks real momentum. Like any single indicator, it is most useful when combined with [price action](/price-discovery/), trend structure, and other volume measures such as [Volume Price Trend](/volume-price-trend/).

## Practical use in trading

Swing traders often watch for Force Index divergences as early warning signs of a turn. If a stock rallies to new highs but Force Index lags, the move may be near its end. Day traders sometimes use raw (unsmoothed) Force Index to spot whether volume spikes are supporting the current price direction or fighting it. Options traders use it to gauge whether implied moves have real volume backing or are merely theoretical.

The indicator also works as a [divergence](/beta/) confirmation tool. When price makes a higher high but Force Index makes a lower high, contrarian traders often bet on a reversal. The inverse—a lower price low paired with a higher Force Index low—often signals the bottom of a pullback and the resumption of the uptrend.

## Adjusting the lookback period

The choice between 13 and 50 periods is not rigid. Shorter periods (5–13 bars) capture rapid momentum swings useful for day traders and scalpers. Longer periods (50–200 bars) smooth out daily chop and highlight sustained buyer or seller dominance over weeks. Some traders layer multiple Force Index moving averages—a fast 13-period and a slow 50-period—to distinguish quick reversals from major trend shifts.

## See also

<div class="wiki-seealso">

### Closely related

- [Volume Price Trend](/volume-price-trend/) — cumulative indicator that weights volume by percentage price change
- [Klinger Oscillator](/klinger-oscillator/) — long-term volume flow measure separating accumulation from distribution
- [Tick Volume](/tick-volume/) — trade count proxy for markets without true volume data
- [Beta](/beta/) — measure of price volatility relative to a benchmark

### Wider context

- [Stock](/stock/) — equity share traded on an exchange
- [Price Discovery](/price-discovery/) — process through which market price is established by supply and demand
- [Bull Market](/bull-market/) — extended period of rising prices and investor optimism
- [Bear Market](/bear-market/) — extended period of falling prices and risk aversion

</div>

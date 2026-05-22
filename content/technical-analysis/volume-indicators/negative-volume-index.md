---
title: "Negative Volume Index"
description: "Technical indicator measuring price movement on declining volume days, contrasting with positive volume moves."
keywords:
  - negative volume index
  - nvi indicator
  - volume-price analysis
  - technical analysis
---

*The **Negative Volume Index** (NVI) is a [technical indicator](/wiki/technical-analysis/) tracking cumulative price changes *on days of falling [volume](/wiki/volume-profile-support/)*. The premise: when [volume](/wiki/volume-profile-support/) drops, smart money is active; informed traders sell into weak volume. Rising prices on low volume are suspect; falling prices on low volume signal hidden strength. The NVI isolates "smart money" behavior from crowd noise.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Calculation** | Cumulative sum of price change, counted only on declining-volume days |
| **Interpretation** | Rising NVI = strength on low volume (smart money buying) |
| **Interpretation** | Falling NVI = weakness on low volume (smart money selling) |
| **Typical lookback** | 255-day moving average (one trading year) |
| **Usage** | Confirmation indicator; rarely standalone |
| **Inventor** | Paul Dysart, circa 1936 |
| **Popularity** | Low; less common than [RSI](/wiki/rsi-relative-strength/) or [MACD](/wiki/macd-indicator/) |

</aside>

## The intuition behind NVI

The NVI rests on a specific behavioral premise: retail traders and noise traders dominate high-volume days. Informed traders (institutions, professionals) operate efficiently—they accumulate quietly on light volume and dump on volume spikes when they have conviction. Thus, price movement on *low* volume signals true conviction; movement on *high* volume is often whipsaw.

Example:
- **Day 1**: Stock rises 2%, volume drops 20%. The NVI increments by the 2% rise. Interpretation: smart money buying into weak demand.
- **Day 2**: Stock falls 1%, volume surges 50%. The NVI is unchanged (only low-volume days count). Interpretation: panic selling on volume; less meaningful.

The cumulative NVI filters out noise and emphasizes conviction moves.

## Calculation mechanics

The Negative Volume Index is calculated as:

```
If Volume(today) < Volume(yesterday):
    NVI(today) = NVI(yesterday) + [Price(today) - Price(yesterday)] / Price(yesterday)
Else:
    NVI(today) = NVI(today-1)  // unchanged
```

This creates a running tally of percentage changes on down-volume days only. The index is rarely used in raw form; traders smooth it with a 255-day [moving average](/wiki/trend-following/) and watch for the index to rise above or fall below the moving average.

## Interpretation and signals

**Bullish NVI signal**: The NVI rises above its 255-day moving average. Interpretation: prices are rising on low volume, indicating smart money is accumulating ahead of broader awareness.

**Bearish NVI signal**: The NVI falls below its 255-day moving average. Interpretation: prices are falling on low volume, suggesting insiders are exiting before public panic.

NVI divergences are considered powerful. If price is at new highs but NVI is at new lows, the indicator suggests the rally is built on low-conviction volume (noise), not smart money accumulation.

## The companion: Positive Volume Index

The **Positive Volume Index** (PVI) does the opposite: it tracks price changes on *rising* volume days. The two indices are often used together:

- **NVI rising above its average + PVI above its average**: Strong bull signal (accumulation on both low and high volume).
- **NVI above, PVI below**: Caution; rally may be driven by informed buying but with weak follow-through from the crowd.
- **Both declining**: Clear bearish signal.

Practitioners sometimes use the ratio NVI/PVI to gauge balance between smart and noise trading.

## Historical context

Paul Dysart developed the NVI in the 1930s as part of broader stock-market analysis. It was popularized in Norman Fosback's "Stock Market Logic" (1978), which touted NVI's forecasting power for stock [returns](/wiki/total-return-index/). Academic validation has been weak; the indicator predicts future returns only slightly better than chance.

Why the gap between anecdotal success and academic finding? Selection bias: traders remember the times NVI worked and forget the misses. Also, the indicator is inherently lagging—it's a [confirmation](/wiki/confirmation-bias/) tool, not a leading signal.

## Practical limitations

1. **Lookback sensitivity**: The choice of 255-day average is arbitrary. Different smoothing windows yield different signals. Backtesting across windows introduces [look-ahead bias](/wiki/backtesting-bias/).

2. **Definition of "low volume"**: What counts as down volume? Is yesterday's volume the right benchmark? How do you handle seasonal volume changes? The indicator is sensitive to these choices.

3. **Index vs. individual stocks**: NVI works better on broad indices (SPY, QQQ) where volume patterns are stable. On individual stocks, idiosyncratic trading (lockups, offerings, block trades) distort volume.

4. **Lagging nature**: The NVI is a cumulative indicator, meaning it reflects history. A signal that NVI is rising above its 255-day average tells you smart money *has been* accumulating, not necessarily that they *will continue* to.

5. **Non-predictive in strong trends**: In strong [bull](/wiki/bull-market/) or [bear](/wiki/bear-market/) markets, the NVI often stays on one side of its average throughout, offering little actionable signal.

## Modern usage and variants

Modern [technical analysts](/wiki/technical-analysis/) rarely rely on NVI as a primary indicator. It's mentioned in some trading education materials but is overshadowed by [momentum indicators](/wiki/momentum-investing/) like [RSI](/wiki/rsi-relative-strength/), [MACD](/wiki/macd-indicator/), and [stochastic oscillators](/wiki/stochastic-oscillator/).

Some quantitative funds have experimented with variants:
- **Volume-weighted price changes**: Instead of equal weighting, scaling price changes by volume magnitude.
- **Entropy-based volume filters**: Using information theory to identify "intelligent" vs. "noise" volume.

These modern variants retain the intuition (low volume = smart money) but adapt to contemporary market structure (algorithmic trading, fragmentation, dark pools).

## When NVI might work

The indicator may have edge in:
- **Early-stage reversals**: A stock in downtrend with NVI persistently rising could signal accumulation before public recognition.
- **Institutional trading patterns**: In less liquid names, institution order logic might create the volume-price patterns NVI captures.
- **Regime shift detection**: Transition from noise-driven to informed-trader dominance might show in NVI.

But these edges are narrow and require rigorous [backtesting](/wiki/model-risk/) and [risk management](/wiki/operational-risk/).

<div class="wiki-seealso">

### Closely related
- [Positive volume index](/wiki/positive-volume-index/) — The complementary indicator
- [On-balance volume](/wiki/obv-on-balance-volume/) — Alternative volume-price indicator
- [Volume profile](/wiki/volume-profile-support/) — Volume distribution by price level
- [Technical analysis](/wiki/technical-analysis/) — Broader framework for NVI
- [Momentum investing](/wiki/momentum-investing/) — Strategy sometimes enhanced by NVI

### Wider context
- [Price discovery](/wiki/price-discovery/) — NVI attempt to filter true price discovery
- [Herding investors](/wiki/herding-investors/) — Behavioral motivation for NVI
- [Crowded trade](/wiki/crowded-trade/) — High-volume crowd behavior NVI tries to identify
- [Market microstructure](/wiki/bid-ask-spread/) — Explains volume-price relationships
- [RSI relative strength](/wiki/rsi-relative-strength/) — More common momentum indicator

</div>

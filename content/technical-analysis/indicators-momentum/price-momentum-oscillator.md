---
title: "Price Momentum Oscillator"
description: "A smoothed rate-of-change indicator used to rank relative momentum across sectors, assets, and time periods."
keywords:
  - momentum oscillator
  - rate of change
  - sector rotation
  - intermarket analysis
  - technical indicator
  - trend confirmation
image: "/svg/technical-analysis.svg"
---

*The **Price Momentum Oscillator** (PMO) is a smoothed derivative of price rate of change, designed to isolate momentum shifts while filtering out noise. It ranks assets by relative strength, making it especially useful for sector rotation and comparative momentum analysis across markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Price Momentum Oscillator — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">A two-stage smoothed momentum measure that clarifies comparative strength without false signals.</div>

|   |   |
|---|---|
| **What it is** | A momentum [indicator](/stock-market/) derived from double exponential smoothing of price rate of change |
| **Also called** | PMO, momentum oscillator |
| **Primary use** | Ranking relative momentum, sector comparison, trade entry/exit signals |
| **Formula basis** | 35-day EMA of 12-day ROC, then 35-day EMA of that result, then multiplied by 10 |
| **Signal line** | Typically a 20-day EMA of the PMO itself |
| **Overbought/oversold** | Relative to historical range; no fixed levels |

</aside>

## The smoothing advantage over raw rate of change

Most traders know [rate of change](/stock-market/) — the simple percentage shift in price over N periods — but it jumps wildly. The PMO applies two layers of exponential moving averages to the 12-day rate of change, creating a waveform that catches direction without whipsaws. This two-stage smoothing is its defining trait: the first EMA kills day-to-day noise, and the second EMA stretches the signal, so real momentum shifts stand out. The multiplication by 10 is a scaling convention that makes the numbers easier to read without changing the shape or meaning.

## Reading positive and negative divergence

The most actionable PMO pattern is divergence — when the price makes a new high but the PMO does not. If a stock rallies to a fresh peak yet the oscillator stays flat or drops, momentum is failing. The crowd has cheered the price up, but fewer traders are actively pushing it. This mismatch often precedes a reversal. Conversely, a new low in price combined with a rising PMO suggests sellers are exhausted; the price decline is slowing even as absolute levels touch new bottoms.

## Sector and intermarket rotation workflows

Because the PMO is relative and not absolute, it excels at comparing strength across a peer group. Calculate the PMO for each stock in an industry, or each sector [ETF](/etf/), and rank them. The ones with PMOs near peaks are the leaders; those with falling PMO curves are lagging. A portfolio manager rotating between sectors — moving from technology into energy, for instance — can use PMO to confirm which name within energy has the strongest recent momentum. Unlike binary buy-or-sell signals, the PMO hands you a ranking: sector A's PMO is +8, sector B's is +3, sector C's is −2. Deploy capital accordingly.

## Signal line crosses as entry and exit cues

The PMO is often paired with a 20-day signal line (another EMA, calculated from the PMO itself). When the PMO crosses above its signal line, momentum is accelerating; when it drops below, momentum is fading. These crosses work best in trending markets and tend to lag in choppy, range-bound action. A PMO cross above the signal line in a stock already showing price strength can be a low-risk entry; a cross below in a weakening trend can prompt an exit before larger losses develop. The signal-line cross is not a predictor; it is a confirmation of momentum shift *in progress*.

## Why comparative analysis beats absolute levels

The PMO has no fixed overbought or oversold threshold — no magical level at which you must sell. Instead, context matters. A PMO of 6 might be extreme for one stock but tame for another. This is why the PMO shines in relative frameworks: you compare today's PMO reading to its own 52-week range, or you compare PMO across a basket of peers. A stock whose PMO is at its 90th percentile versus its five-year history is running hotter than one at its 50th percentile, even if both print the same absolute number.

## Limitations and the risk of smoothing lag

The downside of all that smoothing is lag. By the time the PMO fully registers a momentum shift, the move may already be half done. In a sharp reversal, the PMO will still be rising even as the price has begun to fall. This is the eternal trade-off in technical analysis: smoothing removes noise but delays signal. Traders using the PMO typically combine it with price action cues — support/resistance, [candlestick](/stock-market/) patterns, or volume — to catch turns earlier. Relying on PMO alone in fast markets can put you behind the move.

## See also

<div class="wiki-seealso">

### Closely related

- [Know Sure Thing Oscillator](/know-sure-thing-kst/) — A weighted momentum composite of four smoothed rate-of-change periods
- [Fisher Transform Indicator](/fisher-transform-indicator/) — Converts price into a Gaussian distribution to clarify turning points
- [Market-Making](/market-maker-trading/) — Understanding the dealers who provide liquidity and set bid-ask spreads
- [Factor Investing](/factor-investing/) — Systematic allocation to characteristics like momentum and value

### Wider context

- [Technical Analysis](/stock-market/) — Pattern recognition and indicator-based price prediction
- [Sector Rotation](/sector-rotation/) — Shifting portfolio weight between industries based on business cycle stage
- [Volatility Smile](/volatility-smile/) — How implied volatility varies across strike prices and time horizons
- [Value Investing](/value-investing/) — Long-term stock selection based on intrinsic value metrics
- [Alpha](/alpha/) — Excess return beyond what [market risk](/market-risk/) alone predicts

</div>

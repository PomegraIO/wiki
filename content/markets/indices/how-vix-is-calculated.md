---
title: "How the VIX Is Calculated"
description: "The CBOE formula that derives 30-day volatility expectations from S&P 500 options prices, with worked examples of what VIX readings mean."
keywords:
  - how is the vix calculated
  - vix calculation formula
  - volatility index methodology
  - cboe vix
---

*The **VIX** (Volatility Index) measures expected 30-day volatility of the S&P 500, calculated by the Chicago Board Options Exchange using a formula that averages implied volatility across both call and put options at multiple strike prices. A given VIX reading translates directly to an annualized percentage move; a VIX of 20 implies the market expects the S&P 500 to move roughly ±1.15% over the next 30 days.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VIX Calculation — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A weighted average of implied volatility from S&P 500 options, updated every 15 seconds during market hours.</div>

|   |   |
|---|---|
| **Underlying** | S&P 500 index options (weekly and monthly expirations) |
| **Time horizon** | 30 calendar days (the calculation targets constant expiry) |
| **Input data** | Bid-ask midpoints of near- and next-term option prices |
| **Output** | Index level 0–100+, updated continuously |
| **Interpretation** | Annualized volatility ÷ √12 = expected 30-day move as % |
| **Market use** | Fear gauge, hedge tool, inverse correlation to equities |

</aside>

## Why 30-day volatility matters

The VIX doesn't measure historical volatility—what the market *has* done—but *implied* volatility: what traders expect *will* happen. When equity investors fear a sharp drawdown, they buy protective puts, driving put prices up and simultaneously lifting the options market's volatility premia. The VIX crystallizes this fear into a single number.

Thirty days was chosen because it sits between "too short to be meaningful" and "too long to be predictive." Weekly options are too noisy; quarterly or annual volatility expectations are stale. A rolling 30-day window gives real-time signal of near-term market stress.

## The CBOE formula: building blocks

The calculation has three layers.

**First, isolate implied volatility from each option.** The CBOE takes the bid-ask spread at each strike price (for both calls and puts) on the near-term (typically 8–37 days to expiry) and next-term (29–60 days) S&P 500 options series. It extracts the [implied-volatility](/implied-volatility/) for each using the Black–Scholes inversion—no closed form exists, so the CBOE uses numerical methods to back out the volatility that makes observed price equal predicted price.

**Second, select strikes and weight them.** The formula doesn't use *all* strikes. Instead, it:
- Picks out-of-the-money puts (strike below current S&P 500 price) and calls (strike above).
- Removes any where the option bid is zero (too illiquid).
- Averages the implied volatility of the put and call at each strike (smoothing noise).
- Weights each strike by 1/(strike²), favoring near-the-money options and down-weighting deep out-of-the-money tail strikes (which are thin and hard to price).

This weighting is the mathematical heart of the formula: it pulls real, liquid signal from the strikes traders actually use.

**Third, interpolate to 30 days exactly.** Markets trade discrete expirations (8 days out, 15 days out, 37 days out, etc.). The CBOE never has a contract that's *exactly* 30 days to go. So it:
- Computes a volatility number from near-term options.
- Computes a separate volatility number from next-term options.
- Interpolates linearly to lock in a 30-day timeframe.

The formula is designed so that as the near-term options approach expiry, the calculation seamlessly rotates to the next contract, producing a smooth continuous series.

## A worked example

Suppose the S&P 500 is at 5,000, near-term options expire in 12 days, and next-term options expire in 40 days.

You gather implied volatility quotes at strikes around 5,000: calls at 5,010, 5,020, 5,030 (and puts at 4,990, 4,980, 4,970). Each has a bid and ask; you take the midpoint. You invert each price to get implied volatility—say, 18% at the 5,010 call, 17.5% at the 5,020 call, and so on.

You weight them by 1/(strike²): the 5,010 call gets weight 1/5010² = 0.0000000397, slightly more than the 5,020 call. Then you average puts and calls at the same strike to get a single volatility per strike, and sum the weighted volatilities to get a near-term index number.

Repeat for next-term options (getting, say, 16.5% as the next-term vol).

Now interpolate: you want exactly 30 days. Near-term is 12 days, next-term is 40 days. The 30-day contract is (30 − 12)/(40 − 12) = 18/28 ≈ 64% of the way from near to next. So:

VIX ≈ (0.36 × 17.8%) + (0.64 × 16.5%) ≈ 16.9%

Annualize by multiplying by √(365/30) ≈ 3.48, and multiply by 100 for index points. That's your VIX level.

(The actual CBOE formula is more granular, but this captures the intuition.)

## What the VIX number really means

A VIX of 20 does *not* mean "the market will definitely move ±20% in 30 days." It means: "Based on options prices, traders expect the S&P 500's *annualized* volatility to be 20%."

To get the 30-day expected move:

**30-day volatility = VIX / √12**

So VIX 20 → 20 / √12 ≈ 5.77% expected move over 30 days. That's the 1-sigma (68% confidence) range. Most traders read this as "we expect the S&P to move in a roughly ±6% band."

VIX 30 → 30 / √12 ≈ 8.66% (heightened fear).  
VIX 15 → 15 / √12 ≈ 4.33% (subdued expectations).

The VIX rarely sits still. Overnight news, earnings seasons, and central bank moves shift implied volatility minute to minute. The CBOE publishes the VIX continuously during US equity hours.

## Why it matters for investors and traders

The VIX serves three roles:

1. **Fear barometer.** Spikes above 25 usually signal equity market stress; above 40 signals panic. Prolonged lows below 12 suggest complacency.

2. **Hedge cost.** Buying [protective-put](/protective-put/) options (downside insurance) becomes expensive when VIX is high, because implied volatility—the cost of the option—is high. Professional portfolios buy "cheap" insurance when VIX is low.

3. **Inverse correlation signal.** Stocks and the VIX move opposite about 75% of the time. When equities fall sharply, the VIX spikes. This negative correlation makes VIX futures or call options structural hedges for equity exposure.

## Limitations

The VIX is only as good as the options market data feeding it. If options are sparse or bid-ask spreads are wide at certain strikes, the calculation gets noisier. The formula also assumes the current risk environment will persist for 30 days, which fails during sudden regime shifts—the VIX can lag real catastrophic moves by hours.

And because the VIX derives from S&P 500 options specifically, it reflects large-cap US equity volatility, not global markets, credit spreads, or commodity volatility. A spike in Treasury yields might not immediately move the VIX, even if bond traders are panicked.

## See also

<div class="wiki-seealso">

### Closely related

- [Implied Volatility](/implied-volatility/) — the volatility number backed out from an option's price
- [Option](/option/) — the derivative contract whose prices power VIX calculation
- [Historical Volatility](/historical-volatility/) — realized past volatility, distinct from expected forward volatility
- [Protective Put](/protective-put/) — using options to hedge equity risk, which becomes expensive when VIX spikes
- [Volatility Smile](/volatility-smile/) — why implied volatility differs across strikes, complicating the VIX formula

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — strategies for managing portfolio risk
- [Stock Market](/stock-market/) — the underlying asset class and primary volatility risk
- Risk Management — frameworks for measuring and controlling market exposure
- [Market Risk](/market-risk/) — broader category of portfolio drawdown exposure

</div>

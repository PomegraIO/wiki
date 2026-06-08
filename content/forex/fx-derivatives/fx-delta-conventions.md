---
title: "FX Option Delta Conventions"
description: "How spot delta, forward delta, and premium-adjusted delta differ; quoting conventions vary by currency pair and dealer."
keywords:
  - fx option delta
  - spot delta
  - forward delta
  - premium-adjusted delta
  - currency option
image: /svg/forex.svg
---

*FX [delta](/delta/)—the rate of change in an option's price relative to moves in the underlying exchange rate—is quoted in different ways across currency pairs and dealers. Spot delta, forward delta, and premium-adjusted delta each measure slightly different exposures, and misunderstanding which convention a counterparty uses can lead to costly hedging errors.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Option Delta Conventions — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for currency derivatives." />

<div class="wiki-infobox-caption">Same option, three ways to measure directional exposure.</div>

|   |   |
|---|---|
| **Spot delta** | Change in option price per 1 unit move in the spot rate; ignores forward points |
| **Forward delta** | Adjusted for the interest-rate differential between the two currencies |
| **Premium-adjusted delta** | Normalizes for the premium paid, so delta sums to 100% across call and put |
| **Why it matters** | Different conventions can make the same position appear to hedge or expose you differently |
| **Geographic variation** | European and Asian dealers often prefer forward delta; US dealers mix spot and premium-adjusted |
| **Standard pairs** | EUR/USD, GBP/USD typically quoted in spot or forward; emerging-market pairs often premium-adjusted |

</aside>

## The core issue: what moves when the spot rate moves

The simplest [delta](/delta/) is **spot delta**: the number of units of the foreign currency your option position gains or loses per 1 unit move in the spot exchange rate. A call on EUR/USD with spot delta of 0.60 gains approximately €60 for every 1 cent move in the spot rate (assuming small moves and constant [volatility](/historical-volatility/)).

The trouble: the spot rate isn't the only thing that moves. Interest rates in the euro zone and the US differ. If the USD weakens (spot EUR/USD goes up), the EUR–USD interest-rate differential often moves *with* it, and the value of your forward contract changes too. Spot delta ignores this interaction.

## Spot delta: the purest form, but incomplete

Spot delta measures the immediate sensitivity to the spot rate at the current moment. It answers: "If EUR/USD moves from 1.1000 to 1.1001 right now, keeping all else constant, how much do I make or lose?"

**Advantages:**
- Simple to calculate and explain.
- Standard for short-dated, liquid pairs like EUR/USD.

**Disadvantages:**
- Ignores the interest-rate differential that drives the forward rate.
- Two options with the same spot delta but different maturities can hedge very differently in practice.

For example, a 1-year EUR call and a 3-month EUR call, both with spot delta 0.50, behave differently. The longer-dated option embeds more interest-rate sensitivity; its forward delta diverges from spot delta.

## Forward delta: adjusting for carry and interest-rate risk

**Forward delta** replaces the spot rate with the forward rate as the reference. It measures sensitivity to the forward rate, not the spot.

When EUR–USD interest rates differ—say, EUR yields 3.5% and USD yields 4.0%—the forward EUR/USD rate is wider than spot. If you buy EUR forward, you implicitly borrow USD and lend EUR, locking in the interest-rate pick-up or cost. Forward delta captures this.

The relationship:
Forward rate ≈ Spot rate × (1 + USD rate) / (1 + EUR rate)

If USD rates rise, the forward rate falls (EUR becomes less attractive to buy forward). An option's forward delta accounts for this carry effect automatically.

**When to use forward delta:**
- Longer-dated options (6 months or more).
- Pairs with significant interest-rate differentials (emerging-market currencies often).
- Risk management for portfolios that include both spot and forward positions.

A trader hedging a long-dated foreign currency exposure will find forward delta more intuitive, because it reflects the cost of carry—the interest expense (or benefit) of holding the position to maturity.

## Premium-adjusted delta: normalizing across strikes

In some markets, traders quote **premium-adjusted delta** (also called **percentage delta** or **money delta**). Instead of measuring the raw change in option value, it normalizes the delta by the option premium paid.

Example: You buy a EUR call for USD 0.02 per share, with a spot delta of 0.40. The premium-adjusted delta might be quoted as 80. This means: for every 1% the option premium moves, your delta shifts by approximately 80 basis points.

This convention is common in:
- Emerging-market FX options, where premium size varies wildly across strikes.
- Structured note markets, where dealers want to compare hedge ratios across different strikes and tenors on a common scale.
- Options on commodity currencies (AUD, NZD, CAD) where interest-rate carry is economically significant.

**Advantage:** Allows easier comparison of hedge ratios across different strikes.
**Disadvantage:** Less intuitive; requires understanding the underlying premium.

## Geography and market practice

**EUR/USD and GBP/USD** (major pairs, tight spreads): Most dealers quote both spot and forward delta, letting clients choose. The market is liquid enough to support multiple conventions without confusion.

**Emerging currencies** (MXN, BRL, INR, TRY): Often quoted in premium-adjusted or forward delta, because interest-rate differentials are enormous. A 1-year interest-rate gap between Mexico and the US can be 4% or more; spot delta alone is misleading.

**Commodity-linked currencies** (AUD, NZD, CAD): Forward delta dominates, because carry is economically dominant. The forward rate can be materially different from spot, and hedgers care about the full forward exposure.

## Practical reconciliation: reading a term sheet

Suppose a dealer quotes a EUR call as:
- Strike: 1.1000
- Expiry: 1 year
- Spot delta: 0.45
- Forward delta: 0.38

What happened? The interest-rate differential moved the forward rate lower (EUR is costlier to buy forward than the spot rate suggests). The forward delta is lower because the forward strike is further out-of-the-money than it appears from spot alone.

A treasurer hedging a future EUR cash inflow needs to think in forwards. The forward delta tells them: "You are currently long 38% of the notional in the forward market." A trader focusing on current market moves wants the spot delta: "You make or lose 45 cents per million of the EUR move, right now."

Both are correct; they answer different questions.

## Delta conventions and [gamma](/gamma/) scalping

In [gamma scalping](/fx-gamma-scalping/) or dynamic hedging, the choice of delta convention affects rehedging frequency and cost. If you use spot delta to set your hedge ratio but the forward rate moves (due to interest-rate changes), you'll find yourself under- or over-hedged even if the spot is flat.

Many institutional desks use forward delta for rehedging long-dated books, because it more accurately reflects the economic exposure. The extra mental overhead is worth the precision.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the fundamental rate of change; base concept for all FX delta conventions
- [FX Gamma Scalping](/fx-gamma-scalping/) — dynamic rehedging strategy where delta convention choice matters operationally
- [Implied volatility](/implied-volatility/) — also varies by strike and convention; often shown as an "at-the-money" benchmark
- [FX Swaption](/fx-swaption/) — another FX derivative where forward vs. spot matters for pricing
- [Interest rate](/interest-rate/) — drives the forward rate and thus the divergence between spot and forward delta

### Wider context

- [Option](/option/) — the underlying instrument; delta is one of the Greeks
- Greek letters — broader framework of option Greeks; delta is one of five main sensitivities
- [Volatility smile](/volatility-smile/) — why delta varies across strikes
- [Forward contract](/forward-contract/) — introduces the forward rate; non-optional, unlike options

</div>

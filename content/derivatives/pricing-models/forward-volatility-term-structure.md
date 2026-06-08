---
title: "Forward Volatility and the Term Structure of Volatility"
description: "How forward implied volatility is extracted from the volatility term structure to price and hedge options across different time horizons."
keywords:
  - forward volatility
  - term structure of volatility
  - forward implied volatility
  - calendar spreads options
  - volatility bootstrapping
  - options pricing models
---

*The **forward volatility term structure** describes implied volatility rates for future periods, bootstrapped from options prices across different expiration dates. Traders use forward volatility to price calendar spreads, hedge rolling exposures, and understand when the market expects volatility to rise or fall between now and a distant expiration.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Volatility — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and pricing." />

<div class="wiki-infobox-caption">Forward volatility isolates expected volatility in a future window, extracted from quoted option prices.</div>

|   |   |
|---|---|
| **Core idea** | Implied volatility for a future period, derived from the [volatility curve](/yield-curve/) across expiries |
| **How derived** | Bootstrapped from puts and calls at different strikes and dates |
| **Main use** | Pricing [calendar spreads](/option/) and hedging rolling [delta](/delta/) exposures |
| **Key distinction** | Spot IV = volatility priced into today's option; forward IV = volatility priced into a future window |
| **Market signal** | Contango (rising IV curve) signals expected future turbulence; backwardation signals calm ahead |

</aside>

## The volatility term structure in practice

At any given moment, the options market quotes different [implied volatilities](/implied-volatility/) for options expiring in 30 days, 60 days, 90 days, and so on. Collectively, these form a curve called the *volatility term structure*. When volatility is quoted as higher for longer-dated expirations, the curve is in *contango*; when near-term volatility exceeds far-term, it is in *backwardation*.

But the quoted implied volatility for a 90-day option does not directly tell you what volatility will exist between day 30 and day 90. That is where forward volatility comes in. Forward volatility is the *implied volatility for a future period*, isolated mathematically from the term structure. A trader can extract the "60-to-90-day forward volatility" by comparing the two 90-day and 60-day option prices.

For example, if 60-day calls have an implied volatility of 18% and 90-day calls have an implied volatility of 20%, the market is pricing higher volatility in the 60-to-90-day window (the forward window) than in the first 60 days.

## Bootstrapping forward volatility from option prices

The mechanics rely on the variance-additive property of [Black-Scholes](/black-scholes-model/) and similar models. Under these frameworks, the variance (squared volatility) of returns compounds over time. If you know the total variance for 90 days and the total variance for 60 days, you can back out the variance for the 60-to-90-day window and then take its square root to get the forward volatility.

**Simplified example:**

- 60-day implied volatility: 18% → variance = 0.18² × (60/252) ≈ 0.00258
- 90-day implied volatility: 20% → variance = 0.20² × (90/252) ≈ 0.00714

The 60-to-90-day forward variance is the difference:
- Forward variance = 0.00714 − 0.00258 = 0.00456
- Forward volatility = √0.00456 ÷ √(30/252) ≈ 21.4%

This forward volatility of roughly 21.4% is the market's expected volatility *specifically* for the 30-day window between day 60 and day 90. It is typically higher than both the 60-day and 90-day spot implied volatilities when the curve is in contango.

## Calendar spreads and forward volatility pricing

A [calendar spread](/option/) is a position that buys an option expiring in the distant future and sells a nearer-dated option on the same underlying and strike. The [short position](/short-selling/) benefits from time decay, while the long position is hedged against large directional moves. But the payoff from a calendar spread is fundamentally a bet on realized volatility in the forward window.

When a trader sells a 60-day call and buys a 90-day call, she is implicitly short the realized volatility for the 60-to-90-day window. If realized volatility in that window exceeds the forward volatility priced into the spread, the trade will be profitable. Conversely, if realized volatility falls below forward volatility, the trade loses money.

To properly price and hedge such positions, traders use the forward volatility curve instead of spot volatilities. This removes the confounding effect of near-term volatility decay and isolates the actual volatility bet.

## The relationship between spot and forward implied volatility

When the volatility term structure is steep—that is, when long-dated options are priced with much higher IV than short-dated ones—forward volatility is even higher still. This is because the curve compounds: each marginal volatility point for a longer expiration amplifies the forward rate.

Conversely, when the term structure is flat (all expirations priced with similar IV), forward volatility tends to be close to spot volatility. And in a backwardated environment, where near-term expirations have higher IV than far-term ones, forward volatility can actually drop below both the near and far spot levels.

These inversions are not mathematical errors; they reflect the market's conditional expectations. A steeply contangoed curve during a period of calm markets signals that traders expect a potential shock to arrive within the next few months. A flat or backwardated curve during a crash indicates that volatility is expected to decline as the crisis passes.

## Using forward volatility to hedge rolling positions

Asset managers and [hedge funds](/hedge-fund/) often need to maintain a consistent [delta](/delta/) exposure over months or years. Rather than holding a single long-dated option, they may roll a series of shorter-dated positions—selling a 60-day call and buying a 120-day call every 60 days, for instance.

Forward volatility helps them understand the embedded cost of rolling. If the 60-to-120-day forward volatility is historically high relative to recent realized volatility, rolling is expensive—they will be paying a premium to extend the hedge. If forward volatility is low, rolling is cheap. By monitoring forward volatility, managers can decide whether to extend quickly or wait for prices to become more attractive.

## See also

<div class="wiki-seealso">

### Closely related

- [Implied volatility](/implied-volatility/) — the volatility backed out of an option's market price
- [Options](/option/) — calls and puts, and how their value depends on volatility
- [Calendar spreads](/option/) — long-term and short-term options on the same strike, a pure volatility bet
- [Delta](/delta/) — directional sensitivity of an option to moves in the underlying
- [Volatility smile](/volatility-smile/) — how implied volatility varies across strike prices

### Wider context

- [Black-Scholes model](/black-scholes-model/) — foundational equation for option pricing under constant volatility
- [Interest rate swap](/interest-rate-swap/) — another derivative where forward rates matter
- [Yield curve](/yield-curve/) — the fixed-income equivalent of the volatility term structure

</div>

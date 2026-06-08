---
title: "Double No-Touch Option"
description: "A range option that pays a fixed sum only when the underlying stays between two barrier levels throughout the option's entire life."
keywords:
  - binary options
  - range options
  - barrier options
  - exotic derivatives
  - structured products
  - two-sided barriers
image: "/svg/derivatives.svg"
---

*A **double no-touch option** is a [binary option](/option/) that delivers a fixed payoff if the underlying asset remains strictly between two barrier levels (an upper and lower bound) for the entire option life. It is a bet on *range stability*: the buyer profits if the asset avoids violent moves in either direction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Double No-Touch Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A binary range bet: paid for staying between two barriers.</div>

|   |   |
|---|---|
| **What it is** | Binary option paying fixed sum if both barriers are avoided |
| **Barriers** | Upper and lower price levels defined at inception |
| **Payoff condition** | Underlying never touches either barrier through [expiration-date](/expiration-date/) |
| **Payoff amount** | Fixed cash or notional amount |
| **Also called** | Range option, double-barrier option, tunnel option |
| **Common underlying** | Forex pairs, equity indices, commodity futures |
| **Inverse of** | One-touch structure on either barrier |
| **Primary use** | Hedging [volatility](/historical-volatility/) and rangebound expectations |

</aside>

<div class="wiki-hatnote">

For the one-sided equivalent, see [No-Touch Option](/no-touch-option/).

</div>

## The two-barrier logic: contained markets

A double no-touch option reflects the belief that an asset will trade within a band—neither rallying sharply above an upper level nor crashing below a lower floor. A foreign-exchange trader might buy a double no-touch on EUR/USD if the European Central Bank has just signaled stability and the U.S. Federal Reserve is on hold; he expects the pair to trade between 1.08 and 1.12 for the next three months. If the pair stays in that band throughout, he receives a payoff—compensation for being right about contained volatility. If either boundary is touched, the option expires worthless.

This is fundamentally different from buying a straddle (long both [call-option](/call-option/) and [put-option](/put-option/)), which profits from *movement in either direction*. The double no-touch profits from *restraint*. It is a play on low realized [volatility](/historical-volatility/) and/or mean-reverting price behavior.

## Pricing: the high stakes of dual barriers

A double no-touch is generally cheaper than buying two independent [no-touch-option](/no-touch-option/) contracts (one upper, one lower) because the probabilities are not independent—the asset either stays in the band (both barriers avoided) or breaches at least one. The joint probability of avoidance is the product of individual probabilities only if price movements are normally distributed without drift, a simplification rarely true in reality.

The premium depends on:

1. **Width of the band.** A narrow band (1.10–1.11) is expensive to avoid; a wide band (1.00–1.20) is cheap.
2. **[Volatility](/historical-volatility/).** High volatility makes the band hard to respect; low volatility makes it easy to stay within.
3. **Drift or expected trend.** If the asset is expected to trend upward, the upper barrier becomes more likely to be breached, raising the premium.
4. **[Time decay](/time-decay-theta/).** As expiry approaches, the probability of already having breached either barrier rises, so near-term no-touch premiums are higher than far-term ones.

## Selling and the hedger's dilemma

Banks selling double no-touch options face a classic hedging challenge. The seller collects the premium upfront but is short convexity: he profits only if price stays within the narrow band, and loses large amounts if price ventures near either barrier. Unlike a simple [call-option](/call-option/) seller, who can delta-hedge dynamically, the double no-touch seller cannot easily hedge the barrier risk without buying expensive [one-touch-option](/one-touch-option/) insurance or trading at the barriers continuously.

In practice, banks that sell double no-touch structures in [structured-products](/option/) bundled into notes hold them as negative [gamma](/gamma/) positions and manage them through:

- Selling volatility in derivatives markets (short [straddle](/option/) or strangle structures to offset the short-convexity exposure).
- Buying far-out-of-the-money puts and calls as tail-risk insurance.
- Hedging with closely-spaced barrier positions to create a dynamic rebalance.

This hedging cost is why retail double no-touch products, when offered, carry spreads of 200–400 basis points between the bank's bid and offer.

## Range-trading markets and real applications

Double no-touch options thrive in sideways markets where two-way risk is present but a consensus range exists. In commodity markets, a grain trader expecting prices to remain in a harvest-season band might sell short-dated double no-touch calls and puts together. In equity indices during consolidation phases (post-earnings, pre-rate-decision), hedge funds use double no-touch to profit from rangebound trading without taking directional view.

The structure is also common in emerging-market currency overlay strategies. A pension fund holding Brazilian real assets might sell (be short) a double no-touch option on USD/BRL, meaning it wants the real to remain stable within a band—if the real is stable, the fund avoids hedging costs and pockets the option premium; if volatility breaks the range, the fund absorbs the loss but already has currency risk exposure it wanted to manage anyway.

## Relationship to volatility regimes

Double no-touch pricing is exquisitely sensitive to [implied-volatility](/implied-volatility/) surfaces. A sharp rise in realized or expected volatility makes all existing double no-touch positions less valuable—the barriers become more likely to be breached. This creates a useful hedge for traders and funds: if you believe volatility will spike (earnings season, geopolitical shock, rate hike), being short double no-touch options (or long them with the understanding they will lose value) is a volatility bet.

Many volatility indices and [VIX](/option/)-like products show that double no-touch implied volatility often trades richer than individual [strangle](/option/) volatility, reflecting the premium for respecting two boundaries simultaneously.

## Building blocks and structured products

Large institutional structured-product desks use double no-touch options as building blocks for exotic notes. A reverse-convertible note might include a double no-touch coupon enhancement: if a reference index stays within a band, the coupon is 8% instead of 4%. This sells the client the risk that the index breaches the band (coupon drops), but the client is attracted by the higher coupon in calm markets. From the issuer's perspective, the embedded double no-touch option is a profitable carry if realized volatility stays below implied levels.

## Comparison to simpler structures

- **[One-touch-option](/one-touch-option/).** Single barrier, pays if breached. Asymmetric risk.
- **[No-touch-option](/no-touch-option/).** Single barrier, pays if avoided. Suited to one-sided risk.
- **Double no-touch.** Two barriers, pays if both avoided. Suited to rangebound conviction.
- **Straddle.** Combines long call and long put; profits from large moves. Opposite of double no-touch payoff profile.

## See also

<div class="wiki-seealso">

### Closely related

- [No-Touch Option](/no-touch-option/) — single-barrier inverse payoff
- [One-Touch Option](/one-touch-option/) — single-barrier direct payoff
- [Perpetual Option](/perpetual-option/) — range structure without expiry date
- [Binary Option](/option/) — general fixed-payoff class
- [Barrier Option](/option/) — broader family of path-dependent derivatives
- [Straddle](/option/) — opposite payoff: profit from movement

### Wider context

- [Call Option](/call-option/) — one side of the range boundary
- [Put Option](/put-option/) — other side of the range boundary
- [Implied Volatility](/implied-volatility/) — critical to double-barrier pricing
- [Gamma](/gamma/) — hedging challenge for double no-touch sellers
- [Over-the-Counter Market](/over-the-counter-market/) — primary trading venue
- [Structured Products](/option/) — common application arena

</div>

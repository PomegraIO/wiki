---
title: "One-Touch Option"
description: "A binary option that pays a fixed sum if the underlying asset touches a predetermined barrier level at any point before expiration."
keywords:
  - binary options
  - barrier options
  - exotic options
  - touch options
  - structured derivatives
  - payoff barriers
image: "/svg/derivatives.svg"
---

*A **one-touch option** is a [binary option](/option/) with a fixed payoff triggered when the underlying asset reaches or breaches a specified barrier level at any moment before expiry. Unlike standard options that depend on the final price at maturity, a one-touch option cares only whether the asset *ever touches* the barrier during its life.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">One-Touch Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A binary payoff tied to barrier contact, not final price.</div>

|   |   |
|---|---|
| **What it is** | Binary option paying a fixed sum if barrier is touched |
| **Barrier type** | Single predetermined level (above or below spot) |
| **Payoff trigger** | Contact at any point before [expiration-date](/expiration-date/) |
| **Payoff amount** | Typically 100 (or notional) × fixed cash amount |
| **Also called** | Touch option, one-hit option |
| **Common underlying** | Forex, commodities, stock indices |
| **Risk to seller** | Barrier can be breached early in option life |

</aside>

## Why a single barrier matters

A one-touch option's power lies in its simplicity: it pays if a named price level is ever reached, regardless of where the underlying closes. This makes it useful for traders with a strong view on *whether* an asset will move sharply in a direction, but no conviction about final settlement price. A currency trader might buy a one-touch on EUR/USD struck 1.15 if she expects volatility but not necessarily an uptrend at expiry. The upside is leveraged (the fixed payout can exceed the premium paid); the downside is all-or-nothing—miss the barrier by 0.01, and the option expires worthless.

## How the payoff differs from vanilla options

A [call-option](/call-option/) pays max(spot − strike, 0) at maturity. A one-touch option pays either a fixed amount or zero, depending on whether the barrier was ever touched. This distinction is profound. Imagine a stock trading at 100 with a one-touch strike at 110. If the stock rallies to 110.00 on day 5, then falls to 105 by expiry, the one-touch holder receives the full payoff. A vanilla 110 call would expire worthless. Conversely, if the stock touches 110 but then plummets to 50 by settlement, the one-touch still wins.

This path-dependence makes one-touch options cheaper when the barrier is far from the spot price and volatility is low—the barrier may never be reached. As volatility rises, or as the barrier creeps closer to current price, the one-touch premium climbs, sometimes dramatically.

## Pricing and the role of volatility

Valuing a one-touch option requires calculating the probability that the underlying will hit the barrier at least once during the option's life. This is fundamentally a question about the *path* the asset takes, not just its terminal distribution. Under the Black-Scholes framework (or modern [implied-volatility](/implied-volatility/) surfaces), higher volatility increases the odds of touching any given barrier, so one-touch premiums rise sharply with volatility regime.

A key insight: a one-touch struck far out-of-the-money can actually gain value as rates rise, because higher rates increase the drift of the underlying in certain directions (e.g., a positive drift in a spot FX rate). The seller of a one-touch typically hedges by holding a [barrier-option](/option/) portfolio or by delta-hedging dynamically. Early barrier contact can force the seller into large loss positions if hedges are not maintained tightly.

## Counterparty risk and barrier definitions

The [counterparty-risk](/counterparty-risk/) embedded in a one-touch option is often underestimated. If a barrier is struck at a live market level during volatile trading, a split-second spike might trigger the barrier even if the asset never truly "lived" at that level in steady-state markets. Forex platforms and equities exchanges have different rules about intraday tick level confirmation; some require closing-price confirmation, others any intraday touch. This ambiguity can lead to disputes between buyer and seller, especially in over-the-counter (OTC) [forward-contract](/forward-contract/) markets where there is no central exchange to enforce settlement.

## Practical use cases

One-touch options are popular in forex and commodity derivatives markets. A trader expecting a central-bank announcement might buy a one-touch call on a currency pair at a level 2% above spot, betting on a sharp move but uncertain of direction. The fixed payout appeals to risk managers with limited capital: pay a small premium for leverage, cap downside loss at that premium, and profit a multiples return if the barrier is hit.

Agricultural traders use one-touch options on grain and soft commodity prices to hedge inventory risk around harvest seasons. An exporter might buy a no-touch put-analog (a structure paying off if price *stays above* a floor), locking in an attractive downside while keeping upside open. Banks bundle one-touch options into structured notes sold to retail investors, embedding leverage and barrier mechanics into a single instrument.

## Comparison to other exotic structures

One-touch options sit at the simpler end of the exotic [option](/option/) spectrum. A [double-no-touch-option](/double-no-touch-option/) requires the underlying to stay *between* two barriers; a perpetual structure has no expiry. Standard [knockout options](/option/) are path-dependent but pay a vanilla payoff if the knockout is not triggered. One-touch is the purest barrier bet: touch = paid; no touch = zero. This simplicity has made it a building block in structured products and a common tool for directional speculation in volatile markets.

## See also

<div class="wiki-seealso">

### Closely related

- [No-Touch Option](/no-touch-option/) — inverse payoff: paid if barrier is *never* touched
- [Double No-Touch Option](/double-no-touch-option/) — range bet between two barriers
- [Perpetual Option](/perpetual-option/) — touch-triggered structure with no expiry
- [Binary Option](/option/) — fixed payoff contingent on a price event
- [Barrier Option](/option/) — general class of path-dependent derivatives
- [Option Premium](/option-premium/) — cost of entry and the seller's revenue

### Wider context

- [Call Option](/call-option/) — standard right to buy; contrast with touch mechanics
- [Implied Volatility](/implied-volatility/) — drives one-touch pricing
- [Option](/option/) — foundational derivative contract
- [Over-the-Counter Market](/over-the-counter-market/) — primary venue for exotic options
- [Counterparty Risk](/counterparty-risk/) — key concern in OTC touch-option settlement

</div>

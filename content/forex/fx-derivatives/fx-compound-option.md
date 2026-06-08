---
title: "FX Compound Option"
description: "An option giving the holder the right to buy or sell an underlying FX option at a preset strike and premium on a future date."
keywords:
  - compound option
  - option on option
  - fx derivatives
  - exotic options
  - leverage
  - volatility
  - strike price
image: "/svg/forex.svg"
---

*A **FX compound option** is an option written on an underlying FX option, giving the holder the right (but not obligation) to enter into or modify that option at a predetermined future date. The holder pays an initial premium to own the right to decide later whether to exercise the option on the option.*

## Structure and terminology

A compound option has two exercise decisions and two distinct premium payments. The **outer option** is what you buy today; exercising it either enters you into the **inner option** (the underlying FX option) or allows you to modify its terms.

Suppose you buy a "call on a call" on EUR/USD:
- **Outer option**: Call option, strike €100,000, expiry in 3 months, premium €500.
- **Inner option** (if you exercise the outer call): A call on EUR/USD, strike 1.10, expiry in 6 months (3 months after outer expiry).
- **Exercise premium**: You must pay an additional amount (say €1,000) when you exercise the outer option to enter the inner call.

If EUR/USD climbs to 1.15 in month 3, exercising the outer call is valuable—you spend €1,000 to own a call struck at 1.10 with three months to expiration and an additional upside. If EUR/USD falls to 1.05, the outer call expires worthless; you walk away having lost only €500.

## Why they exist: leverage and optionality

Compound options are levers for managing cost and staged conviction. Rather than buying a long-dated FX option outright, you buy a short-dated option on it, deferring the real decision. This two-step structure saves premium on long-dated optionality and lets you reassess conditions after the first leg expires.

A corporate treasurer uncertain whether a large euro receivable will materialize in six months might buy a call on a call. In month three, they learn the deal is closing. They exercise the outer call, paying the second premium, and now own a three-month call protecting the incoming euro revenue. If the deal falls through in month three, they never exercise the outer option and lose only the initial €500.

Hedge funds and volatility traders exploit compound options to leverage a view on volatility *of volatility*. If you expect implied [volatility](/implied-volatility/) to spike, you buy a call on a call. If realized volatility is low in the first three months, the outer call expires worthless and you lose minimal premium. But if volatility explodes, the inner option's value skyrockets, and the outer option becomes deeply in-the-money.

## The four types

Compound options come in four flavors:

1. **Call on a call**: Right to buy a call. Attractive for bullish traders wanting leverage on upside moves.
2. **Put on a call**: Right to sell a call. The holder gains if the underlying option depreciates; used for defensive hedging or when expecting a sharp decline in the underlying asset's price.
3. **Call on a put**: Right to buy a put. Useful for investors expecting volatility to rise but uncertain of direction.
4. **Put on a put**: Right to sell a put. Uncommon but occasionally used in crisis hedging, where investors want protection against a protection instrument itself depreciating.

In FX markets, the most common are calls on calls (bullish on the pair) and puts on calls (bearish or volatility-neutral, expecting mean reversion).

## Pricing complexity

Compound options are harder to price than vanilla [options](/option/) because they embed a choice about a future choice. The fair value depends on:

- The current spot rate and both strike prices.
- The volatility of the underlying FX pair (affects the inner option's value at outer expiry).
- The volatility of volatility (affects whether the inner option will be in-the-money when the outer option expires).
- Two [time-value](/time-value/) components: one for the outer option, one (embedded) for the inner option.

Banks use [Black-Scholes](/black-scholes-model/) extensions or Monte Carlo methods, modeling the distribution of the inner option's value at the outer option's expiration date. The outer option's payoff is then the maximum of zero and (inner option value minus exercise premium).

The compound option's gamma (sensitivity to spot moves) is especially high around the outer strike, and theta (time decay) is unusual: the outer option bleeds premium while the inner option's value sometimes rises as expiry approaches (if increasing [volatility](/volatility-smile/) makes the inner option more valuable).

## Applications in FX markets

**Corporate hedging**: An importer unsure of a future payment date buys a call on a put (or put on a call) to defer the full hedge cost until the payment is confirmed. Once confirmed, exercising the outer option locks in the inner hedge.

**Carry-trade positioning**: A trader expecting long-dated interest-rate differentials between USD and JPY to widen might buy a call on a call on USD/JPY. If rates diverge as expected, the inner call captures the move; if rates stabilize, the trader exits with minimal loss.

**Volatility speculation**: A quant fund expects implied volatility on EUR/GBP to spike in three months but is uncertain about direction. Buying a call on a put allows them to express volatility-of-volatility without betting on spot direction. The outer premium is cheap; the inner option's value is highly sensitive to realized [volatility](/volatility-smile/).

**Emerging-market optionality**: Central banks in volatile emerging markets sometimes face surprise policy announcements. A local exporter might buy a call on a call on USD/BRL, giving them the right to buy downside protection if the central bank surprises. The initial cost is low because the first leg is deeply out-of-the-money.

## Costs and risks

The headline advantage—deferred cost—comes with trade-offs. The most severe is **path dependency**: the outer option's value at expiration depends on the inner option's delta and vega at that moment, which are themselves volatile. A large move in the first leg can make the outer option either deeply in-the-money (if you get lucky on volatility) or worthless (if volatility collapses).

**Exercise failure**: Even if the outer option is in-the-money, exercising may be irrational if the inner option's remaining time value has deteriorated. The trader is forced to pay the exercise premium and enter a position they may immediately regret. This creates an option on an option on an option in practice—complex decision trees emerge.

**Bid-ask spreads** on compound options are wide because few traders mark them, and rehedging is expensive. A bank short a call on a call must dynamically hedge both legs, rebalancing as volatility moves. This cost is embedded in the pricing, making compounds expensive relative to vanilla alternatives.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the underlying instrument; compound options are written on them
- [Strike price](/strike-price/) — both outer and inner strikes govern payoff
- [Time value](/time-value/) — compounds have two time-decay components
- [Exercise price](/exercise-price/) — the premium you pay to enter the inner option
- [Volatility smile](/volatility-smile/) — affects the inner option's value and hence the compound's pricing

### Wider context

- [Black-Scholes model](/black-scholes-model/) — foundational pricing framework (extended for compounds)
- [Implied volatility](/implied-volatility/) — critical input; volatility of volatility drives compounds
- [Delta](/delta/) — the inner option's delta affects outer option hedging
- [Gamma](/gamma/) — compounds exhibit extreme gamma near outer strike
- [Theta](/theta/) — unusual time decay patterns in compounds
- [Leverage ratio (forex)](/leverage-ratio-forex/) — compounds are leverage vehicles for volatility exposure

</div>

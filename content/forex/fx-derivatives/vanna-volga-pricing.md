---
title: "Vanna-Volga Pricing"
description: "Market-standard FX options valuation method that adjusts Black-Scholes for the cost of hedging vanna and volga Greeks against the volatility smile."
keywords:
  - vanna
  - volga
  - fx options
  - volatility smile
  - greek hedging
image: /svg/forex.svg
---

*The **vanna-volga method** is the industry standard for pricing FX options, particularly exotic structures, by adding smile-adjustment costs to the [Black-Scholes](/black-scholes-model/) baseline. Vanna (sensitivity of delta to volatility changes) and volga (sensitivity to volatility of volatility) represent the cost of hedging a dealer's exposure to the curved shape of the volatility smile; the premium above Black-Scholes reflects the fact that rebalancing hedges against real-world volatility movements will drain cash from a seller's position.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vanna-Volga Pricing — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for FX instruments." />

<div class="wiki-infobox-caption">Smile-adjusted option pricing via replication of vanna and volga costs.</div>

|   |   |
|---|---|
| **What it is** | Adjustment to Black-Scholes for volatility smile impact |
| **Core insight** | Hedging vanna and volga creates real cashflow costs |
| **Key Greeks** | Vanna (∂Δ/∂σ), volga (∂Γ/∂σ) |
| **Smile representation** | Risk reversal and butterfly spreads |
| **Primary use** | FX exotics and vanilla options in major pairs |
| **Alternative model** | Local volatility, stochastic volatility (Heston) |
| **Market adoption** | De facto standard for FX dealer quoting |

</aside>

## The Black-Scholes gap

The [Black-Scholes model](/black-scholes-model/) assumes a flat volatility surface: all strikes and expiries have the same implied volatility. In practice, currency markets exhibit a pronounced volatility smile. For a given expiry, at-the-money (ATM) options have lower implied volatility than far out-of-the-money (OTM) or deep in-the-money (ITM) strikes. Additionally, short-dated options tend to have higher implied volatility (term structure effect).

A dealer who quotes a far-OTM call using only ATM Black-Scholes volatility will systematically underprice it. When the dealer hedges by buying a short-dated ATM straddle to lock in Greeks, market moves cause the hedge to slip in value. Vanna-volga pricing quantifies this slippage cost.

## The Greeks involved

Vanna is the cross-Greek linking delta and volatility: ∂Δ/∂σ. When spot volatility rises and an option was sold, the delta of that position increases (long calls become longer delta), requiring the dealer to sell more spot to re-hedge. The loss incurred if spot then rallies is the vanna cost.

Volga (sometimes called "volvol" or "convexity") is the second-order derivative of option value with respect to volatility: ∂²V/∂σ². A sold option with positive volga loses value as volatility of volatility increases; the dealer is short the convexity of the volatility surface. A buyer of far-OTM calls, for instance, is long volga: if spot becomes chaotic and implied volatility spreads widen, the call's value rises disproportionately.

The vanna-volga adjustment captures the cost of dynamically hedging these Greeks. Rather than assume costless rebalancing (as Black-Scholes does), the method recognises that real hedges demand real money.

## Implementation: smile replication

The vanna-volga model replicates the volatility smile using two instruments:

1. **Risk reversal (RR)**: the price difference between an OTM call and an OTM put at the same delta, e.g., 25 delta. It encodes the slope of the smile—whether the market prices downside volatility higher than upside, or vice versa.

2. **Butterfly (BF)**: the average of OTM call and OTM put implied volatilities minus the ATM volatility, scaled for the strike spacing. It captures the curvature of the smile.

A dealer receives market quotes for ATM, RR, and BF for a given expiry. From these, the method computes the vanna hedge cost (proportional to RR) and volga hedge cost (proportional to BF), then adds both to the Black-Scholes premium. The formula is roughly:

**Vanna-Volga Price = BS Price + Vanna Hedge Cost + Volga Hedge Cost**

For example, if a dealer sells a 25-delta call in EUR/USD, the [Black-Scholes](/black-scholes-model/) price might be 1.50 per cent of notional. If the market prices the risk reversal (OTM call vs OTM put spread) at +0.20 per cent, the dealer adds a vanna component; if the butterfly is +0.10 per cent, a volga component is added. The final quote might be 1.75–1.80 per cent.

## Why it works in FX

Currency markets are particularly suited to vanna-volga because spot rates exhibit strong mean reversion and high correlation with realized volatility. The smile emerges partly from the probability of extreme moves (which demand OTM premiums) and partly from the fact that dealers hedge by trading short-dated ATM options. As spot drifts, delta hedges need constant rebalancing, and vanna captures that friction cost.

Another reason: FX options trade in continuous markets with tight bid-ask spreads on ATM, RR, and BF instruments. Dealers can quickly calibrate the smile to current market prices, making the vanna-volga adjustment practical and real-time.

## Limitations and alternatives

Vanna-volga assumes that the smile remains stable and that [counterparties](/counterparty-risk/) can always execute hedges at quoted spreads. In stressed markets—such as a central bank shock or liquidity event—the smile becomes jagged, hedges blow out in cost or become unavailable, and the model breaks down.

The method also assumes that vanna and volga are the dominant smile drivers. In reality, gamma (second-order spot sensitivity) and other higher-order Greeks matter. A more sophisticated approach is local volatility, which allows spot-dependent implied volatility surfaces; these models are computationally heavier but capture smile dynamics more faithfully.

[Stochastic volatility](/equity-etf/) models (such as Heston) go further, modelling volatility itself as a random process with its own drift and diffusion. For very long-dated or exotic structures, Heston or similar approaches may be more accurate than vanna-volga. However, their complexity and longer calibration time limit real-time trading use.

## Practical trading application

A trader might use vanna-volga to identify basis: if a dealer quotes 1.80 per cent for a 25-delta call but vanna-volga calculation suggests fair value is 1.70 per cent (due to an inexpensive risk reversal), the trader sells the call and hedges with a synthetic long call built from spot, a call option, and a put option positioned to offset vanna and volga.

Market makers also use vanna-volga to set bid-ask spreads. A thin bid-ask on the RR or BF directly widens the spread on exotic options. High-frequency FX options traders constantly recalibrate vanna-volga to respond to microsecond moves in ATM, RR, and BF levels.

Exotic structures like [FX Forward Extra](/fx-forward-extra/) products are typically valued using vanna-volga as a starting point, then adjusted for any additional strikes or barriers that add Greeks outside the simple vanna-volga framework.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes Model](/black-scholes-model/) — foundational option pricing framework assuming flat volatility
- [Option](/option/) — derivative contract granting the right to buy or sell
- [Volatility Smile](/equity-etf/) — pattern of implied volatility across strikes
- [FX Variance Swap](/fx-variance-swap/) — pure volatility exposure independent of directional drift
- [FX Forward Extra](/fx-forward-extra/) — structured product with embedded optionality priced via vanna-volga
- [Delta](/option/) — rate of change of option price with respect to spot
- [Implied Volatility](/equity-etf/) — volatility backed out from option market prices
- [Currency Risk](/currency-risk/) — exposure to adverse FX movements

### Wider context

- [Currency Volatility](/currency-volatility/) — fluctuations in FX spot rates
- [Over-the-Counter Market](/over-the-counter-market/) — decentralised derivatives trading
- [Price Discovery](/price-discovery/) — mechanism by which derivative prices aggregate market views
- [Interest Rate Risk](/interest-rate-risk/) — parallel hedging problem in fixed income
- [Hedge Fund](/hedge-fund/) — institutional investors who often trade FX derivatives

</div>

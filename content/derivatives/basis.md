---
title: "Basis (Futures)"
description: "Basis is the difference between a futures contract price and the spot price of the underlying asset, measuring the market's valuation of carrying the asset forward."
keywords:
  - basis
  - futures basis
  - spot-futures spread
  - convergence
  - hedging
image: "/svg/derivatives.svg"
---

*The **basis** is the difference between the [futures contract](/futures-contract/) price and the spot price of the underlying asset. Basis = Futures Price − Spot Price. When a [futures contract](/futures-contract/) is more expensive than spot (positive basis), the market is in [contango](/contango/). When a futures contract is cheaper (negative basis), the market is in [backwardation](/backwardation/). The basis reflects the [cost-of-carry](/cost-of-carry/) (storage, financing, insurance) and converges to zero at [expiration date](/expiration-date/), creating opportunities and risks for hedgers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis — key facts</div>

<img src="/svg/derivatives.svg" alt="Spot and futures price convergence chart" />

<div class="wiki-infobox-caption">Basis measures spot-futures difference; converges at expiration.</div>

|   |   |
|---|---|
| **Formula** | Basis = Futures Price − Spot Price |
| **Positive** | Futures > spot (contango) |
| **Negative** | Futures < spot (backwardation) |
| **Drivers** | Storage costs, financing, convenience yield |
| **Convergence** | Basis → 0 as contract nears expiration |
| **At expiration** | Basis = 0 (futures = spot) |
| **Hedging impact** | Basis risk remains even with hedge |
| **Measurement** | Can be absolute ($) or percentage (%) |
| **Rolling strategy** | Exploits basis changes |
| **Arbitrage** | Buy spot, sell futures when basis wide |

</aside>

## Basis and cost-of-carry

The basis is fundamentally linked to [cost-of-carry](/cost-of-carry/). When you buy oil today and store it for 6 months, the futures price should equal spot plus storage + financing. The difference is the basis.

Basis = [Cost-of-carry](/cost-of-carry/)

For example:
- Spot oil: $70/barrel
- 6-month storage: $2/barrel
- 6-month financing (interest): $1.50/barrel
- Expected 6-month futures: $73.50
- Basis: $73.50 − $70 = +$3.50 (positive, signaling [contango](/contango/))

## Basis convergence

As a [futures contract](/futures-contract/) nears [expiration date](/expiration-date/), the basis shrinks. At expiration, the futures price must equal the spot price; there is no difference. This creates **basis convergence risk** for hedgers.

Example:
- Jan 1: Spot $70, June futures $73.50 (basis +$3.50)
- June 15: Spot $75, June futures $75.00 (basis converges to ~$0)

A hedger short June futures (locked in at $73.50) and long the commodity loses because the commodity rose to $75, and the futures also converged to $75. The hedge was imperfect due to basis.

## Basis risk in hedging

Perfect hedging requires the basis to remain constant. But basis is dynamic; it changes with [cost-of-carry](/cost-of-carry/), interest rates, and convenience yield.

A farmer hedging the fall harvest by selling September grain futures faces basis risk: if the basis narrows unexpectedly, the future value of his grain falls relative to the locked-in futures price.

## Profitable basis trades

When basis widens (futures diverge from spot), traders can exploit it:

- **Buy spot, sell futures:** If basis is wide positive (contango is steep), buy the commodity and sell the far futures contract. The convergence at expiration locks in profit.
- **Sell spot, buy futures:** If basis is negative (backwardation), short the spot and buy near futures, profiting as basis reverts.

These are called **basis trades** or **cash-and-carry trades**.

## Basis across different assets

**Stock indices:** Basis is usually small (storage not applicable) and varies with interest rates and [dividend](/dividend/) yield.

**Commodities:** Basis is substantial and varies with storage costs (oil, metals) or seasonal patterns (grains).

**Bonds:** Basis varies with repo rates and delivery options in the futures contract.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the derivative with basis
- [Spot price](/strike-price/) — current market price
- [Contango](/contango/) — positive basis
- [Backwardation](/backwardation/) — negative basis
- [Cost of carry](/cost-of-carry/) — drives basis

### Hedging and risk

- [Hedging](/hedge-fund/) — basis risk in hedge effectiveness
- [Convergence](/mark-to-market/) — basis approaches zero at expiration
- [Arbitrage](/alpha/) — exploiting basis mispricings
- [Spread trading](/alpha/) — basis trades

### Market structure

- [Forwards](/forward-contract/) — forward prices embody basis
- [Convenience yield](/backwardation/) — component of negative basis
- [Interest rates](/interest-rate/) — affect basis level
- Storage costs — component of positive basis

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Price discovery](/stock-market/) — basis reflects market expectations
- [Market efficiency](/stock-market/) — basis arbitrage keeps pricing fair

</div>

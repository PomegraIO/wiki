---
title: "Why Futures Basis Converges to Zero at Expiry"
description: "Futures basis converges to zero at expiry because arbitrage eliminates price gaps between futures and spot price at delivery."
keywords:
  - futures basis convergence
  - basis convergence
  - futures contract expiry
  - spot price
  - arbitrage
  - futures pricing
---

*The **futures basis**—the difference between a futures contract's price and the [spot-rate](/spot-rate/) of the underlying asset—shrinks as the contract approaches expiry and becomes zero on the final settlement date. This convergence is not magical; it is the result of pure arbitrage: any gap between futures and spot price creates a risk-free profit for a trader willing to exploit it, and competition for that profit eliminates the gap.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Basis Convergence — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Arbitrage forces convergence; the gap vanishes at settlement.</div>

|   |   |
|---|---|
| **Definition** | Basis = Futures price − Spot price |
| **At expiry** | Basis = 0 (futures price equals spot price) |
| **Reason** | Arbitrage eliminates any profitable gap |
| **Key contract** | Delivery date (or cash-settlement date) |
| **Before expiry** | Basis is nonzero; depends on [carry costs](/cost-of-carry/), [contango](/contango/), [backwardation](/backwardation/) |
| **Arbitrage mechanism** | Cash-and-carry or reverse cash-and-carry |
| **Implication** | Hedgers face basis risk; speculators face basis tightening |

</aside>

## The arbitrage intuition

Suppose crude oil trades at $80 per barrel on the spot market today. A [futures-contract](/futures-contract/) for delivery in three months is trading at $78. A trader can:

1. Buy physical oil at $80 today.
2. Simultaneously sell the futures contract at $78.
3. Store the oil for three months (paying storage costs, let's say $2).
4. At expiration, deliver the oil against the futures contract and receive $78.

Profit: $78 − $80 − $2 = −$4. This is a loss, so the trader would never do it. But the existence of this loss tells us the futures is *underpriced* relative to spot plus carry costs.

Now suppose the futures contract is trading at $83 instead, and storage still costs $2:

1. Buy oil at $80 today.
2. Sell the futures at $83.
3. Store for three months at a cost of $2.
4. Deliver and receive $83.

Profit: $83 − $80 − $2 = $1 per barrel. A free $1. This trade is called a **cash-and-carry arbitrage**, and traders will execute it repeatedly until the opportunity vanishes.

As traders flood into this arbitrage (buying spot, selling futures), the spot price is bid up and the futures price is pushed down. This continues until the gap closes. At equilibrium, Futures price = Spot price + Carry costs. If carry costs are zero or negligible (or are priced into the forward curve), then Futures price ≈ Spot price.

## Why the gap must shrink as expiry approaches

In the three-month example, carry costs ($2) justified a futures-spot gap of $2 (assuming no other factors). But as the contract nears expiry, fewer days remain, and carry costs—storage, insurance, financing—shrink proportionally. With one week until expiry, storing oil costs only a few cents, so the gap shrinks to match.

On the final day before settlement, carry costs are negligible. The last trader holding a futures contract is essentially holding the same economic position as the spot holder: both have the asset (or the obligation to take delivery) at nearly the same cost. The futures price converges to the spot price.

At the moment of settlement or expiry:
- A futures contract holder either takes delivery (receiving the actual asset) or settles in cash at the contract's final settlement price.
- A spot holder owns the asset outright.
- These two positions are economically identical. There is no gap.

If a gap persisted at expiry (say, futures at $80.50 and spot at $80), an arbitrageur would be able to buy spot at $80, sell futures at $80.50, and lock in $0.50 with zero carry cost—an infinite return on a zero-duration trade. This attracts infinite capital, instantly eliminating the gap. In practice, exchanges enforce delivery mechanics that make the gap exactly zero.

## Basis before expiry: carry and convenience yield

Before expiry, the basis can be nonzero, and its sign and magnitude tell a story about supply and demand.

**Contango:** When Futures price > Spot price, the market is in [contango](/contango/). The basis is negative (Futures − Spot = negative). This typically occurs in markets with significant [carry costs](/carry-trade/): storage, insurance, financing. Example: oil in normal market conditions, where storage and transport dominate. A three-month oil futures might trade $3 above spot to compensate the holder for three months of carry.

**Backwardation:** When Futures price < Spot price, the market is in [backwardation](/backwardation/). The basis is positive (Futures − Spot = positive). This occurs when the spot asset is urgently needed—there is a premium to having it *now* rather than later. Example: wheat during a harvest shortage, where end-users need grain immediately. A three-month future might trade $1 *below* spot because immediate delivery is so valuable.

The convenience-yield concept captures this: if holding the spot asset offers immediate benefits (you can mill wheat now, or use oil now), those benefits offset carry costs, causing backwardation.

## The convergence path: rolling and basis risk

For hedgers, understanding convergence is critical. Suppose a farmer locks in a crop sale price using a [futures-contract](/futures-contract/). As the contract nears expiry, the basis tightens. If the farmer had hedged at a time when futures were in contango (futures above spot), the basis tightening works in their favor: they receive a higher futures price as the basis shrinks. If they hedged when futures were in backwardation, the tightening works against them: they receive a lower futures price than they had anticipated.

This basis risk—uncertainty about where the basis will be at settlement—is distinct from price risk. Even a perfectly hedged position (long spot, short futures) can realize a loss if the basis widens unexpectedly or tightens in an unfavorable direction. Over very short periods near expiry, basis risk is small; over longer horizons, it can be material.

Long-term hedgers often "roll" their futures positions—closing the expiring contract and opening a new one further out. On roll dates, they are exposed to basis convergence: the outgoing contract converges to spot, while the incoming contract is at a different basis determined by new carry costs and market conditions.

## Delivery mechanics and cash settlement

Most financial futures (stock index, interest rate, currency futures) settle in cash rather than physical delivery. The exchange sets the final settlement price equal to the spot price (or a specified index value) on the last day. This is the mechanical enforcement of zero basis at expiry: the contract value and spot value are literally defined to be equal.

Physical delivery futures (crude oil, grains, metals) allow holders to take or make physical delivery. Here, the arbitrage mechanism is subtle: the exchange specifies the deliverable grades and locations, storage and transport are the trader's responsibility, and the futures price is set such that the all-in cost of buying spot and delivering equals the futures price. This too enforces convergence.

## Example: crude oil futures

WTI Crude Oil futures (traded on NYMEX) typically trade in contango: a front-month contract might be $79.50, while a three-month contract is $82. The $2.50 gap reflects the cost to store, insure, and finance oil for three months. As the front-month contract nears expiry (say, five days out), that contract converges toward the spot price. It might rise to $80.25 as storage costs shrink to two weeks' worth ($0.75). On the final trading day, the convergence is nearly complete.

A trader who sold the three-month contract at $82 three months ago, and bought the front-month at $80.25 on that final day, captured a tightening basis gain: ($82 − $80.25) = $1.75 profit per barrel, less actual storage and financing costs. This is basis trading—profiting from the convergence itself rather than betting on absolute price direction.

## Why this matters for speculators and hedgers

**Speculators:** A trader betting on crude oil price direction can use futures. But understanding basis convergence reveals a hidden risk: even if your price direction is right, basis tightening can erase gains. A trader who is bullish and buys three-month futures is implicitly short the basis—they will suffer if the basis tightens faster than expected.

**Hedgers:** A farmer hedging next year's harvest with futures needs to account for basis at the time they plan to make the sale. They can lock in a price target by selling futures, but the actual price received is futures price plus (or minus) basis on the settlement date. Basis uncertainty is a real cost.

**Arbitrageurs:** Understanding the carry structure and basis convergence creates exploitable mispricings. A trader who can estimate true carry costs and spot any deviation in the futures-spot gap can execute a risk-free arbitrage.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures-contract](/futures-contract/) — core mechanics and settlement
- [Spot-rate](/spot-rate/) — current market price of the underlying asset
- [Basis](/basis/) — general definition of futures-spot spread
- [Contango](/contango/) — futures above spot; normal carry markets
- [Backwardation](/backwardation/) — futures below spot; convenience premium
- [Carry-trade](/carry-trade/) — profiting from basis convergence
- [Forward-contract](/forward-contract/) — similar but over-the-counter pricing

### Wider context

- Arbitrage — mechanism enforcing convergence
- [Cost-of-carry](/cost-of-carry/) — determines basis magnitude
- Convenience-yield — supply-demand urgency of spot asset
- [Futures-contract](/futures-contract/) — pricing theory and practical markets

</div>

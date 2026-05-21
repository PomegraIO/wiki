---
title: "Contango"
description: "Contango is a situation where futures prices are higher for distant delivery dates than for near-term dates, reflecting the cost of carry (storage, financing, insurance)."
keywords:
  - contango
  - futures pricing
  - cost of carry
  - future prices
  - commodity futures
image: "/svg/derivatives.svg"
---

*In **contango**, futures prices increase with the delivery date. A [futures contract](/futures-contract) expiring in 3 months is cheaper than one expiring in 6 months, which is cheaper than one expiring in 12 months. Contango occurs because holding the underlying asset over time carries costs—storage fees, insurance, financing—passed to the buyer of distant futures. Contango is the normal state in most commodity and interest-rate markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contango — key facts</div>

<img src="/svg/derivatives.svg" alt="Upward sloping futures curve" />

<div class="wiki-infobox-caption">Contango: futures prices rise into the future.</div>

|   |   |
|---|---|
| **Pattern** | Near prices < far prices |
| **Curve shape** | Upward sloping |
| **Causes** | Storage, financing, insurance costs |
| **Formula** | Fwd Price = Spot × e^(r×T+storage) |
| **Common in** | Oil, grains, metals, bonds |
| **Economics** | Imbalance: more storage demand than supply |
| **Opposite** | Backwardation (far < near) |
| **Rolling cost** | Traders lose money rolling long positions |
| **Hedge benefit** | Helps futures look cheap to spot price |
| **Speculation** | Can profit from curve steepening/flattening |

</aside>

## The cost-of-carry explanation

When you buy oil today (spot), you must store it, insure it, and finance the purchase. These costs accumulate over time. A [futures contract](/futures-contract) 6 months out should reflect these costs, so it trades higher than a near-term contract.

The formula:

Forward Price = Spot Price × e^(r×T + storage costs)

The farther out the contract, the larger the storage and financing costs accumulated, so the higher the price.

## Economics of contango

Contango signals that the market has ample supply. Storage is being used; inventory is building. Suppliers can produce today and store for later, so they push prices forward to cover storage.

Conversely, [backwardation](/backwardation) signals tight supply. Immediate delivery is scarce and commands a premium.

## Rolling losses in contango

A trader long oil (betting on price appreciation) might buy a 12-month [futures contract](/futures-contract). As it approaches expiration, they sell it and buy a new 12-month contract, rolling the position forward.

In contango, the near contract (selling) is cheaper than the far contract (buying). The trader loses money on the roll—"buying high, selling low" in the futures curve.

For example:
- Month 1: Buy 12-month contract at $70/barrel
- Month 11: Sell the now-1-month contract at $68/barrel
- Buy the new 12-month contract at $71/barrel
- Loss on roll: $1/barrel

This rolling loss is a cost of holding long positions in contango markets.

## Storage and carry trades

A trader can exploit contango using a **carry trade**: buy the spot commodity, store it, and sell a futures contract for a later date. If the futures price exceeds the spot price plus storage costs, the trader locks in a riskless profit.

Example:
- Buy oil spot at $65/barrel
- Pay $1/barrel storage for 6 months
- Sell 6-month futures at $67/barrel
- Profit: $67 − $65 − $1 = $1/barrel (riskless)

This arbitrage reduces contango; it does not eliminate it because storage capacity is limited and financing costs vary.

## Industry implications

Companies in contango markets (oil producers, grain traders) benefit: they can produce today, lock in future prices above today's costs, and profit from the contango.

Speculators and commodity funds lose: they roll long positions at losses, reducing returns.

## Curve shape and strategy

A steep contango (near-far spread is large) makes rolling expensive and creates opportunities to flatten the curve by selling near futures and buying far futures (spreading strategy).

A flat contango (near-far spread is small) offers less rolling loss but suggests the market is closer to balanced supply-demand.

## See also

<div class="wiki-seealso">

### Closely related

- [Backwardation](/backwardation/) — opposite: far prices < near prices
- [Basis](/basis/) — spot vs. futures spread
- [Cost of carry](/cost-of-carry/) — drives contango
- [Futures contract](/futures-contract/) — where contango appears
- [Forward contract](/forward-contract/) — similar pricing patterns

### Trading implications

- [Rolling](/basis) — moving from near to far contract
- [Carry trade](/alpha/) — exploiting contango for profit
- [Curve flattening](/volatility-smile/) — betting on contango change
- [Curve trades](/alpha) — spreads between maturities

### Market structure

- [Commodity markets](/stock-market) — typical contango pattern
- [Interest-rate futures](/interest-rate-swap) — bond futures often in contango
- [Market equilibrium](/stock-market/) — contango reflects supply-demand
- Storage — fundamental to contango

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Risk management](/hedge-fund/) — understanding contango risk
- [Arbitrage](/alpha/) — exploiting contango mispricings

</div>

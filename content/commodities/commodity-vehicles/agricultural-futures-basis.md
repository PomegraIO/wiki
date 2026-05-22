---
title: "Agricultural Futures Basis"
description: "The price difference between futures contracts and physical crop delivery, reflecting storage, transport, and seasonal supply."
keywords:
  - futures basis
  - crop pricing
  - storage costs
  - commodity spreads
  - delivery dynamics
---

*The **agricultural futures basis** is the gap between the futures contract price and the spot price of the physical crop. It expands and contracts based on harvest timing, storage costs, transportation, and [carry costs](/wiki/cost-of-carry/), making it central to both hedging and [arbitrage](/wiki/arbitrage-defi/).*

<div class="wiki-hatnote">For the broader concept of basis risk in securities, see [Basis Risk](/wiki/basis-risk/).</div>

<aside class="wiki-infobox">

| Component | Role |
|-----------|------|
| Basis definition | Spot price − Futures price (or vice versa by convention) |
| Sign at harvest | Often negative (futures premium over spot) |
| Sign pre-harvest | Often positive (spot premium; scarcity) |
| Storage costs | Widen basis by increasing carry-cost component |
| Convergence | Basis narrows to zero at futures expiration |
| Calendar spreads | Driven by basis changes across contracts |

</aside>

## The source of agricultural basis

The basis emerges from the **cost of carry**—the total cost of storing grain or livestock, insuring it, and transporting it to the delivery point. When corn is harvested in October, elevators and merchants immediately face the question: sell now at harvest prices, or store the crop and sell later? 

The futures market prices future delivery, typically several months hence. If storage costs $0.30 per bushel over six months, buyers will only pay spot price minus $0.30 for a six-month future (or less, accounting for financing and insurance). This creates the "basis"—the discount or premium of futures relative to physical grain.

At harvest, when bins are full and supply is abundant, futures often trade at a premium to spot (negative basis): elevators are desperate to sell physical grain and willing to sell futures contracts at lower prices to hedge supply risk. By spring, storage has depleted supply and raised costs, so spot prices may exceed nearby futures prices (positive basis), reflecting the scarcity of immediate availability.

## Seasonal patterns in basis

Corn, soybeans, wheat, and [cattle](/wiki/live-cattle/) all exhibit predictable basis cycles tied to harvest and movement:

**Harvest season** (late August–November for corn): Supplies are abundant. Elevators and farmers must decide: sell immediately at low prices, or store and sell later at higher prices offset by storage costs. Futures are often at a premium because the market expects lower spot prices once the harvest glut passes.

**Pre-harvest** (May–July): Supplies are tight. Farmers have already sold to elevators; the pipeline is empty. Spot prices often rise above futures as end-users rush to secure inventory before the new crop arrives. This "inverted" basis rewards storage—buying physical grain cheaply in the harvest glut and selling it in the lean season.

**Post-harvest winter**: Storage costs are accruing. The basis widens again, pricing in the cost to carry grain from January to March or June.

## Why basis matters to hedgers

A farmer selling 5,000 bushels of corn might lock in a price by selling [futures](/wiki/futures-contract/) rather than delivering physical grain immediately. But the farmer's actual cash sale often happens at a different location—a local elevator may offer a price 30 cents below the futures price. The farmer's realized price is not the futures price alone; it's futures *minus* the local basis.

If the farmer assumes a basis of −$0.30 (futures 30 cents higher than spot) and the futures move up $1.00, the farmer expects a $0.70 profit. But if the basis shifts unexpectedly to −$0.50 (futures premium widens), the farmer's realized gain falls to $0.50. This **basis risk** is why farmers and elevators track basis obsessively and sometimes trade basis contracts—bets on how the spread will evolve, independent of the direction of prices.

## Basis arbitrage in practice

A grain merchant with storage capacity can exploit wide basis. In October, when harvest is in full swing and the basis is very negative (futures trading at a large premium), the merchant:

1. **Buys physical corn** at the low harvest spot price.
2. **Sells futures** to lock in the premium.
3. **Stores the grain** over winter.
4. **Delivers into the futures contract** at expiration, pocketing the difference (futures premium) minus storage costs.

This is profitable as long as the storage and transport costs are less than the basis premium. If storage is $0.25 per bushel and the basis offers $0.40 premium, the merchant nets $0.15 per bushel on millions of bushels—a high-volume, low-margin business.

Conversely, when the basis is very positive (spot premium), the same merchant might short-sell physical grain and go long futures, profiting if the basis compresses.

## Calendar spreads and rolling basis

Traders also trade the basis *across different contract months*. The December corn futures might trade $0.15 higher than March corn, reflecting the cost to store corn from December to March. A trader who believes storage costs are about to fall (perhaps a new storage facility opens) might sell December and buy March—betting the spread narrows.

This **calendar spread** is really a bet on the *cost of carry*, which is rooted in basis dynamics. As each contract approaches expiration, its basis converges to zero—the futures price equals spot price at the delivery location, because the holder can always demand physical delivery.

## Delivery and settlement

Most agricultural futures never result in actual delivery. Most traders close out positions before expiration. But the *possibility* of delivery is what anchors the basis: if December futures are wildly overpriced relative to spot plus carry costs, a counterparty can always step in, buy spot grain, ship it to the exchange's approved warehouse, and demand delivery of the futures. This arbitrage keeps the basis tethered to the real cost of carry.

For livestock like [feeder cattle](/wiki/feeder-cattle-futures/), basis is even more complex—it includes the cost of feed, care, and weight gain between purchase and delivery, making basis highly sensitive to [feed costs](/wiki/corn/) and logistics.

## Basis and margin requirements

When farmers or merchants carry physical inventory and sell futures as a hedge, they're typically funded by a bank. The [initial margin](/wiki/initial-margin/) on the futures contract is often lower than the cost of the underlying grain, which incentivizes hedging. But if the basis moves against them sharply—say, a storage facility catches fire and spot prices spike—the hedge can lose money while the physical inventory appreciates, creating a margin call risk.

<div class="wiki-seealso">

### Closely related
- [Cost of Carry](/wiki/cost-of-carry/) — theoretical foundation
- [Commodity Swap](/wiki/commodity-swap/) — related hedging tool
- [Futures Contract](/wiki/futures-contract/) — core instrument
- [Basis Risk](/wiki/basis-risk/) — risk perspective
- [Calendar Spread](/wiki/calendar-spread-commodity/) — spread trading

### Wider context
- [Commodity Futures](/wiki/commodity-futures-rolling/) — rolling and roll yield
- [Agricultural Commodity](/wiki/corn/) — specific crops
- [Convenience Yield](/wiki/convenience-yield-commodity/) — supply scarcity premium
- [Contango](/wiki/contango/) — forward curve shape

</div>

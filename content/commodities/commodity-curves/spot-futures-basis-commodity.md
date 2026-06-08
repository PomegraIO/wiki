---
title: "Spot-Futures Basis (Commodities)"
description: "The difference between the cash spot price and the front-month futures price, narrowing predictably to zero at delivery."
keywords:
  - commodity basis
  - spot price
  - futures contract
  - cash convergence
  - hedging
  - price discovery
image: "/svg/commodities.svg"
---

*The **spot-futures basis** in commodities is the gap between the current cash price for immediate delivery and the price of the nearest-term [futures contract](/futures-contract/). This spread converges to zero at contract expiration, creating a powerful arbitrage anchor and defining the cost of deferring delivery.*

<div class="wiki-hatnote">

For the related difference between a contract's spot and forward price in forex, see [Spot-Futures Basis (FX)](/leverage-ratio-forex/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Spot-Futures Basis — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodity trading and price formation." />

<div class="wiki-infobox-caption">The bridge between today's price and tomorrow's contract, tightening to zero at expiration.</div>

|   |   |
|---|---|
| **What it is** | Cash spot price minus front-month futures price |
| **Also called** | "The basis"; often quoted as futures minus spot |
| **Sign** | Positive when futures trade above spot (normal in [contango](/contango/)); negative in [backwardation](/contango/) |
| **Convergence** | Narrows to zero (or nearly zero) at contract delivery |
| **Drives** | Storage costs, convenience yield, financing rates, transport |
| **Used by** | Hedgers, arbitrageurs, cash traders, refiners, millers |

</aside>

## The convergence guarantee

The spot-futures basis exists because they are two prices for almost the same thing—today's commodity and a future delivery of it. A trader can walk into a physical market, buy crude oil or wheat *right now* at the spot price, then sell a futures contract *three months out* at the futures price. If she stores the commodity carefully until the contract matures, she delivers it into the contract and pockets the difference.

This arbitrage is so mechanical—buy low, store at known cost, deliver high, pocket profit—that it forces convergence. If the futures price climbs too far above the spot price, cash traders flood in: they buy physicals and sell futures, pushing futures down and spot up. If futures fall below spot, the opposite happens: holders of inventory sell futures, knowing they can deliver at a premium. On the final day of the contract, spot and futures *must* touch (or come within bid-ask whiskers), because the futures contract *is* cash delivery or settlement.

The basis, then, isn't magic. It's an arbitrage-free relationship that reflects the known cost of carry: storage rent, insurance, financing charges, and—for some commodities—the benefit of holding physical stock immediately available to meet demand.

## What the basis tells you

A positive basis (futures above spot) typically signals a seller's market or normal supply. The owner of crude in a tank or grain in a silo can afford to wait and deliver later; the premium compensates her for tying up capital and warehouse space. A refiner needing crude *today* must buy spot and pay more; a refiner patient enough to wait can lock in a cheaper future price.

A negative basis (spot above futures) signals shortage or convenience premium. Immediate supply is constrained; traders will pay a premium to get the commodity *now* rather than wait for contract delivery. This is backwardation, and it often means supply is tight enough that holding inventory has real value—the privilege of having barrels on hand, available to sell at a moment's notice when someone is desperate. Petroleum refiners, natural-gas utilities, and power generators with just-in-time operations will pay negative basis (spot premium) to ensure they don't shut down waiting for a late shipment.

The magnitude of the basis—whether it's 0.5% or 5% of spot—encodes the tightness of supply and the degree of immediate urgency in the market. During a crude oil supply shock or a grain harvest delay, the basis can spike sharply negative. When supplies are relaxed and storage is comfortable, it settles into a steady positive range, normally equal to storage cost per month.

## Hedging via the basis

A producer or consumer of commodities lives in the basis. Suppose a copper mine knows it will produce 1,000 tonnes in six months. It can hedge by selling a six-month forward or futures contract *today*, locking in a price. That price is the current spot price plus the basis for a six-month contract. If spot is $9,000 per tonne and the basis (six-month futures above spot) is $300, the miner locks in $9,300. Come month 6, the mine digs up copper, sells it at *whatever spot is then*, and realizes profit or loss relative to $9,300.

This hedging works only because the basis can be estimated with reasonable certainty. A miner betting on the basis—expecting it to widen or narrow in a way that beats the consensus—is speculating on supply and demand, not just locking in price. Most producers and consumers try to hedge *at* the consensus basis, not gamble against it.

Refiners and utilities do the same. A refiner knows it will need crude six months out; buying the six-month contract locks in spot-plus-basis. A power plant burning natural gas for winter heating can buy a strip of winter [futures contracts](/futures-contract/) locking in the full cost of heating fuel based on current prices and the known contango (positive basis) curve.

## Basis risk in hedging

Even though the basis converges to zero, there's still a risk called basis risk. A miner hedging copper production six months out assumes the basis today accurately predicts the basis six months later. But if supply conditions shift—a sudden glut or a strike at a competing mine—the basis could widen or flip. The miner might have locked in a price that looks rich in six months, or one that looks cheap. The basis, though anchored by arbitrage in the final days before expiration, can surprise hedgers months earlier.

Basis risk is smaller than the risk of unhedged price swings, but it's real. This is why farmers and producers often layer hedges—selling some far-dated contracts (betting the current basis is fair) and rolling forward closer to harvest, adjusting as the market evolves.

## Local bases and logistics

The spot-futures basis is technically the gap between a standardized delivery point (the exchange delivery location) and the *generic* spot price. In reality, physical commodity prices vary by location, quality, and logistics. Crude at Cushing, Oklahoma, is cheaper than crude at Rotterdam due to shipping; there's a "location basis." Corn at a Kansas elevator is cheaper than corn at a Gulf export terminal. These local bases are determined by transport costs and supply gluts or tightness at each node.

A trader paying attention to the formal spot-futures basis might miss huge local opportunities. An oil trader noticing that Brent crude (North Sea) basis is slightly positive might miss a wider arbitrage if West Texas Intermediate (WTI) basis is deeply negative, signalling supply stress at Cushing. Most professionals monitor dozens of basis spreads simultaneously.

## Non-convergence and delivery substitution

The basis must converge to zero *at* contract expiration, but the contract specifications sometimes allow substitute deliverables. A corn futures contract might accept corn at any of several grades; a crude contract might accept several benchmarks. The cheapest-to-deliver grade often trades at a deep discount to the benchmark, creating a basis "tail" for traders who deliver the cheaper grade into an expensive contract.

Conversely, in some markets (silver, gold) the cash and futures markets are slightly divorced—not every holder of physical metal can economi fully access the futures contract infrastructure. Small regional spot prices can deviate from the futures basis in ways that take weeks to arbitrage away. But for liquid, widely-held commodities (crude, natural gas, corn, soybeans), the basis is tight and predictable.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the standardised delivery instrument whose price drives the basis
- [Nearby-deferred spread](/nearby-deferred-spread/) — the gap between front-month and later-month futures, complementary to spot-basis
- [Contango](/contango/) — positive basis (futures above spot) when supply is ample
- [Backwardation](/contango/) — negative basis (spot above futures) when supply is tight
- [Futures strip pricing](/futures-strip-pricing/) — valuing a position across a sequence of expirations
- [Forward curve](/forward-curve-inversion/) — the full term structure of prices and bases across all expiration dates
- [Price discovery](/price-discovery/) — how spot and futures prices reveal market expectations

### Wider context

- [Crude oil](/crude-oil/) — a major commodity whose basis shapes refinery economics
- [Natural gas](/natural-gas/) — a seasonal commodity with sharp basis swings
- [Corn](/corn/) — agricultural commodity whose basis reflects harvest timing and storage
- [Hedging](/interest-rate-risk/) — using basis-aware futures to lock in commodity costs

</div>

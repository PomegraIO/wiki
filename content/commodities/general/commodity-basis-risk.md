---
title: "Basis Risk in Commodity Hedging"
description: "Commodity basis risk is the divergence between the local spot price and exchange futures price, leaving residual exposure even after hedging."
keywords:
  - commodity basis risk
  - basis risk
  - hedge risk
  - commodity hedging
  - basis convergence
  - imperfect hedges
---

*A producer of wheat or oil who sells a [futures contract](/futures-contract/) to lock in price faces **basis risk**: the difference between the local cash price at the elevator or refinery and the standardized exchange futures contract they shorted. That gap can widen or narrow unexpectedly, leaving the hedger exposed to loss even after paying for the hedge. Understanding basis risk is the difference between a partial and a true risk transfer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Commodity Basis Risk — Key Facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">The residual price gap that persists even after locking in a futures hedge.</div>

|   |   |
|---|---|
| **Definition** | Local spot price minus futures price (or vice versa); the "gap" in a hedge |
| **Cause** | Transportation, quality, timing, and location premiums/discounts relative to contract specs |
| **Typical values** | 5–20% of spot price, depending on commodity and location |
| **At contract expiry** | Basis converges to near-zero (spot and futures must meet) |
| **During contract life** | Basis can widen (bad for short hedgers) or narrow (good for short hedgers) |
| **Hedging benefit** | Reduces but does not eliminate price risk; swaps price risk for basis risk |

</aside>

## The Problem: Spot and Futures Are Not the Same Price

A soybean farmer in Iowa and a crude oil producer in South Texas both face a problem: the commodity they sell locally trades on an exchange miles away, in standardized contracts, with terms they may not match perfectly.

The CBOT soybean futures contract specifies #2 yellow soybeans delivered at certain Midwest shipping points. An Iowa farmer's beans might be #1 or #3, at a different moisture level, and their location may impose $0.15 to $0.30 per bushel to transport to contract points. The difference—local price minus futures price—is the basis.

For crude oil, the WTI (West Texas Intermediate) contract is priced at Cushing, Oklahoma. A producer in the Permian Basin faces $2–5 per barrel in transportation, quality adjustment, and differential to deliver to Cushing. That producer's local price is typically below WTI futures.

Basis is not bad in itself; it simply reflects real costs and frictions. But when a farmer sells soybean futures to lock in revenue, the farmer is not locking in the local cash price—they are locking in a basis-adjusted price. If basis widens (local premium shrinks), the farmer loses; if basis narrows, they gain.

## Why Basis Changes

Basis is not constant. It shifts with seasonal supply, transportation costs, local demand, and the spread between spot and futures markets.

**Seasonality.** After harvest, local supplies are abundant and basis widens (local price drops relative to futures). As the crop year advances and local supplies are consumed or exported, basis narrows. A farmer who sells futures immediately after harvest locks in a wider basis discount than one who sells in spring.

**Transportation and congestion.** If elevators fill up or transportation is congested, the basis widens (discount deepens) because the commodity is less valuable at its current location. Conversely, if storage is available and transport is fluid, basis tightens.

**Quality and location spread.** A commodity of lower grade or at a farther distance trades at a wider discount. If demand shifts toward a commodity of higher quality or nearer location, the basis for that commodity narrows.

**Futures price moves vs. spot moves.** The futures price (settled at contract points) and the local spot price can move at different rates. If a harvest report crashes the futures price, local elevators may not immediately lower their bid, causing basis to widen momentarily. As they adjust, basis narrows again.

## Basis Risk in a Hedge

A farmer who shorts corn futures to hedge owns physical corn and owes futures contracts. At harvest, they sell physical corn locally and buy back futures. The gain or loss on futures partially offsets the loss or gain on the physical sale.

If the farmer locked in a basis of −$0.30 (local price $0.30 below futures), they expect to collect that basis at harvest. But if basis has widened to −$0.50 by harvest time, the farmer loses an extra $0.20 per bushel, even though they hedged. Conversely, if basis narrowed to −$0.15, the farmer gains an extra $0.15.

This is basis risk: the hedge eliminates commodity price risk (the absolute level of corn prices), but the residual gap between futures and local prices remains and can move against the hedger.

## When Basis Risk Matters Most

Basis risk is smallest for major commodities at contract delivery points. Corn and soybeans at major Midwest elevators near CBOT delivery points have tight basis because of arbitrage. Any large basis divergence triggers buying or selling that closes it.

Basis risk is largest:

- **Far from delivery points.** A cattle rancher in Montana faces wider basis risk than one in the Great Plains near live cattle futures delivery.
- **For non-standard grades or qualities.** A producer of specialty coffee or cocoa cannot directly arbitrage NYBOT contracts.
- **In illiquid local markets.** A small producer with few buyers faces a wider bid-ask spread (a form of basis).
- **For long-term hedges.** Basis can be stable over weeks but unstable over months or years.

## Basis Convergence at Expiration

One certainty: basis converges to zero (or very near zero) at futures contract expiration. On the last trading day of a contract, the cash price and the settlement price must be essentially equal, because anyone holding a futures contract to expiration is obligated to deliver physical commodity at the contract price. The arbitrage between futures and cash eliminates any gap.

This is why a long-dated hedge faces higher basis risk. If a farmer has six months to go before they harvest and sell, basis could widen or narrow significantly. But within days of contract expiration, basis is pinched to a narrow band.

## Basis Strategies and Monitoring

Experienced commodity producers monitor basis actively. They may:

- **Delay hedging** to wait for favorable basis. If basis is unusually wide, they might wait to sell futures when basis tightens.
- **Scale into hedges** rather than hedging 100% at once. This reduces the risk that they lock in an unfavorable basis.
- **Choose different contracts or delivery months** that offer tighter basis. Deferred futures contracts may have wider or narrower basis depending on expected supplies.
- **Use basis contracts** (also called "basis deals") with local elevators or merchants. The elevator quotes a basis level, and the farmer sets the futures price later. This unbundles the basis from the commodity price.

## Basis Risk vs. Price Risk

Hedging swaps price risk for basis risk. A farmer without any hedge faces full commodity price risk (if prices fall, revenue falls). With a hedge, the farmer's revenue is stable, but it depends on how basis moves. 

In most cases, basis risk is smaller and more predictable than commodity price risk. A price swing of 20% in corn is common; basis typically moves 2–5%. But basis can behave unexpectedly, and for a hedger, unexpected means uncompensated.

## See also

<div class="wiki-seealso">

### Closely related

- [Basis](/basis/) — The theoretical definition and general application across markets
- [How commodity ETFs track prices](/how-commodity-etfs-track-prices/) — How tracking divergence arises in passive structures
- [Storage costs and commodity futures pricing](/commodity-storage-costs-futures-pricing/) — How carrying costs shape the futures-spot gap
- [Soft commodities vs hard commodities](/soft-commodities-vs-hard-commodities/) — Why soft commodities have wider, more seasonal basis
- [Futures contract](/futures-contract/) — The standardized contracts that underlie commodity hedges
- [Contango](/contango/) — When far-month futures trade above near-month, affecting hedging costs

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — Broad framework for using derivatives to manage risk
- [Forward contract](/forward-contract/) — Over-the-counter alternative to futures; avoids standardization risk
- [Counterparty risk](/counterparty-risk/) — The risk that the futures clearinghouse may fail (rare but real)
- [Volatility](/volatility-smile/) — How commodity price swings create hedging demand
- [Interest rate risk](/interest-rate-risk/) — Similarly, interest rate basis risk affects fixed-income hedges

</div>

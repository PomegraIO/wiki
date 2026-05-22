---
title: "Final Settlement"
description: "The process at contract expiration when a futures or forward contract is resolved by cash payment or physical delivery—the final adjustment determining profit or loss."
keywords:
  - settlement
  - contract expiration
  - futures delivery
  - cash settlement
---

*The **Final Settlement** of a [futures](/wiki/futures-contract/) or [forward contract](/wiki/forward-contract/) is the mechanism by which the contract is discharged at expiration. For most financial futures (stock indexes, bonds, currencies), settlement is *cash*: the contract is marked-to-market one final time, and the profit or loss is cash-settled between the long and short. For commodity futures (crude oil, wheat), settlement can be either cash or *physical delivery*: the seller delivers the actual barrels or bushels of the commodity to the buyer, with the buyer wiring payment. Forward contracts, being customized and settled OTC, are resolved according to their specific terms—usually the fixed-price settlement on the maturity date.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **When it occurs** | At contract expiration date or maturity |
| **Cash settlement** | Final P&L is netted; winner receives payment from loser; position is closed |
| **Physical delivery** | Seller delivers underlying asset; buyer receives it and pays the agreed price |
| **Expiration date** | Typically the third Friday of the contract month (equity futures); varies by commodity |
| **Settlement price** | The final price used to calculate the cash difference between parties |
| **Delivery period** | Some commodity contracts allow delivery over a range of days; others on a fixed date |
| **Clearing house role** | [CCP](/wiki/central-counterparty-clearing/) guarantees settlement; steps between parties to manage credit risk |
| **Variation margin** | Final daily mark-to-market adjustment; largest single P&L realization day |

</aside>

## How cash settlement works

An S&P 500 index futures contract (SPY futures) expires on the third Friday of each month. Suppose you purchased a December 2024 SPY futures contract at 4800, and at expiration it is trading at 4850. Your profit per contract is 50 points, which equals $250 per contract (each point is worth $100 in the SPY contract).

On the final day:
1. The [clearing house](/wiki/clearing-firm/) marks your position to market using the settlement price.
2. Your account is credited $250 per contract.
3. The short's account is debited $250 per contract.
4. The position is automatically closed; you no longer own the December contract.

No delivery of the underlying S&P 500 stocks occurs. The contract is purely financial. This is how nearly all equity index, bond, and currency futures settle in the US and most developed markets.

## Physical delivery and the delivery window

Commodity futures contracts can settle by physical delivery. A crude oil futures contract (WTI) expiring in January allows the short to deliver barrels of crude oil to the buyer at the agreed futures price during a specified delivery period (typically the first 10 days of the expiration month). The buyer must accept delivery and pay the futures price, even if the market price has fallen.

Not all shorts actually deliver. In fact, most commodity futures positions are closed before expiration (rolled forward or liquidated) precisely because physical delivery is expensive and logistically complex. Delivery requires:
- Storage and transportation of the physical commodity
- Quality certification (for commodities, the seller must deliver an approved grade)
- Loading and unloading costs
- Insurance and potential spoilage

Only a tiny fraction—typically 1–3%—of open interest in commodity contracts results in actual delivery. The rest close out for cash.

## The settlement price and daily limits

The settlement price is determined by the exchange rules, usually based on the last trade of the day or a calculation from the order book at expiration. Some exchanges use a volume-weighted average price (VWAP) over the final minute of trading or final 30 seconds.

Leading up to expiration, prices can move in large jumps due to basis risk, delivery logistics, and algorithmic positioning. Daily price limits (circuit breakers) may limit the maximum move to prevent chaos. If the opening is so far away from the previous day's close that it would exceed the daily limit, the exchange may halt trading and expand the limit.

## Delivery mechanics: the commodity example

Suppose you are long a crude oil futures contract (1,000 barrels). The short issues a *notice of intent to deliver* (usually 2–5 days before the actual delivery date). You must then:
1. Designate a receiving point (pipeline, tank farm, dock).
2. Arrange storage and insurance.
3. Verify the crude quality (API gravity, sulfur content, etc.).
4. Wire payment for 1,000 barrels at the futures price (e.g., $80/barrel = $80,000).

The seller delivers the crude to your designated location, and title transfers. Delivery is final; you cannot refuse or re-sell back to the seller (except by entering an opposite futures position and letting the exchange match new longs and shorts).

## Roll forward and avoiding expiration

Most professional traders and funds do not want to physically receive commodities or deliver them. Instead, they *roll* their positions before expiration: they sell the nearby contract (January) and buy the further-out contract (February or March) at the market spread between them. This resets their position to a later expiration date without ever touching the spot market or triggering delivery.

Retail traders can also roll, but they must do so explicitly—exchanges automatically close out positions at expiration. If you hold a January crude oil contract and do nothing, you will be either forced to deliver (if you are short) or forced to accept delivery (if you are long). Brokers typically send loud warnings: "Your contract expires in 5 days; you must roll or exit your position."

## The settlement spread (basis) and delivery arbitrage

The *basis* is the difference between the futures price and the spot (immediate) price of the underlying commodity. As a futures contract approaches expiration, the futures price converges to the spot price because delivery is imminent; traders who are short can no longer claim future costs (storage, convenience yield) as justification for a discount.

This convergence is so predictable that it creates a *cash-and-carry arbitrage*: buy the spot commodity, sell the futures contract, finance your position at the repo rate, and at expiration, deliver against the futures. The profit is locked in at inception. This arbitrage is one of the most reliable in finance, and it is the mechanism by which futures prices are anchored to spot prices.

## Corporate actions and contract adjustments

If a [stock split](/wiki/stock-split/) or [dividend](/wiki/dividend/) occurs before futures expiration, the exchange adjusts the contract terms. For example, if an S&P 500 component pays a large special dividend, the index drops, and the index futures are adjusted downward to reflect the fact that the cash dividend was paid out but is not part of the index return.

Adjusted futures contracts are less liquid, and some traders are forced to flatten or accept the adjustment loss. These adjustments are why it is important to understand contract specifications before entering a position.

## Settlement failures and default

Since the [2008 financial crisis](/wiki/lehman-brothers-collapse/) and the [2020 March melt-down](/wiki/march-2020-vix/), exchanges and clearing houses have been hyper-vigilant about settlement risk. The [DTCC](/wiki/dtcc/) and [LCH.Clearnet](/wiki/lch-clearnet/) have watchers monitoring large positions and margin adequacy. If a trader's account falls below minimum margin, the [clearing firm](/wiki/clearing-firm/) (the broker) is forced to liquidate positions immediately, which normally settles within 24 hours.

Outright default is now rare because central counterparties (the clearing house) step into any default and use the defaulter's collateral to cover losses. This is the main achievement of post-2008 financial regulation: [central counterparty clearing](/wiki/central-counterparty-clearing/) makes settlement nearly risk-free from the perspective of non-defaulting parties.

## Same-day settlement vs. T+1 vs. T+0

Most equity and bond futures settle *same day* (T+0, often intraday). Commodity futures often settle T+1 (one business day after expiration) because physical delivery logistics take time. Currency forwards settle T+2 typically (two business days after the fix date), the global standard for [FX settlement](/wiki/settlement-cycles/).

Faster settlement (T+0) means less credit risk and lower capital requirements for both trader and broker, but it requires higher operational sophistication.

<div class="wiki-seealso">

### Closely related
- [Futures Contract](/wiki/futures-contract/) — Overview of futures mechanics and terms
- [Forward Contract](/wiki/forward-contract/) — OTC contracts with similar settlement logic
- [Cash Settlement](/wiki/cash-settlement/) — The standard settlement method for index and financial futures
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — The role of the CCP in guaranteeing settlement

### Wider context
- [Commodity Futures Rolling](/wiki/commodity-futures-rolling/) — How to roll forward before expiration
- [Settlement Cycles](/wiki/settlement-cycles/) — The timeline for trade settlement across different asset classes
- [Basis](/wiki/basis/) — The spread between futures price and spot price at expiration
- [Clearing Firm](/wiki/clearing-firm/) — The broker that guarantees your settlement with the exchange

</div>

---
title: "Futures Basis: What It Is and Why It Changes"
description: "Define basis as the difference between spot and futures prices, trace how it converges at delivery, and explain basis risk for hedgers."
keywords:
  - futures basis explained
  - basis convergence futures
  - spot futures price difference
  - basis risk hedging
  - contango backwardation
image: "/svg/derivatives.svg"
---

*The basis in futures markets is the difference between the spot price (the current market price for immediate delivery) and the [futures price](/futures-contract/) (the price for delivery at a future date). Basis converges to zero at the contract's delivery date because the futures price and spot price must be equal when the contract matures. Understanding basis is critical for hedgers because changes in the basis—not just changes in the underlying price—determine their hedging effectiveness.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Basis — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and hedging." />

<div class="wiki-infobox-caption">Basis shrinks to zero as the futures contract approaches delivery.</div>

|   |   |
|---|---|
| **Definition** | Basis = Spot Price − Futures Price |
| **At delivery** | Basis converges to zero (spot and futures are identical) |
| **When positive** | Spot > futures (backwardation; contango is negative basis) |
| **When negative** | Futures > spot (contango; futures trading at a premium) |
| **Drivers** | Carry costs, storage, insurance, interest rates, convenience yield |
| **Basis risk** | Hedger loses if basis widens unexpectedly; wins if basis narrows |
| **Example contract** | Crude oil: Dec futures trade at discount to spot; Jan forward trades higher |

</aside>

## What Basis Is and Why It Exists

Imagine crude oil trading at $80 per barrel today. But oil futures maturing three months from now trade at $82. The difference—$2—is the basis. Because oil cannot be instantaneously transported or stored cost-free, the futures price reflects not just expected future spot prices but also the cost of physically holding oil from today until delivery.

This cost includes:
- **Storage costs**: Warehousing the oil.
- **Insurance**: Covering the barrel against loss or damage.
- **Financing costs**: The interest rate to borrow money to pay for the oil while it sits in storage.
- **Convenience yield**: The value of having oil on hand now rather than later (refineries value immediate supply).

These costs are collectively called "carry." If carry is positive (storage and financing cost more than the convenience yield), the futures price will be higher than the spot price. If carry is negative (convenience yield exceeds costs), the futures price will be lower.

Mathematically:
Futures Price ≈ Spot Price + Carry Costs − Convenience Yield

Rearranging:
Basis = Spot Price − Futures Price ≈ Convenience Yield − Carry Costs

## Basis Convergence at Delivery

The most important property of basis is that it *must* converge to zero at the contract's delivery date. Here is why:

On the last day a futures contract is traded (the "last trading day"), the futures price and spot price must be equal. If the futures traded at $82 and the spot price was $80, anyone could:
- Buy the spot commodity at $80.
- Sell the futures contract at $82.
- Lock in a $2 profit with no risk.

This "cash-and-carry" arbitrage would force prices to converge. Similarly, if spot were higher than futures, traders would buy futures and sell spot, pushing the basis back toward zero.

In practice, the futures price typically converges to spot within the last few trading days before delivery, as the opportunity for arbitrage becomes acute. By the final settlement, basis is effectively zero (or within the [bid-ask spread](/bid-ask-spread/)).

This convergence property is *definite*, unlike the spot price itself, which is uncertain. A hedger cannot predict whether crude will be $75 or $85 in three months, but can be certain that the three-month futures price will equal the three-month spot price on delivery day. This certainty is part of what makes futures useful for hedging.

## Contango and Backwardation

When the futures price is higher than the spot price, the market is in **contango**. The basis is negative. This is the "normal" state for most commodity futures when carry costs exceed convenience yield. Crude oil, natural gas, and grain futures often trade in contango, particularly when storage is plentiful and interest rates are low.

When the futures price is lower than the spot price, the market is in **backwardation**. The basis is positive. This typically signals tight supply—the convenience of having the commodity now is worth more than the cost of storing it. During supply shocks (a refinery outage, a hurricane disrupting oil production), oil futures flip into backwardation.

The distinction matters for hedgers. A producer of crude oil (like an oil company) wants to sell futures to lock in a price. In contango, selling the March futures contract at $82 when spot is $80 looks attractive—the producer gets a premium. But if the producer actually sells physical oil in March, the spot price at that time might have fallen to $75. The futures hedge locked in $82, so the producer profits $7 compared to the March spot. In contango, the hedge works well.

In backwardation, the futures trade at a discount. The producer would receive less selling the March futures ($78) than the current spot ($80). Over time, basis converges, and the futures price at March delivery will equal the March spot price. But in the interim, the producer has locked in a lower price, which might seem unattractive. However, if the producer's actual sale must occur in March, the futures contract ensures the producer gets the March spot price, whatever it is—eliminating the uncertainty of spot-price moves.

## How Basis Changes Create Hedging Risk

This is where basis risk enters. A perfect hedge would fully offset price moves. But because the basis itself can change unpredictably, hedges are often imperfect.

**Example: An airline fuel hedge**

An airline uses heating oil futures to hedge jet fuel price risk. The airline buys heating oil futures to lock in a fuel price. Jet fuel and heating oil are similar but not identical; they trade in related but separate markets. The relationship between jet fuel spot and heating oil futures is not fixed. If the relationship tightens (jet fuel appreciates relative to heating oil), the futures hedge becomes more valuable. If it widens (jet fuel appreciates less than heating oil), the hedge underperforms.

This is basis risk in the cross-commodity case. The airline's actual commodity (jet fuel) trades at a basis to the futures contract (heating oil). Basis changes alter the hedge's effectiveness.

**Example: A wheat farmer's harvest hedge**

A farmer plants wheat expected to harvest in July. In May, the farmer buys July wheat futures at $6 per bushel to lock in a price. Two months later, at harvest, spot wheat trades at $5.80. The farmer expected to sell at $6 but the market is at $5.80. However, July futures also trade at $5.80 at harvest (convergence). The farmer delivers against the futures contract and receives $6 (the locked-in price), not $5.80. The futures offset the spot loss, so the hedge works perfectly.

But suppose the farmer can only sell the wheat in the cash market and cannot make delivery on the July contract. The farmer closes the July futures contract (selling it at $5.80) and simultaneously sells the physical wheat. The loss on the futures contract ($6 − $5.80 = $0.20/bushel) is offset by the gain in the cash market (because the farmer would have sold at $5.80 anyway). Again, a perfect hedge.

Now suppose the farmer's wheat is a specific variety (e.g., hard red winter wheat) that trades at a $0.10 discount to the generic "soft red winter wheat" futures contract. Spot hard red winter wheat is $5.70, while soft red winter futures trade at $5.80. The basis (hard red winter spot minus soft red winter futures) is −$0.10. The farmer closes the futures, receiving $5.80, and sells physical wheat at $5.70. The cost of the basis is $0.10/bushel—the farmer's hedge does not fully protect against the price move because of the quality mismatch.

This is **basis risk**: the hedge fails because the actual commodity's basis to the futures contract changes or is not zero.

## Drivers of Basis Changes

Basis is not fixed; it varies based on market conditions:

1. **Interest Rates**: Higher rates increase carry costs, widening the basis. Lower rates narrow it.
2. **Storage Availability**: Tight storage pushes futures lower (backwardation, negative basis). Abundant storage pushes futures higher (contango, positive basis).
3. **Seasonal Patterns**: Agricultural futures typically have negative basis (backwardation) at harvest when supply is plentiful, and positive basis (contango) later in the year as stored supplies deplete.
4. **Supply Shocks**: A sudden supply disruption increases the convenience yield (because scarcity is valuable), pushing spot higher relative to futures (backwardation).
5. **Relative Quality**: If two commodities are close substitutes (heating oil vs. crude oil), basis between them reflects their relative supply-demand dynamics.

A hedger who does not account for basis changes will be surprised by imperfect hedges.

## Basis in Practice: Working Example

Suppose a soybean processor needs to buy soybeans in September and wants to hedge the price today (June). June spot soybeans trade at $13.50/bushel. September soybean futures trade at $13.30 (contango, negative basis of $0.20). The processor buys September futures at $13.30.

Between June and September, several things could happen:

**Scenario A: Spot falls to $13, futures fall to $12.80**
- Basis: $13 − $12.80 = $0.20 (unchanged)
- Processor closes futures at loss of $0.50/bushel ($13.30 − $12.80)
- But spot is now $13, so buying in the cash market would cost $13, not $13.50
- The futures loss ($0.50) roughly equals the spot gain ($0.50 relative to the $13.50 initial spot)
- Effective price: $13.50 − $0.50 = $13.00 (close to $13, the actual cash market price)

**Scenario B: Spot falls to $13, futures fall to $12.90**
- Basis: $13 − $12.90 = $0.10 (basis narrowed from $0.20 to $0.10)
- Processor closes futures at loss of $0.40/bushel ($13.30 − $12.90)
- Spot is $13, but the hedge only offset $0.40, leaving the processor with $0.10 of unhedged loss
- Effective price: $13.50 − $0.40 = $13.10 (vs. the $13 cash spot)

In Scenario B, the basis change (from $0.20 to $0.10) created a $0.10/bushel drag on the hedge. This is basis risk.

## Managing Basis Risk

Hedgers cannot eliminate basis risk entirely, but they can measure and manage it:

1. **Monitor Historical Basis**: Track the basis between the actual commodity and the futures contract over time. If hard red winter wheat typically trades at a $0.10 discount to soft red winter futures, the farmer can forecast that cost.

2. **Use Stacked Hedges**: Instead of one far-distant futures contract, some hedgers buy a series of nearer-term contracts and roll them forward. This can reduce basis risk by keeping the hedge closer to the spot market.

3. **Cross-Hedge Optimization**: If the exact commodity is not futures-tradeable, choose the futures contract with the most stable basis. For example, an airline might choose [crude oil](/crude-oil/) futures over heating oil if the airline's fuel blends are closer to crude.

4. **Accept Basis Risk as a Trade-off**: Sometimes a partial hedge is acceptable. The farmer might accept $0.10/bushel of unhedged risk in exchange for locking in most of the price and eliminating uncertainty.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — Mechanics and uses of futures
- Carrying Costs — Storage, insurance, and financing costs that drive basis
- [Contango and Backwardation](/contango/) — Market structure and basis direction
- [Hedging](/derivatives-hedging/) — Using futures to manage price risk
- Arbitrage — How cash-and-carry arbitrage enforces convergence

### Wider context

- Commodity Markets — Physical and derivative trading
- [Interest Rate Risk](/interest-rate-risk/) — How rates affect carry and basis
- [Operational Risk](/operational-risk/) — Execution and settlement in hedging programs
- [Derivatives](/derivatives-hedging/) — Overview of forwards, futures, swaps, and options

</div>

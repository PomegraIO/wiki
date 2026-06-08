---
title: "Contango vs Backwardation for Hedgers"
description: "How contango and backwardation affect hedgers differently: buyers and sellers face opposite profit/loss scenarios when rolling futures. Critical for cost planning."
keywords:
  - contango vs backwardation
  - hedging futures
  - futures market structure
  - roll cost
  - producer consumer hedging
image: "/svg/derivatives.svg"
---

*When a producer hedges with [futures](/futures-contract/), rising prices hurt the cash position but profit the hedge. When the [futures market](/futures-contract/) is in [contango](/contango/)—near-term prices are lower than deferred—the hedger bleeds cost every time they roll forward to maintain the hedge. In [backwardation](/backwardation/), the arithmetic works the opposite way. Understanding the market structure is essential to hedge design because it determines whether you are paying or collecting carry.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contango vs Backwardation for Hedgers — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Hedgers in contango pay roll costs; hedgers in backwardation collect them. Market structure, not volatility, drives the outcome.</div>

|   |   |
|---|---|
| **Contango** | Near-term futures cheaper than deferred; storage and financing costs embedded in price curve |
| **Backwardation** | Near-term futures expensive; scarcity or convenience yield causes deferred prices to be lower |
| **Producer in contango** | Shorts near-term futures; rolls forward into higher prices; locks in losses on the roll |
| **Producer in backwardation** | Shorts near-term; rolls into lower-deferred prices; collects a gain on the roll |
| **Consumer in contango** | Longs near-term; rolls into higher prices; collects a gain on the roll |
| **Consumer in backwardation** | Longs near-term; rolls into lower prices; bleeds cost on the roll |
| **Economic driver** | Storage costs, financing, convenience yield (scarcity premium) |
| **Time decay** | Contango embeds a "cost of carry"; backwardation embeds a "value to hold" |

</aside>

## The Basic Setup

Imagine an airline that burns 500,000 barrels of jet fuel each month. In January, they fear fuel prices will spike by summer, so they hedge: they buy six months of [futures contracts](/futures-contract/) on crude oil and refined products.

Now imagine a farmer who will harvest 10,000 bushels of corn in August. In February, fearing a price collapse at harvest, the farmer sells August corn futures to lock in a price.

Both are hedgers. Both want to eliminate [market risk](/market-risk/) on their cash position. But they are on opposite sides of the futures market, and they face opposite economic outcomes depending on whether the market is in [contango](/contango/) or [backwardation](/backwardation/).

## Contango: The Hedger's Tax on Deferred Exposure

In [contango](/contango/), prices rise with time to maturity. A June crude contract costs more than a March contract. An August corn contract trades above the May delivery.

This price structure embeds the cost of storage, financing, and insurance. If physical crude costs $70 to store for three months, the June contract will trade roughly $70 higher than March (all else equal). This is not speculation; it is the arithmetic of physical ownership.

**For a producer in contango:**

The farmer sells August corn at, say, $5.00. If August futures were trading in contango above the May contract, this is the *most expensive* contract on the curve.
- May contract: $4.85
- August contract: $5.00
- Difference: $0.15 (contango premium)

When August arrives, the farmer is locked in at $5.00. But six months earlier, they could have sold May instead. If they had, they would have re-hedged in May, selling a new August contract and buying back May. That roll would have cost them $0.15 per bushel—exactly the contango.

**The rule:** *A producer in contango loses on every roll forward because they are selling into a market where deferred prices are higher. They are locking in tomorrow's prices at today's storage costs.*

**For a consumer in contango:**

The airline buys March crude at $70. In two months, they need to roll to a May contract at $72 (contango). They sell the March contract (now worth $71, having rolled down) and buy May at $72. The net cost of rolling: $1 per barrel, paid by the consumer.

But the consumer *benefits* because they are holding a long position. They bought cheap March, and they can roll forward and "let the contango work for them"—they lock in June deliveries at rising prices, which offsets some of the damage if spot prices fall.

**The rule:** *A consumer in contango gains on every roll forward because deferred prices are higher, and they own the near-term. On roll, they sell high and buy higher (but locks in delivery at that higher price).*

## Backwardation: The Reverse Economics

In [backwardation](/backwardation/), near-term prices are higher than deferred. This happens when physical supply is tight or when the market fears near-term shortage. There is a "convenience yield" to holding physical inventory.

**For a producer in backwardation:**

The farmer sells August corn, but August is cheap—say $4.80—while May futures (deferred relative to March) are even cheaper at $4.75.
- March contract: $4.90 (near-term scarcity premium)
- August contract: $4.80 (deferred, cheaper)

The farmer is now locked in at the worst price on the curve (August is deferred and cheap). But every roll forward, the farmer is rolling *from an expensive month into cheaper months*, collecting the backwardation.

If they had to re-hedge and could roll to a June contract at $4.82, they would collect $0.08. Backwardation is a gift to producers because deferred prices rise (toward near-term), and the producer profits on the roll.

**The rule:** *A producer in backwardation gains on every roll forward because deferred prices are lower, and they are selling into a market where the near-term is expensive. Rolling forward collects the backwardation spread.*

**For a consumer in backwardation:**

The airline buys March crude at $75 (near-term premium). Two months later, they roll to May at $73 (backwardated market). They sell March at $76 (having stepped down) and buy May at $73. Cost of rolling: $2.50 per barrel paid by the consumer.

The consumer is *hurt* by backwardation. They bought the expensive near-term contract, and rolling into deferred months forces them to buy cheaper futures, which means they lock in *lower* delivery prices. In a rising market, that is a loss.

**The rule:** *A consumer in backwardation loses on every roll forward because deferred prices are lower, and they own the near-term at a premium. Rolling forward forces them to sell low (relative to where they bought) and buy lower.*

## Contango vs Backwardation: Head-to-Head

| Scenario | Producer (short futures) | Consumer (long futures) |
|---|---|---|
| **In contango** | Loses on each roll; locks in storage costs; hedge becomes expensive | Gains on each roll; lets contango work for them; hedge becomes cheaper |
| **In backwardation** | Gains on each roll; collects scarcity premium; hedge becomes profitable | Loses on each roll; forced to buy into expensive near-term; hedge becomes expensive |

## The Economics Behind the Price Curve

Why does contango or backwardation happen?

**Contango** emerges when:
- Supply is abundant relative to immediate demand.
- Storage is economical (crude in tanks, grain in elevators, precious metals in vaults).
- Financing costs are low relative to spot prices.
- There is no urgent shortage.

The market is saying: "We have plenty now, and it costs money to store it, so deferred delivery is worth less because the holder pays storage."

**Backwardation** emerges when:
- Supply is tight or uncertain.
- Immediate delivery is valuable (a mill needs grain *now*, not in six months).
- Financing rates are high.
- There is scarcity or convenience yield.

The market is saying: "We are short now, and if you hold physical and deliver at the convenient moment, that is valuable. So near-term is expensive."

## Real-World Hedging Implications

**Oil hedging (often contango, sometimes backwardated):**
- In contango (typical), a producer selling crude futures loses $0.20–$0.50 per barrel on each quarterly roll. Over a year, that is $0.80–$2.00 per barrel of hedge cost.
- In backwardation (rare, during supply disruptions), producers *gain* $0.10–$0.30 per roll, and the hedge is self-financing.

**Agricultural hedging (structural backwardation in most crops):**
- Corn and soybeans are typically backwardated because harvest is seasonal. Old-crop (current year) is expensive; new-crop (next year) is cheap.
- A producer selling August futures locks in *deferred prices* (cheap) and rolls forward into expensive near-term contracts. They collect the backwardation on each roll.

**Precious metals (usually contango, but thinner):**
- Gold is often in mild contango (storage and insurance costs). A producer selling gold futures slightly loses on rolls.
- In sharp backwardation (rare, during geopolitical panic), producers gain.

## Hedging Strategy Adjustments

**When contango is steep (>2% annualized):**
- Producers should hedge longer-term deferred contracts directly (sell September instead of June, then hold). They accept basis risk but avoid the roll tax.
- Consumers should use near-term contracts and roll frequently; they collect contango on each roll.

**When backwardation is deep (>5% annualized):**
- Producers should use near-term contracts and roll; they collect on every roll.
- Consumers should hedge deferred months directly (buy September, hold) to avoid the roll cost.

**When the market is flat or transitions:**
- Use [rolling hedges](/futures-contract/) (near-term) and accept the roll mechanics as they come.
- Use longer-dated [forward contracts](/forward-contract/) or [swaps](/swap/) to eliminate roll risk entirely, though at a cost (the swap dealer charges for the risk).

## The Illusion of "Hedging at the Right Time"

Novice hedgers sometimes think "I will hedge when contango is shallow" or "I will wait for backwardation." This usually fails because:

1. Market structure is often mean-reverting. Deep contango attracts storage, which increases supply and flattens the curve. Deep backwardation attracts speculative long bets, tightening supply and reversing it.

2. By the time you notice contango is deep, futures markets have already priced it in, and the trend is likely to reverse soon.

3. Your operational risk (the spot price movement you are trying to hedge) is far larger than the roll cost. Hedging late to optimize contango can leave you unhedged in a market crash.

**The lesson:** Hedge your exposure when it arises. Accept contango or backwardation as part of the cost of doing business. Focus on the hedge ratio and duration, not on gaming the roll.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — Deferred prices higher than near-term; storage cost driver.
- [Backwardation](/backwardation/) — Near-term prices higher; scarcity or convenience yield driver.
- [Futures Contract](/futures-contract/) — The instrument hedgers use; mechanics of rolling and expiration.
- [Forward Contract](/forward-contract/) — Alternative to futures; one-time settlement, no roll risk.
- [Swap](/swap/) — Over-the-counter agreement to eliminate roll mechanics entirely.
- [Carry Trade](/carry-trade/) — Exploiting contango for profit, opposite of hedging.

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Broader framework for hedging with options, futures, and swaps.
- [Basis Risk](/basis-risk/) — Hedging with futures creates basis risk; the price curve and cash price may not move together.
- [Commodity Cycles](/business-cycle/) — Supply and demand cycles drive contango and backwardation patterns.
- [Interest Rate Risk](/interest-rate-risk/) — Financing costs embedded in contango; related to duration in bond hedging.

</div>

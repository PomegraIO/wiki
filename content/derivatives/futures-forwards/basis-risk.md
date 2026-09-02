---
title: "Basis Risk"
description: "The risk that the spot-futures spread (basis) changes unexpectedly, leaving a hedger worse off—the residual exposure that remains after locking in a futures price."
---

*A farmer hedges crop risk by shorting [futures](/wiki/futures-contract/). But they face a new risk: what if the [basis](/wiki/basis/) between spot and [futures](/wiki/futures-contract/) moves against them? This is basis risk—the risk that the hedge itself backfires.*

## What basis risk is

The [basis](/wiki/basis/) is the difference between spot and futures prices. For corn, if spot is $5.00 and December [futures](/wiki/futures-contract/) are $5.20, the [basis](/wiki/basis/) is -$0.20 (futures are $0.20 higher).

A farmer hedging plans: "I'll short December [futures](/wiki/futures-contract/) at $5.20. At harvest in October, I'll sell my corn at spot and buy back the [futures](/wiki/futures-contract/) to close my short. The [basis](/wiki/basis/) will lock in my revenue."

But [basis](/wiki/basis/) is not constant. It depends on storage costs, interest rates, convenience yields, and supply-demand expectations. As the contract approaches expiration, [basis](/wiki/basis/) typically converges to zero (futures price equals spot). But between now and December, the [basis](/wiki/basis/) can widen or narrow unexpectedly.

**Basis risk:** The risk that the [basis](/wiki/basis/) moves adversely, leaving the hedger worse off.

Example:
- Farmer shorts Dec futures at $5.20 when spot is $5.00 (basis = -0.20).
- In October, spot corn is $4.80 (down 4%), but Dec futures close at $5.10 (down 2%).
- New [basis](/wiki/basis/) is -0.30 (worse for the farmer).
- The farmer sells spot at $4.80 and covers the short at $5.10, locking in -$0.30 hedging loss plus the spot price.
- Revenue is $4.80 - ($5.10 - $5.20) = $4.90. But without hedging, revenue would have been $4.80. The hedge made them worse off by $0.10.

The farmer intended to lock in $5.20; instead, they locked in $4.90 because the [basis](/wiki/basis/) widened against them.

## Why basis changes

The [basis](/wiki/basis/) reflects [cost of carry](/wiki/cost-of-carry/): storage, interest to finance inventory, and convenience yield (the value of holding the physical).

**Storage costs shift:** Early season, when storage is empty, the [basis](/wiki/basis/) is typically tight (futures close to spot). As harvest approaches and warehouses fill, storage costs rise, widening the [basis](/wiki/basis/).

**Interest rates shift:** If the Fed cuts rates, financing inventory becomes cheaper, narrowing the [basis](/wiki/basis/). If rates rise, storage becomes more expensive, widening it.

**Convenience yields shift:** In tight supply years, holding physical inventory has high value (you can sell high-quality inventory at a premium). Convenience yield widens the [basis](/wiki/basis/). In abundant supply years, inventory is worthless; convenience yield falls, [basis](/wiki/basis/) tightens.

**Supply and demand expectations shift:** A crop report showing abundance will compress the [basis](/basis/) (the market expects more supply, making physical less valuable). A geopolitical shock that threatens supplies will widen the [basis](/wiki/basis/) (physical becomes more precious).

## Location and grade basis risk

Farmers do not all face the same [basis](/basis/). A farmer in Nebraska shipping to an Illinois elevator faces different logistics costs than a farmer in Iowa shipping locally.

The [futures](/wiki/futures-contract/) contract specifies delivery location(s). If the farmer is 500 miles from the nearest approved delivery point, they must transport their corn to deliver [futures](/wiki/futures-contract/), creating a location-specific [basis](/wiki/basis/].

Similarly, if the [futures](/wiki/futures-contract/) contract permits only "contract grade" corn (certain moisture, test weight, kernel uniformity), a farmer with slightly off-spec corn faces basis risk: they must either downgrade or accept a lower spot price than futures, widening their [basis](/wiki/basis/).

## Hedging with basis risk

Sophisticated hedgers manage basis risk by understanding it:

1. **Historical basis analysis:** A farmer might study historical [basis](/wiki/basis/) patterns for their location. "Over 10 years, Dec corn [basis](/wiki/basis/) in my county averages -0.25, with a standard deviation of 0.10." This gives them a sense of expected [basis](/wiki/basis/) and uncertainty.

2. **Partial hedges:** Instead of shorting [futures](/wiki/futures-contract/) equal to 100% of production, a farmer might short 70%, leaving 30% unhedged. This reduces [basis](/wiki/basis/) risk (the unhedged portion benefits from favorable [basis](/wiki/basis/) moves) while still capturing directional protection.

3. **Cross-hedging:** If a direct hedge does not exist, a farmer might hedge with a related contract. A farmer hedging beef might use [live cattle futures](/wiki/live-cattle/) (not a perfect match), accepting cross-hedge risk (the correlation between beef and cattle futures might break down).

4. **Roll timing:** A farmer planning to harvest in October but hedging December [futures](/wiki/futures-contract/) accepts a 2-month [basis](/wiki/basis/) risk. A savvy farmer might shift to selling spot in a forward contract with a local elevator instead, accepting only the immediate [basis](/wiki/basis/) (which is tighter because the transaction is imminent).

## Basis risk in energy and metals

Basis risk extends beyond agriculture. An airline hedging fuel costs with [heating oil futures](/wiki/heating-oil/) faces [basis](/wiki/basis/) risk: actual jet fuel prices move differently than heating oil [futures](/wiki/futures-contract/).

A copper mining company hedging production with copper [futures](/wiki/futures-contract/) faces location [basis](/wiki/basis/) risk (their mines are in Peru; [futures](/wiki/futures-contract/) are based on LME deliveries in London). They also face grade [basis](/wiki/basis/) risk: their ore produces 99.9% pure copper, while [futures](/wiki/futures-contract/) assume 99.5% purity. The premium for higher purity can widen or narrow, creating [basis](/wiki/basis/) risk even if [futures](/wiki/futures-contract/) prices are locked in.

## Basis convergence at expiration

One certainty: as a [futures](/wiki/futures-contract/) contract nears [expiration](/wiki/expiration-contracts/), [basis](/wiki/basis/) converges toward zero (the [futures](/wiki/futures-contract/) price equals spot, or equals delivery price if physical settlement). An arbitrageur can lock this in: buy spot, store, and deliver via [futures](/wiki/futures-contract/], earning the remaining [basis](/wiki/basis/) as profit.

This convergence means [basis](/wiki/basis/) risk is transient. A wide [basis](/wiki/basis/) is a temporary phenomenon. The question is: *when* do you need to settle? If you settle before convergence, you bear [basis](/wiki/basis/) risk. If you settle at [expiration](/wiki/expiration-contracts/), [basis](/wiki/basis/) risk is eliminated.

## The paradox: hedging creates new risk

Basis risk illustrates a core truth of hedging: **eliminating one risk often creates another.**

- **Without a hedge:** You face directional price risk (corn price falls 20%, you lose 20%). No [basis](/wiki/basis/) risk.
- **With a hedge:** You face [basis](/wiki/basis/) risk (the [basis](/wiki/basis/) widens, your hedge loses money). Directional risk is reduced but replaced.

The goal of hedging is to trade a large, scary directional risk for a smaller, more manageable [basis](/wiki/basis/) risk. If the hedge works as designed, [basis](/wiki/basis/) risk is the "noise"—a small residual uncertainty—while the directional move is captured.

But if [basis](/wiki/basis/) behaves unexpectedly (correlation breaks down, logistics shift, supply shocks), the hedge can fail, leaving you worse off than if you had gone unhedged.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/basis/">Basis</a> — the spot-futures spread, the source of [basis](/wiki/basis/) risk.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — storage, interest, and convenience yields that determine fair [basis](/wiki/basis/) levels.</li>
<li><a href="/wiki/hedging-with-futures/">Hedging with futures</a> — the risk management practice that creates [basis](/wiki/basis/) risk as a byproduct.</li>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the instrument used for hedging, introducing [basis](/wiki/basis/) risk.</li>
<li><a href="/wiki/forward-contract/">Forward contract</a> — alternative that may have different [basis](/wiki/basis/) risk characteristics.</li>
<li><a href="/wiki/commodity-contract-specifications/">Commodity contract specifications</a> — determine allowable grades and locations, affecting [basis](/wiki/basis/) dispersion.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li>Derivatives — the broader category of risk-transfer tools.</li>
<li>Risk management — the strategic context for accepting [basis](/wiki/basis/) risk as a trade-off for eliminating directional risk.</li>
</ul>
</div>

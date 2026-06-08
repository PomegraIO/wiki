---
title: "Basis Risk Explained with an Example"
description: "Basis risk is the mismatch between a hedging instrument and the exposure being hedged, illustrated through jet-fuel hedging for airlines."
keywords:
  - basis risk explained with example
  - basis risk definition
  - hedging mismatch
  - cross-hedge
  - imperfect hedge
image: "/svg/risk.svg"
---

*[Basis risk explained with example](/basis-risk-explained-with-example/) occurs when a company or investor uses a futures contract or other derivative to hedge an exposure, but the contract doesn't move in lockstep with the underlying asset being protected. The mismatch—the "basis"—leaves residual, unhedged loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The difference between hedging instrument and actual exposure creates lingering vulnerability.</div>

|   |   |
|---|---|
| **Definition** | Gap between the price movement of a [hedge](/basis/) and the price movement of the asset or liability being protected |
| **Root cause** | Imperfect correlation, different maturity, different grade or location, or thin futures contracts |
| **Common scenario** | An airline hedges [crude oil](/crude-oil/) futures when it really needs jet fuel; the two correlate strongly but not perfectly |
| **Residual loss** | Even if the hedge "works," the basis can widen or narrow, leaving unprotected profit or loss |
| **Real-world cost** | A 5% basis widening on a large position can be material enough to affect earnings or budget forecasts |

</aside>

## What basis risk is

A **basis** is the difference between the price of an asset in the [spot market](/spot-rate/) (the market for immediate delivery) and its price in a [futures contract](/futures-contract/) (the market for future delivery). When you hedge, you're betting those two prices will move together. But they don't always.

Basis risk is the probability and magnitude of loss from that bet failing.

Suppose an airline's costs depend on jet fuel—Jet A-1 delivered to its hub. But jet fuel futures are thin and expensive to trade in large volume. The airline instead buys crude oil futures, which are liquid and heavily traded. Crude oil and jet fuel are both petroleum products and move in the same direction, but they don't move by the same amount. A shock to refining capacity might widen the spread between crude and jet fuel. An unexpected drop in driving demand might narrow it. The airline's hedge works *most of the time*, but the basis—that gap—is where unprotected risk lives.

## The anatomy of a hedge

Perfect hedges exist only in textbooks. In practice, a hedger picks an instrument—a futures contract, a swap, an option—that correlates with the real exposure but may differ in:

- **Commodity grade or type.** Jet fuel vs. crude oil. Copper #2 grade vs. copper #1 grade.
- **Delivery location.** An industrial buyer in Chicago hedges with COMEX futures, which settle in New York. Transport costs and regional supply can create a basis.
- **Contract maturity.** A company needs to protect revenue three months out, but the nearest liquid futures contract expires in two. It rolls the contract forward, and the basis can shift during the roll.
- **Contract size.** A buyer needs to hedge 50,000 barrels; the futures contract is 42,000. The mismatch creates a small unhedged tranche.
- **Correlation strength.** Two assets move together *on average*, but diverge in tail scenarios. A [credit event](/credit-event-sovereign/) might spike funding costs for a bank while equity futures stay flat.

The wider these gaps, the wider potential basis losses.

## A worked example: airline jet-fuel hedge

An airline forecasts it will need 5 million gallons of jet fuel over the next four months. Current spot price is $3.10 per gallon; the airline fears a jump to $3.50. It wants to lock in a ceiling around $3.15.

Jet fuel futures are illiquid at the scale it needs. Instead, it buys [crude oil](/crude-oil/) futures: a commonly hedged approach, since jet fuel prices are driven by crude. One crude oil contract on COMEX represents 1,000 barrels (about 42,000 gallons). The airline needs about 120 contracts.

Current prices:
- Spot jet fuel: $3.10 per gallon
- Spot crude: $85 per barrel
- Crude futures (4-month out): $86 per barrel

The airline buys 120 crude futures at $86, locking in that crude price.

**Scenario A: Prices both rise**

Two months in, crude rallies to $95 per barrel. Jet fuel rallies to $3.45 per gallon. The airline's crude futures gain $9 per barrel × 42,000 gallons/contract × 120 contracts = $45.36 million gain on futures. Its physical jet fuel purchase costs $3.45 × 5 million = $17.25 million. Combined effective cost: ~$3.10 per gallon. The hedge nearly worked.

**Scenario B: Basis widens (the risk)**

Two months in, crude rallies to $95 per barrel, but jet fuel only rallies to $3.20 per gallon. A refinery closure takes crude offline, but increased imports cover jet-fuel demand. The airline's crude futures gain $9/barrel = $45.36 million. But its physical jet fuel costs only $3.20 × 5 million = $16 million. Combined effective cost: $3.32 per gallon—higher than the unhedged spot price two months earlier. The basis widened, and the hedge backfired.

This gap—the $0.22 per gallon unhedged loss—is basis risk realized.

## Why basis risk matters

Basis risk is often smaller than the risk being hedged. A company with no hedge faces the full upside and downside of price movement. A hedge with basis risk trades that exposure for a narrower, more predictable one. Over time, on average, the trade is favorable.

But basis risk can blow up in specific scenarios:

1. **Correlation breakdown.** In normal markets, crude and jet fuel move together. During a refinery strike, credit crunch, or supply shock, they can decouple violently.

2. **Tail events.** A [value-at-risk](/value-at-risk/) model might assume basis moves within historical bounds—say, ±5%. A tail event can push it to ±15%, wiping out savings from the hedge.

3. **Budget gaming.** A company hedges 80% of an exposure to save cost, planning to self-insure the basis. Market surprise swallows that 20%. This is a conscious trade-off—basis risk accepted in exchange for cheaper hedging—but it's still risk.

4. **Duration mismatch.** A borrower locks in rates on a two-year bond but has a five-year maturity. When it refinances, rates may have moved differently for the longer tenor, leaving basis exposure.

## Measuring and reducing basis risk

Basis risk cannot be eliminated without a perfect hedge—buying the exact asset, in the exact amount, at the exact time. Most practical hedges aim to *minimize* it:

- **Use the closest match.** If jet fuel futures exist and are liquid enough, use them instead of crude oil.
- **Scale the hedge.** Reduce the notional size of the futures to account for lower correlation or sensitivity.
- **Roll strategically.** Time the roll of expiring contracts to avoid rolling into a period of known basis volatility.
- **Cross-hedge calculation.** Use [regression analysis](/basis/) to estimate how much futures you need: if jet fuel moves $0.95 for every $1 crude move, buy 95% of the naive notional.
- **Diversify hedges.** Combine multiple instruments—some futures, some swaps, some operational (like fuel-efficiency upgrades)—to spread basis risk across different basis-risk sources.

Basis risk is not a flaw in hedging; it's the cost of using imperfect tools to protect real exposures. Professional hedgers accept it, measure it, and keep it within policy bounds.

## See also

<div class="wiki-seealso">

### Closely related

- [Basis](/basis/) — the definition of the price gap that drives basis risk
- [Futures Contract](/futures-contract/) — how forward contracts work and why they don't always track spot prices
- [Hedging](/derivatives-hedging/) — the broader practice of offsetting risk through derivatives
- [Cross-Hedge](/basis/) — using a correlated but different instrument to hedge an exposure
- [Contango](/contango/) — how futures prices above spot prices can widen basis over time

### Wider context

- [Crude Oil](/crude-oil/) — the commodity underlying the jet-fuel hedge in this article's example
- [Derivative](/derivatives-hedging/) — the family of instruments used to hedge basis risk
- [Price Risk](/market-risk/) — the underlying exposure that basis risk complicates
- [Correlation](/beta/) — the statistical relationship underlying hedge effectiveness
- [Duration](/duration/) — how maturity mismatch creates basis risk in fixed-income hedging

</div>

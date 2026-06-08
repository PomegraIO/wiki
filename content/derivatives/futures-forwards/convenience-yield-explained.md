---
title: "Convenience Yield Explained"
description: "Convenience yield is the implicit benefit of holding a physical commodity, affecting how futures and forward prices relate to storage costs."
keywords:
  - convenience yield
  - futures pricing
  - commodity storage
  - forward price
  - cost of carry
  - physical commodity holding
  - storage convenience
---

*Convenience yield is the benefit of holding a physical commodity rather than a futures contract on it. It captures everything you gain by owning the actual asset—from having inventory available for immediate sale to avoiding delivery logistics—and it directly lowers the **futures price** below what pure storage economics would predict.*

<div class="wiki-infobox">

<div class="wiki-infobox-title">Convenience Yield — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The premium of owning physical inventory rather than waiting for delivery.</div>

|   |   |
|---|---|
| **Core concept** | Implicit return from holding the physical commodity itself |
| **Effect on prices** | Lowers the [futures price](/futures-contract/) relative to storage costs |
| **Common in** | Oil, natural gas, grains, metals, electricity |
| **Measurable how** | By backing it out of the cost-of-carry formula once real prices are observed |
| **Who benefits** | Merchants, utilities, refineries with active inventories |
| **Who pays** | Hedgers and speculators buying futures |

</aside>

## The Cost-of-Carry Formula and the Gap

Textbook theory says the [futures price](/futures-contract/) should equal the spot price plus all costs to store and finance the commodity until delivery. If you buy oil today at \$70 and it costs \$5 to store it for three months, plus \$2 in financing charges, the three-month futures should trade around \$77.

But in reality, oil futures often trade *below* that sum. The difference is convenience yield. It reflects the real economic value of having the physical asset on hand: a refiner can respond to a spike in crack spreads, a utility avoids the risk of a supply shortage, a merchant can fulfill surprise customer orders. That value isn't fictional; it's just hard to assign a dollar figure until you observe the actual forward curve.

The formula becomes:

**F = S × e^(r + u - c) × T**

where *F* is the futures price, *S* is the spot price, *r* is the risk-free rate, *u* is storage and insurance, *c* is convenience yield, and *T* is time to maturity. When convenience yield is high, *c* grows, and *F* falls relative to costs.

## Why Convenience Yield Varies So Much

Convenience yield isn't constant. It spikes during supply crunches, when the ability to pull from inventory suddenly becomes invaluable. When refineries are running lean on crude oil and a pipeline breaks, the convenience of having tanks full becomes enormous—and futures prices contract sharply relative to spot prices, a state called *backwardation*.

Conversely, when warehouses are stuffed with excess inventory and demand is weak, convenience yield shrinks toward zero. Buyers don't care much about having immediate access to something no one needs right now, so futures prices rise closer to the theoretical cost-of-carry level, a pattern called *contango*.

Agricultural commodities show extreme seasonal swings. Right after harvest, when bins are full, convenience yield is low—futures trade rich. As the season advances and supplies dwindle, convenience yield climbs, and futures grow cheaper than they were months earlier. A grain merchant holding inventory worth \$4.50/bushel spot might be happy to sell it forward at \$4.60 if storage and financing eat \$0.15 but convenience yield is only \$0.05.

## The Cost-of-Carry vs. Convenience Yield Spread

The spread between storage-plus-financing and convenience yield is what traders call the *net cost of carry*. It's the true economic incentive to hold or short the physical commodity.

- **High net carry (convenience yield small):** Incentive to hold spot and short futures, capturing the spread
- **Low net carry (convenience yield large):** Incentive to buy futures and accept a cheap entry, knowing scarcity value is embedded elsewhere
- **Negative net carry (convenience yield exceeds costs):** Rare, but signals that holding the asset is so desirable that owners accept storage losses just to keep it

For oil in a tight market, convenience yield might run 5–8% annually. For wheat in a bumper crop year, it may be near zero. Electricity, with zero storability, has infinite convenience yield in the spot market—you must use it now or lose it—so the cost-of-carry formula barely applies at all.

## Measuring Convenience Yield in Practice

No broker quotes convenience yield directly. Instead, traders back it out from market prices using the cost-of-carry equation. If the futures trade at \$75, spot is \$70, rate is 2%, storage is \$5, and time is three months (0.25 years), you solve for *c*:

\$75 ≈ \$70 × e^(0.02 + 0.05 - c) × 0.25

This gives c ≈ 0.07, or 7% annually—a meaningful scarcity premium that the market is pricing in.

The tighter the supply, the harder the futures fall relative to these cost-of-carry benchmarks, and the easier it is to see convenience yield in action. During the 2008 oil crisis, some [contango](/contango/) spreads were extraordinarily steep because convenience yield was negligible; holders were so desperate to sell that they'd accept \$10 less per barrel if it meant moving volume three months out.

## Who Uses This Framework

Commodity merchants use convenience yield to decide whether to hold inventory or sell it forward. If carrying costs exceed convenience yield, they hedge by shorting futures. If convenience yield exceeds costs, they buy the physical commodity and sell it forward, locking in a spread.

Portfolio managers and index funds exploit convenience yield patterns by studying the shape of the [futures curve](/futures-contract/). In backwardation, spot prices are often rising and convenience yield is high, signaling real scarcity. In contango with low convenience yield, supplies are ample and spot prices may be peaking.

Refineries, utilities, and processing plants monitor convenience yield to decide when to build or draw down strategic reserves. A power plant facing high energy costs will bid hard for natural gas futures when convenience yield implies scarcity, knowing it can delay expensive spot purchases.

## Convenience Yield and Storage Decisions

One of the sharpest lessons convenience yield teaches is that the cost of storing a commodity is not the whole story. A farmer might pay \$0.20/bushel to store wheat, but if convenience yield is \$0.30, he's actually making money by holding it—the scarcity value he captures exceeds his direct costs.

This is why commodity houses and energy firms maintain buffer inventories even when storage is expensive. The convenience yield often justifies it. In weak markets, that same storage becomes a trap; convenience yield collapses, and they're stuck holding assets with negative net carry.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — futures trading above spot; implies low scarcity and positive carry
- [Cost of Carry](/cost-of-carry/) — storage, financing, and insurance costs that theoretical prices incorporate
- [Futures Contract](/futures-contract/) — standardized derivative tied to spot prices and carry dynamics
- [Backwardation](/backwardation/) — futures below spot; signals high convenience yield and tight supply
- [Futures Roll Yield](/futures-roll-yield/) — gain from rolling into the next contract, related to curve shape

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why firms use futures to manage commodity exposure
- [Forward Contract](/forward-contract/) — custom agreements where convenience yield also influences pricing
- Commodity Markets — the spot and derivative landscape where scarcity value emerges
- [Securitization](/securitization/) — how cash flows from physical assets are bundled and priced
- Risk Management — strategic inventory and hedging decisions

</div>

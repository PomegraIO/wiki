---
title: "Convenience Yield in Commodity Futures Explained"
description: "The convenience yield is the implicit return from holding physical inventory instead of buying futures contracts; it explains why futures prices often trade below the spot price."
keywords:
  - convenience yield commodity futures
  - commodity futures contango backwardation
  - futures basis
  - physical commodity storage
  - commodity pricing
image: "/svg/derivatives.svg"
---

*The **convenience yield** is the benefit of owning physical commodity inventory rather than holding a [futures contract](/futures-contract/) on the same commodity. It captures the value of having inventory on hand to meet demand or avoid stockouts. When convenience yield is high, futures prices fall below the spot price (called [backwardation](/backwardation/)); when it is low, futures trade above spot in a state called [contango](/contango/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convenience Yield in Commodity Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The premium from holding real inventory is not captured by futures buyers until they take delivery.</div>

|   |   |
|---|---|
| **Physical inventory benefit** | Ability to meet surprise demand or avoid line shutdowns |
| **Futures contract** | No inventory on hand; delivery happens only at expiration |
| **Convenience yield** | The implicit return for holding stock instead of a forward contract |
| **Backwardation** | Near-term contracts trade above distant ones; producer inventory is tight |
| **Contango** | Distant contracts trade above near-term ones; ample inventory or high storage costs |
| **Who captures it** | Inventory holders (refiners, miners, traders); futures buyers do not |
| **Sign of scarcity** | High convenience yield = tight physical markets |

</aside>

## Definition and the Cost-of-Carry Model

The **convenience yield** sits at the heart of how commodity [futures](/futures-contract/) are priced relative to the spot market. Think of a refinery that holds a tank of crude oil. It could sell the oil today at the spot price, or it could store it and sell the stored oil tomorrow. If it sells via futures, it locks in a forward price, paying for storage and financing. But if it holds the actual oil, it also has the option to sell immediately if a customer suddenly needs it, or to use it in production without transport delays.

This flexibility—the option value of having inventory on hand—is convenience yield. It is the return the refinery earns simply by owning the commodity rather than a futures contract.

In the classic **cost-of-carry** model, the futures price should equal the spot price plus the cost to store and finance the commodity for the given period:

```
Futures Price = Spot Price + Storage Cost + Financing Cost − Convenience Yield
```

Rearranged:

```
Convenience Yield = Spot Price + Storage Cost + Financing Cost − Futures Price
```

If a barrel of crude costs $60 to buy today, costs $1 to store for three months, and costs $0.50 in financing charges, the three-month futures should trade at $61.50 absent convenience yield. But if the three-month future is trading at $60.80, the implied convenience yield is $0.70 per barrel. The refinery is willing to sell the future at a discount because it values the flexibility of holding physical stock.

## Backwardation: High Convenience Yield

When futures prices are lower than spot prices (or when near-term contracts are more expensive than distant ones), the market is in **backwardation**. This signals high convenience yield: inventory holders are willing to pay to own the physical commodity because it is scarce or urgently needed.

Backwardation typically appears when:

- **Physical supplies are tight.** [OPEC](/central-bank/) production cuts, refinery outages, or transportation disruptions reduce available inventory. The refinery that has a tank of oil can use it or sell it to a neighbor quickly; losing that optionality is costly.
- **Production is concentrated.** If only a few refineries control supply, they prize inventory because they control the price.
- **Seasonality.** Before winter, heating oil backwardates because demand spikes and storage dwindles. Holding inventory is valuable.
- **Demand spike.** A geopolitical shock, hurricane, or economic surprise can push spot prices higher than futures, because immediate need trumps future certainty.

In backwardation, a producer or trader holding physical inventory can sell it at spot (high price) while simultaneously buying the future contract cheap, locking in a carry (profit). This is called a **cash-and-carry trade**. The existence of profitable cash-and-carry opportunities is an equilibrium signal: when they disappear, backwardation has peaked.

## Contango: Low or Negative Convenience Yield

**Contango** is the opposite: distant futures trade above near-term ones (or futures trade above spot). This means convenience yield is low or even negative. Reasons include:

- **Abundant inventory.** Refineries and producers have more physical stock than they need. The benefit of having extra inventory is minimal.
- **High storage costs.** If storing crude is expensive (e.g., during an oil glut when every tank is full), the cost-of-carry pushes futures higher, not lower.
- **Low financing costs.** Cheap [interest rates](/interest-rate/) reduce the cost to finance inventory, making the futures premium smaller but still positive.
- **No immediate demand pressure.** Economic slack or oversupply means there is no premium for having oil on hand right now.

In contango, a trader or speculator buying a futures contract and holding it to expiration will lose money relative to buying the commodity spot, storing it, and taking delivery. This loss is the convenience yield (negative). Contango markets punish inventory holders, which is why producers and traders prefer to liquidate stock rather than sit on it.

## The Storage Cost and Financing Spread

Convenience yield does not exist in isolation; it is the residual after storage and financing costs are accounted for. The cost-of-carry model is the scaffold.

A barrel of crude stored in a tank for three months might cost:
- **Tank rental or implicit depreciation:** $0.30
- **Insurance:** $0.05
- **Financing cost** (interest on the cash tied up): $0.40 (at 5% annual rates)

Total carry cost: $0.75 per barrel. If the three-month future is priced at spot + $0.75, convenience yield is zero. If the future is priced at spot + $0.20, convenience yield is negative $0.55—meaning the contract is so expensive that buying futures and waiting is preferable to owning inventory.

## Convenience Yield and Market Participants

**Refineries and producers** capture convenience yield. They own inventories anyway (for operational reasons), and their willingness to sell futures at a discount (backwardation) reflects the real value they place on physical stock.

**Futures traders and speculators** do not capture convenience yield in the traditional sense. When they buy a futures contract, they have no inventory to liquidate and no option value. They are purely exposed to price movement. If they buy in backwardation and hold to expiration, they lose the carry—they pay more for the contract than the spot commodity will be worth.

**Hedgers** (a farmer, airline, or mine) use futures to lock in prices. They neither own inventory nor benefit from convenience yield; they simply reduce price risk.

## Practical Examples: Crude Oil and Agricultural Commodities

**Crude oil** typically swings between backwardation and contango as geopolitical risk and inventory levels fluctuate. During the early 2022 Russia-Ukraine disruptions, backwardation spiked sharply: the March contract traded significantly above June futures because traders and refiners feared immediate supply loss. As inventory rebuilt months later, contango returned.

**Agricultural commodities** show pronounced seasonal convenience yield. Just before harvest, old-crop corn futures backwardate because elevators and farmers with old inventory value the option to sell at spot prices before new supply floods in. Post-harvest, as new supply arrives, contango kicks in—the old crop is no longer scarce, and storing it costs more than what the futures market pays for delayed delivery.

## Implications for Investors and Hedgers

If you buy a [commodity futures contract](/futures-contract/) in deep contango and hold it to expiration, you will implicitly lose the carry: the cost of storage and financing that the futures price embedded. This is why passive [commodity ETFs](/etf/) that roll contracts continuously can underperform spot prices over long periods. They are slowly paying the convenience yield to producers and inventory holders.

Conversely, in backwardation, rolling futures (selling a near-term contract and buying a distant one) can be profitable if supply remains tight. But backwardation eventually reverts; when it does, the trade turns negative.

Speculators and funds that want to bet on commodity prices should be aware: the futures price you see on your screen already reflects market expectations about convenience yield, storage costs, and financing. Comparing the futures price to spot is not naïve—it is part of the pricing calculation—but it is only part. The term structure (the curve of prices across maturities) is the fuller picture.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — structure and mechanics of commodity contracts
- [Contango](/contango/) — futures prices rising over time
- [Backwardation](/backwardation/) — futures prices falling over time
- [Basis](/basis/) — the spread between spot and futures prices
- [Spot Rate](/spot-rate/) — today's physical market price

### Wider context

- [Commodity Futures](/futures-contract/) — general commodity derivative trading
- [Derivatives Hedging](/derivatives-hedging/) — how commodity users manage price risk
- [Forward Contract](/forward-contract/) — direct alternative to futures for locking in prices
- [Crude Oil](/crude-oil/) — major commodity with strong convenience yield dynamics
- [Corn](/corn/) — agricultural commodity with seasonal convenience yield patterns

</div>

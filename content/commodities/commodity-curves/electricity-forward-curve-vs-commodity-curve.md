---
title: "Electricity Forward Curve vs Commodity Futures Curve: Key Differences"
description: "Electricity forward curves differ from commodity futures curves because power cannot be stored. Learn how expected generation costs drive power prices instead of cost-of-carry."
keywords:
  - electricity forward curve
  - commodity futures curve
  - power markets
  - non-storable commodity
  - cost of carry
  - generation cost
---

*The **electricity forward curve vs commodity futures curve** distinction lies in a fundamental fact: power cannot be stored. While oil, gold, and grain forward curves are shaped by interest rates and storage costs, power curves are driven almost entirely by expected fuel and operating costs at the time of delivery. This difference means power markets have unique pricing dynamics, steeper backwardation risk, and less correlation with traditional commodity spreads.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Electricity Forward Curve — Key Facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Power is priced by expected generation cost, not storage arbitrage.</div>

|   |   |
|---|---|
| **Storable commodities** | Prices reflect cost-of-carry (interest + storage + insurance) |
| **Power (non-storable)** | Prices reflect expected generation cost at delivery date |
| **Typical curve shape** | Steep backwardation (near-term higher) due to outage risk |
| **Key driver** | Fuel costs, transmission capacity, seasonal demand |
| **Hedging focus** | Load forecasting and generation availability, not inventory |
| **Cost of financing** | Minimal impact on forward prices |

</aside>

## Why power cannot be stored

Electricity is created at the moment demand emerges; it cannot sit in a warehouse or tank farm waiting for a profitable sale date. Once generated, power must be consumed within microseconds or dissipated through equipment resistance. This physical constraint makes electricity fundamentally different from oil, wheat, or copper.

The absence of storage eliminates the entire cost-of-carry arbitrage mechanism that governs other commodity forward curves. An oil trader holding a barrel incurs interest costs, storage rent, insurance, and degradation risk—all of which must be paid by contango (the spread between future and spot prices). A power plant operator holding electricity cannot do the same. This is why power markets operate under entirely different pricing logic.

## Cost-of-carry in storable commodities

For agricultural, energy, and metal commodities, the forward curve typically lies above the spot price (contango) by the full carry cost. A grain trader who buys corn at the spot price, stores it, and sells it forward locks in the cost of:

- Interest (financing the purchase for X months)
- Physical storage (warehouse rent, bins, handling)
- Insurance (against loss or damage)
- Shrinkage or deterioration (natural degradation over time)

The forward price must exceed the spot price by at least these costs, or a profit-seeker would buy spot, store, and sell forward, driving prices into alignment. This is called the cash-and-carry arbitrage. When it breaks, it signals either a shortage (backwardation) or a glut (steep contango).

## Why electricity forward curves ignore cost-of-carry

Power has zero storable quantity. There is no interest cost, warehouse rent, or inventory holding period. The only economic factor that ties a future power price to today's decisions is the expected cost of generating that power at the specified time and location.

In deregulated markets, the forward price of electricity typically reflects:

- **Forecasted fuel costs** (natural gas, coal, or other dispatch fuels at that date)
- **Expected transmission bottlenecks** (constrained regions trade at a premium)
- **Seasonal demand patterns** (summer peak hours command a premium in cooling-heavy climates)
- **Generation capacity margins** (tight reserves raise near-term prices; slack capacity depresses them)
- **Outage risk** (planned and unplanned generator failures increase near-term scarcity)

Interest rates, financial discounting, and storage arbitrage play almost no role. A 5% rise in Treasury yields does not automatically shift the power curve up by 5%—the way it would for oil or copper. This is why power markets move on power-specific news: a coal plant retirement announcement, a weather forecast affecting hydroelectric supply, or a transmission line closure.

## Forward curve shapes: power vs. traditional commodities

**Storable commodities** (oil, natural gas, grain, metals) typically trade in contango under normal conditions—the forward curve slopes upward. This reflects carry costs. Backwardation emerges only during acute shortage or supply-chain disruption.

**Electricity** almost always trades in steep backwardation—near-term power is more expensive than distant futures. This happens because:

- Outage risk is highest in the next 30 days (unknown plant failures are imminent)
- Generation capacity is most constrained in peak-demand seasons (summer or winter, depending on region)
- Seasonal generation profiles are volatile (hydroelectric in dry years; wind in calm periods)

A power plant's unexpected shutdown next month creates immediate scarcity; months ahead, the market assumes normal operations. This structural backwardation persists even in periods of ample supply, because the risk premium never fully disappears.

Compare this to oil: a geopolitical shock triggers backwardation, but storage economics eventually restore contango as traders buy cheap spot, pay carry, and sell forward.

## Hedging and trading implications

Because power cannot be stored, [hedging strategies](/derivatives-hedging/) must rely on operational measures rather than financial arbitrage. An electric utility cannot buy cheap power in March and store it for July peak demand. Instead, utilities:

- Lock in generation costs through forward contracts and [swaps](/swap/)
- Manage load forecasting to match generation supply
- Diversify fuel sources to reduce exposure to any single generation cost
- Plan maintenance windows to minimize summer outage risk

Traditional commodity traders who profit from carry-arbitrage have no parallel trade in power. A power trader instead builds strategies around:

- Regional [price discovery](/price-discovery/) (buying where transmission constraints create local discounts)
- Seasonal spreads (capturing the pattern of peak-season premiums)
- Outage volatility (volatility spikes when major plants shut down)

These dynamics make power a distinct asset class—closer in structure to utilities and weather risk than to oil or metals.

## Market impact of non-storability

The inability to store power also means:

- **Thinner long-dated markets** – Few traders hold positions 5 years out; most power trading is within 1–2 years. Oil has liquid markets 10+ years forward.
- **Higher basis risk** – A utility buying electricity for delivery in Region A cannot easily redirect it to Region B if regional prices diverge; transmission constraints lock in price differences.
- **No financial buffer** – When demand spikes unexpectedly, prices can spike dramatically because supply cannot be released from storage. An oil shortage can be eased by drawing reserves; power scarcity has no such relief valve.

This is why power markets are more tightly regulated and why prices swing more violently during stress events (summer heat waves, winter cold snaps, plant failures) than in storable commodity markets.

## See also

<div class="wiki-seealso">

### Closely related

- Cost-of-carry — How storage costs shape forward prices in grain, oil, and metals
- [Contango](/contango/) — Forward prices above spot, typical in well-supplied markets
- [Backwardation](/backwardation/) — Forward prices below spot, signaling scarcity or near-term risk
- [Commodity futures curve](/futures-contract/) — The shape and drivers of forward curves across all commodities
- [Derivatives for hedging](/derivatives-hedging/) — Why power hedging differs from traditional commodity hedging
- [Price discovery](/price-discovery/) — How regional electricity markets reveal true supply-demand balance

### Wider context

- [Crude oil](/crude-oil/) — A storable commodity with traditional cost-of-carry pricing
- [Natural gas](/natural-gas/) — Partly storable, but with unique seasonal storage dynamics
- [Forward contract](/forward-contract/) — The mechanics of all forward pricing
- [Market risk](/market-risk/) — How power price volatility differs from commodity volatility
- [Swap](/swap/) — The primary hedging tool in electricity markets

</div>

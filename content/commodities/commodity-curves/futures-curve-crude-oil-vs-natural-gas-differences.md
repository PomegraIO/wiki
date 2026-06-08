---
title: "Why Crude Oil and Natural Gas Futures Curves Behave Differently"
description: "Storage economics, seasonality, and convenience yield explain why crude oil and natural gas futures curves have distinct shapes and dynamics."
keywords:
  - crude oil futures curve
  - natural gas futures curve
  - commodity curves
  - contango backwardation
  - energy commodity spreads
  - futures curve structure
---

*Crude oil and natural gas futures curves often move in opposite directions despite both being energy commodities, driven by differences in storage cost, seasonality, and convenience yield.* Crude oil typically trades in [contango](/contango/) (far contracts higher than near), because storage is cheap and a global market exists. Natural gas often inverts into [backwardation](/backwardation/) (far contracts cheaper than near), especially in winter, because storage is expensive, regional supply is tight, and seasonal heating demand spikes. Understanding these structural differences is essential for [spread](/basis/) trading and hedging energy portfolios.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Oil vs Gas Futures Curves — Key Facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Oil stores globally and cheaply; gas stores regionally and expensively—reshaping the curve.</div>

|   |   |
|---|---|
| **Crude oil curve** | Often contango; storage is capital-efficient |
| **Natural gas curve** | Often backwardation, especially in winter; storage is expensive |
| **Storage economics** | Oil: ~$1–2/barrel/month; Gas: ~$0.30–1.00/mmbtu/month |
| **Seasonality** | Gas: winter demand spike drives near-term premium; Oil: steady global demand |
| **Convenience yield** | Higher in gas (scarcity premium); lower in oil (abundant, fungible) |
| **Basis trading** | Spread between front and back months is price signal |

</aside>

## Storage Economics: The Fundamental Driver

The largest structural difference between crude and natural gas is **cost and ease of storage**.

**Crude oil storage** is relatively cheap and widely available. The world has massive tank farms (Cushing, Rotterdam, Singapore, China) that can hold millions of barrels for months. Storing oil costs roughly $1–2 per barrel per month in lease and carrying fees, or less than 5% per annum on oil at $40/bbl. This low carrying cost encourages inventory building when prices are low and funds [rolling forward](/forward-contract/) positions into distant contracts. The result: crude typically trades in contango, with December futures trading higher than November, which trades higher than October.

**Natural gas storage** is expensive and limited. Gas must be held in underground caverns, salt domes, or specialized tanks. The United States has ~4 trillion cubic feet (Tcf) of working gas capacity; that sounds vast until you realize the U.S. consumes ~30+ Tcf per year. Injection and withdrawal cycles take time and cost $0.30–1.00 per mmbtu (million British thermal units) in compression and transport. For a region facing winter demand spikes, the carrying cost is high relative to the commodity's value. A natural gas trader cannot as easily buy cheap summer gas and store it for winter profit; the storage cost eats the spread.

## Seasonal Demand and Regional Tightness

**Crude oil** demand is driven by global transportation (autos, trucks, aviation), industrial heating, and power generation. These demands are relatively stable year-round; winter heating increases demand slightly, but crude's broad uses mean seasonal swings are mild. A barrel of oil is fungible worldwide; if a buyer needs oil, they can source it from the Middle East, Russia, the North Sea, or West Texas. This global fungibility flattens the curve and removes sharp seasonal premiums.

**Natural gas** is regional and seasonal. In the Northern Hemisphere, winter heating demand spikes 50–100% above summer baseline. The U.S. Northeast, Midwest, and Canada face severe cold; heating is often reliant on natural gas. Storage is insufficient to meet peak demand, so winter gas prices spike relative to summer. A natural gas futures curve from May through February often shows October/November (pre-winter) contract premiums, then a steep drop into spring and summer contracts. Far-out contracts (e.g., December of the following year, when heating demand is again expected) trade at a premium, but not as much as immediate winter months.

This seasonal inversion in the near-term natural gas curve is called a **winter peak**, and it is one of the most reliable seasonal patterns in commodities.

## Convenience Yield Divergence

Convenience yield is the implicit value traders place on holding the physical commodity versus a futures contract. For crude, convenience yield is low: oil in storage is not strategically valuable (except as inventory for refineries, which have their own supply chain), so the futures curve reflects pure carrying costs. For natural gas, convenience yield is high: gas in storage in winter is worth a premium because the risk of not having it is severe. A utility facing a cold snap with depleted storage might pay $50/mmbtu for emergency gas; this optionality—the value of having gas available—drives the convenience yield and inverts the curve into backwardation.

When natural gas inventories are high and summer demand is low, the curve flattens or rolls into contango: storage is plentiful and the pressure to hold gas for winter is low. But a sudden cold snap, a supply disruption, or abnormally low storage levels (as occurred in North America in 2021–2022) can swing the curve sharply into backwardation as the convenience premium spikes.

## Spot Month Dynamics

Both crude and natural gas exhibit **spot month spikes**—the front-month contract trades at a premium to the next month—but for different reasons:

- **Crude oil**: The front-month premium is small and reflects the cost of delivery and carrying. It rarely inverts (back-month higher than spot).
- **Natural gas**: The front-month premium can be massive in winter. If it is December and a cold snap is forecast, the December contract might trade $3/mmbtu higher than January, purely due to immediate shortage premium. Once the month rolls, that premium evaporates into the new front month.

This spot-month volatility in natural gas makes [carry trade](/carry-trade/) strategies riskier and requires active monitoring.

## Implications for [Futures](/futures-contract/) and [Hedging](/derivatives-hedging/)

A crude oil producer might hedge next year's output by selling December futures contracts. Because the curve is typically in contango, the December contract trades above the spot price; the producer locks in a higher price and accepts the market's implicit carry cost. Over time, as the contract rolls, the producer can reinvest in far-out contracts and maintain a rolling hedge.

A natural gas producer faces the opposite problem. If gas is abundant and the curve is in summer contango, selling winter futures (December) at a premium might seem attractive. But a harsh winter could render the contract unprofitable in real terms, or force the producer to buy back the contract at a loss. Conversely, in tight market conditions or early in a heating season when backwardation is steep, a producer might sell front-month contracts at a premium to lock in profit, then roll into back months as the season progresses and the premium collapses.

## Portfolio Implications

A mixed energy portfolio with both oil and gas exposure must account for these curve differences. Oil hedges and gas hedges do not move together. A hedge that works for crude might leave gas exposure naked, and vice versa. Spread traders exploit the difference by long crude far months and short gas back months (or vice versa), betting on mean reversion or macroeconomic scenarios that move oil and gas relative strength.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — The typical curve shape for crude, driven by storage economics
- [Backwardation](/backwardation/) — The inverted curve in natural gas, especially in winter
- [Futures contract](/futures-contract/) — The instruments that express these curve shapes
- [Carry trade](/carry-trade/) — Profiting from the curve structure, especially in oil
- [Basis](/basis/) — The difference between spot and futures prices, and spreads between contracts

### Wider context

- [Crude oil](/crude-oil/) — Global commodity with stable seasonal demand
- [Natural gas](/natural-gas/) — Regional, seasonal commodity with storage constraints
- [Derivative hedging](/derivatives-hedging/) — How energy companies manage price and production risk
- Commodity cycles — Broader patterns in energy and materials markets

</div>

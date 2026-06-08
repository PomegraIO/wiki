---
title: "Curve Kinks Caused by Storage Constraints in Commodity Markets"
description: "Explain why commodity forward curves develop visible kinks and breaks when storage capacity is saturated or constrained at specific contract tenors."
keywords:
  - commodity curve kink storage
  - forward curve kink
  - storage constraint pricing
  - commodity contango kink
image: /svg/commodities.svg
---

*When a **commodity curve kink caused by storage constraint** appears, it reveals the exact moment physical supply exhausts the market's ability to warehouse it. The curve accelerates sharply at one contract month—often flattening or even inverting before that point and normalizing after it—because storage is full at that horizon and barrels cannot roll forward.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Storage-Driven Curve Break — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">A kink marks the boundary where warehouses fill and carry costs spike.</div>

|   |   |
|---|---|
| **Kink definition** | Sharp non-linear change in curve slope at a specific tenor. |
| **Root cause** | Storage capacity saturated; supply cannot roll to the next month. |
| **Typical pattern** | Flat or inverted before kink; steep contango after. |
| **Barrels affected** | All physical supply reaching warehouse at kink tenor faces forced sale. |
| **Duration** | Kink flattens once storage clears or supply route changes. |
| **Market signal** | Extreme scarcity nearby; normal future supply expected. |

</aside>

## How storage constraints create a kink

A normal, well-supplied commodity curve shows smooth progression: near-term months command a slight premium (backwardation) or slight discount (contango) to one another, with the curve widening gradually toward distant months. The slope moves consistently from month to month.

A **kink** breaks this smoothness. The curve is nearly flat or even inverted through, say, March, April, and May contracts. Then, in June, the curve jumps sharply higher, creating a visible elbow. From June onward, [contango](/contango/) is normal and healthy—each month is 50–100 basis points above the prior one. The kink is the discontinuity: the May-to-June spread is 3–5 times larger than any month-to-month spread before it.

This happens because storage terminals or tank farms are running at 95–100% capacity through May. June supply cannot be accepted and stored—there is nowhere to put it. Buyers of June barrels therefore demand a steep discount compared to May, or equivalently, May barrels command a premium because they can be moved out of the warehouse before new supply arrives in June.

Once June delivery arrives, those barrels are consumed or exported, warehouse pressure eases, and the curve normalizes. The kink smooths out over time.

## Why kinks reveal supply-demand turning points

Kinks are invaluable signals because they pinpoint the exact tenor at which the market transitions from acute scarcity to expected normality. 

If a crude oil curve shows a kink at the July contract, traders infer: 

- May and June demand is strong, and warehouses are filling faster than they can drain.
- By July, the market expects either demand to moderate or supply to improve (e.g., a refinery comes back online, a geopolitical crisis eases, or seasonal inventory builds conclude).
- The premium in earlier months reflects the urgency to absorb current supply; the discount (or normalized spread) in later months reflects confidence in future balance.

A kink is distinct from simple curve steepness. A steeply contangoed curve is smooth; it reflects normal carry costs across the entire curve. A kinked curve has a discontinuity—an abrupt change in how much each successive month costs. That abruptness is the storage constraint screaming.

## The mechanics: how barrels get stuck

Consider a crude terminal with 10 million barrels of capacity. Current inventory is 9.5 million. Incoming supply is 500,000 barrels per day. At that inflow, the terminal will be full in one day. Demand from the terminal is 400,000 barrels per day. So the net accumulation is 100,000 barrels per day.

If the terminal is full, the operator must either:

1. Reject or slow deliveries (notify suppliers to delay shipments).
2. Force sell inventory at whatever price clears the market.
3. Route barrels to alternative storage (costly; shipping time eats margin).

In a futures market, this constraint translates directly to the curve. The contract month that corresponds to when the terminal will be full trades at a discount relative to the month before because no one wants to deliver there—the warehouse will reject them or force them to sell at spot minus a penalty.

Conversely, the contract month before the full month trades at a premium: warehouses desperately want to clear inventory before the next inflow arrives, and buyers know that early delivery means easier logistics and higher prices.

## Geographic and seasonal kinks

Kinks do not always occur at the same tenor. They move and intensify based on:

- **Seasonality**: Winter heating oil demand creates kinks in November–December when terminals struggle with the seasonal surge. By February, heating oil demand drops, warehouses drain, and kinks flatten.
- **Infrastructure**: A port or pipeline closure shifts the bottleneck downstream. If a major export terminal is shut for maintenance, regional storage will fill, creating a kink at the contract month corresponding to that maintenance window.
- **Production cycles**: Agricultural markets (corn, soybeans, wheat) show persistent kinks at harvest-into-storage months (September–October in the Northern Hemisphere) because farmers deliver to elevators all at once.

A trader analyzing a commodity curve must therefore understand the physical calendar and infrastructure, not just the mathematical shape.

## Kinks vs. other curve features

A **kink** is distinct from:

- **[Contango](/contango/)**: A smooth, upward-sloping curve reflecting carry costs. No discontinuity.
- **[Backwardation](/backwardation/)**: Inverted or flat curve signaling scarcity. Still smooth; no kink.
- **Implied volatility smile**: In options, a smile reflects uncertainty about direction. Not a storage phenomenon.

A kink is structural and rooted in physical logistics. It persists as long as the storage constraint persists. Once the constraint eases—demand picks up, supply dries up, or warehouses are expanded—the kink smooths and the curve reverts to a normal shape.

## Kinks in different commodities

**Crude oil and refined products** (gasoline, heating oil, diesel) show frequent kinks because refineries and distribution terminals have discrete capacity limits. A maintenance shutdown at a major refinery often produces a kink in the products curve as inventory builds in upstream storage.

**Natural gas** shows kinks at seasonal boundaries: spring and fall shoulder months often have sharp curve breaks as storage management shifts from injection (summer) to withdrawal (winter).

**Metals** (copper, zinc, aluminum) show kinks less frequently because LME warehouses are more flexible and widely distributed. However, a declared warehouse closure or a delivery standstill (as seen in the 2006 tin short squeeze) creates brutal kinks.

**Agricultural commodities** exhibit pronounced kinks at harvest: the US corn curve typically has a kink in November (harvest completion) as elevators move from receiving mode to drawdown mode. This is so regular that basis traders anticipate it and position accordingly.

## Trading the kink

A trader who expects a storage constraint kink has several choices:

- **Sell the near month, buy the far month**: If a kink is widening (May-June spread expanding), profit by shorting May and buying June, betting the spread will narrow once storage clears.
- **Anticipate resolution**: If you know a refinery outage that caused the kink will end in July, buy June futures and sell July, betting that the premium (kink) will collapse as the constraint eases.
- **Physical arbitrage**: If you own warehouses with available capacity, you can profitably buy the discounted kink month and store it, selling into the premium month.

These trades are not risk-free. A kink can deepen if the supply shock worsens, or it can flatten faster than expected if demand surprises. But traders who understand the storage calendar are better positioned to exploit the pricing dislocations kinks create.

## When kinks signal trouble

A deep, persistent kink—especially one that widens despite expectations that it should flatten—is a warning. It suggests that supply constraints are worse than the market anticipated, or that storage alternatives that traders counted on are unavailable.

During the 2020 oil crisis, crude curves developed extreme kinks as storage filled globally; some kinks persisted longer than traders expected because alternative storage (ships, pipeline cushions) filled faster than normal. Traders who expected normal kink behavior got caught off guard.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Curve Flattening vs Inversion](/futures-curve-flattening-vs-inversion/) — How curve shape responds to supply shocks.
- [Contango](/contango/) — Normal carry costs in the forward curve.
- [Backwardation](/backwardation/) — Inverted curve structure signaling scarcity.
- [Backwardation vs Contango for Commodity Producers Hedging Output](/backwardation-vs-contango-producer-hedger/) — How producers hedge based on curve shape.
- [Basis Risk](/basis-risk/) — The mismatch between contract month and actual delivery need.
- [Commodity Futures Curve Construction from Swaps](/commodity-futures-curve-construction-from-swaps/) — Building curves from swap and futures data.

### Wider context

- [Futures Contract](/futures-contract/) — Standardized contracts that define deliverable months.
- [Spot Rate](/spot-rate/) — Physical delivery price driving near-term curve premium.
- [Forward Contract](/forward-contract/) — OTC alternatives when exchange contracts don't match delivery needs.
- [Price Discovery](/price-discovery/) — How markets reveal true supply-demand balance.
- [Securitization](/securitization/) — Warehouse receipts as financing tools in physical commodity markets.

</div>

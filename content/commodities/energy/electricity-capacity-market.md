---
title: "Electricity Capacity Market"
description: "How electricity capacity markets work: why grid operators run separate auctions for standby generation capacity to ensure reliability independent of energy prices."
keywords:
  - electricity capacity market
  - capacity auction
  - reserve margin
  - grid reliability
  - capacity payment
  - generation adequacy
---

*An **electricity capacity market** is a separate auction mechanism where grid operators procure commitments from power plants to remain available and ready, distinct from the spot energy market where electricity is actually dispatched. The capacity market exists because energy prices alone do not guarantee enough generators will be built and maintained to meet peak demand.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Capacity Market — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Grid operators pay for standby generation capacity to prevent blackouts during peak demand.</div>

|   |   |
|---|---|
| **Core purpose** | Ensure sufficient generation capacity exists to meet peak load plus a safety margin, even if energy prices are low |
| **Market design** | Auction; generators bid how much capacity they will keep operational for a commitment period (often 1 year) |
| **Payment type** | Capacity price ($/kW-year) regardless of whether plant actually runs |
| **Rationale** | Energy-only markets fail to recover investment in peaking plants that run infrequently |
| **Geographic scope** | Regional (e.g., ISO/RTO regions in US, UK, parts of Europe) |
| **Participants** | Thermal generators, renewable, demand response, storage operators |

</aside>

## Why capacity markets exist

Energy-only markets price electricity at marginal cost—what it costs to run the next plant. On most days, this keeps prices low: fuel costs for running a coal or [natural gas](/natural-gas/) plant run 20–50 dollars per megawatt-hour. A generator that runs regularly can cover its variable costs and contribute to fixed costs.

But peaking plants—natural gas turbines or reserve diesel units—run only 10–20 days per year, during extreme heat, cold, or unexpected outages. On a typical day, they earn nothing. Over a year, even if they clear very high prices on those 20 peak days, the total revenue often falls short of the annual capital cost (depreciation, financing, staff). Rational investors will not build peaking capacity if they know they cannot reliably recover the investment.

The grid operator (a Regional Transmission Organization or Independent System Operator—ISO/RTO) faces a dilemma: without enough peaking capacity, demand exceeds supply on the hottest or coldest days, causing blackouts or demand destruction (forced shutdowns). But energy prices alone do not create incentive to build it.

**Capacity markets solve this** by creating a second revenue stream. Generators get paid explicitly for keeping capacity available, via an auction. The grid commits to buy enough capacity to cover peak forecast load plus a reserve margin (often 15–20% extra to cover uncertainties and outages). Generators bid competitively; the auction clears at the price where supply of committed capacity equals demand.

## How the auction works

Regional markets vary, but the basic framework is standard. **Forward auctions** (most common) run 1–3 years before the commitment period. The ISO publishes a forecast of peak load and defines the required reserve margin—say, 114% of peak load. It then solicits bids from all generators: "How much capacity will you commit to keep operational for Delivery Year 20XX for a price of $X per kW-year?"

Generators bid both new capacity and existing capacity. A new 500 MW natural gas plant might bid 60 dollars per kW-year (= 30 million dollars annually) because capital costs are high. Existing coal or nuclear plants, with capital already sunk, might bid 5–10 dollars per kW-year. Renewable units with near-zero fuel cost and battery storage operators (which can respond quickly) also participate.

Bids stack from lowest to highest price. The ISO accepts bids until the stacked capacity reaches the required amount (e.g., 120,000 MW). The marginal bid—the highest-priced bid accepted—sets the market price for all successful participants. If the marginal bid is from a generator asking 30 dollars per kW-year, all generators in the auction receive 30 dollars per kW-year for the year ahead, regardless of their individual bid.

This uniform-price design encourages honest bidding and reduces collusion. A generator cannot hope to bid low and "sneak in"; it will receive the clearing price anyway. Conversely, bidding unrealistically high risks being priced out entirely.

## Pricing and revenue implications

Capacity prices are volatile and region-specific. In Texas (which does not run a formal capacity market, relying instead on energy prices and scarcity), peak prices occasionally spike to 9,000 dollars per MWh for a few hours during crises—but average prices are very low because real-time markets are thin. Other regions, like the PJM Interconnection (mid-Atlantic US), run robust capacity auctions where prices routinely clear at 50–150 dollars per kW-year in recent years, providing a predictable revenue stream to support investment.

A 500 MW combined-cycle gas plant in PJM might earn:
- Capacity revenue: 500 MW × 100 $/kW-year = 50 million dollars per year
- Energy revenue: Running 4,000 hours per year at 30 $/MWh average = 60 million dollars per year
- **Total: ~110 million dollars**, covering depreciation, debt service, and operating costs.

Without the capacity market, energy revenue alone (60 million) may not sustain the investment.

## Qualification and enforcement

Generators that win capacity bids must meet strict performance and availability standards. A coal or gas plant must achieve a minimum availability rate—say, 92%—or face financial penalties. The ISO monitors forced outage rates and withholds payments if a unit exceeds the threshold. New capacity must achieve commercial operation by the delivery year. Battery storage must demonstrate charge/discharge capability within defined time windows.

Renewable resources (wind, solar) can participate but their capacity value is often derated because they are intermittent. A 100 MW solar farm might be credited as 20–30 MW of capacity because it does not run at night or on cloudy days. Wind is credited based on historical coincidence with peak demand; coastal wind farms in New England, which peak in winter, receive higher capacity credit than Great Plains wind.

Demand response—industrial or commercial users that reduce consumption when called—also participates. A factory might commit to cutting 10 MW of load for 100 hours per year; it receives capacity payment and avoids paying for energy when called.

## Controversy and evolution

Capacity markets are contentious. Critics argue they create unnecessary payments to incumbent generators and distort investment signals. Natural gas plants with high upfront costs lobbied for high capacity prices; fossil advocates now argue that cheap renewable and storage alternatives should reduce capacity prices.

Proponents counter that without capacity markets, insufficient generation and storage will be built, risking blackouts as demand grows and fossil plants retire. The 2021 Texas winter storm (ERCOT failure) reignited the debate: critics blamed deferred maintenance and low energy-only incentives; defenders noted that a capacity market would only help if it existed.

Regional reforms are ongoing. PJM is testing "resource adequacy" mechanisms that credit solar and wind more generously, and some regions are incorporating battery storage into capacity auctions. The shift toward variable renewable supply has forced capacity markets to evolve, valuing units not by simple MW but by their actual grid contribution during peak-risk hours.

## See also

<div class="wiki-seealso">

### Closely related

- Energy Market — Real-time pricing and dispatch in wholesale electricity
- [Natural Gas](/natural-gas/) — Primary fuel for peaking generators in capacity markets
- Renewable Energy — Wind and solar participation in capacity auctions
- Battery Technology — Emerging competitor to peaking plants for reserve power

### Wider context

- Commodity — Definition and trading of bulk goods
- Infrastructure Investment — Capital required for grid and generation assets
- Risk Management — How operators manage supply and demand variability

</div>

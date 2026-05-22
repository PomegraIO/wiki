---
title: "Power Spreads"
description: "Regional electricity price differentials that reflect transmission constraints, generation mix, and local supply-demand imbalances in energy markets."
keywords:
  - electricity pricing
  - regional markets
  - energy infrastructure
  - commodity trading
---

*A **power spread** is the price difference between electricity in two regional markets, driven by transmission constraints, generation mix variations, and local supply-demand imbalances. A trader can profit by buying cheap power in one region and selling it in an expensive region, or hedging the basis risk of power contracts.*

<aside class="wiki-infobox">

| Spread Type | Example | Typical Width | Driver |
|---|---|---|---|
| North-South (U.S.) | PJM to MISO | $5–$20/MWh | Transmission congestion |
| Peak-to-Off-Peak | Day/Hour-ahead on same node | $10–$50/MWh | Demand cyclicality |
| Hub-to-Node | Pricing point spread | $0.50–$5/MWh | Local distribution losses |
| California-Nevada | CAL-ISO to NV Energy | $10–$30/MWh | Transmission constraints |
| German-Polish | Cross-border | €5–€20/MWh | Grid congestion |

</aside>

## Why power spreads exist: transmission constraints

Unlike other commodities, electricity cannot be easily stored or transported. It flows instantaneously along power lines, constrained by transmission capacity. When demand is high on one side of a transmission line and supply is high on the other, a bottleneck forms. Power on the short side (supply exceeds demand) is cheap; power on the long side (demand exceeds supply) is expensive.

The spread is the "congestion rent"—the additional price you pay to move power across the transmission constraint. In the U.S., the PJM Interconnection (serving the Midwest and Northeast) and MISO (Midwest ISO) are separated by transmission lines of limited capacity. When cold weather drives demand in PJM and supply in MISO is abundant, PJM prices spike 20–30% above MISO, creating a profitable spread opportunity.

This is permanent, not temporary. The power grid is a network with known constraints. Regions with cheap, abundant generation (renewable-heavy areas, hydro-rich areas) chronically export power at lower prices. Regions with expensive generation (coal, natural gas) chronically import and pay premiums. Traders exploit these persistent spreads.

## Generation mix and renewable intermittency

A region's generation mix directly influences its power spreads. California, with abundant solar and wind, experiences periods of extreme oversupply in mid-afternoon (solar peak) and evening (wind peak). Prices in California can fall to zero or even go negative during these hours, while prices in neighboring regions (Nevada, Arizona) remain positive.

A negative price means the grid operator will *pay* you to consume power because it's cheaper to pay for consumption than to shut down inflexible generators (nuclear, coal) that take hours to ramp down. A trader can exploit this by buying power at negative prices in California and selling it (if transmission allows) in neighboring regions at positive prices.

Intermittency is key. On a windy night, California's wind farms flood the grid with cheap power. On a calm afternoon with cloud cover, wind and solar disappear, and prices spike. The spread between California and other regions shifts intraday. A trader betting on wind patterns can profit.

## Peak and off-peak spreads

Even within a single grid, electricity has different prices at different times. Peak hours (typically 2 PM–10 PM in summer, 7 AM–10 PM in winter) command premiums because demand is highest and marginal generators (expensive) must run. Off-peak hours (midnight–6 AM) are cheap because baseload generators satisfy demand.

The peak-to-off-peak spread can be $10–50/MWh, depending on the season and region. This is predictable and arbitraged by energy traders and utilities. A trader might buy off-peak power, store it in a battery, and sell it at peak times. The spread minus battery losses and financing costs is the profit. As battery storage becomes cheaper, this arbitrage intensifies and spreads narrow.

## Cross-border and regional spreads in Europe

European power markets are more fragmented and interconnected across national borders. Germany has abundant wind capacity; France has abundant nuclear capacity. On a windy day, German prices are low; on a calm day, they're high. The German-French spread fluctuates, constrained by interconnection capacity.

During the 2022 energy crisis, French nuclear plants were offline (maintenance, cooling restrictions), driving prices to €500+/MWh, while German renewables kept prices lower. The German-French spread blew out. Traders with positions in both markets faced conflicting signals. The spread ultimately mean-reverted as nuclear plants restarted and demand fell with warmer weather.

## Basis trading and hedging spreads

A utility that generates power in one region and sells it in another faces spread risk. If the generator has a long-term power purchase agreement (PPA) with prices in Region A but is located in Region B, it's short the spread—if the spread widens, its profit margin narrows.

An energy trader can hedge this by buying spread options or futures. If available, they might buy a forward contract for "Region B power minus Region A power," locking in the spread. This reduces basis risk. Alternatively, they might trade the spread dynamically, reducing the long position when the spread is wide (expensive) and increasing when the spread is narrow (cheap).

## Modeling spreads and infrastructure improvements

Traders and utilities model power spreads using supply and demand forecasts, transmission flow analysis, and generation availability. A fundamental model might estimate:

Spread = (Demand_B - Supply_B) × Transmission_Loss – (Demand_A - Supply_A)

Where transmission loss reflects line congestion and physical losses (heat dissipation over distance). If demand is high and supply is low in B, and demand is low and supply is high in A, the spread widens.

Infrastructure improvements narrow spreads. When a new transmission line is built connecting two regions, capacity expands, and congestion rent shrinks. The spread between PJM and MISO has narrowed over decades as transmission infrastructure expanded. Conversely, if a major transmission line fails, spreads spike immediately as congestion increases.

## Seasonal patterns and weather sensitivity

Power spreads have strong seasonal patterns. In summer, air conditioning demand is high in hot regions (South, Southwest); cold-water cooling issues hit nuclear plants in France. Summer spreads between cool and hot regions are wide.

In winter, heating demand is high; natural gas prices affect marginal generators in gas-dependent regions. A cold winter with high gas prices widens spreads from gas-heavy to hydro-heavy regions.

Weather events are binary triggers. A hurricane threatens natural gas production in the Gulf of Mexico; prices spike. A late spring snow melts in the Pacific Northwest, flooding hydro reservoirs; prices crash. A trader monitoring weather forecasts can position in spreads ahead of such events.

## Liquidity and trading venue fragmentation

Power trading is fragmented across many venues and bilateral deals. The NYMEX (New York Mercantile Exchange) trades futures on specific U.S. power hubs (PJM, MISO, Palo Verde, Henry Hub). European trading happens on ICE and EPEX. Bilateral OTC markets are large.

Spread liquidity is lower than single-hub liquidity. A trader wanting to buy "PJM minus MISO" power spread might have to execute two separate trades (buy PJM, sell MISO) or find a market maker offering a spread contract. This creates a bid-offer in the spread itself; the spread trader pays to cross this cost.

## Geopolitical and climate risks

Climate change is reshaping power spreads. Increasing temperatures reduce hydro availability in drought-prone regions and reduce cooling capacity at thermal plants. Water-scarce regions see higher power prices. Geopolitically, energy embargoes (e.g., sanctions on Russian gas) force price divergence between regions with alternative supply and those dependent on Russia.

The 2022 European energy crisis was a geopolitical/climate shock to spreads. Russian gas cutoff, low hydropower, and coal plant shutdowns created an unprecedented spread widening between gas-dependent regions and any region with alternative baseload or renewables.

<div class="wiki-seealso">

### Closely related
- [Commodity Swap](/wiki/commodity-swap/) — bilateral contract to exchange commodity cash flows
- [Commodity Futures Trading](/wiki/commodity-futures-trading-commission/) — regulation and trading of commodity contracts
- [Electricity as Commodity](/wiki/electricity-as-commodity/) — the nature of power as a tradeable good
- [Basis Risk](/wiki/basis-risk/) — risk from divergence of spot and futures prices

### Wider context
- [Commodity Carry Trade](/wiki/commodity-carry-trade/) — trading commodities based on storage costs
- [Natural Gas](/wiki/natural-gas/) — energy commodity that affects power pricing
- [Crude Oil](/wiki/crude-oil/) — energy commodity linked to power markets
- [Energy Complex Correlation](/wiki/energy-complex-correlation/) — how energy commodities move together

</div>

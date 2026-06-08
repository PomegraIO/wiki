---
title: "Power Grid Frequency Regulation and Ancillary Services"
description: "How grid operators maintain AC frequency stability through fast-response generation and battery storage, compensating providers for balancing services."
keywords:
  - power grid frequency regulation
  - ancillary services
  - frequency response
  - grid balancing
  - fast-response generation
  - grid stability
---

*The electricity grid must maintain AC frequency within a very tight band—typically 59.9 to 60.1 hertz in North America—because even small deviations can damage equipment and cascade into blackouts. **Power grid frequency regulation and ancillary services** are the mechanisms grid operators use to keep that balance, paying generators and battery operators to inject or absorb power within seconds when supply and demand shift.*

## Why Grid Frequency Matters

AC power systems are fundamentally synchronized machines. Every generator on the grid spins at the same frequency; every motor, transformer, and relay is designed to operate at that frequency. When demand suddenly spikes—say, millions of air conditioners turn on during a heat wave—the grid's frequency drops because there isn't enough generation online to keep all those motors spinning at full speed. Conversely, when a large generator trips offline or demand plummets, frequency rises. 

Even a deviation of ±1 hertz can trigger protective relays to disconnect lines and equipment, fragmenting the grid into isolated islands. That's why frequency must be held within a narrow deadband, typically ±0.05 hertz on well-managed systems. To do that, grid operators (the independent system operators, or ISOs, in most of North America) procure two types of balancing services: **regulation** and **reserve**. Together, they're called ancillary services, and they're priced separately from the energy itself.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Grid Frequency Regulation — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Regulation is the continuous micro-adjustment keeping frequency locked to its nominal target.</div>

|   |   |
|---|---|
| **Frequency band** | ±0.05–0.1 Hz (grid-dependent) |
| **Response time** | Seconds (regulation) to minutes (spinning reserve) |
| **Payment model** | Capacity fee + energy fee for actual dispatch |
| **Main providers** | Thermal generators, hydropower, batteries, demand response |
| **Typical deployment** | 1–10% of total grid capacity dedicated to regulation |

</aside>

## Regulation versus Reserve

**Regulation** is the smallest, fastest service. The grid operator issues real-time dispatch signals to participating generators and batteries, telling them to increase or decrease output every few seconds. A battery or fast-ramping gas turbine responds within seconds, compensating for the small, continuous fluctuations in supply and demand (and for random trips of equipment). The generator gets paid a capacity fee for being available and an energy fee for every MWh actually dispatched. Regulation is expensive because it requires expensive resources—batteries, gas peakers, hydro dams with fast governors—standing by at low capacity factors.

**Spinning reserve** (sometimes called spinning contingency reserve) is larger and slower. These are generators already connected and running at part-load, able to increase output over 10–30 minutes if a major generator fails. A coal or nuclear plant running at 80% output can increase to 100% fairly quickly. They're paid for availability (capacity) and rarely called upon; if called, they're paid an energy fee as well. Non-spinning reserve operates the same way but may take 30 minutes or longer to start; wind and diesel generators often provide this. At the very largest timescale, **replacement reserve** is slower-starting generation or emergency demand curtailment that backstops the system over hours.

## Who Provides Frequency Regulation?

Until the 1990s, grid operators relied almost entirely on thermal generators—coal and nuclear plants—to provide regulation. A coal plant running at 90% output could increase to 100% or drop to 80% in response to the ISO's control signals. The operator built a thin margin of capacity into the system for that purpose, and thermal plants earned steady revenue from standing by.

Today, regulation comes from a diverse portfolio:

**Gas peaker plants** spin fast governors and respond in seconds. They're built specifically for this work—high ramp rates, low minimum output—and have moved from baseload to the regulation and reserve market over the past two decades.

**Hydropower** is exceptionally good at regulation. A dam operator can adjust spillway and penstock flow in milliseconds, responding to tiny frequency deviations. In regions with lots of hydro (Pacific Northwest, Scandinavia, Quebec), frequency regulation is often free or nearly free because hydro plants provide it as a byproduct.

**Battery storage** (lithium-ion, flow batteries) has become the fastest and most precise regulation provider. A battery can inject or absorb power to the exact MW in under a second, with no ramp-rate limit and no minimum energy cost (unlike spinning a generator). As battery costs have fallen, they've captured a growing share of the regulation market, especially in places with high frequency deviations or renewable penetration.

**Wind and solar**, paradoxically, destabilize frequency in the short term (they vary minute-to-minute with cloud cover and wind gusts) but can provide regulation if equipped with fast power electronic converters. Some grids are beginning to contract frequency response from solar farms using grid-forming inverters.

**Demand response** can also provide reserve. A large industrial load (a chemical plant, a data center) can cut consumption on short notice, reducing the need for generation. Some grids offer lucrative contracts for curtailable industrial load.

## The Changing Economics of Regulation

The rise of renewables has transformed ancillary-services markets. Wind and solar don't spin; they don't have inertia—the physical resistance to frequency change that synchronous generators provide by their rotating mass. When a large wind farm suddenly drops offline (a gust shifts direction), there's no rotational mass to slow the frequency decay. The grid must rely entirely on electronic frequency response. Some grids have introduced new markets specifically for "synthetic inertia"—the ability of an inverter-based resource (a battery or smart inverter) to detect frequency change and inject power proportionally, mimicking the physics of a spinning generator.

This has made regulation more expensive and more valuable. Batteries, which can turn on and off in seconds with zero inertia cost, are now the marginal provider of regulation in many U.S. ISOs. Texas (ERCOT), California (CAISO), and the Mid-Atlantic (PJM) all report falling regulation costs as battery capacity has grown; other grids still rely heavily on thermal plants and see higher ancillary-services costs.

## How Grid Operators Price Regulation

Most ISOs run a separate auction for regulation capacity and energy. The process typically works like this:

1. The operator forecasts demand and generation for the next day.
2. It calculates how much regulation capacity it needs—usually 1–3% of peak load, depending on the region and renewable penetration.
3. Generators and battery operators bid a capacity price (per MW available) and an energy price (per MWh actually used).
4. The operator stacks bids from cheapest to most expensive and selects enough resources to meet its requirement.
5. All selected providers are paid the price of the marginal (most expensive) resource—a "uniform-price auction."

For example, if a battery operator bids $5/MW/hour for capacity and a gas turbine bids $7/MW/hour, the ISO might accept both. If that turbine is marginal (the last unit needed), both the battery and the turbine are paid $7/MW/hour, even though the battery would have accepted $5. This discourages strategic bidding but also allows inefficient generators to remain profitable.

## Real-World Scales

A typical large ISO like PJM (covering 13 U.S. states) procures about 500 MW of regulation for a 100,000 MW peak load—roughly 0.5% of capacity. Regulation costs run $50–$150 million per year, a small fraction of the total $20+ billion energy market. But in grids with higher renewable penetration or stronger hourly volatility, regulation costs can be 2–3x higher.

## See also

<div class="wiki-seealso">

### Closely related

- [Central bank](/central-bank/) — policy authority that sets the nominal frequency standard
- [Electricity market design](/stock-market/) — how generators and loads clear pricing
- [Reserve requirements](/reserve-requirements/) — the regulatory minimum balance sheet buffers
- [Futures contract](/futures-contract/) — how generators hedge long-term capacity obligations

### Wider context

- Commodity price volatility — why power and gas prices swing
- [Cost of equity](/cost-of-equity/) — discount rate for valuing generation assets
- [Free cash flow](/free-cash-flow/) — how to measure utility profitability
- [Market maker trading](/market-maker-trading/) — how intermediaries profit from bid-ask spreads

</div>

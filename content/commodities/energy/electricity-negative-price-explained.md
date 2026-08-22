---
title: "Negative Electricity Prices Explained"
description: "Why do electricity prices go negative? Understand grid economics, renewable oversupply, and the policy incentives that cause wholesale power markets to trade below zero."
keywords:
  - why do electricity prices go negative
  - negative electricity prices
  - wholesale power market
  - renewable energy oversupply
  - grid stability
  - curtailment economics
image: /svg/commodities.svg
---

*Electricity prices periodically go negative in wholesale power markets when excess generation cannot be stored or curtailed—a condition driven by renewable oversupply, inflexible baseload plants, transmission bottlenecks, and regulatory incentives that make it cheaper to pay other traders to take power off the grid than to shut down production.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Negative Electricity Prices — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">When supply outpaces demand, markets pay others to accept power.</div>

|   |   |
|---|---|
| **What causes it** | Renewable generation spikes + inflexible baseload units + transmission constraints |
| **Where it happens** | Regional interconnects (ERCOT, ISO-NE, SPP, Germany, Denmark) during low-demand/high-wind/sun periods |
| **Duration** | Usually 1–6 hours; rare multi-day stretches |
| **Who it affects** | Power generators (pay to stay online), [asset owners](/asset-allocation/), utilities managing [reserves](/reserve-requirements/) |
| **How to profit** | Store during gluts, sell into peak demand; dual-use assets (batteries, demand response) |
| **Physics barrier** | Electricity cannot be stored at grid scale without [capital-intensive](/capital-adequacy/) infrastructure |

</aside>

## Why the Power Grid Cannot Reject Supply

Electricity is generated and consumed in near-real-time; the grid operator must maintain instantaneous [balance](/balance-sheet/) between supply and demand. Unlike oil or natural gas, power cannot sit in inventory. If a generator produces 500 megawatts and the market only needs 400 megawatts, those 100 megawatts must go somewhere. The operator cannot simply "turn off the market"—every connected generator, wind farm, and solar plant is physically pumping electrons onto the network at the instant the sun shines or wind blows.

In the past, this problem solved itself simply: demand was reliably high during day and evening peak, and generators shut down at night or during low-demand periods. Baseload plants (coal, nuclear) ran continuously; [natural gas](/natural-gas/) plants ramped up and down to match hourly swings. The system had flexibility on the supply side.

The rise of renewable energy—wind and solar—flipped that balance. Wind farms generate most power in winter nights when demand is lowest. Solar farms dump peak output at midday when air conditioning loads are heaviest but still below peak evening demand. When weather favors generation (clear skies, strong winds) and demand is weak (mild weather, weekend, early morning), the grid can rapidly hit a physical constraint: too much power, nowhere to send it.

## Renewable Curtailment and the Least-Cost Option

Grid operators have four tools to manage oversupply:

1. **Curtailment**: Force generators to reduce output (pay renewable operators to stop producing).
2. **Export**: Ship power to neighboring regions via [transmission](/operational-risk/) lines.
3. **Demand response**: Pay industrial or commercial customers to consume more (turn up cooling, delay work).
4. **Storage**: Use batteries, pumped hydro, or other storage to absorb excess power.

Curtailment is expensive. It means paying the renewable operator not to generate at zero [marginal cost](/cost-of-debt/)—a waste of free wind or sunlight. Export is limited by transmission capacity. Demand response is limited to a few hundred megawatts. Storage is capital-intensive and often already operating.

When all four tools are exhausted or too expensive, the grid faces a bind: something must give. The operator can either:

- **Pay generators to stay online but reduce output** (economically inefficient but physically safe).
- **Let frequency rise or frequency drop, risking cascading blackouts** (physically catastrophic).

In regions with strong renewable penetration and strict grid codes (e.g., Germany, Denmark, parts of Texas), operators began experimenting with the market mechanism: offer a price so low—even negative—that generators would voluntarily reduce output rather than pay the penalty for oversupply.

## The Mechanics of Negative Prices

Negative wholesale prices mean the regional [market maker](/market-maker-trading/) or operator is paying the generator to accept power. In ERCOT (Texas) or ISO-NE (Northeast US), the day-ahead or real-time market sets a clearing price. If supply is vastly higher than demand, the marginal unit needed to balance the grid is not a traditional generator but a reduction of output. The price discovered is negative—e.g., −$50 per megawatt-hour.

A generator facing that price has a choice:

- Shut down (avoids the penalty but loses [operating margin](/operating-margin/) and risks penalties for unplanned outages).
- Keep running, sell at −$50/MWh, and **receive a $50 payment per MWh sold** (provided its operating costs are covered by other revenue streams, e.g., capacity markets, long-term contracts, or [forward contracts](/forward-contract/)).

A large natural gas plant with a multi-year contract to provide baseload power to a utility faces a locked-in [revenue](/revenue-recognition/) from that contract. Running the plant costs $20/MWh in fuel and [operations](/operational-risk/). If the spot price is −$50/MWh, the plant operators lose $70/MWh to the spot market but are indifferent: their contract revenue covers the operating cost. The negative price becomes a penalty for existing supply that cannot be quickly ramped down.

## Why Baseload Plants Cannot Turn Off Instantly

Coal and nuclear plants cannot be switched off and on like a light bulb. Coal plants take 4–8 hours to cool down safely; nuclear plants take longer. If a plant needs to rampage down (reduce output), it typically follows a ramp rate of 2–5% per minute, meaning even at maximum speed, a 1,000 MW plant takes 20–50 minutes to hit 500 MW. Fast-ramping [natural gas](/natural-gas/) plants can reach full ramp in 15–20 minutes, but even that is slow relative to a sudden surge in renewables.

A utility operating a baseload coal plant overnight during a winter low-demand period with strong wind generation faces a dilemma. If it ramps down the coal plant, it pays ramp-down costs and fuel waste. If it keeps running, the grid operator needs to clear the excess power somehow. The negative price is the mechanism that tells the coal plant, "We have more power than we can use; the market will pay you to stay online if you accept this negative price."

In high-renewable penetration regions, negative prices have become routine. Germany has seen negative prices for 10–20% of hours in recent years; Denmark even more. Texas's ERCOT system has experienced them since wind capacity reached 30% of nameplate.

## Policy Incentives That Accelerate Negative Prices

Several policy levers make negative prices more likely:

**Renewable portfolio standards and tax credits** mandate or subsidize wind and solar generation regardless of market price. A wind farm receiving a 30% investment tax credit or a federal production tax credit has an effective marginal cost of zero; it produces whenever the wind blows, independent of market signals.

**Capacity markets** pay generators (especially baseload units) a fixed amount per megawatt per year to be available, separate from energy [revenue](/revenue-recognition/). A nuclear plant might receive $200/kW/year in capacity payments, which covers a large share of its fixed costs. The plant is incentivized to stay online even at negative energy prices—the capacity market cushions the loss.

**Grid codes and reliability standards** often require plants to stay synchronized (connected and providing voltage support) even when they are not profitable to run. Disconnecting a large coal plant creates stability risks; the operator may be obliged to keep it online.

**Subsidized interconnection** for renewables means new wind and solar farms have no fixed contribution to the grid's cost of managing their variability. A conventional coal or gas plant pays congestion charges and grid fees; renewables in some regions pay less.

These policies were not designed to create negative prices—they aimed to decarbonize the grid and encourage investment in renewables. Negative prices are an unintended side effect, a sign that the grid is reaching high renewable penetration and that the energy market is now hitting its physical and regulatory limits.

## How Negative Prices Affect Different Market Participants

**Renewable operators** are generally unharmed. Most wind and solar contracts either guarantee a floor price or are [hedged](/derivatives-hedging/) with long-term agreements that isolate them from negative spot prices.

**Utilities with baseload portfolios** can lose substantially. A utility operating a coal plant and forced to absorb negative prices loses money on each megawatt-hour sold into a negative market.

**Consumers** may see benefits over years: negative prices incentivize new [battery storage](/reserve-requirements/) investment and demand-response infrastructure, which eventually improve grid efficiency and reduce average [electricity costs](/cost-of-equity/).

**Merchants and traders** with real-time flexibility—especially those operating batteries—can profit: buy during negative prices, sell at positive prices during peak hours.

**Electricity retailers** (those who buy wholesale power and resell to households) absorb volatility. If they are not [hedged](/interest-rate-swap/), negative prices in one hour offset by high prices in another hour can dramatically change their [margin](/operating-margin/).

## See also

<div class="wiki-seealso">

### Closely related

- [Wholesale power market](/stock-market/) — trading mechanisms, participants, and price discovery
- [Renewable energy grid integration](/interest-rate/) — technical and economic challenges of wind and solar
- [Capacity markets](/capital-adequacy/) — mechanism that pays generators to be available
- [Real-time electricity dispatch](/reserve-requirements/) — how grids balance supply and demand minute-by-minute
- [Storage economics and arbitrage](/carry-trade/) — profiting from price differences across time
- [Transmission congestion and pricing](/operational-risk/) — how network constraints affect power costs

### Wider context

- Commodity markets — pricing of all physical goods traded at scale
- [Market efficiency and price discovery](/price-discovery/) — when and why markets fail to allocate resources efficiently
- Regulation of utilities — oversight of power companies and grid operators
- [Energy policy and subsidies](/appropriations-bill/) — government incentives shaping energy markets

</div>

---
title: "Spark Spread Futures"
description: "A spread trade between natural gas futures and electricity futures that hedges or speculates on a generator's margin from producing power."
keywords:
  - spark spread
  - power generation margin
  - natural gas futures
  - electricity futures
  - generator margin
image: "/svg/derivatives.svg"
---

*A **spark spread** is the simultaneous purchase of natural gas futures and sale of electricity futures, capturing the margin a natural-gas-fired power plant earns by buying fuel and selling electricity. The spread represents the difference between the cost of natural gas and the revenue from generating and selling power—the economic return that motivates a generator to run its plant.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Spark Spread Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured products." />

<div class="wiki-infobox-caption">The power generator's core economic margin.</div>

|   |   |
|---|---|
| **What it is** | A spread trade: long natural gas, short electricity, capturing generation margin |
| **Standard ratio** | Depends on plant heat rate; typically 7–15 MMBtu gas per MWh electricity |
| **Primary users** | Power generators, utilities, power traders, private equity sponsors |
| **Futures exchanges** | NYMEX (natural gas), regional power hubs (PJM, ERCOT, ISO-NE) |
| **Profit from** | Generation margins widening; losses when margins compress |
| **Related spread** | [Crack spread futures](/crack-spread-futures/) for crude-to-fuel refining |

</aside>

## The economics of gas-fired power generation

A natural-gas-fired power plant is a fuel conversion machine: buy natural gas, burn it in a turbine to generate heat, use that heat to produce steam that drives an electricity generator. The efficiency of this process—how many BTUs of fuel it takes to produce one megawatt-hour (MWh) of electricity—is called the **heat rate**. A modern efficient plant might have a heat rate of 7 to 8 million British thermal units (MMBtu) per MWh; an older plant might require 12–15 MMBtu. The higher the heat rate, the less efficient the plant, and the higher its fuel cost per unit of output.

A generator's profitability depends on the spread between fuel cost and power revenue. If natural gas costs $5 per MMBtu and a plant has a 9 MMBtu heat rate, each MWh costs $45 in fuel. If electricity sells for $80 per MWh, the gross margin is $35 per MWh (ignoring operating costs, capital, and maintenance). If gas costs spike to $8 per MMBtu, fuel cost rises to $72 per MWh and margin compresses to $8. The spark spread future lets a generator lock in that margin before running the plant.

## Why "spark"?

The name refers to the spark or ignition in the turbine—the moment when gas combustion generates power. Unlike a refinery's "crack" (mechanical pressing of oil), a power plant's margin comes from controlled combustion.

## The standard heat-rate ratio

The spark spread contract ratio depends on the plant's heat rate. A plant with a 10 MMBtu/MWh heat rate would construct a spread by buying 10 MMBtu of natural gas futures and selling 1 MWh of power futures. (In practice, contracts trade in multiples: 10,000 MMBtu of gas, 1,000 MWh of power, to maintain the ratio.) This locks in the fuel-to-power margin for that plant's efficiency. A more efficient plant (lower heat rate) needs less gas per MWh, so the spread is constructed with a lower gas-to-power ratio.

Operators of multiple plants with different heat rates might take different spread positions for each, matching the ratio to each plant's actual efficiency.

## How generators use spark spreads to hedge

Power generators operate in a two-sided business: they commit to supply electricity to wholesale power markets or under long-term contracts, and they must secure fuel to produce it. If a generator commits to sell 1,000 MWh of power to a utility at a fixed price of $60/MWh for the next month, it faces fuel cost risk: if natural gas prices double, the cost of producing that power doubles and the margin evaporates. By buying a spark spread in futures—locking in the fuel cost relative to the power price—the generator can execute the power sale with confidence. Even if gas prices spike, the futures position gains value to offset the higher fuel cost.

Conversely, a power trader (or a generator with no committed customers) might use the spark spread to bet on margin changes. If a trader believes gas prices will fall faster than power prices, or if power prices will rise faster than gas, the spread will widen and the long position profits.

## Seasonal and real-time variations

Unlike soybeans or crude oil, electricity demand and pricing have extreme intraday and seasonal swings. Summer peak hours (afternoon and evening) have much higher prices than winter nights when demand is low. Natural gas prices are also seasonal—winter demand for heating pushes prices up—but the seasonal patterns for gas and power do not align perfectly. This creates seasonal swings in the spark spread. Summer peak power may have a wide margin (high power prices) while winter baseload power has a narrower or even negative margin (if natural gas demand is high). An operator might hedge summer peak generation but allow winter baseload to run at a loss (or not at all), depending on the spread structure.

## Regional power spreads

Electricity is not a uniformly traded commodity; it is tied to regional transmission and demand. The spark spread for natural gas-fired power in PJM (the Eastern power grid) is different from the spread in ERCOT (Texas) or California ISO. Each region has its own power futures market (where they exist) with different prices reflecting local supply, demand, congestion, and fuel mix. A generator in the Southwest might trade the spread differently than one in New England, even if they use identical plants.

## Carbon costs and environmental impact

In regions with carbon pricing (like the EU or California's cap-and-trade program), a generator must account for the cost of emitting carbon dioxide when burning gas. This is a hidden cost that reduces the effective spark spread. A plant burning gas emits roughly 0.4–0.5 metric tons of CO₂ per MWh. If carbon allowances cost $50 per ton, that adds $20–$25 per MWh to the fuel cost, compressing the margin. Some spark spread trades explicitly account for this by including the carbon cost in the calculation—these are called **dark spreads** (which also include coal-based generation) or **green spreads** (for renewable or low-carbon sources).

## Competing fuels and the merit order

Natural gas-fired plants do not operate in isolation. Power grids dispatch generators based on the cheapest available fuel. Coal-fired plants, nuclear plants, wind, and solar all compete. A natural gas plant's actual margin depends on whether it is called to run, which depends on its position in the **merit order**—the ranking of all available generators by fuel cost. On a day when wind is abundant, gas plants are not dispatched and earn zero margin. On a peak demand day with no wind, gas plants run and margins reflect whatever power prices are. A spark spread hedge in futures assumes a certain utilization; if the plant does not actually run, the hedge becomes a speculative bet rather than insurance.

## The relationship to other energy spreads

The spark spread is one of several energy margin trades. The **dark spread** measures coal-to-power margins (coal plant's margin). The **clean dark spread** is dark spread minus carbon costs. The **crack spread** (oil-to-fuel) can be chained with power margins to form energy complexity spreads. Traders use combinations of these to bet on entire energy system transitions—for example, a trade that is long spark spread and short dark spread profits if gas-fired plants displace coal.

## Execution and basis risk

A spark spread in futures locks in the fuel-to-power ratio at one point in time and place. But actual generation involves:
- Fuel procurement: buying gas on the day-ahead or real-time market, not necessarily at the futures price
- Power sales: selling electricity on real-time or day-ahead markets, which may diverge from futures prices
- Transmission and congestion: moving power from the plant to where customers are, with transmission costs and network constraints
- Outages and maintenance: the plant may not run at all due to forced outages or scheduled maintenance

These mismatch risks mean the futures spread is not a perfect hedge for the actual operational margin. A hedge fund or financial trader can execute a pure spark spread in futures, but an actual generator must coordinate the physical and financial sides, which is more complex and costly.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the standardized derivatives underlying the spark spread
- [Natural gas](/natural-gas/) — the fuel input in the spread
- [Crack spread futures](/crack-spread-futures/) — the refinery margin for crude oil
- [Crush spread futures](/crush-spread-futures/) — the agricultural processing margin for soybeans
- Commodity trading — the energy and commodity markets underpinning the spreads
- [Volatility](/historical-volatility/) — generation margins are a primary source of power market volatility

### Wider context

- [Hedging](/hedge-fund/) — how power generators lock in margins
- [Price discovery](/price-discovery/) — spark spreads help establish fair generation cost-plus pricing
- Energy markets — the broader context of fuel and power trading
- [Interest rate risk](/interest-rate-risk/) — also relevant to long-term power plant financing decisions

</div>

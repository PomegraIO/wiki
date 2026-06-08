---
title: "Spark Spread"
description: "The profit margin for a gas-fired power plant, defined as the difference between wholesale electricity prices and the cost of natural gas needed to generate it."
keywords:
  - spark spread
  - power generation economics
  - natural gas power
  - electricity markets
  - commodity spread
  - energy hedging
image: "/svg/commodities.svg"
---

*The **spark spread** is the difference between the wholesale price of electricity and the cost of the natural gas fuel burned to generate it. For gas-fired power plants, it represents the immediate profit margin available from turning fuel into electricity at current market prices.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Spark Spread — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodity trading." />

<div class="wiki-infobox-caption">The economic heartbeat of gas-fired generation.</div>

|   |   |
|---|---|
| **What it is** | Electricity price minus fuel cost (per unit of output) |
| **Unit** | $/MWh (dollars per megawatt-hour) |
| **Counterpart** | [Dark spread](/dark-spread/) (coal-fired plants) |
| **Key inputs** | Electricity futures, natural gas futures |
| **Used by** | Power generators, energy traders, utilities |
| **Risk type** | Commodity price risk, [spread risk](/credit-spread/) |

</aside>

## Why generators care about the spark spread

A gas-fired power plant sits between two markets: it buys fuel (natural gas) on one side and sells electricity on the other. When the spread widens—electricity becomes expensive relative to gas—the plant becomes highly profitable. When the spread narrows or turns negative, the plant loses money on every unit it generates. Operators track the spark spread obsessively because it drives operational decisions: do I run my plant today, or shut it down and wait for better prices?

The spread is never a fixed number. It changes minute-to-minute as electricity and gas prices move independently, driven by different forces. A cold snap drives up electricity prices (more heating demand) but can also drive up gas prices (more heating fuel demand), creating complex cross-currents. A warm day cuts both, sometimes favouring one fuel over the other.

## Calculating the spark spread

The textbook formula is deceptively simple:

Spark Spread ($/MWh) = Electricity Price ($/MWh) − [Natural Gas Price ($/MMBtu) × Heat Rate]

The heat rate is the efficiency metric: how many British thermal units of gas input are required to produce one megawatt-hour of electricity. A modern plant might have a heat rate of 7,000–8,000 BTU/kWh; older plants run 9,000–11,000. The worse the heat rate (higher number), the wider the gas cost portion of the calculation and the less profitable the plant becomes at any given gas price.

Example: if electricity trades at $50/MWh, gas at $3/MMBtu, and a plant's heat rate is 7,500 BTU/kWh, the spark spread is $50 − ($3 × 7.5) = $27.50/MWh. That plant generates a $27.50 margin per unit of output. Subtract operating costs (staff, maintenance, emissions allowances), and what remains is true profit.

In practice, generators also account for transmission losses, variable operating costs, and fuel quality adjustments, making real-world spreads slightly messier. But the core principle holds: electricity price minus fuel cost equals the margin available.

## When spreads go negative

A negative spark spread is the nightmare scenario: the plant would lose money by running. This happens when gas prices spike (a supply disruption, a sudden cold wave, or demand surge) faster than electricity prices rise. Generators facing negative spreads switch to dispatch mode: they shut down, accept demand reductions, or pay other generators to take load. Negative spreads can persist for hours during crises, forcing whole fleets offline.

Some plants are so inefficient—old coal or nuclear units with high heat rates or thermal constraints—that they operate even at thin or negative spreads because stopping and restarting is expensive. Others, like peaking plants built specifically for high-margin opportunities, sit idle unless the spread is very wide.

## Trading and hedging the spread

Sophisticated operators don't wait passively for spreads to present themselves. They actively hedge using futures contracts on electricity and natural gas, locking in margins months or even years ahead. A utility might sell electricity futures (locking in a price to sell) while simultaneously buying gas futures (locking in a fuel cost), thereby fixing the spread and protecting themselves against adverse price movements.

Energy traders, hedge funds, and principal power merchants use spark spread strategies to speculate on the future gap between these two commodities. They bet on mean reversion (spreads widen or narrow back to long-term averages), on seasonal patterns (summer peaks, winter valleys in typical electricity-gas correlations), or on structural shifts (say, retirements of coal plants, which might expand opportunities for gas).

The [crack spread](/crack-spread/) in oil refining follows the same logic—buy crude, sell refined products—and spark spread is its electrical equivalent. Both distil the core economic reality of energy transformation: buy low, sell high, and measure the margin.

## Regional variation and market structure

Spark spreads differ sharply by region. In areas with abundant wind or hydro, a low-cost renewable dispatch can compress spreads, making gas plants less profitable. In areas far from gas pipelines, transportation costs inflate the effective fuel price, tightening margins. Deregulated markets with transparent futures pricing (such as the US power grid operated by ISO and RTO operators) make spreads easy to observe; vertically integrated utilities in regulated markets may not disclose spreads as clearly.

The spread also reflects broader market structure: Where is generation capacity tight relative to demand? How much do renewables contribute (and do they receive subsidies that artificially depress electricity prices)? What are carbon costs in that jurisdiction? A plant in a carbon-priced region like the European Union faces a wider effective spark spread calculation because emissions allowances add to fuel cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Dark Spread](/dark-spread/) — the coal-fired equivalent
- [Natural Gas Liquids](/natural-gas-liquids/) — byproducts of gas processing as tradeable commodities
- [Netback Pricing](/netback-pricing/) — working backward from product value to wellhead economics
- [Futures Contract](/futures-contract/) — the instruments used to lock in spark spread margins
- [Commodity Spread](/credit-spread/) — the broader category of price differences between two related goods
- [Price Discovery](/price-discovery/) — how markets establish electricity and gas prices

### Wider context

- Natural Gas — the fuel underlying spark spread calculations
- [Electricity Markets](/stock-market/) — power trading structures (note: no direct electricity article; this is proximal context)
- [Operational Leverage](/leverage-ratio-forex/) — how thin margins amplify returns and losses
- [Hedge Fund](/hedge-fund/) — principal managers who trade spreads

</div>

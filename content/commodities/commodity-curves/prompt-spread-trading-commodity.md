---
title: "Prompt Spread Trading in Commodity Markets"
description: "Prompt spread trading in commodities captures near-term supply tightness by trading nearby futures contracts against each other."
keywords:
  - prompt spread trading
  - commodity spreads
  - futures spreads
  - contango backwardation
  - near-term supply tightness
  - commodity risk management
  - energy trading
image: "/svg/commodities.svg"
---

*A **prompt spread trade** profits from price differences between the nearest futures contracts in a commodity market, typically the front month versus the second or third month. Traders use these spreads to express views on near-term supply bottlenecks and seasonal imbalances—without betting on absolute price direction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Prompt Spread Trading — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities markets." />

<div class="wiki-infobox-caption">A directional bet on near-term supply stress, expressed through relative contract value.</div>

|   |   |
|---|---|
| **Core idea** | Long the front month, short the back; profits when the spread widens or tightens |
| **Markets** | Crude oil, natural gas, metals, soft commodities |
| **Typical structure** | Buy Month 1, sell Month 2 (or Month 3) |
| **Profit driver** | Supply tightness, seasonal demand spikes, logistical constraints |
| **Risk** | [Basis risk](/basis-risk/), convergence failure, rolling losses |
| **Key metric** | Spread width measured in cents or dollars per unit |
| **Time horizon** | Days to weeks; roll as front month expires |

</aside>

## How Prompt Spreads Work

A **prompt spread** is a [futures](/futures-contract/) position that goes long the nearest-expiry contract and short the next contract (or sometimes the third). If crude oil trades at $80 for the January contract and $77 for February, the spread is $3 wide—the "prompt" is stronger. A trader who believes January oil is undersupplied relative to February can go long the spread, pocketing the difference if it widens.

The appeal lies in sidestepping outright direction bets. You don't need to predict whether oil rallies to $90; you only need to guess whether supply stress will ease faster in February than January. This makes prompt spreads a workhorse tool for both speculators reading real-time supply news and producers managing [logistical constraints](/operational-risk/).

Spreads are quoted in absolute terms (the February contract minus the January contract) and often traded as a single instrument on exchanges. For example, a broker might quote "CL1CL2 at +$2.50," meaning February is trading $2.50 above January, and you can buy or sell that spread directly.

## Contango Versus Backwardation and Supply Signals

When the front month is cheaper than the back month—say, $77 for January and $80 for February—the market is in **[contango](/contango/)**. This usually signals ample supply; storage is cheap, and nobody is rushing to pull oil from the ground right now. A contango market is "normal." Prompt spreads widen in contango.

When the front month is dearer than the back—$80 for January, $77 for February—the market is in **[backwardation](/backwardation/)**. This screams supply tightness. Refiners need crude today, not in two months, so they pay a premium for immediate barrels. Backwardation spreads narrow (the difference shrinks), and widening backwardation—the gap growing bigger—signals intensifying near-term shortage.

A trader betting on a supply crisis buys a backwardated prompt spread, hoping January stays expensive relative to February as the supply crunch persists. A trader expecting the squeeze to ease sells the spread, pocketing gains as the backwardation flattens.

This inversion between front and back contracts is rare but dramatic. During the OPEC embargo of the 1970s and again in March 2020 (COVID storage collapse), energy markets flipped into violent backwardation, and prompt spreads moved in inches per day. Most of the time, contango dominates, and spreads move in cents.

## Real-World Application: Oil and Natural Gas

In crude oil, the front-month contract rolls over a few days before the first of the next month. A prompt spread trader watches this rolling schedule obsessively: when does the "front" become the "back"?

**Example:** A trader watches refinery maintenance schedules and forecasts that spare capacity will shrivel in late January due to seasonal turnarounds. She buys the January crude contract and sells February at a 2-cent contango ($0.02 per barrel). If refinery outages materialize and January crude rallies to a 5-cent contango over February, she exits the spread with a 3-cent/barrel gain—meaningful on 1,000-barrel positions.

Natural gas sees fiercer prompt spread activity. Winter demand swings wildly on weather, and pipelines have finite capacity. A cold snap can flip the prompt from a 20-cent contango into a 50-cent backwardation in a day, creating instant losses for unprepared traders and windfall gains for those positioned correctly. Traders monitor weather forecasts, storage injection/withdrawal schedules, and pipeline nominations (the declared flows for the next day) obsessively.

## Execution and Rolling

Prompt spreads are traded as a single order, not two separate legs, reducing execution risk. An exchange or broker quotes the spread, you buy or sell it once, and the position is marked as a spread. This is cleaner than legging into a position manually.

As expiration nears, the front contract converges toward spot price and volatility explodes. Prompt traders rarely hold into expiration; they roll—close the position days before the front month expires and simultaneously open the same trade in the next pair of contracts. Rolling costs money (you always exit at a slightly worse price than you enter), but it's the cost of staying in the game.

Costs accumulate over time. In a steep contango market, rolling up the curve costs you the difference each month. If you're long a spread and roll repeatedly in a growing contango, the cost compounds. This "roll drag" is why prompt spread traders are typically short-term operators, not buy-and-hold investors.

## Risk and Failure Modes

The biggest risk is [basis risk](/basis-risk/)—the spread doesn't move as expected. A trader goes long a prompt spread because she thinks January is tight, but a surprise announcement of emergency supply relief causes both January and February to fall in unison, and the spread doesn't widen. Both legs lose together, even though the spread itself stayed flat.

Convergence risk is acute. On expiration day, the front contract must converge to the [spot price](/spot-rate/); if it doesn't, there's an arbitrage. Large traders can physically deliver or accept delivery, forcing convergence. But if you're holding a spread position into the final days and liquidity dries up, you might get forced out at unfavorable prices.

Roll failure happens when the next contract doesn't trade enough volume. If you need to sell 1,000 crude contracts tomorrow to roll out of January into February, and February is illiquid, you'll move the market against yourself. This "gap risk" is real in thinly traded commodities or far-dated contracts.

Finally, counterparty risk arises if you're trading through an [over-the-counter](/over-the-counter-market/) derivatives dealer rather than an exchange. A dealer will quote you a spread, and you're exposed to that dealer's [credit risk](/credit-risk/).

## Prompt Spreads in Trading and Hedging

Speculators use prompt spreads to make directional bets on supply. A trader might make 5–10 bps per day in normal markets and 50 bps in volatile ones. The leverage is built in; a 1-cent spread move on 10,000 barrels is $100 in profit, but you only post margin on the spread, not the notional value of both legs.

Producers and refiners use prompt spreads to hedge logistics costs. A refiner buys crude oil forward; if she also shorts the prompt spread (betting on contango), she's locking in the storage and financing costs embedded in that contango. This allows her to manage her effective input cost more precisely than outright forwards alone.

Commodity traders also use prompt spreads to arbitrage complex supply-demand dynamics. A crude trader might observe that pipeline capacity from a producing region is constrained, making nearby barrels scarce, while a ship carrying distant barrels is en route. She goes long the prompt, betting the spread widens until the ship arrives.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — when deferred contracts trade above spot, signaling ample supply
- [Backwardation](/backwardation/) — when nearby contracts trade above deferred, signaling supply tightness
- [Futures contract](/futures-contract/) — the standardized contracts underlying spread trades
- [Basis risk](/basis-risk/) — the risk that two related prices don't move together as expected
- [Derivatives hedging](/derivatives-hedging/) — how producers and refiners use spreads to manage costs
- [Spot rate](/spot-rate/) — the current price, to which front contracts converge at expiration

### Wider context

- [Crude oil](/crude-oil/) — primary commodity for prompt spread trading
- [Natural gas](/natural-gas/) — another heavy user of prompt spread strategies
- [Over-the-counter market](/over-the-counter-market/) — where spreads are sometimes quoted bilaterally
- [Execution risk](/execution-risk/) — rolling and liquidity challenges in active trading

</div>

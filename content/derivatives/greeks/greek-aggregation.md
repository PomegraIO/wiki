---
title: "Greeks Aggregation"
description: "The process of summing and netting first- and second-order sensitivities across a multi-position options book to assess portfolio risk."
keywords:
  - greeks aggregation
  - portfolio risk
  - greek netting
  - delta exposure
  - option sensitivities
image: "/svg/derivatives.svg"
---

*A trader or risk manager aggregates greeks by adding together the [delta](/delta/), [gamma](/gamma/), [vega](/vega/), and [theta](/theta/) of every single position in their portfolio, revealing the portfolio's net directional bias, volatility exposure, convexity, and time decay. This aggregation transforms hundreds of individual option positions into a handful of risk numbers—the dashboard that drives hedging and trading decisions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Greeks Aggregation — portfolio-level risk summary</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and portfolio risk." />

<div class="wiki-infobox-caption">Summing sensitivities across positions reveals true portfolio exposure.</div>

|   |   |
|---|---|
| **What it is** | Netting [delta](/delta/), [gamma](/gamma/), [vega](/vega/), [theta](/theta/) across all option positions |
| **Also called** | Greeks reporting, book greeks, net risk, portfolio sensitivity |
| **Typical depth** | Total greeks + bucketed greeks (by tenor, strike, underlying) |
| **Frequency** | Daily, intraday, or real-time depending on market conditions |
| **Users** | Options traders, market makers, risk managers, compliance |

</aside>

## The aggregation process

A market maker's book might contain 500 individual option positions: calls, puts, at-the-money, deep in-the-money, expiring tomorrow, expiring in two years. Each position has four main greeks: [delta](/delta/), [gamma](/gamma/), [vega](/vega/), [theta](/theta/). (Sometimes risk also includes [rho](/rho/), interest-rate sensitivity, especially for longer-dated or bond options.)

Aggregation is simple arithmetic: sum the [delta](/delta/) across all 500 positions to get the book's net delta. Sum the [gamma](/gamma/) to get net [gamma](/gamma/). And so on.

For example:
- Position 1 (long 100 calls): delta +50, gamma +10, vega +300, theta −20
- Position 2 (short 200 calls): delta −100, gamma −25, vega −750, theta +50
- Position 3 (short 50 puts): delta −25, gamma −5, vega −150, theta +10
- **Net book**: delta −75, gamma −20, vega −600, theta +40

The result: the book is **short 75 deltas** (will lose £75 if the underlying rises £1), **short 20 gamma** (positions worsen with movement; large swings hurt), **short 600 vega** (will lose £600 if [implied volatility](/implied-volatility/) rises 1%), and **positive 40 theta** (gains £40 per day from time decay).

## Why aggregation matters

Without aggregation, a trader managing 500 positions has no visibility. They can't answer: "Are we net long or short this stock?" "What happens if the market crashes 10%?" "How much do we lose if volatility spikes?" Aggregation collapses complexity into a few numbers.

It also enables fast hedging decisions. If net delta is −75 and the trader wants to be neutral, they buy 75 shares. If net [vega](/vega/) is short 600 and they're concerned about a volatility pop, they might buy some longer-dated calls to cover (long [vega](/vega/)).

## Levels of detail

Aggregation can happen at multiple granularities.

**Top-level**: Total delta, total [gamma](/gamma/), total [vega](/vega/), total [theta](/theta/). One number for each greek.

**By underlying**: If the book spans multiple stocks or indices, aggregate greeks per underlying. Trader might be long delta on Stock A and short delta on Stock B, which matters operationally (they hedge each separately).

**By tenor** (via [vega bucketing](/vega-bucketing/)): Total [vega](/vega/) masked that the book is long 3M [vega](/vega/) and short 1Y [vega](/vega/). Bucketing unmasks term-structure exposure.

**By strike**: Sometimes useful for exotic options or volatility surface monitoring. A trader might be short [gamma](/gamma/) near-the-money and long [gamma](/gamma/) far out-of-the-money.

**By [implied volatility](/implied-volatility/) level**: Risk managers sometimes report greeks assuming volatility has moved ±1% or 2%, showing sensitivity across scenarios. ("If IV drops 5%, we gain £50,000 vega; if IV spikes 10%, we lose £100,000.")

## The second-order greek: gamma

[Delta](/delta/) is a first-order sensitivity (linear). [Gamma](/gamma/) is second-order (curved), capturing how delta changes. Many traders obsess over [gamma](/gamma/) aggregation because it's the most subtle and pernicious: a large positive [gamma](/gamma/) seems great (you're long volatility, you profit from moves), but it comes with a cost.

High [gamma](/gamma/) means [delta](/delta/) swings wildly as price moves. If the book is long [gamma](/gamma/), rebalancing to stay delta-neutral becomes expensive—you're always chasing; [delta](/delta/)] gets away from you on sharp swings. If short [gamma](/gamma/), you're paying for [delta](/delta/) hedges that keep becoming stale; you lose on volatility even if [implied volatility](/implied-volatility/) doesn't rise.

Aggregating [gamma](/gamma/) into a single number masks distribution. A portfolio might have net [gamma](/gamma/) of zero but be long [gamma](/gamma/) near-the-money and short [gamma](/gamma/) far out, making it vulnerable to moves away from current spot.

## Theta and time decay

Aggregated [theta](/theta/) tells you how much the book profits (or loses) per day from time decay, assuming nothing else moves. A trader who is [delta-hedged](/delta-hedging/) and long options is spending [theta](/theta/) to hold [gamma](/gamma/)—a classic payoff: you bleed money daily until a big move arrives, at which point [gamma](/gamma/) scalping and [delta](/delta/)-hedging profits compensate.

Conversely, a short-option seller collects [theta](/theta/)—"theta decay works in my favour"—but typically pays [gamma](/gamma/)] (they're short [gamma](/gamma/)). The book's aggregated [theta](/theta/) is often positive, but that's the premium sellers collected, not the edge.

## Real-time monitoring and limits

Large trading desks and market makers monitor aggregated greeks in real-time. Risk systems update [delta](/delta/), [gamma](/gamma/), [vega](/vega/), [theta](/theta/) continuously as prices and [implied volatility](/implied-volatility/) move. They often set limits: "We will not exceed 500 net delta," "Net [vega](/vega/) not to exceed ±1,000," "Net [gamma](/gamma/) not below −50." Traders who breach limits must rehedge.

These limits exist because oversized exposure can turn catastrophic. A trader with ±2,000 net delta is betting heavily on direction, which contradicts the notion of running a hedged, volatility-focused book. A trader with −200 net [gamma](/gamma/) is betting directionally against volatility; they profit if the market sits still and lose if it jumps.

## Interaction with other risk measures

Greeks aggregation is one lens. Risk systems also report [value-at-risk](/value-at-risk/) (VaR)—the largest loss likely in the next day under normal markets—and stress scenarios (e.g., "What if the S&P 500 drops 5% and [implied volatility](/implied-volatility/) spikes 20%?"). Aggregated greeks feed those models: knowing [gamma](/gamma/) helps you estimate [vega](/vega/) moves under stress.

Compliance and regulators care about aggregated risk too. [Capital adequacy](/capital-adequacy/) rules for banks often require large greeks to be hedged or held against capital. A European bank's [vega](/vega/) exposure might determine how much capital they reserve for their options business.

## The paradox of aggregation

Aggregation simplifies, but oversimplifies. A portfolio with net delta zero and net [gamma](/gamma/) zero seems balanced, yet might still suffer a catastrophic loss if [implied volatility](/implied-volatility/) moves in a way the [vega bucketing](/vega-bucketing/) profile doesn't capture. Or a massive shock forces correlations to 1, collapsing the diversification baked into the delta and [gamma](/gamma/) numbers.

Experienced traders use aggregation as a starting point, then drill into underlying positions, exposures by strike and tenor, and stress scenarios to find hidden risks. Numbers alone don't tell the story; context and intuition are required.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — directional exposure; aggregated to show net direction
- [Gamma](/gamma/) — convexity and rebalancing cost; aggregated to show net curve risk
- [Vega](/vega/) — volatility exposure; aggregated and bucketed by tenor
- [Theta](/theta/) — time decay; aggregated to show daily bleed or benefit
- [Delta Hedging](/delta-hedging/) — the primary use of aggregated delta numbers
- [Vega Bucketing](/vega-bucketing/) — a granular view of aggregated vega by time-to-expiry

### Wider context

- Greeks — the four sensitivities being aggregated
- [Option](/option/) — the underlying contract
- [Implied Volatility](/implied-volatility/) — the vol driving vega exposure
- [Value-at-Risk](/value-at-risk/) — a risk measure often built using greeks data
- [Black-Scholes Model](/black-scholes-model/) — the mathematical foundation for calculating greeks

</div>

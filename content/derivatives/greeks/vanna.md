---
title: "Vanna"
description: "The Greek measuring the sensitivity of delta to changes in implied volatility; critical for managing skew and volatility smile risk in options portfolios."
keywords:
  - vanna
  - options greeks
  - delta sensitivity
  - implied volatility
  - volatility skew
  - options risk
---

*The **vanna** (or "volga delta") is an options Greek that measures how an [option](/option/)'s delta changes in response to shifts in [implied volatility](/implied-volatility/). It captures a second-order effect: volatility moves, delta adjusts, and the hedge ratio must be rebalanced. For traders managing [volatility skew](/volatility-smile/) and large multi-leg positions, vanna is as essential as delta itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vanna — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options." />

<div class="wiki-infobox-caption">The bridge between delta hedging and volatility regimes.</div>

|   |   |
|---|---|
| **What it is** | Greek measuring the cross-derivative of option price with respect to spot price and implied volatility |
| **Mathematical form** | ∂Δ / ∂σ (delta's sensitivity to volatility) or equivalently ∂Γ / ∂σ (gamma's sensitivity to volatility) |
| **Units** | Delta per percentage point of volatility (e.g., 0.05 means delta increases by 0.05 for every 1% rise in IV) |
| **Sign pattern** | Typically positive for [calls](/call-option/) (out-of-the-money more sensitive), negative for [puts](/put-option/) |
| **Relevance** | Critical in volatility skew strategies, [volatility smile](/volatility-smile/) trading, and rehedging cycles |
| **Related greeks** | [Delta](/), [gamma](/), [vega](/), [theta](/), [volga](/vega/) |
| **Hedging implication** | High vanna positions are vulnerable to simultaneous moves in price and volatility |

</aside>

## Why delta hedges fail during volatility regime shifts

A trader buying a [call option](/call-option/) and delta-hedging it expects the hedge to neutralize directional risk: if the stock rises, the call gains and the short stock position loses by roughly the same amount. But this works only if delta is constant. In reality, delta drifts. A stock rally often coincides with rising confidence and falling implied volatility, which reduces delta. The hedge unwinds, and the trader finds herself unintentionally short volatility.

Vanna quantifies this drift. When implied volatility rises, out-of-the-money calls become more valuable relative to at-the-money calls, so their deltas climb. A call trader who was delta-neutral suddenly becomes long delta and must sell stock to re-hedge. If volatility is rising fast, the trader is forced to sell into a rally, booking a loss. Conversely, when volatility falls, deltas of out-of-the-money calls shrink, and the trader must buy stock to re-hedge, this time buying into a sell-off.

This vanna effect is why large [options](/option/) positions can blow up during quiet markets. A trader confident in a flat market might build a complex multi-leg position, unaware that a small volatility move will force repeated hedging trades that bleed P&L.

## The mechanics: gamma and volatility

Vanna is the mixed partial derivative of option price: ∂²C / ∂S ∂σ, where C is the option price, S is spot, and σ is volatility. Rearranging, vanna also equals ∂[gamma](/gamma/) / ∂σ—the sensitivity of [gamma](/gamma/) to volatility. This is intuitive. [Gamma](/gamma/) measures the rate at which delta changes with spot moves. If volatility falls, gamma flattens: spot moves produce smaller delta changes. If volatility rises, gamma sharpens. Vanna captures this shift.

In the [Black-Scholes model](/black-scholes-model/), vanna is largest for at-the-money options and shrinks for deep in-the-money or out-of-the-money contracts. The sign and magnitude depend on the option type: calls have positive vanna (higher volatility increases their deltas), and puts have negative vanna (higher volatility decreases their deltas, making them less likely to be exercised).

For a trader holding a portfolio of calls and puts, net vanna can be positive, negative, or zero. A long [call](/call-option/) / short [put](/put-option/) spread, for example, has positive vanna: rising volatility boosts the call's delta more than it reduces the put's delta. A trader can deliberately construct a vanna-neutral portfolio by mixing [calls](/call-option/) and [puts](/put-option/) in specific ratios.

## Trading vanna exposure: the volatility skew

Vanna exposure is often implicit in [volatility skew](/volatility-smile/) trades. Equity [puts](/put-option/) out-of-the-money trade at higher implied volatilities than calls, creating a skew where [protective puts](/protective-put/) are expensive. A trader might sell deep out-of-the-money calls and buy at-the-money calls, pocketing the skew premium. But this trade is long vanna: if the stock rises and volatility falls (a common regime), the short out-of-the-money calls lose delta faster than the long at-the-money calls gain it. The position unwinds, and the trader is forced to adjust the hedge repeatedly, eroding the skew premium that was the whole point of the trade.

Conversely, a short skew trade—selling the overpriced puts and buying cheaper calls—is short vanna. This trade profits if volatility rises or falls in lockstep with spot moves, but loses if price and volatility [diverge](/). A trader who understands vanna can quantify this risk upfront and decide whether the skew premium justifies the vanna drag.

## Rehedging cycles and transaction costs

Vanna matters most during rehedging. A large portfolio of options, say a portfolio of [covered calls](/covered-call/) or a [collar](/), requires periodic adjustments as delta drifts. If the portfolio is long vanna, delta drifts accelerate when volatility rises, forcing more frequent rehedges and higher transaction costs. If it's short vanna, rehedges are less frequent but larger, with their own cost profile.

Professional traders model the expected cost of vanna-driven rehedges using Monte Carlo simulations. They estimate the probability distribution of spot and volatility moves over the hedging interval and calculate how many times the portfolio will breach a delta threshold (say, +/- 5 delta) and require rehedging. High vanna portfolios trigger more rehedges; the trader then decides whether the option strategy's revenue justifies the rehedging cost.

## Vanna in volatility smile and skew models

In models that capture [volatility smile](/volatility-smile/) (where implied volatility varies by [strike](/strike-price/)—not constant as Black-Scholes assumes), vanna becomes essential. Smile models like SABR or local volatility treat volatility as a function of both spot price and the option's strike. As spot moves, the entire smile shifts, and an option's delta changes not just because of the option's intrinsic [gamma](/gamma/), but because the smile itself moves. Vanna in smile models is much larger and more variable than in a flat-volatility world.

A trader who ignores vanna in a smile-heavy market (like equity index options, where skew is pronounced) can face surprise P&L swings. A seemingly stable, delta-neutral portfolio becomes unbalanced when the smile tilts or flips.

## Estimation and hedging vanna

Traders estimate vanna by bumping implied volatility up and down by small increments (say, 0.01 or 0.25 percentage points) and recalculating delta at each level. The slope of the delta-versus-volatility curve is vanna. For a portfolio of options, vanna is the weighted sum of individual vannas.

To hedge vanna, traders buy and sell options that have opposite vanna exposure. For example, a trader holding a long vanna position (long out-of-the-money calls) might hedge by selling a different call (with different strike and maturity) that has negative vanna. This creates a vanna-neutral position that isolates other exposures. Because vanna hedges typically involve selling options at lower implied volatility or buying at higher IV, hedging vanna can be expensive and reduce the strategy's potential return.

Some traders accept vanna risk as a cost of their strategy. A [covered call](/covered-call/) portfolio—owning stock and selling calls—has negative vanna; the trader accepts this risk as the price of generating call premium. Other traders actively manage vanna by trading [variance swaps](/), [volatility swaps](/), or exchange-traded [volatility products](/), which allow more precise control over volatility exposure.

## See also

<div class="wiki-seealso">

### Closely related

- Delta — the primary sensitivity; vanna measures delta's drift
- [Gamma](/gamma/) — convexity; vanna is gamma's sensitivity to volatility
- Vega — overall volatility sensitivity; vanna is a component of the full volatility risk
- [Implied Volatility](/implied-volatility/) — the volatility input that vanna reacts to
- [Volatility Smile](/volatility-smile/) — the context in which vanna matters most
- [Option](/option/) — the instrument whose vanna is being measured
- [Black-Scholes Model](/black-scholes-model/) — the pricing framework in which vanna was first formalized

### Wider context

- Theta — time decay that often offsets vanna gains
- [Covered Call](/covered-call/) — a strategy with negative vanna exposure
- [Protective Put](/protective-put/) — a strategy where vanna interacts with skew
- [Hedge Fund](/hedge-fund/) — professional vehicles that actively trade volatility and vanna
- Options Greeks — broader category of sensitivity measures

</div>

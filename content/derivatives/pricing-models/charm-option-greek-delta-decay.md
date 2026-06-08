---
title: "Charm: How an Option's Delta Changes With Time"
description: "Charm measures how delta drifts as expiration approaches, forcing dynamic hedgers to rebalance even when the underlying price stays flat."
keywords:
  - charm option greek delta decay
  - delta decay over time
  - option charm greek time decay
  - dynamic hedging rebalance delta
---

*An option's [delta](/delta/)—the rate at which its price changes with the underlying—is not constant. As expiration approaches, **charm**, the rate of delta decay over time, forces traders to continuously rebalance hedges even when the underlying asset price never moves. Charm is the second derivative of option value with respect to both time and price, or equivalently, the time decay of delta itself. Understanding charm is essential for anyone managing dynamic hedging programs or trying to model the true cost of maintaining option positions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Charm — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives."/>

<div class="wiki-infobox-caption">Charm quantifies how delta decays as days to expiration shrink, independent of price moves.</div>

|   |   |
|---|---|
| **Other name** | Delta decay, DdeltaDt |
| **What it measures** | Change in delta per day, holding price constant |
| **Sign for a long call** | Typically negative (delta shrinks near expiry) |
| **When it matters most** | Short-dated, at-the-money options |
| **Risk it highlights** | Rebalancing drag and gamma losses near expiry |
| **Related Greeks** | [Gamma](/gamma/), [Theta](/theta/) |

</aside>

## Why Delta Changes With Time

In the [Black-Scholes model](/black-scholes-model/), an option's value depends on five inputs: underlying price, strike, time to expiration, volatility, and the risk-free rate. As any of these change, the delta shifts.

Most traders watch price and gamma (how delta responds to price moves). But time itself reshapes delta even with zero price movement. Here's the intuition:

Imagine a call option that expires tomorrow. If it is deeply out-of-the-money, its delta is nearly zero—moving the stock up or down a dollar barely changes the option's worthless state. Overnight, that option either expires (delta → 0) or the stock rallies hard (delta → 1). There's very little in between; delta is "dead" until the last second, then flips sharply if the stock moneyness shifts.

Now imagine that same call with one month to expiration. A one-dollar stock move has meaningful probability of pushing the option in or out of the money by expiry. Delta is responsive to price; it's "alive." The option value curve is smoother, less extreme.

As days pass, the probability landscape tightens. Extreme moves become less likely (assuming constant volatility), so delta becomes more sensitive to whether the underlying is already above or below the strike. An at-the-money call's delta—nominally 0.50 in the Black-Scholes world—will rise as expiration nears (it becomes more likely that the call finishes in the money). An out-of-the-money call's delta sinks (the option has less time to rally into the money). The underlying didn't move; only the calendar did.

That shift in delta per unit time is charm.

## The Mathematics of Charm

Charm is formally the mixed partial derivative:

**Charm = ∂²V / (∂S ∂t)**

where V is option value, S is underlying price, and t is time. In practical terms, it is the change in delta (per day or per year) as time passes, holding the underlying price steady. It is also equal to the partial derivative of [gamma](/gamma/) with respect to time:

**Charm = ∂Γ / ∂t**

In the Black-Scholes framework, charm has a closed-form expression. For a call option:

**Charm ≈ −[θ·Γ + ρ·Vega] / (underlying price)**

where [theta](/theta/) is time decay, gamma is the price-sensitivity of delta, and [vega](/vega/) is volatility sensitivity. The exact algebra varies, but the intuition is consistent: charm blends the effects of theta and gamma, showing how the rebalancing burden (gamma) shrinks or grows as time passes.

For a **long call** (bought call), charm is typically **negative**. The option's delta decays toward zero as expiration approaches (if the call stays out-of-the-money) or toward one (if it is in the money). The negative charm of an out-of-the-money call means the trader holding that call loses responsiveness to stock moves each day; they must sell stock to rebalance their hedge, locking in losses.

For a **long put**, charm is also usually negative for out-of-the-money puts.

**Short options** (sold calls or puts) tend to have positive charm on out-of-the-money positions; the seller benefits as delta shrinks toward zero because the position becomes easier to hedge.

## Charm in Action: The Rebalancing Drag

Consider a practical example. A trader buys a call option struck at $100 on a stock trading at $95. The call has 30 days to expiration, is out of the money, and carries a delta of 0.25 (meaning a $1 rise in the stock increases the call value by ~$0.25).

To hedge the call, the trader shorts 0.25 shares. The call position + short stock position is delta-neutral.

Ten days pass. The stock is still at $95. Under Black-Scholes (with typical volatility), the call's delta has fallen to, say, 0.20. The option is farther in the "dead" zone; expiration is imminent, and the stock has not rallied, so the call's leverage to a stock move has weakened.

Now the trader is delta-imbalanced: the call (delta 0.20) is hedged by a short position of 0.25 shares. The trader is actually short an extra 0.05 delta. To rebalance, the trader must **buy back 0.05 shares**. But the stock is still at $95, so this rebalance results in a loss versus the entry price for that 0.05 hedge.

This loss is charm. Over many rebalances, charm represents the frictional cost of keeping a hedged option position neutral as expiration approaches—not because the market moves, but because time shrinks the option's leverage. Sellers of options profit from charm (they receive premium that covers these rebalancing losses); buyers lose to it.

## Charm vs. Gamma vs. Theta

Charm, [gamma](/gamma/), and [theta](/theta/) are all second-order Greeks, and their relationships matter:

- **Gamma** ∂²V / ∂S²: how delta changes with the underlying price.
- **Theta** ∂V / ∂t: how the option value decays per unit time (assuming price and other variables are held steady).
- **Charm** ∂²V / (∂S ∂t): how delta decays per unit time (or equivalently, how gamma evolves as the calendar advances).

In the Black-Scholes world, there's a mathematical identity linking these: when volatility is constant, a portion of theta is "paid" by gamma (convexity losses from rebalancing). Charm quantifies precisely how that trade-off shifts as expiration looms.

For a trader:

- **Gamma tells you:** if the stock moves $1, your delta changes by this amount.
- **Theta tells you:** per day of calendar passage, your option value changes by this amount (all else equal).
- **Charm tells you:** per day of calendar passage, your delta changes by this amount, forcing rebalancing to maintain the hedge.

A long-dated, at-the-money call has high gamma and negative charm. Small calendar passage causes a large decay in delta (large negative charm). A short-dated, deep out-of-the-money call has low gamma and (in absolute terms) low charm; delta is already near zero and stays near zero.

## Charm and Gamma Losses

Traders often conflate charm losses with gamma losses, but they are distinct (though related). **Gamma losses** occur when the underlying price whipsaws: you buy low, the stock rallies and you sell, the stock falls and you buy again—locking in losses. Gamma losses depend on the realized volatility of price moves.

**Charm losses** occur even if the price never moves: you rebalance the hedge lower each day simply because delta shrank, and you sell the hedge at prices you previously bought it at. Charm losses depend only on time passage and the profile of gamma over time.

A trader can experience charm losses even in a perfectly calm, zero-volatility market. A buyer of options suffers both: actual realized volatility (gamma losses) plus the inexorable decay of leverage (charm losses). The option seller profits from both, provided they are short gamma and benefit from low realized volatility.

## Charm in Practice and Model Dependency

Charm is highly **model-dependent**. In the Black-Scholes framework (constant volatility), charm has a precise closed form. But real markets violate Black-Scholes assumptions:

- **Volatility is stochastic** and changes with time and price (volatility smile, term structure).
- **Jump risk** (sudden, discrete price gaps) is not captured.
- **Transaction costs** create friction that changes the effective rebalancing schedule.

As a result, traders often rely on empirical estimates or on multi-factor option pricing models (such as Heston, SABR, or local-stochastic-volatility) that allow volatility to drift. Charm estimates from these models can differ significantly from naive Black-Scholes calculations.

Very short-dated options (days to expiration) and at-the-money strikes show the largest charm effects in both direction and magnitude. Deep in-the-money and deep out-of-the-money options have charm close to zero because their delta is already pinned near 0 or 1.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the rate of change of option value with underlying price
- [Gamma](/gamma/) — the rate of change of delta with underlying price
- [Theta](/theta/) — the rate of change of option value with calendar passage
- [Vega](/vega/) — sensitivity to volatility changes
- [Black-Scholes model](/black-scholes-model/) — the foundational option pricing framework
- [Option](/option/) — the derivative contract underlying all Greeks

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — the practice of offsetting option risk with underlying positions
- [Volatility smile](/volatility-smile/) — how real markets deviate from constant volatility
- [Strike price](/strike-price/) — the fixed price at which an option can be exercised
- [Expiration date](/expiration-date/) — when an option ceases to exist
- [Time value](/time-value/) — the portion of an option's premium attributable to time remaining

</div>

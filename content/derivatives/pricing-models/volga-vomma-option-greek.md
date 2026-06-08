---
title: "Volga (Vomma): The Convexity of Vega in Options Pricing"
description: "Volga (vomma) is the second derivative of option price with respect to volatility, measuring vega convexity. Essential for pricing options on volatility and volatility swaps."
keywords:
  - volga vomma option greek
  - vega convexity derivatives
  - option greeks volatility
  - second-order option sensitivity
  - volatility derivative pricing
image: /svg/derivatives.svg
---

*The **volga** (also called vomma) is the second-order [option](/option/) greek—the rate of change of [vega](/vega/) with respect to implied volatility—measuring how much an option's sensitivity to volatility itself changes as volatility moves. For traders and risk managers pricing [volatility swaps](/volatility-smile/), exotic [options](/option/), and volatility derivatives, volga is essential because it quantifies the convexity of volatility exposure, a risk that first-order greeks like vega cannot capture.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volga (Vomma) — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A second-order greek that reveals the convexity of vega—critical for volatility traders and exotic derivative pricing.</div>

|   |   |
|---|---|
| **Definition** | d(vega)/d(implied volatility); second derivative of option price w.r.t. vol |
| **Symbol** | Volga or vomma; sometimes λ or Λ |
| **Units** | Option value change per one-percentage-point change in vega, per percentage-point vol move |
| **Sign convention** | Usually positive for at-the-money options; negative for deep ITM/OTM |
| **Use case** | Hedging volatility of volatility; pricing volatility derivatives |
| **Calculation** | Analytical (Black-Scholes) or numerical approximation |
| **Related greeks** | [Vega](/vega/) (first derivative w.r.t. vol), [gamma](/gamma/) (curvature in spot), theta (time decay) |

</aside>

## Understanding the second derivative

An [option](/option/) price depends on underlying spot price, time to expiration, [interest rates](/interest-rate/), dividends, and implied volatility. The first-order greek [vega](/vega/) measures how much the option value changes when implied volatility moves by 1%. For instance, if an option has a vega of 0.05, a 1% increase in volatility will increase the option's value by approximately 0.05 units.

But vega itself is not constant; it changes as volatility changes. Volga quantifies that change. If volga is 0.02, and volatility rises by 1%, then vega itself will increase by approximately 0.02. On the next 1% volatility move, the option's price will change by the new vega amount (0.05 + 0.02 = 0.07), not the original 0.05.

This second-order effect matters enormously in volatile markets and when hedging volatility derivatives. A trader who hedges [delta](/delta/) and [vega](/vega/) but ignores volga is exposed to nonlinear volatility risk—the risk that increases in volatility make the option more sensitive to further volatility changes, amplifying losses or gains.

## Convexity: why sign matters

For a typical European-style call or put option, volga is positive near the money—meaning vega *increases* as volatility rises. This is a convex relationship: the farther out of the money an option is, the more sensitive it becomes to volatility when volatility itself increases.

Conversely, for deep in-the-money or out-of-the-money options, volga can be negative. These options become *less* sensitive to further volatility changes as volatility rises, because they are already far from the strike and less likely to move in or out of the money.

This convexity matters for structured strategies. A trader who is long volatility exposure via long [call options](/call-option/) and short volatility via short puts is long volga—they benefit if volatility becomes more volatile. A trader pursuing a volatility arbitrage or trading [variance swaps](/swap/) must account for volga to understand the true profit/loss profile across a range of market moves.

## The Black-Scholes formula and volga

Under the [Black-Scholes model](/black-scholes-model/), volga has a closed form. For a European option, volga is proportional to vega times the quantity (d1 * d2), where d1 and d2 are the standard normal quantiles in the Black-Scholes formula. This means volga depends on the moneyness (in-the-money vs. out-of-the-money) and time to expiration.

At-the-money options with long maturities have the highest absolute volga. As expiration approaches, volga decays—the relationship becomes nearly linear, and second-order effects flatten. This dynamic is critical for options traders managing gamma and volga as expiration nears.

In practice, traders compute volga by bumping implied volatility up and down (e.g., by 0.01%) in a pricing model (Black-Scholes, local [volatility](/implied-volatility/), or stochastic volatility) and observing how vega changes. This numerical approach works with any pricing model and avoids the need to derive closed-form formulas.

## Practical use: volatility derivatives and swaps

A volatility swap is a contract whose payoff depends on realized volatility over a period. Pricing and hedging volatility swaps requires understanding both first-order vega exposure and second-order volga effects. If realized volatility is high, the swap becomes more valuable, and a trader long the swap is exposed to further volatility increases—a positive volga position.

Exotic options—those with [barrier](/barrier-option/) features, [American-style](/american-option/) exercise, or path-dependent payoffs—often have nontrivial volga. For example, a knock-in [call option](/call-option/) has lower vega than a standard call (because it can expire worthless if the barrier is not touched), but its vega convexity is different. Traders must measure volga to hedge these exposures correctly.

In volatility trading, a strategy that buys short-term options and sells long-term options can be long vega (exposure to a volatility increase) but short volga (exposure to an increase in volatility itself). Understanding the sign and magnitude of volga is essential to managing the compound risk.

## Limitations and assumptions

Volga, like other greeks, is based on infinitesimal or small moves in underlying variables. In large market shocks—a sudden spike or crash in volatility—the linear (or second-order) approximation breaks down. Traders also use higher-order greeks (e.g., vomma of vomma, or the third derivative) in extreme scenarios, though these are less commonly quoted.

Additionally, volga assumes that implied volatility surfaces move smoothly. In reality, [volatility smiles](/volatility-smile/) (the curve of implied volatility across strikes) can twist and tilt unpredictably. A change in the overall volatility level may or may not accompany a change in the skew, altering the effective volga exposure. Models that account for stochastic volatility—where volatility itself is a random variable with its own dynamics—provide a richer picture, but the Black-Scholes volga remains a useful first approximation.

## Hedging volga exposure

A trader long volga (exposed to an increase in vega sensitivity) can hedge by entering into a variance swap or volatility swap, which has its own volga profile. Alternatively, selling out-of-the-money options (which have lower volga) or buying at-the-money options (high positive volga) adjusts the net volga position.

In regulated dealer desks, volga risk is often managed alongside vega and gamma, though volga is less stringently capital-weighted in standard risk frameworks like [Value-at-Risk](/value-at-risk/). Over-the-counter derivatives desks may compute volga daily and adjust positions if it drifts outside tolerance bands.

## See also

<div class="wiki-seealso">

### Closely related

- [Vega](/vega/) — first derivative of option price w.r.t. implied volatility
- [Gamma](/gamma/) — second derivative of option price w.r.t. spot price (analogous to volga but for delta)
- [Delta](/delta/) — first derivative of option price w.r.t. spot price
- [Theta](/theta/) — time decay; first derivative w.r.t. time
- [Black-Scholes model](/black-scholes-model/) — standard option pricing framework

### Wider context

- [Option](/option/) — derivative contract; right to buy or sell at a fixed price
- [Implied volatility](/implied-volatility/) — volatility level backed out from market option prices
- [Volatility smile](/volatility-smile/) — curve of implied vol across strikes and expirations
- [Derivatives hedging](/derivatives-hedging/) — risk management via offsetting positions
- [Variance swap](/swap/) — bet on realized vs. implied volatility

</div>

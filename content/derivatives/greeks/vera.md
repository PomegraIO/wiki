---
title: "Vera"
description: "The sensitivity of rho (interest-rate risk) to changes in implied volatility, linking interest-rate and volatility risks in option pricing."
keywords:
  - second-order greek
  - interest-rate risk
  - volatility sensitivity
  - option greeks
image: "/svg/derivatives.svg"
---

*Vera is a second-order Greek that quantifies how an option's interest-rate sensitivity (rho) changes as implied volatility moves. It reveals a subtle but important interaction between [interest rates](/interest-rate/) and volatility regimes, exposing hidden risks in portfolios that seem to isolate these two dimensions separately.*

## The forgotten link between rates and volatility

Most option traders think of interest rates and volatility as independent risk factors. A small change in rates affects the option's cost of carry and discounting — the domain of rho. A change in volatility shifts the range of likely future prices — the domain of [vega](/vega/). But vera shows they are not truly separate: as volatility rises, the sensitivity to rates changes in predictable ways.

This matters because interest-rate expectations and volatility regimes are often linked in reality. During recessions, central banks cut rates and volatility spikes simultaneously. During periods of low inflation and stable growth, rates hold steady and volatility contracts. A portfolio hedged for rho and vega separately might experience unexpected losses if vera exposure is ignored when these regimes shift together.

Formally, vera is the second partial derivative of option price: the derivative of rho with respect to implied volatility, sometimes written as ∂rho/∂σ. It is the rate-vol cross-gamma, and like most second-order Greeks, it is small on an absolute basis but compounds over multi-factor moves.

## Why vera is typically negative

For most options, vera is negative. This means that as volatility rises, the option's rho (sensitivity to interest-rate changes) becomes less pronounced in absolute terms. Intuitively, when volatility is high, the intrinsic value dominates the time-value decay calculations, and the impact of discounting via interest rates becomes secondary.

Consider a long call option. Its rho is positive: a higher interest rate reduces the present value of future payoffs and decreases the cost of deferring exercise, both of which slightly reduce call value. But the magnitude of this rho effect shrinks when volatility rises, because the option's value is now driven primarily by the wide range of possible terminal prices, not by interest-rate-driven discounting. This negative vera is almost universal for vanilla options near the money.

However, vera can be positive for some deep out-of-the-money options or in certain exotic structures where the interest-rate impact on the underlying's forward price dominates. The sign and magnitude of vera depends on the option's strike, expiry, and the current volatility level.

## Vera in fixed-income-derivatives books

Vera becomes material in portfolios mixing equities and fixed-income derivatives. A bank managing a book of interest-rate swaptions (options on [interest-rate](/interest-rate/) swaps) must account for vera because the underlying interest-rate volatility and the volatility of volatility both drive rho changes.

Similarly, a portfolio of equity options on dividend-paying stocks involves interest-rate risk (through the cost of carry and discounting) and equity volatility risk. The cross-effect — vera — determines whether hedging the two factors separately will be sufficient or whether the hedge has hidden slippage when both rates and equity volatility move together.

## Computing vera

Like most second-order Greeks, vera can be computed analytically under Black–Scholes but is usually calculated numerically. Risk systems shock volatility up and down (say, ±1%), recalculate rho for each scenario, and compute the change in rho per unit volatility move. Modern systems report vera automatically, though many traders remain unaware of it until a multi-factor stress event reveals it.

Vera is typically small relative to vega or rho, but the absolute size depends on the option's time value and moneyness. A long-dated at-the-money option has larger vera than a short-dated or far-out-of-the-money option.

## Real-world scenarios where vera matters

During the 2022 interest-rate tightening cycle, central banks simultaneously hiked rates sharply and volatility spiked. A portfolio that was hedged for rho and vega separately but ignored vera could suffer unexpected losses. An increase in both rates and volatility would move rho and vega in the expected directions, but vera would amplify or dampen the combined effect unpredictably.

In currency derivatives, vera is relevant because interest-rate differentials (which drive carry trades) interact with volatility regimes. When currency volatility is high, the interest-rate sensitivity of currency options changes, and vera captures that shift. Traders in emerging markets, where rate and vol regimes co-move strongly, are especially vulnerable to vera surprises.

## Vera and portfolio stress-testing

Sophisticated [value-at-risk](/value-at-risk/) and stress-testing frameworks now incorporate vera alongside rho and vega. A scenario analysis might contemplate a 100 basis-point rate hike paired with a volatility spike — a combination that has happened historically. The vera term amplifies the joint impact, and ignoring it can underestimate tail risk.

For options with long tenors, vera effects can compound. A ten-year swaption's vera might be small on a daily basis, but over a quarter or year of sustained rate and volatility co-movement, vera-driven P&L shifts can accumulate to material levels.

## Vera in pricing adjustments

Market participants sometimes apply vera adjustments when pricing exotic options or structured products. A long-term equity-linked note might embed an option whose rho is hedged dynamically. If the hedger monitors vera and adjusts the hedge not just when rates or volatility change independently, but also when they move together, the hedge cost can be reduced.

Similarly, in trading desks that price options off standardised curves and volatility surfaces, vera sensitivity helps traders anticipate how hedge ratios will shift if market conditions evolve. Salespeople can quote adjustments that reflect vera exposure when selling large or illiquid options to clients.

## See also

<div class="wiki-seealso">

### Closely related

- Rho — interest-rate sensitivity; vera measures its volatility dependence
- [Vega](/vega/) — volatility sensitivity; vera links it to interest-rate risk
- Greeks — the complete family of option risk measures
- [Implied volatility](/implied-volatility/) — the factor against which vera measures rho's sensitivity
- [Interest rate](/interest-rate/) — the other factor driving vera
- [Black–Scholes model](/black-scholes-model/) — framework for computing vera analytically

### Wider context

- [Option](/option/) — vera applies to all interest-rate-sensitive options
- Derivatives — second-order Greeks are foundational to risk management
- Interest-rate swaption — fixed-income derivatives where vera is material
- [Value-at-risk](/value-at-risk/) — vera contributes to multi-factor stress tests
- Stochastic volatility — models that capture vera effects more precisely

</div>

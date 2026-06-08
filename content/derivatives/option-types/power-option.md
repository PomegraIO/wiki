---
title: "Power Option"
description: "A nonlinear exotic option whose payoff equals a power function of the underlying asset price at expiry."
keywords:
  - power option
  - exotic option
  - nonlinear payoff
  - derivatives
image: "/svg/derivatives.svg"
---

*A **power option** is an [option](/option/) whose payoff at [expiration](/expiration-date/) is determined by raising the final asset price to a fixed power, rather than by linear subtraction from a strike. A power-2 call on a stock, for instance, pays off as (stock price)² minus (strike)² at expiry, magnifying gains in proportion to how far the asset moves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Power Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured contracts." />

<div class="wiki-infobox-caption">An exotic option with a nonlinear, accelerating payoff structure.</div>

|   |   |
|---|---|
| **What it is** | An option whose payoff equals f(S)ⁿ, where S is the asset price and n is the power exponent |
| **Also called** | Power option, squared-payoff option, non-linear option |
| **Common powers** | 2 (squared), 3 (cubed), fractional exponents (e.g., 0.5 for square root) |
| **Payoff behavior** | Accelerates with larger moves; flattens for small moves |
| **Common underlyings** | Equities, [indices](/sp-500-index/), [forex](/us-dollar/), [commodities](/crude-oil/) |
| **Holder motivation** | Massive leverage on large moves; asymmetric payoff for convex bets |
| **Seller motivation** | Higher premium to cover extreme tail risk |

</aside>

## How the nonlinear payoff works

A standard [call option](/call-option/) pays off linearly: if you hold a call with a [strike price](/strike-price/) of 100 and the asset rises to 110, your payoff is 10. If it rises to 120, your payoff is 20. A power-2 call with the same 100 strike computes payoff as (asset price)² − (strike)². At 110, the payoff is 110² − 100² = 12,100 − 10,000 = 2,100. At 120, it is 120² − 100² = 14,400 − 10,000 = 4,400. The advantage is explosive: a 10% move yields a 21× payoff multiplier; a 20% move yields a 44× multiplier.

This amplification is the power option's defining feature. The payoff structure is **convex**: as the underlying moves further in-the-money, each incremental dollar gain is worth more than the last. The holder effectively has leverage built into the derivative's design, without borrowing money.

## Fractional powers and inverse structures

Power options are not limited to integer exponents. A power-0.5 option (square root) produces the opposite effect: the payoff flattens as the underlying moves further in-the-money. This structure appeals to those seeking to dampen [volatility](/historical-volatility/) or reduce their [tail risk](/tail-risk/) on a long equity position—a subdued payoff that still captures moderate upside but caps extreme gains.

Inverse power options (negative exponents) exist in theory and in specialized derivatives desks, though they are rare in practice. A power-(-1) structure, for instance, would make the option more valuable the closer the asset price stays to some midpoint—useful for very specific hedging scenarios.

## Valuation and [gamma](/call-option/) risk

Power options are expensive to price and even more expensive to hedge. The payoff function is highly [nonlinear](/call-option/)—meaning [gamma](/call-option/), the second derivative of option value with respect to spot price, is very large and changes sharply. A dealer who sells a power option and tries to hedge it by rebalancing a delta-neutral position faces huge transaction costs because small moves in the underlying require large rebalancing trades.

[Monte Carlo simulation](/discounted-cash-flow-valuation/) is the standard approach to valuation. Because the payoff depends only on the asset price at expiry (not on the path taken to get there), the problem is simpler than for [path-dependent](/option/) exotics like [cliquets](/cliquet-option/) or [shout options](/shout-option/). Still, the convexity of the payoff function demands careful calibration of [volatility surfaces](/volatility-smile/) and fine-grained simulation grids.

Closed-form solutions exist in special cases: for example, when the underlying follows a [geometric Brownian motion](/option/) (a standard assumption in derivatives markets), and the power is a simple integer, some analytical results are available. But in general, numerical methods are unavoidable.

## Who buys power options and why

Speculators and hedge funds use power options to take highly leveraged bets on directional moves without posting margin or using repo. A trader bullish on a stock but unwilling to short sell the stock itself might instead buy a power-2 call, capturing exponential upside if the stock rallies 20%+ while keeping [premium](/option-premium/) and [leverage ratio](/leverage-ratio-forex/) under control.

Structured product issuers embed power-option-like features into autocallable notes and other [exotic](/option/) retail products to create the illusion of unusually high coupons or payoffs. The asymmetric risk—hidden tail losses—often escapes retail buyers' notice.

In [commodity](/crude-oil/) markets, a trader may use a power option to hedge a physical position where nonlinear exposure matters. For example, a power station's profit margin may be proportional to (electricity price)² minus (fuel cost), because higher-priced electricity brings in revenue growth that accelerates with further price moves.

## The leverage and risk profile

Power options are operationally leveraged. A power-2 call buyer with a 100 strike on a 100 asset (at-the-money) has zero initial payoff but receives 100 of value per 1 percentage-point rally in the stock. By contrast, a standard at-the-money call would receive roughly 0.5 to 0.6 of payoff value per point (depending on [volatility](/historical-volatility/)).

The catch: if the stock falls, the power-2 call's payoff collapses even more dramatically than a vanilla call's. An at-the-money power-2 call with a negative expiry move (stock down 5%) is worth far less than the corresponding vanilla call. The leverage works both ways.

[Value-at-risk](/value-at-risk/) frameworks often dramatically underestimate the loss potential of power options because standard risk models assume linear payoffs. A position that looks reasonable under normal volatility assumptions can blow up in a severe market move. Dealers and sophisticated traders treat power options as tail-risk instruments and reserve accordingly.

## Variations and applications

A **power-spread** combines a long power call at one strike with a short power call at a higher strike, capping both maximum gain and loss. A **powered call spread** narrows the profile compared to a vanilla spread, concentrating payout in a tighter range.

Equity index funds sometimes encounter power-option-like exposures through [volatility](/historical-volatility/) derivatives or variance swaps, which have payoffs proportional to squared returns. These instruments are often sold unknowingly by passive investors and discovered only when realized [volatility](/historical-volatility/) spikes.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative granting a right to buy or sell
- [Call Option](/call-option/) — the right to purchase an asset at a fixed strike price
- [Strike Price](/strike-price/) — the fixed price at which an option may be exercised
- [Gamma](/call-option/) — the sensitivity of option delta to moves in the underlying price
- [Expiration Date](/expiration-date/) — the date when the option's right expires
- [Shout Option](/shout-option/) — exotic option with a discretionary reset feature
- [Cliquet Option](/cliquet-option/) — exotic option with automatic periodic resets
- [Passport Option](/passport-option/) — exotic option on an optimally-managed account

### Wider context

- [Exotic Option](/option/) — family of nonstandard derivatives with complex payoff structures
- [Volatility Smile](/volatility-smile/) — the observed pattern of implied volatility across strikes
- [Tail Risk](/tail-risk/) — the possibility of extreme losses beyond normal expectations
- [Derivatives](/option/) — financial contracts whose value derives from underlying assets
- [Value-at-Risk](/value-at-risk/) — statistical measure of potential losses under adverse scenarios
- [Leverage Ratio](/leverage-ratio-forex/) — measure of financial leverage and risk

</div>

---
title: "Veta"
description: "The rate of change of vega with respect to time, measuring how volatility sensitivity erodes as an option approaches expiry."
keywords:
  - second-order greek
  - time decay
  - volatility sensitivity
  - option greeks
image: "/svg/derivatives.svg"
---

*Veta is a second-order Greek that quantifies how an option's [vega](/vega/) (volatility sensitivity) decays over time. It bridges the gap between time decay ([theta](/theta/)) and volatility risk, revealing how the urgency of managing volatility exposure evolves as expiration approaches.*

## Why vega erosion matters

An option's value depends on both how much time it has left and how volatile the market might be. [Vega](/vega/) measures sensitivity to volatility changes; [theta](/theta/) measures the impact of the passage of time. Veta is the cross-derivative: how fast does vega itself decay?

Consider a long-dated at-the-money call option. Its vega is high because there is a long window for the stock to swing wildly, and volatility expansion significantly boosts the option's value. As the option inches toward expiry, vega shrinks. The market has fewer days for dramatic moves, so each unit of volatility becomes less valuable. Veta quantifies that shrinkage and is invariably negative for standard vanilla options: vega must decline as you get closer to expiry.

This matters because a trader holding a volatility position cannot assume that vega will remain constant. A position constructed to be vega-neutral today will become vega-positive or vega-negative as time passes, even if implied volatility does not move, because the vega of each option leg decays at different rates.

## The mechanic: veta and time

Formally, veta is the partial derivative of vega with respect to time, sometimes written as ∂vega/∂t. It is negative because, all else equal, fewer days means lower volatility sensitivity. The magnitude of veta tends to be larger for at-the-money options and shorter-dated options. A near-expiry at-the-money option losing a few days can see its vega collapse, while a far-out-of-the-money option might shed vega more gradually.

The Black–Scholes framework yields veta as a closed-form expression, though most traders rely on numerical calculations because veta also depends on the slope of the [volatility smile](/volatility-smile/), which violates Black–Scholes assumptions. In practice, veta is computed by shocking time forward (say, one day) and recalculating vega, then taking the difference.

## Veta in portfolio management

A long volatility position — say, a long straddle or strangle — carries a veta cost. Each passing day erodes the vega benefit, even if realized volatility remains low. This is similar to [theta](/theta/) decay, but it is specifically the decay of vol sensitivity, not the entire option value. A trader in a long-vol position needs to decide: do I expect volatility to rise fast enough to compensate for veta bleed?

Conversely, a short volatility position benefits from negative veta. A short straddle or short strangle seller collects premium and also benefits passively as veta decay shrinks the long holder's vega exposure. Over a series of calendar rolls, veta decay becomes a significant source of profit or loss.

## Rolling and rebalancing around veta

Traders managing dynamic volatility books routinely rebalance to stay vega-neutral, but the rate at which vega fades — driven by veta — forces rebalancing schedules. If you hedge a long-vol position by selling shorter-dated options, you must be aware that those short options are bleeding vega faster (higher negative veta). The short-dated hedge will require frequent adjustment as time erodes the short vega faster than the long vega in your original position.

Calendar spreads (also called time spreads or horizontal spreads) are trades that explicitly exploit veta differences. A trader might sell a near-term option (high negative veta) and buy a far-dated option (lower negative veta), profiting as the short vega decays faster than the long vega, even if implied volatility is flat.

## Veta across strikes and tenors

Veta is not uniform across the option surface. At-the-money options exhibit the largest magnitude veta (fastest vega decay), while deep out-of-the-money and in-the-money options decay more slowly. Similarly, very short-dated options can have high veta in absolute terms, but for a single day, a far-out option might lose more vega percentage-wise.

When volatility smiles are pronounced — as they often are in equity and FX markets — veta is not purely dependent on Black–Scholes time decay. The shape of the smile itself shifts as time shrinks, inducing additional veta effects that purely mechanical models miss. Traders use stochastic volatility models or empirical calibration to capture these second-order effects.

## Veta and risk systems

Modern [value-at-risk](/value-at-risk/) and stress-testing systems now incorporate veta alongside vega and theta. A portfolio might be vega-hedged and theta-neutral but still vulnerable to veta shocks if expiry structures are mismatched. A sudden repricing of term structure — perhaps a jump in near-term volatility relative to far-term volatility — can expose hidden veta imbalances across the book.

Over the life of a multi-leg options position, veta ensures that what was hedged yesterday may not be hedged today, particularly if the hedge legs have different expirations or moneyness. Active management of expiration schedules and strategic rolling of positions are essential to keeping veta under control.

## See also

<div class="wiki-seealso">

### Closely related

- [Vega](/vega/) — first-order volatility sensitivity; veta measures its decay
- [Theta](/theta/) — time decay of option value; veta is the time decay of vega specifically
- [Volga](/volga/) — second-order sensitivity of vega to volatility; complements veta
- Greeks — the complete family of option risk sensitivities
- [Implied volatility](/implied-volatility/) — vega measures sensitivity to this; veta measures that sensitivity's time decay
- [Black–Scholes model](/black-scholes-model/) — framework for computing veta analytically

### Wider context

- [Option](/option/) — veta applies to all option contracts
- Derivatives — second-order Greeks are foundational to derivatives risk management
- [Calendar spread](/option/) — exploits veta differences between near and far options
- Stochastic volatility — models that capture veta more accurately than Black–Scholes

</div>

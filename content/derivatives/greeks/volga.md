---
title: "Volga"
description: "The second-order partial derivative of option price with respect to implied volatility squared, measuring convexity in volatility space."
keywords:
  - second-order greek
  - volatility sensitivity
  - option greeks
  - derivatives risk
image: "/svg/derivatives.svg"
---

*Volga is a second-order Greek that measures how an option's vega (volatility sensitivity) changes as implied volatility moves. It quantifies the convexity of option price with respect to volatility and is essential for traders managing large or dynamic volatility exposure.*

## Why option pricing bends with volatility

When implied volatility rises, an option becomes more valuable — the buyer of a call or put gains more from the wider range of possible future prices. But the relationship is not linear. At low volatility levels, a unit increase in volatility has a larger impact on option value than it does at high volatility levels. Volga captures this curvature.

Formally, volga is the second partial derivative of option price with respect to implied volatility: the rate of change of vega as volatility changes. Where vega tells you how much your option gains or loses if volatility moves by 1%, volga tells you how much *that sensitivity itself* will change if volatility moves again. Traders with large vega exposure use volga to hedge and anticipate gamma-like risks in volatility space.

## The practical role in hedging

A long straddle (simultaneous purchase of a call and put at the same strike) has positive gamma — it profits when the stock moves sharply in either direction. That same straddle also has positive volga: it benefits when volatility rises, because both the long call and long put increase in value as uncertainty increases.

Conversely, a short straddle has negative volga. The seller collects premium today but faces compounding losses if volatility spikes: the option values climb faster and faster the higher volatility goes. A trader managing a short volatility position might hedge volga by buying a strangle or adjusting the mix of strike prices, since different strikes have different volga profiles.

Volga is especially relevant during volatility clusters — periods when volatility itself is volatile. If the market is oscillating between low and high volatility regimes, a position's vega exposure is unstable, and ignoring volga can leave a trader blindsided by the second-order effects.

## Volga in the Black–Scholes framework

Under the [Black–Scholes model](/black-scholes-model/), volga can be computed analytically and is proportional to the option's time value and the distance of the strike from the spot price. Volga peaks near the money for short-dated options and extends across a wider range of strikes for longer-dated options. As expiration approaches, volga typically declines, though the relationship depends on moneyness and volatility levels.

The exact formula involves the vega and the d2 term from the Black–Scholes solution — essentially, volga is the gamma of vega — but most traders use numerical routines or market data to track it in real time rather than memorizing the closed form.

## Real-world variations in volga

Not all options have the same volga profile. Out-of-the-money options can have materially different volga than at-the-money options. American options, which can be exercised early, may exhibit path-dependent volga that stochastic volatility models handle more carefully than the Black–Scholes baseline.

Sector and index options often show positive volga when the underlying volatility is low and mean-reverting: traders expect volatility to rise, so they are willing to pay a premium for the convexity. Single-stock options may exhibit negative volga if the company is in a structural deleveraging phase and volatility is expected to fall.

## Volga and portfolio stress

A large trading book with short vega exposure needs to monitor volga just as closely as vega itself. During the 2020 volatility spike in equities, portfolios that were short volatility at low levels faced explosive losses not just because vega changed, but because volga amplified every successive volatility move. A trader who had hedged only first-order vega risk was left exposed to second-order convexity losses.

Risk managers now routinely stress-test volga alongside vega, delta, and gamma. A one-standard-deviation move in volatility can trigger a much larger change in vega if volga is large and negative, forcing unplanned rebalancing.

## See also

<div class="wiki-seealso">

### Closely related

- [Vega](/vega/) — first-order volatility sensitivity; the foundation on which volga is built
- [Veta](/veta/) — measures vega's decay as time passes, the complement to volga
- [Gamma](/gamma/) — second derivative with respect to price; volga is the vol-space equivalent
- Greeks — the full family of option risk sensitivities
- [Implied volatility](/implied-volatility/) — the input that volga measures sensitivity to
- [Black–Scholes model](/black-scholes-model/) — framework for computing volga analytically
- [Straddle](/option/) — long straddles exemplify positive volga; short straddles exhibit negative volga

### Wider context

- [Option](/option/) — volga is a property of all option contracts
- Derivatives — second-order Greeks are core to derivatives risk management
- [Volatility smile](/volatility-smile/) — real-world volatility surfaces exhibit volga patterns across strikes
- [Value-at-risk](/value-at-risk/) — volga contributes to tail risk in short-vol portfolios

</div>

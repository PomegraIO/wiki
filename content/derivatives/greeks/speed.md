---
title: "Speed"
description: "Third-order derivative measuring the sensitivity of gamma to changes in underlying asset price."
keywords:
  - speed
  - third derivative
  - gamma sensitivity
  - option greeks
  - option pricing
---

*The **Speed** of an option (also called "color" or "gamma of gamma") is a third-order [derivative](/wiki/derivatives-exchange-crypto/) in the [options greeks](/wiki/options-greeks/) hierarchy, measuring how the [gamma](/wiki/gamma-option-greeks/) itself changes as the underlying asset price moves. While [delta](/wiki/delta-option-greeks/) measures the option's price sensitivity and [gamma](/wiki/gamma-option-greeks/) measures how delta changes, speed quantifies the curvature of that curvature, making it a critical input for options traders managing convexity risk over multi-day holding periods and for [algorithmic trading](/wiki/algorithmic-trading/) systems adjusting [hedge](/wiki/hedging-with-futures/) ratios dynamically.*

<div class="wiki-hatnote">
For other Greeks, see <a href="/wiki/options-greeks/">Options Greeks</a>. For the related Greek "color," see also <a href="/wiki/charm/">Charm</a>.
</div>

<aside class="wiki-infobox">

| Attribute | Detail |
|-----------|--------|
| Alternative Names | Color, Gamma of Gamma, DΓ/dS |
| Order | Third derivative of option price |
| Formula Symbol | Λ (lambda), sometimes Σ (sigma) |
| Units | Per dollar squared of underlying |
| Sign | Positive for long options, negative for short |
| Peak Sensitivity | Near-the-money, near expiration |
| Use Case | Dynamic hedging, portfolio rebalancing |

</aside>

## Why speed matters in multi-day options strategies

When an options trader holds a [long call](/wiki/call-option/) or [put](/wiki/put-option/), the [gamma](/wiki/gamma-option-greeks/) grows as the stock rallies (for a long call) or falls (for a long put), toward the strike. This accelerating hedge-ratio change is not gradual — it compounds. Speed captures this compound effect. If a trader rebalances a [delta-hedged](/wiki/delta-option-greeks/) position once per day, ignoring speed leads to underestimation of the cost of daily rebalancing, because each day's rebalancing itself changes the size of tomorrow's rebalancing. Speed quantifies this feedback loop mathematically.

## Mathematical definition and computation

Speed is the third derivative of the option price with respect to the underlying stock price:

Speed = ∂Γ/∂S = ∂³C/∂S³

Under the [Black-Scholes model](/wiki/black-scholes-model/), speed depends on the same variables as delta and gamma — stock price, strike, volatility, time to expiration, interest rate — but it has a different sign pattern and sensitivity landscape. For a long call:

- Speed is **negative** out-of-the-money (where gamma is declining as you move further away).
- Speed is **positive** in-the-money (where gamma is rising as you move further away).
- Speed peaks in magnitude near the strike and very close to expiration.

This contrasts with gamma, which is always positive for a long call and always negative for a short call.

## How speed affects hedging costs and P&L

A trader managing a [covered call](/wiki/covered-call/) or other [option position](/wiki/option/) must rebalance the underlying [hedge](/wiki/hedging-with-futures/) as delta changes. The cost of rebalancing includes both:

1. The difference in delta between today and tomorrow (first order, captured by gamma).
2. The change in that change (second order, where speed enters).

In a market with large daily moves (high realized [volatility](/wiki/volatility-smile/)), speed effects compound rebalancing costs quickly. A portfolio of short [out-of-the-money](/wiki/out-of-the-money/) calls, which have negative speed, becomes cheaper to hedge as the market moves further away from the strikes — a convex payoff. Conversely, a short [straddle](/wiki/straddle-option/) (long gamma risk on both sides) experiences positive speed effects that increase hedging costs when the market swings hard in either direction.

## Portfolio applications and dimension reduction

Options desks typically monitor speed alongside the familiar greeks (delta, gamma, [vega](/wiki/vega-option-greeks/), [theta](/wiki/theta-option-greeks/), and [rho](/wiki/rho-option-greeks/)) in the "Greeks matrix" for a portfolio. However, speed often takes a back seat to the first two greeks because:

- Its magnitude is usually small relative to delta and gamma.
- It only dominates portfolio risk in scenarios of extreme daily price swings or when holding period is very short.
- Most hedge-rebalancing algorithms can absorb speed effects through daily recalibration without explicit modeling.

Algorithmic options traders and [high-frequency trading](/wiki/high-frequency-trading/) (HFT) firms building [execution algorithms](/wiki/algorithmic-execution-benchmark/) do monitor speed explicitly, because even small changes in gamma compounding accumulate into significant P&L surprises over thousands of microsecond-scale rebalances.

## Speed, time decay, and the "color" relationship

Speed is sometimes called "color" because it captures the interaction between [gamma](/wiki/gamma-option-greeks/) (spacial curvature) and [theta](/wiki/theta-option-greeks/) (time decay). An option losing time value (theta decay) while simultaneously experiencing gamma changes creates a "colored" or textured P&L surface that a static Black-Scholes model underestimates. Near expiration, when theta spikes, speed also becomes pronounced. This is why [binary options](/wiki/binary-option/) and other highly levered, short-dated derivatives can exhibit violent speed effects.

## Practical bounds and risk limits

Risk management frameworks rarely set explicit speed limits (unlike delta, gamma, and vega notional limits), but traders use speed to:

- **Assess rebalancing frequency.** High speed indicates frequent rebalancing is necessary.
- **Flag correlation basis risks.** If a hedge instrument's speed differs from the position it hedges, basis risk emerges.
- **Detect gamma scalping opportunities.** A trader capturing gamma profit must account for how gamma itself is changing; speed quantifies that edge.

<div class="wiki-seealso">

### Closely related
- [Options Greeks](/wiki/options-greeks/) — The comprehensive framework of option sensitivities
- [Gamma](/wiki/gamma-option-greeks/) — The second derivative; rate of change of delta
- [Delta](/wiki/delta-option-greeks/) — The first-order price sensitivity
- [Charm](/wiki/charm/) — Another third-order Greek (delta decay)
- [Theta](/wiki/theta-option-greeks/) — Time decay of option value

### Wider context
- [Black-Scholes model](/wiki/black-scholes-model/) — Theoretical option pricing foundation
- [Volatility smile](/wiki/volatility-smile/) — How implied volatility varies across strikes
- [Dynamic hedging algorithm](/wiki/dynamic-hedging-algorithm/) — Rebalancing mechanics
- [Option-adjusted spread](/wiki/option-adjusted-spread/) — Market pricing of embedded options

</div>

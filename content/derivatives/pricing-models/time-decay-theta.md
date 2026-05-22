---
title: "Time Decay (Theta)"
description: "The rate at which option value erodes as expiration approaches, holding all other factors constant; one of the key option Greeks."
keywords:
  - theta decay
  - option Greeks
  - time value
  - option premium
  - option pricing
---

*Theta (θ) is the rate at which an option's value decays as expiration approaches, measured as the daily (or hourly) loss in value from the mere passage of time. It is one of the fundamental [option Greeks](/wiki/options-greeks/) and represents the cost of holding an option position overnight.*

<div class="wiki-hatnote">For the broader Greek framework, see [Options Greeks](/wiki/options-greeks/). For the option price formula, see [Black-Scholes Model](/wiki/black-scholes-model/).</div>

<aside class="wiki-infobox">

| Property | Characteristic |
|----------|-----------------|
| Definition | Daily value loss from time decay alone |
| Direction | Negative for long options; positive for short |
| Unit | $ per day (for equity options, often per 1% per day) |
| Magnitude | Smallest far from expiry; steepest near expiry |
| Dependence | Increases as volatility decreases |
| Optionality | Long options bleed theta; short options collect |
| Relationship | Related to [gamma](/wiki/gamma-option-greeks/) trade-off |

</aside>

## How time decay works

An option's value has two components: **intrinsic value** (how much it's in the money) and **time value** (the premium for the possibility of profitable moves).

A call option on a stock trading at $100 with a $95 strike has $5 of intrinsic value. If the option trades at $7, the extra $2 is time value—the market's assessment that the stock might move above $102 before expiration.

As days pass and the stock stays at $100, that time value erodes. With one week to expiration, the option might be worth $5.30 (only $0.30 time value). With one day left, it's worth $5.01 (negligible time value). At expiration, it's worth exactly $5—intrinsic value only.

This erosion is **theta decay**. All else equal, time decay causes the option to lose value simply because you're closer to expiration.

## Theta in the Black-Scholes model

The Black-Scholes pricing formula includes a theta term:

$$\theta = -\frac{S \cdot \phi(d_1) \cdot \sigma}{2\sqrt{T}} - r K e^{-rT} \Phi(d_2)$$

Where:
- S = current stock price
- σ = volatility
- T = time to expiration (in years)
- r = risk-free rate
- Φ, φ = normal distribution functions

The first term dominates for near-the-money options; the second term is smaller. The key insight: theta is *proportional to 1/√T*. As expiration approaches, theta accelerates—the rate of decay increases nonlinearly in the final days.

## The acceleration near expiration

This is the most important practical insight: theta is not constant. It accelerates sharply in the final week (or day) before expiration.

Consider a call option 60 days to expiration:
- Days 60–30: Theta might be −$0.01 per day (losing 1 cent per day).
- Days 30–15: Theta might be −$0.03 per day.
- Days 14–7: Theta might be −$0.08 per day.
- Days 6–1: Theta might be −$0.20 per day.

A trader holding a long option loses money fastest in the final days, even if the stock doesn't move. This is why options traders often close positions before the final week: theta accelerates, and the cost of carry (in dollars per day) becomes prohibitive.

## Long vs. short theta

**Long options** (call or put holder) **lose theta** every day: the passage of time erodes the time value you paid for, assuming price stays constant.

**Short options** (call or put writer) **gain theta** every day: you collected premium upfront, and time decay gives you the profit without needing the stock to move in your favor.

This is why [covered call](/wiki/covered-call/) writers are willing to give up upside: they're collecting theta. If the stock doesn't move much, the time value decay is their profit.

## Theta and volatility

Theta is **inversely related to volatility**. A call option in a low-volatility stock (VIX 10) decays faster than a call on a high-volatility stock (VIX 30), holding all other factors equal.

Why? High volatility inflates time value (larger probability of big moves), so there's more time value to decay. Low volatility means the market doesn't expect big moves, so time value is thin and decays faster.

This creates a nuance: **short volatility, collect theta**. If you sell a call in a low-volatility stock, you're banking on continued low volatility and accelerating theta decay. If volatility suddenly spikes (e.g., bad earnings), the call's value can jump even as theta decays, leaving you with a loss.

## Theta in context: the gamma-theta trade-off

Theta decay is the "hidden cost" of insurance. An investor holding stock might buy a protective put to limit downside. The put decays via theta every day the stock is flat—the insurance premiums are leaking away.

But the put also has **positive [gamma](/wiki/gamma-option-greeks/)**: if the stock suddenly crashes, the put's value accelerates upward faster than the stock's loss. So the put-buyer is paying theta (time decay) for gamma (convexity) protection.

Conversely, a seller of options is *harvesting* theta but is exposed to negative gamma: if the stock makes a large move, losses accelerate faster than they imagined.

## Practical theta strategies

### Theta farming (covered calls and cash-secured puts)
Write options to collect theta. Hold stock and sell calls on top ([covered calls](/wiki/covered-call/)) or sell puts on stock you want to own ([cash-secured puts](/wiki/cash-secured-put/)). If the stock drifts sideways, theta is your profit. The cost: you cap upside on the call, or accept assignment on the put.

### Short-dated trading
Some traders specialize in very short-dated options (1–3 days to expiration) where theta is steepest. This is high-frequency, low-margin trading: the goal is small daily profits on high leverage.

### Theta bleed avoidance
Long-option buyers avoid holding positions through final week expiration if possible. After earnings or a major news event, buying a one-week call is expensive (high volatility, steep theta). Better to roll out in time (sell the 1-week, buy the 1-month) to lower theta cost.

## Theta in derivatives beyond equities

**Bond options**: Theta decay is more predictable (interest rates are more predictable than stocks), so theta is smaller and more stable.

**Commodity options**: Theta decays faster in months with harvest/supply shocks (convenience yield spikes), slower in normal months.

**FX options**: Theta depends on [carry trade](/wiki/carry-trade/) dynamics; in high-interest-rate pairs, theta can be positive (time helps you) due to interest rate effects.

## The theta cost of leverage and portfolio hedging

A portfolio manager hedging against a crash by buying put options on the S&P 500 is paying theta. If the market stays calm and doesn't crash, the puts lose money purely to decay. This is the cost of insurance. Many investors use [collars](/wiki/collar-strategy/) (buy puts, sell calls) to reduce the theta cost.

<div class="wiki-seealso">

### Closely related
- [Options Greeks](/wiki/options-greeks/) — framework overview
- [Delta](/wiki/delta-option-greeks/) — directional sensitivity
- [Gamma](/wiki/gamma-option-greeks/) — acceleration/convexity
- [Vega](/wiki/vega-option-greeks/) — volatility sensitivity
- [Rho](/wiki/rho-option-greeks/) — interest rate sensitivity

### Wider context
- [Black-Scholes Model](/wiki/black-scholes-model/) — pricing foundation
- [Option Premium](/wiki/option-premium/) — value components
- [Covered Call](/wiki/covered-call/) — theta harvest strategy
- [Protective Put](/wiki/protective-put/) — theta cost of insurance

</div>

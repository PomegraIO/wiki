---
title: "Second-Order Greeks Explained"
description: "Second-order Greeks (vanna, volga, charm, veta) measure how delta, gamma, theta, and vega change. Essential for hedging and portfolio risk management."
keywords:
  - second order options greeks
  - vanna greek
  - volga greek
  - charm greek
  - veta greek
  - derivatives hedging
image: /svg/derivatives.svg
---

*The **second-order Greeks** extend option risk measurement beyond delta, gamma, theta, and vega to describe how those first-order Greeks themselves move. Vanna, volga, charm, and veta are vital for traders managing complex hedges and large portfolios because they capture the real cost of rebalancing.*

## What Second-Order Greeks Measure

The first-order Greeks—[delta](/delta/), [gamma](/gamma/), [theta](/theta/), and [vega](/vega/)—tell you how an option price responds to moves in the stock, time, and volatility. A second-order Greek measures how *one of those* first-order Greeks changes when a market variable shifts.

Think of it as a derivative of a derivative. If delta is how much the option price moves when the stock moves $1, then vanna is how much delta itself shifts when volatility changes. This matters because traders rarely hedge once and walk away; they rebalance, and rebalancing costs money when the Greeks shift in the wrong direction.

## The Four Main Second-Order Greeks

**Vanna** measures how delta changes when implied volatility changes (or equivalently, how vega changes when the stock moves). For a call option, vanna is typically positive: when volatility rises, delta increases. This means a long call that was somewhat protected during a stock spike becomes *more* aggressive at higher volatility—requiring the trader to sell more stock to stay hedged. Vanna is largest for near-the-money options and shrinks as you move deep in-the-money or out-of-the-money.

**Volga** (sometimes called "vomma") measures how vega itself changes when volatility shifts. A trader long vega benefits when volatility rises, but volga tells you whether that benefit gets amplified or dampened by further volatility moves. Volga is typically positive: higher volatility increases vega, so a vega-long position becomes more sensitive to volatility the more volatile the market gets. This creates a feedback loop that can make tail risks steeper.

**Charm** (or "delta decay") measures how delta drifts as time passes—independent of stock or volatility moves. For a call option, charm is typically negative: the delta slowly decreases as expiration approaches, even if the stock and volatility stay flat. This is why an out-of-the-money call that initially has 0.30 delta might decay to 0.25 delta over a week, forcing a delta-hedger to buy back some stock protection at an unfavorable price. Charm is largest for at-the-money options.

**Veta** measures how vega changes as time passes. For most options, veta is negative: as expiration approaches, the vega of the option falls. A trader who owns a short-dated option that started with high vega will see that vega evaporate daily, even if the stock and volatility don't move. This is the "vega decay" risk that time-decay traders exploit.

## Why Hedgers Care

A portfolio hedged purely on delta looks safe until the market moves in an unexpected way. Then the Greeks themselves move, and the hedge no longer works:

- **Vanna risk**: You hedge a call's delta by shorting stock. Volatility spikes. Vanna is positive, so delta jumps higher. Now you are under-hedged and lose money on the next up move.
- **Volga risk**: You are long volatility (long vega). Another volatility spike amplifies your vega through positive volga. You thought you had $1 million of vega exposure, but after the move you have $1.3 million. The position is more sensitive than you planned.
- **Charm risk**: You own a put spread expiring in three weeks, delta-hedged at cost. Every day that passes, charm eats away your delta in the short leg faster than in the long leg. The spread becomes less hedged without you doing anything. Time decay skews your profile.
- **Veta risk**: You sold volatility (short vega). Each day, veta reduces your vega exposure favorably—the vega you're short gets smaller. But veta is the other side: if you're long vega in a near-expiration option, the exposure collapses faster than you'd like.

## Relationship to First-Order Greeks

Second-order Greeks are cross-partials: they measure how one first-order Greek responds to a market variable that also drives another Greek.

Specifically:
- **Vanna** = ∂delta/∂volatility = ∂vega/∂stock = rate at which delta and vega move together
- **Volga** = ∂vega/∂volatility = how vega compounds with volatility moves
- **Charm** = ∂delta/∂time = how delta decays with calendar time
- **Veta** = ∂vega/∂time = how vega shrinks as expiration nears

This interweaving is why option Greeks form a linked system: moving one dimension (stock price, volatility, time) ripples through multiple Greeks, and understanding the second-order effects is what separates competent hedgers from those who get blindsided.

## Practical Sizing: When Second-Order Matters

For small positions or short holding periods, second-order Greeks are noise. But:

- **Large portfolios** with hundreds of options: charm and veta can dominate daily P&L, especially near expiration.
- **Long volatility trades** held into realized vol jumps: volga can double your exposure if vol spikes repeatedly.
- **Dynamic delta hedging** at market turns: vanna tells you whether your hedge will improve or deteriorate as you rebalance.
- **Calendar spreads** and *theta plays*: charm is the "real" theta, accounting for how the Greeks themselves change.

## Estimating and Monitoring Second-Order Greeks

Most option pricing libraries (including standard [Black-Scholes](/black-scholes-model/) implementations) produce second-order Greeks through numerical differentiation: calculate the first-order Greek at volatility+ε and volatility−ε, then take the difference. Vanna is similarly computed by shifting the stock price and recalculating vega.

Professional risk systems track these Greeks alongside delta, gamma, and vega. A trader might set a limit: "Total portfolio vanna < $500K per 1% vol move," signaling that rebalancing costs won't blow up if volatility spikes. Similarly, volga limits prevent compounding exposure to vol-of-vol risk.

For individual traders, understanding vanna and charm qualitatively—knowing that near-the-money options have high vanna and that time decay skews your delta as expiration nears—often suffices to avoid major mistakes.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — first-order Greek measuring how much an option price moves when the stock moves
- [Gamma](/gamma/) — rate of delta change; second-order stock sensitivity and key to rebalancing costs
- [Theta](/theta/) — time decay; negative for long options, the key driver of charm
- [Vega](/vega/) — sensitivity to volatility moves; volga measures how vega compounds
- [Implied Volatility](/implied-volatility/) — the volatility input that drives vega, vanna, and volga
- [How Implied Volatility Affects the Greeks](/implied-volatility-effect-on-greeks/) — directional rules for how vol moves shift all Greeks

### Wider context

- [Option](/option/) — the underlying instrument whose Greeks we measure
- [Derivatives Hedging](/derivatives-hedging/) — the practical application of Greeks in risk management
- [Black-Scholes Model](/black-scholes-model/) — foundational pricing model that produces Greeks
- [Greeks for Deep In-the-Money Options](/greeks-for-deep-in-the-money-options/) — how Greek profiles change at extreme moneyness

</div>
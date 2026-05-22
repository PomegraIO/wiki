---
title: "Ultima"
description: "The fourth derivative measuring how an option's vega changes in response to changes in volatility, a higher-order Greek beyond delta, gamma, vega, and theta."
keywords:
  - ultima
  - option greeks
  - vega sensitivity
  - volatility derivatives
---

*The **Ultima** is a fourth-order [Greek](/wiki/options-greeks/) measuring the sensitivity of [vega](/wiki/vega-option-greeks/) to changes in [implied volatility](/wiki/implied-volatility/). Where [vega](/wiki/vega-option-greeks/) measures how much an option's value changes when volatility moves 1 percentage point, **Ultima** measures how vega itself moves when volatility changes. It captures convexity in the volatility dimension—a critical metric for volatility traders and exotic option hedgers.*

<aside class="wiki-infobox">

| Key Fact | Value |
|---|---|
| **Mathematical Definition** | d(vega) / d(volatility) |
| **Related Greeks** | Vega, volga (vega convexity), vanna |
| **Typical Range** | -0.1 to +0.3 (varies by strike, expiration) |
| **Sign Convention** | Negative for most equity options at-the-money |
| **Use Case** | Volatility-of-volatility hedging, exotic options |
| **Calculation** | Third derivative of option price w.r.t. volatility |
| **Practical Importance** | Rising in modern trading (vol derivatives, variance swaps) |

</aside>

## Understanding the Greek hierarchy

To grasp Ultima, recall the standard Greek hierarchy:

- **Delta:** Change in option price for $1 move in stock price. (∂P / ∂S)
- **Gamma:** Change in delta for $1 move in stock price. (∂delta / ∂S)
- **Vega:** Change in option price for 1 percentage point change in [implied volatility](/wiki/implied-volatility/). (∂P / ∂σ)
- **Theta:** Change in option price for 1 day passage of time. (∂P / ∂t)
- **Rho:** Change in option price for 1 percentage point change in [interest rates](/wiki/interest-rate-swap/). (∂P / ∂r)

Ultima is the **second derivative of vega**, or the **third derivative of the option price with respect to volatility**:

**Ultima = ∂(vega) / ∂σ = ∂²P / ∂σ²**

## An intuitive example

Imagine a trader long a [straddle](/wiki/straddle-option/) (long call + long put), a classic volatility play. The straddle profits from large moves in either direction and is long [vega](/wiki/vega-option-greeks/)—higher volatility increases its value.

But here's the subtlety: **how much does the straddle's vega increase when volatility spikes?**

- If volatility is 15% and rises to 16%, the straddle's vega increases by (say) $50.
- If volatility is 40% and rises to 41%, the straddle's vega might increase by only $35 instead.

This non-linear relationship is captured by **Ultima**. The straddle has negative Ultima—its vega sensitivity decreases at higher volatility levels.

## Why Ultima is negative (usually)

For standard equity [options](/wiki/option/), Ultima is typically **negative** at-the-money:

- At low volatility (15%), the option is cheap; vega is large (a 1% vol move matters).
- At high volatility (50%), the option is expensive; vega is smaller (a 1% vol move matters less in percentage terms).

This is analogous to [convexity](/wiki/convexity/) in bonds: bond prices rise with falling rates, but at a decreasing rate (negative convexity). Option vega declines with rising volatility.

**Mathematical intuition:** The option price is a concave function of volatility (for ITM/OTM options); concave functions have negative second derivatives. So ∂²P / ∂σ² is negative.

## Calculating Ultima (simplified)

For a Black-Scholes call:

**Ultima ≈ −(vega / σ) × (1 + d₁ × √T)**

where d₁ is the cumulative normal parameter and T is time to expiration.

- Higher volatility (σ) makes Ultima less negative (closer to zero).
- Shorter expiration (low T) increases the magnitude of negative Ultima.
- Deep OTM and ITM options (where d₁ is extreme) have different signs of Ultima.

For practical traders, the key insight is: **Ultima is typically a small negative number, making vega sensitivity decrease at higher vol levels.**

## Ultima in practice: volatility trading

For traders managing [volatility positions](/wiki/volatility-swap/), Ultima becomes critical:

### Volatility-of-volatility trading
A trader might be long [realized volatility](/wiki/historical-volatility/) (actual market swings) but short [implied volatility](/wiki/implied-volatility/) (options are overpriced). Their profit/loss depends on:

1. How much realized vol differs from implied vol (realized-implied vol spread).
2. How implied volatility itself changes (vega P&L).
3. How the vega changes as volatility moves (Ultima P&L).

Ignoring Ultima in this trade leads to mispricing: a large spike in volatility kills your vega profits because vega itself shrinks.

### Variance swaps and log contracts
[Variance swaps](/wiki/variance-swap/) (which pay off on realized variance, not price moves) are delta-neutral but vega-long. Their Ultima profile matters for exotic payoff replication.

### Barrier options and knockout structures
[Barrier options](/wiki/barrier-option/) (which disappear if the stock hits a level) have non-standard Ultima because their effective vega changes discontinuously near the barrier. Hedging these requires Ultima management.

## Ultima vs. related Greeks

Related concepts are often confused:

| Greek | Meaning | Formula |
|---|---|---|
| **Vega** | Sensitivity to volatility level | ∂P / ∂σ |
| **Volga** | Convexity in volatility | ∂²P / ∂σ² |
| **Ultima** | Sensitivity of vega to volatility | ∂(vega) / ∂σ |
| **Vanna** | Sensitivity of delta to volatility | ∂(delta) / ∂σ |

**Volga** and **Ultima** are often used interchangeably in practice (they are mathematically identical). **Vanna** is distinct—it measures how delta changes with volatility, important for hedging portfolios that are both long gamma and long vega.

## Practical limitations and computational challenges

1. **Calculation complexity:** Ultima requires numerical differentiation or closed-form solutions (available for Black-Scholes, harder for other models).

2. **Model dependence:** Ultima is highly sensitive to the volatility model used. If you assume [implied volatility](/wiki/implied-volatility/) is flat across strikes, Ultima differs from a model with volatility [smile](/wiki/volatility-smile/) or [skew](/wiki/volatility-smirk/).

3. **Data quality:** Computing Ultima from market data requires high-quality option prices across strikes and expirations—expensive and error-prone.

4. **Hedging cost:** Trading small Ultima exposure (buying/selling a few options to offset Ultima) can be costly because it requires precise strike selection.

For these reasons, most traders focus on delta, gamma, vega, and theta. Ultima hedging is mostly done by:
- Exotic derivatives traders (pricing complex products).
- Volatility arbitrage funds.
- [Systematic volatility traders](/wiki/volatility-factor-performance/) using algorithms.

## Volatility smile and Ultima

When [implied volatility](/wiki/implied-volatility/) varies across strikes (smile or skew), Ultima becomes even more complex. A smile means:

- Call options with different strikes have different implied vols.
- The option's vega depends on the slope of the smile.
- Ultima depends on the curvature of the smile.

This makes Ultima a useful metric for smile traders: it quantifies how sensitive their hedge ratios are to smile shape changes.

## The future of Ultima in practice

As [volatility derivatives](/wiki/variance-derivatives/) and [variance swaps](/wiki/variance-swap/) proliferate, Ultima is becoming more relevant. Quant traders managing large volatility books routinely hedge Greeks including Ultima, treating it as a standard risk metric alongside delta and vega.

However, for most retail and institutional investors, Ultima remains abstract. They focus on directional (delta) and volatility (vega) exposure. But for anyone serious about options trading—especially volatility arbitrage—Ultima is essential.

<div class="wiki-seealso">

### Closely related
- [Vega (Option Greeks)](/wiki/vega-option-greeks/) — Volatility sensitivity (first-order)
- [Volga](/wiki/atomic-swap/) — Volatility convexity (equivalent to Ultima)
- [Gamma (Option Greeks)](/wiki/gamma-option-greeks/) — Price convexity (second derivative w.r.t. price)
- [Options Greeks](/wiki/options-greeks/) — The full hierarchy of option risk metrics

### Wider context
- [Volatility Smile](/wiki/volatility-smile/) — How implied vol varies across strikes
- [Variance Swap](/wiki/variance-swap/) — An instrument sensitive to Ultima dynamics
- [Volatility Arbitrage](/wiki/statistical-arbitrage/) — Trading that exploits Ultima mispricings

</div>

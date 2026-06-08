---
title: "SABR Model"
description: "A pricing framework for interest-rate options where both forward rates and volatility follow stochastic processes, capturing the volatility smile in fixed-income markets."
keywords:
  - SABR model
  - interest rate options
  - stochastic volatility
  - caplets
  - swaptions
image: "/svg/derivatives.svg"
---

*Interest-rate [options](/option/) behave differently from equity options. At-the-money swaptions and caplets trade at lower [implied volatilities](/implied-volatility/) than out-of-the-money equivalents—an inverted smile peculiar to fixed-income markets. The **SABR model** (Stochastic Alpha Beta Rho), introduced in 2002, prices these instruments by allowing both forward rates and volatility to drift stochastically, with parameters tailored to the leverage and mean-reversion properties of bond markets. It has become the market standard for [interest-rate option](/option/) pricing and [Greeks](/delta/), especially among dealers and hedge funds.*

<div class="wiki-hatnote">

*For a broader stochastic volatility framework used across asset classes, see [Heston Stochastic Volatility Model](/heston-stochastic-volatility-model/).*

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">SABR Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and complex instruments." />

<div class="wiki-infobox-caption">Forward rate and volatility evolve jointly; calibrates to the volatility smile in swaptions and caps without constant-volatility assumptions.</div>

|   |   |
|---|---|
| **What it is** | Two-factor stochastic volatility model for [interest-rate options](/option/); assumes CEV dynamics on the forward and a lognormal process on volatility |
| **Core parameters** | Alpha (initial volatility), Beta (CEV elasticity), Rho (correlation of forward and vol), Nu (vol-of-vol) |
| **Typical use** | Pricing [swaptions](/option/), [caps and floors](/option/), bermudan optionality; calibration to liquid benchmark strikes |
| **Advantage** | Captures fixed-income smile naturally; closed-form approximation exists (faster than Monte Carlo for routine hedging) |
| **Compared to** | Black-Scholes (constant vol), [Heston model](/heston-stochastic-volatility-model/) (equity-focused), Hull-White (deterministic vol) |
| **Standard in** | Bond-dealer operations; swaption and cap pricing; [hedge fund](/hedge-fund/) portfolios |

</aside>

## Why equity models fail for rates

The [Black-Scholes model](/black-scholes-model/) and even the [Heston model](/heston-stochastic-volatility-model/) were built with equities in mind. Equities have a natural lower bound (zero) but no obvious ceiling. Forward interest rates, by contrast, are level-constrained: they cannot go far negative (in most economies, central banks set a floor), and they rarely spike without economic dislocation.

Moreover, the implied volatility behaviour in rates markets is *inverted* compared to equities. In equities, out-of-the-money puts (far downside) trade at higher implied volatilities than at-the-money options. In rates, out-of-the-money swaptions—especially those far from the at-the-money strike—trade at *lower* implied volatilities. This reflects the belief that extreme moves in rates are less likely than extreme moves in equity prices.

## The SABR framework: CEV and lognormal

SABR models the forward rate \(F_t\) using a constant-elasticity-of-variance (CEV) process:

\(dF = \alpha F^\beta dW_F\)

and volatility \(\sigma_t\) using a lognormal martingale:

\(d\alpha = \nu \alpha dW_\sigma\)

where \(W_F\) and \(W_\sigma\) are correlated Wiener processes with correlation \(\rho\), and \(\nu\) is the volatility of volatility.

The four parameters are:

- **Alpha**: the initial value of volatility; scales the model to current market levels
- **Beta**: elasticity of volatility to the forward rate (0 = normal, 1 = lognormal, between = CEV)
- **Rho**: correlation between forward-rate and volatility shocks; typically negative (rising rates = falling vol)
- **Nu**: volatility of volatility; how much the volatility process jitters

## The CEV exponent and strike behaviour

The \(\beta\) parameter is crucial. When \(\beta = 1\), the forward follows lognormal dynamics (like Black-Scholes). When \(\beta = 0\), it is normal (arithmetic Brownian motion). Most practitioners calibrate \(\beta\) between 0.5 and 1, depending on the market and tenor.

A lower \(\beta\) means the forward's volatility is higher at low rates and lower at high rates—this naturally produces the inverted smile. Out-of-the-money calls (high-strike swaptions) have lower implied volatility because the forward's conditional volatility is low at elevated levels. This matches what traders observe and is one reason SABR became dominant.

## Closed-form approximation

Unlike Heston, SABR does not have an exact closed-form solution. However, Hagan et al. (who published the model) provided an accurate approximation formula for the implied volatility as a function of strike, forward, and SABR parameters:

$$\sigma_{impl}(K) = \frac{\alpha}{F_0^\beta} \cdot z \cdot \frac{x(z)}{1 + \frac{\rho\nu\alpha}{4F_0^\beta} + ...}$$

where \(z\) and \(x(z)\) encode the forward-strike relationship and the model's dynamics. This approximation is accurate to within a few basis points and evaluates in microseconds, making it ideal for real-time hedging.

The [option](/option/) price itself is then computed using this implied volatility plugged into the Black-Scholes formula or a normal-volatility formula, depending on convention.

## Calibration to swaptions and caps

In practice, a dealer calibrates SABR parameters to market prices of liquid [swaptions](/option/) and [caps](/option/). Given observed implied volatilities across strikes and tenors, the quant team solves:

Minimize: Σ(SABR implied vol - market observed implied vol)²

Over the parameters \(\alpha, \beta, \rho, \nu\).

Once calibrated, SABR generates prices and [Greeks](/delta/) for exotic or bespoke swaptions, [bermudan swaptions](/option/) (which allow exercise on multiple dates), and other exotics that don't trade liquid prices.

Stability of calibration is important: parameters should not jump wildly day-to-day unless the market has genuinely shifted. Quants employ regularization (penalizing parameter changes) to achieve smooth, stable calibrations.

## Greeks: delta, vega, and gamma

SABR [Greeks](/delta/) are derived either from the closed-form approximation (via finite differences) or from Monte Carlo. The [delta](/delta/) hedging ratio tells a dealer how much of the underlying forward to buy or sell to neutralize the option's directional exposure.

[Vega](/vega/) measures sensitivity to shifts in the initial volatility \(\alpha\). Dealers often quote swaption prices in implied-volatility terms (e.g., "25 basis points volatility"), so [vega](/vega/) is how much the price changes if the market's volatility quote shifts by 1 bp.

More subtly, SABR produces [Greeks](/delta/) that vary with the strike—a phenomenon absent in Black-Scholes but present in real markets. An out-of-the-money swaption has different [gamma](/gamma/) (curvature) and [theta](/time-decay-theta/) (time decay) than an at-the-money one, and SABR captures this.

## Strengths and limitations

**Strengths:**
- Explains inverted volatility smile and skew in rates markets
- Closed-form approximation is fast and accurate
- Parameters are economically intuitive
- De facto market standard; all major dealers and pricing systems support it

**Limitations:**
- The approximation formula breaks down far out-of-the-money (extreme strikes)
- Calibration is non-unique; different parameter sets can fit the same strikes equally well
- [Beta](/beta/) is sometimes treated as fixed (not calibrated), introducing model risk
- Normal dynamics of rates near zero are not well-captured; some practitioners use a displacement parameter (shifted SABR) to fix this

## Extensions: displaced SABR and multi-curve

Displaced SABR shifts the forward rate by a constant, allowing negative forwards to be modeled while maintaining lognormal dynamics above zero. This became necessary post-2008 when negative rates emerged in some economies.

Multi-curve SABR calibrates separate volatility surfaces to different [basis](/bid-ask-spread/) curves (funding curves, projection curves), essential for pricing [floating-rate notes](/bond/) and basis swaps.

## See also

<div class="wiki-seealso">

### Closely related

- [Heston Stochastic Volatility Model](/heston-stochastic-volatility-model/) — equity-focused analogue; different economic assumptions
- [Interest Rate Option](/option/) — the instrument class SABR prices
- [Swaption](/option/) — one of the main traded instruments SABR calibrates to
- [Cap and Floor](/option/) — interest-rate [options](/option/); SABR prices caplets and floorlets
- [Implied Volatility](/implied-volatility/) — extracted from swaption and cap prices; SABR generates surface
- [Delta](/delta/) — [Greeks](/delta/) from SABR vary naturally with strike

### Wider context

- [Black-Scholes Model](/black-scholes-model/) — baseline model; SABR extends it for rates
- [Option Premium](/option-premium/) — amount paid upfront; SABR computes this
- [Bond](/bond/) — underlying instrument for [interest-rate options](/option/)
- [Volatility Smile](/volatility-smile/) — inverted smile in rates; SABR's key empirical fit
- [Hedge Fund](/hedge-fund/) — major user of SABR for fixed-income derivatives strategies
- [Value at Risk](/value-at-risk/) — uses SABR [Greeks](/delta/) for [scenario](/value-at-risk/) analysis of [swaption](/option/) portfolios

</div>

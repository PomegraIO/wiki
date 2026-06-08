---
title: "Jump-Diffusion Model"
description: "Merton's extension of Black-Scholes that adds sudden discrete price jumps to capture fat-tailed return distributions."
keywords:
  - Poisson jumps
  - fat tails
  - option pricing
  - jump risk
  - Merton model
image: "/svg/derivatives.svg"
---

*The **jump-diffusion model** is Robert Merton's extension of [Black-Scholes-model](/black-scholes-model/) that appends sudden, discontinuous price jumps to the standard continuous diffusion process. Instead of assuming that prices move in smooth increments (as Brownian motion dictates), jump-diffusion models allow for occasional large, instantaneous moves—gaps that reflect news, earnings surprises, or systemic shocks—giving the model fat tails and better capturing real return distributions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Jump-Diffusion Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">Black-Scholes plus sudden discontinuous jumps, modelled via Poisson process.</div>

|   |   |
|---|---|
| **What it is** | An option pricing model combining geometric Brownian motion with random jump events |
| **Key insight** | Real prices gap; a pure diffusion (like Black-Scholes) misses crash risk and fat tails |
| **Jump arrivals** | Governed by a Poisson process; jump sizes are random (typically lognormal) |
| **Main use** | Pricing options in markets with crash risk, earnings announcements, central bank decisions |
| **Also called** | Merton's jump-diffusion model, jump-risk model |
| **Key parameters** | Jump intensity λ, mean jump size μⱼ, jump-size volatility σⱼ |
| **Advantage over Black-Scholes** | Captures fat tails and [tail-risk](/tail-risk/) premia in [option](/option/) prices |

</aside>

## Why Black-Scholes misses discontinuous price moves

The [Black-Scholes-model](/black-scholes-model/) assumes the underlying stock price follows a geometric Brownian motion:

dS/S = μ dt + σ dW

This process is **continuous**: prices change smoothly, with no jumps. In a small time interval dt, the price move dS is bounded—it cannot be arbitrarily large. Over an entire year, with many small increments, the returns are approximately normally distributed (by the central limit theorem), with no fat tails.

But real markets, especially at the stock level, are full of discontinuities:

- **Earnings announcements.** A company reports unexpectedly weak earnings, and the stock gaps down 10% in minutes.
- **News and events.** Regulatory decisions, lawsuits, mergers, disasters can cause sudden repricing.
- **Market-wide shocks.** Flash crashes, geopolitical events, central bank surprises cause synchronized gaps across many securities.
- **Empirical fat tails.** Real stock return distributions have far more probability mass in the extreme tails than a normal distribution predicts.

These gaps represent **jump risk**—a source of uncertainty that Black-Scholes cannot price. An option seller holding a short [call-option](/call-option/) is exposed to the risk that the stock jumps up and the option finishes deep in the money, destroying the hedge.

Merton's jump-diffusion model adds a second source of randomness to capture these events.

## The model: Brownian motion plus jumps

In Merton's framework, the stock price evolves as:

dS/S = μ dt + σ dW + (J − 1) dN

where:
- dW is a Brownian increment (continuous, as before)
- dN is a Poisson counter: it equals 1 with intensity λ (the jump arrival rate) and 0 otherwise
- J is the random jump size; if J = 1.10, the stock jumps up 10%

Intuitively:
- Most of the time (dN = 0), the price follows Black-Scholes-like continuous motion.
- At random times (Poisson events with expected frequency λ per year), the price jumps by a factor J.

The jump size J is itself random. A common assumption is that ln(J) is normally distributed:

ln(J) ~ N(μⱼ, σⱼ²)

where μⱼ is the mean log jump size and σⱼ is its standard deviation. This ensures J is positive (since e^x > 0 for all x).

## Key parameters and their interpretation

**Jump intensity (λ).** The expected number of jumps per year. If λ = 0.05, you expect about one jump every 20 years. If λ = 2, you expect two jumps per year on average.

**Mean jump size (μⱼ or E[J−1]).** The average percentage move when a jump occurs. If μⱼ = 0, jumps are symmetric on average (as many up-jumps as down-jumps). If μⱼ < 0, jumps are biased downward (a "crash risk" model).

**Jump-size volatility (σⱼ).** The standard deviation of log jump sizes. Larger σⱼ means jump sizes are more variable—some jumps are tiny, others are huge.

In practice, empirical estimates for equities might be:
- λ ≈ 0.1 to 0.5 per year (one jump every 2–10 years on average, though this varies wildly by stock)
- μⱼ ≈ −0.05 to −0.10 (a typical jump is a loss of 5–10%)
- σⱼ ≈ 0.10 to 0.30 (jump sizes have significant dispersion)

## Why jump-diffusion models are hard to price

Unlike Black-Scholes, there is no simple closed-form formula for option prices in a pure jump-diffusion model. The reason is that jump risk cannot be perfectly hedged with the stock alone. You need an extra source of randomness (the jump timing and size), and hedging it requires trading in other derivatives or accepting residual risk.

However, under the risk-neutral measure, Merton shows that you can price an option using an expectation over possible jump scenarios:

The option price is a weighted average of Black-Scholes prices, each calculated assuming a fixed number of jumps occur over the option's life. If zero jumps occur (probability e^(−λT)), the price is Black-Scholes. If exactly one jump occurs (probability λT e^(−λT)), you integrate over all possible jump timings and sizes, compute the Black-Scholes value conditional on that jump, and weight it by the probability.

In practice, this integral is computed numerically or via Monte Carlo simulation:

1. Simulate a large number of price paths.
2. For each path, randomly decide whether a jump occurs (based on λ) and, if so, what size (based on μⱼ and σⱼ).
3. Compute the [call-option](/call-option/) payoff at expiration for each path.
4. Average the payoffs and discount to present value.

## How jump-diffusion affects option prices

Jump-diffusion models change option prices relative to Black-Scholes in predictable ways:

**Out-of-the-money [call-option](/call-option/) become more expensive.** If there is a risk of an upward jump, a call that is currently out-of-the-money has a chance of ending in-the-money due to the jump. Black-Scholes ignores this. A jump-diffusion model prices it in.

**Out-of-the-money [put-option](/put-option/) become much more expensive.** This reflects [crash-risk](/tail-risk/) premium: traders are willing to pay more to insure against a sudden downward jump.

**The [volatility smile](/volatility-smile/) appears.** In Black-Scholes with constant volatility, all [implied volatility](/implied-volatility/) values are the same. But empirically, far out-of-the-money options trade at higher implied vol. Jump-diffusion explains this: investors fear tail events, so they bid up the price of far OTM protection. When you back out the Black-Scholes volatility from a jump-diffusion price, you get higher vols for extreme strikes.

## Jump-diffusion and hedging

A trader holding a short [call-option](/call-option/) can delta-hedge using the stock, but this hedge is incomplete: it does not protect against jumps. If the stock gaps up overnight, the short call is in the money, and the [delta](/delta/) hedge was in the wrong size (computed assuming smooth motion).

This gap risk is priced into the [option-premium](/option-premium/). The option buyer is compensated for bearing jump risk; the seller charges extra to compensate for hedging difficulty.

In practice, traders manage jump risk by:

1. **Buying tail hedges.** Holding out-of-the-money [put-option](/put-option/) to protect against large downward jumps.
2. **Adjusting position sizes.** Sizing short positions smaller than Black-Scholes [delta](/delta/) would suggest, to reduce exposure to gap risk.
3. **Diversification.** Holding positions in names with uncorrelated jump risks, so not all gaps happen at once.

## Extending jump-diffusion: stochastic volatility and multiple jump types

The basic Merton model assumes constant volatility σ and a single (constant-intensity) Poisson jump process. Extensions make it more realistic:

**Stochastic volatility with jumps.** Combine a jump-diffusion base with a stochastic volatility model (e.g., Heston). Volatility itself becomes random and mean-reverting, while jumps add tail risk. This is powerful for fitting smiles but requires numerical methods.

**Multiple jump types.** Different news (earnings, sector shocks, market-wide crashes) might have different jump distributions. You can add several Poisson processes, each with its own intensity, mean size, and size volatility. This is more realistic but requires estimating more parameters.

**Lévy processes.** A fully general extension treats the price process as a Lévy process, which allows flexible jump arrival and jump-size distributions. Jump-diffusion is a special case of a Lévy process (specifically, a Lévy process that is a compound Poisson process plus a Brownian motion).

## Calibrating jump-diffusion models to market data

Estimating λ, μⱼ, and σⱼ from observed option prices is an inverse problem:

1. **Market quotes.** Gather implied volatilities for [call-option](/call-option/) and [put-option](/put-option/) across many strikes.
2. **Optimize parameters.** Adjust λ, μⱼ, σⱼ (and the continuous volatility σ) to minimize the difference between model prices and market quotes.
3. **Validate.** Check that the calibrated model gives economically sensible predictions—e.g., higher implied vol for OTM puts than calls, reflecting downward crash risk.

This calibration is computationally intensive because option prices in jump-diffusion require numerical integration or simulation. But it is standard practice in derivatives trading desks.

## Empirical evidence for jumps

Do real stock prices really jump? Empirical research says yes, though debate persists about how much of the return distribution is explained by large discrete jumps versus continuous diffusion:

- **Stock returns have fat tails.** The probability of a 10%+ move is much higher than Black-Scholes predicts.
- **Jump clustering.** Large moves tend to cluster around earnings announcements, macroeconomic releases, and systemic events.
- **Index vs. stock jumps.** Broad indices (like the S&P 500) jump less frequently than individual stocks, because idiosyncratic jumps average out.

However, separating true jumps from a stochastic-volatility process with continuous paths is statistically subtle. A Heston-type model (continuous but with random volatility) can generate similar-looking returns to a Merton model (continuous plus jumps). Both can fit market data.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes-model](/black-scholes-model/) — The continuous-motion baseline that jump-diffusion extends
- [Option](/option/) — The derivative that jump-diffusion prices
- [Call-option](/call-option/) and [put-option](/put-option/) — The option types affected by jump risk
- [Implied volatility](/implied-volatility/) — The volatility input to pricing; jump-diffusion explains the smile
- [Volatility-smile](/volatility-smile/) — The empirical pattern of higher implied vol for OTM options; jump-diffusion generates this
- [Local-volatility-model](/local-volatility-model/) — An alternative framework for fitting the volatility smile
- [Delta](/delta/) — The hedge ratio; jump-diffusion shows why [delta](/delta/) hedges are incomplete

### Wider context

- [Tail-risk](/tail-risk/) — The concentration risk of large, rare losses that jump-diffusion models
- Stochastic volatility — Random volatility can be combined with jumps for richer models
- Risk management — Jump risk is a key source of portfolio losses and requires active hedging
- Crash risk — The downward jump risk priced into index options and portfolio insurance
- Derivative — The broad class of instruments priced using jump-diffusion frameworks

</div>

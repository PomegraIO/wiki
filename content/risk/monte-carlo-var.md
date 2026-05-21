---
title: "Monte Carlo VaR"
description: "Monte Carlo value-at-risk is a method of estimating portfolio loss by simulating thousands or millions of possible future scenarios using probabilistic models, then calculating loss percentiles from the simulated outcomes."
keywords:
  - Monte Carlo VaR
  - simulation VaR
  - stochastic simulation
  - Monte Carlo simulation
  - risk simulation
image: "https://picsum.photos/seed/monte-carlo-var/900/600"
---

*Monte Carlo value-at-risk (Monte Carlo VaR) is a risk measurement method that simulates thousands or millions of possible future market scenarios using probabilistic models of price movements, correlations, and volatility. The [value-at-risk](/value-at-risk) is then calculated from the distribution of simulated portfolio losses.*

<div class="wiki-hatnote">

This entry covers Monte Carlo VaR calculation. For alternative VaR methods, see [parametric-var](/parametric-var) and [historical-var](/historical-var); for the general [value-at-risk](/value-at-risk) concept.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Monte Carlo VaR — key facts</div>

<img src="https://picsum.photos/seed/monte-carlo-var/900/600" alt="A simulation showing many possible price paths branching from an initial point" />

<div class="wiki-infobox-caption">Monte Carlo VaR simulates thousands of future paths to estimate tail losses.</div>

|   |   |
|---|---|
| **Method** | Simulate many scenarios; calculate portfolio loss for each; use percentile |
| **Flexibility** | Handles any instrument, any distribution; can model complex dynamics |
| **Computational cost** | High; requires thousands or millions of simulations |
| **Accuracy** | As accurate as the underlying models; no distributional assumption errors |
| **Scenario quality** | Depends entirely on the quality of price movement models |
| **Use cases** | Complex portfolios, derivatives, non-linear instruments |
| **Primary risk** | [Model-risk](/model-risk); simulated paths only as good as the model |

</aside>

## How Monte Carlo VaR works

**Step 1: Define models for price movements.**
For each asset in the portfolio, define how its price evolves. Common model: the geometric Brownian motion, where price drifts at some rate and is buffeted by random shocks (volatility).

Example: Stock price follows:
dS = μS dt + σS dW

Where μ is the drift (expected return), σ is volatility, and dW is a random shock.

**Step 2: Generate random scenarios.**
Use a random number generator to create thousands (or millions) of possible future paths for each asset. Each path represents one possible future over the time horizon (e.g., 10 days).

**Step 3: Calculate portfolio value in each scenario.**
For each simulated scenario, calculate the portfolio's value at the horizon (e.g., 10 days from now). Account for:
- Changes in underlying asset prices.
- Changes in correlations (if modeled).
- Non-linear effects (e.g., [options](/option) become more or less in-the-money).

**Step 4: Calculate loss distribution.**
Sort the simulated portfolio values from best to worst. Calculate the loss in each scenario.

**Step 5: Extract VaR.**
For 99% VaR, find the worst 1% of simulated scenarios and use the loss in the 99th percentile worst scenario as the VaR.

## Advantages of Monte Carlo VaR

**Flexibility.** Can handle any instrument, any distribution, any dynamic. Options, bonds with embedded options, exotic derivatives — all can be simulated.

**Realism.** Can model fat tails, jumps in prices, volatility clustering, and correlation breakdowns — all empirically observed in markets.

**No distributional assumption errors.** Unlike [parametric-var](/parametric-var), there is no assumption that returns are normal. The distribution emerges from the simulations.

**Non-linear instruments.** Options are non-linear; their value does not move linearly with the underlying. Monte Carlo naturally handles this.

**Multiple risk factors.** Can model many correlated risk factors (rates, FX, volatility, credit spreads, etc.) simultaneously.

## Disadvantages of Monte Carlo VaR

**Computational cost.** Simulating a million scenarios for a portfolio of 100 assets requires billions of calculations. It is expensive and slow.

**Model risk.** The accuracy of Monte Carlo VaR is entirely dependent on the quality of the underlying models. If the price movement model is wrong, the VaR is wrong.

**Parameter estimation.** You still need to estimate volatility, correlation, and drift. Errors in these estimates feed into simulation errors.

**Scenario quality.** The simulated scenarios are only as realistic as the model. If the model does not capture fat tails, the simulated worst scenarios will not either.

**Black swan blindness.** Monte Carlo simulates based on historical patterns. A new type of tail event (a [black swan](/black-swan)) will not appear in simulations.

## Example: Monte Carlo VaR for a stock portfolio

Suppose a $100M portfolio of 2 stocks, A and B, each $50M.

**Models:**
- Stock A: daily return ~ Normal(0.05%, 1.5%)
- Stock B: daily return ~ Normal(0.05%, 1%)
- Correlation: 0.5

**Simulation:**
1. Generate 100,000 random scenarios of 10-day future returns for A and B.
2. For each scenario, calculate portfolio return.
3. Calculate portfolio loss in each scenario.
4. Sort losses from worst to best.
5. 99% VaR = the 1,000th worst loss (worst 1% of 100,000).

Suppose the 1,000th worst scenario resulted in a loss of $3.5M.

**Result:** 10-day 99% Monte Carlo VaR = $3.5M.

## When Monte Carlo VaR is essential

- **Options portfolios.** [Options](/option) are non-linear; Monte Carlo handles this naturally.
- **Complex instruments.** Structured products, exotics, callable [bonds](/bond) — anything with embedded optionality.
- **Multiple risk factors.** When interest rates, FX, volatility, and credit spreads all matter and are correlated.
- **Stress scenarios.** You can run the simulation under "what if" conditions (e.g., 10% stock decline) to see portfolio impact.

## Model risk in Monte Carlo VaR

The greatest risk in Monte Carlo VaR is [model-risk](/model-risk): the model for price movements is wrong.

Example: A model assumes stock prices follow a geometric Brownian motion (continuous, no jumps). In reality, prices can jump sharply on earnings announcements or crises. The model's simulated scenarios do not include jumps, so Monte Carlo VaR underestimates tail risk.

This is why sophisticated risk managers pair Monte Carlo with [stress-testing](/stress-testing) and [scenario-analysis](/scenario-analysis). Monte Carlo gives a baseline; scenarios test extremes the model might miss.

## Practical use

Large banks and hedge funds use Monte Carlo VaR extensively because:
1. Portfolios are complex; simpler methods do not work.
2. Risk frameworks allow Monte Carlo as an acceptable method.
3. Computing power is cheap relative to the cost of mispricing risk.

But they also:
- Validate the underlying models rigorously.
- Backtest to ensure actual losses do not exceed predictions.
- Supplement with [stress-testing](/stress-testing) and [expected-shortfall](/expected-shortfall).
- Use multiple methods ([parametric](/parametric-var), [historical](/historical-var), Monte Carlo) to cross-check.

## See also

<div class="wiki-seealso">

### Closely related

- [Value-at-risk](/value-at-risk) — the VaR concept itself
- [Parametric-var](/parametric-var) — simpler, faster, less flexible
- [Historical-var](/historical-var) — empirical, no distributional assumption
- [Expected-shortfall](/expected-shortfall) — tail loss average
- [Model-risk](/model-risk) — primary risk in Monte Carlo VaR

### Application areas

- [Option](/option) — most important use of Monte Carlo VaR
- [Derivative](/option) — complex derivatives require Monte Carlo
- [Stress-testing](/stress-testing) — complements Monte Carlo
- [Scenario-analysis](/scenario-analysis) — explicit scenarios complement simulations
- [Basel capital](/capital-adequacy) — allows Monte Carlo as approved method

</div>

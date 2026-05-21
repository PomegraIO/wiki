---
title: "Binomial Option Pricing"
description: "The binomial option pricing model values options by building a tree of possible future stock prices and working backward to calculate option value at each node."
keywords:
  - binomial option pricing
  - binomial tree
  - option valuation
  - discrete pricing
  - american options
image: "https://picsum.photos/seed/binomial-option-pricing/900/600"
---

*The **binomial option pricing model** values [option](/option)s by constructing a discrete tree where at each time step, the underlying [stock](/stock) can move up or down. Starting from expiration and working backward, the model calculates option value at each node as the probability-weighted average of future values, discounted to present value. The binomial model can handle [american-option](/american-option)s (early exercise), dividends, and other features [Black-Scholes model](/black-scholes-model) cannot, making it more flexible though less elegant.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Binomial Option Pricing — key facts</div>

<img src="https://picsum.photos/seed/binomial-option-pricing/900/600" alt="Tree structure of future stock prices" />

<div class="wiki-infobox-caption">Binomial tree: branching paths to all outcomes.</div>

|   |   |
|---|---|
| **Steps** | Typically 50–500 steps to expiration |
| **Branches** | Up and down at each node |
| **Computation** | Backward recursion from expiration |
| **Early exercise** | Can check at each node |
| **Dividends** | Handled at specific dates |
| **Accuracy** | Improves with more steps; converges to Black-Scholes |
| **Volatility** | Input to determine up/down move sizes |
| **Interest rates** | Discount rate for time value |
| **Suited for** | American options, exotics, path dependencies |
| **Complexity** | More computational than Black-Scholes; simpler than Monte Carlo |

</aside>

## The binomial tree structure

In the simplest binomial model:
- Start at today's stock price S
- At each step, stock can move up by factor u or down by factor d
- Continue for n steps to [expiration date](/expiration-date)
- At expiration, calculate option payoff for each possible final price
- Work backward: at each node, value = probability-weighted discounted payoffs

**Example:**
- Stock at $100
- 1 year to expiration
- u = 1.1 (up 10%), d = 0.9 (down 10%)
- 2 steps (semi-annual)

Tree:
- Year 0: $100
- Year 0.5: $110 or $90
- Year 1: $121, $99, or $81

For each final state, calculate option payoff (e.g., $110 − $100 = $10 for a $100 call if price is $110 at expiration).

## Backward recursion

At each node working backward:

Node value = [p × up_value + (1−p) × down_value] / (1 + r)

Where p is the risk-neutral probability of an up move (derived from volatility).

For [american-option](/american-option)s, also check: should I exercise now or hold? Take the max of exercise value or hold value.

## Convergence to Black-Scholes

As the number of steps increases, the binomial model's prices converge to [Black-Scholes model](/black-scholes-model) prices. With 500 steps, binomial prices are nearly identical to Black-Scholes for [european-option](/european-option)s.

This convergence validates both models and allows practitioners to choose based on implementation needs.

## Early exercise and American options

The binomial model shines for [american-option](/american-option)s, where early exercise can be optimal. At each node, the model checks: is it better to exercise now or hold?

For a [call option](/call-option) with [dividend](/dividend), you might exercise just before the dividend goes ex-date. The binomial model captures this.

[Black-Scholes model](/black-scholes-model) cannot, requiring [binomial-option-pricing](/binomial-option-pricing) or other numerical methods.

## Tuning volatility and time steps

The up/down factors are set based on [volatility](/historical-volatility):

u = e^(σ√Δt)
d = 1/u

Where σ is [volatility](/historical-volatility) and Δt is the time step.

Higher volatility → larger up/down moves. More steps → finer granularity.

## Advantages and limitations

**Advantages:**
- Flexible; handles early exercise, dividends, exotic features
- Intuitive; visualize price paths
- Converges to Black-Scholes for confirmation

**Limitations:**
- Computationally intensive (500+ steps for decent accuracy)
- Assumes discrete jumps; real prices continuous
- Harder to compute Greeks numerically

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes model](/black-scholes-model/) — continuous alternative
- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — simulation alternative
- [American option](/american-option/) — primary application
- [European option](/european-option/) — can also price

### Inputs and parameters

- [Volatility](/historical-volatility/) — determines up/down moves
- [Interest rates](/interest-rate/) — discount factor
- [Dividend](/dividend/) — handled in trees
- [Time to expiration](/expiration-date/) — determines tree steps

### Greeks and Greeks

- [Delta](/delta/) — computed via nodes
- [Gamma](/gamma/) — numerical approximation
- [Theta](/theta/) — time step effects
- [Vega](/vega/) — volatility sensitivity

### Deeper context

- [Option](/option/) — the instrument being priced
- [Option pricing](/option-premium/) — fundamental problem
- [Derivatives pricing](/black-scholes-model/) — valuation foundation

</div>

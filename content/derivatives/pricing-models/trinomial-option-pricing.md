---
title: "Trinomial Option Pricing"
description: "A lattice-based option pricing method using three transitions per step, improving convergence and enabling American-style exercise."
keywords:
  - trinomial tree
  - option pricing
  - lattice method
  - american options
  - binomial tree
image: /svg/derivatives.svg
---

*The **trinomial option pricing model** extends the binomial lattice by allowing three transitions at each time step—up, down, or middle—rather than two. This added flexibility improves convergence speed, smooths the pricing surface across strikes, and makes it natural to handle American-style [options](/option/) (which can be exercised before maturity). The trinomial method trades slightly more computation per node for better numerical stability and faster accuracy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trinomial Option Pricing — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for quantitative derivatives pricing." />

<div class="wiki-infobox-caption">A three-branch lattice that converges faster than binomial trees and handles early exercise naturally.</div>

|   |   |
|---|---|
| **What it is** | A recombining lattice where each node branches into three paths: up, middle, down |
| **Transitions per step** | Three states: S×u, S, S×d (or S×u, S×m, S×d with u > m > d) |
| **Basis** | Discretization of the continuous stock-price process |
| **Advantage over binomial** | Faster convergence; smoother pricing surface; easier for American [options](/option/) |
| **Typical parameters** | Step size Δt; up factor u, middle factor m, down factor d |
| **Best use case** | American [options](/option/), highly sensitive to local volatility |
| **Limitation** | Slower than FFT for European [options](/option/); requires memory for large grids |

</aside>

## From binomial to trinomial: adding a middle state

The binomial [option](/option/) pricing tree, introduced by Cox, Ross, and Rubinstein, discretizes the stock price into two branches at each step. At each node with stock price *S* and time *t*, the next step leads to *S*×*u* (up) or *S*×*d* (down). This simplicity is powerful—the tree recombines (a path up then down reaches the same node as down then up), and backward recursion yields the [option](/option/) value in *O*(*n*²) time, where *n* is the number of steps.

The trinomial tree adds a third branch: the stock can move up, down, *or stay at the same level*. This middle state, at price *S*×*m* (where *m* is typically 1, or sometimes *u*^0.5 for continuity), provides an extra degree of freedom in calibrating probabilities to match the underlying volatility and other distributional properties.

The three transition probabilities (*p_u*, *p_m*, *p_d*) are chosen so that:

- The expected return matches the drift (typically the risk-free rate).
- The variance of the log return matches the volatility.
- The tree is arbitrage-free (no dominated strategies).

With three degrees of freedom, the trinomial tree has more flexibility than the binomial. A binomial tree with up factor *u* and down factor *d* = 1/*u* must satisfy specific relationships between *u*, *d*, and the probability *p*. The trinomial tree's extra parameter allows tighter matching of the underlying volatility and smoother convergence.

## Calibrating the trinomial tree

A standard parameterization (due to Boyle) sets:

- Up factor: *u* = exp(σ√(3Δ*t*))
- Middle factor: *m* = 1 (the stock stays flat)
- Down factor: *d* = 1/*u*

The three transition probabilities are then:

- *p_u* = (1/6) + (r − σ²/2)√(Δ*t*) / (2σ)
- *p_m* = (2/3)
- *p_d* = (1/6) − (r − σ²/2)√(Δ*t*) / (2σ)

where *r* is the risk-free [interest rate](/interest-rate/) and σ is the volatility.

The factor √3 arises from the three-state discretization and ensures the variance of the tree matches the continuous volatility. The middle probability is pinned at 2/3, leaving the drift adjustment to split between the up and down branches.

This calibration is remarkably robust. Unlike the binomial tree—which can produce negative probabilities if Δ*t* is too large—the trinomial tree remains well-behaved over a wider range of step sizes, improving convergence.

## Why trinomial converges faster

The binomial tree's convergence to the Black-Scholes price is *O*(1/*n*), where *n* is the number of steps. This means that to reduce error by a factor of 10, you must increase *n* by a factor of 100, a steep computational cost.

The trinomial tree converges at *O*(1/*n*²) under typical conditions—one order faster. Intuitively, the extra middle state allows the tree to approximate the continuous process more faithfully: the local distribution of returns is closer to normal, and the skewness of the tree is smaller.

In practice, a trinomial tree with 50 steps often matches the [Black-Scholes model](/black-scholes-model/) price to within a pip; a binomial tree requires 200–300 steps to achieve the same accuracy. For a trader pricing a large book of [options](/option/), this speedup is material.

## Handling American-style early exercise

A key advantage of the trinomial lattice is its natural handling of [American options](/option/). An American [put](/put-option/) or [call](/call-option/) can be exercised at any time before maturity, not just at expiration.

At each node in the lattice, the option value is the *maximum* of:

- The intrinsic value (exercise now), and
- The discounted expected value of holding (exercise later).

The backward recursion computes this maximum at each node. Because the trinomial tree has three branches, the recursion is:

**Option value** = max(intrinsic, discount × (*p_u* × value_up + *p_m* × value_middle + *p_d* × value_down))

The middle state is especially useful for American [puts](/put-option/). When a put is deep in the money (stock far below the strike), the up and down branches represent holding or exercising. The middle state, where the stock hovers near the current level, lets the recursion smoothly interpolate the exercise decision. This reduces oscillation and improves accuracy compared to a binomial tree, where the choice is binary at each node.

## Trinomial trees for exotic and path-dependent options

The lattice framework extends naturally to more complex derivatives. For instance:

- **Barrier options** (knock-out, knock-in): the tree is truncated or adjusted when the stock hits a barrier level.
- **Asian options** (payoff depends on average stock price): extra state variables track the running sum, enlarging the lattice dimensionality.
- **Callable bonds** (the issuer can redeem early): the lattice prices the bond coupon stream and compares it to the call value at each node.

The trinomial structure again helps: the middle state provides smoother transitions for path averaging and reduces the "lumpy" behavior of barrier hits.

## Trinomial trees for non-constant volatility

The trinomial framework adapts well to [local volatility](/cev-model/) models where volatility changes with the stock price or time. Instead of fixed *u* and *d* factors, each node uses volatility σ(*S*, *t*) to calibrate its up and down factors.

For example, under the [CEV model](/cev-model/), where σ(*S*) = σ₀ × *S*^(β−1), the trinomial tree can adjust its branching at each node to reflect the local volatility. This allows accurate pricing of [options](/option/) under leverage effects and [volatility skew](/volatility-smile/) without requiring stochastic volatility.

## Computational costs and comparison to alternatives

A trinomial tree with *n* steps has *O*(*n*²) nodes (like a binomial tree) and *O*(*n*³) total computations (three branches per node). For a typical book of equity [options](/option/), *n* = 50–100 is sufficient, yielding 7,500–40,000 nodes. Modern computers evaluate this in milliseconds.

Compared to other methods:

- **Finite-difference methods** solve the [option](/option/) pricing PDE on a grid. For European [options](/option/), they converge as fast as trinomial trees and are often faster in wall-clock time. For American [options](/option/), finite-difference with free-boundary conditions is also fast.
- **Monte Carlo simulation** is slower for vanilla [options](/option/) but excels at path-dependent and multi-asset [options](/option/).
- **Fourier methods** (FFT) are extremely fast for European [options](/option/) but do not handle American exercise easily.

For American equity [options](/option/), trinomial lattices remain a benchmark—fast, intuitive, and reliable.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes Model](/black-scholes-model/) — the continuous-time benchmark that lattice methods approximate
- [Option](/option/) — the derivative contract priced via trinomial trees
- [Binomial Option Pricing](/binomial-option-pricing/) — the predecessor lattice model with two branches
- [Constant Elasticity of Variance Model](/cev-model/) — adapts well to trinomial implementations
- [Finite Difference Methods for Options](/finite-difference-methods-options/) — an alternative numerical approach
- [Variance Gamma Model](/variance-gamma-model/) — a pure-jump model also requiring numerical pricing

### Wider context

- [American Option](/american-option/) — the early-exercise feature that trinomial trees handle naturally
- [Implied Volatility](/implied-volatility/) — calibrating tree volatility from market prices
- [Delta Hedging](/delta-hedging/) — using the tree's delta (branch probabilities) to hedge

</div>

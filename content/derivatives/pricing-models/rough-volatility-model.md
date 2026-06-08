---
title: "Rough Volatility Model"
description: "A framework where volatility follows a rough path driven by fractional Brownian motion, matching realized volatility persistence and limiting options smiles."
keywords:
  - rough volatility
  - fractional Brownian motion
  - Hurst parameter
  - volatility clustering
  - option pricing
  - derivatives modeling
image: "/svg/derivatives.svg"
---

*The **rough volatility model**, pioneered by Gatheral, postulates that volatility is not a smooth semimartingale but a rough path—one with local Hölder exponent less than 0.5, typically driven by a fractional Brownian motion with Hurst parameter $H \approx 0.1$ to 0.3. This counterintuitive geometry implies extreme volatility clustering and produces option [smiles](/volatility-smile/) that match market data with parsimony, while preserving the long-memory properties that empirical volatility exhibits.*

## The puzzle with standard models

Classical stochastic volatility models (Heston, SABR, etc.) assume volatility is a semimartingale: a process with finite quadratic variation that can be decomposed into a drift and a martingale part. These models produce realized volatility that is locally smooth (except at the discontinuities of the underlying, which can be added separately). If you simulate a path under Heston, the spot evolves predictably from its starting volatility level.

Empirical realized volatility tells a different story. Over intraday to daily horizons, volatility looks rough: it does not smooth out even as you aggregate data. A 1% move in the index followed by a 2% move followed by a 0.5% move does not reveal a steady underlying volatility; the _realized_ volatility (computed as $\sqrt{\sum r_i^2}$) jumps around. And crucially, high volatility today predicts high volatility tomorrow far more strongly than a mean-reverting stochastic vol model would suggest—a property called **volatility persistence**.

## Fractional Brownian motion and Hurst exponent

A fractional Brownian motion (fBm) with Hurst parameter $H \in (0, 1)$ is a Gaussian process with zero mean and the property that its increments over disjoint time intervals are not independent (unless $H = 0.5$, in which case it is ordinary Brownian motion). For $H < 0.5$, the process has **antipersistent** or **mean-reverting** properties: up moves are likely followed by down moves. For $H > 0.5$, the process is **persistent**: up moves tend to be followed by more up moves.

The Hölder exponent $\alpha$ of a path is the largest power such that $|X(t) - X(s)| \sim |t - s|^\alpha$ on average. An fBm with Hurst parameter $H$ has Hölder exponent exactly $H$. Ordinary Brownian motion ($H = 0.5$) has Hölder exponent 0.5, meaning paths are continuous but nowhere differentiable. For $H < 0.5$, paths are even rougher: they have more pronounced local oscillations, smaller local variation, and slower growth.

Empirical estimates of realized volatility's Hurst parameter sit around $H \approx 0.1$ to 0.3, far below 0.5. This means volatility is very rough indeed: it is fractal-like, with self-similar roughness at many scales.

## The rough volatility framework

In the rough volatility model, the spot price $S_t$ evolves as:

$$dS_t = \mu S_t \, dt + \sigma_t S_t \, dW_t$$

where $W$ is a standard Brownian motion, and $\sigma_t$ (or $v_t = \sigma_t^2$, the variance) evolves according to fractional dynamics, often in a log-normal form:

$$d \ln v_t = \kappa (m - \ln v_t) \, dt + \xi \, dB_t^H$$

where $B^H$ is an fBm with Hurst parameter $H$ and $\xi$ is a volatility-of-volatility scaling. The key parameters are $H$ (roughness), $\kappa$ (mean reversion speed), $m$ (long-run log-variance), and $\xi$ (vol-of-vol).

The correlation between $W$ and $B^H$ can be set to capture leverage effects (negative correlation means volatility spikes when the stock drops, a standard observation).

## Why roughness matters for option pricing

The rough dynamics imply that volatility has memory at all scales. If volatility is high today, it remains elevated tomorrow (persistence from $H < 0.5$), which affects option payoffs that depend on realized volatility. A variance swap, which pays realized variance, is priced higher under rough volatility than under a memoryless stochastic vol model, because the high-vol state will linger.

Second, the rough path property makes the limiting behavior of volatility non-trivial. As you reduce the step size in a numerical simulation, the volatility path does not converge to a smooth limit; instead, it reveals finer and finer texture. This produces a richer tail behavior in the spot distribution, naturally inflating out-of-the-money option prices.

Third, rough volatility produces a flat or even inverted [smile](/volatility-smile/) in log-moneyness across expirations—a finding that matches empirical data better than smooth stochastic vol models. The intuition is that the roughness of volatility induces a diffusive-like tail without the need for heavy-tailed innovations in the spot.

## Calibration and computation

Rough volatility models are harder to calibrate than Heston because the fBm component is not a semimartingale, so classical option-pricing formulas (Black–Scholes, Heston's semi-closed form) do not apply. Most practitioners use one of three approaches:

**Monte Carlo simulation.** Discretize the fBm (using Cholesky decomposition or circulant methods to generate correlated increments) and the spot dynamics together, then simulate paths and price options by averaging payoffs. This is flexible but slow.

**Characteristic function methods.** For some rough vol models (especially rough Bergomi, a common variant), the characteristic function of the log-spot is available in closed or semi-closed form, allowing for fast Fourier inversion to compute option prices. This is orders of magnitude faster than Monte Carlo.

**Neural network surrogates.** Researchers have trained deep neural networks to learn the mapping from model parameters and strike-expiry pairs to option prices, effectively creating a learned "lookup table" that allows millisecond pricing. This is an emerging approach, not yet standard on trading desks.

Calibration itself is a least-squares fit: you choose $H$, $\kappa$, $m$, $\xi$, and leverage correlation to minimize the difference between model option prices and market prices across a [volatility surface](/volatility-surface-construction/). Modern solvers can calibrate a rough vol model to the whole surface in minutes.

## The rough Bergomi model

The **rough Bergomi** model is a popular variant, where the variance process is:

$$v_t = v_0 \exp \left( \xi \int_0^t (t - s)^{H - 1/2} \, dW_s^v - \frac{1}{2} \xi^2 \int_0^t (t - s)^{2H - 1} ds \right)$$

This is a rough version of the Bergomi stochastic vol framework. It is log-normal (variance never goes negative), and it has a closed characteristic function, enabling fast pricing. It fits volatility smiles across equity index and FX derivatives exceptionally well with only a few parameters.

## Relationship to sticky-delta and smile dynamics

Rough volatility naturally produces smile dynamics that are closer to "sticky delta" than to pure local vol. When the underlying moves, the smile pattern follows the forward (or spot), not absolute strikes. This is because the roughness induces path dependence: the spot's realized path affects the volatility distribution, and in turn, the smile shape.

This meshes well with hedging workflows. A delta hedge computed using rough volatility and updated at market-moving times is more consistent with realized P&L than hedges based on smooth volatility models.

## Limitations and open questions

Rough volatility is a research frontier, not yet fully standardized on most trading desks. Challenges include:

**Computation scale.** For a whole portfolio (hundreds of exotics), daily repricing under rough vol is still expensive without neural surrogates. Hedging algorithms that run intraday are even costlier.

**Correlation and multi-asset.** Extending rough volatility to a basket of correlated assets is non-trivial. Defining a multivariate fBm and its coupling to multiple spots is an active research area.

**Central bank interventions and regime shifts.** Rough volatility models are calibrated in normal markets. If a central bank makes a shock announcement, the Hurst parameter may shift, and old calibrations become unreliable.

**Tail risk.** Rough volatility handles small moves well but can misprice extreme tail scenarios (10+ standard deviation moves) because it assumes continuous fBm dynamics, not jumps. Adding jump components is an important extension.

## Practical use cases

Rough volatility shines for **correlation and variance** products, where persistence matters. It is increasingly used by **exotic desks** hedging long-dated or barrier options, and by **quant** funds seeking realistic forward distributions for options trading. For **plain vanilla** index and equity options on liquid underlyings, the computational cost may not justify the slight pricing improvement unless the desk is very large and tick-sensitive.

## See also

<div class="wiki-seealso">

### Closely related

- [Volatility surface construction](/volatility-surface-construction/) — the smile that rough vol models aim to fit
- [Volatility smile](/volatility-smile/) — the empirical pattern the roughness explains
- Stochastic volatility — the parent class of models; Heston is the smooth alternative
- [Implied volatility](/implied-volatility/) — the input data used to calibrate rough vol
- Variance swap — a derivative where rough vol makes a quantitative difference
- [Stochastic local volatility model](/stochastic-local-volatility-model/) — a hybrid that can incorporate rough vol

### Wider context

- Option pricing — the discipline rough vol serves
- Monte Carlo — the simulation tool most rough vol implementations use
- Path dependence — the property that rough vol naturally captures
- Volatility clustering — the market behavior rough vol models
- Derivative risk management — the application domain for all these models

</div>

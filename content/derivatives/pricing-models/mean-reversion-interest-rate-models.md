---
title: "Mean Reversion in Interest Rate Models"
description: "Why interest rate models like Vasicek and CIR use mean reversion, what the speed parameter controls, and how it shapes bond prices and yield curves."
keywords:
  - mean reversion interest rate models
  - vasicek model
  - cox ingersoll ross
  - interest rate drift
  - short rate models
  - yield curve dynamics
---

*Interest rates do not wander randomly forever. Over decades, they revert toward a long-term average or "normal" level. This **mean reversion** is the defining feature of short-rate models like Vasicek and CIR, which use a drift term to pull the short rate toward an equilibrium value. The speed of that pull shapes how bond prices move and what yield curves look like.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mean Reversion — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Interest rates are pulled back toward a long-term average; the pull speed is a model parameter that determines bond-price sensitivity.</div>

|   |   |
|---|---|
| **Definition** | Drift in the short rate that pushes it toward a long-term mean |
| **Common models** | Vasicek, CIR, Hull-White |
| **Model form** | $dr = \kappa(\theta - r) dt + \sigma dW$ |
| **Parameters** | $\theta$ (long-run mean), $\kappa$ (speed of reversion), $\sigma$ (volatility) |
| **Effect on [yield curve](/yield-curve/)** | Higher speed → flatter long rates; lower speed → steeper curve |
| **Implication** | Rates cannot stray far; bonds are less risky at long maturities |

</aside>

## The Core Idea: Reversion vs. Drift

In a random walk, a variable drifts wherever initial conditions and noise take it. A stock price with no dividend grows at an expected return µ and can climb or fall without limit (in expectation).

Interest rates are different. Long-term inflation targets, central bank policy, and the natural productivity of capital create a gravitational pull toward a "normal" level. When the [federal funds rate](/federal-funds-rate/) is at 1%, it tends to rise over time. When it is at 6%, it tends to fall. This is mean reversion: the rate is drawn back to its long-run equilibrium.

A short-rate model captures this with a drift term. The simplest form is:

$$dr = \kappa(\theta - r) dt + \sigma dW$$

Breaking this down:

- **$r$:** The current short rate.
- **$\theta$:** The long-run mean (or "steady-state") rate toward which $r$ is attracted.
- **$\kappa$:** The **speed of reversion**, measured in inverse time units. Higher $\kappa$ means faster reversion.
- **$\sigma$:** The volatility of rate shocks.
- **$dW$:** A Wiener increment (random noise).

The drift term is $\kappa(\theta - r)$. If $r < \theta$ (rate is below the mean), the drift is positive, pushing $r$ upward. If $r > \theta$ (rate is above the mean), the drift is negative, pushing $r$ downward. The farther $r$ is from $\theta$, the stronger the pull.

## How Speed of Reversion Shapes the Path

Suppose the long-run mean $\theta = 4\%$, volatility $\sigma = 1\%$ per annum, and the current rate is $r_0 = 2\%$.

**High reversion speed ($\kappa = 0.5$ per year):**

The drift term is $0.5 \times (4\% - 2\%) = 1\%$ per year. The rate is expected to rise 1% per year on average, so it reaches 3% in a year, 3.5% in two years, approaching 4%. With rapid reversion, future values of $r$ are clustered tightly around the mean, and the distribution's standard deviation narrows as time extends into the future.

**Low reversion speed ($\kappa = 0.1$ per year):**

The drift term is $0.1 \times (4\% - 2\%) = 0.2\%$ per year. The rate rises slowly, taking much longer to approach 4%. With slow reversion, the rate can wander far from the mean for an extended period. The long-term distribution is much wider.

Mathematically, the conditional expectation of the rate at time $t$ is:

$$E[r_t | r_0] = \theta + (r_0 - \theta) e^{-\kappa t}$$

For high $\kappa$, the exponential $e^{-\kappa t}$ decays rapidly, so the effect of the initial condition $r_0$ fades quickly, and the rate converges to $\theta$ in expectation.

For low $\kappa$, the exponential decays slowly, so the initial condition persists longer.

## Impact on Bond and Yield Curve Pricing

Bond prices depend on expected future short rates. In a mean-reversion model:

- **High reversion speed:** Future short rates are expected to hover near the mean $\theta$. This stabilizes long-term bond prices. Long-duration bonds are less sensitive to shifts in the current short rate $r_0$.

- **Low reversion speed:** Future short rates are uncertain and can stay high (or low) for a long time. Long-term bond prices are more volatile and more sensitive to today's rate level.

This translates directly into the **yield curve shape**:

**High reversion speed** produces a flatter yield curve. Long rates are anchored to the mean, so forward rates (and spot rates for long maturities) are similar to near-term rates.

**Low reversion speed** produces a steeper yield curve when the short rate is below the mean. The market knows rates will rise, so investors demand higher yields on long bonds to compensate for the expected rate increases.

### Example: Vasicek Bond Prices

The Vasicek model, which uses the mean-reversion framework above, produces an explicit formula for zero-coupon bond prices:

$$P(r, t, T) = A(t, T) e^{-B(t, T) r}$$

where $B(t, T)$ measures the bond's sensitivity to the short rate. When $\kappa$ is large, $B$ is small (long bonds are less sensitive). When $\kappa$ is small, $B$ is large (long bonds are more sensitive).

For the yield curve, the forward rate at time $s$ seen from time $t$ is approximately:

$$f(t, s) \approx \theta + (f(t, t) - \theta) e^{-\kappa(s - t)}$$

where $f(t, t)$ is the current short rate. High $\kappa$ flattens this forward curve; low $\kappa$ keeps it steep.

## The Trade-Off: Tractability vs. Reality

**Vasicek models** allow the short rate to go negative, which is a weakness since real rates cannot drop below some floor. The model is simple and yields closed-form bond prices, making it popular for pricing and risk management.

**CIR (Cox-Ingersoll-Ross) models** enforce a non-negative rate by modifying the volatility term:

$$dr = \kappa(\theta - r) dt + \sigma \sqrt{r} \, dW$$

When $r$ approaches zero, the $\sqrt{r}$ term shrinks the volatility, which prevents the rate from going deeply negative. This is more realistic but less tractable (bond prices are harder to compute).

Both models include mean reversion as a core feature. The choice of $\kappa$ is calibrated from historical interest-rate data or from market prices of swaptions and other interest-rate derivatives.

## Calibrating the Reversion Speed

In practice, the speed $\kappa$ is estimated from historical rate observations or implied from option prices.

**Historical estimates** typically find $\kappa$ in the range $0.05$ to $0.3$ per year for the [U.S. dollar](/us-dollar/) short rate (e.g., the federal funds rate). This implies a half-life of reversion (time for the rate to move halfway back to the mean) of 2–14 years, depending on $\kappa$.

**Implied estimates** from swaption markets sometimes yield different values, suggesting that investors' expectations (embedded in option prices) differ from historical averages. This discrepancy is itself informative: if swaption-implied $\kappa$ is higher than historical $\kappa$, the market expects faster reversion than history suggests.

## Role in Derivatives Pricing

Short-rate models with mean reversion are used to price:

- **[Callable bonds](/callable-bond/):** The borrower's option to refinance is valuable when rates fall. Mean reversion bounds how low rates can go in the model, which affects the option's value.
- **[Bond options](/bond-etf/):** The payoff depends on future bond prices, which depend on the short rate path. Mean reversion controls the distribution of future rates.
- **[Interest-rate swaps](/interest-rate-swap/) and swaptions:** Pricing complex swap derivatives requires a dynamic interest-rate model.
- **[Fixed-rate mortgages](/fixed-rate-mortgage-personal/):** Prepayment risk depends on the future rate path, which is shaped by reversion.

## Limitations and Extensions

The basic mean-reversion framework has drawbacks:

1. **Single factor:** It assumes all rates move together. In reality, the yield curve twists and shifts in more complex ways. Multi-factor models (e.g., Hull-White with two factors) address this.

2. **Constant parameters:** In reality, $\kappa$ and $\theta$ may change over time or depend on the economic regime. Regime-switching models add this flexibility.

3. **Calibration trade-offs:** A model fit to historical volatility may not match market-implied volatility from options, or vice versa. Traders often use different parameter sets for pricing vs. hedging.

4. **Non-parallel shifts:** Mean reversion implies that the yield curve shape is stable. But in reality, long rates sometimes move more than short rates, violating the model's assumptions.

Despite these limitations, mean-reversion models remain the industry standard for bond and short-rate derivative pricing because they balance simplicity with economic intuition.

## See also

<div class="wiki-seealso">

### Closely related

- Vasicek Model — Foundational mean-reversion model for short rates
- Cox-Ingersoll-Ross Model — CIR model with non-negative rate constraint
- [Hull-White Model](/hull-white-model/) — Multi-factor and time-dependent extensions
- [Interest Rate](/interest-rate/) — The underlying rate and its drivers
- [Yield Curve](/yield-curve/) — How mean reversion shapes term structure
- [Interest Rate Swap](/interest-rate-swap/) — Derivative priced using rate models

### Wider context

- [Callable Bond](/callable-bond/) — Pricing depends on reversion-implied rate paths
- [Bond](/bond/) — Prices and yields depend on the future short-rate distribution
- [Federal Reserve](/federal-reserve/) — Central bank policy anchors the long-run mean
- [Duration](/duration/) — Interest-rate sensitivity affected by reversion speed
- Stochastic Volatility — Extensions to dynamic volatility models

</div>

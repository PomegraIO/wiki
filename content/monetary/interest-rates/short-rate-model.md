---
title: "Short-Rate Model"
description: "Stochastic models like Vasicek and Cox-Ingersoll-Ross that describe how the instantaneous interest rate evolves over time and price fixed-income securities."
keywords:
  - short-rate model
  - vasicek
  - cox-ingersoll-ross
  - bond pricing
  - stochastic process
  - interest rate dynamics
  - interest rate risk
---

*A **short-rate model** is a mathematical framework that describes how the instantaneous (overnight) interest rate evolves randomly over time, allowing traders, risk managers, and policymakers to forecast interest rates, price bonds, and measure [interest rate risk](/interest-rate-risk/). Rather than guessing future rates, a short-rate model specifies a stochastic equation—one with both predictable and random components—such that today's bond prices and the entire [yield curve](/yield-curve/) are consistent with the model's assumptions. The two most influential models are Vasicek (1977) and Cox-Ingersoll-Ross (1985).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Short-Rate Model — key facts</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for monetary economics." />

<div class="wiki-infobox-caption">Stochastic models of the policy rate provide a unified framework for bond valuation and risk management.</div>

|   |   |
|---|---|
| **What it is** | A mathematical model of instantaneous rate dynamics, used for bond pricing and risk analysis |
| **Purpose** | Price bonds, measure interest-rate risk, and forecast future rate paths |
| **Key models** | Vasicek, Cox-Ingersoll-Ross (CIR), and extensions (Hull-White, Black-Karasinski) |
| **Model output** | Bond prices at any future date; [yield curve](/yield-curve/) trajectory; value-at-risk metrics |
| **Limitation** | Assumes all rates move together; does not capture term-structure slope shifts |
| **Modern use** | [Derivatives pricing](/option/), risk management, monetary-policy simulation |

</aside>

## The Vasicek model

Introduced by Oldřich Vasicek in 1977, the Vasicek model is the simplest short-rate model and remains widely taught. It assumes the instantaneous rate r(t) follows a mean-reverting process:

dr = a(b − r) dt + σ dW

In English: the change in the rate has two parts. The first term, a(b − r), is the **drift**: if the rate is above the long-term mean b, the drift is negative (the rate is pulled downward toward the mean). If the rate is below b, the drift is positive (the rate is pulled upward). The parameter a controls the speed of mean reversion—how quickly the rate gravitates back to b. The second term, σ dW, is **randomness**: σ is the volatility of rate shocks, and dW represents a random shock drawn from a normal distribution.

The Vasicek model has two major strengths. First, it is analytically tractable: you can solve the equations to obtain explicit formulas for bond prices and yields. Second, the mean reversion property is realistic: very high interest rates tend to suppress borrowing and inflation, causing central banks to lower rates; very low rates encourage borrowing and inflation, prompting rate hikes. The model captures this self-correcting behavior.

The model has one significant flaw: it permits negative interest rates. In the Vasicek framework, there is no floor preventing r(t) from dropping to −50%, −100%, or lower. Mathematically, this is permissible; economically, it is odd. Savers would not accept negative returns if they could hold currency (at a zero percent return). Before the 2010s, this seemed like a curiosity. After central banks in Europe, Japan, and elsewhere moved to negative policy rates, the criticism lost some force, but the theoretical anomaly persisted.

## The Cox-Ingersoll-Ross model

John Cox, Jonathan Ingersoll, and Stephen Ross addressed the negative-rate problem in 1985 with their now-eponymous model:

dr = a(b − r) dt + σ √r dW

The key difference is the volatility term: σ √r instead of σ. Because volatility depends on the square root of r, when r approaches zero, volatility shrinks to zero. The rate cannot cross zero because volatility vanishes right at zero, creating a floor—a boundary the rate cannot breach. This ensures r(t) ≥ 0 at all times and in all simulations.

The Cox-Ingersoll-Ross (CIR) model also has explicit bond-pricing formulas and is widely used in practice. Its mean reversion feature is intuitive, and the non-negativity constraint is theoretically sound. The trade-off is slightly greater mathematical complexity: the closed-form solutions involve more elaborate special functions than Vasicek, and numerical simulation requires careful discretization to preserve the boundary condition.

## Using short-rate models for bond pricing

The central application is bond valuation. Suppose you own a 5-year bond and want to know its fair value. You could use the [yield-to-maturity](/yield-to-maturity/) method, which discounts future cash flows at a single yield rate. But the short-rate model goes deeper. It simulates thousands of possible paths that the short rate might take over the next five years, following the Vasicek or CIR dynamics. For each path, you calculate what the bond's cash flows will be and discount them using the short rate at each time step. Averaging across all paths gives you the bond's expected present value—a theoretically sound price.

This method reveals something the simple [yield-to-maturity](/yield-to-maturity/) approach misses: the bond price depends not only on yields today but also on the volatility of future rates and the curvature of the discount function. A bond in a high-volatility environment might be priced differently than in a low-volatility environment, even if current yields are identical.

## Measuring interest-rate risk

Short-rate models are invaluable for [risk management](/market-risk/). Suppose a bank holds a portfolio of bonds and wants to know how much it could lose if rates jump up 1% tomorrow. A bank manager would simulate many different rate shocks using the short-rate model and calculate the resulting loss in bond values. This generates a [value-at-risk](/value-at-risk/) (VaR) metric: "There is a 95% probability that we will not lose more than $10 million tomorrow due to rate moves." [Interest rate risk](/interest-rate-risk/) is a major source of losses in the banking system, and short-rate models are the standard tool for quantifying and hedging it.

Risk managers also use short-rate models to compute duration and [convexity](/duration/)—Greeks-like sensitivity measures that show how a bond's price responds to small and large rate changes. These numbers guide hedging decisions: if a bond is highly convex (gaining more when rates fall than it loses when rates rise), the bank may want to sell bonds or swap into a less convex position.

## Extensions and limitations

The Vasicek and CIR models assume that all rates move together in a single factor (the short rate). This "one-factor" assumption is powerful but unrealistic. In practice, the entire [yield curve](/yield-curve/) moves, and sometimes long rates and short rates move in opposite directions (the curve can steepen or flatten independent of changes to the policy rate). Multi-factor models—such as the Hull-White model (which extends Vasicek) or the Longstaff-Schwartz model—allow the short rate and long-term volatility or term premiums to move independently, capturing more complex curve behavior.

Another limit is that both Vasicek and CIR assume a constant mean and volatility. Real data suggest that volatility is stochastic—it changes over time. Stochastic volatility models (like the SABR model) allow σ to follow its own random process, better matching the observed behavior of swaptions and other rate derivatives. However, adding complexity exacts a cost: calibration becomes harder, numerical simulation slower, and intuition more elusive.

## Calibration and practical use

To use a short-rate model, you must first **calibrate** it: estimate the parameters (a, b, σ) that best fit today's market data. Traders typically calibrate to today's [yield curve](/yield-curve/) and the prices of interest-rate derivatives (swaptions, caps, floors). Once calibrated, the model is used to price non-standard bonds, measure hedge ratios, or simulate future rate scenarios for stress testing.

A key insight is that no single short-rate model is universally superior. Vasicek is simpler and faster to compute, making it suitable for quick pricing and large portfolios. CIR is more realistic (no negative rates) but slightly slower. Multi-factor models capture reality better but demand more computational power and data. Practitioners choose based on the intended use and computational constraints.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate](/interest-rate/) — the price of borrowing and the discount rate in bond pricing
- [Yield Curve](/yield-curve/) — the relationship between maturity and interest rate that short-rate models help explain
- [Duration](/duration/) — a measure of bond sensitivity to interest-rate changes, computed from short-rate models
- [Value-at-Risk](/value-at-risk/) — a risk-management metric quantifying potential losses, calculated using short-rate simulations
- [Bond](/bond/) — the fixed-income security whose value depends on interest-rate dynamics
- [Interest Rate Risk](/interest-rate-risk/) — the risk that rising rates reduce bond values, measured using short-rate models

### Wider context

- [Derivatives Pricing](/option/) — options and swaps on rates are priced using short-rate models
- [Monetary Policy](/monetary-policy/) — central banks simulate future rate paths using short-rate model frameworks
- [Term Structure](/yield-curve/) — the full landscape of rates across maturities, driven by short-rate dynamics

</div>

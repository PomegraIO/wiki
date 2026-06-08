---
title: "Nelson-Siegel Model"
description: "A three-factor parsimonious model that fits the entire yield curve using level, slope, and curvature, widely used by central banks and traders to smooth and forecast interest rates."
keywords:
  - Nelson-Siegel model
  - yield curve fitting
  - level slope curvature
  - term structure
  - curve smoothing
image: "/svg/fixed-income.svg"
---

*The **Nelson-Siegel model** is a [yield curve](/yield-curve/) fitting framework that represents the entire term structure of interest rates using just three factors: level (the overall height of the curve), slope (the spread between long and short rates), and curvature (the hump or dip in the middle). Proposed in 1987 and refined since, it is both parsimonious and flexible enough to capture realistic curve shapes, making it a standard tool for central banks, bond traders, and risk managers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Nelson-Siegel Model — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">A three-factor framework for fitting and forecasting the yield curve.</div>

|   |   |
|---|---|
| **What it is** | Parsimonious parametric model of the [yield curve](/yield-curve/) |
| **Factors** | Level (long-term), slope (10-2 spread), curvature (mid-curve hump) |
| **Created** | 1987 by Charles Nelson and Andrew Siegel |
| **Use cases** | Curve smoothing, forecasting, risk decomposition, central bank analysis |
| **Advantage** | Only 4 parameters fit the entire curve; interpretable; stable |
| **Limitation** | Cannot replicate extreme curve shapes or very steep/inverted curves perfectly |

</aside>

## The mathematics and intuition

The Nelson-Siegel model expresses the [yield to maturity](/yield-to-maturity/) at maturity *m* as a function of three latent factors:

y(m) = β₀ + β₁ × exp(−λm) + β₂ × (λm) × exp(−λm)

Where:
- **β₀** is the *level* factor: the asymptotic long-term yield, roughly the 10-year or longer rate.
- **β₁** is the *slope* factor: a short-maturity bias that controls the spread between short and long rates. Negative β₁ produces an upward-sloping curve.
- **β₂** is the *curvature* factor: a hump or depression in the middle of the curve, capturing the non-linearity between short and long.
- **λ** is the *decay rate*, controlling how fast the exponential terms flatten out. It determines where the curve's most extreme curvature sits.

The elegance is that only four parameters—three betas and one lambda—describe the entire [yield curve](/yield-curve/). A typical bond market has 10, 20, or even 50 observable yields (for Treasury, agency, or corporate issuers). Nelson-Siegel collapses that information into a compact, interpretable summary.

## Intuition: level, slope, and curvature

**Level (β₀).** This is the long-end asymptote. If the Fed raises long-term inflation expectations or real-rate expectations, level rises. A parallel upward shift of the curve is an increase in level. Economically, it reflects investors' beliefs about the long-run neutral rate and inflation.

**Slope (β₁).** This controls the tilt. If slope is negative and large in magnitude, the curve is steep: short yields are much lower than long yields, a classic recovery or "risk-on" curve. If slope is small (close to zero) or positive, the curve is flat or inverted, a classic recessionary signal. The slope factor directly encodes the [term premium](/yield-curve/) and growth expectations.

**Curvature (β₂).** This is the "hump" or deviation from a straight line. A positive curvature produces a mid-curve bulge: the 5-year yield is higher than a linear interpolation between the 2-year and 10-year. A negative curvature is a depression: the 5-year sits below the linear fit. Curvature often reflects supply-demand imbalances (e.g., heavy 5-year issuance pushing yields higher) or the market pricing a turning point in monetary policy.

## Why Nelson-Siegel matters

**Central bank standardisation.** The Federal Reserve, European Central Bank, and Bank for International Settlements all publish Nelson-Siegel-fitted curves. It is the lingua franca of institutional yield curve analysis. A central bank can track the evolution of level, slope, and curvature over time, understanding whether the economy is in a "growth" regime (steep curve, high level) or a "recession" regime (flat or inverted, lower level).

**Curve smoothing.** Real observed yields are noisy. Trading activity, issuance calendars, and bid-ask spreads create kinks and anomalies. Nelson-Siegel smooths out that noise, producing a clean curve estimate. Bond traders use it to price illiquid maturities or spot arbitrage opportunities when real yields deviate sharply from the fitted curve.

**Forecasting.** By modelling how level, slope, and curvature evolve over time, researchers can forecast future yield curves. A simple autoregressive model on the three factors is often more stable than direct forecasting of individual maturities. If you believe slope will steepen (recession ending), you can mechanically recompute the full curve.

**Risk decomposition.** A portfolio's [duration](/duration/) and curve positioning can be restated in level, slope, and curvature risk. A long-duration portfolio is exposed mainly to level risk (a parallel shift); a barbell is exposed to slope risk. This decomposition aids in hedging and understanding what moves hurt or help a portfolio.

## Extensions and variants

The original Nelson-Siegel model is simple and robust, but researchers have extended it.

**Dynamic Nelson-Siegel (DNS).** Introduced by Christensen, Diebold, and Rudebusch, DNS models the evolution of level, slope, and curvature through time as a system of equations, capturing persistence and mean-reversion in each factor. This is popular for forecasting and scenario analysis.

**Added factors.** Some researchers add a fourth "ultra-long" factor to better fit 20-year and 30-year yields, or a "term structure of risk premium" to account for time-varying risk prices. The tradeoff is losing parsimony.

**Alternative models.** The [Svensson model](/yield-curve/) adds a second hump factor, allowing two inflection points. Arbitrage-free models (Vasicek, Hull-White) impose no-arbitrage constraints. Spline-based models use piecewise polynomials. Each has merits; Nelson-Siegel remains popular because it is simple and works well in practice.

## Practical use: spotting curve moves

Imagine the Fed signals rate hikes. What happens to the Nelson-Siegel factors?

- **Level often rises:** higher neutral rate expectations.
- **Slope may compress:** if hikes are expected to be aggressive and swift, the short end reprices faster than the long end, creating a [bear flattener](/yield-curve/) or even inversion.
- **Curvature may invert:** front-loading of rate hikes can create a "inverted" curvature, with the 5-year yielding less than the 2-year.

Conversely, in a recession, level typically falls sharply, slope steepens (as the Fed cuts aggressively), and curvature may bulge as long-end yields resist the decline.

A curve trader who understands Nelson-Siegel can quickly decompose an observed curve move, identify which factor is driving returns, and position accordingly. A [bull flattener](/bull-flattener/) is predominantly a slope tightening with a level shift. A [bear steepener](/bear-steepener/) is a slope widening with a level rise.

## Limitations and caveats

Nelson-Siegel is powerful but not perfect.

**Extreme shapes.** In rare markets (e.g., deeply inverted curves or very steep ones), Nelson-Siegel may struggle to fit the data accurately. The exponential decay structure constrains flexibility.

**Structural breaks.** If the policy regime changes sharply (e.g., a shift from fixed exchange rates to floating, or a move to negative rates), the historical parameters may not port forward.

**Forward curve limitations.** Nelson-Siegel fits spot curves well but can produce artificial shapes in [forward rates](/interest-rate/), particularly at very long maturities.

Despite these caveats, it remains the standard for practitioners who need a robust, interpretable summary of the yield curve's state and outlook.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield curve](/yield-curve/) — the term structure the model fits
- [Curve steepening](/curve-steepening/) — widening slope factor
- [Bull flattener](/bull-flattener/) — slope compression with lower level
- [Bear steepener](/bear-steepener/) — slope expansion with higher level
- [Duration](/duration/) — bond price sensitivity the model helps quantify
- [Term premium](/yield-curve/) — the slope factor captures this component

### Wider context

- [Interest rate risk](/interest-rate-risk/) — the model aids risk decomposition
- [Monetary policy](/monetary-policy/) — policy shifts drive factor evolution
- [Inflation](/inflation/) — embedded in the level factor's long-term expectation
- [Bond](/bond/) — the yields being modelled
- [Yield to maturity](/yield-to-maturity/) — what the model estimates

</div>

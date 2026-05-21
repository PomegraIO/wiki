---
title: "Historical Volatility"
description: "Historical volatility measures past price movements as the standard deviation of returns over a lookback period, used to forecast future volatility for option pricing."
keywords:
  - historical volatility
  - realized volatility
  - standard deviation
  - volatility measurement
  - option pricing input
image: "/svg/derivatives.svg"
---

*The **historical volatility (HV)** of an asset is the standard deviation of its past returns over a specific period—typically 20, 60, 120, or 252 trading days. It measures how turbulent the asset's price moves have actually been. Historical volatility is used as a proxy for future volatility when pricing [option](/option)s and is compared to [implied volatility](/implied-volatility) to identify if options are cheap or expensive.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Historical Volatility — key facts</div>

<img src="/svg/derivatives.svg" alt="Past price movements and standard deviation calculation" />

<div class="wiki-infobox-caption">Historical volatility quantifies past price turbulence.</div>

|   |   |
|---|---|
| **Calculation** | Standard deviation of log returns |
| **Time periods** | Typically 20, 60, 120, or 252 days |
| **Annualized** | Multiplied by √252 for annual percentage |
| **Lookback bias** | Period choice affects result significantly |
| **Mean reversion** | HV tends to revert to long-term average |
| **Compared to** | Implied volatility for trading signals |
| **High HV** | Stock has been moving a lot recently |
| **Low HV** | Stock has been calm recently |
| **Forward-looking** | No; HV is backward-looking |
| **Input to pricing** | Used as volatility estimate if IV unavailable |

</aside>

## Calculation and interpretation

Historical volatility is the standard deviation of daily (or periodic) returns. For a stock with returns r₁, r₂, ..., rₙ over n periods:

HV = √(Σ(rᵢ − mean)² / n) × √252

The √252 annualizes the daily volatility to an annual percentage. If a stock's daily return standard deviation is 1%, its annualized HV is roughly 15.8%.

A high HV means the stock's returns have been scattered (large daily swings, high standard deviation). A low HV means returns have been tight (small daily swings, clustered around the mean).

## Lookback period matters

HV depends critically on the lookback period. A stock's 20-day HV might be 10%, but 60-day HV might be 15%, and 252-day HV might be 18%. Shorter periods capture recent turbulence; longer periods smooth it. The choice of period is subjective.

Traders often track multiple HV timeframes (20, 30, 60, 252 days) to identify regime changes.

## HV vs. [implied volatility](/implied-volatility)

**Historical volatility** is what the stock has done (backward-looking, observed).

**[Implied volatility](/implied-volatility)** is what the market thinks it will do (forward-looking, inferred from option prices).

The relationship between HV and IV is central to option trading:

- If IV > HV, options are expensive (market fears more moves than history shows); consider selling.
- If IV < HV, options are cheap (market underestimates turbulence); consider buying.

But this is not a simple buy/sell rule. IV can spike in anticipation of earnings or can be depressed before a calm period. Traders use the HV-IV spread as one signal among many.

## Mean reversion in volatility

Volatility tends to mean-revert over longer timeframes. Periods of high HV are often followed by lower HV, and vice versa. This does not happen immediately, but the pattern is consistent. A stock experiencing 40% HV is likely to see lower HV in the coming months.

## Realized volatility vs. historical

Some quants use **realized volatility**—the volatility that was actually observed—distinct from HV, which is an estimate based on past data. The distinction matters for backtesting strategies.

## In option pricing

When [Black-Scholes model](/black-scholes-model) or other pricing models are run without market option prices (e.g., for bespoke or new options), traders input historical volatility as an estimate of what volatility the option should have. This is a rough proxy; reality is that implied volatility is usually higher (options are expensive) or lower (options are cheap) than simple HV would suggest.

## See also

<div class="wiki-seealso">

### Closely related

- [Implied volatility](/implied-volatility/) — market expectation vs. realized
- [Volatility smile](/volatility-smile/) — IV varies by strike
- Standard deviation — mathematical basis of HV
- [Option premium](/option-premium/) — driven by volatility (HV or IV)

### Greeks and volatility

- [Vega](/vega/) — sensitivity to volatility changes
- [Volatility trading](/volatility-smile/) — exploiting HV-IV differences
- [Mean reversion](/stock-market/) — volatility reverts to long-term average

### Valuation

- [Black-Scholes model](/black-scholes-model/) — uses volatility input
- [Binomial option pricing](/binomial-option-pricing/) — alternative volatility modeling
- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — volatility in simulation

### Deeper context

- [Option](/option/) — volatility is critical to pricing
- [Stock](/stock/) — underlying asset whose volatility is measured
- [Risk management](/hedge-fund/) — volatility is primary risk metric

</div>

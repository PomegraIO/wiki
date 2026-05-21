---
title: "Parameter Risk"
description: "Parameter risk is the exposure to losses when input parameters in a financial model are estimated incorrectly or change unexpectedly, causing the model's output to be wrong."
keywords:
  - parameter risk
  - input risk
  - estimation risk
  - calibration error
  - assumption uncertainty
image: "https://picsum.photos/seed/parameter-risk/900/600"
---

*Parameter risk is the danger that the input parameters estimated for a financial model — volatility, correlation, interest rates, default probabilities — are wrong, incorrect, or unrepresentative, leading to misdecision, mispricing, or losses. It is a subset of [model-risk](/model-risk) focused on the inputs rather than the model structure itself.*

<div class="wiki-hatnote">

This entry covers risks from incorrect parameters in sound models. For risks from the models themselves being wrong, see [model-risk](/model-risk); for risks of unforeseeable extreme events, see [tail-risk](/tail-risk).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Parameter Risk — key facts</div>

<img src="https://picsum.photos/seed/parameter-risk/900/600" alt="A slider adjustment on a control panel showing a parameter being misset" />

<div class="wiki-infobox-caption">Small parameter errors can lead to large output errors.</div>

|   |   |
|---|---|
| **What it is** | Error from wrong parameter estimates in a model |
| **Most common sources** | Historical estimation; quiet market periods; extrapolation errors |
| **Affects** | [Options pricing](/option), [value-at-risk](/value-at-risk), credit models |
| **Example** | Volatility estimate too low; model underprices options |
| **Can be reduced by** | Multiple estimation methods; out-of-sample testing; stress-testing |
| **Severity** | Ranges from minor to catastrophic depending on model sensitivity |

</aside>

## How parameters are estimated (and where errors creep in)

A [value-at-risk](/value-at-risk) model needs three key parameters: the historical return of the portfolio, its volatility (standard deviation), and the correlation between portfolio components. These are all estimated from historical data, and each estimation introduces risk.

**Example of volatility estimation error:**
- You estimate a portfolio's volatility using the past 252 trading days (one year).
- If that year was unusually calm, volatility is low, and your [value-at-risk](/value-at-risk) estimate is low.
- But if you had used five years of data (which includes calmer and more volatile periods), your volatility estimate would be higher.
- Which is right? Neither — both are estimates, both can be wrong.

When markets calm down after a volatile period, estimates tend to be too low. When volatility spikes, estimates lag behind. This is why [value-at-risk](/value-at-risk) models notoriously underestimate risk just before a crash — the parameters were estimated during a calm period.

## Where parameter risk is highest

**Volatility:** Estimated from past price moves, volatility parameters are notoriously unstable. In 2019, US stock volatility was 12%; in March 2020 it spiked to 82%. Models that assumed 12% volatility were catastrophically wrong.

**Correlation:** Two assets are assumed to move together 40% of the time. But during crises, correlations break down. Stocks and bonds are assumed to be uncorrelated; they both crashed in March 2020. A diversified portfolio that should have been stable swung wildly.

**Default probability:** Estimated from credit rating data, default probabilities are biased toward calm periods. In recessions, defaults spike above estimates.

**Interest rates:** Models assume interest rates follow a particular process. But interest rate paths are hard to forecast. Models that worked when the [Federal Reserve](/federal-reserve) was signalling zero rates failed when it suddenly raised rates in 2022.

## Consequences of parameter error

Small parameter errors can lead to large output errors if the model is sensitive:

- A [value-at-risk](/value-at-risk) model that is sensitive to volatility: if true volatility is 20% but estimated at 16%, the model underestimates risk by about 25%. A $1M portfolio could lose more than expected.

- An options pricing model sensitive to volatility: if you estimate volatility at 15% but it is actually 25%, you underprice [options](/option) by a large margin. If you are the seller, you lose money on every option sold.

- A credit model sensitive to default correlation: if defaults are more correlated in downturns than your model assumes, credit losses in a recession are worse than expected.

## Managing parameter risk

Sophisticated approaches include:

- **Multiple estimation methods.** Do not rely on a single historical window or method. Estimate volatility using multiple periods and methods (realized, implied, GARCH). Use the range to bound risk.

- **Sensitivity analysis.** Vary parameters up and down by 10-20% and see how model outputs change. If outputs are highly sensitive, parameter risk is material.

- **Out-of-sample testing.** Estimate parameters on one period of data, and test the model on a different period. If the model fails out-of-sample, parameter risk is high.

- **Implied parameters.** For some parameters, you can extract market expectations. Implied volatility from [option](/option) prices, term structure from [bond](/bond) yields. Use these to cross-check historical estimates.

- **Regime-switching models.** Acknowledge that different market regimes have different parameters. Use regime-switching models that adapt parameters based on current conditions.

- **Conservatism.** Assume parameters are worse than estimated. If estimated volatility is 15%, use 18% for risk management. The extra buffer cushions parameter error.

For individual investors, parameter risk is mostly implicit. When you use a [value-at-risk](/value-at-risk) calculator or a robo-adviser, parameters are already built in. The practical defense is to:

- Understand what parameters the model uses.
- Check whether they seem reasonable for current market conditions.
- Size positions conservatively; do not trust a model completely.
- Monitor actual outcomes versus model predictions; if they diverge, reduce reliance on the model.

## See also

<div class="wiki-seealso">

### Closely related

- [Model-risk](/model-risk) — broader concept; parameter risk is a type
- [Value-at-risk](/value-at-risk) — commonly affected by parameter risk
- [Volatility](/stock-market) — parameter that is hard to estimate accurately
- [Tail-risk](/tail-risk) — parameter models do not capture tail events
- [Stress-testing](/stress-testing) — identifies parameter sensitivity

### Broader context

- [Correlation](/stock-market) — a parameter that breaks down in crises
- [Option](/option) — valuation very sensitive to volatility parameter
- [Credit-risk](/credit-risk) — default probability parameters underestimate recession risk
- [Backtesting](/model-risk) — checks whether parameters hold out-of-sample
- [Risk management](/value-at-risk) — addresses parameter uncertainty

</div>

---
title: "Model Risk"
description: "Model risk is the danger that a financial model is wrong — due to faulty assumptions, incorrect inputs, incomplete data, or misuse — leading to misdecision, mispricing, or catastrophic losses."
keywords:
  - model risk
  - quantitative risk
  - valuation error
  - assumption risk
  - parameter risk
image: "/svg/risk.svg"
---

*Model risk is the exposure to losses stemming from errors in financial models — whether from flawed logic, faulty assumptions, poor data, incorrect calibration, or misapplication of an otherwise sound model. It is a form of [operational-risk](/operational-risk/) and is one of the most insidious risks in finance.*

<div class="wiki-hatnote">

This entry covers risks from models themselves. For risks from incorrect input parameters in otherwise sound models, see [parameter-risk](/parameter-risk/); for the risk of losing from tail events not captured in models, see [tail-risk](/tail-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Model Risk — key facts</div>

<img src="/svg/risk.svg" alt="A complex equation on a screen with a red X through it" />

<div class="wiki-infobox-caption">Models are simplifications; reality often deviates from the simplification.</div>

|   |   |
|---|---|
| **What it is** | Loss from faulty, misapplied, or misunderstood models |
| **Sources** | Bad assumptions, poor data, incomplete logic, wrong use |
| **Most common in** | Derivatives pricing; [value-at-risk](/value-at-risk/); credit scoring |
| **Worst case** | Model is catastrophically wrong; embedded in trading or risk systems |
| **Can be reduced by** | Validation; backtesting; robustness checks; independent review |
| **Cannot be eliminated** | All models are simplifications of reality |
| **Regulatory concern** | Basel capital standards require banks to manage model risk |

</aside>

## Why models are risk

All finance uses models. A [value-at-risk](/value-at-risk/) model estimates portfolio loss at a 99% confidence level over one day. A pricing model values a [derivative](/option/) using assumptions about volatility and rates. A credit scoring model estimates default probability.

Models are simplifications. Reality is complex; models reduce it to tractable equations. This is useful — you cannot plan without simplification — but it is also risky. When reality deviates from the model, losses can be severe.

**Example:** A bank uses a normal distribution to model daily stock returns, calculating [value-at-risk](/value-at-risk/). The model says the 99% confidence daily loss is 2%. But real markets have fat tails: the actual 99% loss is 3%, and the 99.9% loss is 6%. On a 1% day (the 1% tail), the model is wrong, and the portfolio loses 6% while the risk system expected 2%. Traders, risk managers, and executives were all misled by the model.

## Types of model risk

Model risk takes several forms:

- **Logical error.** The model's equations are wrong. A pricing model uses the wrong interest rate or volatility. A risk model neglects to account for a correlation.

- **Assumption error.** The model assumes a parameter is constant when it is actually variable. Assumes independence when variables are correlated. Assumes normality when returns have fat tails.

- **Data error.** The model is trained on bad, incomplete, or biased data. A credit model is trained on data from a period of economic expansion, not recessions, and fails when a recession hits.

- **Calibration error.** The model's parameters are estimated incorrectly. A volatility estimate is too low due to a quiet period in the market; when volatility spikes, the model underprices [options](/option/).

- **Misuse.** The model is sound, but it is used outside its domain. A model calibrated on liquid large-cap stocks is applied to illiquid microcap stocks and is wrong.

- **Overfitting.** The model is fit too closely to historical data and does not generalize to new conditions. It captures noise, not signal.

## Model risk in practice: historical examples

- **Long-Term Capital Management (LTCM), 1998.** Used sophisticated mathematical models to identify mispricings and trade. The models assumed correlations among assets that broke down during the Russian financial crisis. The firm lost 90% of its capital in weeks.

- **Credit rating agencies, 2008.** Models used to rate mortgage-backed securities were based on the assumption that housing prices never fall nationally. When they did, the ratings were catastrophically wrong, and trillions of dollars of securities were mispriced.

- **Facebook's 2018 revenue models.** The company's models predicted continued strong growth. When iOS privacy changes reduced ad targeting ability, revenue models were off, and the stock fell 30%.

## Managing model risk

Regulators and institutions use several tools:

- **Model validation.** Independent teams (separate from those who built the model) review the logic, assumptions, and code.

- **Backtesting.** Apply the model to historical data and check whether its predictions match what actually happened. If the model predicted a 99% daily loss of 2%, did only 1% of daily returns exceed 2% loss?

- **Stress testing.** Apply the model to extreme scenarios to see whether it breaks. If the model assumes normal returns and you feed it a market crash, does it blow up?

- **Robustness checks.** Vary the model's assumptions and parameters slightly and see whether results change dramatically. If small parameter changes cause huge output swings, the model is fragile.

- **Independent review.** Have experts outside the building team critique the model.

- **Documentation.** Write down exactly what the model does, its assumptions, its limitations, and its range of validity.

- **Governance.** Designate a "model risk officer" or committee to oversee all models and their outputs.

For traders and portfolio managers, the practical defense is:

- **Distrust models.** View them as tools, not truth. Check model outputs against intuition and real-world data.
- **Monitor in real time.** Watch whether the model's predictions are matching reality. If not, investigate.
- **Size positions for model risk.** Do not bet the farm on a model; assume it could be wrong.
- **Diversify across models.** Use multiple approaches to estimate prices or risk. If they agree, confidence rises.

## See also

<div class="wiki-seealso">

### Closely related

- [Parameter-risk](/parameter-risk/) — risk from incorrect parameters in an otherwise sound model
- [Operational-risk](/operational-risk/) — model risk is often classified as operational risk
- [Value-at-risk](/value-at-risk/) — common source of model risk in risk management
- [Tail-risk](/tail-risk/) — risk of outcomes models do not capture
- [Stress-testing](/stress-testing/) — method to assess model robustness

### Broader context

- [Derivative](/option/) — pricing models critical to derivatives markets
- [Credit-risk](/credit-risk/) — credit models are major source of model risk
- [LTCM](/hedge-fund/) — famous example of model risk failure
- [2008 financial crisis](/credit-risk/) — model risk in credit ratings contributed
- [Fat-tail-risk](/fat-tail-risk/) — models miss extreme tails, a key model risk

</div>

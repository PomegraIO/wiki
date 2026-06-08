---
title: "Model Risk in VaR Estimation"
description: "Understand model risk in VaR: distributional assumptions, correlation estimates, and calibration errors that cause VaR to underestimate tail losses."
keywords:
  - model risk in var estimation
  - value at risk
  - var model error
  - distributional assumptions
  - tail risk measurement
image: /svg/risk.svg
---

*Every **model risk in VaR estimation** stems from the gap between the model's assumptions and reality. A [value-at-risk](/value-at-risk/) calculation assumes that returns follow a specific distribution, that correlations are stable, that historical data predicts the future, and that the portfolio can be liquidated at quoted prices. Break any of those assumptions — and in stress scenarios they all break — and the VaR estimate becomes dangerously low. The larger the loss you need to forecast, the wider the model error tends to be.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Model Risk in VaR — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">VaR models fail where they matter most: in the tail.</div>

|   |   |
|---|---|
| **Primary sources** | Distributional assumptions, correlation estimates, calibration window, liquidity assumptions |
| **Effect** | Underestimation of tail risk; confidence intervals too tight |
| **Worst case** | Model breaks in sudden regime shifts (crisis, market halt, flight to quality) |
| **Common models** | Parametric (normal distribution), historical simulation, Monte Carlo |
| **Stress-test trigger** | When actual loss exceeds VaR prediction; when correlations spike |
| **Mitigation** | Scenario analysis, backtesting, overlapping calibration windows, regime-aware calibration |

</aside>

## What Model Risk in VaR Is

**Model risk** in [value-at-risk](/value-at-risk/) is the possibility that the model's output underestimates (or overestimates) the true loss distribution. VaR answers the question: "What is the maximum loss I could face with X% confidence over Y days?" The answer depends entirely on the model's assumptions about how asset returns are distributed, how correlated they are, and how representative historical data is of future scenarios. If those assumptions are wrong, VaR is wrong.

There are four primary sources of model error in VaR:

1. **Distributional assumptions** — the shape of the return distribution in the tail
2. **Correlation estimation** — instability of asset-pair correlations, especially in crashes
3. **Calibration window** — whether the historical period used to fit parameters was representative
4. **Liquidity assumptions** — whether the portfolio can be unwound at mid-market prices in stress

Each is a separate layer of uncertainty. A single wrong assumption can produce large errors; multiple wrong assumptions produce catastrophic errors.

## Distributional Assumptions and Tail Risk

Most VaR models assume returns follow a **normal distribution** (the bell curve). Under a normal distribution, extreme returns are rare but predictable: a 5-sigma move (five standard deviations from the mean) happens about once every 1.5 million days. This assumption is convenient because the normal distribution has only two parameters (mean and standard deviation) and is easy to estimate and communicate.

The problem is that financial returns do not follow a normal distribution. They have **fat tails**: extreme events occur far more often than the normal distribution predicts. A 5-sigma move in equities happens roughly every 100–1000 days, not every 1.5 million. In foreign exchange, commodities, and credit, the tail is even fatter. An investor who builds a VaR model on the assumption of normality systematically underestimates the probability of large losses.

The 2008 financial crisis and the 2020 March volatility spike both exemplified this: institutions with normal-distribution-based VaR models were shocked by moves that were statistically "impossible" under their assumptions. Losses exceeded VaR estimates by multiples.

**Parametric VaR** (which assumes a known distribution) is particularly vulnerable to this error. **Historical simulation** (which calculates the empirical distribution of past returns and uses that to forecast future losses) avoids the distributional assumption — but it has a different weakness: it assumes that the distribution of the past will repeat. If the market regime changes (say, a sudden deleveraging or regulatory shock), historical simulation lags reality.

## Correlation Instability

VaR models rely on correlation matrices — estimates of how different assets move together. If you know the correlation between the stock index and the bond index, the correlation between currencies, the correlation between equities and volatility, you can calculate the joint loss distribution and estimate VaR.

The problem: correlations are stable in normal times and unstable in crises. In a market panic, "risk-off" correlations spike. Stocks, commodities, emerging-market currencies, and high-yield bonds all fall together — correlations approaching 1 — even if historical correlations were 0.5 or lower. This is known as **correlation compression** or **contagion**. Bonds, which normally hedge stocks, sometimes rally (flight to quality), sometimes sell off (central bank tightening), creating negative correlation surprises.

A VaR model calibrated on five years of normal-times data estimates correlations of 0.3 to 0.6 between equities and credit spreads. In a liquidity-shock scenario (like March 2020), the true correlation is 0.9. The model's estimate of the loss in a joint downturn is far too optimistic. [Diversification](/diversification/) appears to be a buffer when it is not.

Tail-correlation models and regime-switching approaches attempt to address this, but they introduce complexity and estimation error of their own. A simpler approach is to stress-test correlations explicitly: "What if equity-bond correlation rises to 0.8? What if equity-HY spread correlation is 0.95?" This is scenario analysis, not VaR, but it complements VaR by bounding model error.

## Calibration Window and Regime Shifts

All VaR models must calibrate their parameters (mean, standard deviation, correlations) using historical data. The choice of calibration window — typically one to five years — is arbitrary and consequential.

A model calibrated on the last two years of data captures recent patterns but may miss rare, large moves that happen once per decade. A model calibrated on twenty years of data includes multiple regimes (low-volatility expansion, crisis, recovery) and may over-weight old patterns that are no longer relevant. And because the calibration window is **rolling** (moving forward daily or monthly), the oldest data eventually drops out and the newest data enters. The calculated VaR can shift sharply simply because of the rolling window, with no change in underlying market conditions — a source of noise and model drift.

In a sudden regime shift (the start of a bear market, a central bank pivot, a geopolitical shock), the historical distribution assumed by the model becomes invalid. The market is now in a state that was rarely visited in the calibration window, and the tail estimate is inadequate.

**Overlapping calibration windows** and **dynamic recalibration** can help. Instead of using a fixed two-year window, some quants use multiple overlapping windows and blend the VaR estimates, or recalibrate parameters weekly if volatility spikes. This trades off responsiveness against noise and increases operational overhead.

## Liquidity Assumptions

VaR models typically assume that a portfolio can be liquidated at mid-market prices within the holding period (one day, ten days, etc.). This works fine in normal markets, where bid-ask spreads are tight and order books are liquid.

In a crisis, this assumption fails. When everyone is trying to sell and few buyers exist, actual liquidation prices are far worse than mid-market. A portfolio that VaR said could be liquidated for a 2% loss actually liquidates for a 10% loss. The [bid-ask spread](/bid-ask-spread/) widens, [market depth](/price-discovery/) evaporates, and some positions cannot be sold at any price.

Illiquid assets (corporate bonds, emerging-market debt, real estate, certain derivatives) are most vulnerable to this error. A VaR model of a high-yield bond portfolio assumes the bonds can be sold at Bloomberg-quoted prices within one day. In a credit crisis, actual liquidation takes weeks and happens at 5–20 cents per dollar below mid-market. The VaR estimate is optimistic by orders of magnitude.

Some models apply a **[liquidity adjustment](/liquidity-risk/)** — a multiplier or time extension — to holdings of less-liquid assets. Instead of assuming one-day liquidation, the model assumes three days or a week, and recalculates. This is useful but ad hoc and tends to underestimate liquidity stress precisely when it matters most.

## Stress-Testing and Backtesting VaR Models

Because model error is large, practitioners combine VaR with explicit stress tests. A typical framework:

- **Daily VaR:** Calculate a baseline one-day 95% or 99% value at risk using the standard model. This is the headline number.
- **Scenario stress tests:** Calculate the portfolio loss under 10–20 severe scenarios: a 10% equity crash, a 200 bps credit spread widening, a currency depreciation, a volatility spike, a central bank policy reversal, etc. Include regime-specific scenarios (e.g., a stagflation scenario or a geopolitical shock).
- **Backtesting:** Track daily P&L and compare it to the daily VaR forecast. If the actual loss exceeds the one-day 99% VaR estimate more than about once per 100 days, the model is too optimistic and needs recalibration. If it never is breached, the model may be too conservative.
- **Correlation stress:** Recalculate VaR under elevated correlation assumptions. This bounds the model error from correlation compression.
- **Reverse stress tests:** Identify the market conditions under which the portfolio would experience a catastrophic loss (say, a loss exceeding available capital). Are those conditions plausible? If so, the portfolio's risk appetite is too high.

## Sources of Model Risk Beyond Statistical Assumptions

Model risk is not purely statistical. It also includes:

- **Parameter estimation risk:** The model may use the "right" distributional form but estimate its parameters incorrectly due to data noise or a misaligned calibration window.
- **Model specification risk:** The model may miss important economic relationships. For example, a model that does not account for [carry trade](/carry-trade/) dynamics may misprice currency correlations in a deleveraging scenario.
- **Implementation risk:** The code that implements the model may have bugs, or the data input may be stale or corrupted.
- **Regime-switching risk:** The market may enter a regime (high inflation, financial repression, negative real rates) that is rare in historical data and so is underweighted in the calibrated model.

## Regulatory Perspectives

Regulators (the Federal Reserve, the European Central Bank, the Basel Committee) recognize that model risk is large and require banks to use **multiple VaR approaches**: parametric, historical simulation, and stressed VaR (calibrated on a period including a crisis). Banks must also perform regular backtests, report model exceptions, and increase capital reserves if models are breaching frequently.

Basel III capital rules penalize portfolios with high [stressed](/stress-testing/) [expected shortfall](/expected-shortfall/) relative to normal VaR, acknowledging that tail risks are often underestimated in ordinary times. This regulatory pushback has driven banks to adopt more conservative VaR models and to supplement VaR with extreme value theory and [stress-testing](/stress-testing/) frameworks that explicitly model tail scenarios.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — the foundational risk measure and its core assumptions
- [Expected Shortfall](/expected-shortfall/) — tail-risk measure addressing some VaR limitations
- [Stress Testing](/stress-testing/) — forward-looking scenario analysis complementing VaR
- Correlation — instability and regime-dependence of asset relationships
- Backtesting — validating VaR model accuracy over time

### Wider context

- Risk Measurement — broader landscape of quantitative risk tools
- [Liquidity Risk](/liquidity-risk/) — when portfolios cannot be liquidated at fair value
- [Tail Risk](/tail-risk/) — extreme, rare market events that break normal assumptions
- [Capital Adequacy](/capital-adequacy/) — regulatory use of VaR in capital requirements

</div>

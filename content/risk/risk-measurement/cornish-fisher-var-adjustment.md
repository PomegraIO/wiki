---
title: "Cornish-Fisher VaR Adjustment for Skewness and Kurtosis"
description: "How the Cornish-Fisher expansion corrects Value-at-Risk estimates for non-normal return distributions."
keywords:
  - cornish fisher var adjustment
  - cornish fisher quantile
  - var skewness kurtosis
  - non-normal var adjustment
  - modified var
  - parametric var adjustment
image: "/svg/risk.svg"
---

*The **Cornish-Fisher VaR adjustment** modifies parametric [Value-at-Risk](/value-at-risk/) estimates to account for skewness and excess kurtosis in return distributions. Standard VaR assumes returns are normally distributed; real financial returns are not. Cornish-Fisher stretches the normal quantile based on the actual shape of the data, yielding a more accurate worst-case estimate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cornish-Fisher VaR — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">Cornish-Fisher refines parametric VaR by accounting for non-normal tail behavior observed in real returns.</div>

|   |   |
|---|---|
| **What it adjusts** | Standard parametric VaR, which assumes normality |
| **Uses** | Skewness (3rd moment) and excess kurtosis (4th moment) of return distribution |
| **Result** | Modified quantile that is wider (higher) if left-skewed or fat-tailed |
| **Advantage** | Captures tail risk better than normal assumption for many asset classes |
| **Limitation** | Still assumes a parametric form; extreme events can exceed even adjusted estimates |
| **Common use** | Risk management for equity portfolios, hedge funds, options books |

</aside>

## Why Normal VaR Fails

Standard parametric VaR assumes returns follow a normal distribution. Under this assumption, the 95% confidence one-day Value-at-Risk is:

VaR₉₅ = −(mean return − 1.645 × standard deviation)

For a portfolio with mean return 0.05% and daily volatility 1%, this gives:

VaR₉₅ = −(0.05% − 1.645 × 1%) = −1.60%

This says there is only a 5% chance of losing more than 1.60% in a day.

But real financial returns are not normal. Equity returns exhibit:

- **Negative skewness**: large down moves happen more often than large up moves
- **Excess kurtosis** (fat tails): extreme losses and gains occur more frequently than normal theory predicts

In the 2008 financial crisis, daily equity losses exceeded 10 standard deviations in magnitude—an event with a normal probability of 10^−22. It happened. Normal VaR drastically underestimated tail risk.

## Skewness and Kurtosis

**Skewness** is the third standardized moment of a distribution. It measures asymmetry:

- Skewness = 0: symmetric, like a normal distribution
- Skewness < 0: left-skewed (negative tail is thicker); more downside risk
- Skewness > 0: right-skewed (positive tail is thicker); less downside risk

Many equity indices have skewness around −0.5 to −1.0, meaning downside risk is worse than upside opportunity.

**Excess kurtosis** is the fourth standardized moment minus 3 (the kurtosis of a normal distribution). It measures tail thickness:

- Excess kurtosis = 0: normal distribution
- Excess kurtosis > 0: fat tails; both very large losses and very large gains are more frequent
- Excess kurtosis < 0: thin tails (rare; usually seen only in bounded distributions)

Daily equity returns often have excess kurtosis of 5–10 or higher, meaning tail events are much more common than normality predicts.

## The Cornish-Fisher Expansion

Cornish-Fisher is a statistical technique that modifies a standard normal quantile to account for skewness and kurtosis. The adjusted quantile is:

z_CF = z_N + (z_N² − 1) × S / 6 + (z_N³ − 3z_N) × K / 24 − (2z_N³ − 5z_N) × S² / 36

where:
- z_N is the standard normal quantile (e.g., 1.645 for 95% confidence)
- S is the skewness of returns
- K is the excess kurtosis of returns

The first term (z_N) is the normal VaR. The subsequent terms are adjustments. If returns are negatively skewed, the adjustment pushes the quantile higher (more negative), widening the VaR estimate. If returns have fat tails (excess kurtosis > 0), the adjustment again increases the magnitude of the quantile.

### Worked Example

Suppose a portfolio has:
- Daily mean return: 0.05%
- Daily volatility: 1%
- Skewness: −0.8 (negative skew)
- Excess kurtosis: 4.0 (fat tails)

Normal VaR at 95% confidence:
VaR_normal = −(0.05% − 1.645 × 1%) = −1.60%

Now apply Cornish-Fisher. With z_N = 1.645, S = −0.8, K = 4.0:

z_CF = 1.645 + (1.645² − 1) × (−0.8) / 6 + (1.645³ − 3 × 1.645) × 4.0 / 24 − (2 × 1.645³ − 5 × 1.645) × (−0.8)² / 36

Breaking it down:
- First adjustment (skewness): (2.707 − 1) × (−0.8) / 6 = −0.227
- Second adjustment (kurtosis): (4.448 − 4.935) × 4.0 / 24 = −0.081
- Third adjustment (skewness-squared): −(5.885 − 8.225) × 0.64 / 36 = 0.052

z_CF ≈ 1.645 − 0.227 − 0.081 + 0.052 ≈ 1.389

Cornish-Fisher VaR:
VaR_CF = −(0.05% − 1.389 × 1%) = −1.34%

In this case, the adjusted VaR is *less* severe than the normal VaR. This happens because the negative skewness and fat tails push the adjusted quantile *inward* — the distribution is not as extreme in the direction of our confidence level. (This is counterintuitive; skewness and kurtosis effects can offset.)

But in many equity scenarios, especially during market stress, Cornish-Fisher yields a higher (more conservative) VaR estimate.

## When It Works Well

Cornish-Fisher is most useful for:

- **Equity portfolios and equity indices**: Stock returns exhibit reliable negative skewness and excess kurtosis over long observation periods.
- **Option books**: Option P&L is convex and non-linear, generating fat tails and skewness. Cornish-Fisher captures this better than normal VaR.
- **Intraday risk**: When looking at short time horizons (hours, one day), distributional assumptions matter more because there is less central-limit-theorem averaging.

## Limitations

**Model risk**: Cornish-Fisher is a parametric adjustment. If the true distribution has features (like multimodality or rare mega-events) that skewness and kurtosis do not capture, the adjustment will miss them.

**Historical dependence**: Skewness and kurtosis must be estimated from historical data. If the market regime changes (volatility spike, structural break), historical estimates become obsolete.

**Extreme events**: Cornish-Fisher adjusts the tail based on skewness and kurtosis, but real financial crises often exceed even adjusted estimates. Supplements like historical simulation or [stress testing](/stress-testing/) are needed.

**Negative variance trap**: In rare cases (high negative skewness, high kurtosis), the adjustment can yield an impossible result (e.g., negative variance). Practitioners must constrain or use variants that avoid this.

## Variants and Alternatives

**Higher-order Cornish-Fisher**: Extends the adjustment to include sixth and higher moments, at the cost of more parameter estimation.

**Modified VaR (Meucci)**: A related approach that directly models the quantile of a distribution fitted to observed skewness and kurtosis.

**Historical simulation**: Instead of parametric adjustment, bin empirical returns and compute percentiles directly. This avoids distributional assumptions but requires longer history.

**Extreme Value Theory**: Focuses specifically on the tail, fitting a generalized Pareto distribution to losses beyond a threshold. More robust for tail risk than moment-based adjustments.

## See also

<div class="wiki-seealso">

### Closely related

- [Value-at-Risk](/value-at-risk/) — the parametric VaR framework that Cornish-Fisher refines
- [Historical Volatility](/historical-volatility/) — moment estimation from data
- [Stress Testing](/stress-testing/) — scenario analysis for extreme tail events
- [Tail Risk](/tail-risk/) — the specific risk of rare, large losses
- [Volatility Smile](/volatility-smile/) — how implied volatility varies with strike; related to non-normal distributions

### Wider context

- Risk Measurement — broader field of quantifying financial risk
- [Options](/option/) — derivative whose risk profile is highly non-normal
- [Hedge Fund](/hedge-fund/) — investor type sensitive to tail risk and distribution assumptions
- [Portfolio Theory](/asset-allocation/) — framework within which risk measures are applied
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — how to test robustness of risk assumptions

</div>
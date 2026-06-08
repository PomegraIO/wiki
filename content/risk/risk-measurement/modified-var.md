---
title: "Modified Value at Risk"
description: "Adjusts Value at Risk estimates for non-normal distribution features like skewness and kurtosis using Cornish-Fisher expansion."
keywords:
  - modified value at risk
  - cornish-fisher expansion
  - tail risk
  - distribution skewness
  - excess kurtosis
image: /svg/risk.svg
---

*Modified Value at Risk (MVaR) extends the basic [Value at Risk](/value-at-risk/) framework by accounting for the shape of the return distribution itself—specifically skewness (asymmetry) and kurtosis (tail thickness)—rather than assuming returns follow a normal bell curve. For portfolios where extreme losses cluster in one direction or tail events occur more frequently than normal theory predicts, MVaR typically captures real risk more honestly.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Modified VaR — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">A refinement of parametric VaR that adjusts for real-world distribution shape.</div>

|   |   |
|---|---|
| **What it is** | [Value at Risk](/value-at-risk/) adjusted for skewness and excess kurtosis |
| **Also called** | Cornish-Fisher VaR, modified parametric VaR |
| **Built on** | [Value at Risk](/value-at-risk/), portfolio [volatility](/volatility-smile/), higher moments of return distribution |
| **When useful** | Portfolios with credit exposure, options, or historical tail events not captured by normal assumptions |
| **Limitation** | Requires estimating skewness and kurtosis; backward-looking; assumes higher moments are stable |

</aside>

## Why standard VaR can mismeasure tail risk

Parametric [Value at Risk](/value-at-risk/) assumes returns are normally distributed—a convenient fiction that lets analysts compute VaR from just two numbers: mean return and [volatility](/volatility-smile/). Under that assumption, a 95% confidence VaR at one horizon tells a complete story about downside risk.

But real financial returns are not normal. They exhibit *skewness*—asymmetry in the tails. Equities, especially individual stocks, often show negative skewness: the left tail (losses) is fatter and longer than the right tail (gains). Interest-rate portfolios can show positive skewness. Credit-sensitive portfolios routinely show both negative skewness and excess *kurtosis*—jumbo tail events that occur far more often than a normal distribution would predict.

When a portfolio's left tail is genuinely fatter than normal theory assumes, standard parametric VaR understates true downside risk. When the right tail is unexpectedly long, it overstates downside. Either mismeasurement creates capital decisions on a false foundation.

## The Cornish-Fisher adjustment

Modified VaR corrects for these shape irregularities using the **Cornish-Fisher expansion**, a statistical technique that adjusts the quantile (the cut-off point on the distribution) based on the portfolio's actual skewness and kurtosis.

The logic is straightforward: instead of using the normal distribution's 95% quantile (which assumes skewness = 0 and excess kurtosis = 0), you compute a *corrected* quantile that shifts left if the distribution is negatively skewed (meaning downside tail is fatter) and shifts further left if excess kurtosis is high (meaning both tails are thicker). The result is typically a larger VaR estimate—but one that matches the real shape of historical returns.

Mathematically, the adjustment is:

$$z_{\text{CF}} = z + \frac{1}{6}(z^2 - 1)S + \frac{1}{24}(z^3 - 3z)K - \frac{1}{36}(2z^3 - 5z)S^2$$

where $z$ is the standard normal quantile (e.g., 1.645 for 95% confidence), $S$ is skewness, and $K$ is excess kurtosis. The resulting $z_{\text{CF}}$ then replaces $z$ in the VaR formula. The bigger the skewness and kurtosis, the larger the divergence from standard VaR.

## When MVaR matters most

A buy-and-hold equity portfolio with no options or credit exposure will usually show only modest skewness and kurtosis; MVaR will be close to standard [Value at Risk](/value-at-risk/). The same investor who buys long-dated [call options](/call-option/) to hedge downside, or who holds [high-yield bonds](/high-yield-bond/), or whose portfolio includes [credit spread](/credit-spread/) positions, will typically see significant negative skewness and heavy tails. For those portfolios, MVaR is no longer a fine point—it's the difference between recognising real tail risk and sleepwalking into a loss that statistical theory insisted couldn't happen.

Credit portfolios are the classic case. Default is a jump event: a borrower either pays or doesn't. The loss distribution is bimodal, not smooth and bell-shaped. Standard [Value at Risk](/value-at-risk/) severely understates the probability of simultaneous defaults during a recession, leading to artificially low [Value at Risk](/value-at-risk/) estimates just when tail risk is highest.

## Estimation challenges

MVaR's appeal is also its weakness. To compute the Cornish-Fisher adjustment, you must estimate skewness and excess kurtosis from historical returns. Those estimates are noisy—they require far more history than estimating volatility does, and they tend to flip sign or magnitude as you add or remove a few years of data. A portfolio showing negative skewness over the last ten years might show positive skewness if you look only at the last five. That instability can make MVaR estimates unreliable month to month.

This is why practitioners often blend MVaR with other approaches. A risk manager might compute both standard parametric [Value at Risk](/value-at-risk/) and MVaR, then cross-check both against [historical](/historical-volatility/) and [Monte Carlo](/sensitivity-analysis-valuation/) methods. When all three methods converge, confidence in the VaR estimate rises. When they diverge—especially when MVaR jumps because kurtosis spiked—it's time to dig into why.

## MVaR in practice

Banks and asset managers typically use MVaR for daily or weekly [Value at Risk](/value-at-risk/) reporting on credit-heavy or option-laden books. Insurance companies, which hold portfolios of claims distributions and catastrophe bonds, routinely rely on MVaR because their return distributions are starkly non-normal. Pension funds use it to adjust [Value at Risk](/value-at-risk/) for equity portfolios with derivatives overlays.

The regulatory world has been cautious about MVaR. For years, international banking rules emphasised [historical simulation](/sensitivity-analysis-valuation/) and stressed [Value at Risk](/value-at-risk/) over parametric variants, partly because regulators distrusted distributional assumptions. That said, major banks use MVaR internally for their own [capital-adequacy](/capital-adequacy/) calculations and for client risk reporting.

One crucial caveat: MVaR assumes that today's skewness and kurtosis resemble those you'll observe over the [Value at Risk](/value-at-risk/) horizon. In a crisis, return distributions can shift shape dramatically. A portfolio showing moderate negative skewness in calm times can exhibit much more extreme skewness and kurtosis during a market crash, rendering the historical estimate obsolete. This is why forward-looking [stress-testing](/stress-testing/) and scenario analysis remain indispensable alongside MVaR.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — the foundation; parametric VaR assumes normality, which MVaR corrects
- [Historical Volatility](/historical-volatility/) — the measurement of returns' dispersion from which skewness and kurtosis are estimated
- [Stress-Testing](/stress-testing/) — forward-looking technique that complements MVaR's historical anchoring
- [Tail Risk](/tail-risk/) — the extreme downside losses that MVaR explicitly accounts for
- [Credit Spread](/credit-spread/) — a typical source of portfolio skewness and excess kurtosis

### Wider context

- [Risk Factor Sensitivity](/risk-factor-sensitivity/) — another way to decompose portfolio risk beyond a single headline number
- [Market Risk](/market-risk/) — the broader category of risk that VaR measures
- [Concentration Risk](/concentration-risk/) — portfolios concentrated in skewed exposures need MVaR more urgently

</div>

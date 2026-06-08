---
title: "Sortino Ratio"
description: "A risk-adjusted return metric that penalizes only downside volatility, not upside gains."
keywords:
  - downside deviation
  - risk-adjusted performance
  - downside risk
  - portfolio evaluation
  - excess return
image: "/svg/ratios.svg"
---

*The **Sortino ratio** is the [Sharpe ratio](/sharpe-ratio/)'s more discriminating cousin. It divides excess return not by total [volatility](/historical-volatility/) but only by downside volatility — the standard deviation of returns below a target threshold, usually zero or the [risk-free rate](/interest-rate/). This distinction matters greatly for strategies that pursue asymmetric bets: a portfolio that makes 15% in good months and loses 2% in bad months is riskier than one that makes 5% consistently, yet the Sharpe treats them differently depending on the magnitude of the swings.*

<div class="wiki-hatnote">

For other risk-adjusted measures, see [Sharpe Ratio](/sharpe-ratio/) and [Treynor Ratio](/treynor-ratio/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sortino Ratio — downside-risk focus</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for performance measurement." />

<div class="wiki-infobox-caption">Excess return divided by downside deviation; ignores upside volatility.</div>

|   |   |
|---|---|
| **Formula** | (Return − Target) ÷ Downside Deviation |
| **Inventor** | Frank Sortino (1994) |
| **What it measures** | Return per unit of negative volatility |
| **Scale** | Higher values are better; typically 0.8–3.0 |
| **Advantage over Sharpe** | Treats upside and downside volatility differently |
| **Limitation** | More subjective; requires defining the target return |

</aside>

## The intuition: upside is not risk

The core insight behind the Sortino ratio is that investors do not dislike all [volatility](/historical-volatility/) equally. A stock that doubles in value one month and stays flat the next has caused upside volatility; few investors complain about that. By contrast, a stock that halves in value in one month and recovers slowly has caused downside volatility; that is what keeps investors awake.

The [Sharpe ratio](/sharpe-ratio/) penalizes both equally because it uses the standard deviation of all returns — above and below the mean — in its denominator. A portfolio with returns of +10%, +10%, −8%, and −8% has the same standard deviation as one with returns of +12%, +8%, −6%, and −4%. Yet most investors prefer the second: the downside is shallower.

The Sortino ratio corrects this by using downside deviation, which counts only the variance of returns that fall below a target. If you define the target as zero, then positive returns do not increase the denominator at all; only losses do. This rewards strategies that generate consistent returns or large gains without penalizing them for upside surprises.

## Calculating downside deviation

Downside deviation is computed similarly to standard deviation, but only the negative deviations (below the target) are squared and summed. If the target is zero and a portfolio's monthly returns are +5%, +3%, −2%, and −1%, the downside deviation includes only the −2% and −1% months.

Formally: downside deviation = √[sum of (negative deviation)² ÷ count]. Unlike standard deviation, downside deviation is always smaller than or equal to standard deviation, because upside movements are ignored. Thus, the Sortino ratio is typically higher than the Sharpe ratio for the same portfolio, because you are dividing the same excess return by a smaller denominator.

The choice of target return is important. Most practitioners use zero or the [risk-free rate](/interest-rate/) (the rate you could earn in a Treasury instrument). Some use a minimum acceptable return specific to the investor — a pension fund's liability rate, for instance. The lower the target, the higher the downside deviation and the lower the Sortino ratio.

## When Sortino reveals what Sharpe hides

Suppose two [hedge funds](/hedge-fund/) both generate 12% annual returns over ten years. Fund A has a [volatility](/historical-volatility/) of 8%, producing a [Sharpe ratio](/sharpe-ratio/) of 1.25 (assuming a 2% risk-free rate: 10 ÷ 8). Fund B has the same 8% volatility but achieved its returns through a strategy that had few small losses and occasional spectacular gains. Its downside deviation is 4%. Its Sortino ratio is 1.25 ÷ (4 ÷ 8) = 2.5.

The Sharpe ratios are equal; the Sortino ratios are not. Fund B has asymmetric returns — more upside than downside — which is economically preferable for most investors. The Sortino ratio captures this; the Sharpe does not.

This advantage is especially pronounced for [options](/option/) strategies, [covered calls](/covered-call/), [tail-risk](/tail-risk/) hedges, and other non-linear payoff profiles. A [protective put](/protective-put/) strategy (buying [put options](/put-option/) to limit downside) necessarily incurs upside [volatility](/historical-volatility/) as prices move above the strike — yet it is exactly what risk-averse investors want. The Sortino ratio scores such strategies more fairly than the Sharpe.

## The tradeoff: simplicity versus precision

The [Sharpe ratio](/sharpe-ratio/) is simpler: total return, total volatility, done. Every investor, every asset class, every market situation produces a Sharpe in the same way. This standardization and transparency made it the dominant industry metric.

The Sortino ratio requires choosing a target return. Should it be 0%, the [risk-free rate](/interest-rate/), inflation, or something else? Different choices produce different ratios for the same portfolio. This subjectivity makes Sortino ratios harder to compare across different managers or strategies, especially if they use different targets. A manager reporting a Sortino of 2.0 with a 0% target is not immediately comparable to one reporting 1.6 with a 3% target.

Moreover, computing downside deviation requires higher precision in return data and longer observation periods. The [Sharpe ratio](/sharpe-ratio/) stabilizes on shorter samples; the Sortino needs more months or years of data to yield a reliable estimate. For recently launched funds or strategies, a Sharpe ratio is more credible than a Sortino.

## Downside risk in practice

In reality, investors care about downside risk above all else. Drawdowns, [maximum loss](/value-at-risk/), and [value-at-risk](/value-at-risk/) measures all focus on the left tail of the return distribution — the bad outcomes. The Sortino ratio aligns with that intuition more directly than the Sharpe.

This is why [hedge funds](/hedge-fund/) and [private equity](/private-equity-fund/) firms often emphasize Sortino or downside-focused metrics when marketing to institutional [investors](/stock/). They want to highlight that their strategies manage downside better than a passive [equity](/stock/) portfolio would, even if total [volatility](/historical-volatility/) is high.

For [mutual funds](/mutual-fund/) and [index funds](/index-fund/), the Sortino advantage is smaller. A broad [equity index](/sp-500-index/) fund's returns are roughly symmetrical around the long-term mean (positive skew, but not extreme), so the Sortino and Sharpe ratios move closely together.

## Limitations beyond the formula

Even a perfectly calculated Sortino ratio cannot predict the future. It is a backward-looking statistic, vulnerable to luck and regime change. A strategy that had low downside volatility over ten years may hit unforeseen tail risk in the next crisis. [Backtested](/sensitivity-analysis-valuation/) Sortino ratios, especially those computed on monthly or quarterly data, can be misleading if the true tail risk was masked by the sampling frequency.

Additionally, the Sortino ratio does not directly address [systematic risk](/beta/). A diversified portfolio might have lower downside deviation than an individual [stock](/stock/), yet the stock might be a better addition to a portfolio that is already well [diversified](/diversification/) on [systematic risk](/beta/) terms. For that question, the [Treynor ratio](/treynor-ratio/) is more appropriate.

## See also

<div class="wiki-seealso">

### Closely related

- [Sharpe Ratio](/sharpe-ratio/) — excess return divided by total volatility
- [Treynor Ratio](/treynor-ratio/) — excess return divided by beta
- [Value at Risk](/value-at-risk/) — maximum expected loss at a confidence level
- [Downside Risk](/historical-volatility/) — volatility of negative returns only
- [Beta](/beta/) — systematic risk relative to the market

### Wider context

- [Hedge Fund](/hedge-fund/) — private fund using diverse strategies to manage downside
- [Protective Put](/protective-put/) — buying put options to limit losses
- [Tail Risk](/tail-risk/) — the probability of extreme market moves
- [Portfolio Allocation](/asset-allocation/) — balancing assets to optimize risk and return
- [Risk Management](/credit-risk/) — techniques for controlling portfolio losses

</div>

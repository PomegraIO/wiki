---
title: "Sharpe Ratio"
description: "A measure of risk-adjusted returns that divides excess return by total volatility to assess portfolio efficiency."
keywords:
  - risk-adjusted return
  - volatility metric
  - portfolio performance
  - excess return
  - investment efficiency
image: "/svg/ratios.svg"
---

*The **Sharpe ratio** answers a deceptively simple question: are the returns you are getting worth the risk you are taking? By dividing a portfolio's excess return — the return above a safe [risk-free rate](/interest-rate/) — by its [volatility](/historical-volatility/), this metric strips away the comforting illusion that high returns are always an unqualified win. A volatile strategy that barely beats [Treasury bills](/treasury-bill/) has a worse Sharpe ratio than a steady one, no matter which one generates larger dollar gains.*

<div class="wiki-hatnote">

For other risk-adjusted measures, see [Sortino Ratio](/sortino-ratio/) and [Treynor Ratio](/treynor-ratio/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sharpe Ratio — risk-adjusted performance</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for performance measurement." />

<div class="wiki-infobox-caption">Excess return divided by total volatility; higher is better.</div>

|   |   |
|---|---|
| **Formula** | (Return − Risk-Free Rate) ÷ Standard Deviation |
| **Inventor** | William F. Sharpe (1966) |
| **What it measures** | Return per unit of total risk taken |
| **Scale** | Higher values are better; typically 0.5–2.0 |
| **Strength** | Simple, comparable across portfolios |
| **Weakness** | Treats upside and downside volatility equally |

</aside>

## The math and intuition

The formula is straightforward. If a portfolio returned 10% over a year while the [risk-free rate](/interest-rate/) was 2%, the excess return is 8%. If the portfolio's [standard deviation](/historical-volatility/) (volatility) was 15%, then the Sharpe ratio is 8 ÷ 15 = 0.53.

What does that number mean? It expresses: for every percentage point of [volatility](/historical-volatility/) I endured, I earned 0.53 percentage points of excess return. A portfolio with a Sharpe of 1.2 delivers 1.2 percentage points of excess return per percentage point of risk. The higher the ratio, the more efficiently the portfolio converts risk into reward.

William F. Sharpe introduced the metric in 1966, as part of the broader revolution in quantitative portfolio theory. It became the lingua franca of [hedge fund](/hedge-fund/) and [mutual fund](/mutual-fund/) marketing because it is intuitive, standardized, and enables comparison across wildly different asset types. A [bond](/bond/) fund's Sharpe can be directly compared to a [stock](/stock/) fund's Sharpe, a [currency](/canadian-dollar/) trading strategy's, or a [real estate investment trust](/real-estate-investment-trust/)'s.

## Why the benchmark matters

The choice of [risk-free rate](/interest-rate/) is not trivial. Most practitioners use the yield on a U.S. [Treasury bill](/treasury-bill/) or [Treasury bond](/treasury-bond/) matching the measurement period — 3-month bills for monthly returns, 10-year yields for long-term strategies. The assumption is that you could always park your money in that instrument, so any additional return must compensate for taking additional risk.

In a low-rate environment (such as the early 2020s), risk-free rates hovered near zero. A portfolio returning 8% with 10% volatility had a Sharpe of roughly 0.8. If rates rise to 4%, the same 8% return and 10% volatility portfolio now has a Sharpe of 0.4. Critically, the portfolio's actual returns and volatility did not change — only the benchmark did. This highlights that Sharpe ratios are not absolute judgements; they are relative to the prevailing opportunity cost of capital.

## Comparing portfolios and strategies

The Sharpe ratio shines as a comparative tool. Suppose you are evaluating two [actively managed funds](/actively-managed-fund/) with identical returns but different [volatility](/historical-volatility/). The smoother one has a higher Sharpe and is theoretically superior, because it delivered the same returns with less risk. If a [value fund](/value-fund/) has a Sharpe of 0.7 and a [growth fund](/growth-fund/) has a Sharpe of 1.1, the growth fund is extracting more reward per unit of risk, all else equal.

This comparison works across asset classes. A [bond](/bond/) portfolio's Sharpe can be compared to an [equity](/stock/) portfolio's, or to a [commodity](/crude-oil/) [futures](/futures-contract/) strategy's. Because all are expressed in the same units — excess return per unit of volatility — managers, [hedge funds](/hedge-fund/), and institutional investors use Sharpe ratios as a first-pass screen for performance quality.

## The downside volatility problem

The Sharpe ratio's most famous limitation is that it treats upside and downside [volatility](/historical-volatility/) identically. A portfolio that swings wildly upward and downward around a stable mean has the same [volatility](/historical-volatility/) — and thus the same Sharpe ratio — as one that drops precipitously and recovers slowly. Intuitively, investors prefer upside shocks to downside ones, yet the Sharpe penalizes both equally.

This led researchers to develop alternatives. The [Sortino Ratio](/sortino-ratio/) replaces total volatility with downside deviation, counting only returns below a target (usually zero or the risk-free rate). The [Treynor Ratio](/treynor-ratio/) uses [beta](/beta/) — systematic risk — instead of total volatility, appropriate for [diversified](/diversification/) portfolios where [idiosyncratic risk](/idiosyncratic-risk/) is irrelevant.

For a [hedge fund](/hedge-fund/) or [leveraged strategy](/leverage-ratio-forex/) that makes money from asymmetric bets, the Sortino or Treynor may better capture economic reality than the Sharpe. Still, the Sharpe's ubiquity means it remains the baseline.

## Historical-period and forward-looking pitfalls

The Sharpe ratio is almost always calculated on historical data. You compute past returns and past [volatility](/historical-volatility/) to arrive at a past Sharpe ratio. But what you care about is the future. A strategy with an excellent historical Sharpe may have been lucky, or may have been calibrated to patterns that have already broken.

Many [hedge funds](/hedge-fund/) and systematic strategies report suspiciously high historical Sharpe ratios — 2.0 or higher — often the result of [selection bias](/overconfidence-bias/) (only the profitable strategies get marketed) or [backtesting](/sensitivity-analysis-valuation/) on cherry-picked periods. The [Securities and Exchange Commission](/securities-and-exchange-commission/) and various industry groups have tightened rules around how Sharpe ratios can be advertised precisely because of this problem.

Forward-looking Sharpe estimates — based on expected returns and forecasted [volatility](/historical-volatility/) — are more useful but also more speculative. Few investors forecast either correctly.

## When Sharpe ratios converge and diverge

In [bull markets](/bull-market/), many strategies generate positive Sharpe ratios simply because all returns are rising with [volatility](/historical-volatility/). In [bear markets](/bear-market/), Sharpe ratios can turn negative, indicating that even the returns you did earn did not justify the risk. This is not a flaw in the metric; it is a feature. A strategy that has a negative Sharpe is destroying value relative to a risk-free alternative.

Sharpe ratios also reveal the importance of [diversification](/diversification/). A single highly volatile [stock](/stock/) may have a lower Sharpe than a well-diversified [index fund](/index-fund/), even if the stock's total return is higher, because [diversification](/diversification/) dampens [volatility](/historical-volatility/) without proportionally cutting returns.

## See also

<div class="wiki-seealso">

### Closely related

- [Sortino Ratio](/sortino-ratio/) — excess return per unit of downside volatility only
- [Treynor Ratio](/treynor-ratio/) — excess return divided by beta, for diversified portfolios
- [Beta](/beta/) — measure of systematic risk relative to the market
- [Volatility](/historical-volatility/) — standard deviation of returns over time
- [Risk-Free Rate](/interest-rate/) — the return available from a default-free bond
- [Alpha](/alpha/) — excess return beyond what beta explains

### Wider context

- [Actively Managed Fund](/actively-managed-fund/) — fund manager seeking to beat the benchmark
- [Index Fund](/index-fund/) — fund tracking a market index passively
- [Hedge Fund](/hedge-fund/) — private fund using diverse strategies
- [Portfolio Allocation](/asset-allocation/) — how to divide capital across asset classes
- [Diversification](/diversification/) — reducing risk by holding uncorrelated assets

</div>

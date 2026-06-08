---
title: "Treynor Ratio"
description: "A risk-adjusted return metric that divides excess return by beta to measure systematic-risk efficiency."
keywords:
  - beta risk
  - systematic risk
  - risk-adjusted return
  - portfolio performance
  - market risk
image: "/svg/ratios.svg"
---

*The **Treynor ratio** shifts focus from a portfolio's total [volatility](/historical-volatility/) to its [systematic risk](/beta/) — the risk inherent in the overall market that cannot be diversified away. By dividing excess return by [beta](/beta/), this metric asks: how much market-correlated risk did I have to take to earn this return? For investors holding a [diversified](/diversification/) portfolio, the Treynor ratio often reveals more about efficient risk-taking than the [Sharpe ratio](/sharpe-ratio/) does, because it ignores the [idiosyncratic risk](/idiosyncratic-risk/) that should have been eliminated.*

<div class="wiki-hatnote">

For other risk-adjusted measures, see [Sharpe Ratio](/sharpe-ratio/) and [Sortino Ratio](/sortino-ratio/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Treynor Ratio — systematic-risk focus</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for performance measurement." />

<div class="wiki-infobox-caption">Excess return divided by beta; higher is better.</div>

|   |   |
|---|---|
| **Formula** | (Return − Risk-Free Rate) ÷ Beta |
| **Inventor** | Jack Treynor (1965) |
| **What it measures** | Return per unit of systematic (market) risk |
| **Scale** | Higher values are better; varies by market regime |
| **Best for** | Diversified portfolios; comparing fund managers |
| **Limitation** | Requires accurate beta estimation |

</aside>

## Why beta, not volatility?

The fundamental insight of the Treynor ratio is that for a well-[diversified](/diversification/) investor, [idiosyncratic risk](/idiosyncratic-risk/) — the risk specific to one asset or sector — should not command a [risk premium](/interest-rate/). You can eliminate it by holding many uncorrelated assets. What you cannot eliminate is [systematic risk](/beta/): the tendency of your portfolio to rise and fall with the overall market.

The [Sharpe ratio](/sharpe-ratio/) measures return per unit of total [volatility](/historical-volatility/), which includes both systematic and [idiosyncratic components](/idiosyncratic-risk/). If a manager outperforms through skill, she should do so with proportionally less [systematic risk](/beta/) — earning high returns without taking excess market risk. If she outperforms only by concentrating the portfolio (low [diversification](/diversification/)), she has taken on [idiosyncratic risk](/idiosyncratic-risk/) that a rational investor could have avoided.

The Treynor ratio penalizes high [idiosyncratic risk](/idiosyncratic-risk/) by using [beta](/beta/) in the denominator instead of total [volatility](/historical-volatility/). A manager with a high [Sharpe ratio](/sharpe-ratio/) because she took [idiosyncratic risk](/idiosyncratic-risk/) will have a lower Treynor ratio, revealing that her true market-adjusted efficiency is less impressive.

## Computing beta and the Treynor formula

[Beta](/beta/) measures how much a portfolio's returns move relative to a benchmark — typically the [S&P 500 Index](/sp-500-index/) for U.S. equities. A [beta](/beta/) of 1.0 means the portfolio moves in lockstep with the index. A [beta](/beta/) of 1.2 means it swings 20% more than the market; a [beta](/beta/) of 0.8 means it swings 20% less.

Beta is computed via regression: plotting the portfolio's historical returns against the benchmark's returns, then measuring the slope of the best-fit line. The regression yields [alpha](/alpha/) (the intercept, or excess return not explained by market movement) and beta (the slope).

Once you have beta and excess return, the Treynor ratio is straightforward: divide excess return by beta. If a portfolio returned 15% while the [risk-free rate](/interest-rate/) was 2% and the benchmark returned 10%, excess return is 13%. If [beta](/beta/) is 1.1, the Treynor ratio is 13 ÷ 1.1 ≈ 11.8. The higher the ratio, the more excess return per unit of [systematic risk](/beta/).

## Comparing diversified portfolios

The Treynor ratio excels at comparing [diversified portfolios](/diversification/) or [mutual funds](/mutual-fund/) with similar benchmark [beta](/beta/) exposures. Suppose two [actively managed funds](/actively-managed-fund/) both track the [S&P 500](/sp-500-index/) with a [beta](/beta/) of 1.05, but Fund A returned 12% while Fund B returned 11%. Assuming a 2% risk-free rate, Fund A's Treynor is 10 ÷ 1.05 ≈ 9.5, and Fund B's is 9 ÷ 1.05 ≈ 8.6. Fund A is generating more excess return per unit of [market risk](/market-risk/), making it the better choice for a [diversified](/diversification/) investor.

This comparison is fair because the funds have similar [systematic risk](/beta/) profiles. Both are exposed to the same market movements; the question is pure alpha generation. The fund with the higher Treynor has either better stock-picking, better market timing, or lower costs — all true advantages for a diversified investor.

The Treynor ratio also works across asset classes with some care. A [bond](/bond/) fund's Treynor (measured against a [bond](/bond/) index) can be compared to an [equity fund](/equity-etf/)'s Treynor (measured against an [equity index](/sp-500-index/)), as long as you are comparing within each asset class's own benchmark.

## The beta challenge

Beta is straightforward in theory but messy in practice. Which time period should you use to compute beta? Daily data? Monthly? The choice matters. A stock's [beta](/beta/) over five years may differ substantially from its [beta](/beta/) over the past two years, especially if the company's business has changed or if market relationships have shifted.

Moreover, [beta](/beta/) is unstable for stocks or sectors in transition. A company transitioning from growth to value, or from a cyclical industry to a defensive one, will have different [betas](/beta/) in different periods. When you compute a Treynor ratio using historical [beta](/beta/), you are implicitly assuming that the [beta](/beta/) will persist. If it does not, the metric loses predictive power.

For [diversified portfolios](/diversification/), beta is more stable and thus the Treynor ratio is more reliable. A large [mutual fund](/mutual-fund/) or [index fund](/index-fund/) tracking the market will have a [beta](/beta/) very close to 1.0, with little variation across time periods. For such funds, the Treynor ratio is nearly identical to the [Sharpe ratio](/sharpe-ratio/) (both will increase with alpha), so the distinction is less important.

## Treynor versus Sharpe in practice

For a [mutual fund](/mutual-fund/) with a [beta](/beta/) of 1.1 that is poorly [diversified](/diversification/) and has a [Sharpe ratio](/sharpe-ratio/) of 0.9 but a Treynor of 0.7, the Treynor reveals that much of the return came from [idiosyncratic risk](/idiosyncratic-risk/). An investor holding a broader [diversified](/diversification/) portfolio already captures most of the market's return with less [idiosyncratic risk](/idiosyncratic-risk/), so the fund's true efficiency is lower than its Sharpe suggests.

Conversely, if a [hedge fund](/hedge-fund/) has a [beta](/beta/) of 0.3 and a Treynor of 1.5 and a [Sharpe ratio](/sharpe-ratio/) of 1.2, the Treynor is actually higher — the fund's return per unit of [systematic risk](/beta/) is superior because it filters out the fund's low [idiosyncratic](/idiosyncratic-risk/) [volatility](/historical-volatility/). In this case, the fund is valuable precisely because it takes minimal market risk while generating returns.

This dynamic explains why the Treynor is preferred for comparing [actively managed funds](/actively-managed-fund/). If a manager is truly skilled, she should generate positive [alpha](/alpha/) — excess return beyond what [beta](/beta/) explains — without taking excess [systematic risk](/beta/). A high Treynor means [alpha](/alpha/) is high relative to [beta](/beta/), which is what institutional investors want to see.

## Relationship to the capital asset pricing model

The Treynor ratio is built on the same intellectual foundation as the Capital Asset Pricing Model (CAPM), a cornerstone of modern finance. CAPM posits that expected return = risk-free rate + beta × (market return − risk-free rate). In other words, investors should be compensated for [systematic risk](/beta/) but not for [idiosyncratic risk](/idiosyncratic-risk/).

If you rearrange CAPM, you get the Treynor ratio on the left: (return − risk-free rate) ÷ beta. A manager earning a Treynor ratio equal to the market's risk premium (market return − risk-free rate) is earning exactly what CAPM predicts; a higher Treynor indicates [alpha](/alpha/), or outperformance.

Thus, the Treynor ratio is directly testable against the theoretical benchmark. A fund with a Treynor of 8% when the [market risk premium](/interest-rate/) is 6% has generated alpha. This makes the Treynor especially useful for evaluating [hedge funds](/hedge-fund/), [private equity](/private-equity-fund/), and other alternative investments, where the question of true alpha (skill versus luck) is paramount.

## Limitations and real-world complications

Beta estimates depend on historical data and are backward-looking. A [leveraged](/leveraged-etf/) portfolio with a [beta](/beta/) of 2.0 is theoretically riskier than an unlevered one, but the Treynor does not distinguish between [leverage](/leverage-ratio-forex/) from market movement and [leverage](/leverage-ratio-forex/) from actual borrowing. A [leveraged ETF](/leveraged-etf/) might show a high Treynor ratio because it amplifies market returns, but it is also exposed to [counterparty risk](/counterparty-risk/) and [margin calls](/margin-call-forex/) that the metric ignores.

Additionally, the Treynor assumes that the risk-free rate is truly risk-free and that [diversification](/diversification/) is costless. In reality, even [Treasury bills](/treasury-bill/) carry [inflation risk](/inflation-risk/), and true diversification requires access to global [markets](/stock-market/), which incurs transaction costs and currency risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Sharpe Ratio](/sharpe-ratio/) — excess return divided by total volatility
- [Sortino Ratio](/sortino-ratio/) — excess return divided by downside volatility only
- [Beta](/beta/) — measure of systematic risk relative to a benchmark
- [Alpha](/alpha/) — excess return not explained by beta
- [Capital Asset Pricing Model](/interest-rate/) — framework linking risk and expected return

### Wider context

- [Actively Managed Fund](/actively-managed-fund/) — fund seeking to beat the benchmark
- [Index Fund](/index-fund/) — fund tracking a market index passively
- [Hedge Fund](/hedge-fund/) — private fund evaluated on alpha generation
- [Diversification](/diversification/) — reducing idiosyncratic risk through portfolio breadth
- [Market Risk](/market-risk/) — risk inherent in owning financial assets

</div>

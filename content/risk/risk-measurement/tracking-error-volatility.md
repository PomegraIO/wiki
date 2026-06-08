---
title: "Tracking Error Volatility"
description: "The standard deviation of a portfolio's returns relative to a benchmark, measuring active management drift."
keywords:
  - tracking error
  - active management
  - benchmark variance
  - portfolio performance
  - risk measurement
  - index fund
image: "/svg/risk.svg"
---

*Tracking error volatility measures how much a portfolio's returns deviate from its [benchmark](/wiki/slug/) in statistical terms—the standard deviation of the excess returns. It quantifies the consistency of [active management](/wiki/slug/) or the tightness of an [index fund](/wiki/slug/) replication. A low tracking error suggests the fund closely follows its benchmark; a high one signals either deliberate active bets or poor implementation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tracking Error Volatility — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Active managers trade benchmark precision for the chance to outperform.</div>

|   |   |
|---|---|
| **What it is** | Standard deviation of portfolio excess returns versus the benchmark |
| **Also called** | Tracking error standard deviation, active risk, relative volatility |
| **Typical range** | 0.5% to 5% annually for equity funds |
| **Inverse concept** | [Index fund](/index-fund/) replication (tracking error ≈ 0%) |
| **Uses in analysis** | Information ratio calculation, risk-adjusted performance assessment |
| **Common culprit** | Expense drag, cash drag, position sizing mismatches |

</aside>

## The formula behind the concept

Tracking error volatility is the square root of the average squared difference between portfolio returns and benchmark returns, computed over a rolling window (typically 3 or 5 years). In plain terms: collect monthly or quarterly returns for the portfolio and its benchmark, subtract one from the other to get excess returns, then calculate the standard deviation of those differences.

A [mutual fund](/mutual-fund/) tracking the S&P 500 might deliver 9.8% in a year when the index returns 10.0%—a one-off shortfall of 0.2%. But if this 0.2% annual drag appears consistently every quarter, the standard deviation of quarterly excess returns is low, hence low tracking error. Conversely, a fund might match the index in some periods and lag by 2% in others; that variance is high tracking error.

## Why active managers accept higher tracking error

An [actively managed fund](/actively-managed-fund/) deliberately holds different positions than its benchmark to exploit perceived mispricing. Deviating from the benchmark is the entire strategy. A fund manager might overweight technology stocks, underweight energy, and hold cash—all bets that the index gets wrong. The tracking error, measured ex-post, reflects the magnitude of these bets.

Higher tracking error is not inherently bad; it is the price of the attempt to outperform. The [information ratio](/wiki/slug/)—excess return divided by tracking error—penalizes funds that deviate from the benchmark without producing enough additional return. A fund with 3% tracking error and 2% outperformance has an information ratio of 0.67; one with the same 2% outperformance but only 1% tracking error achieves a ratio of 2.0—same excess return, but at lower "volatility cost."

## Why passive funds still show non-zero tracking error

Even [index funds](/index-fund/) and [ETFs](/etf/) that aim for zero tracking error rarely achieve it. The main culprits:

- **Expense ratios.** Management fees and administrative costs drain return relative to the benchmark, which is typically hypothetical or includes dividends reinvested at no cost.
- **Cash drag.** Holding cash for redemptions or inflows introduces a lag relative to the fully-invested index.
- **Sampling.** Some funds hold a subset of index constituents rather than all of them, introducing small tracking misses.
- **Rebalancing and dividend treatment.** Minor timing differences in rebalancing schedules or dividend reinvestment can accumulate.

A low-cost S&P 500 index ETF might achieve annual tracking error of 0.05%, while an actively managed large-cap fund might run 2–3%.

## Tracking error as a constraint in portfolio construction

Institutional investors often set a maximum acceptable tracking error when hiring a manager. A pension fund might hire an equity manager with a mandate like "outperform the Russell 2000 by 1% per year, with tracking error no more than 2%." This constraint forces the manager to make high-conviction bets without straying too far from the benchmark in terms of statistical risk.

Conversely, a [hedge fund](/hedge-fund/) or concentrated portfolio—where the objective is absolute return, not relative performance—may have no formal tracking error constraint. The fund's risk is measured in [value at risk](/value-at-risk/) or [volatility](/wiki/slug/), not relative to an index.

## The tail risk blind spot

Tracking error, as a standard deviation, can underestimate [tail risk](/tail-risk/). Two funds might have identical annual tracking errors yet behave very differently in extreme market moves. A fund that lags the benchmark by 0.3% in calm years but drops 5% behind in a crash has the same statistical tracking error as one that consistently lags by 1.5%, but the tail risk exposure is larger in the first case. Risk committees increasingly supplement tracking error with [scenario analysis](/sensitivity-analysis-valuation/) and stress testing.

## Tracking error and market efficiency

In an [efficient market](/wiki/slug/), the average [actively managed fund](/actively-managed-fund/) underperforms its benchmark by roughly the expense ratio, with tracking error inversely correlated to skill. High tracking error with negative excess return suggests bad timing or poor security selection. High tracking error with positive excess return suggests genuine alpha generation—or, more cynically, exposure to a risk factor ([factor investing](/factor-investing/)) that has recently outperformed.

The rise of factor-aware indices has complicated interpretation: a fund might have high tracking error to the broad index but low tracking error to a [thematic ETF](/thematic-etf/) or style index that better captures its holdings.

## See also

<div class="wiki-seealso">

### Closely related

- [Information ratio](/wiki/slug/) — excess return divided by tracking error; a scorecard for active manager efficiency
- [Active ETF](/active-etf/) — a fund that reports tracking error to a disclosed benchmark while exercising discretionary bets
- [Index fund](/index-fund/) — the benchmark-hugging alternative; tracks with minimal error by design
- [Volatility](/wiki/slug/) — the broader measure of return fluctuation; tracking error isolates relative drift
- [Value-at-risk](/value-at-risk/) — a complementary risk metric that captures tail loss probability

### Wider context

- [Actively managed fund](/actively-managed-fund/) — a vehicle for active strategies that incur tracking error
- [Expense ratio](/expense-ratio/) — the main drag on passive funds' tracking error
- [Alpha](/alpha/) — the outperformance that managers hope to earn to justify their tracking error
- [Beta](/beta/) — the systematic risk embedded in benchmark exposure

</div>

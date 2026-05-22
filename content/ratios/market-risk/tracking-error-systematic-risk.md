---
title: "Tracking Error vs. Systematic Risk"
description: "Portfolio variance from index versus market beta exposure; two measures of risk with different implications for active management."
keywords:
  - tracking-error
  - active-risk
  - beta
  - systematic-risk
  - active-management
---

*[Tracking Error](/wiki/etf-tracking-error/) and [systematic (market) risk](/wiki/systematic-risk/) are often conflated but measure different dimensions of portfolio risk. Tracking error is the volatility of relative returns (active risk); systematic risk is the sensitivity to market moves (beta). A portfolio can have zero tracking error (perfectly replicates the benchmark) but high systematic risk, or vice versa.*

<aside class="wiki-infobox">

| Item | Detail |
|------|--------|
| **Tracking Error** | Volatility of (Portfolio Return − Benchmark Return) |
| **Systematic Risk (Beta)** | Portfolio return sensitivity to market benchmark |
| **Independence** | Not correlated; can diverge significantly |
| **Active management sign** | High tracking error suggests high active bets |
| **Passive management ideal** | Low tracking error, systematic risk = 1.0 |
| **Unit** | TE in %; Beta as coefficient |

</aside>

## Tracking error: measurement of active deviation

[Tracking error](/wiki/etf-tracking-error/) quantifies how much a portfolio's returns deviate from its benchmark. It is computed as:

**Tracking Error** = Standard deviation of (Portfolio Return − Benchmark Return)

Example: If an actively managed fund benchmarked to the S&P 500 returns 12% in a year while the S&P returns 10%, the excess return is +2%. If this pattern repeats with varying excess returns (sometimes +3%, sometimes +0.5%, sometimes −1%), the standard deviation of these excess returns is the tracking error.

Low tracking error (1–2%) suggests the portfolio closely hugs the benchmark — typical of [index funds](/wiki/index-fund/) or quasi-passive strategies. High tracking error (5–10% or more) suggests large active bets — concentrated holdings, significant overweights/underweights, or different asset allocation.

## Systematic risk: measurement of market sensitivity

[Systematic risk](/wiki/systematic-risk/) or [beta](/wiki/beta/) measures how a portfolio moves with the broad market. It is the slope of the regression of portfolio returns on benchmark returns:

**Portfolio Return** = Alpha + Beta × Benchmark Return

A beta of 1.0 means the portfolio moves in line with the market. A beta of 1.2 means the portfolio is 20% more volatile than the market; a beta of 0.8 means it is 20% less volatile.

Example: If the S&P 500 gains 10%, a portfolio with beta = 1.2 is expected to gain 12%. If the S&P falls 10%, the portfolio is expected to fall 12%.

## Why they diverge: idiosyncratic vs. market risk

Tracking error and beta measure different things:

- **Tracking error** captures idiosyncratic (stock-specific) risk and active bets. A fund that [overweights](/wiki/concentration-risk/) Apple +5% relative to the S&P 500 introduces tracking error but doesn't necessarily change beta if Apple correlates with the overall market.

- **Beta** captures market-wide sensitivity. A fund that holds the same percentage of stocks as the benchmark but with higher-volatility stocks may have the same tracking error as the index but higher beta.

### Scenario: two portfolios, similar tracking error, different beta

**Portfolio A:** Matches the S&P 500 allocation exactly but holds small-cap stocks within each sector (higher volatility). Tracking error is low (replicates index); beta is ~1.3 (more sensitive to market swings).

**Portfolio B:** Underweights financials −5% and overweights tech +5% relative to the S&P 500, but both with large-cap holdings. Tracking error is moderate (active bets); beta is ~0.95 (slightly defensive).

Both have tracking error in the 2–3% range, but Portfolio A's beta is elevated due to small-cap tilt, while Portfolio B's is depressed due to sector bets that happen to dampen market sensitivity.

## Active management and information ratio

[Active managers](/wiki/actively-managed-fund/) aim to generate **alpha** — excess returns above the benchmark. The quality of active bets is captured by the **Information Ratio**:

**Information Ratio** = (Portfolio Return − Benchmark Return) ÷ Tracking Error
or
**Information Ratio** = Alpha ÷ Tracking Error

A manager with 2% alpha and 3% tracking error has an Information Ratio of 0.67. A manager with 3% alpha and 5% tracking error has an IR of 0.60. The higher the IR, the better the manager's skill relative to the risk taken.

Low tracking error with positive alpha is the "active manager's dream" — outsized returns with low deviation. High tracking error with small alpha is the nightmare — volatile underperformance.

## Beta-neutral strategies and portable alpha

Some [hedge funds](/wiki/hedge-fund-market-neutral/) and quantitative managers pursue **beta-neutral strategies**: they create positions with zero beta (or explicit beta hedging) while taking active bets via [market-neutral](/wiki/hedge-fund-market-neutral/) long-short positions. This setup allows them to isolate alpha from beta.

Example: A manager goes **long** $10M of software stocks (beta = 1.3) and **short** $7.7M of the S&P 500 ETF (beta = 1.0). The beta of the combined position is 1.3 × $10M − 1.0 × $7.7M = 0. The manager is "portable alpha" — they've extracted alpha from the stock picks without market sensitivity.

## Passive investing and the tracking error norm

For [passive index funds](/wiki/index-fund/), the goal is to minimize tracking error. A fund tracking the S&P 500 should deliver returns within ±0.05% of the index annually, achieved via:

- Replicating the index exactly (buying all 500 stocks in the correct weight).
- Using [optimization](/wiki/portfolio-mental-accounting/) (holding a subset that statistically replicates the index).
- Accepting the drag of fees, [bid-ask spreads](/wiki/bid-ask-spread/), and [cash drag](/wiki/cash-flow-ratio/) (which reduces tracking error to a predictable negative number equal to fees).

An index fund with 0.05% fees and 0.03% turnover drag will have tracking error of ~0.08% and beta = 1.0.

## Systematic risk in bonds and alternatives

Tracking error and beta concepts extend to bonds and other asset classes:

- **Bond funds:** Tracking error = volatility of relative return vs. benchmark (e.g., Bloomberg Aggregate). Beta is sensitivity to moves in the underlying benchmark (interest-rate and credit risk).

- **Real estate and commodities:** Tracking error quantifies deviation from property indices or commodity benchmarks; beta captures correlation with public market moves.

A [commodity hedge fund](/wiki/hedge-fund-commodity/) might have 0% beta to equities (orthogonal returns) but 5% tracking error against a commodity benchmark due to active sector rotation.

<div class="wiki-seealso">

### Closely related

- [Beta](/wiki/beta/) — market-sensitivity measure
- [ETF Tracking Error](/wiki/etf-tracking-error/) — benchmark deviation in funds
- [Systematic Risk](/wiki/systematic-risk/) — market-wide risk component
- [Information Ratio](/wiki/hedge-fund-market-neutral/) — active manager quality metric

### Wider context

- [Actively Managed Fund](/wiki/actively-managed-fund/) — active bets introduce tracking error
- [Index Fund](/wiki/index-fund/) — minimize tracking error intentionally
- [Market Neutral Strategy](/wiki/hedge-fund-market-neutral/) — beta-neutral active strategies
- [Capital Asset Pricing Model](/wiki/capital-asset-pricing-model/) — theoretical framework linking beta and returns

</div>

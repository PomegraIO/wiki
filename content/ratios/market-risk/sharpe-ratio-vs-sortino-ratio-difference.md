---
title: "Sharpe Ratio vs Sortino Ratio: Key Differences"
description: "Compare Sharpe and Sortino ratios: Sharpe penalizes all volatility, while Sortino focuses on downside risk, essential when returns are skewed."
keywords:
  - sharpe ratio vs sortino ratio difference
  - downside deviation vs standard deviation
  - risk-adjusted return measurement
  - skewed return distribution
  - Sharpe ratio limitations
  - Sortino ratio advantage
image: "/svg/ratios.svg"
---

*The **Sharpe ratio** and **Sortino ratio** both measure risk-adjusted return, but they treat volatility differently. The Sharpe ratio penalizes *all* price swings equally—gains and losses alike. The Sortino ratio counts only downside volatility, ignoring beneficial upswings. When returns are skewed—when positive shocks outweigh negative ones—the Sortino ratio gives a clearer picture of true risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sharpe vs Sortino — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two measures of risk-adjusted return that diverge when return distributions are asymmetric.</div>

|   |   |
|---|---|
| **Sharpe ratio** | Excess return ÷ standard deviation (all volatility) |
| **Sortino ratio** | Excess return ÷ downside deviation (negative volatility only) |
| **Volatility penalty** | Penalizes upside and downside equally |
| **Downside penalty** | Penalizes only negative returns below a threshold |
| **Symmetric distributions** | Both ratios yield similar rankings |
| **Skewed distributions** | Sortino often shows higher ratio (fewer downside surprises) |
| **Use case** | Sharpe: traditional benchmarks; Sortino: hedge funds, tail-risk strategies |

</aside>

## The denominator difference

The **Sharpe ratio** is calculated as:

> (Return − Risk-free rate) ÷ Standard deviation

Standard deviation treats all variance the same: a month of +5% returns and a month of −5% returns both increase the denominator equally, even though an investor usually prefers upside swings.

The **Sortino ratio** replaces standard deviation with *downside deviation*:

> (Return − Risk-free rate) ÷ Downside deviation

Downside deviation counts only returns below a specified threshold (often zero or the risk-free rate). Positive returns don't increase the denominator. A fund that drifts up 30% in half its months and stays flat in the other half has low downside deviation but high standard deviation—and thus a higher Sortino ratio than Sharpe ratio.

## Why the distinction matters in real portfolios

Most investment returns are not symmetrically distributed. Equity funds tend to have occasional large losses (market crashes) paired with frequent modest gains. Options strategies and hedge funds often show return streams with pronounced positive skew: many small losses and a few large wins.

Under the Sharpe ratio, a strategy that captures most of a bull market but misses the worst 10% of down days looks worse than it should—because its volatility spiked during the brief downturns. The Sortino ratio correctly ignores the upside skew and focuses on whether the strategy controls downside losses.

Conversely, a strategy that churns through small losses regularly but offers no alpha will have similar downside deviation to standard deviation, and the two ratios will largely agree.

## A worked comparison

Imagine two funds with identical 10% average annual returns over a five-year period:

**Fund A** (steady, symmetric volatility):
- Returns: +9%, +11%, +10%, +9%, +11%
- Standard deviation: ≈ 0.89%
- Downside deviation: ≈ 0.89% (all months included, no threshold breaches)
- Assuming 2% risk-free rate:
  - Sharpe ratio = (10% − 2%) ÷ 0.89% ≈ 8.99
  - Sortino ratio = (10% − 2%) ÷ 0.89% ≈ 8.99

**Fund B** (skewed, tail-risk hedge):
- Returns: +15%, +15%, +8%, +2%, +10% (higher upside, clustered downside)
- Standard deviation: ≈ 4.68%
- Downside deviation: ≈ 0% (no returns below 2% threshold)
- Assuming 2% risk-free rate:
  - Sharpe ratio = (10% − 2%) ÷ 4.68% ≈ 1.71
  - Sortino ratio = (10% − 2%) ÷ 0% = undefined (or very high)

Fund A's ratios are identical because its volatility is symmetric. Fund B's Sortino ratio skyrockets relative to its Sharpe because downside is minimal, but the Sharpe penalizes the normal month-to-month variance.

An investor seeking true downside protection would prefer Fund B (it never falls below 2% annually), yet the Sharpe ratio would wrongly suggest Fund A is superior on a risk-adjusted basis.

## When to use Sharpe

The Sharpe ratio remains the standard for most institutional [portfolio analysis](/asset-allocation/). It's:

- Simple and widely understood across asset classes.
- Appropriate for [mutual funds](/mutual-fund/) and [index funds](/index-fund/) with symmetric return distributions.
- Easier to compare across many strategies (Sortino can break down if downside deviation is very low).
- Built into most portfolio-optimization platforms and [ETF](/etf/) screeners.

Use Sharpe when evaluating broad equity portfolios, bond portfolios, or balanced allocations.

## When to use Sortino

The Sortino ratio shines for:

- **Hedge funds** and alternative strategies with pronounced skew.
- **Options strategies**, covered calls, or protective put strategies that cap downside.
- **Tail-risk funds** designed specifically to avoid large losses.
- Evaluating managers whose strength is downside protection, not upside capture.
- Comparing strategies where the cost of downside is materially higher than the cost of upside (e.g., when losses trigger [margin calls](/margin-call-forex/) or forced liquidations).

## The threshold question

Both ratios require choosing a threshold below which returns count as "downside." The Sharpe ratio implicitly uses zero (since standard deviation is centered on the mean). For Sortino, common choices are:

- Zero (any negative month or quarter)
- The risk-free rate (any return below what safe bonds earn)
- A minimum acceptable return (e.g., 5%, if the investor will reallocate if returns fall below that)

Different thresholds yield different Sortino ratios, so always check the denominator when comparing published figures.

## A limitation of Sortino

The Sortino ratio can be gamed. A strategy that avoids small losses but blows up once per decade looks amazing on Sortino if the decade is long enough (downside deviation is low), yet it's obviously worse than steady performance. Sortino ignores *tail risk* and extreme loss probability if downside variance is low.

For this reason, sophisticated investors use Sortino *alongside* other metrics like [value at risk](/value-at-risk/) or maximum drawdown to get a fuller picture.

## Sharpe and Sortino in practice

Many analysts report both:
- **Sharpe ratio** as the primary benchmark (for board presentations and broad peer comparison).
- **Sortino ratio** as a secondary lens (to highlight downside control when it's genuinely superior).

A strategy with a Sharpe of 0.8 and a Sortino of 1.2 says: "Yes, volatility is moderate, but most of that volatility is upside—downside is controlled." Conversely, high Sharpe and low Sortino suggests a strategy that swings both ways without particular downside protection.

## See also

<div class="wiki-seealso">

### Closely related

- [Sharpe ratio](/sharpe-ratio/) — risk-adjusted return using standard deviation
- [Sortino ratio](/sortino-ratio/) — risk-adjusted return using downside deviation
- [Beta vs standard deviation](/beta-vs-standard-deviation-risk-measure/) — two ways to measure portfolio risk
- [Value at risk](/value-at-risk/) — probability of extreme loss
- [Standard deviation](/volatility-smile/) — statistical spread of returns
- Skew — asymmetry in return distribution
- Downside deviation — volatility of negative returns only

### Wider context

- Risk-adjusted return — return accounting for volatility
- [Hedge fund](/hedge-fund/) — actively managed alternative strategy
- [Asset allocation](/asset-allocation/) — portfolio construction across asset classes
- Performance evaluation — comparing fund returns
- Portfolio theory — framework for optimizing risk and return

</div>

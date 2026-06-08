---
title: "Risk-Adjusted Return Explained"
description: "How risk-adjusted return metrics like Sharpe and Sortino ratios compare investments with different risk levels on equal footing."
keywords:
  - risk-adjusted return
  - sharpe ratio
  - sortino ratio
  - excess return
  - risk-free rate
image: "/svg/risk.svg"
---

*A **risk-adjusted return** measures investment performance in relation to the amount of risk taken to achieve it—letting you compare portfolios or securities that carry vastly different volatility on equal terms. Without adjusting for risk, a 15% return looks identical whether it came from steady gains or violent swings; risk adjustment reveals which genuinely performed better.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk-Adjusted Return — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Isolates skill from luck by penalizing volatility and drawdowns.</div>

|   |   |
|---|---|
| **Core idea** | Return per unit of risk taken |
| **Sharpe ratio** | (Return − risk-free rate) ÷ volatility |
| **Sortino ratio** | (Return − risk-free rate) ÷ downside volatility |
| **Why it matters** | Two portfolios with 12% returns may have wildly different risk profiles |
| **Typical benchmark** | [Risk-free rate](/interest-rate/) (e.g., Treasury yield) |
| **Time period** | Minimum 3 years preferred; shorter periods can mislead |

</aside>

## Why raw returns mislead

An investment delivering 20% annual returns sounds excellent—until you learn it swung from +60% to −40% in a single year. Another fund returned 12% with movements confined to a ±5% band. Most investors would accept the second trade-off, yet the first shows a higher headline number. Raw return ignores the journey; risk-adjusted return accounts for it.

The intuition is financial: if you can borrow at the [risk-free rate](/interest-rate/) (roughly the yield on a Treasury bond), then beating that rate is the only thing that matters. Any excess above the risk-free rate is your skill or luck—and the more volatility you endure, the harder you worked to earn it. Risk adjustment divides that excess by a measure of volatility, yielding a score that compares different investment paths fairly.

## The Sharpe ratio: volatility matters

The **Sharpe ratio** is the most widely used risk-adjusted return metric. Its formula is straightforward:

> Sharpe ratio = (Portfolio return − Risk-free rate) ÷ Standard deviation of returns

Suppose a stock fund returned 14% annually while the risk-free rate was 4%, and its standard deviation was 18%. The Sharpe ratio would be (14% − 4%) ÷ 18% = 0.56. A competing bond fund with 6% returns, 0% excess above the risk-free rate, and 5% volatility yields 0.40. The stock fund's higher Sharpe ratio—despite greater risk—suggests superior performance relative to the risk borne.

The denominator, standard deviation, captures total volatility: both upside and downside swings from the average return. Higher Sharpe ratios mean the manager delivered more excess return per unit of risk. A Sharpe above 1.0 is respectable; above 2.0 is excellent and rare.

The Sharpe ratio works well when returns are roughly normally distributed—that is, when extreme moves are rare and symmetric. It struggles in markets prone to violent tail events (the 2008 crisis, flash crashes) because it treats big losses the same as big gains when calculating volatility.

## The Sortino ratio: penalizing downside only

The **Sortino ratio** refines Sharpe by replacing standard deviation with **downside deviation**—the volatility of only negative returns. This sidestep the Sharpe's weakness: why penalize an investor for upside surprise?

> Sortino ratio = (Portfolio return − Risk-free rate) ÷ Downside deviation

Consider a fund that gains 20% in half the months and loses 10% in the other half, averaging 5% annually with extreme volatility. The Sharpe ratio suffers because of the upside swings; the Sortino barely flinches, since it ignores positive volatility. For managers who deliberately target occasional large gains (e.g., trend-following traders), Sortino reflects their true risk profile better.

Sortino ratios tend to be higher than Sharpe ratios for the same portfolio, because downside deviation is smaller than total standard deviation. A Sortino above 2.0 is considered strong.

## Information ratio and alpha

Beyond Sharpe and Sortino, other metrics serve specific contexts. The **information ratio** compares a portfolio's excess return (above a [benchmark](/index-fund/)) to the tracking error—how much it strays from the benchmark. An active manager beating the S&P 500 by 2% per year with 3% tracking error has an information ratio of 0.67.

**Alpha**, the return unexplained by [market risk](/market-risk/), is closely related. A manager whose portfolio's volatility would predict a 10% return given market conditions, but delivered 13%, generated 3% alpha. Risk-adjusted return metrics try to isolate alpha from plain [beta](/beta/)—market exposure.

## Pitfalls and context

Risk-adjusted returns are useful, not gospel. A fund with a stellar Sharpe ratio over five years might have been [market-timing](/market-timing/) luck, not skill. Metrics calculated from short histories (under three years) are noisy; they'll swing as new data arrives. Survivorship bias inflates averages: poorly performing funds close, vanishing from the record, leaving only winners visible.

Different time periods yield different rankings. A ratio that favors bonds in a bull market becomes unflattering when rates rise. And no single metric captures every dimension: a portfolio with brilliant Sharpe but severe [tail-risk](/tail-risk/) might blow up if an outlier event strikes.

Use risk-adjusted returns as a screening tool—a reason to look closer—not as a final verdict. Pair them with qualitative review: What's the investment thesis? How has the manager behaved in stress? Are returns repeatable, or a fluke of the period?

## Practical thresholds

In practice, institutional investors often use these benchmarks:

| Metric | Threshold | Interpretation |
|--------|-----------|-----------------|
| Sharpe ratio > 1.0 | Acceptable | Outpaced risk-free rate meaningfully |
| Sharpe ratio > 2.0 | Excellent | Top-quartile manager |
| Sortino ratio > 2.0 | Strong | Downside risk well-managed |
| Information ratio > 0.5 | Competitive | Active manager earning fees |

These are rules of thumb, not law. A hedge fund with a 0.8 Sharpe might still be worth holding if its returns are uncorrelated with your other assets (adding [diversification](/diversification/)).

## See also

<div class="wiki-seealso">

### Closely related

- [Sharpe ratio](/sharpe-ratio/) — the canonical formula and interpretation
- [Beta](/beta/) — systematic risk relative to the market
- [Volatility smile](/volatility-smile/) — why standard deviation can mislead in options markets
- [Value-at-risk](/value-at-risk/) — another risk metric, useful for downside tail events
- [Market risk](/market-risk/) — risk from market-wide movements you cannot diversify away

### Wider context

- [Diversification](/diversification/) — how spreading capital lowers risk without sacrificing return
- [Capital asset pricing model](/capital-asset-pricing-model/) — explains expected return as a function of risk
- Efficient frontier — the theoretical boundary of optimal risk-return trade-offs
- [Hedge fund](/hedge-fund/) — strategies that often target high risk-adjusted returns
- [Behavioral finance](/loss-aversion/) — why investors often mismeasure their own risk tolerance

</div>

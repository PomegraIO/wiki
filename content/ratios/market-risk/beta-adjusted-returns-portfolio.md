---
title: "Beta-Adjusted Returns: How to Compare Unequal-Risk Portfolios"
description: "Beta-adjusted returns normalize portfolio performance for market risk exposure. Learn how to compare high-beta and low-beta portfolios fairly."
keywords:
  - beta adjusted returns
  - portfolio comparison
  - risk-adjusted returns
  - beta normalization
  - market risk exposure
image: /svg/ratios.svg
---

*To compare two portfolios fairly, you must account for the risk each took to earn its return—which is where **beta-adjusted returns** come in. This metric normalizes raw performance by dividing a portfolio's excess return by its [beta](/beta/), revealing whether outperformance came from skill or simply from betting larger on market moves. A high-beta portfolio will naturally outperform in bull markets; beta-adjusted returns separate the market's contribution from the manager's own edge.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Beta-Adjusted Returns — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The key tool for comparing portfolios that took different levels of market risk.</div>

|   |   |
|---|---|
| **Formula** | (Portfolio Return − Risk-Free Rate) ÷ Portfolio Beta |
| **What it measures** | Return earned per unit of market-risk exposure |
| **Common alias** | Jensen's alpha per unit beta; risk-adjusted return |
| **Related concept** | [Sharpe ratio](/sharpe-ratio/) (return per unit of total volatility) |
| **Interpretation** | Higher value = more efficient use of market risk |
| **Typical application** | Comparing mutual funds, hedge funds, or custom portfolios |

</aside>

## The Core Problem: Raw Returns Hide Risk

Imagine two stock portfolios over a five-year period. Portfolio A returned 12% annualized; Portfolio B returned 8%. At first glance, A looks superior. But if A held twice the market risk (beta = 2.0) while B held half the market risk (beta = 0.5), the picture reverses.

When markets rally, high-beta portfolios ride the wave. When markets crash, they crash harder. A manager who constructs a portfolio with beta of 2.0 is essentially borrowing—taking on leverage, whether explicit or through concentration—to amplify market returns. A manager with beta of 0.5 is hedging or holding defensive assets.

The problem: raw returns conflate market exposure with manager skill. To isolate skill—the return earned *per unit of risk taken*—you must normalize the returns by the amount of market risk each portfolio carried.

## Calculating Beta-Adjusted Returns

The standard formula is:

**Beta-Adjusted Return = (Portfolio Return − Risk-Free Rate) ÷ Beta**

Suppose Portfolio A returned 12%, the risk-free rate is 2%, and its beta is 2.0. The beta-adjusted return is (12% − 2%) ÷ 2.0 = 5%.

Portfolio B returned 8%, risk-free rate 2%, beta 0.5. Its beta-adjusted return is (8% − 2%) ÷ 0.5 = 12%.

Now the ranking flips. Portfolio B earned more return per unit of market risk—a higher-quality result, because it achieved outperformance without leverage or concentration.

The numerator (portfolio return minus the risk-free rate) is known as the **excess return**—the return above what you could have earned in bonds. The denominator (beta) scales this excess return by the amount of market exposure. A beta of 1.0 means the portfolio moved in lockstep with the market; a beta of 2.0 means it moved twice as far on average.

## Why Beta-Adjusted Returns Matter

Institutional investors, endowments, and hedge fund allocators use beta-adjusted returns to compare managers fairly. Without normalization, a manager in a bull market will outperform a manager in a bear market regardless of skill. By dividing by beta, you strip away the market's gift or curse and isolate the manager's contribution.

This is particularly critical in hedge fund and [alternative investment](/alternative-trading-system/) spaces, where managers often take asymmetric bets—some target low beta (market-neutral or long-short strategies), while others pursue higher-beta opportunities (long-only growth, emerging markets). A long-short manager with 0.3 beta earning 6% excess return is delivering 20% in beta-adjusted terms, which may outpace a 1.0-beta manager earning 10% excess return (10% in beta-adjusted terms).

For mutual fund comparisons, the metric also exposes closet indexing—managers who charge active fees but hold portfolios nearly identical to the market index (beta ≈ 1.0). A fund with 0.98 beta and 8% annualized return delivered 8% excess return ÷ 0.98 beta ≈ 8.2% in beta-adjusted terms, essentially just capturing the market's risk premium with minimal added value.

## Beta-Adjusted Returns vs. Sharpe Ratio

The [Sharpe ratio](/sharpe-ratio/) is a cousin metric, but it normalizes returns by *total volatility* rather than just market risk. Total volatility includes both systematic risk (beta) and [idiosyncratic risk](/idiosyncratic-risk/)—the unique risks of individual holdings.

A portfolio with high [idiosyncratic risk](/idiosyncratic-risk/) but low beta (e.g., a small number of uncorrelated small-cap stocks) will show a lower Sharpe ratio than its beta-adjusted return would suggest, because Sharpe penalizes all volatility, including diversifiable risk that beta ignores.

Beta-adjusted returns are more useful when comparing portfolios or managers *expected to carry similar idiosyncratic risk*—for instance, two long-short equity funds. Sharpe ratio is more useful when comparing strategies with very different risk structures—an equity fund vs. a credit fund vs. a commodities strategy.

## Real-World Example: High-Beta Growth vs. Low-Beta Value

Suppose a growth-oriented manager runs a concentrated portfolio of technology stocks (beta 1.8) and returns 16% in a strong year. A value investor runs a diversified portfolio of dividend stocks (beta 0.7) and returns 9% the same year. The risk-free rate is 2%.

Growth: (16% − 2%) ÷ 1.8 = 7.8% beta-adjusted.
Value: (9% − 2%) ÷ 0.7 = 10% beta-adjusted.

The value manager earned more return per unit of market risk, despite a much lower headline return. This is a signal of superior stock-picking or portfolio construction skill. The growth manager's outperformance was largely a gift of the market cycle favoring technology and leverage.

Over a five-year period, if market conditions shift and tech underperforms, the growth portfolio may lag significantly while the value portfolio holds up—not because of manager incompetence, but because the growth bet became mispriced by the market. Beta-adjusted returns history would have flagged this ex-ante.

## Limitations and Caveats

Beta-adjusted returns assume that beta is stable. In reality, portfolio beta shifts over time—especially during market dislocations, when correlations shift and leverage unwinds. A portfolio with historical beta of 1.2 might spike to 2.0 in a crash, because the diversification that usually exists evaporates.

The metric also assumes the [capital asset pricing model](/capital-asset-pricing-model/) is correct—that the only priced risk is market risk, and that higher beta simply means higher expected returns. This breaks down in practice. Some low-beta strategies outperform in the long run ([low volatility anomaly](/low-volatility-anomaly/)), while some high-beta bets underperform. Factors beyond market beta (value, momentum, quality, size) also price risk.

Additionally, beta-adjusted returns can hide tail risk. A portfolio with moderate beta but extreme [downside](/tail-risk/) exposure (e.g., a short [volatility](/volatility-smile/) position) will look good in normal times but blow up in rare, violent events. Beta captures average co-movement; it does not capture asymmetric payoffs or [event risk](/operational-risk/).

For long-term investor comparisons, [total return](/return-on-invested-capital/) relative to a benchmark, adjusted for [expense ratio](/expense-ratio/) and turnover costs, often matters as much as raw beta-adjusted excess return.

## When to Use Beta-Adjusted Returns

This metric shines when you need a quick, apples-to-apples comparison of active managers in the same or overlapping asset classes. It is standard in institutional reporting and [fund prospectuses](/fund-prospectus/). It is less useful for comparing strategies across uncorrelated asset classes (equities vs. bonds vs. commodities), where beta itself becomes a crude concept.

For individual investors, beta-adjusted returns are most useful as a sanity check on portfolio performance. If your concentrated stock portfolio earned 15% but the market earned 12% and your portfolio beta is 1.5, your beta-adjusted return is (15% − 2%) ÷ 1.5 = 8.67%, which may be in line with other low-cost equity positions, not exceptional. If instead your return was 20%, you may have genuine alpha—or you may have gotten lucky.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — the systematic market risk that drives beta-adjusted return calculations
- [Sharpe ratio](/sharpe-ratio/) — normalizes returns by total volatility instead of just market risk
- Jensen's alpha — the excess return after adjusting for risk, closely related to beta-adjusted returns
- [Capital asset pricing model](/capital-asset-pricing-model/) — the theory underpinning beta and market-risk premiums
- Excess return — the numerator in beta-adjusted return formulas

### Wider context

- Risk-adjusted returns — the broader category of performance metrics
- [Active management](/actively-managed-fund/) — the practice of outperforming benchmarks; beta-adjusted returns measure its success
- [Market risk](/market-risk/) — the systematic exposure that beta quantifies
- [Idiosyncratic risk](/idiosyncratic-risk/) — unsystematic risk that beta ignores
- Benchmark — the comparison point for evaluating manager performance

</div>

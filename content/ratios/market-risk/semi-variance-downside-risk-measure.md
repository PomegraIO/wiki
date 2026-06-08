---
title: "Semi-Variance as a Downside Risk Measure"
description: "Semi-variance captures downside risk by measuring only negative returns below a target, offering loss-averse investors a more realistic picture than full variance."
keywords:
  - semi-variance downside risk measure
  - downside deviation
  - loss-averse risk metric
  - below-target return volatility
  - variance alternative
image: "/svg/ratios.svg"
---

*A **semi-variance** measures risk using only returns below a target threshold, ignoring positive surprises. Unlike variance, which treats upside and downside equally, semi-variance speaks directly to the question most investors care about: how badly can things go wrong? It is the metric of choice for anyone who cares far more about avoiding losses than capturing gains.*

## Why Standard Variance Misses Half the Story

Traditional variance is calculated as the average squared deviation of all returns from the mean. If your portfolio returned −5%, 10%, −3%, and 8% over four periods, variance treats the downswings (−5%, −3%) and upswings (10%, 8%) as equally bad. Mathematically, they contribute equally to the squared deviations. But in lived experience, a −5% drop feels much worse than a +10% gain feels good.

This asymmetry is called [loss aversion](/loss-aversion/), and it's well-documented in behavioral economics. An investor facing a 50/50 chance of losing $100 or gaining $100 will typically demand odds closer to 60/40 or 65/35 in their favor—because the pain of loss outweighs the pleasure of equivalent gain.

Standard variance can't capture this. If one portfolio has returns of −20%, −10%, +10%, +20% and another has returns of 0%, 0%, 0%, 0%, they have the same variance (150 and 0, respectively—wait, the second has zero, but the point is the same: variance penalizes all dispersion equally). Semi-variance focuses only on the negative tail, making it more aligned with how loss-averse investors actually think about risk.

## How Semi-Variance Is Calculated

Semi-variance begins with a target return—often the mean return, zero, or a minimum acceptable return (MAR) set by the investor.

The formula is:

**Semi-Variance = (1 / n) × Σ (min(R_i − Target, 0))²**

Where:
- **R_i** is the return in period _i_
- **Target** is the threshold (commonly the mean)
- **min(R_i − Target, 0)** returns the shortfall if the return is below target, or zero if it's above
- **n** is the number of periods

**Example:** Suppose annual returns are −8%, 6%, −2%, 12%, and 4%, with a target of 2%.

| Year | Return | Shortfall | Shortfall² |
|------|--------|-----------|-----------|
| 1    | −8%    | −10%      | 0.01      |
| 2    | 6%     | 0         | 0.00      |
| 3    | −2%    | −4%       | 0.0016    |
| 4    | 12%    | 0         | 0.00      |
| 5    | 4%     | 0         | 0.00      |

Sum of shortfalls squared: 0.01 + 0.0016 = 0.0116
Semi-Variance = 0.0116 / 5 = 0.00232
Semi-Deviation (square root) = √0.00232 ≈ 4.82%

Notice that the two positive years and one modestly negative year contribute nothing. Only the −8% and −2% returns enter the calculation. If those same returns appeared in a standard variance calculation, the positive returns would count as negative deviations too, inflating the total risk score.

## Semi-Variance vs. Full Variance: When It Matters

Consider two funds with identical mean returns (7%) and identical full variance (100, or 10% standard deviation):

**Fund A:** −5%, −3%, 10%, 12%, 16% (mean 6%, variance 91)
**Fund B:** 2%, 4%, 7%, 11%, 21% (mean 9%, variance 67)

Wait, those don't have the same variance. Let me revise: imagine two portfolios with the same variance but one has extreme downside:

**Portfolio X:** −20%, 0%, 0%, 20%, 20% (mean 4%, variance 128)
**Portfolio Y:** 4%, 4%, 4%, 4%, 4% (mean 4%, variance 0)

Portfolio X has much higher variance. But if your question is strictly "how much can I lose in a bad year?", Portfolio Y is zero risk. Semi-variance would heavily penalize Portfolio X for the −20% observation.

The practical distinction: use full variance when you care about volatility for its own sake (perhaps if you rebalance frequently and benefit from selling high and buying low). Use semi-variance when you care about shortfall risk—the probability and magnitude of losses you can't afford or didn't expect.

Many [hedge funds](/hedge-fund/) and [value investors](/value-investing/) use semi-variance or its close relative, downside deviation, as the denominator in a modified [Sharpe ratio](/sharpe-ratio/) (called the Sortino ratio), which measures excess return per unit of downside risk rather than total risk.

## Choosing the Target Threshold

The target isn't always the mean. An investor might set it to:

- **Zero:** I only care about years I lose money.
- **The risk-free rate:** I only count returns below Treasury yields as disappointing.
- **A minimum acceptable return (MAR):** I need 5% annually; anything below that is failure.
- **The historical mean:** I care about below-average years.

The choice reshapes the semi-variance. A target of 0% will include fewer negative periods than a target of 5% if most of your returns are positive. A higher target makes semi-variance larger because more periods count as shortfalls.

This flexibility is both a strength and a weakness. It lets you match your actual risk tolerance, but it also requires judgment. Two analysts using the same return series but different targets will reach different conclusions about which investment is riskier.

## Comparing Downside Risk Across Assets

Semi-variance makes direct comparison easier when you have opposing return profiles. Compare a stable dividend stock (consistent 4% returns, zero semi-variance) to a growth stock (−15%, +20%, −5%, +25%, mean +6%, positive semi-variance). The growth stock has higher total variance and higher semi-variance; the dividend stock dominates both metrics. But if the dividend stock returned 2% and the growth stock 6%, a loss-averse investor might use semi-variance to decide: is the extra return worth the downside exposure?

This is precisely what the Sortino ratio answers: **Sortino = (Mean Return − Target) / Semi-Deviation**. If the dividend stock's Sortino is 0.40 and the growth stock's is 0.80, the growth stock delivers more excess return per unit of downside risk, even though it's more volatile overall.

## Limitations of Semi-Variance

Semi-variance isn't perfect. First, it's calculation-heavy compared to standard deviation, though modern tools handle this instantly. Second, it depends entirely on the target you choose—change the target and the risk score changes. Third, it says nothing about tail risk (the probability of catastrophic losses) or correlation; a portfolio of two negatively correlated assets might have low semi-variance but still crater together in a crisis.

Finally, semi-variance doesn't account for the magnitude of the worst case. A portfolio with a single −50% return and two −1% returns might have lower semi-variance than one with five −8% returns, even though the first is arguably riskier for someone who can't stomach a 50% drawdown.

These gaps don't invalidate semi-variance; they just mean it's a tool, not a complete picture. Use it alongside [value at risk](/value-at-risk/) (the maximum likely loss over a time horizon) and [stress testing](/stress-testing/) (how the portfolio behaves in extreme scenarios) for a fuller view.

## See also

<div class="wiki-seealso">

### Closely related

- Variance and Standard Deviation — The foundational risk measure semi-variance refines
- [Sharpe Ratio](/sharpe-ratio/) — Return per unit of total risk
- [Sortino Ratio](/sortino-ratio/) — Return per unit of downside risk
- [Loss Aversion](/loss-aversion/) — The behavioral bias semi-variance addresses
- Downside Deviation — The square root of semi-variance

### Wider context

- [Value at Risk](/value-at-risk/) — Maximum likely loss over a horizon
- Risk Management — Framework for choosing among risk metrics
- [Asset Allocation](/asset-allocation/) — How investors combine assets with different downside profiles
- [Hedge Fund](/hedge-fund/) — Often emphasizes downside protection

</div>
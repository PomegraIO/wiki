---
title: "What Low vs High R-Squared Means for a Portfolio"
description: "Low R-squared means a portfolio's returns are not explained by its benchmark, making beta and alpha statistics unreliable. High R-squared means the benchmark captures the fund's behavior."
keywords:
  - low vs high r-squared portfolio
  - r-squared interpretation
  - beta reliability
  - alpha measurement validity
  - benchmark tracking deviation
  - fund divergence from benchmark
---

*When a portfolio has **low R-squared** versus its benchmark, it means the benchmark explains very little of the fund's actual returns—the fund is doing its own thing. When R-squared is high, the benchmark explains most of the variation, so the fund is essentially a tracked version of the benchmark with some active tweaks. Low R-squared doesn't mean the fund is bad; it often means the benchmark is simply wrong for measuring what the fund does.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">R-Squared: Low vs High — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">R-squared reveals how much of a portfolio's return variation comes from the benchmark; it determines whether other statistics are even valid.</div>

|   |   |
|---|---|
| **R-Squared** | Square of correlation between portfolio and benchmark returns; ranges 0–100% |
| **High R-Squared** | >70%–80%; benchmark explains most variation; beta and alpha are reliable |
| **Low R-Squared** | <30%–40%; benchmark explains little; beta and alpha are misleading |
| **Implication of low R²** | Fund strategy diverges from benchmark; a different benchmark may fit better |
| **Alpha reliability** | Only meaningful when R-squared is high (typically >70%) |
| **Beta reliability** | Only meaningful when R-squared is high (typically >70%) |

</aside>

## What R-squared actually measures

**R-squared** (R²) is the square of the correlation coefficient between the portfolio's returns and the benchmark's returns. It answers: "What percentage of the fund's return variation is explained by moves in the benchmark?"

An R² of 0.85 (85%) means the benchmark accounts for 85% of the fund's up-and-down movements. The other 15% comes from the fund's active decisions—stock picking, market timing, sector tilts, or manager skill.

An R² of 0.20 (20%) means the benchmark explains only 20% of the variation. The fund and benchmark are moving to fundamentally different drummers.

## Why R-squared matters: the beta and alpha problem

**Beta** is supposed to measure a fund's sensitivity to its benchmark. A beta of 1.2 means the fund swings 20% more dramatically than the benchmark—up 12% when the benchmark is up 10%, down 12% when the benchmark is down 10%.

But this relationship only works if the benchmark actually correlates strongly with the fund. When R² is low, the beta figure is nearly useless. Imagine a global macro hedge fund benchmarked against the S&P 500. The fund's returns might be driven by currency moves, commodity prices, and interest-rate expectations—things the S&P 500 doesn't represent. Computing the fund's beta to the S&P 500 becomes a statistical fantasy. The fund's beta to the S&P 500 is a number that means almost nothing.

**Alpha** is the excess return attributable to manager skill—return that can't be explained by benchmark exposure. Alpha = Portfolio Return − (Risk-Free Rate + Beta × Benchmark Excess Return).

When R² is high, alpha is credible. The formula assumes the benchmark captures the fund's systematic exposure; whatever's left over is skill. When R² is low, the alpha figure is garbage. You've estimated a fund's alpha using the wrong benchmark's beta.

## A worked example: the mismatched benchmark

A small-cap growth manager's portfolio returns over five years average 14% annually. Her assigned benchmark is the S&P 500 (large-cap). Here are the stats:

| Metric | Value |
|---|---|
| **Annual volatility** | 18.2% |
| **Correlation with S&P 500** | 0.35 |
| **R-Squared** | 0.122 (12.2%) |
| **Estimated beta** | 0.65 |
| **Risk-free rate** | 2% |
| **Benchmark return** | 11% |

The small-cap fund's R² is only 12%—the S&P 500 explains almost none of her outperformance or underperformance. She might beat the S&P 500 because small-caps surged; she might underperform because small-caps cratered. The benchmark is simply not relevant to her strategy.

Now compute alpha using the formula:
> Alpha = 14% − (2% + 0.65 × (11% − 2%)) = 14% − 7.85% = 6.15%

This looks impressive—6.15 percentage points of pure skill! But it's a mirage. The benchmark doesn't capture her exposure, so beta is wrong, and alpha is unreliable. She might not have 6.15 percentage points of skill; she might just be riding a small-cap tailwind that has nothing to do with market-beating ability.

Switch her benchmark to a small-cap index (say, the Russell 2000). Now her R² jumps to 0.78 (78%). The same manager, same portfolio—but now the benchmark is meaningful, and beta and alpha are worth reading.

## High R-squared: comfort and constraint

A fund with 85% R-squared to its benchmark is reliably tracking a strategy tilted around that benchmark. Think of a [large-cap](/market-capitalization/) value fund that tracks the Russell 1000 Value index but picks 80% of its holdings from the index and adds 20% custom positions.

The high R² tells you:
1. The benchmark captures the fund's core exposure.
2. Beta is credible—if it's 0.95, the fund is slightly less volatile than the benchmark.
3. Alpha figures are meaningful—if the fund shows 1.2% annual alpha, it's genuinely beating its benchmark by that amount, after adjusting for systematic exposure.

The downside: a high R² fund has little room to surprise. You're essentially buying the benchmark plus a small active bet. If you want a manager to take completely different risks, a high R² fund will disappoint.

## Low R-squared: flexibility and ambiguity

A [hedge fund](/hedge-fund/) with 25% R² to the S&P 500 is running a strategy uncorrelated with large-cap equities. It might be trading currency pairs, mining [credit-spread](/credit-spread/) opportunities, or arbitraging commodity futures—entirely different game.

The low R² tells you:
1. The benchmark is irrelevant to this strategy.
2. Beta to the benchmark is misleading.
3. Alpha (relative to that benchmark) is not a meaningful performance metric.

What should the investor do? Find a more appropriate benchmark—or recognize that the fund doesn't fit any traditional benchmark and evaluate it on absolute returns, maximum drawdown, and [Sharpe ratio](/sharpe-ratio/) instead.

## R-squared and portfolio construction

When building a portfolio, R-squared helps reveal overlap and concentration risk. If you own two "diversified" equity funds that both have 92% R² to the S&P 500, you've essentially bought the index twice. If you own a global macro hedge fund (R² of 0.15 to equities, 0.10 to bonds), you've genuinely added diversification.

## When R-squared is mid-range (40–70%)

This is the murky zone. A [sector-rotation](/sector-rotation/) fund targeting technology might have 55% R² to the S&P 500—it moves with the market but pursues a distinct strategy. Beta is somewhat meaningful; alpha is somewhat meaningful; but both are attenuated. The fund's outperformance relative to the S&P 500 may be skill, or may be sector drift. A more granular benchmark (a tech-specific index) would clarify.

## The bigger problem: choosing the right benchmark

Low R-squared usually signals a mismatch between fund strategy and assigned benchmark. Before dismissing a fund as unmeasurable, ask:

- Is this fund actually pursuing a different strategy than its benchmark?
- Is there a better benchmark available?
- Should the fund be evaluated against multiple benchmarks?

A global macro hedge fund shouldn't be benchmarked against the S&P 500. A commodity-trading advisor shouldn't be benchmarked against bonds. Forcing a low R² is often a signal to change the benchmark, not to distrust the fund.

## The bottom line

High R-squared means the benchmark is relevant, and beta and alpha are credible statistics. Low R-squared means the benchmark is wrong, the fund is pursuing a different strategy, and beta and alpha should be ignored or recomputed against a better benchmark. Before accepting any fund's beta or alpha claim, check the R² value. If it's below 50%, the quoted statistics are not reliable. If it's above 75%, they're fair game.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — systematic risk measure, valid only when R-squared is high
- [Alpha](/alpha/) — excess return, only meaningful with high R-squared
- Correlation — the statistical foundation of R-squared
- Benchmark — the critical choice that determines R-squared interpretation
- [Sector Rotation](/sector-rotation/) — a strategy that often has moderate R-squared to broad indices

### Wider context

- [Actively-Managed Fund](/actively-managed-fund/) — where benchmark choice and R² become critical
- [Hedge Fund](/hedge-fund/) — often low-R² strategies evaluated differently
- [Index Fund](/index-fund/) — the 95%+ R-squared portfolio
- Tracking Error — how R-squared relates to active risk

</div>

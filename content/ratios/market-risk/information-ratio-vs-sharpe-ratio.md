---
title: "Information Ratio vs Sharpe Ratio"
description: "Information ratio measures active-management skill relative to tracking error; Sharpe measures overall risk-adjusted returns. Both reward skill but answer different questions."
keywords:
  - information ratio vs sharpe ratio
  - active management skill metrics
  - tracking error vs standard deviation
  - risk-adjusted performance comparison
  - alpha measurement
  - benchmark outperformance
---

*The **information ratio vs Sharpe ratio** distinction separates two views of investment skill: the Sharpe ratio asks "how much return did you earn per unit of total risk," while the information ratio asks "how much extra return did you earn per unit of tracking error relative to your benchmark." The Sharpe ratio is a standalone measure of absolute risk-adjusted performance; the information ratio is the manager's skill score against a chosen baseline.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Information Ratio vs Sharpe Ratio — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Both measure risk-adjusted excess returns, but over different risk metrics and for different purposes.</div>

|   |   |
|---|---|
| **Information Ratio** | Active return ÷ tracking error |
| **Sharpe Ratio** | Excess return ÷ standard deviation |
| **Use case** | Evaluate active manager skill vs benchmark |
| **Benchmark required** | Yes, essential for the denominator |
| **Typical range (annual)** | 0.3–1.0 for skilled active managers |
| **Standard interpretation** | >0.5 suggests meaningful outperformance |

</aside>

## The core formulas

The **Sharpe ratio** divides your excess return (return above a risk-free rate) by your total volatility:

> Sharpe = (Portfolio Return − Risk-Free Rate) ÷ Standard Deviation

The **information ratio** divides your active return (return above the benchmark) by your active risk:

> Information Ratio = (Portfolio Return − Benchmark Return) ÷ Tracking Error

Tracking error is the standard deviation of the difference between your returns and the benchmark's returns over time. It captures how much your portfolio actually deviates from the benchmark path—not the portfolio's total volatility, but only the volatility of *outperformance or underperformance*.

## Why tracking error matters

A large active manager running a $50 billion fund that holds 85% of the S&P 500 and selects 15% in individual stocks will have a very low tracking error—perhaps 2–3% annually. The same stock-picking alpha might appear in a small hedge fund that holds a completely different set of positions, with tracking error of 15–20% if it never benchmarks itself at all.

The information ratio reveals the second manager has the same skill, while the Sharpe ratio alone would penalize her for running a volatile portfolio. Neither manager is wrong; they're optimizing for different mandates. The information ratio isolates the quality of the active bets.

## When each metric makes sense

Use the **Sharpe ratio** when comparing investments on a standalone basis: a mutual fund against another mutual fund, a hedge fund against Treasury bonds, your personal portfolio against a diversified index. The Sharpe ratio tells you the absolute bang-for-buck—how much excess return you earned per unit of risk you took on.

Use the **information ratio** when you want to assess active management skill against a specific benchmark. If you hire a manager to beat the S&P 500, the information ratio tells you whether her alpha is real or just luck. A Sharpe ratio of 0.8 might sound great, but if the benchmark had a Sharpe of 0.85, you're not getting your money's worth.

## The relationship between the two

The two ratios are connected: a manager's Sharpe ratio depends on her benchmark's Sharpe ratio plus her information ratio (scaled by her active risk). In formula form:

> Sharpe (Manager) = Sharpe (Benchmark) + Information Ratio × (Tracking Error ÷ Benchmark Std Dev)

This relationship shows why a mediocre manager tracking a strong benchmark can still report a decent Sharpe ratio—the benchmark is doing the heavy lifting. The information ratio strips away that disguise.

## Information ratio in practice

An active equity fund that beats its benchmark by 1.2% per year with a tracking error of 2.5% has an information ratio of 0.48. That's respectable but not exceptional. A [value-fund](/value-fund/) manager consistently beating her [benchmark](/price-to-earnings-ratio/) by 0.8% with only 1.6% tracking error achieves an information ratio of 0.5, demonstrating tighter, more repeatable skill.

By contrast, a [leveraged-etf](/leveraged-etf/) with a Sharpe of 1.2 might sound better than a 0.5 information ratio suggests—until you remember the leveraged fund is taking on 3x the volatility of an unleveraged equivalent. The information ratio reveals whether the manager is actually better or just more aggressive.

## When information ratio breaks down

The information ratio assumes the benchmark is appropriate and remains stable over time. If a manager drifts from her mandate or the market regime changes, the information ratio can mislead. A growth-stock fund versus a value benchmark will show false negative alpha. Also, information ratios computed over short windows (one or two years) are volatile and unreliable; three years minimum is standard.

The metric also assumes tracking error is a fair penalty for active risk. In reality, some portfolio differences from the benchmark are intentional bets (which the manager should be rewarded for), while others are implementation noise. The information ratio doesn't distinguish.

## Comparing funds: a worked example

Two [mutual funds](/mutual-fund/) both targeted at beating the Russell 2000 small-cap index:

| Fund | Annual Return | Benchmark Return | Tracking Error | Information Ratio |
|------|---|---|---|---|
| **Small-Cap Alpha** | 12.5% | 10.2% | 3.1% | 0.74 |
| **Small-Cap Value Pick** | 11.8% | 10.2% | 4.8% | 0.33 |

The first fund beat the benchmark by 2.3 percentage points with tight tracking error—high-quality active management. The second beat by only 1.6 percentage points but took on 50% more tracking error—lower quality skill, suggesting luck or excessive portfolio risk.

Now check the Sharpe ratios assuming a 2% risk-free rate:

| Fund | Total Std Dev | Sharpe Ratio |
|------|---|---|
| **Small-Cap Alpha** | 18.2% | 0.58 |
| **Small-Cap Value Pick** | 20.1% | 0.49 |

The first fund is also better on an absolute basis, but the Sharpe ratio understates the gap. The information ratio better reveals the manager's actual skill.

## The bottom line

The information ratio and Sharpe ratio answer different questions. If you care whether a fund manager is beat the market, use the information ratio. If you care whether a portfolio is giving you the best return per unit of volatility on a stand-alone basis, use the Sharpe ratio. Many investors use both: the Sharpe ratio to decide whether to hold an investment at all, and the information ratio to decide if it's time to fire an [actively-managed-fund](/actively-managed-fund/).

## See also

<div class="wiki-seealso">

### Closely related

- [Sharpe Ratio](/sharpe-ratio/) — the foundational risk-adjusted return measure
- Tracking Error — volatility of returns relative to a benchmark
- [Beta](/beta/) — systematic risk exposure relative to a benchmark
- [Alpha](/alpha/) — excess return not explained by benchmark exposure
- [Actively-Managed Fund](/actively-managed-fund/) — funds employing managers whose information ratios matter

### Wider context

- Risk-Adjusted Returns — the philosophy behind adjusting returns for risk
- [Index Fund](/index-fund/) — the benchmark alternative to active management
- [Hedge Fund](/hedge-fund/) — where information ratios are often calculated differently
- [Performance Fee](/performance-fee/) — compensation structures tied to information ratios and alpha

</div>

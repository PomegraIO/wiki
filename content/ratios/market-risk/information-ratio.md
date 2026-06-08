---
title: "Information Ratio"
description: "A risk-adjusted measure of how consistently a portfolio manager generates excess returns relative to a benchmark."
keywords:
  - information ratio
  - active return
  - active risk
  - alpha
  - tracking error
  - performance measurement
image: "/svg/ratios.svg"
---

*The **information ratio** measures a manager's skill at generating returns above a benchmark, adjusted for the consistency of that outperformance. It divides the annualized excess return by the annualized tracking error, telling investors whether a manager is beating the benchmark through luck or genuine alpha.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Information Ratio — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">A measure of manager skill relative to volatility of performance divergence from a benchmark.</div>

|   |   |
|---|---|
| **What it is** | Active return divided by tracking error, measuring consistency of excess performance |
| **Also called** | Appraisal ratio (synonym in some contexts) |
| **Numerator** | Annualized excess return (portfolio return minus benchmark return) |
| **Denominator** | Annualized tracking error (standard deviation of excess returns) |
| **Higher is better** | Yes—a higher ratio indicates better risk-adjusted alpha generation |
| **Common benchmark** | S&P 500, MSCI World, fund-specific index |
| **Typical range** | 0.2–1.0 for skilled active managers; negatives suggest persistent underperformance |

</aside>

## Why active return alone misleads

A [mutual fund](/mutual-fund/) that beats its benchmark by 2% annually looks impressive until you learn it swung 8% wild relative to that benchmark each month. A different fund that beats by only 1% but deviates by barely 1% from its index has won through sharper stock-picking, not luck or leverage. The information ratio strips away the noise by penalizing inconsistent outperformance and rewarding steady alpha.

This is the tension at the heart of active management: delivering excess returns is the entire job, but doing so erratically is worse than doing it steadily. A fund that randomly outperforms then underperforms by larger margins may deliver acceptable long-term surplus, but investors will lose faith and redeem shares during the downswings—and transaction costs will harm the bottom line.

## The calculation in practice

The formula is straightforward:

**Information Ratio = (Portfolio Return − Benchmark Return) / Tracking Error**

Suppose a technology-focused fund returned 14% over five years, while the Nasdaq-100 returned 11%. The excess return is 3 percentage points. If the fund's quarterly returns relative to the index had a standard deviation of 1.2%, annualized that becomes roughly 2.4% tracking error. The information ratio is 3 ÷ 2.4 = 1.25.

By contrast, a large-cap value fund that returned 8.5% versus an 8% benchmark has 0.5 points of excess return, but if its deviations are tighter at 0.8% annualized tracking error, the information ratio is 0.5 ÷ 0.8 = 0.625. The value fund's alpha is weaker, but it may still be worth holding if the technology fund later stumbles.

The ratio is typically annualized using roughly 36–60 months of data, giving a genuine picture of whether outperformance is systematic or cyclical.

## What counts as good

An information ratio above 0.5 is respectable; above 0.75 is strong; above 1.0 is excellent. But context matters. A fixed-income fund tracking a bond index might have an information ratio of 0.3 simply because bonds move less than stocks, leaving less room for active bets to diverge without triggering high tracking error. An [equity-etf](/equity-etf/) tracking the S&P 500 might have a ratio near zero by design—it's supposed to hug the index.

Negative ratios are red flags. A manager with −0.3 or worse is not just underperforming but doing so inconsistently, which suggests either bad luck, bad timing, or skill deficit that investors should avoid. Persistent negative ratios across multiple years are a sign to exit.

## Information ratio versus other metrics

The information ratio differs from the [Sharpe ratio](/sharpe-ratio/), which measures excess return above the risk-free rate divided by total volatility. A Sharpe ratio of 1.0 could come from a fund that steadily outperforms or one that swings wildly. The information ratio peels away that ambiguity by focusing on benchmark-relative performance.

It also complements [alpha](/alpha/), which tells you the magnitude of outperformance, and [beta](/beta/), which tells you correlation to the market. A high-beta fund might deliver impressive absolute returns but weak alpha and a mediocre information ratio. A low-beta fund might generate solid alpha but struggle in bull markets.

For [hedge funds](/hedge-fund/) and other alternative strategies, the information ratio is often more relevant than Sharpe because these funds explicitly aim to beat a benchmark, not merely to achieve a target return above the risk-free rate.

## Practical limits and caveats

Information ratios are backward-looking. A manager with a stellar 1.2 ratio over the past three years may lose their edge as markets shift, rivals copy their bets, or the markets reward a different style. Overweighting this metric in fund selection can lead to performance-chasing—buying what worked, right before it stops.

Short measurement windows (one to two years) are noisy and unreliable. The ratio improves with longer histories, but even five years is modest given the influence of market cycles. A manager might have one stellar cycle and one mediocre one, averaging to a deceptive middle score.

Survivor bias distorts the historical record: funds with poor information ratios shut down, vanishing from databases, which artificially inflates the average ratio of remaining competitors.

## Information ratio in portfolio construction

Institutional investors use information ratios to allocate capital across multiple managers. If Manager A has an information ratio of 0.8 and Manager B has 0.5, and both are hired, an investor might allocate 60% to A and 40% to B. The higher-ratio manager gets bigger capital because the probability of sustained outperformance is better.

Similarly, a fund family comparing the information ratios of various strategies—value, growth, momentum, convertibles—can identify which teams have genuine edge and should receive more internal resources or outside capital.

## See also

<div class="wiki-seealso">

### Closely related

- Tracking Error — the denominator of the information ratio; standard deviation of excess returns
- [Alpha](/alpha/) — the numerator expressed as absolute return; magnitude of outperformance
- [Beta](/beta/) — market sensitivity; helps interpret whether outperformance is earned or inherited
- [Sharpe Ratio](/sharpe-ratio/) — risk-adjusted return relative to the risk-free rate, not a benchmark
- Active Management — the broader strategy that information ratios evaluate
- [Maximum Drawdown](/maximum-drawdown/) — alternative risk measure emphasizing worst-case loss
- [Calmar Ratio](/calmar-ratio/) — risk-adjusted return using maximum drawdown instead of tracking error

### Wider context

- [Mutual Fund](/mutual-fund/) — vehicles where information ratios are most commonly cited
- [Hedge Fund](/hedge-fund/) — alternative vehicles relying heavily on information ratio analysis
- Portfolio Construction — how ratios influence capital allocation
- Performance Attribution — deeper analysis of sources of outperformance

</div>

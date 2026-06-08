---
title: "Sterling Ratio"
description: "A risk-adjusted return metric that divides annualized return by the average annual maximum drawdown, extending the Calmar concept to multi-year fund evaluation."
keywords:
  - sterling ratio
  - risk-adjusted return
  - drawdown measurement
  - fund evaluation
  - return per unit of loss
image: "/svg/ratios.svg"
---

*The **Sterling Ratio** answers a practical question for fund investors: How much annual return does a manager generate for every percentage point of average annual drawdown suffered? It pairs return with the pain of losses, year after year, revealing whether outperformance compensates for the underwater stretches investors endure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sterling Ratio — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for risk metrics." />

<div class="wiki-infobox-caption">Annualized return divided by average annual drawdown—a multi-year frame.</div>

|   |   |
|---|---|
| **What it is** | Annualized [return](/return-on-equity/) divided by average annual [maximum drawdown](/maximum-drawdown/). |
| **Formula** | Sterling Ratio = Annualized Return / Avg Annual Max Drawdown (%) |
| **Range** | Often –5 to +10; higher is better. Negative when cumulative return is negative. |
| **Also called** | Sterling ratio (lowercase in journals). |
| **Key advantage** | Uses annual worst-case rather than peak-to-trough; adapts to longer timescales. |
| **Related to** | [Calmar Ratio](/calmar-ratio/), which normalises return by *total* drawdown. |

</aside>

## Why annualized drawdown matters for long-term funds

The [Calmar Ratio](/calmar-ratio/) divides return by the single deepest drawdown in the entire history. Over a decade, that one crash—a financial crisis, a sector implosion—sets the denominator. The Sterling Ratio instead asks: each year, what's the average worst month-to-peak drop? Then what return does the manager deliver per unit of that recurring pain?

This reframes the question from "What's the absolute worst you'll see?" to "What's the typical worst you'll see annually?" For a fund running over 20 years, that's often far more relevant. Markets suffer drawdowns every few years. An investor needs to know what returns come with that rhythm, not just the all-time nadir.

## Calculating: a three-year example

Suppose a fund posts these annual performances:

**Year 1:** +18% return, maximum drawdown –8%.
**Year 2:** +5% return, maximum drawdown –12%.
**Year 3:** +12% return, maximum drawdown –6%.

Average annual maximum drawdown = (8 + 12 + 6) / 3 = 8.67%.

Annualized return (geometric) ≈ (1.18 × 1.05 × 1.12)^(1/3) – 1 ≈ 11.6%.

Sterling Ratio = 11.6% / 8.67% ≈ 1.34.

This fund returns 1.34% for every 1% of average annual drawdown. A competitor with 9% annualized return and 6% average annual drawdown would score 1.5—better discipline, higher payout per unit of pain.

## Strengths: the multi-year lens

Unlike [volatility](/volatility-smile/) (which treats all ups and downs as bad), Sterling directly penalises losses and rewards staying relatively flat during boom years. A fund with low volatility but steady 12% returns can score higher on Sterling than a highly volatile fund with the same return—because Sterling ignores the benign days, focusing on the maximum damage each year.

Equally, Sterling values *consistency of pain*. A fund that drawdowns –15% every year (average 15) looks worse than one that drawdowns –20% once every ten years, because Sterling uses the average. That's sometimes sensible (if you're reinvesting annual distributions) and sometimes not (if one catastrophic year scares you out of the fund for life).

## When Sterling misleads

A fund with two catastrophic years and one stellar recovery can hide true risk in its average. Suppose: Year 1 –40%, Year 2 +80%, Year 3 +20%. Annualized return is roughly +18% (geometric); average drawdown is 40%. Sterling Ratio = 0.45. That's terrible—yet the raw return is good. The problem: most investors balk at 40% annual drawdowns, regardless of recovery. Sterling doesn't capture tail risk or the *distribution* of drawdowns; it only averages them.

Conversely, a fund with tiny, frequent drawdowns (–2%, –3%, –2% each year) has low average drawdown and high Sterling, but investors rarely sleep through multiple small cuts to their capital. The metric treats a 40% crash and eight 5% hiccups the same if the average lands at 5%—which ignores psychometric reality.

## Comparing to Calmar and other risk ratios

The [Calmar Ratio](/calmar-ratio/) uses the fund's largest *single* drawdown. Over short periods (3–5 years), Calmar and Sterling often rank funds similarly. Over decades, Calmar becomes hostage to one bad year (e.g., the 2008 financial crisis), while Sterling treats it as one data point among many.

The Sharpe Ratio divides return by standard deviation; it ignores drawdown shape and cares only about aggregate volatility. A bumpy but positive fund can beat a smooth bear market on Sharpe, yet investors prefer the smooth experience. Sterling bridges that gap, measuring actual downside episodes.

## Practical thresholds

A Sterling Ratio above 2.0 is strong—1% of return per 0.5% of average annual pain. Between 1.0 and 2.0 is decent; the fund pays off, but with meaningful drawdown drag. Below 1.0, the fund is struggling: annual losses are nearly as large as annual gains. Negative Sterling signals funds that are underwater on average or have experienced multi-year decline.

In practice, a [hedge fund](/hedge-fund/) or [actively managed fund](/actively-managed-fund/) with Sterling above 2.5 is competing seriously with passive alternatives; below 1.5, it's hard to justify the fees and complexity.

## See also

<div class="wiki-seealso">

### Closely related

- [Calmar Ratio](/calmar-ratio/) — return divided by maximum drawdown; simpler but less suited to long-term comparison.
- [Maximum Drawdown](/maximum-drawdown/) — the single worst peak-to-trough loss; Sterling uses the average annual version.
- Sharpe Ratio — return per unit of volatility; treats all fluctuations, not just downside.
- [Sortino Ratio](/sortino-ratio/) — return per unit of downside volatility; closer to Sterling's spirit.
- [Ulcer Index](/ulcer-index/) — weights both depth and duration of drawdowns into one score.
- [Return on Equity](/return-on-equity/) — how annualized return is calculated for the numerator.

### Wider context

- Risk-Adjusted Return — the family of metrics normalising performance by risk.
- [Actively Managed Fund](/actively-managed-fund/) — where Sterling is often used to justify active fees.
- [Hedge Fund](/hedge-fund/) — traditional home of drawdown-centric metrics like Sterling.
- [Fund Prospectus](/fund-prospectus/) — disclosure of historical returns and drawdowns.

</div>

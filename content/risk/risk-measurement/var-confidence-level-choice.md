---
title: "Choosing a Confidence Level for Value at Risk"
description: "Why the choice between 95% and 99% VaR matters for capital requirements, tail coverage, and the loss scenarios each confidence level captures."
keywords:
  - var confidence level 95 vs 99
  - value at risk confidence level choice
  - var 95 percent vs 99 percent
  - var capital adequacy threshold
image: "/svg/risk.svg"
---

*The **confidence level** of a Value at Risk (VaR) calculation determines how extreme a loss scenario the measure is designed to capture. A 95% [value at risk](/value-at-risk/) (VaR) describes the maximum expected loss over a holding period with 95% confidence; a 99% VaR is more conservative, capturing a more severe tail loss. The choice between 95% and 99% is not academic—it directly drives capital requirements, buffer sizes, and whether the firm is prepared for truly exceptional market events.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VaR Confidence Level Comparison</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Higher confidence = larger buffer for tail risk.</div>

|   |   |
|---|---|
| **95% VaR interpretation** | 1 in 20 chance of exceeding this loss in one holding period |
| **99% VaR interpretation** | 1 in 100 chance of exceeding this loss in one holding period |
| **Typical use case (95%)** | Day-to-day risk monitoring, hedge fund position limits |
| **Typical use case (99%)** | Bank capital adequacy, regulatory minimums |
| **Loss magnitude (99% vs 95%)** | 99% VaR is typically 1.3x to 1.5x larger than 95% VaR |
| **Missed event frequency (95%)** | ~5 days per year (in a 250-day trading year) |
| **Missed event frequency (99%)** | ~1–2 days per year (in a 250-day trading year) |
| **Regulatory baseline** | Basel III mandates use of 99% VaR for capital calculations |

</aside>

## Interpreting the Confidence Level

A 95% VaR of $1 million over a one-day holding period means: "There is a 95% probability that losses will not exceed $1 million tomorrow." Equivalently, there is a 5% probability that losses will exceed $1 million—a "1 in 20" event.

A 99% VaR of $1.4 million over the same period means: "There is a 99% probability that losses will not exceed $1.4 million tomorrow." There is a 1% probability that losses exceed $1.4 million—a "1 in 100" event.

The difference is in the tail of the loss distribution. Both measures are estimates of potential loss, but 99% VaR reaches further into the left tail (the extreme loss scenarios) than 95% VaR does. When you increase the confidence level, you are asking: what is the loss threshold that captures an even more rare, more severe scenario?

## Why the Confidence Level Matters: Capital and Buffers

The choice of confidence level directly determines capital requirements and risk buffers. 

Under **Basel III**, the international banking standard, banks must hold capital equal to at least their 99% VaR (plus other adjustments) over a 10-day holding period. This regulatory standard ensures that banks can absorb losses up to a more extreme threshold before depleting reserves. The use of 99%, not 95%, reflects the regulatory philosophy that banks are critical infrastructure; they must be prepared for scenario that is rarer and more severe than a typical bad day.

A bank with a 99% 10-day VaR of $100 million must hold at least $100 million in equity capital (plus other capital tiers) to meet the standard. If the bank were instead to use a 95% VaR of, say, $60 million, its capital requirement would be $60 million—a material reduction. But that capital buffer would be inadequate during a 1 in 20 loss event, risking insolvency.

For hedge funds and trading desks, 95% VaR is more common for day-to-day position limits and intra-day risk monitoring. A desk manager might issue a mandate: "No single position may have a 95% 1-day VaR greater than $10 million." This allows traders flexibility for typical market days while policing excessive tail exposure. The assumption is that traders monitor these limits continuously and can react if limits are breached; the 5% tail is acceptable risk for operational agility.

## The Loss Magnitude Gap: Why 99% VaR Is Larger

The gap between 95% and 99% VaR is non-linear. Assuming a normal distribution of returns, the ratio is roughly 1.3x to 1.4x. But real financial returns have "fat tails"—extreme events occur more frequently than a normal distribution predicts—so the actual ratio can be larger, sometimes 1.5x or higher.

**Worked example.** A portfolio has historical daily returns with mean 0% and standard deviation 1.5%. Using a normal distribution:
- 95% VaR (1.645 standard deviations): 1.645 × 1.5% = 2.47% loss
- 99% VaR (2.326 standard deviations): 2.326 × 1.5% = 3.49% loss

Ratio: 3.49% / 2.47% = 1.41x

For a $100 million portfolio:
- 95% VaR = $2.47 million
- 99% VaR = $3.49 million

The additional $1.02 million in buffer (from 95% to 99%) may seem small in percentage terms, but it reflects the cost of preparing for a loss scenario that is 5 times rarer. Over many positions and a large institution, these buffers compound.

## Impact on Capital Adequacy and Crisis Resilience

The choice between 95% and 99% is a fundamental trade-off between operational flexibility and crisis resilience.

**95% confidence** is pragmatic for daily operations. It acknowledges that markets are often volatile, losses are frequent, and capital cannot be infinite. A firm using 95% VaR for position limits allows traders to deploy more capital per position and capitalize on opportunities, knowing that roughly 5% of days (about 12 days per year in a 250-day trading year) will exceed the VaR threshold. The firm must have mechanisms to react (margin calls, position reductions) when these exceedances occur.

**99% confidence** is conservative. It assumes the firm wants to be prepared for a loss scenario that is so rare it may only occur a handful of times per decade. The cost is tied-up capital and reduced return on equity, but the benefit is that ordinary market stress is absorbed without drama. If a 1 in 100 day occurs, the firm can survive it.

For a bank with $1 trillion in assets, the difference between 95% and 99% VaR capital requirements can amount to tens of billions of dollars. That is why regulators mandate 99%: they want banks to survive even uncommon crises without triggering taxpayer bailouts. For a prop trading desk with $100 million under management, the difference might be $5–10 million in tied-up capital, a meaningful constraint but not existential.

## The Problem of the "Tail Beyond VaR"

A critical limitation of VaR, regardless of confidence level, is that it says nothing about losses *beyond* the VaR threshold. A 99% VaR of $100 million tells you losses will likely not exceed $100 million, but it does not tell you whether a loss beyond $100 million could be $101 million or $500 million.

This "tail risk" beyond VaR became painfully relevant in the 2008 financial crisis and the 2020 COVID-19 crash. Firms calculated VaR, believed they were safe, and then experienced losses far beyond the VaR estimate. For this reason, regulators and risk managers increasingly complement VaR with **Conditional Value at Risk (CVaR)**, also called Expected Shortfall. CVaR estimates the *average* loss in scenarios where the loss exceeds VaR—a more complete picture of tail risk.

A 99% VaR of $100 million with a CVaR of $150 million means: losses will likely not exceed $100 million, but if they do exceed $100 million, the average overage is about $50 million. That tells the risk manager: "Plan for buffers beyond $100 million; tail events are severe."

## Practical Trade-Offs: When to Use 95% vs. 99%

**Use 95% VaR when:**
- Monitoring intra-day trading desk positions (high operational frequency, daily recalibration)
- Setting position limits for a liquid, actively managed portfolio (traders react continuously)
- Running scenario analysis or stress testing (95% captures typical bad days; stress tests cover tail separately)
- Resources are constrained (capital must be deployed for returns; perfect crisis preparedness is not feasible)

**Use 99% VaR when:**
- Calculating regulatory capital requirements (Basel III mandates 99%)
- Sizing buffers for systemically important institutions (banks, insurance companies)
- Managing concentrated or illiquid positions (reaction time is slow; buffer must be larger)
- Modeling multi-day or multi-week holding periods (longer holding periods compound risk; higher confidence protects against cumulative shock)

**Use both when:**
- Designing a firm-wide risk governance framework (report 95% for operational insight, 99% for regulatory compliance and board oversight)
- Stress-testing for capital planning (use 99% VaR as baseline, then model scenarios beyond VaR)
- Communicating with stakeholders (95% for managers and risk officers; 99% for regulators and audit committees)

## The Holding Period and Confidence Level Interaction

VaR always includes a holding period (1 day, 10 days, 1 quarter, etc.). The confidence level and holding period interact. A 1-day 99% VaR and a 10-day 99% VaR are measuring different things:

- **1-day 99% VaR:** The loss threshold for a single day that is exceeded only 1% of the time. Regulators use this for day-to-day trading risk.
- **10-day 99% VaR:** The loss threshold for a 10-day period that is exceeded only 1% of the time. This is larger (roughly sqrt(10) ≈ 3.16x) because risk compounds over time.

Basel III specifies 10-day holding periods because banks need capital that is stable over a multi-day period of stress. A 1-day VaR is unsuitable for a 10-day capital requirement, as it would underestimate cumulative risk. Conversely, using a 10-day VaR for daily position limits would be overly conservative.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — Core VaR definition, methods, and interpretation
- [Conditional Value at Risk](/) — Expected shortfall; loss scenarios beyond VaR
- [Basel III Capital Adequacy](/) — Banking standard mandating 99% VaR over 10 days
- [Stress Testing](/) — Modeling losses beyond VaR in extreme scenarios
- [Expected Shortfall](/) — Average loss conditional on exceeding VaR

### Wider context

- Risk Measurement — Overview of quantitative risk frameworks
- [Volatility and Standard Deviation](/) — Building block for VaR calculation
- [Tail Risk](/) — Rare, extreme events not fully captured by normal distributions
- [Monte Carlo Simulation](/) — Method for estimating VaR under complex correlations

</div>

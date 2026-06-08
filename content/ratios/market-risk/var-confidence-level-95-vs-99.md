---
title: "VaR at 95% vs 99% Confidence: What the Difference Means"
description: "Compare 95% and 99% confidence level Value at Risk: tail risk capture, regulatory requirements, and practical interpretation for portfolio risk."
keywords:
  - var 95 vs 99 confidence level
  - value at risk confidence level
  - tail risk measurement
  - var 95 percent
  - var 99 percent
image: /svg/ratios.svg
---

*The difference between a **95% and 99% confidence level in Value at Risk** is the difference between capturing the worst 1 trading day in 20 versus the worst 1 in 100. At 99%, you're measuring deeper into the tail, and that tail can be dramatically worse—which is why some regulators mandate 99% for certain institutions, while 95% is the market default for most risk dashboards.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VaR Confidence Levels — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">Higher confidence catches rarer, uglier losses.</div>

|   |   |
|---|---|
| **95% VaR definition** | Maximum expected loss in 95 out of 100 trading days (or 5% worst-case days) |
| **99% VaR definition** | Maximum expected loss in 99 out of 100 trading days (or 1% worst-case days) |
| **Frequency difference** | 95%: 1 breach every ~20 days; 99%: 1 breach every ~100 days |
| **Tail depth** | 99% captures more extreme tail risk; often 1.5x to 3x higher than 95% |
| **Market standard** | 95% is most common for trading desks and daily risk reporting |
| **Regulatory mandate** | 99% required for many bank capital rules (Basel III); some derivatives dealers prefer 99% |
| **Limitation** | Both assume historical patterns repeat; neither predicts unprecedented shocks |

</aside>

## What the confidence level actually measures

[Value at Risk](/value-at-risk/) (VaR) answers: "What is the maximum loss I could face, given normal market conditions, over a specific holding period?"

The **confidence level** defines what you mean by "normal." At 95% confidence over one trading day, you're saying: "I am 95% confident that my portfolio will not lose more than X dollars tomorrow." Put another way, there's a 5% chance tomorrow's loss will exceed X.

At 99% confidence, you're saying: "I am 99% confident the loss won't exceed Y dollars." There's a 1% chance it will be worse.

Since 99% demands a higher level of confidence, the dollar amount (Y) must be larger than 95% VaR (X). You're paying for extra certainty by accepting a larger potential loss number.

## Concrete example

Suppose a portfolio manager calculates:

- 95% VaR over 1 day = USD 500,000
- 99% VaR over 1 day = USD 1,200,000

This means:

- In a normal trading day, the portfolio is expected to lose USD 500,000 or less 95 times out of 100.
- In the remaining 5 days out of 100, losses could exceed USD 500,000.
- In 99 days out of 100, the portfolio is expected to lose USD 1,200,000 or less.
- In 1 day out of 100, losses could exceed USD 1,200,000.

The gap between USD 500,000 and USD 1,200,000 reflects the additional tail risk captured by moving from 95% to 99% confidence. Rare days are much worse than normal days.

Over 250 trading days per year:

- At 95%, you'd expect roughly 12 to 13 breaches (days exceeding 95% VaR) per year.
- At 99%, you'd expect roughly 2 to 3 breaches per year.

This is why 99% is sometimes called the "stress level" confidence—it's catching days that almost never happen under normal conditions, but when they do, they're severe.

## Why the tail gets fatter at 99%

The shape of the loss distribution is not uniform. In calm markets, daily losses cluster tightly around small negative numbers. But as you move toward extreme losses, the distribution flattens and stretches—the "tail."

Imagine a histogram of daily losses. The peak is around -0.5% per day. As you walk rightward toward -5%, -10%, -20%, the bars get shorter, but they don't disappear as quickly as a simple bell curve would predict. This is especially true during crises, when correlations between assets spike and normally uncorrelated risks suddenly move together.

A 95% VaR might be measured at the point where you've captured the densest 95% of past observations. A 99% VaR pushes further into the tail, where losses are rare but brutal. Empirically, the ratio of 99% VaR to 95% VaR often ranges from 1.5 to 3.0 depending on the portfolio and market conditions. In extreme markets (2008, 2020), that ratio can widen even further.

## When regulators mandate 99%

Different rules apply to different institutions:

**Basel III (bank capital requirements)**

Most large banks must calculate risk-weighted assets using 99% VaR over a 10-day holding period. This conservative standard reflects the regulator's goal: ensuring banks can survive losses that would occur roughly once per year or less frequently. A 1% tail-loss number forces banks to hold more capital than they'd need under 95%.

**Securities dealers and proprietary traders**

The SEC and FINRA historically allowed 95% VaR for daily risk reporting because trading desks have shorter holding periods and higher turnover. However, some firms use 99% VaR internally as a stricter risk discipline, especially for leverage-heavy strategies.

**Derivatives clearinghouses**

Many clearinghouses use 99% VaR (or even higher confidence levels like 99.5%) to set margin and default fund requirements. The logic: a clearinghouse must survive the default of its largest members, which is a tail event, so it needs to measure very-tail risk.

## 95% vs. 99% in practice: a trader's view

Most trading desks display 95% VaR on dashboards because it's the market standard and easier to justify day-to-day. A trader who sees her USD 500,000 limit breached twice a month might adjust leverage, diversify, or tighten risk parameters.

But senior risk officers and CFOs often overlay 99% VaR as a "stress" metric. They're asking: "If tomorrow is the worst day we've seen in the past 100 trading days, what's our loss?" The answer—USD 1,200,000 in the example—becomes a board-level talking point about the firm's true downside exposure.

Some firms use both: 95% for red-light early warnings, 99% for capital adequacy and stress testing.

## The big limitation: tail assumptions

Both 95% and 99% VaR assume that historical tail behavior will repeat. If the worst day in the past decade was a -8% loss, the 99% VaR will be calibrated to something close to -8%. But in a genuine black-swan event—a surprise geopolitical shock, a pandemic, a financial collapse—losses can far exceed any historical precedent.

This is why risk managers always pair VaR with [stress testing](/stress-testing/) and scenario analysis. A 99% VaR might say "our worst-case loss is USD 1.2 million." But a scenario that assumes a sudden 20% equity market crash might produce a USD 5 million loss. Stress testing fills in what VaR can't.

## Confidence level jargon across asset classes

- **Equities**: 95% is common for daily portfolio risk; 99% for capital requirements.
- **Fixed income**: Often use 99% for credit spread risk because tail moves are infrequent but large.
- **Forex**: 95% or 99% for daily trading; emerging-market FX sometimes uses 99% due to higher tail risk.
- **Commodities**: 99% often used because commodity crashes tend to be sudden and severe.

There's no universal standard; it depends on the firm's risk appetite, regulator, and counterparty expectations.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — the main VaR framework
- [Tail Risk](/tail-risk/) — the distant-loss events VaR tries to measure
- [Stress Testing](/stress-testing/) — complementary risk discipline that VaR alone cannot replace
- [Expected Shortfall](/expected-shortfall/) — an alternative to VaR that measures average loss beyond the VaR threshold
- [Risk-Weighted Assets](/risk-weighted-assets/) — Basel framework that uses 99% VaR

### Wider context

- [Capital Adequacy](/capital-adequacy/) — why regulators care about tail-loss measures
- [Market Risk](/market-risk/) — the broader category VaR addresses
- [Volatility Smile](/volatility-smile/) — why tail risk is priced into options
- [Beta](/beta/) — a simpler risk measure that complements VaR

</div>

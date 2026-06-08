---
title: "Conditional Value at Risk: Calculation with an Example"
description: "Conditional Value at Risk (CVaR) measures average losses beyond the Value at Risk threshold, providing a fuller picture of tail risk than VaR alone."
keywords:
  - conditional value at risk
  - how to calculate conditional value at risk
  - expected shortfall
  - tail risk
  - value at risk
  - risk metrics
image: /svg/ratios.svg
---

*Conditional Value at Risk (CVaR), also called expected shortfall, measures the average loss a portfolio will suffer on its worst-case days—specifically, days when losses exceed the standard [Value at Risk](/value-at-risk/) threshold. It answers: "If my losses are worse than my X% confidence level predicts, how bad will they really be?"*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CVaR — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A tail-risk metric that captures the pain point VaR leaves blind.</div>

|   |   |
|---|---|
| **Formula** | Average of all losses exceeding the VaR threshold |
| **Also called** | Expected shortfall, average tail loss |
| **Common use** | 95% confidence (5th percentile worst case) |
| **Interpretation** | "If outcomes are in the bottom X%, what's my average loss?" |
| **Advantage over VaR** | Shows severity of rare, extreme moves |
| **Disadvantage** | Harder to calculate; less standardized |
| **Why it matters** | [Value at Risk](/value-at-risk/) ignores the tail; CVaR doesn't |

</aside>

## Why VaR alone misses the plot

[Value at Risk](/value-at-risk/) at the 95% confidence level tells you: "There is a 95% chance my loss won't exceed X on any given day." Equivalently, there is a 5% chance it will be worse. That 5% tail is where disaster lives.

The problem: VaR is a threshold, not an average. It says where the cliff edge is. It does not say how far down the cliff goes. If you're standing on a 10-meter drop, knowing the drop exists is useful. Knowing it could be 100 meters is crucial—and that's what CVaR reveals.

In practice, financial markets do not distribute losses symmetrically. Crises cluster. When volatility spikes, losses cascade. The worst day of a month may be ten times worse than the 95th-percentile expectation. CVaR captures this by averaging the actual losses across all outcomes that exceed the VaR threshold. It answers the question: "Given that things went very wrong, how much did I lose, on average?"

## Step-by-step CVaR calculation

Assume you have 100 days of historical returns for a portfolio, arranged from worst to best.

**Step 1: Calculate VaR at 95% confidence.**

At 95% confidence, you're interested in the worst 5% of outcomes. With 100 days, that's the worst 5 days (days ranked 1–5 when sorted worst-first).

Suppose the daily losses on those 5 days are:
- Day 1: −$50,000
- Day 2: −$35,000
- Day 3: −$28,000
- Day 4: −$18,000
- Day 5: −$12,000

The Value at Risk at 95% confidence is the boundary—often defined as the loss on the exact 5th-worst day: **−$12,000**. (Some methods interpolate; others use the 4th worst at exactly 5%.)

**Step 2: Average the losses that exceed VaR.**

Now take all losses worse than or equal to the VaR threshold:
- −$50,000
- −$35,000
- −$28,000
- −$18,000
- −$12,000

Average = (50,000 + 35,000 + 28,000 + 18,000 + 12,000) ÷ 5 = **−$28,600**

That is your Conditional Value at Risk: **CVaR₉₅% = −$28,600**.

**Interpretation:** If outcomes are bad enough to breach the 95th-percentile threshold, your average loss is $28,600—more than double the VaR itself ($12,000). On a really bad day, the portfolio bleeds worse than the typical tail scenario suggests.

## A realistic multi-asset example

Consider a simple two-asset portfolio: 60% stock, 40% bonds. You track daily returns over a year (252 trading days).

Suppose, when sorted worst-to-best, the worst 13 days (5% of 252) show:

| Rank | Stock return | Bond return | Portfolio return |
|------|--------------|-------------|------------------|
| 1    | −12%         | +0.5%       | −6.8%            |
| 2    | −9%          | −0.2%       | −5.4%            |
| 3    | −8%          | +1%         | −4.2%            |
| 4    | −7%          | −1%         | −4.4%            |
| 5    | −6%          | +0.3%       | −3.3%            |
| 6    | −5.5%        | +0.5%       | −3.0%            |
| 7    | −5%          | −0.5%       | −3.2%            |
| 8    | −4.5%        | +0.2%       | −2.5%            |
| 9    | −4%          | +1%         | −1.8%            |
| 10   | −3.5%        | −0.1%       | −2.0%            |
| 11   | −3%          | +0.5%       | −1.6%            |
| 12   | −2.5%        | −0.2%       | −1.4%            |
| 13   | −2%          | +1.5%       | −0.9%            |

The VaR₉₅% is the return on day 13: **−0.9%**. On a $1 million portfolio, that's a loss of $9,000.

To calculate CVaR, average all losses equal to or worse than −0.9%:

CVaR₉₅% = (−6.8 − 5.4 − 4.2 − 4.4 − 3.3 − 3.0 − 3.2 − 2.5 − 1.8 − 2.0 − 1.6 − 1.4 − 0.9) ÷ 13 = **−3.34%**

On the $1 million portfolio, that's an average loss of $33,400 when things go wrong. The true tail risk is 3.7 times worse than VaR suggests.

## Why this matters in practice

**For capital allocation:** A [hedge fund](/hedge-fund/) or [asset manager](/asset-allocation/) using only VaR to size positions underestimates the worst outcomes. CVaR forces acknowledgment of tail events. If CVaR is 4% but VaR is 1%, the gap signals a distribution with severe tail skew—the kinds of crises where correlations spike and diversification fails.

**For risk budgets:** Banks and asset managers allocate a "risk budget"—a maximum expected loss—across desks and strategies. Using VaR alone, a desk can trade up to the VaR limit on each position and appear compliant. But if several desks hit their worst-case CVaR simultaneously (common in market stress), the firm's aggregate loss can wildly exceed the sum of the budgets. CVaR forces conservative position sizing by revealing the true cost of tail breaches.

**For derivatives and concentrated portfolios:** A concentrated [call option](/call-option/) or [leveraged ETF](/leveraged-etf/) position may have a modest VaR under normal conditions but catastrophic CVaR in a market crash. CVaR reveals whether your worst case is merely bad or genuinely catastrophic.

**For tail-risk hedging:** Investors buying [protective puts](/protective-put/) or [tail-risk funds](/hedge-fund/) care about CVaR, not VaR. The hedge is meant to cap the average loss on the worst days. CVaR quantifies what that protection buys.

## CVaR under different confidence levels

You can calculate CVaR at any confidence level. Higher confidence levels (99%, 99.9%) examine even rarer scenarios:

- CVaR₉₅%: average of the worst 5% of days
- CVaR₉₉%: average of the worst 1% of days
- CVaR₉₉.₉%: average of the worst 0.1% of days

With limited historical data, CVaR at very high confidence levels becomes unstable—you're averaging a handful of extreme events, and one tail outlier can skew the average. At 99.9%, you're averaging perhaps 2–3 days across 1,000 observations. A single crisis day dominates the calculation.

This is where **[stress testing](/stress-testing/)** complements CVaR: you simulate scenarios (a 2008-style crash, a flash-crash shock, a geopolitical event) and measure CVaR under those hypothetical shocks, rather than relying on the thin tail of actual history.

## CVaR limitations and complementary metrics

CVaR is not flawless. It assumes past distributions repeat—a weak assumption during regime shifts. It is also harder to calculate and less standardized than VaR, leading to inconsistent implementations across firms.

Complement CVaR with:
- **[Stress testing](/stress-testing/):** Scenario analysis of extreme moves
- **Expected shortfall by source:** Break down tail losses by market factor (equity beta, credit spread, [volatility](/volatility-smile/)) to understand which risks matter on bad days
- **[Drawdown analysis](/value-at-risk/):** The largest peak-to-trough decline in cumulative performance, a different lens on tail severity
- **Tail-risk correlation:** Do your hedges actually reduce CVaR, or are they also correlated to your main risks in crises?

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — the threshold CVaR builds on
- [Stress testing](/stress-testing/) — scenario analysis of tail scenarios beyond historical data
- [Volatility smile](/volatility-smile/) — why tail risks are priced into options
- [Beta](/beta/) — systematic risk that CVaR captures alongside idiosyncratic risk
- [Tail risk](/tail-risk/) — the phenomenon CVaR quantifies

### Wider context

- Risk management — the framework that uses CVaR
- [Hedge fund](/hedge-fund/) — a common user of CVaR-driven position limits
- [Asset allocation](/asset-allocation/) — how CVaR influences portfolio construction
- [Drawdown analysis](/value-at-risk/) — alternative measures of downside severity
- [Capital adequacy](/capital-adequacy/) — regulatory frameworks using CVaR-like measures

</div>

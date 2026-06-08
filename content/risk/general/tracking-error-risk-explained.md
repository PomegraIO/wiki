---
title: "Tracking Error as a Risk Measure Explained"
description: "Tracking error risk explained: how active funds are measured against their benchmark, calculated from return variance, and interpreted as manager skill or drift."
keywords:
  - tracking error risk explained
  - active fund performance measurement
  - benchmark deviation
  - active management cost
  - portfolio risk measurement
image: /svg/risk.svg
---

*Tracking error is the standard deviation of the difference between a [fund](/mutual-fund/)'s returns and its [benchmark](/sp-500-index/) index—a measure that quantifies how far and how consistently an active manager strays from their stated comparison. Understanding tracking error matters because it reveals whether returns differ from the benchmark due to intentional skill, unintentional drift, or simply high trading costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tracking Error Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The bridge between passive and active: a measure of deviation, not of absolute risk.</div>

|   |   |
|---|---|
| **Definition** | Standard deviation of excess returns versus benchmark |
| **Expressed as** | Percentage per annum (e.g., 2.5% tracking error) |
| **Low tracking error** | Fund hugs benchmark (near-passive behavior) |
| **High tracking error** | Fund diverges materially from benchmark (high active bets) |
| **Typical range** | 0.5% to 5%+ depending on strategy and mandate |
| **Not the same as** | Absolute [volatility](/volatility-smile/), [alpha](/alpha/), or [beta](/beta/) |

</aside>

## Defining Tracking Error Risk

**Tracking error** is the volatility of a fund's excess return—the gap between what the fund earned and what its benchmark earned, measured over time. If the S&P 500 returned 10% and an active large-cap fund returned 11%, the excess return was 1 percentage point. But excess return varies month to month. Tracking error is the standard deviation of those excess returns.

For example: A fund returns 8%, 11%, 12%, 9% annually while its benchmark returns 7%, 10%, 10%, 10%. The excess returns are +1%, +1%, +2%, −1%. The standard deviation of those excess returns is the tracking error. A fund with 1% tracking error should stay within roughly 1 percentage point of its benchmark two-thirds of the time (one standard deviation). A fund with 5% tracking error is vastly more volatile relative to its benchmark, meaning the manager is taking much larger bets.

Tracking error is not the same as [volatility](/historical-volatility/). Volatility measures absolute price swings. Tracking error measures only the unpredictable part of returns relative to a stated index. This distinction is central: a fund might be highly volatile in absolute terms but have very low tracking error if its volatility mirrors its benchmark. Conversely, a [hedge fund](/hedge-fund/) with low absolute volatility might have high tracking error if it systematically bets against the market.

## How Tracking Error Is Calculated

The mathematical approach is straightforward:

1. Calculate the excess return for each period: Fund return − Benchmark return
2. Find the standard deviation of those excess returns
3. Annualize if using monthly or quarterly data

For a monthly tracking error, multiply the monthly figure by √12. For quarterly, multiply by √4. This converts the periodic volatility into an annual figure, making comparisons fair across different reporting frequencies.

Many funds publish tracking error in their prospectuses or annual reports. It is also a standard metric in [fund](/fund-prospectus/) comparison tools and academic research on [active management](/actively-managed-fund/).

## High Tracking Error vs. Low Tracking Error

**Low tracking error** (below 1%) usually signals a fund that is behaving like a closet indexer—making only small, subtle bets relative to the benchmark. This might happen intentionally (a fund marketed as "low-cost active" with a tight mandate) or as an accident of poor fund management. Low tracking error paired with returns that trail the benchmark by more than the [expense ratio](/expense-ratio/) suggests the manager is neither adding value nor taking meaningful risk—a red flag for [active management](/actively-managed-fund/).

**High tracking error** (3–8%+) indicates the manager is making large, distinct bets: overweighting certain sectors or stocks, holding cash differently, perhaps using [derivatives](/derivatives-hedging/) or [short positions](/short-selling/). High tracking error is not inherently bad—it reflects the manager's conviction. But high tracking error paired with returns near the benchmark suggests the bets are canceling out, and the investor is paying [management fees](/management-fee/) for volatility that adds no value.

The optimal tracking error depends on the fund's stated strategy. A [value fund](/value-fund/) tracking the S&P 500 might have 2–3% tracking error because value stocks differ from the index. A [growth fund](/growth-fund/) might have 3–5% because growth is a more distinct tilt. An [index fund](/index-fund/) should have near-zero tracking error (minus a small drag from fees).

## Tracking Error and Active Manager Skill

Tracking error is a building block in assessing manager skill. The ratio of excess return to tracking error is called the [information ratio](/sharpe-ratio/)—one of the most widely used metrics for evaluating active managers. A manager with 2% excess return and 4% tracking error has an information ratio of 0.5, while a manager with 2% excess return and 2% tracking error has an information ratio of 1.0. The second manager has achieved the same outperformance with tighter bets, suggesting greater precision.

Over long periods, [alpha](/alpha/) (true excess return from skill) should be positive and exceed the costs of active management. If a manager has high tracking error but negative or near-zero alpha, the tracking error is pure noise—wasted risk that neither adds nor subtracts value.

## Benchmark Choice Matters

Tracking error is meaningless without the right benchmark. A technology-focused fund tracked against the S&P 500 will have very high tracking error, because the S&P 500 includes many non-tech sectors. The same fund tracked against a technology index will have much lower tracking error. Investors must ensure the stated benchmark is actually comparable to the fund's holdings. A mismatch—a tech fund tracked against the S&P 500—masks whether the manager is actually outperforming the right index.

## Practical Implications for Investors

High tracking error is a cost. If you want your portfolio to move like the S&P 500, you should buy an [index fund](/index-fund/) with near-zero tracking error and minimal fees. If you hire an active manager and pay them 1% annually, you expect them to earn that 1% through [alpha](/alpha/)—a return above the benchmark. If the manager has 5% tracking error but only delivers 0.5% alpha, you have paid for risk that did not translate to return. The tracking error itself is not free; it is variance you are absorbing that a passive alternative would not impose.

Conversely, if a manager with high tracking error is delivering consistent [alpha](/alpha/) above their fees, that tracking error is the manager's strategy at work, and it is justified by results.

## See also

<div class="wiki-seealso">

### Closely related

- [Alpha](/alpha/) — Excess return independent of market movements
- [Beta](/beta/) — Systematic market risk and correlation to benchmark
- [Information ratio](/sharpe-ratio/) — Excess return divided by tracking error
- [Actively managed fund](/actively-managed-fund/) — How active managers diverge from benchmarks
- [Index fund](/index-fund/) — Passive benchmark replication

### Wider context

- [Standard deviation and volatility](/historical-volatility/) — Foundation of variance-based risk measures
- [Expense ratio](/expense-ratio/) — Cost that reduces alpha and must be overcome
- [Sharpe ratio](/sharpe-ratio/) — Risk-adjusted return metric for absolute performance
- [Value at risk](/value-at-risk/) — Alternative tail-risk measurement

</div>

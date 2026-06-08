---
title: "Modigliani Risk-Adjusted Performance"
description: "A portfolio's return rescaled to match the benchmark's volatility, producing a directly comparable percentage return independent of the fund's actual risk level."
keywords:
  - modigliani risk-adjusted performance
  - m-squared
  - risk adjustment
  - performance metrics
  - portfolio comparison
  - volatility equalization
image: "/svg/ratios.svg"
---

*Modigliani risk-adjusted performance (M-squared) takes any fund's historical return and asks: "What would this fund have earned if it held the same volatility as the benchmark?" By levering or deleveraging the fund's returns to match the benchmark's [risk](/market-risk/), M-squared produces apples-to-apples return comparisons. A conservative 8% fund and an aggressive 12% fund become directly comparable once volatility is standardized.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Modigliani Risk-Adjusted Performance — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Expressed as a percentage; higher is better; directly comparable across any two portfolios.</div>

|   |   |
|---|---|
| **What it is** | Fund return adjusted upward/downward to match benchmark volatility; named after Franco Modigliani |
| **Formula** | Fund return + [Sharpe ratio](/market-risk/) × (benchmark volatility − fund volatility) |
| **Benchmark volatility** | Usually the S&P 500 or relevant index; typically 15–20% annually |
| **Interpretation** | M² = 10% means: at benchmark risk level, this fund would earn 10% |
| **Strength** | Handles different-risk portfolios; not dependent on correlation |
| **Limitation** | Assumes returns scale linearly with volatility; past volatility may not persist |

</aside>

## The core insight: volatility as the common denominator

Imagine two portfolio managers. One runs a conservative fund with 10% annual volatility, earning 7% returns. The other runs an aggressive [hedge fund](/hedge-fund/) with 25% volatility, earning 9% returns. Which manager is better?

The 25% volatility fund looks superior by raw return: 9% beats 7%. But that manager is taking 2.5 times more risk to earn 28% more return. The conservative manager is doing more with less. Without adjusting for risk, the comparison is incomplete.

[Alpha](/alpha/) and [beta](/beta/) try to answer this, but they depend on [correlation](/r-squared-finance/) to a specific benchmark. M-squared sidesteps that complexity. It rescales both funds to the same volatility level—say, the benchmark's 18% volatility—and asks: at that risk level, how much would each fund earn?

If the conservative fund's 7% return at 10% volatility scales up to 12.6% at 18% volatility, and the aggressive fund's 9% at 25% volatility scales down to 8.1% at 18% volatility, the conservative manager has revealed superior risk-adjusted skill. The comparison is now apples-to-apples.

## The mechanism: scaling returns to a standard risk level

M-squared uses the [Sharpe ratio](/market-risk/)—the fund's excess return divided by its volatility—to measure efficiency per unit of risk. That ratio is then applied to the benchmark's volatility to produce the adjusted return.

M² = Fund return + Sharpe ratio × (Benchmark volatility − Fund volatility)

If a fund earned 12% with 15% volatility (and assuming a risk-free rate of 2%, a Sharpe ratio of 0.67), and the benchmark has 18% volatility:

M² = 12% + 0.67 × (18% − 15%) = 12% + 2.01% = 14.01%

The message: at the benchmark's 18% volatility, this fund's methodology would have delivered 14.01%. Compare that figure directly to another fund's M² figure, and risk is already accounted for.

## Why Modigliani matters for portfolios of different styles

Modigliani is especially useful for comparing portfolios that deliberately differ in risk level. A stable-value fund and a growth fund shouldn't be ranked by absolute return alone; they serve different purposes. M² lets you ask: if the stable-value fund were levered to growth-fund volatility, would it outperform?

Similarly, when evaluating a [low-volatility ETF](/equity-etf/) against a standard [equity ETF](/equity-etf/), M² converts the low-volatility fund's modest returns into an equivalent return at benchmark risk. If the low-vol fund earned 6% at 10% volatility, and the benchmark returned 10% at 18% volatility, M² would show the low-vol fund's equivalent return at 18% volatility. That adjusted figure reveals whether the low-vol manager's security selection is genuinely skilled or just riding the low-volatility factor.

## The lever assumption: a source of controversy

M-squared rests on a critical assumption: that a fund's return scales proportionally with volatility. If you lever a fund's portfolio by 1.5x (taking 50% more risk), the theory assumes returns also scale by 1.5x.

In practice, that's only partially true. Leverage is costly. A fund that levered its holdings would bear [financing charges](/cost-of-debt/), widening [bid-ask spreads](/bid-ask-spread/), and potential margin calls during market stress. These frictions eat into returns, so a levered portfolio underperforms the theoretical scaling.

Conversely, the assumption breaks down during market dislocations. A fund's volatility measured over calm years may spike during crashes when correlations shift and [tail risk](/tail-risk/) activates. An M² figure calculated from historical calm-period data could overstate the fund's risk-adjusted returns in a true stress scenario.

## M-squared versus other risk-adjusted metrics

M-squared differs meaningfully from [alpha](/alpha/), which is return beyond what [beta](/beta/) would predict for a given [benchmark](/sp-500-index/). Alpha assumes a linear relationship to the benchmark; M² abstracts away the benchmark entirely, using volatility alone.

It differs also from [Sharpe ratio](/market-risk/), which measures return per unit of risk but doesn't convert to an actual dollar return—it's a ratio, not a return percentage. M² converts that ratio into a return figure, making it more intuitive for side-by-side fund comparisons.

And it differs from [down-capture ratio](/down-capture-ratio/), which ignores upside entirely and focuses on loss severity. M² weights both upside and downside equally through volatility.

For a complete assessment, pair M² with [up-capture ratio](/up-capture-ratio/) and [down-capture ratio](/down-capture-ratio/) to understand whether the fund's risk comes from large rallies (benign) or potential crashes (concerning).

## The evergreen problem: past volatility is not future volatility

M-squared is a historical metric. It answers: "Based on what this fund did, here's its risk-adjusted return at benchmark volatility." It doesn't predict what the fund will do forward.

A fund's volatility can shift for many reasons: strategy changes, manager departure, [market regime](/business-cycle/) shift, or growth in asset size. A small, nimble fund with 12% historical volatility might swell to billions under management and end up with 18% volatility as manager skill matters less. The M² figure would be stale.

Institutional investors often recompute M² using rolling windows (e.g., the trailing three years) to catch shifts in fund behaviour. Even so, M² remains a backward-looking snapshot, not a forward covenant.

## When to use M-squared, and when to dig deeper

M² shines when comparing two funds with materially different risk profiles serving different purposes. Should a retiree use this low-volatility equity fund or that standard equity fund? M² translates both to the same risk level and compares returns directly.

It's less useful when comparing funds already matched to the same benchmark and risk profile—two [large-cap growth funds](/growth-fund/), for instance. In that case, [up-capture ratio](/up-capture-ratio/) and [alpha](/alpha/) are more relevant because they measure outperformance within the same environment.

It's also incomplete without context. A 12% M² is stellar if earned over 10 years; it's suspicious if earned over 18 months of a bull market. Pair M² with the fund's [Sharpe ratio](/market-risk/), [R-squared](/r-squared-finance/) to the benchmark, [down-capture ratio](/down-capture-ratio/), and absolute return history to build a full picture.

## See also

<div class="wiki-seealso">

### Closely related

- [Up-Capture Ratio](/up-capture-ratio/) — fund's participation in benchmark upswings; complements M² for a fuller view
- [Down-Capture Ratio](/down-capture-ratio/) — fund's loss participation in downturns; essential context for volatility assumptions
- [Alpha](/alpha/) — excess return; can be rephrased as M² relative to a leveraged baseline
- [Beta](/beta/) — systematic sensitivity; M² abstracts away beta in favour of pure volatility
- [Sharpe ratio](/market-risk/) — the efficiency ratio underlying M²; fundamental to the calculation
- [R-Squared](/r-squared-finance/) — how closely the fund correlates with the benchmark; context for whether M² applies

### Wider context

- [Market risk](/market-risk/) — systematic volatility that M² assumes scales linearly with returns
- [Volatility](/market-risk/) — the standardizing metric; fund and benchmark volatility drive the adjustment
- [Actively managed fund](/actively-managed-fund/) — likely to differ from the benchmark in both return and volatility
- [Index fund](/index-fund/) — by definition has 100% M² relative to its benchmark at its own volatility
- [Hedge fund](/hedge-fund/) — often has high absolute volatility; M² reveals whether that risk is compensated
- [Leverage](/leverage-ratio-forex/) — the mechanism by which M² rescales returns; less costly for passive indices than active funds

</div>

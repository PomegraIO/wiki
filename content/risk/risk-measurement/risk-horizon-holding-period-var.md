---
title: "Risk Horizon and Holding Period in VaR"
description: "Understand holding period and risk horizon in VaR—what they mean, how to scale from one-day to ten-day VaR under Basel rules, and the assumptions behind scaling."
keywords:
  - holding period risk horizon var
  - risk horizon value at risk
  - ten-day var one-day var scaling
  - var holding period
  - basel var assumptions
image: "/svg/risk.svg"
---

*In **value at risk (VaR)**, the holding period (or risk horizon) is the length of time over which you expect to hold a position before being able to close it or hedge it. A one-day VaR answers "how much could I lose in one trading day?" A ten-day VaR answers the same question over ten days. Scaling between horizons is not straightforward; it requires assumptions about market liquidity, position size, and return distributions. Basel regulations mandate specific scaling rules, most commonly the [square root of time](/annualizing-volatility-square-root-of-time/) method, which assumes independent returns and normal tails—assumptions real markets violate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Horizon in VaR — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Holding periods reflect how fast you can exit; scaling assumes independence and normality.</div>

|   |   |
|---|---|
| **One-day VaR** | Loss potential over one trading day, assuming position is unchanged |
| **Ten-day VaR (Basel standard)** | Loss potential over ten trading days; minimum [VaR](/value-at-risk/) horizon for capital rules |
| **Scaling formula** | VaR_10day = VaR_1day × √10 |
| **Assumption** | Returns are independent; normality; no regime shift or liquidity cliff |
| **Key limitation** | Understates tail risk in stress; ignores correlation clustering |
| **Regulatory use** | Bank capital requirements, position limits, stress testing benchmarks |

</aside>

## What Holding Period Means

The holding period is the time span over which a portfolio's losses are measured in a VaR calculation. It reflects the realistic time needed to liquidate a position or hedge its risk.

For a **highly liquid asset** (e.g., shares of a large-cap stock, government bonds, active futures contracts), the holding period might be one day. A trader holding 10,000 shares of a mega-cap stock can sell them all within minutes. For risk management, one-day VaR reflects the most likely scenario: a sudden shock forces a mark-to-market loss today, and the position is closed or rebalanced before market close.

For **less liquid assets** (e.g., small-cap equities, thinly traded corporate bonds, real estate positions), the holding period is longer—three days, ten days, or more. If you hold illiquid positions that take a week to sell, the VaR horizon should reflect that reality. You cannot liquidate instantly, so you face ten days of price risk, not one.

**Regulatory holding periods** are mandated by Basel frameworks and other supervisors. For bank capital requirements, the standard is ten trading days (two weeks, excluding weekends). This reflects the idea that even liquid markets can seize up temporarily; during stress, a large position might take a week or two to fully unwind without severe market impact.

## The Square Root of Time Scaling Rule

The most common method to scale VaR across horizons is the [square root of time rule](/annualizing-volatility-square-root-of-time/). If you know one-day VaR at a given confidence level, multiply it by √10 to estimate ten-day VaR:

VaR_10day = VaR_1day × √10 ≈ VaR_1day × 3.16

This rule derives from the assumption that returns are independent and identically distributed. Under that assumption, the variance of cumulative returns over 10 days equals 10 times the one-day variance, so volatility scales by √10 and so does VaR (which is proportional to volatility).

More generally:

VaR_n-day = VaR_1day × √n

For three-day VaR (often used in [internal models](/stress-testing/)):

VaR_3day = VaR_1day × √3 ≈ VaR_1day × 1.73

For five-day VaR (common in hedge fund risk reporting):

VaR_5day = VaR_1day × √5 ≈ VaR_1day × 2.24

This scaling is mechanically exact if returns are i.i.d. and the confidence level and distribution type are held constant.

## When This Assumption Holds and When It Breaks

The square root of time rule works reasonably well for **liquid, exchange-traded instruments** during normal market conditions. Equities, government bonds, and major currency pairs scale reliably over short horizons (one to ten days). Academic studies confirm that one-day equity volatility scaled by √10 often predicts ten-day volatility within 10–20% error.

The rule breaks down under several conditions:

**Autocorrelation and momentum** push realized ten-day volatility above the rule's prediction. If markets exhibit short-term momentum (positive autocorrelation), cumulative moves grow faster than √10 would suggest. Conversely, mean reversion (negative autocorrelation) produces realized volatility lower than predicted. During crises, momentum effects can be strong; the square root scaling understates tail risk.

**Fat tails and regime shifts** violate the normality assumption. During market stress, extreme price moves occur far more frequently than a normal distribution allows. The square root rule assumes the same distribution on each day; in reality, a crisis day has a different distribution than a calm day. A ten-day period spanning a crisis will suffer losses much larger than √10 times one-day VaR.

**Liquidity evaporation** is perhaps the most critical limitation. The rule assumes you can liquidate continuously and at stable prices. In a market crash, liquidity dries up. A position you expected to close in one day might require ten days. The loss over those ten days is not just the price move; it is also the cost of forced liquidation in a stressed market (called [adverse selection](/bid-ask-spread/) or market impact). The square root rule ignores this cost entirely.

## Basel's Regulatory Approach

Under Basel III, banks must calculate internal [value-at-risk](/value-at-risk/) using a specified methodology and horizon. The standard is ten trading days at a 99% confidence level. The calculation proceeds as follows:

1. Estimate one-day volatility using [EWMA](/ewma-volatility-model/) (decay parameter λ = 0.94).
2. Compute one-day [VaR](/value-at-risk/) using a normal (or student-t) distribution at 99% confidence.
3. Scale to ten-day VaR by multiplying by √10.
4. Use this ten-day VaR to calculate minimum capital reserves.

Basel also requires **stress testing**: banks must compute VaR under a pre-defined crisis scenario (e.g., 2008 financial crisis data) and set capital high enough to cover losses in both normal and stressed conditions.

The regulators deliberately chose a long holding period (ten days) and high confidence level (99%) because they want banks to be well-capitalized against tail risk. A one-day VaR is too optimistic; it ignores the possibility of sequential losses over multiple days. Ten days is more conservative.

## The Illiquidity Premium and Holding Period Extension

In practice, many large financial institutions adjust the holding period upward for illiquid assets. A bank's risk framework might use:

- One day for major stock indices and government bonds
- Three days for investment-grade corporate bonds and [equity indices](/sp-500-index/) in emerging markets
- Ten days for [high-yield bonds](/high-yield-bond/), thinly traded derivatives
- Twenty or more days for real estate, private equity holdings, or illiquid credit

This reflects the true time needed to liquidate without severe market impact. A longer holding period then scaled by √n produces a higher VaR, forcing the bank to reserve more capital—a rational response to illiquidity.

Some institutions apply an "illiquidity premium" on top of the baseline √n scaling:

VaR_adjusted = VaR_scaled × (1 + illiquidity_factor)

The illiquidity factor might be 10% for investment-grade bonds, 30% for high-yield, and 50% for derivatives on illiquid underlyings. This is a heuristic, not a regulatory formula, but it reflects a widespread belief that square root scaling alone is insufficient.

## Limitations of the Standard Approach

The square root of time rule is transparent and easy to implement, which is why regulators endorsed it. But it carries several risks.

**Short holding periods underestimate concentration risk.** A one-day horizon misses the possibility of a "flash crash" followed by liquidity collapse lasting several days. A fund that assumes it can exit a large position in one day may face forced liquidation at fire-sale prices if markets jam up.

**Long holding periods may be conservative overestimates.** For highly liquid assets during normal times, a ten-day VaR is unnecessarily pessimistic. Regulators chose it as a one-size-fits-all rule, accepting that it will be too high for some portfolios and possibly too low for others.

**Regime shifts are not captured.** If volatility or correlation regimes shift during the holding period—which happens frequently in crises—the i.i.d. assumption is violated. A ten-day period straddling a market shock will experience larger losses than the √10 scaling predicts.

## Holding Period and Stress Testing

To address these gaps, regulators now require supplementary [stress testing](/stress-testing/). Banks must compute losses under historical scenarios (e.g., 1987 crash, 2008 crisis) or hypothetical scenarios (e.g., a 50% stock market decline, a sudden 200-basis-point rate spike). These scenarios explicitly model regime change, correlation breakdown, and liquidity collapse—all things the square root rule misses.

A bank's capital buffer must cover both the ten-day Basel VaR *and* the worst-case losses under stress scenarios, whichever is larger. This dual requirement provides a more realistic safety margin.

## Choosing Holding Period for Your Portfolio

For individual investors or non-regulated entities, the choice of holding period should match reality:

- If you actively trade and can exit most positions within hours, use a one-day or two-day horizon.
- If you rebalance weekly or hold positions for months, use a weekly or monthly horizon.
- If you hold illiquid investments (real estate, private equity), extend the horizon to match the actual liquidation time.

Then scale [volatility](/annualizing-volatility-square-root-of-time/) using the square root rule, but add a stress-test layer. Calculate what losses you would suffer under a historical crisis (e.g., 2008), and ensure your risk budget accommodates both the scaled VaR and the worst-case scenario. This two-pronged approach is more robust than relying on a single formula.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at risk](/value-at-risk/) — Core risk metric; holding period is a key parameter
- [Annualizing volatility using square root of time](/annualizing-volatility-square-root-of-time/) — The volatility scaling formula underlying VaR scaling
- [EWMA volatility model](/ewma-volatility-model/) — Standard volatility estimator for Basel VaR
- [Rolling window volatility estimation](/rolling-window-volatility-estimation/) — Alternative volatility input for VaR
- [Stress testing](/stress-testing/) — Captures regime shifts and tail risk missed by scaling formulas
- [Expected shortfall](/value-at-risk/) — Average loss beyond VaR threshold; also horizon-dependent

### Wider context

- [Market risk](/market-risk/) — Systematic losses from adverse price movement
- [Counterparty risk](/counterparty-risk/) — Credit exposure during extended holding periods
- [Liquidity risk](/liquidity-risk/) — Risk of large market impact or inability to liquidate
- [Basel Committee](/dodd-frank-act/) — Regulatory framework governing bank capital and risk limits
- [Tail risk](/tail-risk/) — Extreme outcomes beyond typical [volatility](/volatility-smile/) estimates

</div>

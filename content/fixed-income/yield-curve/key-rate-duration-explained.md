---
title: "Key Rate Duration: Measuring Yield Curve Risk by Maturity"
description: "Key rate duration measures a portfolio's sensitivity to yield changes at specific curve points, isolating risk at each maturity rather than assuming parallel shifts."
keywords:
  - key rate duration explained
  - partial duration
  - yield curve risk
  - key rate duration portfolio
image: "/svg/fixed-income.svg"
---

*A **key rate duration**—also called partial duration—measures how sensitive a bond or portfolio is to a yield change at a specific point on the [yield curve](/yield-curve/), holding other maturities constant. Unlike overall [duration](/), which assumes the entire curve shifts in parallel, key rate duration isolates risk at each maturity, revealing which parts of the curve drive portfolio losses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Key Rate Duration — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Breaks curve risk into maturity buckets; reveals where portfolio bets actually live.</div>

|   |   |
|---|---|
| **What it is** | Sensitivity of portfolio value to a 1 basis point change in yield at one curve point |
| **Relationship to duration** | Sum of all key rate durations ≈ overall [duration](/duration/) |
| **Key rate points** | Typically 2y, 3y, 5y, 10y, 30y; banks use finer grids (1y, 2y, …, 30y) |
| **Example** | If 5-year key rate duration = 3, a 1% rise in 5-year yields drops portfolio value by ~3% |
| **Use case** | Identifying which curve segment poses the greatest risk to a portfolio |
| **Limitation** | Assumes other rates don't move; real markets have correlated curve shifts |

</aside>

## Why Overall Duration Is Not Enough

When a portfolio manager asks, "How much does my portfolio lose if rates rise?", a single [duration](/duration/) number gives only part of the answer. A portfolio with 5 years of overall duration could lose 5% if yields everywhere rise 1%, but that assumes the entire [yield curve](/yield-curve/) shifts in parallel—a rare event.

More often, the curve twists. Short-term rates might jump while long-term rates stay flat. Or a single part of the curve—the 10-year, for example—moves sharply while others inch. A portfolio full of 30-year bonds is far more exposed to a 30-year yield spike than a portfolio of 2-year bonds, yet a single duration number obscures this difference.

**Key rate duration** solves this by breaking the curve into segments and measuring sensitivity to each.

## How Key Rate Duration Works

Key rate duration isolates the portfolio's sensitivity to yield movements at specific maturity points along the curve. The standard framework defines key rates at eight points:

- 2-year
- 3-year
- 5-year
- 7-year
- 10-year
- 20-year
- 30-year

For each key rate, you calculate: **If the yield at that point rises by 1 basis point, holding all other yields constant, how much does the portfolio value fall?**

The answer is the key rate duration at that point.

### A Worked Example

Imagine a portfolio consisting of:
- $50 million of 2-year bonds (duration 1.9)
- $30 million of 10-year bonds (duration 8.2)
- $20 million of 30-year bonds (duration 15.1)

Overall duration is approximately 7.2 (a weighted average, very roughly).

But the key rate durations tell a richer story:

| Key Rate | Portfolio KRD |
|----------|---|
| 2-year | 3.1 |
| 3-year | 0.2 |
| 5-year | 0.1 |
| 10-year | 5.8 |
| 30-year | 2.1 |

This breakdown reveals:
- The portfolio has major exposure to the 2-year and 10-year points. Most risk lives there.
- The 3-year, 5-year portions are nearly neutral; those segments don't drive much P&L.
- A 1% rise in 10-year yields alone would drop the portfolio by ~5.8%, while a 1% rise in 3-year yields would drop it by only 0.2%.

A manager worried about long-duration risk would focus on 10-year and 30-year rate moves; a manager betting on a steepening [yield curve](/yield-curve/) (10-year yields rising while 2-year yields fall) would use key rate durations to isolate that specific exposure.

## Building the Key Rate Duration Ladder

In practice, risk managers compute key rate durations using a pricing model:

1. **Build a yield curve model.** Start with current yields at all standard maturities (2y, 3y, 5y, etc.).
2. **Bump each key rate by 1 basis point (0.01%).** Shift only that one point; interpolate or hold other points constant (the convention varies by vendor).
3. **Reprice the portfolio** under each bumped scenario.
4. **Measure the change.** The price change under a 1 bp bump at each key rate = that key rate's duration (scaled).

Different risk vendors (Bloomberg, Refinitiv, bank internal systems) use slightly different curve-building and interpolation methods, so key rate durations can vary between systems. The standardized conventions exist, but implementation details matter.

## Sum of Key Rate Durations ≈ Overall Duration

A crucial property: **the sum of all key rate durations approximately equals the overall [duration](/duration/)** of the portfolio.

In the example above:
- Sum of KRDs = 3.1 + 0.2 + 0.1 + 5.8 + 2.1 = 11.3 (simplified; actual grid has 8 points)
- Overall duration ≈ 7.2

The mismatch occurs because key rate durations are computed under hypothetical single-maturity shifts, which is unrealistic. In real market moves, rates at different maturities move together with varying magnitudes. But the property still holds approximately and helps validate a risk system.

## Why Banks and Portfolio Managers Use Key Rate Duration

1. **Stress testing.** A mortgage bank's deposit-funding model might show: "If the 2-year rate spikes 50 bps while 10-year rates stay flat, our margin narrows by X." Key rate durations quantify those specific scenarios.

2. **Curve positioning.** A fixed-income trader with a bet on a curve flattening (long-duration at long end, short at short end) uses key rate durations to ensure the portfolio has the intended shape without unwanted parallel-shift risk.

3. **Hedging.** To hedge a 10-year rate risk precisely, a manager uses the 10-year key rate duration to calculate how many 10-year [Treasury futures](/treasury-bond/) to short, rather than relying on an average duration that muddles short and long risks.

4. **Regulatory capital.** [Interest-rate risk](/interest-rate-risk/) capital models (e.g., CCAR, [CAALM](/)) decompose curve risk into key rate buckets to ensure banks aren't concentrated in one maturity segment.

## Limitations and Practical Considerations

Key rate duration assumes **other rates don't move**, which is unrealistic. In practice:
- Rates at different maturities are correlated. If 5-year rates spike, 10-year rates typically rise too (though not by the same amount).
- The interpolation method for intermediate maturities (e.g., 4-year, 6-year) varies across vendors.
- In a liquidity crisis or flight-to-quality event, correlations break down, and key rate durations become less predictive.

For these reasons, sophisticated firms complement key rate duration with **scenario analysis**—modeling realistic curve shifts (e.g., "all rates up 50 bps"; "curve flattens 25 bps") and measuring portfolio impact.

## Complement: Effective Duration vs. Key Rate

Some bond types (callable bonds, mortgages with prepayment risk) have yields that change in nonlinear ways when rates move. For these, [effective duration](/duration/) (measured from actual price-yield data rather than assumed cashflow schedules) replaces traditional duration. Key rate durations for callable bonds use effective duration methods and can be less stable than those for plain-vanilla bonds.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — Overall measure of bond sensitivity to parallel yield shifts
- [Yield Curve](/yield-curve/) — The term structure that key rates map onto
- [Interest Rate Risk](/interest-rate-risk/) — How yields affect portfolio values
- [Swap Curve vs Treasury Curve](/swap-curve-vs-treasury-curve/) — The curves on which key rates are defined
- [Inverted Yield Curve and Bank Profitability](/inverted-yield-curve-bank-profitability/) — How curve shape (a key-rate matter) stresses bank earnings

### Wider context

- [Bond](/bond/) — Fixed-income securities whose prices key rate duration measures
- Fixed-Income — Asset class for which curve risk is central
- [Sensitivity Analysis Valuation](/sensitivity-analysis-valuation/) — Framework for stress-testing portfolios
- [Federal Reserve](/federal-reserve/) — Authority whose policy influences curve and key rates

</div>

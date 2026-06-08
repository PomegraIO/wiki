---
title: "Swap Curve vs Treasury Curve: Key Differences"
description: "Compares the interest-rate swap curve and Treasury curve: what they measure, why they diverge, and which curve professionals use as a benchmark."
keywords:
  - swap curve vs treasury curve
  - interest rate swap curve
  - swap spread benchmark
  - treasury curve comparison
image: "/svg/fixed-income.svg"
---

*The **swap curve vs Treasury curve** comparison is essential for fixed-income professionals. The Treasury curve prices risk-free government debt; the swap curve is built from [interest-rate swaps](/interest-rate-swap/) and reflects the cost of borrowing at floating rates plus a credit spread. The two diverge when credit stress rises or liquidity shifts, and **swap spreads**—the gap between the two—signal financial system health.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Curve vs Treasury Curve — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Swap curves embed credit risk; Treasuries do not. Spreads widen in stress and narrow in calm.</div>

|   |   |
|---|---|
| **Treasury curve** | Prices of government bonds; reflects risk-free rate for each maturity |
| **Swap curve** | Implied from interest-rate swaps; reflects SOFR-plus-spread pricing |
| **Swap spread** | Difference between swap rate and Treasury yield; signals credit/liquidity risk |
| **Why they diverge** | Banking crisis, tightening financial conditions, or supply/demand imbalance |
| **Typical spread range** | 0–50 bps in calm; 50–150+ bps in stress (2008 crisis exceeded 200 bps) |
| **Practitioner preference** | Swaps often more liquid; used as primary benchmark in many markets |
| **What spread tells you** | Higher spread = higher perceived credit risk or funding stress in banking system |

</aside>

## The Treasury Curve: The Baseline

The **Treasury curve** is the most fundamental [yield curve](/yield-curve/) in finance. It plots the [interest rates](/interest-rate/) on U.S. government bonds of different maturities—3-month, 2-year, 5-year, 10-year, 30-year—and represents the time value of money for a risk-free borrower (the U.S. government).

When an investor buys a 10-year Treasury, they lock in a known coupon and know they will be repaid in 10 years. The curve shows the premium (or discount) investors demand for lending longer; a steep upward curve means long-term investors demand a large yield premium over short-term rates.

The Treasury curve is the anchor for all other [bond](/bond/) pricing. Corporate bonds, [mortgages](/fixed-rate-mortgage-personal/), municipal bonds—all are quoted as spreads *over* Treasuries. A 10-year corporate bond might trade at "Treasury + 100 basis points," meaning it yields 1% more than the equivalent Treasury.

## The Swap Curve: A Credit-Adjusted Benchmark

The **swap curve** is constructed from [interest-rate swaps](/interest-rate-swap/) rather than bonds. In an interest-rate swap, two parties exchange payment streams: one pays a fixed rate, the other pays a floating rate (typically [SOFR](/sofr/) or another benchmark). The fixed rate in a swap for a given maturity defines that point on the swap curve.

Why use swaps? Because a swap is not a loan; it is a synthetic instrument in which the fixed-rate payer is economically equivalent to borrowing at a fixed rate in the swap market. A bank that pays fixed in a 10-year swap has effectively locked in a 10-year borrowing cost.

The key insight: **swaps embed credit risk**. When a bank enters a swap, the counterparty (the floating-rate payer) is exposed to the fixed-payer's credit. If the fixed payer defaults, the counterparty loses the future stream of fixed payments. Therefore, the fixed rate in a swap is higher than the Treasury rate at the same maturity—it includes the cost of counterparty credit risk.

## The Swap Spread: The Gap That Signals Stress

The **swap spread** is the difference between the swap curve and the Treasury curve at each maturity:

**Swap Spread = Swap Rate – Treasury Rate (at same maturity)**

In normal conditions, swap spreads are tight—typically 10 to 50 basis points. This reflects modest compensation for [credit risk](/credit-risk/) in the banking system (since the primary swap counterparties are banks).

But swap spreads widen dramatically during financial stress:
- **2008 financial crisis:** 10-year swap spreads exceeded 200 basis points as counterparty risk spiked.
- **March 2020 (COVID-19 shock):** Spreads widened to 100+ basis points in days as liquidity evaporated.
- **2023 regional bank stress:** Spreads widened as SVB and other bank failures raised systemic credit concerns.

When spreads blow out, it signals that the fixed-income market is pricing elevated risk of bank default or severe funding stress. Conversely, when spreads compress to near zero, it suggests confidence in the banking system and abundant liquidity.

## Why Practitioners Often Prefer the Swap Curve

Although the Treasury curve is risk-free, the swap curve has become the dominant benchmark for many fixed-income markets, especially among large institutions:

1. **Liquidity.** Swap markets are deep and active. Treasury markets are liquid, but swap volumes (especially mid-curve maturities) often exceed Treasury volumes.

2. **Corporate issuance benchmark.** Corporations borrow by issuing bonds at spreads to the swap curve, not Treasuries. A company pricing a 5-year bond quotes it as "swap + 80 bps," not "Treasury + 80 bps." This convention makes the swap curve the natural reference.

3. **Hedging efficiency.** A large borrower or portfolio manager often hedges interest-rate exposure with swaps, not Treasuries. The swap curve is the natural hedge for swap market participants.

4. **Standardization.** Swap conventions are standardized globally. Treasury curves vary by country; the U.S. Treasury curve does not apply to European or Asian borrowers.

## How the Two Curves Diverge Beyond Spreads

Beyond the swap spread, the curves can shape differently:

- **Level shifts.** In a [monetary policy](/monetary-policy/) tightening, the Federal Reserve raises short-term [interest rates](/interest-rate/). Swap and Treasury curves both shift upward, but short-end rates on swaps may move faster than Treasury short-end rates because bank funding costs respond immediately to Fed action.

- **Slope changes.** A curve flattening (long-term rates falling relative to short-term) can occur at different speeds on the swap curve vs. the Treasury curve. If long-term [credit risk](/credit-risk/) premia compress faster than long-term real growth expectations change, the swap curve flattens more than the Treasury curve.

- **Supply imbalances.** Massive Treasury issuance (e.g., government deficits) can depress long-term Treasury yields without affecting swap rates equally, if the supply is absorbed domestically by banks. This can invert the typical relationship.

## Which Curve for What Purpose?

- **Policy rates and economic expectations:** Watch the **Treasury curve** to gauge the market's view of [Fed funds](/federal-funds-rate/) paths and real growth.
- **Corporate and bank funding costs:** Watch the **swap curve** to see where non-government borrowers actually fund.
- **Financial stability:** Watch the **swap spread** to gauge systemic credit and liquidity conditions.
- **Relative value:** Compare the two; if swap spreads are unusually tight, it may signal complacency about banking system risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield Curve](/yield-curve/) — Overview of term structure and economic signaling
- [Interest-Rate Swap](/interest-rate-swap/) — Definition and mechanics of the instrument underlying the swap curve
- [SOFR](/sofr/) — The floating-rate benchmark that replaced LIBOR in modern swaps
- [Inverted Yield Curve and Bank Profitability](/inverted-yield-curve-bank-profitability/) — How curve inversion stresses swap and Treasury spreads together
- [Key Rate Duration Explained](/key-rate-duration-explained/) — How to measure rate risk along either curve

### Wider context

- [Bond](/bond/) — Fixed-income securities priced relative to curves
- [Interest Rate Risk](/interest-rate-risk/) — How curve shifts affect portfolio values
- [Federal Reserve](/federal-reserve/) — The authority that shapes policy rates and curve expectations
- [Credit Risk](/credit-risk/) — The risk that defines swap spreads

</div>

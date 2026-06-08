---
title: "Conditional Prepayment Rate (CPR) Explained"
description: "Conditional Prepayment Rate (CPR) is an annualized measure of how fast borrowers prepay loans. It converts monthly prepayment speed (SMM) into a yearly percentage used to project bond cash flows."
keywords:
  - conditional prepayment rate explained
  - CPR prepayment speed
  - SMM to CPR conversion
  - prepayment assumption securitization
  - annualized prepayment rate
---

*The **Conditional Prepayment Rate (CPR)** is a standardized way to express how fast borrowers are paying off loans ahead of schedule, converted into an annualized percentage. It is used in securitization to project future cash flows: a 6% CPR means that, if the prepayment pace holds steady, 6% of the remaining pool balance will be prepaid each year. CPR and its monthly sibling, the Single Monthly Mortality (SMM), are linked by a formula; different CPR assumptions produce vastly different bond [cash flows](/cash-flow-statement/) and maturities.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Conditional Prepayment Rate (CPR) Explained — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income and structured products." />

<div class="wiki-infobox-caption">A single metric that captures borrower behavior and reshapes a bond's life.</div>

|   |   |
|---|---|
| **Definition** | Annualized percentage of remaining balance prepaid in a year |
| **Formula** | CPR = 1 − (1 − SMM)^12 |
| **Inverse formula** | SMM = 1 − (1 − CPR)^(1/12) |
| **Typical range** | 2–12% for mortgage pools; varies by rate environment |
| **Key driver** | Interest rate differential (borrowers refinance when rates fall) |
| **Data source** | Historical speeds from servicers or MBS indices (Public Securities Association PSA) |
| **Impact on bonds** | Higher CPR = faster payoff, shorter [weighted average life](/weighted-average-life-abs/), lower extension risk |

</aside>

## From Monthly Speed to Annualized Rate

When a borrower pays off a mortgage or auto loan faster than the scheduled amortization, that is a **prepayment**. Servicers track the percentage of the pool's beginning balance that prepays each month, called the **Single Monthly Mortality (SMM)** or monthly speed.

If a mortgage pool has $100 million outstanding at the start of a month and $2 million prepays during that month (ignoring scheduled principal), the SMM for that month is 2%. That seems small, but if it happens every month, it compounds.

To convert this monthly pace into an annual figure, the formula is not simply to multiply by 12 (which would give 24% and overstate the true effect). Instead, we use the **conditional prepayment rate** formula:

**CPR = 1 − (1 − SMM)^12**

If SMM is 2% per month:

CPR = 1 − (1 − 0.02)^12
CPR = 1 − (0.98)^12
CPR = 1 − 0.7837
CPR = 0.2163, or 21.63%

This 21.63% CPR is the annualized rate that, if held steady month over month, would produce the observed monthly speed.

Going the other direction, if you know CPR and want to find the implied SMM:

**SMM = 1 − (1 − CPR)^(1/12)**

For a 6% CPR:

SMM = 1 − (1 − 0.06)^(1/12)
SMM = 1 − (0.94)^(0.0833)
SMM = 1 − 0.9949
SMM ≈ 0.51%, or about 0.5% per month

This relationship means that small monthly speeds compound into surprisingly large annual rates, and vice versa.

## Why CPR Matters for Bond Investors

A [mortgage-backed security](/mortgage-backed-security/) or auto loan ABS promises to return principal over time, but the timing is uncertain. If CPR is 2%, the pool prepays slowly, and investors get a long stream of payments (good if they want a long duration, bad if rates rise). If CPR is 12%, the pool races to payoff, cash returns sooner (good if rates are falling, bad if they rise—cash is reinvested at lower rates).

This uncertainty is called **prepayment risk** or **extension/contraction risk**. It is not systematic risk; it is a result of borrower behavior and interest rate movements.

Bond traders use CPR assumptions to model cash flows. A typical projection might assume:

- **Base case**: 6% CPR throughout the life of the pool
- **Upside case**: 20% CPR (borrowers are eager to refinance or sell)
- **Downside case**: 2% CPR (rates are high; prepayment is low)

For each scenario, the modeler calculates when principal returns and computes the bond's yield and effective [duration](/duration/).

## What Drives CPR: The Refinancing Effect

The single biggest driver of CPR is **interest rates**. When mortgage rates fall significantly below the coupon borrowers are paying, they refinance. A homeowner with a 5% mortgage refinances to 3%, saves money on the monthly payment, and prepays the old loan at par (plus costs).

Historical data shows a strong empirical relationship:

- When the refinancing incentive (current rate minus mortgage coupon) is 1%, CPR might be 4–6%.
- When the incentive is 2–3%, CPR might be 10–15%.
- When the incentive is above 3–4%, CPR can spike to 20%+ (borrowers rush to refinance before rates drift back up).

When rates rise above the coupon, the refinancing incentive disappears, and CPR can drop to 1–3% (borrowers move or let rates stabilize before paying down).

This is why mortgage-backed bond yields reflect prepayment risk: a bond with a 3% coupon offers higher yield than a comparable risk-free bond, compensating investors for the fact that if rates fall, prepayments accelerate and investors' attractive return is shortened.

## The Public Securities Association (PSA) Speed Benchmark

The **PSA model** is an industry standard for forecasting prepayment speeds. It defines "100% PSA" as a gradual ramp-up in CPR from 0.2% in month 1 to 6% by month 30, then flat 6% thereafter. This pattern roughly matches historical prepayment behavior in the absence of strong refinancing incentives.

Traders will say a mortgage pool is trading at "150% PSA" if speeds are expected to be 150% of the PSA curve—i.e., 0.3% CPR in month 1, 9% CPR by month 30, then 9% flat.

The PSA model lets traders quickly communicate assumptions without spelling out every month's CPR.

## CPR Assumptions and Cash Flow Projections

To see how CPR drives outcomes, consider a simple $100 million mortgage pool with a 3% pass-through coupon, 30-year remaining term, and 3% weighted-average coupon on the underlying loans:

| Assumption | Monthly payment (avg) | Total principal in year 1 | Scheduled + prepaid principal year 1 |
|---|---|---|---|
| 2% CPR (slow) | $423.5K | $5.1M | $7.2M |
| 6% CPR (baseline) | $423.5K | $5.1M | $11.8M |
| 12% CPR (fast) | $423.5K | $5.1M | $22.5M |

At 2% CPR, the pool returns principal slowly; noteholders have a long duration and are exposed to extension risk (if rates rise, the bonds don't shorten up quickly). At 12% CPR, investors get their principal back fast; if rates fall further, they face contraction risk (they must reinvest proceeds at lower rates).

This is why securitizations are typically modeled across a range of CPR scenarios, and why professional investors care deeply about their CPR assumption.

## CPR and Weighted Average Life

The CPR assumption directly determines a bond's [weighted average life (WAL)](/weighted-average-life-abs/), the time-weighted average date on which principal is repaid.

A higher CPR shortens WAL. A lower CPR extends it.

For a 3% coupon, 30-year mortgage pool:
- At 2% CPR: WAL ≈ 18–20 years
- At 6% CPR: WAL ≈ 7–9 years
- At 12% CPR: WAL ≈ 3–4 years

This matters enormously for investors comparing bonds. Two mortgage-backed bonds issued from the same pool might have nominally identical coupons and origination, but different WAL estimates if market expectations for CPR diverge.

## CPR in Different Rate Environments

CPR is not constant. Historical data shows:

- **Falling rate environment** (rates declining): CPR accelerates as refinancing incentives grow. Pools can move from 4% to 15% CPR within months.
- **Stable rate environment**: CPR stabilizes near the PSA baseline, usually 5–8%.
- **Rising rate environment** (rates climbing): CPR decelerates as refinancing appeal evaporates. Pools can slow from 8% to 1–2% CPR.

A borrower's propensity to prepay also depends on whether they have a recent refinance (less likely to refi again soon), their home equity (positive equity supports refinancing), and their income stability (job loss reduces ability to refi). These "seasoning" effects cause CPR to decline naturally over time, even in stable rate environments.

## See also

<div class="wiki-seealso">

### Closely related

- [Weighted Average Life in Asset-Backed Securities](/weighted-average-life-abs/) — The bond maturity metric that CPR determines
- [Mortgage-Backed Security](/mortgage-backed-security/) — The most common securitization where CPR is critical
- [Prepayment Risk](/prepayment-risk/) — The investment uncertainty CPR quantifies
- [Duration](/duration/) — How CPR affects bond price sensitivity
- [Interest Rate Risk](/interest-rate-risk/) — The driver of refinancing behavior and CPR changes

### Wider context

- [Securitization](/securitization/) — The structure within which CPR is modeled
- Asset-Backed Security — All ABS pools have a prepayment component
- [Bond](/bond/) — Bonds backed by prepayable assets must price in CPR risk
- Yield — CPR assumptions determine the true yield to investor

</div>

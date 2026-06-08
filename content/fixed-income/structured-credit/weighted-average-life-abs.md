---
title: "Weighted Average Life in Asset-Backed Securities"
description: "Weighted Average Life (WAL) in asset-backed securities is the time-weighted average date on which a tranche's principal is repaid, varying with prepayment and loss scenarios."
keywords:
  - weighted average life asset backed securities
  - WAL ABS calculation
  - weighted average maturity securitization
  - bond maturity uncertainty
  - prepayment assumption WAL
---

*The **Weighted Average Life (WAL)** in an asset-backed security is the effective maturity of a bond tranche, calculated by weighting each dollar of principal repayment by the number of years until it is returned. Unlike a straight bond with a fixed maturity date, an ABS tranche matures early if borrowers prepay, or late if borrowers default and take longer to liquidate—so WAL is a range, not a fixed point, and depends heavily on the assumed [Conditional Prepayment Rate (CPR)](/conditional-prepayment-rate-explained/) and loss scenarios.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Weighted Average Life in Asset-Backed Securities — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income and structured products." />

<div class="wiki-infobox-caption">The true maturity of a bond backed by prepayable collateral is always uncertain.</div>

|   |   |
|---|---|
| **Definition** | Time-weighted average of all principal repayment dates |
| **Formula** | Σ (Principal payment_t × Years until repayment) / Total principal |
| **Typical range** | 2–15 years for mortgage/auto pools (varies with CPR) |
| **Key driver** | Prepayment speed; loss severity affects senior vs. subordinate WAL differently |
| **Stability** | High CPR = short WAL (contraction risk); low CPR = long WAL (extension risk) |
| **Comparison** | Legal maturity is often 30 years; WAL is typically 5–10 years |
| **Investor use** | Matches portfolio duration targets; prices bonds accordingly |

</aside>

## Why WAL Exists: The Prepayment Problem

A traditional 30-year corporate bond has a maturity date. Investors know the bond will be repaid on a specific day, 30 years out (barring default). An asset-backed security backed by mortgages, auto loans, or credit card receivables has a stated legal maturity, but the **actual** repayment date depends on how fast borrowers pay down the collateral.

If borrowers prepay quickly, principal returns sooner than the legal maturity. If they prepay slowly, principal returns much later. And if defaults are severe, subordinate tranches may not receive their full allocation until near the legal maturity date or even get written down.

**Weighted Average Life** is a practical compromise: it estimates the average date on which a tranche's principal will be returned, given an assumed prepayment and loss scenario.

## The Calculation: A Simple Example

Suppose a mortgage pool of $10 million with a 30-year legal maturity will prepay at 6% CPR and assume no losses. A [trustee](/trustee-role-in-securitization/) models the month-by-month principal payments.

The calculation proceeds month by month:

| Month | Years elapsed | Scheduled principal | Prepaid principal | Total principal | Running balance |
|---|---|---|---|---|---|
| 1 | 0.083 | $25K | $50K | $75K | $9.925M |
| 2 | 0.167 | $25K | $49K | $74K | $9.851M |
| 3 | 0.25 | $25K | $49K | $74K | $9.777M |
| … | … | … | … | … | … |
| 120 (10 yrs) | 10.0 | $25K | $40K | $65K | $5.2M |

(This is a simplified illustration; real pools have thousands of loans with varying coupon and maturity.)

Each month's principal is weighted by its timing. Then all weighted principal amounts are summed and divided by total principal:

**WAL = Σ (Principal_t × Years_t) / Total principal**

For this pool, if the total principal repaid across 120 months (10 years) is $10 million, and the weighted-timing sum is $57 million "principal-years," then:

WAL = $57M / $10M = 5.7 years

This means the average dollar of principal is returned after 5.7 years. Some dollars come back in year 1; some in year 8. The weighted average is 5.7.

## WAL Under Different CPR Scenarios

The same pool with different CPR assumptions produces different WALs:

| CPR assumption | Monthly prepayment (avg) | WAL (years) | Interpretation |
|---|---|---|---|
| 2% (slow) | ~0.17% | 11–13 | Borrowers prepay slowly; principal extends far out |
| 6% (baseline) | ~0.51% | 5–7 | Baseline expectation; moderate life |
| 12% (fast) | ~1.0% | 2–4 | Borrowers eager to prepay; principal returns quickly |

This sensitivity is critical: if an investor models the pool at 6% CPR and buys the bond assuming a 6-year WAL, but CPR turns out to be 2%, the WAL effectively becomes 12 years—a significant extension of duration, with real impact on portfolio risk.

## How Loss Scenarios Affect WAL

Losses complicate the calculation, particularly for subordinate tranches. Consider a two-tranche securitization:

- **Senior tranche**: $80 million at 2.5% coupon
- **Subordinate (mezzanine) tranche**: $20 million at 5% coupon

If prepayments are 6% CPR and losses are zero, the senior tranche might have a WAL of 5.8 years and the subordinate tranche a WAL of 6.1 years (the mezzanine trail the senior slightly, but both principal streams are intact).

But if cumulative losses reach 8% of the pool (a common assumption for subprime mortgages), the senior tranche is unaffected: its $80M is fully protected by the subordinate's $20M buffer. But the subordinate tranche is hit hard. If $8M of principal is lost, the subordinate receives only $12M of its promised $20M, and that $12M trickles back over whatever timeline the servicer can recover or liquidate collateral.

In this scenario:

- **Senior WAL**: Still ~5.8 years (protected from loss)
- **Subordinate WAL**: Might extend to 9–12 years, if losses drag out the liquidation timeline

Or the subordinate might be entirely wiped out, with a WAL of 0 (no principal returned at all).

## WAL vs. Legal Maturity

The indenture always specifies a legal maturity—often 30 years for mortgages, 10 years for auto loans. But WAL is almost always shorter than legal maturity, because some principal is always repaid before the legal maturity date.

For example:

| Security type | Legal maturity | Typical WAL (6% CPR) | Differential |
|---|---|---|---|
| Mortgage-backed bond | 30 years | 5–7 years | 23–25 years shorter |
| Auto loan ABS | 10 years | 3–5 years | 5–7 years shorter |
| Credit card receivables | 12 years | 2–4 years | 8–10 years shorter |

The legal maturity acts as a backstop: if all collateral prepays at par or defaults and is recovered quickly, principal returns by that date. WAL estimates when it actually comes back under normal conditions.

## WAL and Investor Matching

Professional bond investors use WAL to match portfolio duration targets. A pension fund with a 6-year liability wants bonds with a 6-year average life. A 30-year mortgage-backed bond with a 6-year WAL fits that need better than a 30-year corporate bond (which truly has 30 years of duration).

But WAL is an estimate. If prepayment speeds turn out differently than expected:

- **Faster CPR than expected**: Bond matures earlier (contraction risk). Investor gets principal back sooner and must reinvest at potentially lower rates.
- **Slower CPR than expected**: Bond extends (extension risk). Investor's duration is longer than planned, and their portfolio is exposed to rate risk longer than intended.

This duration uncertainty is one reason ABS carry higher yields than equivalent-duration risk-free bonds: investors demand compensation for the prepayment risk that creates WAL volatility.

## Modeling and Sensitivity Analysis

Securitization underwriters and [rating agencies](/credit-rating/) use scenario analysis to show WAL across a range of CPR and loss assumptions:

**WAL sensitivity table** (10-year mortgage pool, senior tranche):

| Loss scenario | 2% CPR | 6% CPR | 12% CPR |
|---|---|---|---|
| 0% loss | 12.1 yrs | 5.8 yrs | 2.9 yrs |
| 3% loss | 12.3 yrs | 5.9 yrs | 3.0 yrs |
| 6% loss | 12.5 yrs | 6.0 yrs | 3.1 yrs |

This table shows investors the range of possible maturities. A conservative investor might price the bond for the extended scenario (12% CPR, 6% loss, yielding a 3.1-year WAL). An aggressive investor might assume 2% CPR and 0% loss, accepting a 12.1-year WAL and commensurately longer duration risk.

## The 2008 Lesson: When WAL Forecasts Fail

Before the mortgage crisis, underwriters modeled mortgage-backed WALs assuming 6% CPR and historical loss rates (1–2%). Actual results proved far different. As defaults spiked and home prices crashed, borrowers could not refinance or sell. CPR plummeted to 1–3%, extending WAL dramatically. Simultaneously, losses exceeded 15–20%, wiping out subordinate tranches entirely.

Investors who bought senior bonds expecting a 5-year WAL found themselves holding 12-year duration exposure in a rising-rate environment—a painful mismatch. The crisis showed that WAL, while useful, is only as good as the assumptions behind it, and that extreme scenarios can break historical models.

## See also

<div class="wiki-seealso">

### Closely related

- [Conditional Prepayment Rate (CPR) Explained](/conditional-prepayment-rate-explained/) — The prepayment speed that determines WAL
- [Trigger Events in Structured Finance](/trigger-event-structured-finance/) — Performance thresholds that can affect WAL via cash flow diversion
- [Duration](/duration/) — The interest-rate sensitivity measure that WAL approximates for ABS
- [Mortgage-Backed Security](/mortgage-backed-security/) — The most common application where WAL is critical

### Wider context

- [Securitization](/securitization/) — The structure within which WAL is calculated
- Asset-Backed Security — General framework for collateral-backed bonds
- [Prepayment Risk](/prepayment-risk/) — The fundamental risk that makes WAL uncertain
- [Tranche](/tranche/) — Different tranches in the same pool have different WALs
- [Extension Risk](/extension-risk/) — The risk that actual WAL exceeds expected WAL

</div>

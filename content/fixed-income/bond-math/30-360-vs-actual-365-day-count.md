---
title: "30/360 vs Actual/365 Day Count: Which Bonds Use Which"
seo_title: "30/360 vs Actual/365: Which Bonds Use Which Day Count"
description: "30/360 assumes 30-day months and a 360-day year; Actual/365 counts real days. Which bond markets use each and how the choice shifts accrued interest."
keywords:
  - 30/360 vs actual/365 day count convention
  - bond day count convention
  - accrued interest day-count method
  - 30/360 actual/365 bonds
  - bond yield day count basis
image: /svg/fixed-income.svg
---

*The **day-count convention** determines how many days elapse in an interest period, which directly affects accrued interest, yield calculations, and cash flows. The two dominant conventions are **30/360** (each month has 30 days, each year 360) and **Actual/365** (actual number of calendar days, 365-day year), with different bond markets applying each.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">30/360 vs Actual/365 Day Count — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Day-count convention choice is market-specific and embedded in bond terms; it shifts interest and yield calculations slightly but visibly.</div>

|   |   |
|---|---|
| **30/360 uses** | 30 days per month; 360 days per year (fixed) |
| **Actual/365 uses** | Actual calendar days; 360 or 365 depending on leap years |
| **30/360 common in** | Corporate bonds, municipal bonds, agency bonds (US) |
| **Actual/365 common in** | Government bonds (UK, Eurozone), many [treasury-bills](/treasury-bill/) |
| **Impact on accrual** | 1–2% difference over a full year depending on coupon dates |
| **Industry standard** | Set in bond indenture; rarely negotiable |

</aside>

## The Role of Day-Count Conventions

Every [bond](/bond/) is issued with a [coupon rate](/coupon-rate/) and a **coupon-payment schedule** (e.g., semi-annual or quarterly payments). The coupon payment is calculated as:

**Coupon Payment = (Coupon Rate × Face Value × Days in Period) / Days in Year**

The "days in period" and "days in year" components depend on the day-count convention. A change in the convention shifts the coupon payment and the accrued interest owed to the previous bondholder at settlement. This is why conventions are standardized and explicitly stated in the bond indenture—they are not negotiable details; they are embedded in the contract.

## The 30/360 Convention Explained

**30/360**—sometimes called "30/360 US" or "bond basis"—treats every month as having exactly 30 days and every year as having exactly 360 days. This simplification makes hand calculations easy and was the market standard before electronic trading.

The rule works as follows:

- Every month, regardless of its true length (28, 29, 30, or 31 days), counts as 30 days.
- If the start date is the 31st of a month, adjust it down to the 30th.
- If the end date is the 31st of a month (and the start date is the 30th or 31st), adjust the end date down to the 30th.
- Exception: If the coupon period includes February and the bond is due at maturity on the last day of February, leave the end date as the last day of February.

**Example**: A bond has a semi-annual coupon. The coupon period is from March 15 to September 15. Using 30/360:
- Start: March 15
- End: September 15
- Days elapsed: (30 - 15) + 30 + 30 + 30 + 30 + 30 + 15 = 180 days (exactly)
- Days in year: 360
- Coupon payment: (Annual Coupon Rate × Face Value × 180) / 360 = Coupon Rate × Face Value / 2

The semi-annual payment is exactly half the annual coupon, which is tidy and intuitive.

## The Actual/365 Convention Explained

**Actual/365**—used in UK government bonds and many eurozone instruments—counts the *actual* number of calendar days between coupon dates and divides by 365 (or by 366 in leap years, depending on the variant). This method is more "real" but less convenient for mental math.

The rule:

- Count every calendar day from the start date to the end date (inclusive of start, exclusive of end, or by market convention).
- Divide by 365 for a regular year; by 366 if February 29 falls in the period.
- Some markets use Actual/360 instead, which counts actual days but divides by 360.

**Example**: The same bond maturing from March 15 to September 15, using Actual/365:
- March 15 to March 31: 16 days
- April 1 to 30: 30 days
- May 1 to 31: 31 days
- June 1 to 30: 30 days
- July 1 to 31: 31 days
- August 1 to 31: 31 days
- September 1 to 15: 15 days
- Total: 184 actual calendar days
- Coupon payment: (Annual Coupon Rate × Face Value × 184) / 365

The semi-annual payment is slightly higher (184/365 ≈ 0.5041 of the annual coupon) because the actual period has slightly more days than the 180 days assumed under 30/360.

## Market-Specific Usage

**US Corporate Bonds**: Virtually all use 30/360. This is the default for bonds issued under US law and is deeply embedded in market conventions. Bond traders assume 30/360 unless told otherwise.

**US Municipal Bonds**: Also 30/360, with some exceptions. Some older or specialized municipal instruments use other conventions, but the market baseline is 30/360.

**US Agency Bonds**: [Fannie Mae](/fannie-mae/), [Freddie Mac](/freddie-mac/), and other US agencies typically use Actual/360 (actual days, 360-day year) rather than 30/360. This is a middle ground and reflects these agencies' role in mortgage markets, where Actual/360 is common.

**UK Government Bonds (Gilts)**: Use Actual/Actual (the actual number of days, with the year divided into actual calendar year lengths). This is different from Actual/365 but similar in spirit.

**European Government Bonds**: Many use Actual/365 Fixed (actual days, divided by 365 even in leap years) or Actual/Actual per ISDA convention.

**Money-Market Instruments** ([Treasury Bills](/treasury-bill/), commercial paper): Often use Actual/360, counting actual days and dividing by 360.

## Impact on Accrued Interest and Yield

Because different conventions count days differently, they affect:

**Accrued Interest**: When a bond is sold between coupon dates, the buyer must pay the seller accrued interest—the fraction of the coupon earned from the last coupon date to the settlement date. Using 30/360 vs. Actual/365 changes this accrued amount by roughly 1–2% per quarter, or more over longer periods.

**Yield Calculation**: A bond quoted with a [yield-to-maturity](/yield-to-maturity/) (YTM) assumes a particular day-count convention. A US corporate bond quoted at a 4.5% YTM uses 30/360; if the same cash flows were valued using Actual/365, the quoted yield would differ slightly (typically by 5–15 basis points, depending on coupon dates and time to maturity).

This is why traders must always specify the convention when quoting or trading a bond. Quoting a price without the convention is ambiguous—the true economic value depends on the day count.

## Historical Context and Standardization

The **30/360 convention originated** in the 1920s as a practical simplification for manual calculation. With 30-day months and 360-day years, periodic interest could be divided easily by 2 (semi-annual) or 4 (quarterly). It became entrenched in US bond markets and remains the default.

**Actual/365 and variants** became the standard in non-US markets and in money-market instruments. The UK's use of Actual/Actual reflects both market tradition and the fact that the UK Treasury's coupon periods sometimes align with half-years ending on March 31 and September 30, making actual-day counting more natural.

Over the past 30 years, electronic trading has made the computational convenience of 30/360 largely irrelevant. Yet conventions have not converged; instead, they have hardened into market silos. A US corporate-bond trader assumes 30/360 without asking. A London gilt trader assumes Actual/Actual. Trying to trade across these markets requires explicit convention translation.

## Practical Implications for Bond Investors

**Yield comparisons**: When comparing the yield on a US corporate bond (30/360) to a UK government bond (Actual/Actual), the quoted yields are not directly comparable until both are converted to a common convention. A 4.5% US corporate yield is not the same as a 4.5% gilt yield.

**Pricing and settlement**: Day-count convention must be specified in every trade. If buyer and seller disagree on the convention, the settlement price is wrong.

**Floating-rate notes**: These often use Actual/360 or Actual/365, tied to benchmark [interest rates](/interest-rate/) that use the same convention. Matching the convention to the benchmark ensures consistency in interest payments.

**Historical bond data**: Research databases may convert historical bond prices to a single convention for comparability, but the original convention should be noted.

## See also

<div class="wiki-seealso">

### Closely related

- [Coupon Payment](/coupon-payment/) — the periodic interest that day-count conventions help calculate
- [Coupon Rate](/coupon-rate/) — the stated annual rate that is adjusted by day-count method
- [Yield-to-Maturity](/yield-to-maturity/) — the return metric that depends on the day-count convention used
- [Accrued Interest](/accrued-interest/) — the seller's benefit from partial-period interest, calculated via day-count convention
- [Bond](/bond/) — the instrument whose terms embed the day-count convention

### Wider context

- [Treasury Bill](/treasury-bill/) — money-market instrument with its own day-count norms
- [Interest Rate](/interest-rate/) — the benchmark tied to a day-count convention for floating-rate notes
- Fixed-Income — the broader market context where conventions vary by region and asset class
- [Basis Risk](/basis-risk/) — the mismatch risk that can arise when hedging instruments use different conventions

</div>

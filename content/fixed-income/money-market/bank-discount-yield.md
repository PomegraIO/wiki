---
title: "Bank Discount Yield"
description: "A yield calculation method used for short-term instruments like T-bills and commercial paper, based on face value and a 360-day year."
keywords:
  - bank discount yield
  - treasury bill yield
  - discount rate
  - money market convention
  - yield calculation
image: "/svg/fixed-income.svg"
---

*The **bank discount yield** is a standardised method of quoting returns on short-term debt instruments such as [Treasury bills](/treasury-bill/), [commercial paper](/corporate-bond/), and [agency discount notes](/agency-discount-note/). It expresses the annualised return as a simple discount from [par value](/par-value/), rather than the actual dollar return an investor receives, and assumes a 360-day year rather than 365.*

## Why a special convention exists

The [money market](/treasury-bill/) developed its own language because traders needed speed and consistency. When you quote the price of a long-term [bond](/bond/), you specify a yield-to-maturity or a [current yield](/current-yield/); both require compounding and are tied to the actual cash flows. But in the money market, where instruments mature in weeks, traders wanted a quick, visual way to compare rates across different maturities without a calculator. The bank discount yield was born: a simple, one-line quote that lets a dealer say "T-bills at 5.40 bid, 5.38 ask" and everyone understands immediately. The 360-day convention is a historical oddity, but it stuck—financial markets are, above all, creatures of habit.

## How the calculation works

Bank discount yield is calculated as:

Discount Yield (%) = (Discount / Face Value) × (360 / Days to Maturity) × 100

Suppose you buy a $10 million Treasury bill maturing in 91 days at a discount yield of 5.25%. The discount amount is:

Discount = $10,000,000 × 0.0525 × (91/360) = $132,291.67

You pay $10,000,000 − $132,291.67 = $9,867,708.33 today and receive $10,000,000 at maturity. Your actual dollar gain is $132,291.67. But the quoted yield (5.25%) is *not* your true [return-on-assets](/return-on-assets/). That is the point: the market speaks in discount terms, not economic terms. Traders recite the discount yield; investors must translate it to know what they actually earn.

## The mathematical gap: discount vs. bond equivalent yield

Here is where practitioners stumble. The bank discount yield systematically understates the true annualised return because it uses face value (not the purchase price) as the denominator and assumes 360 days (not 365). The same instrument quoted at 5.25% bank discount yield has a higher true [bond equivalent yield](/current-yield/). For a 91-day bill, the bond equivalent yield would be roughly 5.38%—about 13 basis points higher. The gap widens for longer maturities; it shrinks for shorter ones.

Why does anyone tolerate this? Because the convention is universal within short-dated debt markets. Everyone knows the gap exists and translates unconsciously. A portfolio manager thinking "I want 5.5% annualised return" will immediately ask for the bank discount equivalent (roughly 5.37%) and move on. The convention is a feature, not a bug—it collapses otherwise wordy comparisons into a single number.

## Treasury bills and the standard case

The [U.S. Treasury](/treasury-bill/) quotes all short-dated bills using the bank discount convention. When the Federal Reserve announces an auction of 91-day T-bills, bidders submit discount yields. The Treasury then converts the high bid into a price, pays that price in new securities, and everyone settles at what is called the "investment yield"—a slightly different calculation that bridges to the bond equivalent yield. But the auction itself, the talking, the trading—all in discount yield.

This is where most newcomers first encounter the convention. A Treasury auction result might read: "91-day bill awarded at 5.15% bank discount yield." A savvy investor thinks: "That's roughly 5.28% true yield; at current [inflation](/inflation/), my real return is modest." An inexperienced buyer might assume 5.15% is the effective rate and overpay.

## Commercial paper and agency notes

Corporations issuing [commercial paper](/corporate-bond/) also quote in bank discount yield. So do [Fannie Mae](/fannie-mae/), the Federal Home Loan Banks, and other agencies. The reason is simple: the money market is one ecology. A bank's overnight deposit rate, a corporate issuer's borrowing cost, and the Treasury's new auction—all are framed in the same dialect. Switching conventions would fragment the market and slow price discovery. Instead, everyone thinks in discount yield and translates to true yield only when reporting to clients or when a mandate (e.g., a [fund](/mutual-fund/) prospectus) requires it.

## Regulatory and accounting use

Financial regulators, tax authorities, and corporate accountants typically use the bank discount yield to record rates on very short-term borrowings. It is the standard in [loan origination](/loan-origination-fees/) documents and [interest-rate](/interest-rate/) templates. When a municipality issues a [tax anticipation note](/tax-anticipation-note/) or a bank borrows from the [Federal Reserve](/federal-reserve/) in the discount window, the rate is quoted as bank discount yield. Tax law references it; contract boilerplate references it. A financial professional who does not understand the convention will misread contracts, misestimate costs, and make pricing errors.

## The 360-day year: historical accident, ongoing standard

No one defends the 360-day year as mathematically pure. It is a leftover from the era before electronic calculators, when 360 was easier to work with than 365 (it has more factors: 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360). Traders could divide and multiply quickly in their heads. When computers arrived, no one bothered to "correct" the convention because the entire infrastructure—software, contracts, dealer quotes, auctions—was built on it. Changing now would create chaos. So the 360-day year persists in the money market, a monument to habit.

## Conversion and practical use

Portfolio managers, researchers, and risk officers typically convert bank discount yield to a more intuitive measure—often the [money market yield](/treasury-bill/) or bond equivalent yield—before analysing returns. But they must do the conversion correctly. A tool or spreadsheet error here can cost millions. Most institutional money-market platforms handle the conversion automatically; a trader enters a target rate in one convention, and the system quotes it in all three (bank discount, money market yield, bond equivalent yield) simultaneously. But traders who work across markets or use legacy systems must translate by hand.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill/) — the primary instrument using bank discount yield
- [Agency Discount Note](/agency-discount-note/) — agency short-term borrowing quoted in discount yield
- [Tax Anticipation Note](/tax-anticipation-note/) — municipal TANs also use the convention
- [Commercial Paper](/corporate-bond/) — corporate short-term debt quoted in discount yield
- [Par Value](/par-value/) — the face value of a bill, used as the denominator

### Wider context

- [Current Yield](/current-yield/) — an alternative yield calculation for longer-dated instruments
- [Yield to Maturity](/yield-to-maturity/) — used for bonds; different from discount yield
- [Interest Rate](/interest-rate/) — the foundation concept that discount yield approximates
- [Money Market](/treasury-bill/) — the ecosystem in which the convention governs

</div>

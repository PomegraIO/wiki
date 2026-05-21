---
title: "Prepayment Risk"
description: "Prepayment risk is the danger that a borrower will repay a loan or mortgage ahead of schedule, typically when interest rates fall, forcing the lender to reinvest principal at lower rates."
keywords:
  - prepayment risk
  - early repayment risk
  - mortgage refinancing
  - call optionality
  - reinvestment risk
image: "/svg/risk.svg"
---

*Prepayment risk is the risk that a borrower will repay a loan or mortgage before the maturity date — typically when interest rates fall — forcing the lender to reinvest the principal at lower rates, reducing expected returns. It is the inverse of [extension-risk](/extension-risk/) and represents the asymmetry inherent in mortgages and callable [bonds](/bond/).*

<div class="wiki-hatnote">

This entry covers the risk that borrowers repay early. For the risk that they hold longer than expected, see [extension-risk](/extension-risk/); for the risk that a [bond](/bond/) issuer calls it away, see [call-risk](/call-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Prepayment Risk — key facts</div>

<img src="/svg/risk.svg" alt="A calendar with an early red circle marking an unexpected mortgage payment date" />

<div class="wiki-infobox-caption">Prepayment robs lenders of high-coupon income when rates fall.</div>

|   |   |
|---|---|
| **What it is** | Risk that loan is repaid early, forcing reinvestment at lower rates |
| **Most common in** | Mortgages; callable corporate [bonds](/bond/); agency mortgage-backed securities |
| **Trigger** | Falling interest rates; borrower refinances to lower rate |
| **Materializes when** | Rates fall after loan originated |
| **Opposite of** | [Extension-risk](/extension-risk/); rates rising instead |
| **Affects returns** | Caps upside if rates fall sharply; shortens duration |
| **Measured by** | WAL (weighted average life), OAS (option-adjusted spread) |

</aside>

## How prepayment works

You lend $300,000 to a homeowner at a 6% rate, with a 30-year mortgage. You expect $300,000 × 6% = $18,000 per year for 30 years (plus return of principal at the end).

But suppose two years later, interest rates fall to 4%. The homeowner can refinance — take out a new $300,000 loan at 4%, using the proceeds to pay off your loan in full. The homeowner saves money; you lose the difference.

From your perspective, you were earning 6% on a long-term investment. Suddenly, you have $300,000 principal back, which you must reinvest at 4%. You have lost the 2% spread forever. Over the remaining 28 years of the mortgage, this shortfall compounds into a significant loss relative to what you expected.

This is prepayment risk. It is particularly asymmetric: when rates fall and you want to hold your high-coupon loan, the borrower exercises their implicit option and prepays. When rates rise, the borrower holds the low-rate loan. You lose in one direction (prepayment when rates fall) without winning in the other (extension when rates rise, if there is no [extension-risk](/extension-risk/) to offset it).

## Prepayment risk in mortgages and mortgage-backed securities

The largest manifestation of prepayment risk is in mortgages and mortgage-backed securities (MBS). When rates fall, refinancing volume spikes. In 2020, when the [Federal Reserve](/federal-reserve/) cut rates to near zero, mortgage refinancing exploded. Investors in MBS who had been earning 4% rates suddenly had principal returned and faced a choice: reinvest at 1% rates or move to riskier assets.

MBS present a special complexity: the investor does not know when prepayment will occur. Some pools prepay slowly; others (when rates fall sharply) prepay rapidly. This makes MBS harder to analyze and price than regular bonds.

The yield on an MBS accounts for some prepayment risk — it is higher than a Treasury of the same maturity because of it. But if prepayment actually occurs, the realized return falls short of the stated yield.

## Prepayment risk in callable bonds

Corporate [bonds](/bond/) often come with a **call option**: the issuer has the right to repay the bond before maturity, usually after a call-protection period (e.g., 5 years). Similar to mortgages, issuers exercise this option when rates fall and they can refinance at lower rates.

An investor in a callable [bond](/bond/) yielding 6% gets paid that yield only if rates stay high or rise further. If rates fall, the issuer calls the bond, and the investor has to reinvest at the lower rates. The call option is valuable to the issuer (worth maybe 1% of the coupon) and thus comes out of the bondholder's expected return.

This is why callable [bonds](/bond/) yield more than non-callable [bonds](/bond/): the extra yield compensates investors for the prepayment risk.

## Managing prepayment risk

Investors concerned about prepayment risk have limited options:

- **Accept the trade-off.** Receive the higher yield that compensates for prepayment risk. This is what most MBS investors do.

- **Avoid callable bonds and mortgages.** Stick to non-callable [bonds](/bond/), Treasury bonds, and other assets without embedded optionality. The trade-off is lower yield.

- **Hedge the option.** Use derivatives to hedge the risk that rates fall and the borrower prepays. Investors can buy interest-rate swaptions or caps to hedge prepayment risk, though these are complex and costly.

- **Ladder maturities.** If one of your mortgages prepays, move proceeds into new mortgages with different characteristics, so you are not reinvesting everything at once.

- **Model and price carefully.** Use **option-adjusted spread (OAS)** analysis, which accounts for the value of the embedded prepayment option and allows comparison of mortgages and callable [bonds](/bond/) on an apples-to-apples basis.

For most individual investors, the practical approach is to avoid concentrations in MBS and callable bonds, hold a mix of assets with different durations, and accept that prepayment risk is part of the fixed-income landscape.

## See also

<div class="wiki-seealso">

### Closely related

- [Extension-risk](/extension-risk/) — opposite risk when rates rise
- [Call-risk](/call-risk/) — risk of callable [bonds](/bond/) being called
- [Interest-rate-risk](/interest-rate-risk/) — underlying driver of prepayment
- [Reinvestment-risk](/reinvestment-risk/) — consequence of prepayment
- [Bond](/bond/) — carries prepayment risk if callable or mortgage-backed

### Broader context

- [Mortgage-backed security](/bond/) — classic example of prepayment risk
- [Federal Reserve](/federal-reserve/) — rate changes trigger prepayment waves
- [Duration](/interest-rate-risk/) — shortens with prepayment
- [Yield-curve](/yield-curve/) — drives prepayment decisions
- [Stress testing](/stress-testing/) — assesses portfolio under prepayment scenarios

</div>

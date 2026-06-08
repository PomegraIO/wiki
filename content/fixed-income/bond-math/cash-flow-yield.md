---
title: "Cash Flow Yield"
description: "The internal rate of return on a mortgage-backed or asset-backed security given an assumed prepayment rate."
keywords:
  - mortgage-backed security
  - asset-backed security
  - prepayment risk
  - yield measurement
  - internal rate of return
  - fixed income
image: "/svg/fixed-income.svg"
---

*The **cash flow yield** is the [yield](/yield-to-maturity/) of a [mortgage-backed security](/mortgage-backed-security/) or [asset-backed security](/mortgage-backed-security/) calculated under an explicit prepayment assumption. Unlike a traditional [bond's](/bond/) fixed maturity, MBS and ABS cash flows depend heavily on borrower behaviour. The cash flow yield bridges this uncertainty by modelling one specific prepayment scenario—typically the [conditional prepayment rate](/mortgage-backed-security/) published by the market—and deriving the internal rate of return on that assumed cash-flow stream.*

## Why prepayment assumptions matter

Traditional bonds return principal at maturity on a known date. [Mortgage-backed securities](/mortgage-backed-security/) and [asset-backed securities](/mortgage-backed-security/) do not. When a homeowner refinances or sells, the underlying mortgage is repaid early. When credit card debt is paid down, the backing asset generates cash faster than scheduled.

This [prepayment risk](/prepayment-risk/) creates a problem: you cannot calculate a single "maturity" or "yield to maturity" because the timing of cash flows is uncertain. A 30-year mortgage-backed security might average 8 years of actual cash flows if prepayment rates are high, or 18 years if they are low.

The cash flow yield solves this by pinning down an assumption. The market publishes a standard prepayment model—the PSA (Public Securities Association) model or its variants—which assumes a certain annual prepayment rate. Given that assumption, the issuer's cash flows become deterministic, and a [yield to maturity](/yield-to-maturity/) calculation becomes possible.

## Calculation and interpretation

The cash flow yield is the discount rate that equates the market price of the security to the present value of its assumed cash flows:

Price = Σ (Cash Flow_t / (1 + YieldCF)^t)

where Cash Flow_t includes principal repayment, scheduled interest, and prepayments based on the assumed CPR (Conditional Prepayment Rate).

If the market quotes an MBS at 100 par and assumes a 6 per cent CPR, the cash flow yield is the IRR of that specific prepayment scenario. A different CPR assumption yields a different IRR.

Investors can then compare cash flow yield to yields on other securities (Treasuries, corporates) to decide whether the extra [credit risk](/credit-risk/) and [prepayment risk](/prepayment-risk/) justify the return.

## How prepayment assumptions vary

Prepayment models are not scientific laws; they are behavioural estimates. Mortgage holders refinance when rates fall and their credit allows it, accelerating prepayments. They prepay less readily when rates are high or their home value has declined.

The PSA model assumes prepayments ramp up over time, starting low in month 1 and peaking at month 30, then holding steady. A "100 per cent PSA" is the baseline; "200 per cent PSA" means twice the baseline rates. Market participants may use different multiples depending on prevailing rates, the age of the mortgage pool, and seasonal patterns.

This flexibility is both powerful and dangerous. The same MBS security priced at 100 PSA looks cheap, but priced at 300 PSA looks expensive—because the higher prepayment rate compresses the average life and limits price upside if yields fall. Investors burned by misjudged prepayment assumptions have learned this lesson painfully.

## Cash flow yield versus static yield

A [bond's](/bond/) [yield to maturity](/yield-to-maturity/) assumes the bondholder holds to maturity and receives all coupon and principal on schedule. A [mortgage-backed security's](/mortgage-backed-security/) cash flow yield assumes the bondholder holds to the average life under the stated prepayment model. The two concepts are fundamentally different in horizon and assumption.

This matters because [mortgage-backed securities](/mortgage-backed-security/) often outperform when yields fall—not because price appreciation is unlimited, but because falling rates slow prepayments, extending average life and allowing the security to hold duration. Investors who calculated cash flow yield at one CPR and saw actual CPR fall lower often benefited unexpectedly.

Conversely, cash flow yield can overstate returns if the market's prepayment forecast proves optimistic. Borrowers may refinance faster than modelled if lending standards ease or rates drop sharply. Faster prepayment means the investor's principal comes back sooner, forcing reinvestment at lower yields.

## Comparing securities across prepayment regimes

Asset-backed securities—backed by car loans, credit card receivables, or student loans—have different prepayment characteristics. Credit card ABS prepay faster if consumer confidence is high and delinquencies are low. Auto ABS prepay when used car prices rise and borrowers have equity to tap.

The cash flow yield framework applies to all of them: pick a prepayment assumption, calculate the IRR, and compare to Treasuries and other [fixed-income](/bond/) benchmarks. An investor might find that auto ABS at 250 basis points over Treasuries looks attractive at a 50 per cent CPR assumption but risky at 100 per cent CPR.

Portfolio managers use stress-testing on prepayment scenarios—the bull case, the base case, the bear case—to quantify [tail risk](/tail-risk/) and decide position sizing.

## The role of option-adjusted spread

More sophisticated analysis goes beyond cash flow yield. The [option-adjusted spread](/bond/) (OAS) reflects the spread over Treasuries after stripping out the [option value](/option/) of the embedded prepayment option. An MBS trading at a high cash flow yield but low OAS is overpriced—the yield includes compensation for prepayment risk that does not fairly value the option.

Still, cash flow yield remains the lingua franca of MBS trading. Traders quote prices and yields based on standard CPR assumptions, allowing dealers and investors to communicate risk and opportunity quickly.

## See also

<div class="wiki-seealso">

### Closely related

- [Mortgage-Backed Security](/mortgage-backed-security/) — the primary asset for which cash flow yield is calculated
- [Asset-Backed Security](/mortgage-backed-security/) — consumer receivables securitised with similar yield measurement
- [Prepayment Risk](/prepayment-risk/) — the core uncertainty that makes cash flow yield necessary
- [Yield to Maturity](/yield-to-maturity/) — traditional bond yield that assumes fixed maturity
- [Price-Yield Relationship](/price-yield-relationship/) — how MBS prices respond to yield moves under prepayment models
- [Duration](/duration/) — time-weighted measure of cash flow timing and rate sensitivity

### Wider context

- [Bond](/bond/) — the foundational fixed-income instrument
- [Yield Curve](/yield-curve/) — the structure of yields across maturities
- [Credit Risk](/credit-risk/) — additional return required for default risk
- [Real Estate Investment Trust](/real-estate-investment-trust/) — an alternative structure for real-estate-backed cash flows
- Securitisation — the process of pooling loans and issuing securities

</div>

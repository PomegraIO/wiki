---
title: "Sequential-Pay CMO"
description: "A collateralized mortgage obligation in which all principal repayments flow to the first tranche until it is fully retired, then sequentially cascade to lower-priority tranches."
keywords:
  - sequential-pay CMO
  - CMO structure
  - principal waterfall
  - mortgage tranches
  - structured credit
image: /svg/fixed-income.svg
---

*A **sequential-pay CMO** is the most straightforward variant of a [collateralized mortgage obligation](/sequential-pay-cmo/), a securitization structure where all principal recovered from the underlying mortgage pool flows exclusively to the most senior tranche until that tranche is retired, then cascades down to the next tranche, and so on. This waterfall structure creates a ladder of maturities and risk profiles from a single pool of mortgages.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sequential-Pay CMO — Key Facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income securities and structured credit." />

<div class="wiki-infobox-caption">A tiered principal waterfall that transforms mortgage cash flows into tranches of varying duration.</div>

|   |   |
|---|---|
| **What it is** | CMO structure where all principal goes to Tranche A until retired, then to Tranche B, etc. |
| **Also called** | Vanilla CMO, plain-vanilla CMO |
| **Tranches** | Typically 4–6, most senior to most junior |
| **Principal flow** | Serial redemption; each tranche repays in full before next begins receiving principal |
| **Interest flow** | All tranches receive coupon interest concurrently |
| **Maturity range** | From short (1–2 years) to very long (20+ years) depending on prepayment speed |
| **Key risk** | Prepayment risk for short tranches; extension risk for long tranches |

</aside>

## The original CMO problem

Before CMOs, investors in [mortgage-backed securities](/mortgage-backed-security/) faced an uncomfortable choice: accept a single average-life maturity that didn't fit their portfolio needs, or build their own duration ladder through cash-flow analysis and guesswork. The mortgage pool's actual cash flows—principal, interest, and prepayments—were unpredictable, and pass-through MBS holders had to estimate their real duration and hope that prepayment speeds aligned with assumptions.

The sequential-pay CMO solved this by explicitly segmenting the cash flows. Instead of buying a single MBS that might mature in 4 years or 12 years depending on rates, investors could buy Tranche A (short), Tranche B (intermediate), Tranche C (long), and Tranche D (very long), each with a predictable principal schedule relative to the others—though all still subject to the underlying prepayment speed of the mortgage pool.

## How principal cascades

The mechanics are simple. All [coupon payments](/coupon-payment/) go to all tranches in proportion to their outstanding balance. All principal repayments (scheduled [amortization](/amortization/) and prepayments alike) go exclusively to whichever tranche is currently "active." Once a tranche is fully redeemed—meaning all its original principal has been returned—it goes silent, and principal automatically redirects to the next tranche down the ladder.

Suppose the deal has $100 million in four tranches of $25 million each. If the mortgage pool generates $5 million in principal in month one, that $5 million reduces Tranche A's balance to $20 million. All interest continues to all tranches. The next month, another $5 million in principal goes to Tranche A again, bringing it to $15 million. This repeats until Tranche A is fully paid off—say, in year 4. Then Tranche B starts receiving principal, and so on.

## Duration and maturity in sequential-pay

The sequential-pay structure creates a natural ladder of expected lives. The most senior Tranche A has the shortest average life because it gets first claim on all principal. In a stable [interest-rate](/interest-rate/) environment with normal [prepayment](/mortgage-backed-security/) speeds, it might have an average life of 2–3 years. Tranche B might average 4–5 years, Tranche C 7–10 years, and Tranche D 15–20 years or more.

But these are expectations, not guarantees. If [interest rates](/interest-rate/) fall sharply and homeowners refinance en masse, prepayment speeds accelerate. Tranche A might retire in 18 months instead of three years. Conversely, if rates rise, prepayments dry up, scheduled [amortization](/amortization/) becomes the only principal source, and Tranche A stretches to 5+ years. The sequential structure constrains uncertainty—Tranche A will always pay off before Tranche B—but it does not eliminate prepayment risk.

## Coupon structure and yield relationships

Sequential-pay CMOs typically have a coupon structure that reflects the duration and risk of each tranche. Tranche A, the shortest, might carry a coupon of 3.5 per cent. Tranche B might be 4.0 per cent. Tranche C 4.5 per cent. Tranche D 5.0 per cent or higher. The issuer—often a bank originating mortgages, a mortgage servicer, or a securities underwriter—prices each tranche to reflect its expected maturity and [credit-risk](/credit-risk/), with the underlying mortgages (and the [mortgage-backed-security](/mortgage-backed-security/) itself) serving as collateral.

The spread relationship between tranches compensates investors for accepting extension risk (in the case of longer tranches) or reinvestment risk (in the case of shorter tranches receiving their principal earlier than expected). Tranche D investors get paid a higher coupon in exchange for the possibility that they might hold a tranche that extends far beyond its expected maturity if rates spike.

## Prepayment-speed sensitivity

The great weakness of sequential-pay CMOs is that the maturity ladder depends entirely on prepayment assumptions. When loans are issued at a 4 per cent rate and long-term rates drop to 2 per cent, everyone refinances at once. Principal floods in, Tranche A vanishes, Tranche B follows shortly after, and [mortgage-backed-security](/mortgage-backed-security/) investors who thought they were buying a 5-year bond end up holding a 1-year asset. They must reinvest at 2 per cent instead of the 4 per cent coupon they were earning.

The flip side: if rates rise from 4 per cent to 6 per cent, homeowners hold mortgages, prepayments evaporate, and Tranche D investors watch their expected 15-year bond stretch to 25 years while the coupon now looks paltry. This [extension risk](/interest-rate-risk/) can be severe and is the primary concern for long-tranche holders in rising-rate environments.

## Comparison to other CMO structures

Sequential-pay CMOs are the foundation, but they are not the only answer. [Planned amortization class bonds](/planned-amortization-class-bond/) (PACs) use companion tranches to stabilize the principal schedule of PAC tranches, reducing prepayment risk for those investors. [Z-bonds](/z-bond/) defer all interest and principal, accumulating it until senior tranches retire. Floating-rate tranches peg coupons to [SOFR](/sofr/) or other indices to hedge [interest-rate-risk](/interest-rate-risk/). Each variant trades simplicity for different risk exposures.

Sequential-pay remains popular because it is transparent, easy to understand, and genuinely useful for investors with simple duration targets. It is the vanilla structure against which more exotic CMO variants are measured.

## The servicer's role

A [clean-up call](/clean-up-call/) is typically embedded in sequential-pay CMO deals. Once the remaining mortgage pool balance falls below 10 per cent of the original collateral (or another threshold), the servicer can redeem all remaining tranches at par. This prevents the deal from becoming a zombie with a tiny pool generating trivial cash flows. For investors, it caps the latest possible maturity and makes horizon planning more certain.

## See also

<div class="wiki-seealso">

### Closely related

- [Collateralized mortgage obligation](/sequential-pay-cmo/) — the parent securitization structure
- [Mortgage-backed security](/mortgage-backed-security/) — the foundational pass-through security underlying CMO tranches
- [Planned amortization class bond](/planned-amortization-class-bond/) — a CMO variant with prepayment protection for specific tranches
- [Z-bond](/z-bond/) — an accrual tranche in CMO structures
- [Clean-up call](/clean-up-call/) — servicer option to redeem when the pool shrinks below a threshold
- [Amortization](/amortization/) — scheduled principal repayment
- [Prepayment risk](/mortgage-backed-security/) — the core uncertainty in mortgage-backed structures

### Wider context

- [Securitization](/securitization/) — the underlying asset-backed security process
- [Bond](/bond/) — the foundational fixed-income instrument
- [Interest-rate risk](/interest-rate-risk/) — the overarching risk framework for CMO investors
- [Duration](/duration/) — maturity-adjusted measure of interest-rate sensitivity

</div>

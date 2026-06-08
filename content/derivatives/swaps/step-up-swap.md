---
title: "Step-Up Swap"
description: "An interest-rate swap where the fixed coupon rises on a pre-set schedule, matching the step-up structure of many corporate debt facilities."
keywords:
  - step-up swap
  - stepped coupon
  - structured interest rate swap
  - tiered coupon schedule
  - amortizing swap
image: "/svg/derivatives.svg"
---

*A **step-up swap** is an [interest-rate swap](/interest-rate-swap/) in which the fixed-rate coupon increases in discrete steps at pre-agreed dates. Rather than a single flat rate for the swap's life, the payer delivers, for example, 2% for the first two years, 2.5% for the next two, and 3% thereafter. The floating leg remains unchanged. Step-up swaps allow borrowers to match their natural [cost-of-debt](/cost-of-debt/) trajectory, deferring high coupons to later years when creditworthiness may have improved or refinancing may be possible.*

## Why step-up structures exist

Corporate bond issuers, especially those in cyclical industries, often prefer debt structures where early coupons are lower and later coupons are higher. A mining company with rising production capacity might issue bonds at, say, 3% for year one, 3.5% for year two, and 4% for year three. The logic is sound: the issuer buys time to establish cash flow, improve credit metrics, and reduce [leverage-ratio-forex](/leverage-ratio-forex/). A [bond](/bond/) buyer accepts the rising coupon in exchange for lower upfront payments.

Step-up swaps let borrowers replicate this structure synthetically without issuing multiple tranches. Instead of selling a 3-year bond at 3.5% flat (an average), a borrower can issue at a lower flat rate and swap into a step-up, paying less than the market average early and more later. The total [cost-of-equity](/cost-of-equity/) may be comparable, but the timing of outflows is optimized for the borrower's cash-generation profile.

Banks also use step-ups to match their balance-sheet realities. A bank's [funding costs](/cost-of-debt/) often rise as deposit rates climb with inflation; by entering a step-up on the [swap](/interest-rate-swap/) side, the bank can hedge its own rising cost structure without buying successive rolling swaps.

## How the coupon schedule works

Step-ups are defined by a table or formula: the coupon at date *t* is a function of *t*. Common schedules are linear (adding a fixed increment each year), exponential (compounding), or lumpy (jumping at specific milestones). A typical contract might read:

- Years 1–2: 2.00%  
- Years 3–4: 2.50%  
- Years 5–7: 3.00%

The floating leg usually remains [SOFR](/sofr/), [LIBOR](/libor/), or a [treasury-bill](/treasury-bill/) rate, reset quarterly. The borrower (fixed payer) knows exactly what their all-in cost will be across time, while the fixed receiver (typically a bank) prices in the time value of money, weighting later higher coupons less than earlier ones using [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/).

Schedules can be more elaborate. A borrower with rising EBITDA might negotiate a schedule that steps up only if certain [leverage-ratio-forex](/leverage-ratio-forex/) thresholds are breached, introducing a small conditional element. However, most step-ups are deterministic—the coupon is fixed in advance.

## Pricing and valuation

The present value of a step-up swap differs from a vanilla swap because of the timing of cash flows. Using [duration](/duration/), a step-up fixed receiver holds coupons that are higher in later years, reducing the effective duration compared to a flat swap. If [yield-curve](/yield-curve/) is steep, this is a valuable feature—the receiver's later high coupons are worth less in present-value terms, so the fixed rate can be lower.

Pricing breaks into two parts: first, the present value of the floating payments (standard [interest-rate swap](/interest-rate-swap/) logic), and second, the present value of the stepped fixed leg. Dealers compute the spread—the rate or points added to [SOFR](/sofr/) or [treasury-bill](/treasury-bill/)—that makes both sides equal in value at inception.

[Gamma](/gamma/) and [vega](/vega/) matter less in step-ups than in range accruals. Step-ups have predictable cash flows; their sensitivity to rate moves is primarily [duration](/duration/) (parallel rate shift) and limited [convexity](/interest-rate-risk/) (curve shape). A borrower issuing at a fixed step-up rate has little uncertainty about their cash outflows, which is often the whole point.

## Use cases and borrower archetypes

Startup-stage companies love step-ups. A fast-growing software firm might borrow at 1.5% early (when it's high-risk), stepping to 2.5% later (as growth is proven and credit improves). By the time the coupon rises, the company has hopefully matured enough to absorb higher rates.

[Merger](/merger/) and [acquisition](/acquisition/) targets sometimes use them in financing. An acquirer might assume the target will quickly reduce debt, making early low rates attractive and later higher rates palatable. If the integration fails, the acquirer is stuck with rising coupons on shrinking cash flow—a real hazard.

Mortgage originators and [securitization](/securitization/) vehicles use step-ups to match amortization schedules. A mortgage-backed security might step up in tandem with expected principal reduction, keeping coupon risk in phase with [prepayment-risk](/prepayment-risk/).

Pension funds occasionally swap into step-up exposure by buying [bond](/bond/)s and entering step-up pay-fixed swaps, locking in a rising yield stream that matches anticipated return requirements as liabilities shift.

## Real-world mechanics and risks

One risk is [refinancing-risk](/refinancing-risk/). A borrower issuing a 7-year debt with step-ups hopes to refinance by year 5 when rates are lower. If rates rise instead, the borrower is trapped—the rising coupon becomes a burden just when refinancing is most needed.

Another risk is market comparability. If a peer in the same industry issues at a flat rate, the step-up issuer's early coupons appear cheaper than the peer's, masking real credit differences. Rating agencies are alert to this; they may penalize step-up issuers for the deferred cost, effectively treating the later higher coupons as if they applied from day one.

Accounting treatment varies. Under [generally-accepted-accounting-principles](/generally-accepted-accounting-principles/), step-up interest expense is recognized as it accrues, so a borrower's year-one income statement shows lower interest cost than year five, all else equal. This can distort [earnings-per-share](/earnings-per-share/) and return-on-equity comparisons over time.

For banks and dealers, the risk is that the borrower fails to repay when the coupon steps up. Credit quality typically declines precisely when the coupon rises, creating a nasty feedback loop. A [credit-spread](/credit-spread/) widening forces the swap's mark-to-market lower, crystalizing losses at an inopportune moment.

## Variants and hybrids

Some step-ups include caps or floors: the coupon rises but not above 4%, for instance. Others are triggered—the step only occurs if the borrower's credit rating falls below a threshold, introducing a conditional element.

Reverse step-ups are rare but exist: a coupon that falls over time, used by borrowers with rising cash flows who want to show good faith by paying less later (though refinancing incentives usually make this backward-seeming).

[Range-accrual-swap](/range-accrual-swap/) structures sometimes incorporate step-up features, so the accrual band itself moves up over time. The mathematics become complex, but the intuition is simple: match the swap's trajectory to the borrower's expected life cycle.

## Comparison to plain vanilla swaps

A vanilla [interest-rate swap](/interest-rate-swap/) has a fixed coupon that never changes; a step-up coupon rises in discrete jumps. This makes step-ups slightly more expensive to price and settle but often cheaper for the borrower upfront. The fixed receiver (bank) demands a higher all-in yield to compensate for the timing mismatch and the risk of early default.

A [differential-swap](/differential-swap/) is entirely different: it exchanges two floating rates from separate currency zones. A step-up swap is interest-rate only and single-currency.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Rate Swap](/interest-rate-swap/) — the vanilla foundation on which step-ups build
- [Range-Accrual-Swap](/range-accrual-swap/) — another conditional swap variant
- [Differential Swap](/differential-swap/) — cross-currency floating-rate exchange
- [Duration](/duration/) — key metric for valuing step-up cash flows
- [Cost of Debt](/cost-of-debt/) — the metric step-ups help optimize
- [Bond](/bond/) — the underlying debt instrument often paired with step-up swaps

### Wider context

- [Interest-Rate Risk](/interest-rate-risk/) — the exposure being hedged
- [Refinancing Risk](/refinancing-risk/) — a key real-world hazard for step-up issuers
- [Credit Spread](/credit-spread/) — widening spreads can harm both borrower and receiver
- [Securitization](/securitization/) — a common venue for step-up structures
- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — metric sometimes tied to step-up triggers

</div>

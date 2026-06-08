---
title: "Range Accrual Swap"
description: "A swap in which interest accrues only when a reference rate stays within a pre-defined range, compressing costs for rate-sensitive hedgers."
keywords:
  - range accrual swap
  - corridor swap
  - conditional interest accrual
  - structured interest rate swap
  - range-accrual derivative
image: "/svg/derivatives.svg"
---

*A **range accrual swap** is an [interest-rate swap](/interest-rate-swap/) where interest accrues on one leg only on days the reference rate remains within a pre-specified corridor, or "range." The other leg typically accrues normally. By restricting accrual to a bounded rate band, both parties gain: the payer receives lower coupons in exchange for bearing the risk that rates will drift outside the band, while the receiver benefits from elevated coupons on "in-range" days.*

## Why banks structure them

Range accrual swaps exist because they address a real tension in borrowing: most debt markets move in bands. A mortgage borrower might expect rates to oscillate between 3% and 7%; an emerging-market debtor might face a 4% to 9% corridor. By selling a range accrual, borrowers give up some upside at the cost of paying a lower all-in rate. Banks build them to intermediate this preference.

The economics are roughly mutual. If you are a corporate borrower expecting rates to stay within, say, 1% to 3%, you can pay a [fixed-rate mortgage-personal](/fixed-rate-mortgage-personal/) or buy a range accrual where the coupon accrues only on in-range days. The second option is cheaper upfront—you pocket a lower rate—but if rates escape the band, you stop accruing (or accrue at a penalty). It's a bet you're willing to make.

## How accrual mechanics work

Range accruals use daily or quarterly observation windows. Each day (or period), the reference rate—typically [SOFR](/sofr/), [LIBOR](/libor/), or a currency benchmark—is observed. If it falls within the range, the notional accrues interest for that day at the agreed coupon. If it breaches the band, that day's accrual is skipped (or deferred, depending on the contract). The final coupon is the sum of all in-range accruals, often spread linearly over the remaining swap life.

This structure means the effective rate paid varies inversely with how many days the reference rate strays outside the corridor. In stable periods, accrual is nearly constant; in volatile periods, the borrower's cost can jump sharply if rates overshoot. The risk is concentrated but visible—you always know the band.

## Who uses them and why

[Hedge funds](/hedge-fund/) use range accruals to express neutral-to-low views on [volatility-smile](/volatility-smile/) or rate dispersion. A fund expecting rates to stay flat might sell range accrual risk and pocket the lower coupon. [Corporate bond](/corporate-bond/) issuers use them to reduce borrowing costs when they believe rates will remain anchored to central bank guidance. Pension funds occasionally buy them as a way to earn extra yield on a sector they think is range-bound.

The appeal is leverage without explicit leverage. You are not borrowing to magnify returns; you are simply concentrating risk in a band you feel confident about. If you are right, you save money. If you are wrong, the cost is real but capped by the spread above the accrual rate outside the band.

## Pricing and risk

The fair value of a range accrual hinges on the probability that the reference rate will remain in-range. If the band is tight (say, 50 basis points) and [implied-volatility](/implied-volatility/) is high, the seller demands a much larger spread to compensate. If the band is wide and volatility is low, the spread compresses because in-range probability is high.

The Greeks are unusual. A range accrual has strong [gamma](/gamma/) exposure—as rates move closer to the band's edge, the sensitivity to further moves rises sharply. [Theta](/theta/) can be positive or negative depending on whether the rate is in-range at the measurement date. [Vega](/vega/) is generally negative for the accrual receiver (seller of the range); falling volatility helps them.

There is also [operational-risk](/operational-risk/) in the mechanics. If the reference rate is observed at, say, 4:15 p.m. Eastern but the swap contract specifies 4:00 p.m., timing differences can matter. Banks are careful to document the exact observation window and settlement mechanics.

## Real-world constraints

Range accruals work best when the reference rate is liquid and well-documented. In emerging markets or for less-tracked indices, the cost of settling disputes over whether a rate was truly in-range becomes prohibitive. [Counterparty-risk](/counterparty-risk/) is concentrated—if your swap counterparty fails, you lose both the swap's mark-to-market value and the stream of future accrual payments.

They are also subject to regulatory scrutiny. In jurisdictions with strict [fair-value](/fair-value/) accounting rules, range accruals require expensive mark-to-market models, raising cost of entry. A hedge fund or smaller corporate often finds it cheaper to use a standard [interest-rate swap](/interest-rate-swap/) and layer in separate [swaptions](/option/) or other options to capture the same view.

Range accruals also struggle in persistent low or high rate environments. If the [Federal Reserve](/federal-reserve/) holds rates at 0% for a decade, in-range days become rare and the effective coupon collapses; the trade turns into a loss. Conversely, if rates spike and stay high, the same thing happens on the other side. The strategy works only if rates truly oscillate within the band.

## Relationship to other swaps

Range accruals sit between vanilla [interest-rate swaps](/interest-rate-swap/) and more exotic products like [swaptions](/option/). A vanilla swap always accrues; a range accrual accrues conditionally; a [step-up-swap](/step-up-swap/) accrues at a deterministic rising coupon. A [differential-swap](/differential-swap/) is distinct—it exchanges two floating rates in different currencies, both in one domestic currency, without reference to a corridor.

Some dealers offer variants: double-range accruals (where accrual occurs outside a band instead of inside), and knock-in/knock-out versions where the range only activates if certain conditions are met. These hybrids appeal to traders with strongly directional volatility views.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Rate Swap](/interest-rate-swap/) — the vanilla version on which range accruals are built
- [Step-Up Swap](/step-up-swap/) — another structured swap variant with a predetermined coupon schedule
- [Differential Swap](/differential-swap/) — swaps two floating rates from different currency markets
- [Volatility Smile](/volatility-smile/) — the pricing dynamic underlying range accrual exposure
- [Implied Volatility](/implied-volatility/) — key input for range accrual valuation
- [Option Premium](/option-premium/) — the extra spread sellers demand for bearing out-of-range risk

### Wider context

- [Swap](/interest-rate-swap/) — broad class of derivative contracts
- [Forward-Guidance](/forward-guidance/) — central bank signaling that can anchor rates within bands
- [Counterparty Risk](/counterparty-risk/) — key risk in bilateral swap agreements
- [Fair Value](/fair-value/) — accounting treatment affecting range accrual adoption
- [Hedge Fund](/hedge-fund/) — typical user of sophisticated swap structures

</div>

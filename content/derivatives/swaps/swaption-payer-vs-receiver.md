---
title: "Payer Swaption vs Receiver Swaption"
description: "Payer swaption vs receiver swaption: understand the right to pay fixed and receive floating, the economic exposures they hedge, and their payoff profiles."
keywords:
  - payer swaption
  - receiver swaption
  - swaption payer vs receiver
  - interest rate swaptions
  - swap option hedge
image: /svg/derivatives.svg
---

*A **payer swaption vs receiver swaption** distinguishes the two main variants of a [swaption](/option/), which is an [option](/option/) on an interest-rate [swap](/swap/). A **payer swaption** gives the holder the right to enter a [swap](/swap/) where they pay fixed and receive floating; a **receiver swaption** gives the right to pay floating and receive fixed. Each is a hedge for the opposite market scenario: payer swaptions protect against rising rates, receiver swaptions protect against falling rates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Payer vs Receiver Swaption — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Two options on swaps, structured for opposite rate environments and financing profiles.</div>

|   |   |
|---|---|
| **Payer swaption exercise** | Holder pays fixed rate, receives floating |
| **Receiver swaption exercise** | Holder pays floating rate, receives fixed |
| **Payer benefits if** | [Interest rates](/interest-rate/) rise after purchase |
| **Receiver benefits if** | Interest rates fall after purchase |
| **Typical payer user** | Borrower facing variable-rate debt |
| **Typical receiver user** | Lender receiving variable-rate income |
| **Moneyness at exercise** | Payer ITM when strike > [swap rate](/interest-rate-swap/); Receiver ITM when strike < swap rate |

</aside>

## The Core Mechanics

A [swaption](/option/) is a legal right—not an obligation—to enter an [interest-rate swap](/interest-rate-swap/) on a future date at a preset fixed rate (the strike or exercise rate). Two parties can agree on a swaption: one can hold the right to pay fixed, the other to pay floating.

In a **payer swaption**, the holder has the right to pay a fixed rate and receive [SOFR](/sofr/) (or another floating rate benchmark). In a **receiver swaption**, the holder has the right to pay floating and receive a fixed rate.

The [premium](/option-premium/) paid upfront reflects the value of the embedded optionality—the right to enter the swap if circumstances favor the holder and walk away if they do not.

## Payer Swaptions: Insurance Against Rising Rates

A corporate treasurer who knows the company will need to refinance a $100 million variable-rate [loan](/cost-of-debt/) in two years worries that [interest rates](/interest-rate/) might spike in the interim, inflating future borrowing costs. Today's [swap rate](/interest-rate-swap/) (the fixed rate on a two-year swap) is 4%. She buys a payer swaption: the right to pay 4% fixed and receive floating in two years.

If rates rise to 5.5% by year 2, the swaption is valuable. She exercises it, locking in 4% instead of the prevailing 5.5%. She pays the [option premium](/option-premium/) upfront, but it is a form of insurance. If rates fall to 2.5%, she does not exercise; she borrows at market rates and walks away from the swaption, losing only the premium.

The payoff to the payer swaption is:

**Payer swaption value = max(0, (future swap rate - strike rate) × notional × swap duration)**

In the example above, if the future 2-year swap rate settles at 5.5% and the strike was 4%, the intrinsic value is (5.5% − 4%) = 1.5% times the notional and duration, a substantial gain.

The mechanics of payer swaptions make them useful in several hedging scenarios:

- A company with floating-rate debt that expects rates to climb.
- A project finance entity that will assume variable-rate borrowing at a future closing date.
- A [bank](/federal-reserve/) originating variable-rate mortgages that wants to cap its funding costs.

## Receiver Swaptions: Insurance Against Falling Rates

Now invert the scenario. A pension fund receives variable-rate income (floating-rate corporate bond coupons or loan interest) and worries that [interest rates](/interest-rate/) will decline, shrinking future reinvestment yields. It buys a receiver swaption: the right to pay floating and receive fixed at, say, 4%.

If rates fall to 2.5% over the next two years, the receiver swaption is in the money. The fund exercises it, locking in 4% income instead of the market's 2.5%. If rates rise to 5.5%, the fund does not exercise, keeps its floating income (now worth more), and walks away from the swaption premium.

The payoff to the receiver swaption is:

**Receiver swaption value = max(0, (strike rate - future swap rate) × notional × swap duration)**

If the future swap rate falls to 2.5% and the strike was 4%, the intrinsic value is (4% − 2.5%) = 1.5% of notional and duration.

Receiver swaption users include:

- Fixed-income investors or asset managers holding variable-rate securities and concerned about reinvestment risk.
- Banks that fund operations with floating-rate deposits and face compression of [net interest margin](/net-interest-margin/) if rates fall.
- Corporates with floating-rate receivables or surplus cash that want to lock in yield.

## Payoff Profiles and Moneyness

Both swaptions are options, so both have bounded downside (the premium paid) and leveraged upside (the intrinsic value of the swap at exercise).

At the exercise date, if the swaption is in the money (ITM):

- **Payer swaption ITM**: the current market swap rate is higher than the strike. The holder benefits by paying the lower strike fixed and receiving the higher floating.
- **Receiver swaption ITM**: the current market swap rate is lower than the strike. The holder benefits by receiving the higher strike fixed and paying the lower floating.

Both can be worth zero at expiration (or abandoned) if the market has moved against the option. This bounded loss is the core value proposition: pay a premium today for the right, not the obligation, to lock in a rate later.

## Premium Determinants and Pricing

Swaption premiums depend on:

1. **Strike choice**: A swaption struck at-the-money (strike equals the forward [swap rate](/interest-rate-swap/)) costs less than one struck far in the money. A treasury willing to pay more premium can buy a lower strike on a payer swaption, locking in a tighter cap on rates.

2. **Volatility expectations**: Higher expected [interest-rate](/interest-rate/) volatility increases swaption value, because a wider potential price move makes the option more valuable. [Implied volatility](/implied-volatility/) in swaption markets is a traded input.

3. **Tenor and swap duration**: A longer-duration underlying swap (e.g., a 10-year swap) embedded in the swaption carries more value than a 2-year swap, all else equal. A swaption on a longer swap can be worth multiples more.

4. **Time to expiration**: Swaptions are most commonly 6 months to 5 years to expiration. Longer-dated options cost more, reflecting more time for rates to move.

Swaption premiums are quoted in basis points (1 bp = 0.01%) of the notional and typically run from 25 bp to 200+ bp depending on the above factors.

## Payer and Receiver as Mirror Strategies

Interestingly, a payer swaption and a receiver swaption on the same underlying swap are not mirror images in cost; the premium differential reflects the market's expectations about future [interest-rate](/interest-rate/) paths and [volatility](/historical-volatility/).

If the [yield curve](/yield-curve/) is upward sloping and the market expects rates to remain relatively stable, receiver swaptions (betting on falling rates) may trade at a premium to payer swaptions. In a declining rate environment or when volatility is skewed toward downside, payer swaptions become relatively expensive.

Traders and hedgers monitor the cost differential as a signal of market sentiment about the direction and volatility of future rate moves.

## Comparing to Plain-Vanilla Swaps and Bonds

A payer swaption is not the same as entering a [swap](/swap/) today. A swap locks in the rate immediately; a payer swaption preserves optionality until the exercise date. The option value is insurance: the holder pays the premium but keeps the right to walk away if the market moves in their favor.

A receiver swaption is not the same as buying a [bond](/bond/) today, either. A bond purchase locks in the yield immediately and requires capital outlay. A receiver swaption preserves cash today (paying only the small option premium) and gives the holder the right to lock in a specific yield at a future date if rates fall.

This is why swaptions appeal to treasurers, investors, and asset managers with uncertain future financing or investment needs. They provide optionality—the ability to adapt to future rate environments without full commitment.

## Practical Use in Floating-Rate Debt Management

A company with a floating-rate [bank loan](/cost-of-debt/) linked to [SOFR](/sofr/) + 200 bp faces two risks: (1) SOFR could spike, and (2) the bank's credit spread could widen. A payer swaption on SOFR hedges the first risk. Once exercised, the company pays fixed + 200 bp instead of floating + 200 bp.

If the company also wants to cap the credit spread component, it might layer in a [cap](/interest-rate/) on the floating rate (a separate derivative) or negotiate a fixed-rate loan refinancing at a future date. Swaptions are often one tool in a multi-layered hedge.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — the underlying interest-rate swap contract
- [Interest-rate swap](/interest-rate-swap/) — the mechanics of fixed-for-floating exchange
- [Option](/option/) — the basic right to buy or sell
- [Call option](/call-option/) — conceptually parallel to payer swaption (both benefit from price increases)
- [Put option](/put-option/) — conceptually parallel to receiver swaption (both benefit from price decreases)
- [Option premium](/option-premium/) — upfront cost of the swaption

### Wider context

- [Interest rate](/interest-rate/) — the underlying market factor
- [SOFR](/sofr/) — the floating benchmark used in many swaps
- [Yield curve](/yield-curve/) — shapes relative value of payer vs. receiver swaptions
- [Implied volatility](/implied-volatility/) — key input in swaption pricing
- [Derivatives hedging](/derivatives-hedging/) — why treasurers buy swaptions
- [Credit spread](/credit-spread/) — complements swaption hedging for floating-rate debt

</div>

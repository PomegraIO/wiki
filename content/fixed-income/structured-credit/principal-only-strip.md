---
title: "Principal-Only Strip"
description: "A securitized mortgage strip that receives only principal repayments and gains value when rates fall and prepayments accelerate."
keywords:
  - mortgage-backed-security
  - securitization
  - prepayment-risk
  - structured-credit
  - fixed-income
  - interest-rate-risk
image: /svg/fixed-income.svg
---

*A **principal-only strip** (PO strip) is a derivative security created by separating the [mortgage-backed security](/mortgage-backed-security/) cash flow into principal and interest components. The PO strip holder receives only the principal payments (both scheduled and accelerated via prepayment) and benefits when interest rates fall—a sharp reversal of ordinary bond behaviour. As borrowers refinance or pay down mortgages faster, the PO strip principal value rises because the remaining loan balances prepay more quickly, delivering the capital gain sooner. This makes PO strips powerful [duration](/duration/) hedges but punishingly volatile for the unprepared.*

<div class="wiki-hatnote">

For the mortgage pool being divided, see [Mortgage-Backed Security](/mortgage-backed-security/). For the interest-only counterpart, see [Interest-Only Strip](/interest-only-strip/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Principal-Only Strip — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the fixed-income topic." />

<div class="wiki-infobox-caption">The principal-flow piece of a tranched mortgage security; its value swings directly with rate direction and prepayment risk.</div>

|   |   |
|---|---|
| **What it is** | A [securitized](/securitization/) claim to principal-only payments from a pool of mortgages |
| **Also called** | PO strip, principal coupon strip |
| **Issued from** | [Mortgage-backed securities](/mortgage-backed-security/), split into principal and interest flows |
| **Value driver** | Interest rates and [prepayment speed](/prepayment-speed/) (positive correlation) |
| **Core feature** | Gains value when rates fall and borrowers refinance; loses when rates rise |
| **Typical holder** | Hedge funds, mortgage specialists, short-duration traders, [duration](/duration/) hedgers |
| **Tax treatment** | Amortization discount accrual; market gain/loss on principal |

</aside>

## Carving principal from the cash flow

A [mortgage-backed security](/mortgage-backed-security/) consists of a pool of mortgages generating monthly payments of *principal + interest*. When a dealer [securitizes](/securitization/) these mortgages, they can separate the streams: one tranche gets all interest payments, another gets all principal payments. **The principal-only strip is the second tranche.** It receives zero interest income but owns the claim to every dollar of principal repaid—both the regular amortization and any early payoffs when homeowners refinance or sell.

This separation is purely mechanical. The mortgages themselves don't change; the cash flows are simply redirected to different investors. A PO strip holder never holds the underlying mortgages—they hold a contractual right to receive principal cash flow in a specific order (determined by [securitization](/securitization/) deal terms and any subordination).

## The inverse prepayment behaviour

The defining characteristic of a PO strip is its *positive* relationship to prepayment. When interest rates fall, homeowners refinance, and the mortgage principal is repaid early. This is terrible for [interest-only strips](/interest-only-strip/) (which lose future interest income) but excellent for PO strips: the principal comes back faster, shortening the bond's effective life *while rates are falling*. The investor receives their capital back in a rising-price environment, allowing them to reinvest at (theoretically) higher rates.

Example: You hold a PO strip backed by mortgages with 4.5% coupons. Mortgage rates drop to 3.5%. Homeowners rush to refinance. The underlying principal balances fall sharply—exactly when the market price of new mortgages has risen. Your PO strip, which was trading at a discount (because it was originally issued at par when rates were higher), gains price as prepayments accelerate. A 100-basis-point rate drop can easily drive a 20–40% price gain in a PO strip.

Conversely, when rates rise, refinancing stalls, the principal stays in place longer, and the PO strip duration extends. Your capital is locked in at a lower price, and you are earning 0% coupon while the market moves away from you. This can be painful in a rising-rate regime.

## Duration and convexity gone wild

PO strips exhibit extreme [negative convexity](/duration/). In standard bond terminology, convexity is the second-order price sensitivity to rate moves. Normal bonds have positive convexity: prices accelerate upward as rates fall (good for the bondholder) and decelerate as rates rise (bad, but less extreme). PO strips have *negative* convexity: prices accelerate upward as rates fall (fantastic) but also compress downward as rates rise (worse than a straight bond).

The [effective duration](/duration/) of a PO strip can be very short or even negative in certain rate scenarios. This makes them unwieldy tools for traditional portfolio construction. A 10-year mortgage PO might act like a 2-year instrument in a bull-market scenario and a 15-year instrument in a bear-market scenario.

## Why traders use PO strips as hedges

Sophisticated investors use PO strips as [duration](/duration/) hedges or short-duration bets. A fund manager who is long conventional long-duration bonds might short PO strips to neutralize duration while maintaining [credit risk](/credit-risk/) exposure. Conversely, a manager with a strong bullish (falling-rate) conviction might overweight PO strips because the asymmetry favours them: rates fall hard, they make money on the rate move *and* on the prepayment acceleration.

Some mortgage specialists build complex [hedging](/hedge-fund/) trades by pairing regular [mortgage-backed securities](/mortgage-backed-security/) (which suffer when rates fall) with long PO strips (which gain when rates fall). This isolates [volatility](/historical-volatility/) and credit views from rate direction.

## Valuation and market pricing

PO strips are priced using [option-adjusted spread](/interest-rate-risk/) (OAS) and prepayment-model frameworks. The dealer must forecast [prepayment speed](/prepayment-speed/) across a range of interest rate scenarios, typically using historical [PSA](/prepayment-speed/) curves or proprietary refinancing models. The price is heavily dependent on these prepayment assumptions, which means two dealers can quote the same PO strip at different prices if they disagree on refinancing behaviour.

This model risk is material. A PO strip priced assuming 150% PSA might look cheap at a 5% yield—until rates drop, refinancing hits 250% PSA, and the principal comes back in three years instead of seven. The bond's true return was much lower than quoted because the duration assumption was wrong.

## Liquidity and market depth

PO strips trade in a thinner secondary market than regular [mortgage-backed securities](/mortgage-backed-security/). Most issuance is absorbed by hedge funds, mortgage REITs, and insurance companies that are skilled at pricing prepayment risk. Retail investors rarely own PO strips directly. Bid-ask [spreads](/bid-ask-spread/) range from 5 to 25 basis points depending on pool composition and market conditions, which is wide compared to Treasury bonds but normal for mortgage derivatives.

Large trades can move the market, and forced sellers (such as a troubled [mortgage REIT](/mortgage-reit/)) can generate temporary price dislocation. This creates opportunity for patient, well-capitalized buyers.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Only Strip](/interest-only-strip/) — the complementary strip receiving only interest cash flows
- [Mortgage-Backed Security](/mortgage-backed-security/) — the underlying pool of mortgages being stripped
- [Prepayment Speed](/prepayment-speed/) — the PSA or CPR measure used to forecast principal repayment rates
- [Securitization](/securitization/) — the process of separating and selling cash-flow tranches
- [Duration](/duration/) — the interest-rate sensitivity measure, inverted for PO strips
- [Negative Convexity](/duration/) — the asymmetric price behaviour of PO strips across rate scenarios
- [Option-Adjusted Spread](/interest-rate-risk/) — the valuation framework for rate-sensitive mortgages

### Wider context

- [Bond](/bond/) — basic fixed-income security and pricing mechanics
- [Mortgage-Backed Security](/mortgage-backed-security/) — foundational mortgage derivative
- [Hedge Fund](/hedge-fund/) — typical institutional holder and sophisticated user
- [Mortgage REIT](/mortgage-reit/) — real-estate investment trust often holding PO and IO strips
- [Interest-Rate Risk](/interest-rate-risk/) — the dominant risk in mortgage derivatives

</div>

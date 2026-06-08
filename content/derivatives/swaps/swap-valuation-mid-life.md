---
title: "How an Interest Rate Swap Is Valued After Inception"
description: "Learn how to value an interest rate swap mid-life using discounted cash flows as rates move, creating positive or negative mark-to-market after trade date."
keywords:
  - how to value an interest rate swap mid-life
  - swap valuation methods
  - mid-life swap pricing
  - interest rate swap mark-to-market
  - discounted cash flow swap valuation
image: /svg/derivatives.svg
---

*Immediately after an **interest rate swap** starts, rising or falling rates create value for one party and loss for the other—even though both legs looked equal at inception. Mid-life valuation measures exactly how much that mark-to-market has shifted, using the same discounted cash flow logic that prices bonds.*

<div class="wiki-hatnote">

This entry covers the practical mechanics of marking a swap to market partway through its life. For how payments are calculated each period, see [Fixed-for-floating swap payment mechanics](/fixed-for-floating-swap-mechanics/). For the default risk that arises when a swap gains value, see [Counterparty credit risk in swaps](/swap-counterparty-credit-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Mid-Life Valuation — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A swap's value changes whenever the discount rates used to price its remaining cash flows shift.</div>

|   |   |
|---|---|
| **Core idea** | Revalue fixed and floating legs separately at current market rates, then take the difference. |
| **Fixed leg valuation** | Discount all remaining fixed coupons at the current fixed rate curve. |
| **Floating leg valuation** | Discount all remaining floating payments at the current [spot rates](/spot-rate/) or [LIBOR](/libor/) curve. |
| **Net swap value** | Fixed leg PV minus floating leg PV (from the fixed-rate payer's perspective). |
| **Mark direction** | Falling rates help the fixed payer; rising rates help the floating payer. |
| **Why it matters** | Determines [counterparty credit risk](/swap-counterparty-credit-risk/), collateral requirements, and reported profit or loss. |

</aside>

## The Swap Starts at Par

On the trade date, both legs of a [fixed-for-floating swap](/fixed-for-floating-swap-mechanics/) are worth exactly the same. The fixed rate—called the swap rate—is set so that the discounted value of all future fixed payments equals the discounted value of all expected floating payments. This is par: each party pays present value for present value received.

As soon as market interest rates move, that equality breaks. If rates fall, the fixed-rate payer (who committed to pay a rate that now looks generous) gains value. If rates rise, the floating-rate payer (who will now receive floating payments worth more than the fixed coupons) comes out ahead. One party's gain is the other's loss—a zero-sum revaluation.

## Revalue Each Leg Independently

To mark a swap to market mid-life, treat the two legs as separate instruments and price them at current rates.

**Fixed leg:** Take every remaining fixed coupon and discount it to present value using the current fixed-rate curve. If the swap had five years to maturity at inception and two years have passed, discount the remaining three years of fixed payments at the three-year, two-year, and one-year spot rates applicable on the valuation date.

**Floating leg:** Discount all remaining floating payments at the current floating-rate curve. For an [LIBOR](/libor/)-based swap, use the current LIBOR forward curve (the market's expectation of LIBOR rates for each period ahead). The next floating payment is usually known (or recently fixed) and discounted by the shortest tenor; future payments, which haven't yet been set, are discounted by their respective forward LIBOR rates.

**Net value:** The swap's mark-to-market is the fixed leg's present value minus the floating leg's present value. If the result is positive, the fixed-rate payer is in profit; if negative, they owe value to the other party.

## A Worked Example

Assume a five-year, $100 million fixed-for-floating USD LIBOR swap was initiated three years ago. The fixed rate was 3.00%, paid annually. The current date is just before the fourth annual payment.

**Market snapshot (valuation date):**
- Current one-year spot rate: 4.50%
- Current two-year spot rate: 4.25%
- Current forward one-year LIBOR: 4.75%
- Current forward two-year LIBOR: 4.50%

**Remaining fixed payments:** $3.00 million in one year, and $3.00 million in two years (at maturity, the notional is also repaid; for clarity, assume it's exchanged separately).

**Fixed leg PV:**
- Year 1 payment: $3.00M ÷ (1 + 0.045) = $2.87M
- Year 2 payment: $3.00M ÷ (1 + 0.0425)² = $2.75M
- Fixed leg PV = $5.62M

**Floating leg remaining payments:** Unknown, but discounted at forward rates.
- Year 1 floating: $100M × 0.0475 = $4.75M; PV = $4.75M ÷ 1.045 = $4.54M
- Year 2 floating: $100M × 0.045 = $4.50M; PV = $4.50M ÷ (1.0425)² = $4.13M
- Floating leg PV = $8.67M

**Swap mark-to-market:** $5.62M − $8.67M = **−$3.05M**

The fixed-rate payer is underwater by $3.05 million. They locked in 3.00% when market rates have risen to 4.50%+, making their fixed payments less attractive. If the swap is terminated, they must pay $3.05 million to walk away.

## The Valuation Depends on Rate Assumptions

The floating leg's present value hinges on forward rate expectations. Market practitioners often use the current [forward rate](/forward-guidance/) curve (derived from [futures contracts](/futures-contract/) and [swaps](/swap/) themselves) as the baseline. Some use [SOFR](/sofr/) curves now that LIBOR is being phased out.

The exact market rates and conventions—day count, compounding frequency, whether the next floating coupon has already been set—matter for precision. But the principle is universal: revalue both legs at current market rates and take the difference.

## Why This Valuation Matters in Practice

**Collateral and credit exposure:** As a swap's mark-to-market swings, the in-the-money party accumulates [counterparty credit risk](/swap-counterparty-credit-risk/). If the swap is collateralized (as most dealer swaps are now), the losing party must post cash or securities daily to cover the mark.

**Termination economics:** If one party wants to unwind the swap early, the mark-to-market determines the cash settlement. The party with a positive mark receives a payment equal to that amount.

**Financial reporting:** Under IFRS 9 and ASC 815, derivatives are marked to market in the financial statements. The mid-life swap valuation directly impacts reported gains and losses.

**Hedge accounting:** If a swap qualifies as a [hedge](/derivatives-hedging/), its changing value is often deferred in equity rather than flowing through earnings immediately, subject to effectiveness tests.

## Mark-to-Market Is Relative to Par

It's crucial to remember that "par" is reset every time the swap is repriced. When a swap is created, the counterparties lock in a rate such that both legs are worth the same. As rates move, one leg becomes more valuable and the other less so. The valuation captures that shift. If rates move back to the original level, the mark typically returns to zero.

## See also

<div class="wiki-seealso">

### Closely related

- [Fixed-for-floating swap payment mechanics](/fixed-for-floating-swap-mechanics/) — How each period's net payment is calculated
- [Counterparty credit risk in swaps](/swap-counterparty-credit-risk/) — Why gaining value in a swap exposes you to default risk
- [Swap vs forward rate agreement](/swap-vs-forward-rate-agreement/) — How swaps and FRAs differ in valuation and use
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — The PV framework used to price both legs

### Wider context

- [Interest rate swap](/interest-rate-swap/) — Introduction to how swaps hedge or speculate on rate changes
- [Derivatives hedging](/derivatives-hedging/) — Why companies use swaps to manage exposure
- [Credit risk](/credit-risk/) — General principles of default exposure
- [Spot rate](/spot-rate/) — The discount rates used in valuation
- [LIBOR](/libor/) — The floating rate benchmarked in classic swaps

</div>

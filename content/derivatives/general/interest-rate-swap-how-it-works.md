---
title: "Interest Rate Swap: How the Fixed-for-Floating Exchange Works"
description: "How interest rate swaps exchange fixed-rate and floating-rate payments, with a step-by-step example of cash flows and the economics driving both sides."
keywords:
  - interest rate swap how it works
  - fixed-for-floating swap
  - swap cash flows
  - plain vanilla swap mechanics
image: "/svg/derivatives.svg"
---

*An **interest rate swap** is a derivatives contract in which one party agrees to pay a fixed rate of interest on a notional principal, while the other pays a floating rate tied to a [benchmark index](/sofr/) such as SOFR. No principal changes hands—only the difference in interest payments is exchanged. Swaps allow borrowers to change the character of their debt or investors to hedge [interest rate risk](/interest-rate-risk/), and they are the largest [derivatives](/derivatives-hedging/) market by notional value.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Swap Mechanics — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A direct exchange of fixed and floating interest payments on a notional principal.</div>

|   |   |
|---|---|
| **Notional principal** | The fictional balance on which rates are applied; principal itself is never exchanged |
| **Fixed payer** | Party committed to pay a fixed rate; receives floating-rate payment |
| **Floating payer** | Party pays a floating rate (e.g., SOFR + spread); receives fixed payment |
| **Settlement** | Interest differential paid every 3 or 6 months; only net cash flows occur |
| **Common tenors** | 2, 5, 10, and 30-year terms; longer terms are illiquid |
| **Pricing** | Fixed rate determined at initiation so swap has zero initial value |

</aside>

## Why Swaps Exist and Who Uses Them

A bank borrows at floating rates because customers demand floating deposits. But the bank may prefer to lock in a predictable cost. Without a swap, it must refinance at [SOFR](/sofr/) every quarter. With a swap, it pays a fixed rate to a counterparty and receives floating, mathematically converting its liability.

A corporate treasurer may have issued fixed-rate bonds but now wants floating exposure to match floating revenues. A swap converts the bond's cost from fixed to floating.

An asset manager holding floating-rate notes may want fixed income certainty. The manager can enter a swap to pay floating and receive fixed.

The swap dealer (usually a bank) profits by quoting a bid-ask spread—the fixed rate the dealer will pay is slightly lower than the fixed rate it will receive.

## The Mechanics: A Plain-Vanilla Swap

Parties agree on:
- **Notional:** $10 million
- **Tenor:** 5 years
- **Payment frequency:** Every 6 months
- **Fixed rate:** 5.00% per annum (0.05)
- **Floating index:** SOFR
- **Floating spread:** +0.30% (0.003)

There are 10 semiannual periods (6 months × 5 years).

**Party A (fixed payer):** Commits to pay fixed; receives floating. Party A is hedging against floating-rate increases or converting fixed borrowings to floating.

**Party B (floating payer):** Commits to pay floating; receives fixed. Party B wants certainty or is converting floating debt to fixed.

### Cash Flow on Period 1 (Month 6)

Suppose SOFR averaged 4.70% over the first 6-month period.

- **Party A pays fixed:** 5.00% × $10M × (180/360) = $250,000
- **Party B pays floating:** (4.70% + 0.30%) × $10M × (180/360) = 5.00% × $10M × (180/360) = $250,000

Net exchange: Both pay $250,000. No cash flows occur because the rates are equal at period 1.

### Cash Flow on Period 3 (Month 12)

Suppose SOFR averaged 4.20% during the second 6-month period.

- **Party A pays fixed:** 5.00% × $10M × (180/360) = $250,000
- **Party B pays floating:** (4.20% + 0.30%) × $10M × (180/360) = 4.50% × $10M × (180/360) = $225,000

Party B owes $25,000 less than Party A. Net settlement: Party A pays Party B $25,000.

### Cash Flow on Period 5 (Month 18)

Suppose SOFR averaged 5.40% during the third 6-month period.

- **Party A pays fixed:** 5.00% × $10M × (180/360) = $250,000
- **Party B pays floating:** (5.40% + 0.30%) × $10M × (180/360) = 5.70% × $10M × (180/360) = $285,000

Party B owes $35,000 more than Party A. Net settlement: Party B pays Party A $35,000.

The swap continues for 10 periods. In each period, one party pays the difference in interest costs. No principal is transferred.

## Why the Fixed Rate Is Set at Initiation

When the swap is struck, the fixed rate is set so the swap has zero initial value. That is, the [discounted](/discount-rate/) present value of expected fixed payments equals the [discounted](/discount-rate/) present value of expected floating payments.

If SOFR is expected to average 4.70% over the 5-year period and the spread is 0.30%, the fair fixed rate is approximately 5.00%. Party A and Party B each view the deal as fair because neither is giving up value at entry.

After initiation, if [interest rates](/interest-rate/) rise, the fixed payment becomes cheaper relative to future floating payments, and the swap gains value for Party A (the fixed payer). If rates fall, the swap gains value for Party B.

## Hedging Interest-Rate Risk

A large pension fund holds $100 million in floating-rate corporate bonds. Floating coupons reset every quarter. The fund worries rates will fall, reducing future coupon income.

The fund enters a $100 million, 5-year interest-rate swap as the floating payer—agreeing to pay floating and receive fixed (5.00%). This locks in 5% income on the notional amount, regardless of where SOFR moves.

If SOFR falls to 3.00%, the bonds' coupons drop but the swap pays the fund the difference (5% − 3% = 2% of notional), offsetting the loss. The fund is hedged.

Similarly, a borrower with floating debt can hedge by paying fixed via a swap, ensuring a maximum [cost of debt](/cost-of-debt/).

## Counterparty and Settlement Risk

Each party faces counterparty risk: if the other party defaults, it may owe substantial cash. Early termination or collateral posting mitigates this. Most swaps now clear through central counterparties, which reduce bilateral risk.

Settlement is typically net—only the difference in interest is exchanged, not both sides' full amounts. This lowers operational risk and cash requirements.

## Variations and Extensions

**Basis swaps** exchange two floating rates (e.g., SOFR vs. EURIBOR) instead of fixed for floating.

**Cross-currency swaps** exchange fixed or floating payments in different currencies, combining [interest-rate risk](/interest-rate-risk/) and [currency risk](/currency-risk/).

**Swaptions** are options on swaps—the right to enter a swap at a future date at a rate agreed today.

**Amortizing swaps** reduce notional principal over time (used to hedge amortizing loans).

**Inflation swaps** exchange fixed payments against inflation indexes, used by pension funds and real-assets investors.

## See also

<div class="wiki-seealso">

### Closely related

- [Derivatives and Hedging](/derivatives-hedging/) — Broad overview of hedging tools and strategies
- [SOFR](/sofr/) — The floating benchmark replacing LIBOR in many swaps
- [Interest Rate Risk](/interest-rate-risk/) — What rate swaps protect against
- [Forward Rate Agreement](/interest-rate-swap-how-it-works/) — Single-period sibling to the swap
- [Swap Pricing and Valuation](/interest-rate-swap-how-it-works/) — How swaps are marked to market

### Wider context

- [Discount Rate](/discount-rate/) — Principle behind swap valuation
- [Cost of Debt](/cost-of-debt/) — Using swaps to manage financing costs
- [Central Bank](/central-bank/) — How monetary policy affects swap rates
- [Counterparty Risk](/counterparty-risk/) — Risk management in derivatives markets

</div>

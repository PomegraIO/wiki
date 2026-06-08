---
title: "Swap Upfront Fee vs Par Swap: How Off-Market Swaps Work"
description: "Off-market swap upfront payment explained: why swaps are structured with cash at inception instead of at-market rates, how the fee is calculated, and when they're used."
keywords:
  - off-market swap upfront payment
  - swap upfront fee
  - par swap
  - swap valuation
  - loan hedge restructuring
image: /svg/derivatives.svg
---

*An **off-market swap** is one where the fixed rate (or other terms) differs from the current market rate, requiring an upfront cash payment to compensate the disadvantaged party—a structure commonly used in loan hedges, refinancings, and restructurings where aligning with market rates would be expensive or impractical.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Off-Market Swaps — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">When swap terms aren't at-market, cash flows at inception.</div>

|   |   |
|---|---|
| **Par swap** | Both parties' terms are at current market rates; no upfront payment |
| **Off-market swap** | One party's rate is better/worse than market; upfront fee compensates |
| **Upfront fee** | Present value of the difference between contract rate and market rate |
| **Common triggers** | Loan refinancing, hedging existing debt, credit event restructuring, lender accommodation |
| **Who pays** | Party receiving the more favorable rate pays upfront to the other |
| **Mechanics** | Upfront fee is lump-sum cash transfer at swap inception |
| **Tax treatment** | Upfront fee is typically capitalized into [cost basis](/cost-basis/) and amortized over swap life |

</aside>

## Par Swaps and Market Rates

In a standard interest-rate [swap](/interest-rate-swap/), two parties exchange cash flows based on fixed and floating [interest rates](/interest-rate/). The parties agree on a fixed rate and a floating-rate index (e.g., [SOFR](/sofr/)). On each reset date, the party paying fixed sends cash to the floating-rate payer if rates have fallen, and vice versa.

A **par swap** (or at-market swap) is one where both parties' legs are fairly valued relative to the market rate observed at the time the swap is negotiated. Neither party has an advantage; both are trading at the current cost of [fixed-rate](/fixed-rate-mortgage-personal/) capital or floating-rate exposure.

The swap [fixed rate](/coupon-rate/) on a par swap is the rate that makes the [present value](/discounted-cash-flow-valuation/) of fixed cash flows equal to the present value of floating cash flows, given current market conditions. If a bank quotes a five-year USD interest-rate swap fixed rate of 4.50% against three-month [SOFR](/sofr/), and a borrower accepts that 4.50%, the swap is at-market. No upfront payment is needed; both sides have equal [economic value](/enterprise-value/).

## Off-Market Swaps and Upfront Payments

An **off-market swap** intentionally deviates from the at-market rate. The fixed rate might be higher or lower than what the current market would demand. This creates a mismatch: one party is getting a better deal than the market would offer.

To balance that asymmetry, the disadvantaged party receives a cash payment at inception. The upfront fee is calculated as the [present value](/discounted-cash-flow-valuation/) of the cumulative advantage the other party receives over the life of the swap.

**Example:** A borrower is refinancing a five-year loan at a floating rate of SOFR + 1.50%. The loan balance is $50 million. The current market [fixed rate](/coupon-rate/) for a five-year USD swap is 4.50%, but the borrower wants to pay fixed at 4.25% instead (25 basis points lower than market).

To compensate the swap counterparty for accepting a below-market fixed rate, the borrower pays an upfront fee. That fee is roughly the [present value](/discounted-cash-flow-valuation/) of 25 basis points per year for five years, applied to the $50 million notional:

- Annual cost advantage: 0.0025 × $50M = $125,000 per year
- Rough PV of five years of $125,000 (at 4.50% discount rate): ~$540,000

The borrower receives the $50 million loan and enters the swap, but also pays the counterparty $540,000 upfront. This is the **upfront fee**.

## Why Borrowers Accept Off-Market Terms

Off-market swaps arise in contexts where paying an upfront fee is more practical than negotiating at-market rates:

**Loan restructuring and refinancing.** A borrower with an existing loan that has unfavorable terms may refinance with a new lender. Rather than renegotiating rate spreads with the original lender, the borrower takes a new loan at market terms and enters a swap to synthetically recreate the original terms (or improve them). The upfront fee is a one-time negotiation cost.

**Credit event hedging.** After a credit downgrade, a borrower's cost of borrowing rises. If the borrower wants to lock in a lower fixed rate than the current market, it pays an upfront fee to do so. This is especially common in leveraged finance and when firms are under duress.

**Lender accommodation and retention.** A bank may offer a below-market swap rate to retain a valuable client, with the fee compensating the bank for the concession. This is less formal than renegotiating the underlying loan, and avoids drawing the attention of credit rating agencies.

**Loan portfolio hedging.** A financial institution holding a portfolio of floating-rate loans may enter swaps to hedge interest-rate exposure. If the bank wants to hedge at rates better than current market (e.g., to lock in a spread assumption in its [business model](/business-cycle/)), it pays an upfront fee.

## Calculating the Upfront Fee

The upfront fee is derived from a **swap valuation model**. At any point in time, a swap has a market value—the amount a third party would pay (or require you to pay) to take over your position. For a new swap initiated at market rates, that value is zero by definition. For an off-market swap, that initial value is non-zero.

The upfront fee equals the absolute value of the swap's net [present value](/discounted-cash-flow-valuation/):

**Upfront Fee = PV(fixed leg) − PV(floating leg)**

Where:

- **PV(fixed leg)** is the discounted value of all fixed cash flows the fixed-rate payer will send.
- **PV(floating leg)** is the discounted value of all floating cash flows.

If the fixed rate is below market (better for the floating payer), then PV(fixed leg) is lower, and the result is negative. The absolute value is the fee the fixed-rate payer (the borrower) must remit.

The discount rate used is typically the risk-free curve (e.g., OIS or [SOFR](/sofr/) term structure) plus a [credit spread](/credit-spread/) reflecting both parties' [counterparty risk](/counterparty-risk/).

## Tax and Accounting Implications

For the party **paying** the upfront fee, the fee is typically capitalized as a deferred cost and amortized into [interest expense](/interest-coverage-ratio/) over the swap's maturity. Under [ASC 815](/asc-606/) (derivatives and hedging), if the swap qualifies as a cash-flow hedge of floating-rate debt, the upfront fee is deferred and amortized symmetrically with the swap's cash flows.

**Example continuation:** The borrower pays $540,000 upfront. Over the five-year swap life, this $540,000 is amortized to [interest expense](/interest-coverage-ratio/) in line with the swap's cash flows, reducing the synthetic [cost of debt](/cost-of-debt/) to the borrower.

For the party **receiving** the upfront fee, the fee is typically recognized as [revenue](/revenue-recognition/) over the swap's life, offset by the below-market rate received. The net effect on [earnings](/earnings-per-share/) is small; the upfront fee is largely a timing matter.

## Par Swaps vs. Off-Market Swaps in Practice

Most plain-vanilla interest-rate swaps initiated between a bank and a corporate borrower start as **par swaps**. The borrower asks for a rate, the bank quotes its at-market rate, and they trade. No upfront payment.

Off-market swaps are more common in:

- **Loan-level hedging**: A borrower refinancing an existing loan may hedge the new loan's floating-rate risk with an off-market swap to replicate historical rates.
- **Bilateral negotiations**: In illiquid or customized deals, one party may concede on rate in exchange for an upfront payment.
- **Portfolio management**: Asset managers and hedge funds routinely buy and sell off-market swaps (by taking or selling positions at non-par rates, equivalent to accepting an upfront fee in reverse).

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate swap](/interest-rate-swap/) — mechanics, pricing, and use cases of vanilla swaps
- [Swap pricing and valuation](/discounted-cash-flow-valuation/) — how swaps are valued over time
- [Counterparty risk](/counterparty-risk/) — exposure from derivative positions with banks
- [Cash-flow hedging](/derivatives-hedging/) — accounting treatment of hedges and deferred items
- [Fixed-rate mortgages and loan refinancing](/fixed-rate-mortgage-personal/) — why borrowers refinance and hedge
- [Credit spreads](/credit-spread/) — impact of credit quality on borrowing costs and hedge prices

### Wider context

- [Derivatives fundamentals](/option/) — swap, forward, and option mechanics
- [Hedging strategies](/derivatives-hedging/) — use of derivatives to reduce risk
- [Cost of debt](/cost-of-debt/) — how interest expense affects firm valuation
- [Accounting for derivatives](/asc-606/) — ASC 815, hedge accounting, and mark-to-market

</div>

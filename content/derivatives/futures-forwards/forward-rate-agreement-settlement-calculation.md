---
title: "Forward Rate Agreement Settlement Calculation"
description: "How the cash settlement of an FRA is computed using the contract rate, reference rate, notional principal, and day-count convention."
keywords:
  - forward rate agreement settlement
  - forward rate agreement calculation
  - FRA settlement
  - interest rate forward
  - cash settlement derivative
image: "/svg/derivatives.svg"
---

*A **forward rate agreement (FRA) settlement** is a cash payment computed at the fixing date to make whole the party disadvantaged by the gap between the agreed contract rate and the market reference rate (usually SOFR or its predecessor LIBOR). The calculation pins the notional principal amount, accrual period, day-count fraction, and difference between rates into a single formula.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FRA Settlement Calculation — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A standardized cash settlement tied to rate fixing and notional sizing.</div>

|   |   |
|---|---|
| **Settlement timing** | Usually one or two business days after fixing date |
| **Key inputs** | Contract rate, reference rate (e.g., [SOFR](/sofr/)), notional, day-count |
| **Formula** | Notional × (Reference − Contract) × Day-count fraction / (1 + Reference × Day-count) |
| **Who pays** | Buyer pays seller if reference > contract; otherwise seller pays buyer |
| **Discount factor** | Accounts for time value; settles present value today, not at maturity |
| **Day-count convention** | Typically ACT/360 or 30/360; stated in trade confirmation |

</aside>

## The economic logic

An FRA locks in an interest rate for a future period. If you buy a 3×6 FRA (fixing in 3 months, maturity in 6 months), you have agreed to "pay" the contract rate on a notional principal and "receive" the market reference rate. When the fixing date arrives, the reference rate is set. If the reference rate is higher than your contract rate, you win—you receive a cash payment equal to the difference. If lower, you lose and must pay.

The settlement is a present-value adjustment made immediately after fixing, not a deferred payment at the end of the accrual period. This matters: if rates fell, the buyer of the FRA is owed money, but that money is valuable today, not six months from now. The formula discounts it.

## The standard formula

Most FRAs settle via:

**Settlement Payment = Notional × [Reference Rate − Contract Rate] × (Day Count / Year Basis) / [1 + Reference Rate × (Day Count / Year Basis)]**

Let's break each component:

- **Notional principal**: The face amount on which interest is calculated. Usually in millions (e.g., USD 10 million). Not exchanged; only interest is settled.
- **Reference rate − contract rate**: The "spread" in basis points (typically quoted as, e.g., SOFR flat, meaning the contract rate is whatever SOFR is on the fixing date). If SOFR at fixing is 5.50% and the contract rate was 5.25%, the spread is +0.25% (25 basis points).
- **Day-count fraction**: The number of days in the accrual period divided by the year basis. For a 3-month period (91 days), using ACT/360: 91/360 = 0.2528.
- **Year basis**: Almost always 360 for USD FRAs (ACT/360 convention); sometimes 365 for GBP or EUR (Actual/365).
- **Discount factor** [1 + Reference Rate × Day-count]: Converts the interest payable at the end of the accrual period into its present value, using the reference rate as the discount rate.

## Worked example

**Trade details:**
- Buyer of a 3×6 GBP FRA
- Notional principal: GBP 5,000,000
- Contract rate (fixed at deal time): 5.00%
- Fixing date: 3 months from now
- Reference rate (SOFR) at fixing: 5.35%
- Day-count convention: ACT/360
- Accrual period: 92 calendar days (from month 3 to month 6)

**Step 1: Calculate the rate difference**
5.35% − 5.00% = 0.35% (or 35 basis points)

**Step 2: Calculate the day-count fraction**
92 days / 360 days = 0.2556

**Step 3: Calculate interest difference (not yet discounted)**
5,000,000 × 0.0035 × 0.2556 = 4,480 GBP

**Step 4: Build the discount factor**
1 + 0.0535 × 0.2556 = 1 + 0.01367 = 1.01367

**Step 5: Discount to present value**
4,480 / 1.01367 = 4,422 GBP

**Settlement Payment = 4,422 GBP** (paid by seller to buyer, since the reference rate was higher than the contract rate)

## When the reference rate is lower

If the reference rate at fixing had been 4.80% (lower than the 5.00% contract rate):

**Step 1:** 4.80% − 5.00% = −0.20% (−20 basis points)
**Step 2:** 92 / 360 = 0.2556
**Step 3:** 5,000,000 × (−0.0020) × 0.2556 = −2,556 GBP
**Step 4:** Discount factor = 1 + 0.0480 × 0.2556 = 1.01227
**Step 5:** −2,556 / 1.01227 = −2,524 GBP

The buyer would **owe 2,524 GBP** to the seller.

## The role of the discount factor

The discount factor is the linchpin. It converts a future interest obligation into a present cash payment. Why? Because if you were to wait until the end of the accrual period for settlement, you'd be holding cash idle that could be invested at the reference rate. The discount factor deducts that opportunity cost, ensuring both parties get fair value today.

In the first example, the undiscounted interest difference was 4,480 GBP. Discounting reduced it to 4,422 GBP—a 58 GBP haircut. With higher reference rates, the discount factor grows larger (future value is worth less in today's money), and vice versa.

## Day-count conventions and regional variation

The day-count convention is crucial because it affects both the interest fraction and, in many cases, how the actual days are counted.

- **ACT/360** (actual/360): Count actual calendar days; divide by 360. Standard for USD [SOFR](/sofr/) FRAs and most money-market instruments.
- **30/360**: Assume each month has 30 days and each year has 360. Simplifies but introduces rounding. Used in some corporate bond markets.
- **ACT/365** (actual/365): Count actual calendar days; divide by 365. Sometimes used for GBP or EUR.

A 3-month period might be 91, 92, or 93 days depending on the calendar. Using ACT/360, this makes a small but measurable difference in the settlement amount.

## Settlement timing and discrepancies

Most FRAs settle on a T+0 or T+1 basis (same day or next business day after fixing). The fixing itself—determination of the reference rate—typically occurs at a standard time (e.g., 11:00 a.m. London time for GBP SOFR) on a specified date. Once fixed, the settlement is mechanical: plug the numbers in, calculate, and transfer cash.

In rare cases, disputes arise over the fixing reference. For [SOFR](/sofr/) and other regulated benchmarks, the fixing administrator publishes an official rate. For legacy LIBOR, before its discontinuation, the rate was polled from banks, and disputed fixings could trigger litigation. Most modern FRAs reference SOFR, which is transaction-based and harder to manipulate, reducing settlement disputes.

## See also

<div class="wiki-seealso">

### Closely related

- [SOFR](/sofr/) — the standard reference rate for USD FRAs
- [Repurchase agreement](/repurchase-agreement/) — similar cash-settled instrument for short-term lending
- [Interest-rate swap](/interest-rate-swap/) — longer-dated version of the FRA concept, often with multiple notional periods
- [Forward contract](/forward-contract/) — broader class of derivatives of which FRAs are a subset
- [Basis risk](/basis-risk/) — the risk that the reference rate diverges from the borrower's actual cost

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — how FRAs fit into larger hedging strategies
- [Counterparty risk](/counterparty-risk/) — settlement risk and credit exposure
- [Monetary policy](/monetary-policy/) — how central-bank rate decisions drive FRA pricing
- [Capital-adequacy](/capital-adequacy/) — regulatory capital charges for FRA positions

</div>

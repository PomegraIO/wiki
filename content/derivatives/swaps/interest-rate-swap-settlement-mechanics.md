---
title: "Interest Rate Swap Settlement Mechanics"
description: "How interest rate swap settlement works: net cash flows, day-count conventions, fixing dates, and why only the difference is exchanged rather than notional amounts."
keywords:
  - interest rate swap settlement
  - how does interest rate swap settlement work
  - swap cash flow mechanics
  - fixing date swap
  - accrued interest swap
image: /svg/derivatives.svg
---

*Interest rate swap settlement is the process by which two counterparties exchange **only the difference** in interest payments on a notional principal amount at each payment date. Rather than swapping gross interest payments, they net them into a single cash flow paid by whichever party owes more, using standardized day-count conventions and reset dates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Swap Settlement — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and swaps." />

<div class="wiki-infobox-caption">Only the net difference in interest is paid, reducing counterparty risk and settlement friction.</div>

|   |   |
|---|---|
| **Settlement type** | Net cash flow (not gross principal exchange) |
| **Payment frequency** | Typically quarterly or semi-annual |
| **Key date** | Fixing date (1–3 days before payment date) |
| **Day-count method** | Actual/360 (floating) or 30/360 (fixed) |
| **Typical contract length** | 2 to 30 years |
| **Counterparty exposures** | Interest rate risk, not notional principal risk |

</aside>

## The Swap Settlement Flow

On each settlement date, neither party actually hands over the full notional principal (say, $10 million). Instead, they:

1. **Fix the floating rate** on a designated fixing date (typically 1–3 business days before the settlement date).
2. **Calculate accrued interest** for each leg using the agreed day-count convention.
3. **Net the two interest payments** against each other.
4. **Transfer only the net difference** from one party to the other.

For example, if Party A owes the fixed-rate receiver $100,000 in interest and Party B owes Party A $85,000 on a floating rate, Party B sends Party A a net of $15,000. This netting reduces settlement volume, lowers counterparty risk, and simplifies accounting.

## Fixing Dates and Rate Reset

The **fixing date** is when the floating rate is locked in for that settlement period. On a swap referencing SOFR, the fixing date is typically 1–3 business days before settlement, allowing time for rate data to be published and calculations to complete. On older swaps using LIBOR, fixing dates followed similar conventions but with published LIBOR fixings at specific times.

The rate used is the **market rate on that fixing date**, not the current day's rate. This protects both parties from last-minute rate surprises and keeps the settlement process orderly. Most swaps reset quarterly or semi-annually, though some institutional deals may reset monthly or even daily.

## Day-Count Conventions

The number of days in each period is calculated using one of several standard methods. The two most common are:

- **Actual/360**: Used for floating-rate legs. Count the actual number of calendar days in the period and divide by 360. Widely used for USD SOFR swaps.
- **30/360**: Used for fixed-rate legs. Assume each month has 30 days and each year has 360 days, simplifying arithmetic. Common in corporate bonds and fixed-rate swap legs.

These conventions matter because they affect the dollar amount owed. A six-month period of 184 actual days, divided by 360, gives a different interest factor than dividing 180 calendar days by 360. Swap confirmations always state which convention applies to each leg.

## Net Settlement vs. Gross Settlement

Under **net settlement**, counterparties exchange only the difference. A $10 million notional swap with fixed at 3% and floating at 2.5% results in one party owing 0.5% of $10 million (adjusted for day count) to the other—a few thousand dollars, not millions.

**Gross settlement** would involve exchanging all interest due on both sides (the $300,000 and the $250,000), then one party paying back the difference. Net settlement is vastly more efficient and has been standard market practice for decades.

This netting is also the reason interest rate swaps carry relatively low **counterparty risk** compared to their notional size. The true exposure is the difference in interest payments, plus any mark-to-market value, not the underlying principal.

## Settlement Mechanics: Step by Step

On a typical quarterly settlement date:

1. **T-3 or T-2 (fixing day)**: The floating rate is set. For a SOFR swap, the relevant SOFR fixing is published and locked.
2. **T-0 (settlement date)**: Accrued interest is calculated for both legs using the day-count method.
3. **Net calculation**: Fixed-leg interest minus floating-leg interest = net amount.
4. **Payment**: The party owing the net amount transfers funds (usually by wire) to the other party.

Swap settlements are typically settled in cash on the settlement date, though settlement can occasionally be delayed if market disruptions occur. Standard market documentation (ISDA Master Agreements) governs all these mechanics and provides fallback rules for calendar holidays and weekends.

## Why Settlement Works This Way

Net settlement exists for three practical reasons:

**Efficiency**: Exchanging only the difference is faster and cheaper than moving gross amounts across both legs.

**Risk reduction**: Counterparty exposure is capped at the net payment, not the notional principal.

**Market function**: A swap's value swings daily, but settlement happens only on fixed dates. Netting isolates interest-rate exposure (the intended trade) from unnecessary operational friction.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/interest-rate-swap/) — the basic structure and purpose of the contract
- [Counterparty Risk](/counterparty-risk/) — why netting reduces settlement exposure
- [SOFR](/sofr/) — the modern benchmark rate used in US interest rate swap fixings
- [Swap](/swap/) — the broader category of swap contracts and their mechanics
- [Duration](/duration/) — how to measure sensitivity of the swap's value to rate changes
- [Federal Funds Rate](/federal-funds-rate/) — the policy rate that anchors floating-rate swaps

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why corporates and investors use swaps to manage rate risk
- [Monetary Policy](/monetary-policy/) — how central bank rate decisions affect swap rates
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulates swap markets and disclosure

</div>

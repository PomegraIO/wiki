---
title: "Fixed-for-Floating Swap: Payment Mechanics Explained"
description: "See exactly how net settlement payments are calculated in a fixed-for-floating swap, with a worked numerical example showing who pays whom."
keywords:
  - fixed for floating swap payment mechanics
  - how swap payments are calculated
  - interest rate swap settlement
  - swap net payment calculation
  - floating rate swap example
image: /svg/derivatives.svg
---

*In a **fixed-for-floating swap**, each party owes interest to the other on the same notional amount, but at different rates. Rather than exchange gross payments, the two legs net into a single cash flow paid by whoever owes the larger amount. Understanding the math behind that net settlement—and which direction it flows—is the foundation of swap trading.*

<div class="wiki-hatnote">

This entry details the mechanics of calculating and settling each period's payment. For how the swap's value changes as rates move mid-life, see [How an interest rate swap is valued after inception](/swap-valuation-mid-life/). For the default risk created when swaps develop value, see [Counterparty credit risk in swaps](/swap-counterparty-credit-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fixed-for-Floating Swap Payment Mechanics — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Each party calculates what they owe, then one side pays the net difference.</div>

|   |   |
|---|---|
| **Two obligations** | Fixed payer owes: Notional × fixed rate × day count. Floating payer owes: Notional × floating rate × day count. |
| **Floating rate** | Usually set at the start of each period (e.g., LIBOR, SOFR); rarely reset mid-period. |
| **Net settlement** | Only one net payment is made per period, not two gross payments. |
| **Timing** | On settlement date (typically 2 business days after period end). |
| **Day count** | Actual/360, 30/360, or Actual/Actual depending on the market and currency. |
| **Notional amount** | Often never exchanged; it's only used to calculate interest. |

</aside>

## The Two Legs: Gross Payment Obligations

A **fixed-for-floating swap** has two legs:

1. **Fixed leg:** One party (the fixed-rate payer) owes a fixed coupon calculated as:  
   **Notional × Fixed Rate × Day Count Fraction**

2. **Floating leg:** The other party (the floating-rate payer) owes a floating coupon calculated as:  
   **Notional × Floating Rate × Day Count Fraction**

On each settlement date, both parties have a claim against the other. The party who owes the larger amount pays the difference—the **net settlement**—to the party owed the smaller amount.

## How the Floating Rate Is Set

The floating rate is almost always fixed in advance. In most interest rate swaps, the floating rate is observed at the **start** of each accrual period, not at the end.

**Example timeline:**
- June 15: The floating rate (say, 3-month LIBOR) is published at 4.85%.
- June 15 to September 14: The accrual period (exactly 91 days).
- September 15: Settlement date. The floating-rate payer owes 4.85% on the notional for the 91-day period.

This advance-set, in-arrears-settlement pattern means counterparties know their obligation early and can manage liquidity. It also creates predictability: a swap's floating payments are nearly as certain as its fixed payments once each rate fixes at the start of its period.

Some institutional swaps use a different convention: the floating rate is observed and paid in arrears (during the next period). The mechanics remain the same, just the timing of knowledge shifts.

## A Numerical Example

Assume:
- Notional: $10,000,000
- Fixed rate: 3.50% per annum
- Floating rate index: 3-month LIBOR, reset quarterly
- Settlement: Quarterly on March 15, June 15, September 15, December 15
- Day count convention: Actual/360 (most USD swaps use this)

**First settlement period: March 15 to June 14 (91 days)**

On March 15, the published 3-month LIBOR is 4.20%. This rate applies to the entire period.

Fixed-rate payer owes:
$$10,000,000 \times 0.0350 \times \frac{91}{360} = 10,000,000 \times 0.0350 \times 0.252778 = \$88,472$$

Floating-rate payer owes:
$$10,000,000 \times 0.0420 \times \frac{91}{360} = 10,000,000 \times 0.0420 \times 0.252778 = \$106,207$$

**Net settlement:** The floating-rate payer owes the fixed-rate payer:  
$106,207 − $88,472 = **$17,735**

The floating-rate payer sends $17,735 to the fixed-rate payer on June 15. (In this example, LIBOR is above the fixed rate, so the floating side pays.)

**Second settlement period: June 15 to September 14 (91 days)**

On June 15, the published 3-month LIBOR is 3.85% (rates have fallen).

Fixed-rate payer owes:
$$10,000,000 \times 0.0350 \times \frac{91}{360} = \$88,472$$ (unchanged)

Floating-rate payer owes:
$$10,000,000 \times 0.0385 \times \frac{91}{360} = \$97,294$$

**Net settlement:** The floating-rate payer owes the fixed-rate payer:  
$97,294 − $88,472 = **$8,822**

Payment flows to the fixed-rate payer again, but now the amount is smaller because LIBOR has fallen.

**Third settlement period: September 15 to December 14 (91 days)**

On September 15, LIBOR is 3.10%.

Fixed-rate payer owes:
$$10,000,000 \times 0.0350 \times \frac{91}{360} = \$88,472$$

Floating-rate payer owes:
$$10,000,000 \times 0.0310 \times \frac{91}{360} = \$78,431$$

**Net settlement:** The fixed-rate payer now owes the floating-rate payer:  
$88,472 − $78,431 = **$10,041**

The direction has reversed. The fixed-rate payer sends $10,041 to the floating-rate payer because LIBOR has fallen below the fixed rate.

## The Direction of Payment Reflects Rate Movement

In the example above, the net payment direction flips each quarter because LIBOR moves. The fixed-rate payer is "long" falling rates (benefits from lower LIBOR) and "short" rising rates (pays more when LIBOR rises). The floating-rate payer has the opposite exposure: they benefit from rising rates and lose when rates fall.

This is why companies and investors use swaps as [hedges](/derivatives-hedging/). A corporation with floating-rate debt (paying LIBOR + 2%) can enter a swap as the fixed-rate payer, effectively locking in a total cost of (Fixed Swap Rate + 2%), insulating themselves from rising rates.

## Day Count Conventions Matter

The fraction of the year (day count) varies by market convention:
- **Actual/360:** Count actual days, divide by 360. Used for most USD short-term rates (LIBOR, SOFR) and corporate swaps.
- **30/360:** Assume each month has 30 days, each year 360 days. Used for corporate bonds and some fixed-rate swaps.
- **Actual/Actual (ISDA):** Count actual days, divide by 365 (or 366 in leap years). Used for some government bond markets and [index](/sp-500-index/)-linked instruments.

In the example above, Actual/360 applied. If it had been 30/360 (assuming exactly 90 days per quarter), the day count fraction would be 90/360 = 0.25, and amounts would differ slightly.

## When the Notional Is and Isn't Exchanged

In most vanilla fixed-for-floating swaps, the notional principal is **never exchanged**. It's used only to calculate interest. At maturity, each party's obligation ends; there's no principal repayment (unless the swap is explicitly structured with principal exchanges).

However, in some derivatives and swaps linked to asset prices or currencies, the notional itself might be exchanged or might vary over time (amortizing swaps, accreting swaps). The mechanics still apply: interest is calculated on whatever the outstanding notional is for each period.

## Timing and Settlement Details

Settlement happens on a **settlement date**, typically 2 business days after the end of each accrual period (the [standard accrued period](/accrual-accounting/)-to-settlement lag, or "T+2"). The paying party must deliver funds to the receiving party's account. 

In modern markets, this is often handled via automated clearing systems (e.g., Fedwire for USD settlements). Large institutional swaps may be handled via a central counterparty clearinghouse, which guarantees settlement and manages collateral.

## Early Termination and Mid-Period Valuation

If a swap is terminated before maturity, the [valuation](/swap-valuation-mid-life/) determines how much cash one party owes the other. The next period's floating payment, if not yet set, is valued using the prevailing forward [LIBOR](/libor/) or [SOFR](/sofr/) rates. The remaining fixed payments are discounted at current market swap rates. The party in the money receives the present value of all remaining net cash flows.

## See also

<div class="wiki-seealso">

### Closely related

- [How an interest rate swap is valued after inception](/swap-valuation-mid-life/) — How to calculate what a swap is worth mid-life
- [Counterparty credit risk in swaps](/swap-counterparty-credit-risk/) — Why swaps create default exposure
- [Swap vs forward rate agreement](/swap-vs-forward-rate-agreement/) — How single-period FRAs differ from multi-period swaps
- [Derivatives hedging](/derivatives-hedging/) — Why companies use swaps to manage exposure

### Wider context

- [Interest rate swap](/interest-rate-swap/) — Overview of swap markets and uses
- [LIBOR](/libor/) — The floating rate most commonly swapped
- [SOFR](/sofr/) — The replacement floating rate post-LIBOR
- [Forward rate](/forward-guidance/) — How forward rates are derived for valuation
- [Accrual accounting](/accrual-accounting/) — How interest is accrued and recognized

</div>

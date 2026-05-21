---
title: "Interest Rate Swap"
description: "An interest rate swap is an agreement to exchange fixed interest payments for floating interest payments on a notional principal, enabling borrowers to change interest-rate exposure."
keywords:
  - interest rate swap
  - fixed floating
  - swap
  - rate hedge
  - derivative
image: "/svg/derivatives.svg"
---

*An **interest-rate swap** (IRS) is a [swap](/swap/) contract where one party pays a fixed interest rate and receives a floating rate (typically [SOFR](/sofr-swap/) or another index), while the counterparty does the opposite. No principal is exchanged; only interest rate differences are settled periodically. Interest-rate swaps are the most-traded derivatives globally, used by banks, corporations, and investors to manage [interest-rate](/interest-rate/) risk and match assets to liabilities.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="Fixed vs. floating rate exchange diagram" />

<div class="wiki-infobox-caption">IRS swaps fixed payments for floating.</div>

|   |   |
|---|---|
| **Notional principal** | Amount on which interest is calculated |
| **Fixed payer** | Receives floating; commits to fixed rate |
| **Floating receiver** | Pays fixed; receives rate index + spread |
| **Duration** | 1–30 years typically |
| **Payment frequency** | Quarterly, semi-annual, or annual |
| **Floating rate index** | SOFR (US), EURIBOR (EU), etc. |
| **Spread** | Fixed rate relative to curve |
| **Par value** | Swap's value = 0 at initiation |
| **Mark-to-market** | Value changes as rates move |
| **Clearing** | Increasingly moved to central counterparties |

</aside>

## How interest-rate swaps work

A corporation borrows $50M at floating [SOFR](/sofr-swap/) + 1% for 5 years. It wants to lock in a fixed cost. It enters a 5-year IRS with a bank:

**On each quarter:**
- Corporation pays bank: Fixed 4% on $50M = $500K
- Bank pays corporation: SOFR + 1% on $50M = (SOFR + 1%) × $50M

**Net result:** Corporation pays fixed 4%; any change in SOFR doesn't affect the corporation's total payment.

If SOFR is at 5%, the corporation's floating cost is 6%, but it pays 4% fixed via the swap, netting 4% total.

## Why corporations use IRS

**Floating to fixed:** A floating-rate borrower locks in costs, avoiding rate-rise risk.

**Fixed to floating:** A fixed-rate borrower—if it believes rates will fall—swaps to floating to benefit from the decline.

**Liability-asset matching:** An investor with fixed-rate [bond](/bond/)s but floating-rate liabilities swaps to align maturities and durations.

## Swap pricing

The fair fixed rate is determined by the [yield curve](/yield-curve/). For a 5-year swap, the fixed rate is approximately the 5-year par swap rate—the rate at which the present value of fixed payments equals the present value of expected floating payments.

As the [yield curve](/yield-curve/) shifts, swap rates shift. A flattening curve typically lowers longer-dated swap rates.

## Marked-to-market values

When you enter a swap at par (fixed rate set to be fair), its value is zero. As rates move, the value changes.

Example:
- You pay fixed 4% (locked in). Rates rise to 5%.
- Your fixed 4% is now cheap (market wants 5%).
- Your swap has positive value; you could sell it for a gain.

The fixed-rate payer gains when rates rise; the floating-rate payer gains when rates fall.

## Counterparty risk and clearing

Swaps are bilateral contracts with counterparty risk. If the bank defaults after rates have moved significantly, you lose the present value of the remaining cash flows.

Post-2008, standardized IRS are increasingly cleared through central counterparties (LCH Swapclear, CME, etc.), reducing bilateral risk and requiring [margin](/initial-margin/).

## SOFR transition from LIBOR

The global derivatives market transitioned from [LIBOR](/interest-rate/) to SOFR (Secured Overnight Financing Rate) in 2021–2023. Existing [LIBOR](/interest-rate/)-based swaps were converted or allowed to mature. New IRS are SOFR-based, reflecting lower counterparty risk (SOFR is repo-based, more transparent).

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — general contract structure
- [SOFR swap](/sofr-swap/) — USD IRS reference rate
- [Swaption](/swaption/) — option to enter IRS
- [Bond](/bond/) — often matched via IRS
- [Yield curve](/yield-curve/) — determines swap rates

### Rates and indices

- [Interest rate](/interest-rate/) — IRS manages this risk
- [SOFR](/interest-rate/) — replacement for LIBOR
- [Forward rates](/forward-contract/) — used in swap pricing
- [Spread](/bond/) — above curve in IRS pricing

### Risk management

- [Hedging](/hedge-fund/) — primary IRS use
- [Duration](/bond/) — matched via IRS
- [Counterparty risk](/bond/) — central concern
- [Interest-rate risk](/interest-rate/) — IRS reduces this

### Deeper context

- [Derivative](/option/) — the family of instruments
- [OTC market](/stock-market/) — IRS trade here
- [Central clearing](/stock-exchange/) — post-reform requirement
- [Fixed income](/bond/) — IRS essential market

</div>

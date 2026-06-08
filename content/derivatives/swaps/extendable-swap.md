---
title: "Extendable Swap"
description: "A swap contract where one party holds the right to extend the maturity beyond the original termination date, embedding a payer swaption."
keywords:
  - extendable swap
  - swap maturity extension
  - payer swaption embedded
  - interest rate derivative
  - duration extension
  - long-dated hedging
image: "/svg/derivatives.svg"
---

*An **extendable swap** is an [interest rate swap](/interest-rate/) in which one party holds an embedded [option](/option/) to extend the contract's maturity beyond the originally scheduled [termination date](/expiration-date/). The party holding the extension right—typically the fixed-rate receiver—can commit the swap to run longer if rates move favourably, securing an extended hedge at the original fixed rate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Extendable Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for financial derivatives." />

<div class="wiki-infobox-caption">A hybrid embedding a payer [swaption](/option/) into a base-case [swap](/interest-rate/).</div>

|   |   |
|---|---|
| **What it is** | An [interest rate swap](/interest-rate/) with a right to extend maturity beyond the original final date |
| **Also called** | Swap with extension option; extendable interest-rate swap |
| **Embedded option** | [Swaption](/option/) allowing the extension-holding party to lengthen the swap term |
| **Typical holder** | Fixed-rate receiver (lender seeking extended income protection) |
| **Value** | Base swap value plus the extension [option premium](/option-premium/) |
| **Key risk** | Fixed-rate payer faces [extension risk](/expiration-date/) in falling-rate scenarios |

</aside>

## How an extendable swap works

In a plain [interest rate swap](/interest-rate/), both parties commit to a fixed [maturity date](/expiration-date/). An extendable swap introduces a unilateral right: one party may elect to extend the swap's life beyond its originally scheduled termination date, typically by 1, 3, or 5 years.

When the extension-holding party exercises this right, the swap continues under the original fixed [rate](/interest-rate/) and the same terms, but for a longer period. Both parties remain locked in, now with a new final maturity date (e.g., a 5-year swap becomes 8 years). Neither party can unwind the swap earlier than the newly extended termination date without penalties or negotiation.

The extension right is economically equivalent to a [payer swaption](/option/): the right to enter a swap in which the holder pays floating and receives fixed, starting at the original swap's final date. By embedding this right into the live swap, the extension-holder locks in the ability to extend protection at the already-negotiated fixed rate, protecting themselves against rising [interest rates](/interest-rate/).

## Motivation: who uses extendable swaps and why

A fixed-rate receiver (e.g., a pension fund, long-term investor, or lender) often buys an extendable swap to ensure they can continue receiving a fixed [coupon](/coupon-payment/) if rates fall. If rates decline, the receiver benefits from extending the swap—they continue earning the original (now relatively high) fixed rate rather than rolling into a new, lower-rate swap.

Conversely, a fixed-rate payer (often a borrower or dealer) is reluctant to grant this extension right. If rates fall sharply, the payer's cost of the swap—the fixed rate they must pay—becomes expensive relative to new market rates. The extension forces them to continue paying the original rate for longer, locking in losses. They demand compensation via a lower fixed rate (i.e., the extension premium is baked into the rate) or an upfront fee.

In a rising-rate scenario, the extension right is out-of-the-money: the fixed receiver has no incentive to extend because new market rates would be higher, making the original fixed rate valuable anyway. The payer has still borne extension risk but rarely sees it realized.

## Valuation and pricing

An extendable swap is valued as:

**Extendable Swap Value = Base Swap Value + Extension Option Value**

The extension [option premium](/option-premium/) is added to the value of the base swap (from inception to the original final date). The [fixed rate](/interest-rate/) offered on an extendable swap is typically 10–40 basis points lower than a comparable vanilla swap with the same maturity (because the payer is selling the extension option).

The exact discount depends on:

- Moneyness: how likely the extension is to be in-the-money at the original maturity date
- [Volatility](/historical-volatility/) of [interest rates](/interest-rate/): higher volatility increases the option's value
- Time horizon: the longer the extension period and the further away the exercise date, the higher the option value
- [Credit spread](/credit-spread/): the [credit risk](/credit-risk/) of the extension-holding party

Dealers use binomial trees, Black-Scholes approximations, or interest-rate Monte Carlo models to decompose and value the option component.

## Comparison with related structures

An extendable swap differs from a [callable swap](/callable-swap/) in that it extends maturity rather than allowing early termination. It differs from a [puttable swap](/puttable-swap/)—which grants the floating-rate payer an early exit—in that it grants the fixed-rate receiver a continuation right, not an exit right.

An extendable swap can also be viewed as a package: a vanilla swap from now to the original maturity date, plus an embedded [payer swaption](/option/) exercisable at the original maturity. Separating these components helps traders understand the option value and hedge ratio.

## Risks and considerations

**[Extension risk](/expiration-date/)**: The fixed-rate payer faces forced continuation of a swap that may have become uneconomic. In a falling-rate scenario, they are locked into paying the original fixed rate for a longer period, crystallizing losses on a mark-to-market basis.

**Duration mismatch**: A fixed-rate receiver intending a 5-year hedge may find it extended to 8 years, creating duration overrun if their underlying [liability](/accounts-payable/) or [asset](/balance-sheet/) exposure is only 5 years.

**Model risk**: Accurate pricing requires forecasts of [volatility](/historical-volatility/) and [correlation](/concentration-risk/) over a longer horizon. Volatility estimates made at inception may be materially wrong, causing the option to be mispriced.

**[Counterparty risk](/counterparty-risk/)**: The fixed-rate payer's [credit exposure](/credit-risk/) grows if the swap goes in-the-money (rates fall) and is then extended. The extension locks in this exposure for longer, increasing [counterparty risk](/counterparty-risk/).

**Optionality incentives**: The fixed-rate receiver may exercise the extension for reasons unrelated to overall economic value—e.g., accounting convenience, risk reporting thresholds, or organizational inertia—leaving the payer with no control over the continuation decision.

## See also

<div class="wiki-seealso">

### Closely related

- [Callable Swap](/callable-swap/) — grants the fixed-rate payer the right to terminate early
- [Puttable Swap](/puttable-swap/) — grants the floating-rate payer the right to terminate early
- [Interest Rate Swap](/interest-rate/) — the underlying vanilla structure
- [Swaption](/option/) — standalone option to enter or receive a swap on a future date
- [Option](/option/) — foundational right-but-not-obligation derivative
- [Payer Swaption](/option/) — option to initiate a swap paying fixed and receiving floating

### Wider context

- [Swap](/interest-rate/) — exchange of cash flows between parties over time
- [Derivatives](/option/) — instruments whose value derives from underlyings
- [Interest Rate Risk](/interest-rate-risk/) — exposure to [interest rate](/interest-rate/) movements
- [Duration](/duration/) — measure of a bond or swap's sensitivity to rate changes
- [Counterparty Risk](/counterparty-risk/) — risk that the other party defaults or fails to perform

</div>

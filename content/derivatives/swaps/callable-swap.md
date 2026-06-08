---
title: "Callable Swap"
description: "A swap contract where one party has the right to terminate the agreement early on specified dates, shifting exercise risk to the counterparty."
keywords:
  - callable swap
  - swap termination right
  - swaption embedded
  - interest rate derivatives
  - early exercise
  - counterparty risk
image: "/svg/derivatives.svg"
---

*A **callable swap** is an [interest rate swap](/interest-rate/) in which one party holds an embedded [option](/option/) to terminate the contract early on one or more pre-agreed dates. The party holding the call—typically the fixed-rate payer—can force termination if market conditions move in their favour, transferring exercise risk and [basis risk](/bid-ask-spread/) to the other side.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Callable Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for financial derivatives." />

<div class="wiki-infobox-caption">A hybrid between a plain-vanilla swap and an embedded [swaption](/option/).</div>

|   |   |
|---|---|
| **What it is** | A [swap](/interest-rate/) with an early termination right held by one party |
| **Also called** | Callable interest-rate swap; swap with embedded call option |
| **Embedded option** | [Swaption](/option/) allowing termination on scheduled exercise dates |
| **Typical holder** | Fixed-rate payer (hedger seeking rate cap-like behaviour) |
| **Value** | Swap value less the call [option premium](/option-premium/) |
| **Key risk** | [Reinvestment risk](/reinvestment-risk/); unfavourable early termination by counterparty |

</aside>

## How a callable swap works

In a plain [interest rate swap](/interest-rate/), both parties are locked in until [maturity](/expiration-date/). A callable swap introduces asymmetry: the call-holding party may unwind the trade on one or more predefined dates (exercise dates), typically 1, 3, 5, or 7 years into a longer-dated swap.

The party exercising the call terminates the swap and both [principal](/bond/) streams stop. The exercising party is then free to enter a new swap at market rates—or exit the [interest rate](/interest-rate/) market entirely. The non-calling party loses the economics of the original trade and must replace it, often at worse rates if markets have moved against them.

The embedded call is economically equivalent to a [swaption](/option/) bundled into the swap. The call-holding party pays for this right through a lower fixed rate on the swap leg (relative to a plain-vanilla comparable), or it is built into pricing upfront.

## Motivation: when and why

Fixed-rate payers often buy callable swaps to hedge [interest rate](/interest-rate/) exposure in a declining-rate environment. If rates fall sharply, the fixed payer's underlying borrowing or [liability](/accounts-payable/) becomes cheaper; the callable feature lets them unwind the swap and avoid overpaying on the [interest](/interest-rate/) hedge.

Conversely, a callable swap is unfavourable to the fixed-rate receiver (often a bank or dealer). Receivers face [call risk](/call-risk/): when rates fall, the counterparty exercises and leaves the receiver refinancing at lower (less profitable) rates. This embedded option risk is compensated through wider [spreads](/bid-ask-spread/) or a lower upfront payment to the receiver.

In a rising-rate scenario, the call is out-of-the-money and likely unexercised. The swap then behaves like a standard trade, but the receiver has still taken on the risk of adverse early termination, for which they demand compensation.

## Valuation and pricing

A callable swap is priced as:

**Callable Swap Value = Plain Vanilla Swap Value − Call Option Value**

The call option [premium](/option-premium/) is deducted from the value of an equivalent non-callable swap. A dealer pricing a callable swap to a client must model the probability and timing of exercise, the [volatility](/historical-volatility/) of the underlying rates, and the [time decay](/time-decay-theta/) of the option leg.

The [fixed rate](/interest-rate/) offered on a callable swap is typically 10–50 basis points lower than a comparable vanilla swap, depending on:

- Moneyness: how in-the-money or out-of-the-money the call sits at pricing
- [Volatility](/historical-volatility/): higher volatility increases the option value
- [Spread](/credit-spread/): the [credit spread](/credit-risk/) between the swap parties
- Remaining time to exercise dates

Dealers use [Black-Scholes](/black-scholes-model/) or binomial tree models to value the embedded swaption component.

## Comparison with related structures

A callable swap differs from a [puttable swap](/puttable-swap/) in that the fixed-rate payer holds the call, while the floating-rate payer holds a put on the puttable. It differs from an [extendable swap](/extendable-swap/) in that a callable extends the right to exit early, whereas an extendable extends the right to lengthen maturity.

A callable swap also closely resembles a direct purchase of a [swaption](/option/), but bundles the option economics into a single swap rate rather than charging separate [option premium](/option-premium/), making the structure cleaner for some corporate hedgers.

## Risks and considerations

**Exercise risk**: The non-calling party faces forced early termination when it is least convenient—typically when rates have fallen sharply and the swap has become valuable to the calling party. The counterparty must then [reinvest](/reinvestment-risk/) at lower rates or unwind other positions.

**Hedging incompleteness**: A fixed-rate borrower expecting a callable swap to fully hedge [interest rate](/interest-rate/) risk may find their hedge unravels early, leaving them unhedged in a low-rate environment precisely when they most wanted protection.

**Model risk**: Accurate valuation hinges on correct forecasting of [volatility](/historical-volatility/) and [correlation](/concentration-risk/) between rates and the embedded option's value. If [volatility](/historical-volatility/) estimates are wrong at execution, the pricing is mispriced.

**[Counterparty risk](/counterparty-risk/)**: As with all [swaps](/interest-rate/), exposure depends on in-the-money value and [duration](/duration/) remaining. Early termination by one party removes this [counterparty risk](/counterparty-risk/) but does so unilaterally.

## See also

<div class="wiki-seealso">

### Closely related

- [Puttable Swap](/puttable-swap/) — the receiver's counterpart, with a put option embedded
- [Extendable Swap](/extendable-swap/) — grants the right to extend maturity rather than exit early
- [Interest Rate Swap](/interest-rate/) — the vanilla underlying contract
- [Swaption](/option/) — explicit option to enter or receive a swap, separate instrument
- [Option](/option/) — foundational derivative giving the right but not obligation to transact
- [Call Option](/call-option/) — generic right to buy or terminate, priced separately

### Wider context

- [Swap](/interest-rate/) — broad class of exchanged cash flows between parties
- [Derivatives](/option/) — family of contracts deriving value from underlyings
- [Interest Rate Risk](/interest-rate-risk/) — exposure to changes in [interest rates](/interest-rate/)
- [Counterparty Risk](/counterparty-risk/) — risk that the other party defaults or fails to perform
- [Volatility](/historical-volatility/) — measure of rate movement uncertainty, inputs to option pricing

</div>

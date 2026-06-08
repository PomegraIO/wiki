---
title: "Puttable Swap"
description: "A swap contract where the floating-rate payer holds the right to terminate the agreement on specified dates, embedding a receiver swaption."
keywords:
  - puttable swap
  - receiver swaption
  - swap termination
  - floating rate payer
  - interest rate derivatives
  - early exit right
image: "/svg/derivatives.svg"
---

*A **puttable swap** is an [interest rate swap](/interest-rate/) in which the floating-rate payer holds an embedded [option](/option/) to terminate the contract early on pre-agreed exercise dates. The put-holder can force early exit if [interest rates](/interest-rate/) rise unfavourably, protecting them against [reinvestment risk](/reinvestment-risk/) while shifting exercise risk to the fixed-rate payer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Puttable Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for financial derivatives." />

<div class="wiki-infobox-caption">A hybrid embedding a receiver [swaption](/option/) into a standard [swap](/interest-rate/).</div>

|   |   |
|---|---|
| **What it is** | An [interest rate swap](/interest-rate/) with an early exit right held by the floating-rate payer |
| **Also called** | Puttable interest-rate swap; swap with embedded put |
| **Embedded option** | [Swaption](/option/) allowing the floating-rate payer to terminate on scheduled dates |
| **Typical holder** | Floating-rate payer (borrower seeking downside protection) |
| **Value** | Swap value plus the put [option premium](/option-premium/) received |
| **Key risk** | Fixed-rate payer faces [call risk](/call-risk/) in falling-rate scenarios |

</aside>

## How a puttable swap works

In a plain [interest rate swap](/interest-rate/), the floating-rate payer exchanges a [variable rate](/interest-rate/) (usually indexed to [LIBOR](/libor/) or [SOFR](/sofr/)) for a fixed rate. A puttable swap grants this floating payer the right—but not the obligation—to terminate the swap on one or more predefined exercise dates.

When the floating payer exercises the put, the swap unwinds immediately. Both parties' cash flows stop, and the floating payer is released from the [swap obligation](/bond/). They can then choose to refinance, enter a new swap, or exit [interest rate](/interest-rate/) markets entirely.

The put is economically equivalent to a [receiver swaption](/option/): the right to enter a swap in which the holder receives fixed and pays floating. By embedding this right into a live swap, the put-holder effectively buys downside protection against rising [interest rates](/interest-rate/).

## When and why puttable swaps are used

A floating-rate borrower (e.g., a company with a [variable-rate loan](/interest-rate/)) often buys a puttable swap to hedge [interest rate](/interest-rate/) risk with an escape clause. If rates rise sharply, their floating-rate debt becomes expensive. The puttable swap lets them exit the [interest rate](/interest-rate/) risk cheaply by exercising the put.

In contrast, a fixed-rate payer—usually a dealer, bank, or investor receiving fixed—enters a puttable swap reluctantly, accepting a put option they do not want. They are compensated by receiving a higher [fixed rate](/interest-rate/) than on a vanilla swap (the put premium is baked into the rate, or they collect it upfront).

A puttable swap is particularly valuable in rising-rate environments. If rates spike, the floating payer's exposure (the extra interest they must pay) is offset by the optionality value of the put. In a stable or falling-rate scenario, the put is out-of-the-money and rarely exercised, but the fixed-rate payer has nonetheless borne the risk of early termination.

## Valuation and pricing

A puttable swap is valued as:

**Puttable Swap Value = Plain Vanilla Swap Value + Put Option Value**

The embedded put [option premium](/option-premium/) is added to the value of an equivalent vanilla swap. The [fixed rate](/interest-rate/) offered on a puttable swap is typically 10–50 basis points higher than a comparable vanilla swap, reflecting the cost of the embedded put to the fixed-rate payer.

The exact spread depends on:

- Moneyness: how far in-the-money or out-of-the-money the put sits at pricing
- [Volatility](/historical-volatility/): higher [volatility](/historical-volatility/) increases option value
- [Credit spread](/credit-spread/): the credit quality spread between counterparties
- Distance to exercise dates and [time decay](/time-decay-theta/)

Dealers use [Black-Scholes](/black-scholes-model/), binomial models, or Monte Carlo simulation to isolate and price the embedded swaption component.

## Comparison with related structures

A puttable swap is the counterpart to a [callable swap](/callable-swap/): the floating-rate payer holds the put (early exit right), whereas in a callable swap, the fixed-rate payer holds the call. An [extendable swap](/extendable-swap/) grants the right to extend maturity rather than terminate, creating a different risk profile.

A puttable swap also resembles a direct purchase of a [receiver swaption](/option/), but bundles the option economics into a single rate, simplifying execution and accounting for end-users.

## Risks and considerations

**[Reinvestment risk](/reinvestment-risk/)**: Although the puttable swap lets the floating payer exit early, they face [reinvestment risk](/reinvestment-risk/) if they put the swap and rates have already fallen. They must reinvest at lower yields or accept being unhedged.

**Optionality imbalance**: The fixed-rate payer is systematically disadvantaged. They receive a higher fixed rate, but still face forced early termination when rates fall and the floating payer's economics improve. This is essentially a one-way bet against them.

**Model risk**: Valuation depends on accurate forecasts of rate [volatility](/historical-volatility/) and the [correlation](/concentration-risk/) between rates and swap value. Mispricings in the option component create mark-to-market losses for the wrong-way bettor.

**[Counterparty risk](/counterparty-risk/)**: The fixed-rate payer's [credit exposure](/credit-risk/) is highest when rates are falling and the swap is most valuable to the put-holder. Early exercise eliminates this exposure but unilaterally and at the worst time for the receiver.

**Exercise timing**: The floating payer may exercise opportunistically or strategically, not necessarily when it economically makes sense for overall portfolio management. The fixed-rate payer cannot control when the termination occurs.

## See also

<div class="wiki-seealso">

### Closely related

- [Callable Swap](/callable-swap/) — the fixed-rate payer's counterpart, with a call option embedded
- [Extendable Swap](/extendable-swap/) — grants the right to extend maturity, not terminate early
- [Interest Rate Swap](/interest-rate/) — the underlying vanilla structure
- [Option](/option/) — general right to buy, sell, or terminate
- [Swaption](/option/) — standalone option to enter or receive a swap contract
- [Put Option](/put-option/) — right to sell or exit, the economic analogue

### Wider context

- [Swap](/interest-rate/) — exchange of cash flows between counterparties
- [Derivatives](/option/) — instruments deriving value from underlyings
- [Interest Rate Risk](/interest-rate-risk/) — exposure to movements in [interest rates](/interest-rate/)
- [Counterparty Risk](/counterparty-risk/) — risk that the other party defaults or fails to honour terms
- [Volatility](/historical-volatility/) — measure of rate uncertainty, a key input to option pricing models

</div>

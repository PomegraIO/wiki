---
title: "Knock-In Option"
description: "A knock-in option is activated only when the underlying asset's price crosses a barrier level, making it cheaper than vanilla options due to lower exercise probability."
keywords:
  - knock-in option
  - barrier option
  - conditional option
  - activation
  - exotic option
image: "https://picsum.photos/seed/knock-in-option/900/600"
---

*A **knock-in option** is a [barrier option](/barrier-option) that does not exist (has zero value) until the underlying asset's price crosses a predetermined barrier level. Once the barrier is breached, the option is "activated" and behaves like a vanilla [call](/call-option) or [put](/put-option) for the remainder of its life. There are two types: **down-and-in** (activated when price falls below the barrier) and **up-and-in** (activated when price rises above the barrier). Knock-in options are cheaper than vanilla options because activation is uncertain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Knock-In Option — key facts</div>

<img src="https://picsum.photos/seed/knock-in-option/900/600" alt="Price path crossing barrier to activate option" />

<div class="wiki-infobox-caption">Option activates when barrier is crossed.</div>

|   |   |
|---|---|
| **Types** | Down-and-in (DIC/DIP), up-and-in (UIC/UIP) |
| **Activation** | When spot price crosses barrier |
| **Pre-activation** | Option is worthless |
| **Post-activation** | Behaves as vanilla option |
| **Barrier monitoring** | Continuous throughout option life |
| **Price vs. vanilla** | Cheaper (lower probability of activation) |
| **Moneyness** | Barrier in-the-money or out-of-the-money |
| **Strike** | Independent of barrier level |
| **Primary use** | Cost reduction for conditional hedges |
| **Settlement** | Cash or physical |

</aside>

## How knock-in options work

A stock trader is moderately bullish but only wants upside protection if the stock breaks through resistance at $120. The stock is currently $100 and the strike is $110.

The trader buys an **up-and-in call**:
- Strike: $110
- Barrier: $120
- Premium: $0.50 (very cheap)

**Scenario 1:** Stock rises to $125 then above the barrier to $120 (activation occurs). The up-and-in call springs to life, behaving like a normal $110 call. The trader profits from the move.

**Scenario 2:** Stock rises to $118 (barrier not crossed). The up-and-in option remains worthless. The trader loses the $0.50 premium.

The cheap premium is the trade-off for the activation requirement.

## Down-and-in options

A **down-and-in put** is activated only if the stock price falls below the barrier. Useful for tail hedging: a shareholder wants downside protection (via a put) only if the stock crashes sharply (below the barrier).

Example:
- Stock at $100; strike $90; barrier $70
- Premium: $0.30 (cheap)

If stock falls to $60 (below $70 barrier), the put activates and protects the shareholder. If the stock stays above $70, the put never activates and the $0.30 is lost.

## Activation and path-dependence

Once the barrier is crossed at any point during the option's life, the option is **permanently activated**. Even if the price rebounds and moves away from the barrier, the option remains active.

This path-dependent nature makes knock-in options cheaper than vanilla options: you are paying for the *chance* the barrier will be crossed, not for a guaranteed right.

## Pricing knock-in options

Pricing requires calculating the probability of barrier crossing before expiration and the option's value upon activation.

The probability depends on:
- Current stock price vs. barrier distance
- Time to expiration
- Volatility
- Interest rates

Higher [volatility](/historical-volatility) increases crossing probability, raising knock-in value. Lower [volatility](/historical-volatility) decreases it.

[Monte-carlo-options-pricing](/monte-carlo-options-pricing) or [binomial-option-pricing](/binomial-option-pricing) models handle knock-in valuation by simulating paths and checking if the barrier is touched.

## Cost reduction use case

An exporter earning revenue in 6 months wants downside protection but finds a vanilla put expensive at $2 per contract.

A down-and-in put with a low barrier (far out-of-the-money) might cost $0.30. The exporter gets protection if the currency crashes hard (below the barrier); if it doesn't, the exporter saves $1.70 per contract.

This is ideal for unlikely but catastrophic scenarios.

## Barrier rebate

Some knock-in contracts include a **rebate**: if the barrier is never touched, the buyer receives a small refund (e.g., 5% of premium). This makes them slightly more attractive to buyers.

## See also

<div class="wiki-seealso">

### Closely related

- [Barrier option](/barrier-option/) — parent category
- [Knock-out option](/knock-out-option/) — opposite mechanism
- [Call option](/call-option/) — vanilla right to buy
- [Put option](/put-option/) — vanilla right to sell
- [Exotic option](/binary-option/) — non-standard structure

### Pricing and valuation

- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — simulation method
- [Binomial option pricing](/binomial-option-pricing/) — tree method
- [Black-Scholes model](/black-scholes-model/) — extended for barriers
- [Implied volatility](/implied-volatility/) — affects barrier crossing probability

### Related concepts

- [Barrier](/barrier-option) — activation level
- [Path-dependent option](/asian-option/) — full history matters
- [Option premium](/option-premium/) — lower for knock-ins
- [Strike price](/strike-price/) — independent of barrier

### Deeper context

- [Option](/option/) — the family of derivatives
- [Hedging](/hedge-fund/) — cost reduction for protection
- [Risk management](/hedge-fund/) — tail hedging with knock-ins

</div>

---
title: "Compound Option"
description: "A compound option is an option on an option—the underlying is another derivative contract, not a stock, creating nested optionality and lower cost."
keywords:
  - compound option
  - option on option
  - exotic option
  - nested optionality
  - derivative
image: "/svg/derivatives.svg"
---

*A **compound option** is an exotic derivative where the underlying asset is another [option](/option) rather than a [stock](/stock), commodity, or currency. The holder of a compound option receives the right to buy (call-on-call), sell (put-on-call), buy (call-on-put), or sell (put-on-put) another option at a predetermined [strike price](/strike-price). Compound options are used when future hedging demand is uncertain or to reduce premium cost for contingent positions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Compound Option — key facts</div>

<img src="/svg/derivatives.svg" alt="Nested layers representing option on option structure" />

<div class="wiki-infobox-caption">A compound option nests one option inside another.</div>

|   |   |
|---|---|
| **Structure** | Option on an option |
| **Types** | Call-on-call, call-on-put, put-on-call, put-on-put |
| **Two strike prices** | Inner strike and outer strike |
| **Two expiration dates** | First option expires, then inner option if exercised |
| **Cost** | Lower than owning both options outright |
| **Use case** | Contingent hedging, uncertain future needs |
| **Valuation** | Requires nested Black-Scholes calculations |
| **Settlement** | Physical delivery of the inner option |
| **Liquidity** | Very low; mostly bespoke OTC |

</aside>

## The nested structure

A compound option involves two layers of optionality. Suppose you buy a call-on-call at strike price $10, expiring in 3 months. The underlying is a standard [call option](/call-option) on Apple [stock](/stock) struck at $150, expiring in 6 months.

At the 3-month mark (first [expiration date](/expiration-date)), you have the right to buy the Apple call for $10. If Apple is trading at $160 and the Apple call is worth $15, you exercise: you pay $10, receive the Apple call (now worth $15), and profit $5. You then own an Apple call for the next 3 months.

If Apple is trading at $140 and the Apple call is worth only $3, you do not exercise: you let the compound option expire worthless, losing the compound option premium you paid. You never take ownership of the Apple call.

This two-step structure is why compound options are called "options on options."

## The four types

1. **Call-on-call:** Right to buy a [call option](/call-option). You exercise if the underlying call rises in value, then you own the call and can profit from further stock moves.

2. **Put-on-call:** Right to sell a [call option](/call-option). Less common; used if you expect the underlying call to decline in value (e.g., due to falling [volatility](/historical-volatility)) and want to profit from that decline without short-selling.

3. **Call-on-put:** Right to buy a [put option](/put-option). You exercise if the put rises in value, then you own the put and profit from further downside in the stock.

4. **Put-on-put:** Right to sell a [put option](/put-option). Used if you expect puts to decline in value and want to capture that decay.

## Why compound options exist

Compound options are useful for hedging contingent future needs. Suppose you are bidding on a contract that, if you win, will expose you to currency risk. You do not know yet if you will win. Buying a currency [put option](/put-option) right now is expensive and you may not need it.

Instead, you buy a call-on-put at a low premium. If you win the bid, you exercise the call and acquire the put, protecting yourself. If you lose the bid, you let the call-on-put expire worthless and save the premium you would have paid for an unnecessary put. The compound option saves cost on contingent risk.

Similarly, a company with uncertain future financing needs might buy a call-on-swaption (option to acquire the right to enter an interest-rate [swap](/swap)). If the financing deal closes, they exercise and obtain the swaption, locking in hedge costs. If the deal falls through, they lose only the call premium, not the full swaption cost.

## Pricing compound options

Valuing a compound option requires working backward from the inner option's expiration. At the first [expiration date](/expiration-date), the inner option has a known value (or range of values depending on the stock price scenario). You then apply [Black-Scholes model](/black-scholes-model) or another pricing method to the compound option itself, using the distribution of inner-option values as the payoff distribution.

In essence: apply Black-Scholes to get the inner option's value, then apply Black-Scholes again (treating that value as the payoff) to get the compound option's value. This double calculation is why compound options are more complex to price and typically require numerical methods or approximations.

The inputs are the inner [strike price](/strike-price), outer [strike price](/strike-price), two [expiration date](/expiration-date)s, [volatility](/historical-volatility), and interest rates. Higher [volatility](/historical-volatility) raises the value of both layers.

## Risks and Greeks

[Delta](/delta) for a compound option is the product of two deltas: how much the inner option's value changes with the stock, times how much the compound option's value changes with the inner option's value. This nested [delta](/delta) makes the compound option less sensitive to stock moves than owning both options separately would be.

[Gamma](/gamma) (convexity) is compressed compared to owning two separate options, because the nesting reduces sensitivity to small stock moves. [Vega](/vega) (sensitivity to [volatility](/historical-volatility)) is also compressed for the same reason.

[Theta](/theta) (time decay) works against both the outer and inner option, creating a complex decay pattern as two [expiration date](/expiration-date)s approach.

## Practical examples

A bank lending to emerging markets might buy a call-on-put struck on an exchange rate. If political risk spikes and the currency crashes, the bank exercises the call, acquires the put, and hedges further downside. If stability prevails, the bank lets the call expire.

An oil producer uncertain about future drilling might buy a call-on-call on crude oil. If prices rise and drilling becomes attractive, they exercise and own an oil call, locking in upside. If prices fall and drilling is abandoned, they let the compound option expire.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the inner/outer option right to buy
- [Put option](/put-option/) — the inner/outer option right to sell
- [Swaption](/swaption/) — option to enter a swap; used as underlying in compound structures
- [Exotic option](/binary-option/) — non-standard payoff structure

### Pricing & Greeks

- [Black-Scholes model](/black-scholes-model/) — applied twice (nested)
- [Implied volatility](/implied-volatility/) — drives both layers of pricing
- [Delta](/delta/) — product of two deltas
- [Vega](/vega/) — compressed relative to two separate options

### Deeper context

- [Option](/option/) — the family of derivatives
- [Time value](/time-value/) — both layers contribute
- [Strike price](/strike-price/) — two prices in compound options

</div>

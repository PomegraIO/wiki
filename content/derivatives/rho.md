---
title: "Rho"
description: "Rho measures how much an option's price changes for each 1% change in interest rates, with smaller effects than other Greeks for most options."
keywords:
  - rho
  - option greeks
  - interest rate sensitivity
  - option pricing
  - derivative risk
image: "/svg/derivatives.svg"
---

*The **rho** of an option is the amount by which its price changes for each 1% change in interest rates. [Call option](/call-option)s have positive rho (higher rates increase call value); [put option](/put-option)s have negative rho (higher rates decrease put value). Rho is typically the smallest of the five Greeks for short-dated options and becomes meaningful only for long-dated options or in high-rate environments. Rho captures the time-value-of-money effect on option pricing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rho — key facts</div>

<img src="/svg/derivatives.svg" alt="Interest rate chart showing option sensitivity" />

<div class="wiki-infobox-caption">Rho measures interest rate sensitivity.</div>

|   |   |
|---|---|
| **Calls** | Positive rho (higher rates = higher value) |
| **Puts** | Negative rho (higher rates = lower value) |
| **Magnitude** | Smallest Greek for short-dated options |
| **Long-dated options** | Rho becomes more significant |
| **Interpretation** | Option value change per 1% rate move |
| **Typically ranges** | 0.01 to 0.30 (depending on expiration) |
| **Affected by** | Time to expiration (longer = higher rho) |
| **Moneyness effect** | Similar magnitude at all strikes (smaller effect) |
| **Applied to** | Stock, currency, index options primarily |
| **Practical importance** | Low for most equity option traders |

</aside>

## Why interest rates affect options

Interest rates appear in option pricing because of the cost of carry—the expense of financing a position over time. In the [Black-Scholes model](/black-scholes-model), the risk-free rate is one of five inputs (alongside stock price, strike, time, and volatility).

Higher interest rates increase the [present value](/compound-interest) discount factor, making future payoffs worth less in today's dollars. This affects calls and puts differently:

- **Calls:** Higher rates increase the call's value because the cost of holding the stock (financing) becomes more expensive, making the option to defer purchase (the call) more attractive.
- **Puts:** Higher rates decrease the put's value because the opportunity cost of holding cash (receiving interest) increases, making the option to defer sale less attractive.

## Rho magnitude for different options

For a typical 3-month stock option, rho might be 0.02–0.05. A 1% increase in interest rates changes the option price by $0.02–$0.05. This is small compared to typical [delta](/delta) (0.5 for ATM), [vega](/vega) (0.2–0.3 for ATM), or [theta](/theta) (0.05–0.10 for ATM).

For a 2-year option, rho becomes more significant—0.20–0.40. Longer duration means more time-value-of-money impact.

## Rho and bond options

Rho becomes critically important when the underlying is interest-rate-sensitive. In interest-rate [swap](/swap) options or [swaption](/swaption)s, rho is one of the primary Greeks because the option holder is exposed to interest-rate risk directly.

## Rho in practice

For most equity option traders, rho is negligible. Stock option positions have rho somewhere around zero; interest-rate changes have minimal daily impact on equity option portfolios. Even a 1% Fed rate move is a minor factor in equity options.

For bond traders, currency traders, and swap dealers, rho is more relevant. A 1% shift in Treasury yields can meaningfully affect the value of rate options and bond option positions.

## Rho and [delta](/delta) hedging

When delta-hedging an option portfolio, rho is rarely the binding constraint. Traders focus on [delta](/delta), [gamma](/gamma), and [vega](/vega). Rho is managed passively or ignored unless the portfolio holds long-dated options in a volatile-rate environment.

## See also

<div class="wiki-seealso">

### Closely related

- [Options Greeks](/options-greeks/) — rho is one of the five (smallest)
- [Call option](/call-option/) — positive rho
- [Put option](/put-option/) — negative rho
- [Interest rate](/interest-rate/) — the driver of rho
- [Discount rate](/compound-interest) — related concept

### Greeks for comparison

- [Delta](/delta/) — stock price sensitivity (largest effect)
- [Vega](/vega/) — volatility sensitivity
- [Theta](/theta/) — time decay
- [Gamma](/gamma/) — delta sensitivity

### Interest-rate derivatives

- [Swaption](/swaption/) — rho is critical
- [Interest rate swap](/interest-rate-swap/) — underlying for swaptions
- [Bond](/bond/) — underlying for bond options
- [Yield curve](/yield-curve/) — affects rho

### Valuation

- [Black-Scholes model](/black-scholes-model/) — incorporates interest rates
- [Implied volatility](/implied-volatility/) — usually varies with rates
- [Discount factor](/compound-interest) — interest rate effect mechanism

### Deeper context

- [Option](/option/) — the family of derivatives
- [Derivatives pricing](/black-scholes-model/) — rho is one input
- [Risk management](/hedge-fund/) — rho typically low priority

</div>

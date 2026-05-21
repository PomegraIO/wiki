---
title: "FX Option"
description: "An FX option is a currency option traded in the professional OTC market. FX options are customized, large-sized, and priced using volatility models. They serve as hedging tools for corporations and are the basis for exotic derivatives."
keywords:
  - FX option
  - OTC option
  - professional option
  - at-the-money
  - in-the-money
image: "/svg/forex.svg"
---

*An **FX option** is a [currency option](/currency-option) in the institutional over-the-counter market, as opposed to the standardized, exchange-traded options on currency futures. FX options are customized to size and expiration, priced using volatility models (particularly the Black-Scholes framework), and are available in both vanilla and exotic structures. They are the primary tool for corporate currency hedging with payoff flexibility.*

<div class="wiki-hatnote">

For standardized exchange-traded contracts, see [currency future](/currency-future); for binding obligations, see [FX Forward](/fx-forward).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Option — key facts</div>

<img src="/svg/forex.svg" alt="FX option Greeks: delta, gamma, vega, theta" />

<div class="wiki-infobox-caption">OTC options priced using advanced volatility models.</div>

|   |   |
|---|---|
| **Structure** | OTC, bilateral, fully customized |
| **Sizes** | Typically $1 million+ notional minimum |
| **Expiry** | Any date, negotiated between counterparties |
| **Pricing model** | Black-Scholes, local volatility, stochastic volatility |
| **Greeks** | Delta, gamma, vega, theta quantify sensitivities |
| **Counterparty** | Major bank or financial institution |
| **Styles** | American (exercise anytime) or European (at expiry) |

</aside>

## OTC vs. exchange-traded currency options

Exchange-traded options on currency futures (like CME options) come in standardized sizes and expiries. An OTC FX option is bespoke: you can request any notional size, any expiry date, any strike price.

Exchange-traded options are cheap to trade (tight spreads), but you are limited to the exchange's contract specifications. OTC options are more expensive (wider bid-ask spreads), but you get exactly what you need.

Large corporations dealing in significant foreign-currency flows use OTC FX options because the precise hedging they require is not available on exchanges.

## Volatility and option pricing

An FX option's premium depends on five factors:

1. **Spot rate** — the current exchange rate
2. **Strike price** — the rate at which you can exercise
3. **Time to expiration** — longer time = higher premium
4. **Interest rates** — affect the expected drift of the currency
5. **Volatility** — the expected range of movement before expiration

The first four are observable. Volatility is not; it must be estimated. Higher volatility = higher premiums (larger potential payoff, more valuable to the holder).

Dealers use the **Black-Scholes model** or more advanced models (local volatility, stochastic volatility) to price options. These models convert forward assumptions about volatility into a dollar premium.

## The Greeks and risk management

Dealers managing a portfolio of options use the "Greeks" — sensitivities to changes in the five pricing factors:

- **Delta:** How much the option price changes if the spot rate moves by $0.01. Ranges from 0 to 1 for calls; −1 to 0 for puts.
- **Gamma:** How much delta changes if spot moves by $0.01. Higher gamma = more convexity = higher risk.
- **Vega:** How much the option price changes if volatility increases by 1%. All options are long vega.
- **Theta:** How much the option price decays per day as expiration approaches. Negative for long options (you lose money just from time passing).
- **Rho:** How much the option price changes if interest rates move by 1%.

A dealer quoting an option will manage these sensitivities by hedging with spot, forwards, and other options.

## Barrier options and exotic FX options

A **barrier option** (also called a "knock-in" or "knock-out" option) has a special feature: it becomes worthless (knock-out) or begins to exist (knock-in) if the spot rate touches a predetermined level before expiration.

Example: A European company buys a EUR/USD call with strike 1.1000 and a knock-out barrier at 1.1500. If the spot ever touches 1.1500, the option ceases to exist (even if it's profitable at that moment). The company paid less premium for this barrier because of the knock-out risk.

Barriers are cheaper than vanilla options and are popular with companies looking for cost-effective hedging.

## Implied volatility and the volatility smile

Dealers quote options in terms of implied volatility, not dollar premium. They might say: "EUR/USD 1-month 1.1000 call, 12.5% vol."

The market prices different strikes and maturities at different implied volatilities. Out-of-the-money options often trade at higher implied vol than at-the-money options, creating a "smile" shape in a volatility surface plot. This reflects the market's belief that crashes (large moves) are more likely than smooth distributions would suggest.

## See also

<div class="wiki-seealso">

### Closely related

- [Currency option](/currency-option) — conceptual foundation
- [FX Forward](/fx-forward) — binding alternative
- [Currency future](/currency-future) — exchange-traded alternative
- [FX Volatility Surface](/fx-volatility-surface) — option pricing landscape
- [Vanilla FX Option](/vanilla-fx-option) — standard option types

### Wider context

- [Interest rate](/interest-rate) — affects option pricing
- [Spot exchange rate](/spot-exchange-rate) — baseline for options
- [Central bank](/central-bank) — sometimes uses options in policy

</div>

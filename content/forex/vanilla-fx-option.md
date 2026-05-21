---
title: "Vanilla FX Option"
description: "A vanilla FX option is a standard currency option: a call (right to buy) or put (right to sell) a currency pair at a strike price on or before a specific date. Vanilla options are the building blocks; exotic options add special features."
keywords:
  - vanilla option
  - call option
  - put option
  - standard option
  - American European
image: "/svg/forex.svg"
---

*A **vanilla FX option** is a standard [currency option](/currency-option) with no special features. It is simply a call (the right to buy) or a put (the right to sell) at a fixed strike price, with a European or American exercise style. Vanilla options are the reference point for all option pricing and the building blocks from which exotic options are constructed.*

<div class="wiki-hatnote">

For options with special features, see [exotic FX option](/exotic-fx-option); for the professional market, see [FX option](/fx-option).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vanilla FX Option — key facts</div>

<img src="/svg/forex.svg" alt="Payoff diagrams for vanilla call and put options" />

<div class="wiki-infobox-caption">Call and put payoffs define all vanilla options.</div>

|   |   |
|---|---|
| **Types** | Call (right to buy) and put (right to sell) |
| **Exercise** | European (at expiry only) or American (anytime before) |
| **Payoff at expiry** | Call: max(0, spot − strike); Put: max(0, strike − spot) |
| **Premium** | Paid upfront by buyer; collected by seller |
| **Moneyness** | In-the-money (ITM), at-the-money (ATM), out-the-money (OTM) |
| **Pricing** | Black-Scholes model; based on spot, strike, time, rates, volatility |

</aside>

## Call options on currency pairs

A **call option** on EUR/USD with strike 1.1000 gives the right to buy euros at 1.1000. The buyer pays a premium (say, 0.0050 per euro, or $50 per 10,000 euros) upfront.

At expiration:

- If spot > strike (e.g., spot = 1.1500): The option is in-the-money. The buyer exercises, buys at 1.1000, and immediately sells at 1.1500, netting $5,000 per 10,000 euros. Minus the premium paid ($50 × 10,000 / 10,000 = $5,000), the net profit is... wait, that math is off. Let me recalculate: premium of 0.0050 per euro on 100,000 euros = $5,000 total premium. Payoff at exercise = (1.1500 − 1.1000) × 100,000 = $5,000. Net profit = $5,000 − $5,000 = $0. Break-even is at spot = strike + premium.

- If spot < strike (e.g., spot = 1.0800): The option is out-of-the-money. The buyer does not exercise. Loss = premium paid = $5,000 per 100,000 euros.

The seller (writer) of the call receives the premium but must deliver euros at the strike price if exercised. If the euro surges to 1.2000, the seller delivers at 1.1000 and loses on the position (sold euros at 1.1000 that they must buy at 1.2000).

## Put options on currency pairs

A **put option** on EUR/USD with strike 1.0800 gives the right to sell euros at 1.0800. The buyer pays a premium.

At expiration:

- If spot < strike (e.g., spot = 1.0600): The option is in-the-money. The buyer exercises, sells euros at 1.0800 (higher than the 1.0600 spot), and nets a payoff. Minus premium, this is a profit if the payoff exceeds the premium paid.

- If spot > strike (e.g., spot = 1.1000): The option is out-of-the-money. The buyer does not exercise. Loss = premium paid.

A put is useful for a company that fears the euro will weaken. By buying a put, they have insurance: if the euro crashes, they exercise and lock in a selling price.

## Moneyness and time value

**In-the-money (ITM):** A call is ITM if spot > strike; a put is ITM if spot < strike. ITM options have intrinsic value.

**At-the-money (ATM):** Spot = strike. The option has no intrinsic value, only time value.

**Out-of-the-money (OTM):** A call is OTM if spot < strike; a put is OTM if spot > strike. OTM options have no intrinsic value unless exercised.

Time value decays as expiration approaches. An OTM option that is 2 months away might be worth $1,000 (all time value). With one week left, it might be worth $100 (theta decay accelerates). On expiration day, an OTM option is worthless.

## American vs. European vanilla options

A **European vanilla option** can be exercised only on the expiration date. This is the standard in OTC currency options (FX options).

An **American vanilla option** can be exercised on any day before expiration. This added flexibility increases the premium. However, American options on currency pairs are rare; most OTC options are European.

## The binomial and Black-Scholes models

The **Black-Scholes model** is the standard for pricing vanilla options. It assumes:

- The underlying follows a lognormal distribution (random walk).
- Markets are frictionless (no transaction costs).
- No arbitrage.
- Constant volatility.

Given these assumptions, Black-Scholes produces a closed-form formula for the option premium.

The **binomial model** is an alternative: it models the currency as moving up or down in discrete steps and values the option recursively. Binomial is slower but more flexible for American options and exotic features.

## See also

<div class="wiki-seealso">

### Closely related

- [Currency option](/currency-option) — conceptual foundation
- [FX Option](/fx-option) — professional OTC vanilla options
- [Exotic FX Option](/exotic-fx-option) — non-standard options
- [FX Volatility Surface](/fx-volatility-surface) — how vanillas are priced
- [Strike](/forex-spread) — the exercise rate

### Wider context

- Interest rate parity — affects option pricing
- [Spot exchange rate](/spot-exchange-rate) — reference for strike selection
- [Forward exchange rate](/forward-exchange-rate) — pricing relationship

</div>

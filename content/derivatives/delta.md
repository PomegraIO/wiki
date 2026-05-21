---
title: "Delta"
description: "Delta measures how much an option's price moves for each one-dollar move in the underlying asset, ranging from 0 to 1 for calls and -1 to 0 for puts."
keywords:
  - delta
  - option greeks
  - price sensitivity
  - hedge ratio
  - derivative risk
image: "/svg/derivatives.svg"
---

*The **delta** of an option is the rate of change of the option's price with respect to the underlying asset's price. A delta of 0.5 means the option moves $0.50 for each $1 move in the stock. [Call option](/call-option/) deltas range from 0 (deep [out-of-the-money](/out-of-the-money/)) to 1.0 (deep [in-the-money](/in-the-money/)); [put option](/put-option/) deltas range from -1.0 to 0. Delta is also the hedge ratio—the number of shares needed to hedge an option position.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Delta — key facts</div>

<img src="/svg/derivatives.svg" alt="Price sensitivity slope chart" />

<div class="wiki-infobox-caption">Delta quantifies option price moves with stock moves.</div>

|   |   |
|---|---|
| **Call delta range** | 0 to +1.0 |
| **Put delta range** | -1.0 to 0 |
| **ATM delta** | ~0.5 for calls; ~-0.5 for puts |
| **Changes with** | Stock price and time |
| **Interpretation** | $0.50 option move per $1 stock move (delta = 0.5) |
| **Hedge ratio** | Shares to buy/sell to neutralize delta |
| **Affected by gamma** | Delta drifts as stock moves ([gamma](/gamma/)) |
| **Affected by time decay** | Delta drifts as expiration nears |
| **Probability implication** | ~40% ITM chance for 0.4 delta option |
| **Updated frequency** | Continuously during trading |

</aside>

## How delta works

If you own a [call option](/call-option/) on Apple with a delta of 0.6, and Apple stock rises $1, the call option typically rises about $0.60 in value. If the stock falls $1, the call falls about $0.60.

A delta of 1.0 means the option moves dollar-for-dollar with the stock—it behaves almost exactly like owning the stock. A delta of 0.0 means the option does not move at all with the stock.

For puts, deltas are negative. A [put option](/put-option/) with a delta of -0.6 means if the stock rises $1, the put falls about $0.60 in value (and vice versa for stock declines). This negative delta makes sense: puts gain value when stocks fall, the opposite of calls.

## Delta and moneyness

An [at-the-money](/at-the-money/) [call option](/call-option/) typically has a delta near 0.5, because there is roughly a 50% chance of finishing [in-the-money](/in-the-money/) vs. [out-of-the-money](/out-of-the-money/) by expiration.

A deep [in-the-money](/in-the-money/) call (stock at $110, strike at $100) has a delta near 0.9 or higher, because it is likely to remain in-the-money and behaves like the stock itself.

A deep [out-of-the-money](/out-of-the-money/) call (stock at $90, strike at $100) has a delta near 0.1 or lower, because there is a low probability of the stock rising 10%+ by expiration.

## Delta as hedge ratio

Delta has a second interpretation: the number of shares required to hedge an option position. If you own 100 [call options](/call-option/) with a delta of 0.5 each, your net delta exposure is 50 shares (100 options × 0.5). To hedge this directional exposure, you would short 50 shares. Any further price moves would roughly offset: a $1 stock rise gains you $50 on the calls but loses $50 on the short shares, netting zero.

This is the basis of [delta hedging](/call-option/)—constructing a position that is delta-neutral (net delta = 0) to eliminate directional risk.

## Delta changes with stock price: gamma

Delta is not constant; it changes as the stock price moves. This is where [gamma](/gamma/) comes in. [Gamma](/gamma/) tells you how fast delta changes. 

If you short 50 shares to hedge your 100 calls with delta 0.5 each, and the stock rises $1, the calls' delta might increase to 0.55 per option, for a total delta of 55. Your hedge is now 50 short shares against 55 delta exposure—you are under-hedged by 5 deltas. You must buy 5 more shares to rebalance.

This rebalancing, required because of [gamma](/gamma/), is how losses accumulate in delta-hedged positions.

## Delta and time decay

As [expiration date](/expiration-date/) nears, option deltas become more binary—closer to 0 or 1. An [at-the-money](/at-the-money/) call with 1 day to expiration has a delta close to 0.5 and very high [gamma](/gamma/). An [in-the-money](/in-the-money/) call with 1 day to expiration has a delta close to 1.0 (it will almost certainly finish in-the-money and convert to stock).

This is why near-expiration options are riskier to manage: small stock moves cause large delta changes, requiring constant rehedging.

## Delta in Black-Scholes

The [Black-Scholes model](/black-scholes-model/) computes delta as the derivative (rate of change) of the option price formula with respect to the stock price. For [european-option](/european-option/)s, this yields a clean closed-form formula. For exotic or [american-option](/american-option/)s, delta must be approximated numerically.

In practice, every broker and trading terminal displays delta automatically for every option contract.

## Portfolio delta

For a portfolio holding multiple options, you sum the deltas of all positions to get the portfolio's net directional exposure. If you own 100 calls with delta 0.6 and 50 puts with delta -0.4, your portfolio delta is 100 × 0.6 + 50 × (-0.4) = 60 − 20 = 40. This means a $1 move in the underlying would change your portfolio value by roughly $40.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — how delta changes with stock price
- [Theta](/theta/) — time decay
- [Vega](/vega/) — volatility sensitivity
- [Options Greeks](/options-greeks/) — the five Greeks
- [Call option](/call-option/) — positive delta (0 to +1)
- [Put option](/put-option/) — negative delta (-1 to 0)

### Applications

- [Delta hedging](/call-option/) — using delta to neutralize directional risk
- Covered call — delta-based hedge
- Bull call spread — balancing deltas
- Protective put — delta-based insurance

### Valuation

- [Black-Scholes model](/black-scholes-model/) — computes delta precisely
- [Implied volatility](/implied-volatility/) — affects delta through time decay
- [In-the-money](/in-the-money/) — higher delta
- [Out-of-the-money](/out-of-the-money/) — lower delta

### Deeper context

- [Option](/option/) — the family of derivatives
- Hedge ratio — delta expresses hedge size
- [Rebalancing](/alpha/) — delta-hedging requires continuous rebalancing

</div>

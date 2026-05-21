---
title: "Theta"
description: "Theta measures the daily decay of an option's time value, showing how much value an option loses each day as expiration approaches."
keywords:
  - theta
  - option greeks
  - time decay
  - daily decay
  - option value erosion
image: "/svg/derivatives.svg"
---

*The **theta** of an option is the rate at which its [time value](/time-value) decays as one day passes. Theta is negative for [option](/option) buyers (the option loses value daily) and positive for option sellers (the decay works in your favor). Theta accelerates as [expiration date](/expiration-date) approaches, with the steepest decay occurring in the final week. All else equal, theta favors the seller and penalizes the buyer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Theta — key facts</div>

<img src="/svg/derivatives.svg" alt="Decay curve showing accelerating time value loss" />

<div class="wiki-infobox-caption">Theta quantifies daily time value decay.</div>

|   |   |
|---|---|
| **Buyers** | Negative theta (lose money daily) |
| **Sellers** | Positive theta (gain money daily) |
| **Highest at** | At-the-money options |
| **Time pattern** | Low decay early; rapid decay near expiration |
| **Volatility impact** | Higher volatility = higher theta cost |
| **Interpretation** | Option loses $X per day (negative theta) |
| **Acceleration** | Theta doubles/triples in final weeks |
| **At expiration** | All remaining time value evaporates |
| **Formula basis** | Rate of change of option value with time |
| **Portfolio theta** | Sum of all position thetas |

</aside>

## How theta works

If you own a [call option](/call-option) with a theta of -$0.05, the option loses (roughly) $0.05 per day to time decay, all else equal. If the stock price and [volatility](/historical-volatility) do not change, your option loses $0.05 today, another $0.05 tomorrow, and so on.

For a [put option](/put-option), the same principle applies: negative theta for buyers, positive theta for sellers.

The negative theta for buyers is the price of holding a leveraged, wasting asset. The option's [time value](/time-value) evaporates toward zero at expiration. Unlike a [stock](/stock) that can hold value indefinitely, an option is a clock counting down.

## Theta decay acceleration

Theta is not constant over the option's life. Early on, decay is slow. An option with 6 months to expiration might lose $0.01 per day. The same option with 30 days left might lose $0.05 per day. With 5 days left, it might lose $0.20 per day.

This acceleration is why timing is critical for option buyers. Holding a slightly profitable option for two more weeks can erase the profit through theta decay.

## Theta and position management

For buyers, the standard approach is to sell the option before expiration, capturing remaining [time value](/time-value) rather than letting it decay to zero. If you buy an [out-of-the-money](/out-of-the-money) [call](/call-option) for $1 and two weeks later it is worth $1.10 due to [volatility](/historical-volatility) expansion, you might sell immediately rather than hold and watch theta decay it back to $0.50.

For sellers (covered call or naked calls/puts), theta is a friend. You pocket the daily decay. The strategy is to let time pass while the [stock](/stock) stays near or above the [strike price](/strike-price) (for calls) or below it (for puts).

## Theta and the gamma-theta trade-off

There is a mathematical relationship: for a delta-neutral portfolio, theta + ½ × [volatility](/historical-volatility)² × [gamma](/gamma) ≈ 0.

This says: if you are [theta](/theta)-positive, you are [gamma](/gamma)-negative (short [volatility](/historical-volatility)); if you are [theta](/theta)-negative, you are [gamma](/gamma)-positive (long [volatility](/historical-volatility)). You cannot have both working in your favor.

This is why calendar spreads (sell short-dated options, buy long-dated) are [theta](/theta)-positive but [gamma](/gamma)-negative: you collect time decay but lose if the market moves big.

## Theta at different option moneyness

**At-the-money [calls](/call-option):** Highest theta decay. The entire value is [time value](/time-value), and it evaporates quickly near expiration.

**In-the-money [calls](/call-option):** Lower theta decay (as a percentage). The option is anchored by [intrinsic value](/intrinsic-value), which does not decay.

**Out-of-the-money [calls](/call-option):** Moderate theta decay as a dollar amount, but since the option is cheap, the percentage decay is high.

The result: [at-the-money](/at-the-money) options have the highest absolute theta (in dollars per day).

## Theta in portfolio management

A large portfolio of short options (sold positions) with positive theta is profitable as long as the [stock](/stock) does not move much. Conversely, a large portfolio of long options (bought positions) with negative theta is fighting time decay—you need the [stock](/stock) to move enough to overcome theta losses.

This is why volatility prediction matters: high realized [volatility](/historical-volatility) helps long positions overcome [theta](/theta), while low realized [volatility](/historical-volatility) hurts them.

## See also

<div class="wiki-seealso">

### Closely related

- [Time value](/time-value/) — what theta measures decay of
- [Gamma](/gamma/) — gamma-theta trade-off
- [Options Greeks](/options-greeks/) — theta is one of the five
- [Expiration date](/expiration-date/) — theta accelerates approaching expiration
- [Call option](/call-option/) — negative theta for buyers
- [Put option](/put-option/) — negative theta for buyers

### Strategies exploiting theta

- Covered call — collect theta
- Calendar spread — pure theta play
- Iron condor — theta-positive short volatility
- [Naked puts](/put-option) — collect theta but face assignment risk

### Valuation

- [Black-Scholes model](/black-scholes-model/) — computes theta
- [Implied volatility](/implied-volatility/) — affects theta
- [At-the-money](/at-the-money/) — highest theta in dollars
- [Intrinsic value](/intrinsic-value/) — protected from decay

### Deeper context

- [Option](/option/) — the family of derivatives
- [Risk management](/hedge-fund/) — managing theta exposure
- [Time decay](/time-value) — theta quantifies daily decay rate

</div>

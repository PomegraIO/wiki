---
title: "Option Premium Components Explained"
description: "How an option premium breaks into intrinsic value and time value, and how each component changes as expiration approaches and the underlying moves."
keywords:
  - option premium components
  - intrinsic value time value
  - option pricing
  - time decay
  - theta decay
  - option value
---

*An **option premium** is the price you pay to buy (or receive to sell) an [option](/option/), and it comprises two distinct components: **intrinsic value** (the immediate profit if exercised) and **time value** (the probability of future profit before expiration).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Premium Components — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Premium = Intrinsic Value + Time Value; both shrink as expiration approaches.</div>

|   |   |
|---|---|
| **Total premium** | Sum of intrinsic and time value |
| **Intrinsic value** | Profit if exercised immediately (never negative) |
| **Time value** | Probability of additional gain; decays predictably |
| **Time decay** | Accelerates in final weeks before [expiration](/expiration-date/) |
| **At expiration** | Only intrinsic value remains; time value = zero |

</aside>

## Intrinsic Value: Immediate Profit

**Intrinsic value** is the profit an option holder would realize if they exercised it right now, at the current underlying price. It is never negative; options always have intrinsic value ≥ 0.

For a **call option**, intrinsic value = (underlying price − strike price), or zero if that figure is negative. A call on Apple stock with a $150 strike is worth $5 of intrinsic value if Apple trades at $155. If Apple trades at $140, the call has zero intrinsic value.

For a **put option**, intrinsic value = (strike price − underlying price), or zero if negative. A put with a $150 strike is worth $5 of intrinsic value if the underlying is at $145. At $160, it has zero intrinsic value.

Only [in-the-money](/in-the-money/) options have intrinsic value. Options that are [out-of-the-money](/out-of-the-money/) or [at-the-money](/at-the-money/) have zero intrinsic value.

The critical insight: intrinsic value is deterministic and easy to calculate. It depends only on the current price of the underlying and the strike price. It does not change based on time or future uncertainty.

## Time Value: The Premium Over Intrinsic

**Time value** is the portion of the premium that exceeds intrinsic value. It represents the market's assessment of the probability that the option will become more profitable (or stay profitable) before it expires.

Premium = Intrinsic Value + Time Value

If an Apple call with a $150 strike trades at $8 when Apple is at $155, the breakdown is:
- Intrinsic value: $5 (immediate exercise profit)
- Time value: $3 (the extra cost for future upside or protection)

The $3 time value reflects the possibility that Apple could move higher, yielding additional profit. It also reflects uncertainty: markets assign value to optionality, even if the option ends out-of-the-money.

Time value is always ≥ 0 and typically decreases as [expiration](/expiration-date/) approaches. The closer the expiration, the less time remains for the underlying to move favorably, so the option becomes riskier and cheaper.

## How Time Value Decays

**Theta** (or time decay) is the rate at which an option loses time value as days pass. For most options, theta is negative—meaning the option loses value each day, all else equal.

Time decay is *not* linear. It accelerates sharply in the final 2–4 weeks before expiration, and then explodes in the last few days. An option that loses $0.10 per day of time value with 60 days to expiration might lose $0.30 per day with 10 days left.

Consider a 90-day call option that costs $2.00 per share. After 30 days of price stability, it might be worth $1.50 (losing $0.50 of time value). After another 30 days, it might drop to $0.80. In the final 30 days, it could fall to $0.10. The buyer loses money simply because time passes, even if the underlying price stays flat.

This asymmetry favors sellers. Sellers of options benefit from theta decay; they collect the premium upfront and profit if the option expires worthless or in-the-money. Buyers face an uphill battle: they must see the underlying move enough to offset the decay.

## How Intrinsic and Time Value Change Together

When the underlying price moves, intrinsic and time value move in opposite directions for options approaching expiration.

If a call is [at-the-money](/at-the-money/) and the underlying rises by $1:
- Intrinsic value increases by $1.
- Time value typically *decreases* (because the call is now more profitable and has less room for further gain).
- The net effect depends on how fast time decay is occurring.

This relationship is captured by **delta** (the change in option price for a $1 move in the underlying) and **gamma** (the change in delta itself). Far from expiration, time value cushions the impact of price moves. Near expiration, every dollar of intrinsic gain eats into time value, and the option price becomes mostly determined by intrinsic value alone.

## Volatility's Role

**Implied volatility** (the market's forecast of future price swings) is the primary driver of time value. Higher volatility means the underlying could move further, so options become more valuable. A stock with 50% annualized volatility will have much higher option premiums (more time value) than a stock with 10% volatility, even with the same underlying price and strike.

As expiration approaches, the impact of volatility shrinks. With only one day to expiration, implied volatility matters far less than the current price. Volatility is most important for options with months to expiration.

## Example: Decomposing a Real Premium

Suppose IBM stock is trading at $140, and you see a call option with a $135 strike and 60 days to expiration offered at $8.50.

- **Intrinsic value:** $140 − $135 = $5.00
- **Time value:** $8.50 − $5.00 = $3.50

The $3.50 time value reflects 60 days of probability: IBM could rise further, volatility could surge, or even a pullback would still leave the call profitable. If you held this option and did nothing, you would watch:

- After 20 days: the option might be worth $7.80 (time value down to $2.80; IBM unchanged)
- After 40 days: the option might be worth $6.50 (time value down to $1.50)
- After 59 days: the option might be worth $5.05 (time value near zero)
- At expiration: the option is worth exactly $5.00 (intrinsic value only)

This decay happens even if IBM trades flat the entire time. A buyer who does not exit the position faces a losing trade; a seller would pocket the full $3.50 of time value.

## At Expiration

At the moment an option expires, time value vanishes. The option's value equals its intrinsic value, which is zero for out-of-the-money options and (underlying price − strike) for in-the-money calls or (strike − underlying price) for in-the-money puts.

Early assignment or forced settlement occurs at expiration for [in-the-money](/in-the-money/) options. The holder either exercises (receiving the intrinsic value in stock or cash) or allows the option to expire worthless.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — General overview of calls, puts, and how options work
- [Intrinsic Value](/intrinsic-value/) — Definition and role in valuation
- [Time Decay (Theta)](/time-decay-theta/) — How options lose value over time
- [Implied Volatility](/implied-volatility/) — Market's forecast of future price movement
- [In-the-Money](/in-the-money/) — Options with intrinsic value
- [Out-of-the-Money](/out-of-the-money/) — Options with zero intrinsic value

### Wider context

- [Black-Scholes Model](/black-scholes-model/) — Theoretical framework for option pricing
- [Strike Price](/strike-price/) — The agreed price for exercise
- [Expiration Date](/expiration-date/) — When the option ceases to exist
- [Volatility Smile](/volatility-smile/) — How implied volatility varies across strikes

</div>

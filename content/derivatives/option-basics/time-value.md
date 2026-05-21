---
title: "Time Value"
description: "Time value is the portion of an option's price that reflects the possibility of future profitable movement before expiration, independent of current intrinsic value."
keywords:
  - time value
  - option pricing
  - extrinsic value
  - decay
  - theta
image: "/svg/derivatives.svg"
---

*The **time value** of an option is the amount by which its market price exceeds its [intrinsic value](/intrinsic-value/). It represents the market's bet that the underlying asset will move enough to make the option more profitable before [expiration date](/expiration-date/). Time value decays toward zero as expiration approaches, a process captured by the Greek [theta](/theta/). For [at-the-money](/at-the-money/) or [out-of-the-money](/out-of-the-money/) options, time value is the entire option price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Time Value — key facts</div>

<img src="/svg/derivatives.svg" alt="Countdown to option expiration" />

<div class="wiki-infobox-caption">Time value decays as expiration nears.</div>

|   |   |
|---|---|
| **Formula** | Option price − intrinsic value |
| **[ATM](/at-the-money/) options** | Entire value is time value |
| **[ITM](/in-the-money/) options** | Often has meaningful time value |
| **[OTM](/out-of-the-money/) options** | All value is time value |
| **Decay pattern** | Slower early; faster near expiration |
| **At expiration** | Zero; option = intrinsic value only |
| **Sensitivity** | Driven by volatility and time remaining |
| **Theta decay** | Daily decay of time value |
| **Early seller gain** | Captures time value before decay |
| **Buyer headwind** | Time value evaporation costs money daily |

</aside>

## Time value defined

An option's market price has two components: [intrinsic value](/intrinsic-value/) (the immediate exercise profit) and time value (everything else). If a [call option](/call-option/) struck at $100 is trading at $8 and the stock is at $105, the intrinsic value is $5 and the time value is $3.

Time value represents the market's collective belief that the option will become more profitable before expiration. That $3 reflects the probability and magnitude of the stock moving above $105 further, or the value of waiting to see where the stock lands.

At [expiration date](/expiration-date/), all time value evaporates. The option becomes worth exactly its [intrinsic value](/intrinsic-value/) (or zero if [out-of-the-money](/out-of-the-money/)). This is why owning an option as expiration approaches is risky: you are watching your [time value](/time-value/) decay to nothing.

## The decay pattern: theta

Time value does not decay uniformly. Early in an option's life, the decay is slow. With 180 days to expiration, the option loses little time value per day. As expiration nears, decay accelerates. With 5 days left, the option loses significant time value daily. With 1 day left, decay is rapid—the time value can halve in a matter of hours.

This decay is measured by [theta](/theta/), the Greek that quantifies daily time value loss. A long option position has negative [theta](/theta/) (you lose money from time decay); a short option position has positive [theta](/theta/) (you profit from time decay).

## Time value and volatility

Higher [volatility](/historical-volatility/) means bigger expected price moves, which means a higher probability the option will become (or remain) profitable. This drives higher [time value](/time-value/).

When [implied volatility](/implied-volatility/) spikes—during a market crash or political uncertainty—option [time value](/time-value/) rises sharply, even if the stock itself has not moved. Conversely, when volatility falls in calm markets, [time value](/time-value/) declines, all else equal.

This is why [at-the-money](/at-the-money/) options (which are pure [time value](/time-value/)) are the most sensitive to [volatility](/historical-volatility/) changes. The entire option value derives from uncertainty about future movement.

## For different option positions

**For [call option](/call-option/) buyers:** You pay [time value](/time-value/) upfront. You profit if the stock moves enough in your direction to overcome [time decay](/theta/). The longer to expiration and the higher the [volatility](/historical-volatility/), the more [time value](/time-value/) you pay.

**For [put option](/put-option/) buyers:** Same logic; you pay [time value](/time-value/) betting the stock will fall enough.

**For [call option](/call-option/) sellers:** You pocket the [time value](/time-value/) premium. Your profit is the [time value](/time-value/) you collected minus any stock move that erodes your position.

**For [put option](/put-option/) sellers:** Same logic; you profit from [time decay](/theta/) as long as the stock does not fall hard enough to make you lose on intrinsic value.

## Early exit to capture time value

Many option traders do not hold to expiration. Instead, they sell early to capture a portion of the [time value](/time-value/) before it evaporates. If you buy a [call option](/call-option/) for $3 and it rises to $4.50 after a few weeks due to [volatility](/historical-volatility/) or stock movement, you can sell for $4.50 and lock in a $1.50 gain, rather than holding and watching [time decay](/theta/) erode your position.

This is especially true for [at-the-money](/at-the-money/) and [out-of-the-money](/out-of-the-money/) options, whose entire value is [time value](/time-value/). Holding them to expiration usually means watching the premium evaporate to zero.

## Time value in strategies

**Calendar spreads** (or "time spreads") exploit [time decay](/theta/) directly. You sell a short-dated option (which decays fast) and buy a longer-dated option (which decays slowly), profiting from the [time decay](/theta/) difference.

**Covered calls** allow you to profit from [time decay](/theta/) on the sold call while maintaining stock ownership upside below the strike.

**Strangles and straddles** on earnings often exploit the [time value](/time-value/) expansion and contraction around the event.

## Time value vs. intrinsic value behavior

[Intrinsic value](/intrinsic-value/) changes only when the stock price moves relative to the strike. [Time value](/time-value/) changes continuously with [volatility](/historical-volatility/), time to expiration, and interest rates.

A call struck at $100 with the stock at $105 has $5 intrinsic value that will not change unless the stock moves. But the [time value](/time-value/) component changes every second: if [volatility](/historical-volatility/) rises, [time value](/time-value/) rises; if [volatility](/historical-volatility/) falls, [time value](/time-value/) falls. As the hours tick toward expiration, [time value](/time-value/) erodes.

## See also

<div class="wiki-seealso">

### Closely related

- [Intrinsic value](/intrinsic-value/) — the other component of option price
- [Theta](/theta/) — daily time value decay
- [Option premium](/option-premium/) — total price = intrinsic + time value
- [Expiration date](/expiration-date/) — when time value drops to zero
- [In-the-money](/in-the-money/) — may have significant time value
- [At-the-money](/at-the-money/) — all value is time value
- [Out-of-the-money](/out-of-the-money/) — all value is time value

### Volatility effects

- [Implied volatility](/implied-volatility/) — drives time value
- [Historical volatility](/historical-volatility/) — realized moves vs. expected
- [Vega](/vega/) — sensitivity to volatility changes
- [Volatility smile](/volatility-smile/) — time value skew across strikes

### Strategies

- Calendar spread — exploits time decay
- Covered call — seller profits from time decay
- Straddle — benefits from volatility-driven time value
- Strangle — betting on time value expansion

### Deeper context

- [Option](/option/) — the family of derivatives
- [Black-Scholes model](/black-scholes-model/) — calculates time value
- [Decay](/theta/) — systematic time value loss
- [Greeks](/options-greeks/) — measure sensitivities including theta

</div>

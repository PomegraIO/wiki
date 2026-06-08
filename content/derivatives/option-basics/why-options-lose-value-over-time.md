---
title: "Why Options Lose Value Over Time"
description: "Explanation of time decay in options: why time value erodes, why decay accelerates near expiration, and its impact on buyers and sellers."
keywords:
  - why do options lose value over time
  - time decay options
  - theta decay
  - option time value erosion
  - time decay acceleration
image: /svg/derivatives.svg
---

*An option's value consists of [intrinsic value](/intrinsic-value/) (immediate profit if exercised) and [time value](/time-value/) (the price of remaining time). **Why do options lose value over time** is a function of diminishing probability and declining potential for profit as expiration approaches—a predictable decay that accelerates in the final weeks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Time Decay (Theta) — the erosion of option value</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Time value starts high and falls to zero at expiration; the rate of decay accelerates as the option nears its death date.</div>

|   |   |
|---|---|
| **Time value** | Premium minus intrinsic value; what you pay for time remaining |
| **Theta (decay rate)** | $ per day lost by the buyer; gained by the seller |
| **Decay acceleration** | Linear at first, then sharp in the final 2–4 weeks |
| **Effect on buyers** | Lose value daily even if stock does not move; need rapid move to profit |
| **Effect on sellers** | Gain value daily; profit if stock stays put |
| **Volatility interaction** | High volatility = higher time value = faster absolute dollar decay |
| **Out-of-the-money impact** | Worst hit—all value is time value, so 100% decay from start to finish |

</aside>

## The two components of option value

An option's premium consists of two distinct pieces: [intrinsic value](/intrinsic-value/) and time value. Intrinsic value is the profit you would realize if you exercised immediately. A call with a $100 strike and a $110 stock is $10 intrinsic. A put with a $100 strike and a $90 stock is $10 intrinsic. An [out-of-the-money](/out-of-the-money/) option has zero intrinsic value.

Time value is everything else—the extra premium you pay for the possibility that the option will move further in your favor. A $100 call on a $110 stock that costs $13 has $10 intrinsic and $3 time value. That $3 is what you are paying for the chance the stock rallies to $115 or beyond before expiration.

Time value is not free. Every day that passes, the probability distribution tightens—there is less time for a large move. Time value erodes toward zero as expiration approaches. On expiration day, time value is exactly zero. An option costs its intrinsic value only: call is $10, put is $10, out-of-the-money option is $0.

## Why the decay happens: shrinking opportunity

The longer an option has until expiration, the wider the range of possible stock prices at expiration. A call six months away could reasonably end up in the money if the stock moves 5, 10, or 20 percent—plenty of ways to profit. A call expiring tomorrow has a narrow window: only if the stock moves a significant percent in one day.

Statistical models like [Black-Scholes](/black-scholes-model/) quantify this: the probability of landing in the money shrinks as time shrinks, all else equal. Time value reflects this shrinking probability. With less time, there is less opportunity, and less opportunity means less value.

## The shape of decay: linear then exponential

Time decay is not uniform. In the early weeks of an option's life, the daily decay is gentle. A three-month option might lose $0.05 per day. In the final two to four weeks, the decay accelerates sharply. The final week might see $0.20 per day or more.

This curve is not due to the calendar—it is driven by probability math. The first day of an option's life removes 1 day from 90, a small fraction. The final day removes the last 1 day from 1, a 100% loss. The decay curve is similar to a square root function: slow at first, then sharp.

For an out-of-the-money option, this is devastating. An out-of-the-money call has no intrinsic value, so its entire value is time value. It starts at, say, $1.00, decays to $0.50 by week eight, then collapses to $0.10 in the final three weeks, to $0.01 in the final days, and finally to $0.00 at expiration. You might sell at $0.50 thinking the option is still worth something—then watch it decay to dust even if the stock never moves.

## Time decay and stock volatility

Time decay is not independent of [volatility](/historical-volatility/). Higher volatility inflates time value because there is a wider range of likely outcomes. A call on a volatile stock might carry more time value than a call on a stable stock, all else equal. This means the absolute dollar decay per day is also higher for volatile options.

However, the *rate* of decay (theta) as a percentage of remaining premium is faster for lower-volatility options. A very expensive, volatile call decays by 5 dollars per day; a cheap, stable call decays by $0.10 per day. But the expensive call's $5 decay is maybe 2 percent of its $250 value, while the cheap call's $0.10 is 10 percent of its $1.00 value. Either way, time decay is a percentage drag that accelerates into expiration.

## The buyer's problem: needing the stock to move

A call buyer pays $3 in time value, betting the stock will rally. If the stock goes nowhere for two weeks, theta decay eats the option. The buyer must now be right not only on direction but on timing. By the time the stock finally rallies, the option may have decayed so much that the move is not enough to offset the premium paid.

For example: you buy a three-month call for $5, betting the stock will rally from $100 to $110. The stock does eventually rally to $110 by month three—but by then, the call (worth $10 intrinsic) has lost so much time value that it is trading near $10 or below. You make a small profit or break even, not the doubling you imagined when you paid $5.

The longer the option is out-of-the-money, the more violent the decay. Out-of-the-money options are lotteries: cheap, but with a very high probability of expiring worthless. The odds are baked into the low price.

## The seller's advantage: collecting theta

Option sellers profit from time decay. A seller who writes a call for $5 wants the stock to go nowhere or down. Every day that passes, theta decay works in the seller's favor. If the stock stays flat, the $5 premium shrinks to $3, then $1, then $0. The seller keeps the premium. This is why [covered call](/covered-call/) writers (selling calls on stock they own) are often indifferent to modest stock rallies—the premium income from theta decay compensates for the foregone upside.

Institutional [option sellers](/option/) like market makers and hedge funds actively manage theta decay. They short calls and puts, collecting premium, and manage the resulting delta [hedge](/derivatives-hedging/) to remain neutral to price moves. Theta decay is free money for someone holding a delta-neutral short position.

## Volatility decay and smile effects

Time decay is complicated by the smile: the shape of [implied volatility](/implied-volatility/) across strikes. An out-of-the-money option decays not just because of calendar time but because the market reprices it as time passes. If implied volatility for far-out-of-the-money options drops (a common pattern as expiration approaches), the option decays even faster.

## Managing decay: buying earlier or using spreads

Option buyers fighting decay have a few approaches. One is to buy earlier—shorter-duration options (15–30 days to expiration) have less time value to lose absolutely, though the percentage decay is faster. Another is to use [spreads](/option-premium/)—for example, buying a call and selling a call further out of the money, thereby collecting some premium to offset the decay of the long call.

A put spread—buying a put at one strike and selling at a lower one—reduces the time value you are paying and caps your loss. The sold put's decay offsets some of the bought put's decay, smoothing the theta bleed.

## Expiration and the final collapse

On expiration day, any remaining time value is gone. An option costs its intrinsic value only. For out-of-the-money options, this is $0. The premium you paid is a total loss. This is the finality that makes holding expiration-day options so treacherous—there is no recovery, only the hard close.

## See also

<div class="wiki-seealso">

### Closely related

- [Time Decay (Theta)](/time-decay-theta/) — the Greek that measures option decay per day
- [Time Value](/time-value/) — what time value is and how it shrinks
- [Intrinsic Value](/intrinsic-value/) — the irreducible value at any moment
- [Implied Volatility](/implied-volatility/) — how the market prices future price swings, driving time value
- [Out of the Money](/out-of-the-money/) — options with zero intrinsic value, pure time decay
- [Option Premium](/option-premium/) — what you pay for an option, split into intrinsic and time value
- [Covered Call](/covered-call/) — selling calls to harvest theta decay on held stock

### Wider context

- [Options](/option/) — introduction to option mechanics and Greeks
- [Black-Scholes Model](/black-scholes-model/) — the mathematical framework underlying option pricing
- [Derivatives Hedging](/derivatives-hedging/) — why traders use options and how decay affects hedges
- [Option Expiration Date](/expiration-date/) — when options stop existing and all time value vanishes

</div>

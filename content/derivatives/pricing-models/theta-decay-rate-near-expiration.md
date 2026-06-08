---
title: "Why Theta Decay Accelerates Near Option Expiration"
description: "How theta decay, the rate of option premium erosion, accelerates exponentially in the final days before expiration as time-value vanishes."
keywords:
  - theta decay accelerates near expiration
  - theta decay
  - time decay option
  - option expiration
  - time value premium
image: "/svg/derivatives.svg"
---

*The rate of **theta decay**—premium loss due to the passage of time—accelerates sharply as an [option](/option/) approaches expiration. With 90 days to expiry, an option loses a fraction of its [time value](/time-value/) per day; with 7 days left, that daily loss per day accelerates dramatically. This non-linear pattern is a mathematical consequence of how volatility and time interact in option pricing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Theta Decay Near Expiration — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Time decay accelerates exponentially as an option nears its expiration date.</div>

|   |   |
|---|---|
| **Theta** | Greek letter representing daily time-decay in option value |
| **Rate of decay** | Non-linear; accelerates near expiration |
| **90 days out** | Might lose $0.05 per day |
| **7 days out** | Might lose $0.50 per day (10× faster) |
| **At the money** | Theta decay is greatest for ATM options |
| **Deep in/out of the money** | Theta decay is minimal (mainly intrinsic value) |
| **Expiration day** | All remaining time value vanishes to zero |

</aside>

## The math of time value and theta

An option's price has two components: [intrinsic value](/intrinsic-value/) and time value.

**Intrinsic value** is what the option is worth if exercised today. A [call option](/call-option/) with a [strike price](/strike-price/) of $100 on a stock trading at $110 has $10 of intrinsic value. A put option with a $100 strike on the same $110 stock has zero intrinsic value.

**Time value** is the premium above intrinsic. That $110 call on a $100 strike might be trading at $13, meaning $3 of time value ($13 − $10 intrinsic). This $3 represents the probability that the stock will move further in-the-money before expiration, benefiting the option holder. Time value is pure optionality—the right to benefit from further price movement.

Time value depends on:
- **Time to expiration**: more time means more opportunity for large price swings, so more value.
- **Volatility**: higher [implied volatility](/implied-volatility/) means larger expected price swings, so more value.
- **Current stock price vs. strike**: at-the-money options have the most time value (because they benefit from a move in either direction).

## Why decay accelerates exponentially

The key insight is that time value decays *non-linearly*. It's not like a battery running down at a constant rate. Instead, decay accelerates as expiration approaches.

Imagine a stock and a call option with a 90-day horizon. The implied volatility is 30%, meaning the market expects annualized price swings around 30%. Over 90 days (one quarter), that annualized volatility translates to an expected move of roughly 15% (annualized volatility ÷ √4 quarters). That big possible move supports substantial time value.

Now jump to 7 days to expiration, and implied volatility is still 30%. But 7 days is only 1/52 of a year. The expected move shrinks to about 4% (annualized volatility ÷ √52 weeks). The option is far less likely to swing wildly, so the time value is tiny.

The rate of decay from 90 days to 60 days is shallow—maybe the option loses $0.02 per day. But from 14 days to 7 days, the option might lose $0.30 per day. And in the final 3 days, it might lose $0.50 per day—a ten-fold acceleration.

Mathematically, this comes from the [Black-Scholes model](/black-scholes-model/), where theta (the time-decay Greek) depends on both the square root of time and the [volatility smile](/volatility-smile/). As time shrinks, the denominator (√ time) shrinks, and theta's magnitude increases. The effect compounds: the closer you get to zero, the steeper the decay.

## Theta and [gamma](/gamma/)

There's a related Greek called [gamma](/gamma/), which measures how much an option's [delta](/delta/) (its directional sensitivity) changes when the underlying stock moves $1. Gamma also spikes near expiration, particularly for at-the-money options.

Intuitively: with 90 days to go, a $1 move in the stock is relatively small compared to the expected 15% move. The option's delta (the percentage of the stock price change that flows through to the option) doesn't change much. But with 1 day to go, a $1 move is huge relative to the expected move, and the option's delta can swing from 10 to 90 in a single trade. That's high gamma.

Theta and gamma are linked by a seesaw: when gamma is high (near expiration, near-the-money), theta is also high. When gamma is low (far from expiration, deep in or out of the money), theta is low. This is a key principle in [derivatives hedging](/derivatives-hedging/): you cannot have high time decay without accepting high directional risk.

## The shape of decay: why near-the-money options suffer most

An at-the-money (ATM) option has the most time value per dollar of intrinsic value. A call with strike $100 on a $100 stock has zero intrinsic and maybe $5 of time value; a call with strike $90 on a $100 stock has $10 intrinsic and maybe $1 of time value.

Because ATM options are pure time value, theta decay hits them hardest. As the option nears expiration, the ATM option's time value does not just decay—it evaporates. With 1 week left, the ATM $100 call might be worth $2 (down from $5 a week prior). If the stock stays at $100 at expiration, that option expires worthless.

Deep in-the-money (ITM) and deep out-of-the-money (OTM) options decay more slowly as a proportion of their value, because they have more intrinsic value (for ITM) or are so unlikely to matter (for OTM) that time value is minimal to begin with.

## Practical implications for traders

**Short sellers of options** benefit from theta decay. A trader who sells a call, betting the stock won't rise much, earns money from the daily decay of the option's premium—regardless of whether the stock moves. This is often called "selling time" or being "short theta." The closer to expiration, the faster the short option seller's profit accumulates.

**Long buyers of options** suffer from theta decay. Every day, the option loses money to time erosion. This is a drag on the trade; the stock must move in the buyer's favor to overcome both the decay and the [bid-ask spread](/bid-ask-spread/) paid at entry. Options are a "wasting asset"—they decline in value over time, all else equal.

**Time decay and [volatility](/implied-volatility/)**: If a trader buys an option hoping for a big move, they pay premium for implied volatility. If the stock then stays quiet, the implied volatility contracts, and the option loses value on two fronts: theta decay and falling IV. This is called "losing on volatility" and is a major risk for long-option traders.

## The final day: expiration

On the day of expiration, all time value is gone. An at-the-money option is worthless; an in-the-money option is worth exactly its intrinsic value. A call with a $100 strike, on a stock trading at $101 at 4 PM on expiration day (in-the-money by $1), is worth exactly $1 (or $100 per contract). No more, no less.

This is why expiration weeks can be volatile. Market makers, traders, and the public are all adjusting positions, and a $1 move in the stock can swing an ATM option from $2 to worthless. The [gamma](/gamma/) risk (the non-linearity of delta) is extreme, and prices can whip around. Traders often close options before expiration to avoid this frenzy and the risk of illiquid trading in the final hours.

## Using theta decay strategically

Professional traders exploit theta decay in several ways:
- **[Covered call](/covered-call/)**: Own stock, sell a call option. Collect theta premium as time decay. If the stock stays flat or rises, the premium is pure profit.
- **Iron condor / short straddle**: Sell both a call and put near-the-money, bet the stock stays within a range, and profit from theta decay.
- **Calendar spreads**: Buy a long-dated option and sell a short-dated option on the same strike. The short position decays faster, and the trader profits if volatility expands or the stock stays near the strike.

These strategies work because they harness the predictable nature of theta decay. The cost is [gamma](/gamma/) risk—the possibility of a sharp move that overwhelms the benefit of time decay.

## See also

<div class="wiki-seealso">

### Closely related

- [Theta](/theta/) — the Greek measuring time decay
- [Time value](/time-value/) — the component of option price that theta erodes
- [Gamma](/gamma/) — related Greek; spikes when theta spikes
- [Implied volatility](/implied-volatility/) — affects the rate of theta decay
- [Option premium](/option-premium/) — the price paid for time value and intrinsic value
- [Time decay theta](/time-decay-theta/) — foundational concept in options pricing

### Wider context

- [Black-Scholes model](/black-scholes-model/) — mathematical framework for calculating theta
- [Covered call](/covered-call/) — strategy that harvests theta decay
- [Derivatives hedging](/derivatives-hedging/) — how traders manage theta and gamma risk
- [Volatility smile](/volatility-smile/) — affects theta across different strikes
- [Option](/option/) — the underlying instrument

</div>

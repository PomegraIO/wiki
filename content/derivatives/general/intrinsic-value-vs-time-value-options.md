---
title: "Intrinsic Value vs Time Value in an Option Premium"
description: "An option's price splits into intrinsic value (immediate exercise worth) and time value (remaining probability premium). Understanding this decomposition is key to pricing, risk, and trading strategy."
keywords:
  - intrinsic value vs time value options
  - option premium decomposition
  - time value decay theta
  - in-the-money options
image: /svg/derivatives.svg
---

*An option's total price—its **premium**—divides into two components: **intrinsic value**, the amount the option would be worth if exercised immediately, and **time value**, the additional premium paid for the possibility that the option will become more valuable before expiration. Understanding this split is fundamental to pricing, hedging, and recognizing how decay and volatility shape your position.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Intrinsic vs. Time Value — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Every option premium is the sum of what it's worth now plus what it might become.</div>

|   |   |
|---|---|
| **Intrinsic value** | Amount in-the-money; zero if out-of-the-money |
| **Time value** | Premium - Intrinsic Value |
| **At expiration** | Time value collapses to zero; only intrinsic remains |
| **Theta decay** | Time value erodes daily, accelerating near expiration |
| **Volatility impact** | Higher volatility increases time value |
| **Out-of-money calls** | Comprise 100% time value |

</aside>

## Intrinsic Value: The In-The-Money Portion

**Intrinsic value** is the profit you would realize if you exercised the option immediately. For a call option, it is the amount by which the current stock price exceeds the strike; for a put, the amount by which the strike exceeds the current stock price.

**Call intrinsic value** = max(Stock Price − Strike Price, 0)

**Put intrinsic value** = max(Strike Price − Stock Price, 0)

If the intrinsic value is zero (the option is out-of-the-money), you cannot exercise profitably and intrinsic is zero by definition.

### Examples

- **Call option, strike $100, stock trading $110:** Intrinsic = $110 − $100 = $10. You could exercise today, buy the stock at $100, and sell it for $110, netting $10 per share (before commissions and taxes).

- **Put option, strike $50, stock trading $48:** Intrinsic = $50 − $48 = $2. Exercising sells the stock at the $50 strike when the market price is $48, yielding $2 per share of profit.

- **Call option, strike $100, stock trading $95:** Intrinsic = 0. The call is out-of-the-money; there is no exercise profit. However, the call may still have a positive premium (time value) if there is a chance the stock will exceed $100 before expiration.

## Time Value: The Probability Premium

**Time value** is the amount of the option premium above intrinsic value. It represents the market's assessment of the probability that the option will increase in value (become more in-the-money or less out-of-the-money) before expiration.

**Time Value** = Option Premium − Intrinsic Value

Time value reflects three forces:

1. **Remaining time to expiration.** The longer the option lives, the more opportunity for the stock to move favorably. A 6-month call has more time value than a 1-week call, all else equal.

2. **Volatility.** If the stock is likely to move a lot, the option has more upside probability. A call on a volatile biotech stock has higher time value than a call on a stable utility, even with the same strike and time to expiration.

3. **Interest rates and dividends.** Slight factors, but factored into pricing models. Higher rates increase call time value (deferred capital outlay is worth more). Dividends reduce call time value (the stockholder gets paid; the call holder does not).

### Worked Example

Suppose a stock trades at $100. A 3-month call option with a $100 strike is priced at $5.50 per share.

- **Intrinsic value** = $100 − $100 = $0
- **Time value** = $5.50 − $0 = $5.50

The entire $5.50 premium is the market's bet that the stock will rise above $100 in the next 3 months (or that volatility offers upside optionality). If you buy this call and the stock stays at $100 on expiration day, the option expires worthless; you lose the full $5.50.

Now suppose the same stock rallies to $105 after 1 month, and the call is re-priced at $6.80.

- **New intrinsic value** = $105 − $100 = $5
- **New time value** = $6.80 − $5 = $1.80

The intrinsic value grew by $5 (the stock moved $5 in-the-money). But the option premium only rose $1.30 (from $5.50 to $6.80). The time value shrank by $3.70 (from $5.50 to $1.80) because 1 month elapsed and the remaining time-to-expiration is now 2 months instead of 3. This erosion is **theta decay**.

## Theta Decay: Time Value's Countdown

**Theta** (or time decay) measures how much an option loses per day as expiration approaches, assuming the stock price and volatility stay flat. For an option holder, theta is an enemy; for a seller, an ally.

Time value decay is not linear. It accelerates in the final weeks before expiration. An at-the-money option with 1 month remaining might lose $0.05 per day; an otherwise identical option with 1 week to go might lose $0.15 per day. This is why short-dated options are so useful for sellers and risky for buyers.

### Why Time Value Collapses at Expiration

At expiration, there is zero time remaining, so zero time value. An option is worth exactly its intrinsic value:

- An in-the-money call expires and is exercised for its intrinsic value.
- An out-of-the-money call expires worthless.

There is no "one more day" to hope for a favorable move.

## Volatility's Role in Time Value

**Implied volatility** (the market's forecast of future price swings) is the largest lever on time value. Higher volatility = higher time value, because the greater the expected move, the greater the probability the option will finish in-the-money or more in-the-money.

A classic example: on the day before earnings, a stock's implied volatility (IV) often spikes. Calls and puts both become more expensive, even if the stock price doesn't move. Once earnings are announced and the stock settles, IV collapses, and the option premium drops sharply—even if the intrinsic value increased. This is **volatility crush**: the loss of time value as uncertainty is resolved.

## Out-of-The-Money Options: Pure Time Value

An out-of-the-money option has zero intrinsic value. Its entire premium is time value. This is why OTM options decay so visibly and why sellers love them.

**Example:** A call with a $110 strike on a $100 stock, 3 months to expiration, priced at $2.00 per share. All $2.00 is time value. The option has no immediate exercise profit; it is a pure bet on a $10+ move (plus the strike) in 3 months. As expiration nears and the stock doesn't reach $110, the $2.00 erodes day by day. On the final day, if the stock is still at $100, the option is worth zero.

## Put-Call Parity and the Intrinsic-Time Value Link

The relationship between call and put premiums is not arbitrary. **Put-call parity** ensures that the combined cost of a call and the sale of a put (both same strike and expiration) equals the forward price of the stock adjusted for interest rates and dividends.

In practical terms, this means the time value of a call and put at the same strike are linked. If a call's time value is high (stock is volatile), the put's time value will be similarly high, because both benefit from the same volatility.

## Using Intrinsic-Time Value Decomposition in Trading

Traders and hedgers use this decomposition for several purposes:

**Estimating fair value.** Using models like the [Black-Scholes Model](/black-scholes-model/), you can estimate the theoretical time value for a given volatility. If the market is trading an option above or below fair value, that's a signal to buy or sell.

**Understanding theta risk.** Holding an OTM option naked exposes you to pure time decay. Many traders hedge theta by simultaneously selling nearby OTM options (a spread) to offset the daily bleed.

**Selling volatility.** Short sellers (calls and puts) benefit from theta decay and, if volatility drops, from the collapse in time value. This is the classic "short premium" strategy.

**Evaluating ITM vs. OTM entry points.** Buying an in-the-money call gives you intrinsic value (downside floor) but costs more upfront. Buying an out-of-the-money call is cheaper but all-or-nothing.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational structure and mechanics
- [Option Premium](/option-premium/) — the full price of which intrinsic and time are parts
- [Time Decay (Theta)](/time-decay-theta/) — daily erosion of time value
- [Implied Volatility](/implied-volatility/) — market forecast baked into time value
- [Strike Price](/strike-price/) — the reference point for intrinsic calculation
- [Black-Scholes Model](/black-scholes-model/) — standard framework for pricing both components

### Wider context

- [Call Option](/call-option/) — applies to long calls in particular
- [Put Option](/put-option/) — applies to long puts
- [Vega](/vega/) — sensitivity to volatility changes
- [Theta](/theta/) — the sensitivity to time decay

</div>

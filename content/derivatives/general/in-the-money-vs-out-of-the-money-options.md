---
title: "In-the-Money vs Out-of-the-Money Options"
description: "In-the-money vs out-of-the-money options differ in intrinsic value, probability of profit, and premium. Understand moneyness and how it shapes option pricing and exercise."
keywords:
  - in the money options
  - out of the money options
  - option moneyness
  - intrinsic value
  - option premium
  - at the money
image: /svg/derivatives.svg
---

*The **moneyness** of an option describes whether it is profitable to exercise right now. An **in-the-money (ITM)** option has [intrinsic value](/intrinsic-value/)—exercising it immediately yields a profit. An **out-of-the-money (OTM)** option has no intrinsic value; immediate exercise would be a loss. **At-the-money (ATM)** options sit on the boundary. Moneyness is the primary determinant of how much of an option's [premium](/option-premium/) is due to intrinsic value versus [time value](/time-value/), and it drives the [delta](/delta/)—the sensitivity of the option's price to moves in the underlying.*

## Defining Moneyness for Calls and Puts

For a **call option** (the right to buy), moneyness is straightforward:
- **In-the-money:** The stock price is above the strike price. If you own a call with a $50 strike and the stock is trading at $55, you are ITM by $5. Exercising yields $5 of profit per share (before commissions).
- **Out-of-the-money:** The stock price is below the strike price. A $50 call when the stock is at $45 is OTM by $5. Exercising would mean buying at the strike and immediately selling in the market for a loss.
- **At-the-money:** The stock price equals the strike price. A $50 call with the stock at $50 is ATM.

For a **put option** (the right to sell), the logic inverts:
- **In-the-money:** The stock price is below the strike price. A $50 put when the stock is at $45 is ITM by $5. You could exercise (sell at the strike) and pocket $5 per share versus the market price.
- **Out-of-the-money:** The stock price is above the strike price. A $50 put when the stock is at $55 is OTM by $5.
- **At-the-money:** Strike and spot price are equal.

## Intrinsic Value vs. Time Value

An option's total premium breaks into two components: **intrinsic value** and **time value**.

**Intrinsic value** is the profit you would realize by exercising immediately. For a $50 call when the stock is $55, intrinsic value is $5. For a call when the stock is $45, intrinsic value is zero (you would never exercise a loss). Intrinsic value is never negative.

**Time value** is the premium paid above intrinsic value. A $50 call trading at $7 when the stock is $55 has $5 of intrinsic value and $2 of time value. Time value reflects the possibility that the option will become even more profitable before expiration. With 60 days to expiration, the stock could climb further, so buyers pay $2 for that chance.

The split between intrinsic and time value changes with moneyness:
- **Deep in the money:** A $50 call when the stock is $80 has $30 of intrinsic value but very little time value. The option is almost certain to be exercised, so there is little upside uncertainty left.
- **At the money:** A $50 call when the stock is $50 has zero intrinsic value, but time value is at its maximum. With 60 days, the stock could go up, generating profit. Buyers will pay the highest premium for ATM options because the upside is maximized.
- **Deep out of the money:** A $50 call when the stock is $30 has zero intrinsic value and minimal time value. The stock would need to rally $20 to even reach the strike, so the probability of profit is low, and buyers pay very little.

This relationship is critical: the time value of an option decays as expiration approaches. An OTM call with 60 days to expiration has meaningful time value. The same call with 1 day to expiration has nearly zero—[theta](/theta/), the rate of time decay, accelerates into expiration.

## Delta and the Probability of Profit

The **delta** of an option is the change in the option price for a $1 move in the underlying stock. It also approximates the probability that the option will expire ITM (under a simplified model).

- **ATM options** have a delta of roughly 0.50 (for calls) or -0.50 (for puts). They are equally likely to expire ITM or OTM, so there is a ~50 percent chance of intrinsic value at expiration.
- **ITM options** have deltas closer to 1.0 (calls) or -1.0 (puts). A deep ITM call might have a delta of 0.95, meaning it moves almost dollar-for-dollar with the stock and has a very high probability of expiring ITM.
- **OTM options** have deltas closer to 0. An OTM call with a delta of 0.20 has roughly a 20 percent chance of expiring ITM. It is a longer-shot bet.

This is why OTM options are cheaper than ATM, which are cheaper than ITM: you are paying less for less probability. But the leverage is reversed. A $1 move in the stock might move an OTM call by $0.20 (delta 0.20), a 20 percent gain in the call's price. The same move in an ITM call with delta 0.90 might be a 1 percent gain. Speculators often prefer OTM options for leverage, even though they have low probability, because a small move yields a large percentage return.

## Implied Volatility and the Smile

The [implied volatility](/implied-volatility/) of an option—the market's forecast of how much the stock will move—also varies with moneyness. In many markets, implied volatility is higher for OTM options than for ATM or ITM. This **volatility smile** or **skew** reflects the market's belief that crashes and jumps are more likely than smooth moves. A crash might take the stock down sharply, making far OTM puts valuable as insurance; the market prices them with higher implied vol to compensate for this tail risk.

This means an OTM put is sometimes more expensive than ATM put theory alone would predict, because the implied volatility is lifted. A portfolio manager buying index puts for downside protection often finds OTM puts are not as cheap (relative to the move they insure against) as a naive reading of delta would suggest.

## Why Moneyness Matters for Hedging and Speculation

**For hedging:** An investor long a stock at $100 might buy a $95 put to protect against declines below $95. A $95 put when the stock is $100 is OTM—the buyer is paying for insurance that may not be needed. But the cost is low because the put has low probability of expiring ITM, and this is the point of insurance: you pay a small premium for large downside protection. An ITM put ($105 strike) would cost much more because it is closer to certain to be exercised. The hedge is more expensive but leaves less unprotected downside.

**For speculation:** A trader bullish on a stock might buy a call OTM (cheaper leverage) rather than ATM or ITM. If the stock rallies, the OTM call can yield a large percentage gain. But if the stock stalls, the call decays and expires worthless. This is the classic OTM option trade: low cost, high probability of loss, but a large payoff if you are right.

## Practical Pricing Example

Imagine a stock trading at $100 with 30 days to expiration and 20 percent implied volatility. An approximate pricing model (like [Black-Scholes](/black-scholes-model/)) might show:
- $95 call (ITM by $5): $6.50 premium ($5 intrinsic, $1.50 time value)
- $100 call (ATM): $1.80 premium (all time value, zero intrinsic)
- $105 call (OTM by $5): $0.35 premium (all time value, low probability)

Buying the $105 call for $0.35 is cheaper, but the stock must close above $105.35 at expiration to profit (break even). The $100 call costs $1.80 but only needs a close above $101.80. The $95 call is nearly guaranteed profit if the stock moves at all, but you paid the most for it.

With one day left, that same $100 call might be worth $0.10 if the stock is still at $100—[theta](/theta/) has evaporated almost all time value. The $105 OTM call might be worth a penny or expire worthless. This is why time decay accelerates for OTM options: with little intrinsic value and expiration approaching, there is almost no chance left.

## Early Exercise and American vs. European Options

For **American options**, which can be exercised any time before expiration, being ITM creates an additional consideration: should you exercise now or wait? An ITM call might be worth more unexercised (because of remaining time value) than as stock. But if the underlying pays a [dividend](/dividend/), the call owner might exercise before the ex-dividend date to capture the dividend, even though time value remains.

For **European options**, which can only be exercised at expiration, moneyness is only relevant at the end. But during the life of the option, an OTM European option might drift further OTM (worthless decay) or back into the money. Speculators and hedgers track moneyness throughout to understand whether their bet is working.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — The right to buy (call) or sell (put) an asset at a set price.
- [Intrinsic value](/intrinsic-value/) — The immediate profit from exercising an in-the-money option.
- [Time value](/time-value/) — The portion of an option premium above intrinsic value.
- [Delta](/delta/) — The sensitivity of an option price to moves in the underlying; approximates probability of expiring ITM.
- [Theta](/theta/) — Time decay; how much an option loses value each day as expiration approaches.
- [Implied volatility](/implied-volatility/) — The market's forecast of the stock's volatility, baked into the option price.
- [Call option](/call-option/) — The right to buy at a fixed price.
- [Put option](/put-option/) — The right to sell at a fixed price.

### Wider context

- [Black-Scholes model](/black-scholes-model/) — The standard framework for option pricing based on moneyness and time to expiration.
- [Covered call](/covered-call/) — A strategy selling OTM calls on a stock you own.
- [Protective put](/protective-put/) — A hedging strategy buying OTM puts for downside protection.
- [Volatility smile](/volatility-smile/) — How implied volatility varies with moneyness.

</div>

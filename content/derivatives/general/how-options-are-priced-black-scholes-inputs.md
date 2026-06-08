---
title: "How Options Are Priced: The Black-Scholes Inputs Explained"
description: "How spot price, strike, time to expiration, volatility, and interest rate move an option premium via Black-Scholes model intuition."
keywords:
  - how options are priced black scholes inputs
  - black scholes model parameters
  - option pricing spot strike time vol
  - option premium calculation
image: /svg/derivatives.svg
---

*The Black-Scholes model is the backbone of modern option pricing. Five inputs go in — the stock price, the strike price, time to expiration, volatility, and the interest rate — and out comes the fair value of a call or put. Each input tells you something about the option's likelihood of profit and how much breathing room it has. Understanding how each moves the premium shows you intuitively why options trade the way they do.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Black-Scholes Inputs — the five levers</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Five numbers determine what an option is worth: current price, strike, time left, volatility, and rates.</div>

|   |   |
|---|---|
| **Spot (S)** | Current stock price. Higher spot = higher call value, lower put value. |
| **Strike (K)** | Agreed exercise price. Out-of-money strikes are cheaper; in-the-money are pricier. |
| **Time (T)** | Years to expiration. More time = more value (time decay accelerates near expiry). |
| **Volatility (σ)** | Annualized % move. Higher vol = higher call and put values. |
| **Rate (r)** | Risk-free interest rate. Small effect; higher rate = slightly higher calls. |

</aside>

## The Black-Scholes equation and its intuition

The Black-Scholes formula for a European call option is:

C = S × N(d₁) − K × e^(−rT) × N(d₂)

where d₁ and d₂ are functions of the five inputs, and N() is the cumulative normal distribution.

This looks intimidating. The intuition is cleaner: an option's value is the probability-weighted sum of its payoff at expiration, discounted back to today. A call is worth what you'd expect to gain if you exercised it, multiplied by the probability you'd want to, and discounted for the cost of money over time.

Each of the five inputs changes that probability and that expectation. Let's walk through them.

## Spot Price: the current fuel

The spot price is the stock price *right now*. 

For a **call option** (the right to buy), a higher spot price is good news. If you own a call with strike $100 and the stock jumps from $90 to $100, your call is now in-the-money; it's worth at least $0 at expiration. Every dollar the stock rises, the call premium rises roughly $0.50 to $0.70 (the exact amount depends on other factors, but it's always positive and less than $1.00).

For a **put option** (the right to sell), a higher spot price is bad news. If you own a put with strike $100 and the stock rises from $90 to $100, your put is now out-of-the-money; it's worthless at expiration. Every dollar the stock rises, the put premium falls.

The reason the call doesn't rise dollar-for-dollar with the spot is that you only have the *right* to buy, not an obligation. If the stock plummets, your call is worthless, and you haven't lost more than your premium. The put owner has limited upside (the stock can only fall to zero) and therefore receives less than a $1.00 sensitivity to spot price.

**Intuition**: Spot price is the current state of the world. A call is more valuable when the spot is high (closer to a profitable exercise). A put is less valuable.

## Strike Price: the exercise threshold

The strike (or exercise price) is the price at which the option holder can buy (call) or sell (put).

An out-of-the-money (OTM) call — one where the strike is above the current spot — is cheap. It only has value if the stock rises above the strike before expiration. The farther OTM, the less likely that happens, so the cheaper the call.

An in-the-money (ITM) call — where the strike is below the spot — is expensive. It has intrinsic value already (the difference between spot and strike) plus additional time value. The farther ITM, the more expensive and the more it behaves like owning the stock.

For puts, it's reversed: OTM puts (strike below spot) are cheap; ITM puts (strike above spot) are expensive.

**Example**: A stock trades at $50. A $45 call (ITM) might be worth $6. A $50 call (at-the-money) might be worth $2.50. A $55 call (OTM) might be worth $0.75. As you move strikes higher (for calls), the option gets cheaper because it's farther from profit.

The relationship is not linear. The curve is convex — the drop in value accelerates as you move OTM. This is because very OTM options have almost no chance of finishing ITM.

**Intuition**: Strike determines how much room the stock has to move in your favor. A lower strike for a call (deeper ITM) is more valuable; a higher strike (deeper OTM) is cheaper.

## Time to Expiration: the edge and the decay

Time to expiration is the amount of calendar time left. Time value is the amount of the premium that comes from "there's still time for this to move in my favor."

An option with 6 months until expiration has much more time value than an option with 1 week left, even if everything else is identical. That's because the stock could move much farther in 6 months than in 1 week.

**Holding everything else constant**, more time is always worth more. A 6-month call is worth more than a 3-month call on the same stock at the same strike. The reason: the stock has more opportunity to move above the strike.

But time decay is not linear. Early in the life of an option, time decay is slow. The option loses a small amount of value each day. As expiration approaches, time decay accelerates. In the final week, the premium erodes quickly because there's little chance for large moves.

This is why selling options (collecting time decay) becomes more profitable near expiration, and why holding long options into expiration is often a bad trade — you're fighting accelerating time decay for diminishing upside.

**The Greeks capture this**: Theta (time decay) is negative for long calls and puts; it gets more negative (faster decay) as expiration nears.

**Intuition**: Time is optionality. The more time you have, the more chances for the stock to move in your favor. But that benefit compounds slowly early on and accelerates as expiration draws near.

## Volatility: the engine of option value

**Volatility** is the annualized standard deviation of the stock's percentage moves. It's the most misunderstood input.

Volatility does not tell you the direction the stock will move. It tells you how much it *might* move. A high-volatility stock could explode up or crash down with equal probability; the point is that large moves are likely.

For an option holder, large moves are good news. If you own a $50 call on a $50 stock (at-the-money), you make money if the stock rises. If volatility is high, the stock might jump to $65 or fall to $35 — large moves either way. If volatility is low, the stock might only move to $52 or $48 — small moves.

The call owner doesn't care which direction, because the call's downside is capped at the premium paid. If the stock falls to $35, the call is worthless, and you lose the premium. But you don't lose more. If it rises to $65, you gain $65 − $50 = $15, minus the premium you paid. The upside is asymmetric.

This asymmetry means **higher volatility raises the value of both calls and puts**. A call benefits from large upside moves and is protected on the downside. A put benefits from large downside moves and is protected on the upside.

Volatility is so important that traders talk about the "vol smile" or "vol surface." Different strikes and expirations have different implied volatilities, which embeds market expectations about how much risk exists.

**Intuition**: Volatility is the magnitude of surprise. High volatility means big moves are likely; big moves help option buyers. Sellers prefer low volatility.

## Interest Rate: the quiet input

The risk-free interest rate (usually the U.S. Treasury yield matching the option's tenor) has the smallest effect of the five inputs on most options.

The mechanism is discounting. An option's payoff is received at expiration, not today. If you have to wait 1 year to exercise a call and receive the profit, that profit is worth less in today's dollars than if you received it now. A higher interest rate (higher discount rate) makes that future payoff worth less today.

But the effect is small unless interest rates are very high or the time to expiration is very long. For a typical option on a stock, moving rates from 1% to 3% might change the premium by a few cents, barely visible.

The interest rate also affects the [time value](/time-value/) component. Technically, the Black-Scholes formula includes a drift term related to the interest rate, which slightly boosts call values and reduces put values. But again, the effect is modest for typical options.

**Where interest rate matters more**: in currency options, commodity options, or bond options, where the carry (storage cost or repo rate) is significant.

**Intuition**: Interest rate is the opportunity cost of capital. Higher rates mean waiting to receive a payoff is more costly, so options are worth slightly less (calls) or more (puts). The effect is usually negligible.

## Putting the five together: a worked example

Suppose you want to value a call option on a stock. The inputs are:

- S (Spot) = $100
- K (Strike) = $100
- T (Time) = 0.25 years (3 months)
- σ (Volatility) = 0.30 (30% annualized)
- r (Rate) = 0.05 (5% annual)

Using Black-Scholes, the call value comes out to roughly $2.70.

Now, suppose volatility spikes to 0.50 (50% annualized). Holding everything else the same, the call value rises to roughly $4.40. The option is more valuable because the stock is more likely to move significantly.

Suppose instead volatility stays at 0.30, but the spot price rises to $110. Now the call is $10 ITM with time value still available. The call value is roughly $12.50.

Finally, suppose spot is back at $100, vol is 0.30, but we shorten the time to expiration to 0.05 years (1 week instead of 3 months). The call value drops to roughly $0.90 because time decay has eroded the option significantly.

Each input moves the value, and they interact. A call that is OTM but has high volatility and long time to expiration can be valuable because the odds of ITM finishing are reasonable. A call that is ITM but is about to expire and volatility is very low is worth close to its intrinsic value — almost no time value.

## Why the model breaks down

Black-Scholes assumes a few things that are not always true in practice:

- **No dividends** (some stocks pay them, which reduces call value and increases put value)
- **European exercise only** (American options can be exercised early, which raises their value)
- **Constant volatility** (volatility is actually changing, and options of different strikes have different implied vols)
- **Lognormal distribution** (stock returns don't follow a perfect bell curve; they have fatter tails, meaning crashes are more likely than the model predicts)
- **No transaction costs or taxes** (real traders face both)

For these reasons, traders adjust Black-Scholes values or use more sophisticated models. But Black-Scholes is the starting point and the mental model that makes option pricing intuitive.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the contract type and basic mechanics
- [Call Option](/call-option/) — the right to buy
- [Put Option](/put-option/) — the right to sell
- [Strike Price](/strike-price/) — the exercise price (one of the five inputs)
- [Exercise Price](/exercise-price/) — another name for strike price
- [Time Value](/time-value/) — the premium above intrinsic value
- [Implied Volatility](/implied-volatility/) — market's forecast of future volatility
- [Option Premium](/option-premium/) — what the buyer pays for the option

### Wider context

- [Black-Scholes Model](/black-scholes-model/) — the full formula and assumptions
- [Derivatives Hedging](/derivatives-hedging/) — practical use of options to manage risk
- [Volatility Smile](/volatility-smile/) — why different strikes have different implied vols
- Greeks — delta, gamma, theta, vega, rho (sensitivity measures)

</div>

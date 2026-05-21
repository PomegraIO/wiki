---
title: "American Option"
description: "An American option can be exercised at any time up to and including its expiration date, giving the holder more flexibility and typically higher value than a European option."
keywords:
  - american option
  - early exercise
  - option pricing
  - flexible exercise
  - derivative
image: "/svg/derivatives.svg"
---

*An **American option** is a [call option](/call-option/) or [put option](/put-option/) that can be exercised at any time up to and including the [expiration date](/expiration-date/), not just on that final day. This flexibility makes American options more valuable than otherwise identical [european-option](/european-option/) options, particularly when early exercise can be advantageous. American options are the standard contract on individual [stock](/stock/) options in the United States.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">American Option — key facts</div>

<img src="/svg/derivatives.svg" alt="Multiple calendar dates showing flexible exercise timing" />

<div class="wiki-infobox-caption">American options offer the flexibility to exercise at any time before expiration.</div>

|   |   |
|---|---|
| **Exercise timing** | Anytime up to and including expiration |
| **Early exercise** | Permitted |
| **Pricing complexity** | Higher (continuous exercise decision) |
| **Typical underlying** | Individual stocks, some ETFs |
| **Price vs. European** | Higher premium (more flexibility) |
| **Assignment risk** | Can occur any trading day |
| **Valuation method** | Binomial tree, Monte Carlo simulation |
| **Settlement** | Physical delivery or cash |
| **Liquidity** | Very high on major stocks |

</aside>

## The early exercise advantage

The defining feature of an American option is the right to exercise at any moment, not just at expiration. This flexibility has real value. Suppose you own a [call option](/call-option/) on a [stock](/stock/) and a takeover bid is announced at a 40% premium. You can exercise immediately, pocket the shares, and enjoy the windfall. A European call holder must hold the option and wait for expiration, facing risk that the deal falls through in the interim.

Similarly, a [put option](/put-option/) holder benefits from early exercise when the underlying crashes. You can exercise the put, lock in profit by selling shares at the above-market [strike price](/strike-price/), and redeploy the cash into other investments. A European put holder cannot capture that advantage until expiration day arrives.

For [dividend](/dividend/)-paying stocks, American [call option](/call-option/) holders sometimes exercise just before the ex-[dividend](/dividend/) date to capture the upcoming [dividend](/dividend/), even if the option is not yet in-the-money by much. This is often rational if the [dividend](/dividend/) is large and the [call](/call-option/) has little [time value](/time-value/) left.

## Pricing American options

Valuing an American option is more complex than a [european-option](/european-option/) because the holder has a continuous decision to make: exercise now or wait? This cannot be solved with a closed-form equation like the [Black-Scholes model](/black-scholes-model/); instead, traders use numerical methods.

The [binomial-option-pricing](/binomial-option-pricing/) model is the workhorse. It builds a tree of all possible future stock prices at each time step from now to expiration, then works backward from expiration to today, calculating at each node whether it is optimal to exercise immediately or hold on. The result is a probability-weighted value reflecting the optimal exercise strategy.

[Monte-carlo-options-pricing](/monte-carlo-options-pricing/) is another approach, simulating thousands of possible price paths from today to expiration and calculating the payoff under the optimal early-exercise rule.

## When early exercise makes sense

For American [call option](/call-option/) on non-dividend-paying stocks, the theoretical answer is: never exercise early. It is always worth more to sell the option (capturing both [intrinsic value](/intrinsic-value/) and remaining [time value](/time-value/)) than to exercise and throw away the time value. But for [dividend](/dividend/)-paying stocks, early exercise can be optimal just before the stock goes ex-[dividend](/dividend/).

For American [put option](/put-option/), early exercise is much more common. A put that is deep in-the-money—say, a $100 strike and the [stock](/stock/) at $60—can be exercised immediately to lock in the $40 profit and redeploy capital. Waiting for expiration means accepting the risk that the stock bounces and sitting with capital tied up. This is why American puts trade at noticeably higher premiums than European puts.

## Assignment risk

Because American options can be exercised at any time, the seller faces assignment risk any trading day. If you sell a call that goes in-the-money and the [dividend](/dividend/) is approaching, the call buyer may exercise and force you to deliver shares. If you sell a put that plummets in-the-money, the buyer may exercise and force you to buy shares.

This unpredictability is one reason selling American options (writing naked calls or puts) requires close risk management and broker approval. The assignment can force you into an unexpected position at the worst moment.

## The [option](/option/) Greeks for American options

The [options-greeks](/options-greeks/) measure the same sensitivities as for [european-option](/european-option/) options—[delta](/delta/), [gamma](/gamma/), [theta](/theta/), [vega](/vega/), [rho](/rho/)—but the numbers reflect the early-exercise possibility. An American [put option](/put-option/) deep in-the-money may have lower [theta](/theta/) than a European put because there is less time value left to decay; the holder will likely exercise soon anyway.

[Gamma](/gamma/) (the convexity of [delta](/delta/) movement) tends to be higher for American options because the early-exercise boundary creates a kink in the value curve.

## Typical stock option contracts

A standard American option on a US stock option contract represents the right to buy or sell 100 shares. The [strike price](/strike-price/) typically comes in increments of $1 or $2.50, depending on the stock price. The [expiration date](/expiration-date/) is usually the third Friday of the month, though many stocks now also trade weekly and monthly expirations.

[Implied volatility](/implied-volatility/) on American options is high in periods of market stress and lower in calm markets. The [options Greeks](/options-greeks/) are continuously updated and quoted by brokers and market data vendors.

## See also

<div class="wiki-seealso">

### Closely related

- [European option](/european-option/) — exercise only at expiration
- [Bermudan option](/bermudan-option/) — exercise on specific dates
- [Call option](/call-option/) — right to buy
- [Put option](/put-option/) — right to sell
- [Expiration date](/expiration-date/) — the final exercise date
- [Strike price](/strike-price/) — the fixed exercise price
- Exercise and assignment — mechanics of exercising
- [Dividend](/dividend/) — triggers early exercise on calls

### Pricing & Greeks

- [Binomial option pricing](/binomial-option-pricing/) — standard valuation method
- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — alternative simulation approach
- [Options Greeks](/options-greeks/) — delta, gamma, theta, vega, rho
- [Implied volatility](/implied-volatility/) — market's bet on future movement

### Deeper context

- [Option](/option/) — the family of derivatives
- [Stock](/stock/) — the typical underlying asset
- [Stock exchange](/stock-exchange/) — where these options trade

</div>

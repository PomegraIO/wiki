---
title: "Put Option"
description: "A put option is a contract granting the holder the right, but not the obligation, to sell an underlying asset at a fixed price on or before a specific date."
keywords:
  - put option
  - derivative
  - option contract
  - downside protection
  - bearish strategy
image: "/svg/derivatives.svg"
---

*A **put option** is a contract granting the holder the right—but not the obligation—to sell an underlying [stock](/stock/) at a predetermined [strike price](/strike-price/) on or before an [expiration date](/expiration-date/). The buyer pays an [option premium](/option-premium/) upfront, betting that the asset's price will fall below the strike, making the right to sell at the higher fixed price valuable.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Put Option — key facts</div>

<img src="/svg/derivatives.svg" alt="A downward pointing arrow on a financial chart" />

<div class="wiki-infobox-caption">A put option grants the right to sell at a locked-in price.</div>

|   |   |
|---|---|
| **What it is** | Right to sell an asset at a fixed price |
| **Also called** | Put, long put |
| **Underlying assets** | Stocks, indices, futures, currencies, commodities |
| **Strike price** | Price at which the put can be exercised |
| **Premium** | Upfront cost paid by the buyer |
| **Expiration** | American, European, or Bermuda-style exercise |
| **Profit potential** | Limited to strike minus premium paid |
| **Maximum loss** | Limited to the premium paid |
| **Right is held by** | The put buyer (holder) |
| **Obligation falls on** | The put seller (writer) |

</aside>

## How a put option works

When you buy a put option, you own the right to sell the underlying asset at the strike price. If the [stock](/stock/) falls below your strike, you can exercise the put, forcing the seller to buy shares from you at the above-market strike price. Your profit is the strike price minus the current market price, less the premium you paid.

If the stock rises above the strike, the put expires worthless and you lose the premium. The maximum gain on a put is the strike price minus the premium paid (when the stock drops to zero, which almost never happens in practice).

The put seller, conversely, collects the premium upfront but faces the obligation to buy shares at the strike price if the option is exercised. If the stock crashes, the seller faces a loss—the difference between the strike and the lower market price. This is why put sellers demand premium proportional to the perceived downside risk.

A put's value consists of [intrinsic value](/intrinsic-value/) (how far it is already in-the-money) and [time value](/time-value/) (the market's price for the chance it will move further). Both decay as [expiration date](/expiration-date/) approaches.

## Why buyers use puts

The most common reason to buy a put is **downside protection**. You own shares of a [stock](/stock/) and worry it might fall, but you do not want to sell because you believe in the long-term story. A put acts as insurance: if the stock tumbles, the put compensates you for the loss, keeping your downside capped at the strike price.

Buying a [put option](/put-option/) is also a direct bearish bet. If you expect a stock to fall, you can buy a put—cheaper than short-selling and with defined, limited downside (the premium paid). Short sellers face theoretically unlimited losses if the stock rises; put buyers never lose more than the premium.

Puts are also used in portfolio insurance strategies, particularly at large institutions. Buy puts on an index after a strong rally to protect against a sudden [bear market](/bear-market/) without having to sell the entire portfolio.

## American vs. European puts

An [american-option](/american-option/) put can be exercised at any time up to expiration. A [european-option](/european-option/) put can be exercised only on the expiration date. American puts are worth more because early exercise is sometimes optimal—especially if the underlying falls sharply, the dividend goes ex-date, or you expect further decline.

In fact, early exercise of American puts is far more common than early exercise of American calls, because a put that is deep in-the-money can be exercised immediately to lock in profit and invest the proceeds.

## Puts in context: the Greeks

A put's [delta](/delta/) is negative, ranging from 0 (out-of-the-money) to -1.0 (deep in-the-money). An at-the-money put typically has a delta around -0.5, meaning a $1 drop in the stock increases the put's value by about $0.50. [Gamma](/gamma/) works the same way but measures how delta changes.

[Theta](/theta/), the decay of time value, works against put buyers just as it does call buyers—every day that passes with the stock flat costs the put holder money. [Vega](/vega/) tells you how much the put's value moves for each 1% change in [implied volatility](/implied-volatility/). Higher volatility means the put is more likely to end up in-the-money, so puts gain value when volatility rises.

## Pricing and payoff

At expiration, a put's value is simple:
- **If the stock is above the strike:** the put expires worthless; the buyer loses the premium.
- **If the stock is below the strike:** the put's value equals strike price minus stock price.

Before expiration, the put's price is strike price minus stock price (intrinsic value) plus time value. The [Black-Scholes model](/black-scholes-model/) and other pricing methods value puts by accounting for the likelihood they will finish in-the-money and how deep.

## Risks for put buyers and sellers

For the buyer, the risk is limited to the premium paid. You cannot lose more than 100% of what you spent on the put. The risk is that you overpay for insurance that never gets used, as the stock rises or stays flat and time value decays.

For the seller, the risk is the difference between the strike price and zero. If the underlying stock crashes, the seller may be forced to buy shares at an inflated strike price. Naked put selling is a leveraged bet that the stock will not fall hard—a position that requires careful risk management.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the mirror image; the right to buy
- [Option premium](/option-premium/) — the upfront cost of the put
- [Strike price](/strike-price/) — the locked-in selling price
- [Expiration date](/expiration-date/) — the deadline to exercise
- [Intrinsic value](/intrinsic-value/) — profit built in right now
- [Time value](/time-value/) — profit from future moves
- [American option](/american-option/) — can be exercised anytime
- [European option](/european-option/) — can be exercised only at expiration
- [Out-of-the-money](/out-of-the-money/) — stock above strike (unprofitable)

### Strategies & Greeks

- [Options Greeks](/options-greeks/) — delta, gamma, theta, vega, rho
- [Delta](/delta/) — how much the option moves with the stock
- Protective put — own stock, buy put for downside protection
- Bear put spread — sell put, buy lower put
- Straddle — long call plus long put at same strike

### Deeper context

- [Option](/option/) — the family of derivatives
- [Black-Scholes model](/black-scholes-model/) — pricing standard
- [Implied volatility](/implied-volatility/) — market's bet on future movement
- [Short selling](/short-selling/) — another way to bet on decline

</div>

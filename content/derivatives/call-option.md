---
title: "Call Option"
description: "A call option is a contract giving the holder the right, but not the obligation, to buy an underlying asset at a fixed price on or before a specific date."
keywords:
  - call option
  - derivative
  - option contract
  - strike price
  - bullish strategy
image: "/svg/derivatives.svg"
---

*A **call option** is a contract granting the holder the right—but not the obligation—to purchase an underlying [stock](/stock) (or other asset) at a predetermined [strike price](/strike-price) on or before an [expiration date](/expiration-date). The buyer pays an [option premium](/option-premium) upfront for that right, betting that the asset's price will rise above the strike price before expiration.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Call Option — key facts</div>

<img src="/svg/derivatives.svg" alt="A contract document with upward price arrow" />

<div class="wiki-infobox-caption">A call option grants the right to buy at a locked-in price.</div>

|   |   |
|---|---|
| **What it is** | Right to buy an asset at a fixed price |
| **Also called** | Call, long call |
| **Underlying assets** | Stocks, indices, futures, currencies, commodities |
| **Strike price** | Price at which the call can be exercised |
| **Premium** | Upfront cost paid by the buyer |
| **Expiration** | American, European, or Bermuda-style exercise |
| **Profit potential** | Unlimited above the strike |
| **Maximum loss** | Limited to the premium paid |
| **Right is held by** | The call buyer (holder) |
| **Obligation falls on** | The call seller (writer) |

</aside>

## How a call option works

When you buy a call option, you are purchasing the *privilege*—not the obligation—to exercise the contract. If the underlying [stock](/stock) rises above your strike price, you profit by exercising (buying at the lower strike and immediately reselling at the higher market price, or holding the shares). If it falls below the strike, you simply let the contract expire worthless, losing only the premium you paid.

The counterparty—the call seller or "writer"—collects your premium immediately but faces unlimited loss if the [stock](/stock) price soars. If you exercise the call, the seller must deliver the shares at the strike price, even if the market price is vastly higher. This is why call sellers demand premium to compensate for that risk.

The value of a call option breaks into two pieces: [intrinsic value](/intrinsic-value) (how far it is already in-the-money) and [time value](/time-value) (the market's bet that it will move further before expiration). As the [expiration date](/expiration-date) approaches, time value decays, typically accelerating in the final weeks.

## Why buyers use calls

A call option lets you control a large position with a small cash outlay. Buying 100 shares of a $100 stock requires $10,000; buying one call option on the same stock might cost $200–$500, depending on how far the [strike price](/strike-price) is from the current market price and how much time remains.

This leverage is double-edged. If you win, your return on the option premium can be spectacular—a $200 investment turning into $2,000 or more if the stock surges. If you lose, you lose the entire premium. But unlike buying shares on margin, that loss is finite and predictable.

Calls also let you express specific market views:
- **Bullish but cautious:** Buy a call when you think a stock will rise but want to limit your downside risk.
- **Long-term bullish:** Use calls to build a position cheaply, then exercise and hold for [dividend](/dividend) income.
- **Income generation:** Sell calls against shares you own—a covered call—to collect premium on stock you would be happy to sell at a higher price.

## American vs. European calls

An [american-option](/american-option) call can be exercised at any time up to expiration. A [european-option](/european-option) call can be exercised only on the expiration date itself. American calls are more valuable because of that extra flexibility, so they trade at a higher premium.

In practice, early exercise of an American call is rare if the underlying pays no [dividend](/dividend). You would typically sell the call instead of exercising, capturing both intrinsic and time value. But if the underlying pays a fat dividend and expiration is imminent, it may make sense to exercise early to capture the dividend.

## Calls in context: the Greeks

The price of a call option moves with the underlying asset's price, but not one-to-one. A stock's [delta](/delta) tells you how much the call price will move for each $1 move in the stock. At-the-money calls typically have a delta around 0.5, meaning a $1 stock move translates to about a $0.50 call move. Deep in-the-money calls have deltas closer to 1.0; out-of-the-money calls have deltas closer to 0.

[Gamma](/gamma) measures how delta itself changes. High gamma means small stock moves cause big shifts in how much the option price will move next. [Theta](/theta) measures the daily decay of time value—how much the call loses each day as expiration nears. [Vega](/vega) tells you how much the call's price moves for each 1% change in [implied volatility](/implied-volatility).

## Pricing and payoff

The call option payoff at expiration is simple:
- **If the stock is below the strike:** the option expires worthless; the holder loses the premium paid.
- **If the stock is above the strike:** the option's value equals stock price minus strike price.

Before expiration, the call is worth the sum of its intrinsic value plus time value. Time value decays daily, faster as expiration nears. The [Black-Scholes model](/black-scholes-model) is the standard formula for pricing calls, incorporating the underlying price, strike, time to expiration, interest rates, and [volatility](/historical-volatility).

## Risks for call buyers and sellers

For the buyer, the risk is straightforward: if the stock does not rise above the strike plus the premium paid, you lose money. The longer you wait, the more time value evaporates. Buying calls on a stock you expect to move big is a bet on both direction (up) and timing (soon).

For the seller, the risk is inverted. You keep the premium if the stock falls or stays flat, but you face mounting losses if it rises sharply. Selling calls against stock you own (covered call) limits that risk because you already own the asset; selling naked calls (without owning shares) is much riskier and may require special broker approval.

## See also

<div class="wiki-seealso">

### Closely related

- [Put option](/put-option/) — the mirror image; the right to sell
- [Option premium](/option-premium/) — the upfront cost of the call
- [Strike price](/strike-price/) — the locked-in purchase price
- [Expiration date](/expiration-date/) — the deadline to exercise
- [Intrinsic value](/intrinsic-value/) — profit built in right now
- [Time value](/time-value/) — profit from future moves
- [American option](/american-option/) — can be exercised anytime
- [European option](/european-option/) — can be exercised only at expiration
- [In-the-money](/in-the-money/) — stock above the strike

### Strategies & Greeks

- [Options Greeks](/options-greeks/) — delta, gamma, theta, vega, rho
- [Delta](/delta/) — how much the option moves with the stock
- Covered call — sell calls on stock you own
- Bull call spread — buy call, sell higher call
- Straddle — long call plus long put at same strike

### Deeper context

- [Option](/option/) — the family of derivatives
- [Black-Scholes model](/black-scholes-model/) — pricing standard
- [Implied volatility](/implied-volatility/) — market's bet on future movement
- [Stock](/stock/) — the typical underlying asset

</div>

---
title: "Option Premium"
description: "The option premium is the price paid by the buyer and received by the seller for the right (but not obligation) to exercise the option."
keywords:
  - option premium
  - option price
  - call price
  - put price
  - derivative pricing
image: "/svg/derivatives.svg"
---

*The **option premium** is the upfront price an option buyer pays the seller for the right to buy (in a [call option](/call-option/)) or sell (in a [put option](/put-option/)) the underlying asset. The premium is the total value of the option, comprising [intrinsic value](/intrinsic-value/) and [time value](/time-value/). Premiums are quoted in dollars per share (for stocks) or per contract unit, and they move continuously throughout the trading day based on supply, demand, and changes in the underlying asset.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Premium — key facts</div>

<img src="/svg/derivatives.svg" alt="Price quote for option contract" />

<div class="wiki-infobox-caption">The premium is the market-quoted option price.</div>

|   |   |
|---|---|
| **What it represents** | Buyer's cost; seller's income |
| **Paid at** | Initiation of the contract |
| **Quoted per** | Share (stocks) or contract unit |
| **Components** | Intrinsic value + time value |
| **Determinants** | Stock price, strike, time, volatility, rates |
| **Bid-ask spread** | Premium varies based on liquidity |
| **ITM premiums** | Higher due to intrinsic value |
| **OTM premiums** | Lower; only time value |
| **Pricing model** | Black-Scholes, binomial, Monte Carlo |
| **Settlement** | Typically T+0 (same day) in most US markets |

</aside>

## What the premium covers

When you buy a [call option](/call-option/), you pay the premium to acquire the right to buy the underlying [stock](/stock/) at the [strike price](/strike-price/). That premium is not refundable; if you change your mind, you must sell the option to someone else (if there is a buyer) to recover some value.

The premium includes two elements:

1. **Intrinsic value:** If the option is [in-the-money](/in-the-money/), the premium includes the immediate exercise profit. A [call option](/call-option/) struck at $100 on a $105 stock has at least $5 of intrinsic value, so the premium is at least $5.

2. **Time value:** This is the market's bet on future movement. That same call at $100 with the stock at $105 and 3 months to [expiration](/expiration-date/) might trade at $7 ($5 intrinsic + $2 time value), because the market thinks the stock could move further.

## How premiums are quoted

Premiums are expressed in dollars per share for stock options. A [call option](/call-option/) with a premium of $2.50 costs $2.50 per share, or $250 per contract (since each contract represents 100 shares).

Index and some currency options are quoted differently—e.g., $10 per index point rather than per share. Always confirm the unit before trading.

Premiums are continuously updated during trading hours, reflecting bids (what buyers will pay) and asks (what sellers demand). The actual transaction price is somewhere between these two, depending on supply and demand pressure.

## Risk of premium loss

The buyer's maximum loss is the premium paid. If you buy a [call option](/call-option/) for $2 and the stock falls sharply, the option might expire worthless, and you lose the entire $2 premium. This bounded risk is one reason options are attractive to retail traders—you cannot lose more than you paid.

For the seller, the maximum profit is the premium received. If you sell a $2 [call option](/call-option/) and the stock falls to zero, you keep the $2 premium and profit the full amount (ignoring commissions). But if the stock soars, you face losses exceeding the premium.

## Premium determinants

The [Black-Scholes model](/black-scholes-model/) shows that option premiums depend on:

1. **Stock price:** Higher stock prices increase call premiums and decrease put premiums.
2. **Strike price:** Lower strikes increase call premiums; higher strikes increase put premiums.
3. **Time to expiration:** Longer durations increase both call and put premiums (more time for moves).
4. **Volatility:** Higher [volatility](/historical-volatility/) increases both call and put premiums (more probability of large moves).
5. **Interest rates:** Higher rates slightly increase call premiums and decrease put premiums.
6. **Dividends:** Upcoming [dividend](/dividend/)s decrease call premiums and increase put premiums (the buyer loses the dividend).

## Bid-ask spreads and pricing

The premium a buyer actually pays is usually higher than the quote you see; you pay the ask price (seller's asking price). Similarly, when selling, you receive the bid price (buyer's offered price), which is lower. The difference is the bid-ask spread—the market maker's profit.

In liquid markets (e.g., S&P 500 options), spreads are tight (a few cents). In illiquid options, spreads can be wide (dollars or more), eating into your returns.

## Early sale and premium recovery

If you buy an option for $2 premium and sell it before expiration when it is worth $3, you pocket a $1 profit. You have captured some of the [time value](/time-value/) before it decays to zero. This is the standard practice for option buyers rather than holding to expiration and watching [time decay](/theta/) erode the premium.

## Extrinsic vs. intrinsic in pricing

The premium is sometimes decomposed as:
- **Intrinsic value** (the guaranteed minimum): What you would receive if you exercised immediately.
- **Extrinsic value** (= time value): The speculative premium you pay for future upside or downside potential.

Only the intrinsic value is forced by arbitrage to be in the option price; the extrinsic value is what the market thinks future moves are worth.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — premium is the cost to buy the call
- [Put option](/put-option/) — premium is the cost to buy the put
- [Intrinsic value](/intrinsic-value/) — component of premium
- [Time value](/time-value/) — component of premium
- [Strike price](/strike-price/) — affects premium level
- [Expiration date](/expiration-date/) — affects premium duration

### Valuation models

- [Black-Scholes model](/black-scholes-model/) — standard premium formula
- [Implied volatility](/implied-volatility/) — key input to premium pricing
- [Historical volatility](/historical-volatility/) — realized moves vs. premium expectations
- [Binomial option pricing](/binomial-option-pricing/) — alternative premium model
- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — simulation approach

### Greeks

- [Delta](/delta/) — sensitivity of premium to stock price
- [Vega](/vega/) — sensitivity of premium to volatility
- [Theta](/theta/) — daily decay of premium
- [Gamma](/gamma/) — convexity of premium
- [Rho](/rho/) — sensitivity to interest rates

### Deeper context

- [Option](/option/) — the family of derivatives
- [Bid-ask spread](/call-option/) — component of trading cost
- [Arbitrage](/alpha/) — exploiting premium mispricings

</div>

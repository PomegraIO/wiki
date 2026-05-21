---
title: "In-the-Money"
description: "In-the-money describes an option that has positive intrinsic value because the underlying asset's price makes exercise immediately profitable."
keywords:
  - in-the-money
  - itm
  - option value
  - intrinsic value
  - moneyness
image: "https://picsum.photos/seed/in-the-money/900/600"
---

*An option is **in-the-money (ITM)** when exercising it would immediately be profitable. For a [call option](/call-option), this means the [stock](/stock) price is above the [strike price](/strike-price). For a [put option](/put-option), this means the stock price is below the strike. In-the-money options have positive [intrinsic value](/intrinsic-value) and are worth more than otherwise-identical out-of-the-money options, all else equal.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">In-the-Money — key facts</div>

<img src="https://picsum.photos/seed/in-the-money/900/600" alt="A stock price line above a strike level" />

<div class="wiki-infobox-caption">In-the-money options have positive intrinsic value.</div>

|   |   |
|---|---|
| **Call ITM condition** | Stock price > strike price |
| **Put ITM condition** | Stock price < strike price |
| **Intrinsic value** | Positive; call = stock - strike; put = strike - stock |
| **Time value** | May be positive or zero |
| **Total value** | Intrinsic + time value |
| **Automatic exercise** | Often at expiration if ITM |
| **Probability of profit** | Generally higher than OTM options |
| **Delta** | For ITM calls, typically 0.5 to 1.0 |
| **Moneyness measure** | How far ITM (e.g., 5% ITM, 20% ITM) |

</aside>

## ITM for calls and puts

A [call option](/call-option) is in-the-money if the underlying [stock](/stock) price exceeds the [strike price](/strike-price). A $100 strike call is in-the-money if the stock is trading at $105, $110, $150, or any price above $100.

A [put option](/put-option) is in-the-money if the underlying stock price is below the strike. A $100 strike put is in-the-money if the stock is at $95, $80, $50, or any price below $100.

The logic is straightforward: a call holder wants to buy at the strike price, so the call is profitable if the market price is higher. A put holder wants to sell at the strike price, so the put is profitable if the market price is lower.

## Intrinsic value

The amount by which an option is in-the-money is its [intrinsic value](/intrinsic-value). If a call is struck at $100 and the stock is at $107, the intrinsic value is $7. If a put is struck at $100 and the stock is at $92, the intrinsic value is $8.

This [intrinsic value](/intrinsic-value) is the minimum value an option can have. A call deep in-the-money is worth at least its intrinsic value, plus any remaining [time value](/time-value). But even if [time value](/time-value) is zero (on the expiration date itself), the in-the-money option is worth at least its intrinsic value.

## ITM options vs. OTM options

An in-the-money option is always worth more than an otherwise-identical out-of-the-money option, because it has [intrinsic value](/intrinsic-value). A $100 strike call is worth more when the stock is at $110 (ITM, intrinsic value $10) than when the stock is at $90 (out-of-the-money, intrinsic value $0).

This premium for ITM-ness is reflected in the [delta](/delta). An ITM call might have a delta of 0.7 or 0.8, meaning it moves 70–80 cents for each $1 move in the stock. An OTM call might have a delta of 0.2 or 0.3. The in-the-money option is more sensitive to stock price moves.

## Moneyness: how far ITM?

Traders measure how far in-the-money an option is using "moneyness"—the ratio of the stock price to the strike. A moneyness of 1.05 means the stock is 5% above the strike (for a call). A moneyness of 0.95 means the stock is 5% below the strike (for a put).

Deep ITM options (e.g., 20% or 30% ITM) behave almost like the underlying stock itself; their [delta](/delta) is near 1.0. Slightly ITM options (e.g., 1–2% ITM) are less certain to remain ITM and are more sensitive to [volatility](/historical-volatility).

## Assignment and automatic exercise

If you own an in-the-money [american-option](/american-option) at or near expiration, your broker will typically exercise it automatically. An ITM call is converted to long stock; an ITM put is converted to short stock. You must have the capital available (for calls) or the shares available (for puts).

For [european-option](/european-option) options, exercise happens only on the expiration date, not before.

If you sell (are short) an ITM option, your counterparty will almost certainly exercise, forcing you to deliver shares (for short calls) or accept delivery of shares (for short puts). This is why managing short options requires vigilance near expiration.

## ITM and time decay

An in-the-money option still loses [time value](/time-value) as expiration approaches, though the decay is slower than for at-the-money options. A call struck at $100 with the stock at $120 loses [time value](/time-value) as expiration nears, but it is protected by $20 of intrinsic value that cannot decay.

The [time value](/time-value) decay ([theta](/theta)) is slower for deep ITM options because they are less likely to move out-of-the-money, and the payoff is nearly certain.

## Profit and breakeven

Owning an in-the-money option is profitable, but profit and loss depend on your entry price (the premium you paid). If you bought a call at $2 and the call is now ITM by $7 (stock at $107, strike at $100), the call is worth at least $7. But your profit is only $5 ($7 intrinsic value minus the $2 premium paid).

Your breakeven on a call is strike price plus premium paid. A $100 strike call bought at $3 premium breaks even at $103. If the stock is at $105 at expiration, you profit $2 per share ($105 – $100 – $3).

## See also

<div class="wiki-seealso">

### Closely related

- [Out-of-the-money](/out-of-the-money/) — opposite; stock below call strike or above put strike
- [At-the-money](/at-the-money/) — stock exactly at strike
- [Call option](/call-option/) — ITM when stock > strike
- [Put option](/put-option/) — ITM when stock < strike
- [Strike price](/strike-price/) — the reference level
- [Intrinsic value](/intrinsic-value/) — the ITM amount

### Greeks and valuation

- [Delta](/delta/) — higher for ITM options
- [Theta](/theta/) — time decay slower for deep ITM
- [Vega](/vega/) — less sensitive for ITM options
- [Black-Scholes model](/black-scholes-model/) — prices ITM options
- [Implied volatility](/implied-volatility/) — varies by ITM vs. OTM

### Management

- [Time value](/time-value/) — still present even for ITM options
- Exercise and assignment — likely for ITM options
- [Early exercise](/american-option/) — often makes sense for ITM American options
- Roll — extending ITM options to later expirations

### Deeper context

- [Option](/option/) — the family of derivatives
- [Moneyness](/in-the-money/) — technical measure of ITM degree

</div>

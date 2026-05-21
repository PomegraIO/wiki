---
title: "Strike Price"
description: "The strike price is the fixed price at which the holder of an option can buy (call) or sell (put) the underlying asset, set when the option contract is issued."
keywords:
  - strike price
  - exercise price
  - option contract
  - derivative pricing
image: "/svg/derivatives.svg"
---

*The **strike price** (also **exercise price**) is the fixed price at which a [call option](/call-option) holder has the right to buy or a [put option](/put-option) holder has the right to sell the underlying asset. The strike is set when the option is issued and does not change during the option's life. It is one of the two key determinants of an option's value and profitability, along with the underlying asset's current price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Strike Price — key facts</div>

<img src="/svg/derivatives.svg" alt="A fixed price level on a trading chart" />

<div class="wiki-infobox-caption">The strike price is the fixed purchase/sale price for an option.</div>

|   |   |
|---|---|
| **Fixed by** | At contract initiation |
| **Call holder uses** | To buy at the strike |
| **Put holder uses** | To sell at the strike |
| **Call payoff** | max(stock price - strike, 0) at expiration |
| **Put payoff** | max(strike - stock price, 0) at expiration |
| **Relative to spot** | Above, at, or below current price |
| **In-the-money call** | Current price > strike |
| **In-the-money put** | Current price < strike |
| **Increments** | Often $1, $2.50, or $5 depending on stock |
| **Determines** | Intrinsic value and time value |

</aside>

## The role of strike in option value

The strike price is the pivot point for all option economics. For a [call option](/call-option), the further the [stock](/stock) price is above the strike, the more [intrinsic value](/intrinsic-value) the call has. For a [put option](/put-option), the further the stock price is below the strike, the more intrinsic value the put has.

If you own a call struck at $100 and the stock is at $110, the call has $10 of intrinsic value. If the stock falls to $95, the intrinsic value is $0—the call has no value related to the current stock price, though it still has [time value](/time-value) until [expiration date](/expiration-date).

The strike is the level where the option "tips" from worthless to valuable (or vice versa). For a call, every dollar above the strike is profit; every dollar below the strike is loss (of the premium paid). For a put, every dollar below the strike is profit; every dollar above the strike is loss.

## Strike selection and cost

Higher strike prices on calls are cheaper because they are further out-of-the-money and less likely to finish profitably. A $110 call on a $100 stock costs less than a $100 call, which costs less than a $90 call.

Conversely, lower strike prices on puts are cheaper because they are further out-of-the-money. A $80 put on a $100 stock costs less than a $90 put, which costs less than a $100 put.

This creates a trade-off for investors. A cheap $120 call on a $100 stock has limited payoff potential (you profit only if the stock rises above $120). An expensive $100 call has lower breakeven (stock only needs to rise above $100 + call premium). The strike selection encodes your conviction in the move size.

## In-the-money, at-the-money, out-of-the-money

An option's position relative to the strike is described in three states:

- **In-the-money (ITM):** A call is ITM if the spot price exceeds the strike. A put is ITM if the spot price is below the strike. The option has [intrinsic value](/intrinsic-value).
- **At-the-money (ATM):** The spot price equals the strike. The option has no intrinsic value, only [time value](/time-value).
- **Out-of-the-money (OTM):** A call is OTM if the spot price is below the strike. A put is OTM if the spot price is above the strike. The option is worthless at expiration if the stock does not move.

## Strike spacing and available strikes

For a [stock](/stock) trading above $250, strikes typically come in $2.50 or $5 increments (e.g., $250, $252.50, $255, $257.50). For stocks below $250, strikes usually come in $1 increments ($100, $101, $102). For very cheap stocks, strikes might be $0.50 apart.

This spacing allows traders to fine-tune the [strike price](/strike-price) to their view while keeping the options exchange manageable. Too many strikes create illiquidity; too few make hedging imprecise.

## Strike and the Greeks

The [delta](/delta) of an option—how much the option price moves for each $1 move in the stock—depends heavily on the [strike](/strike-price) relative to the spot. A deep-in-the-money call has a delta near 1.0 (moves almost dollar-for-dollar with the stock). An at-the-money call has a delta around 0.5. A deep out-of-the-money call has a delta near 0.

[Gamma](/gamma) (how delta changes) is highest at-the-money and falls toward zero far from the strike. [Theta](/theta) (time decay) is typically negative for long option positions and concentrated around at-the-money strikes. [Vega](/vega) (sensitivity to [volatility](/historical-volatility)) is highest at-the-money.

## Strike, [volatility smile](/volatility-smile), and [implied volatility](/implied-volatility)

The [implied volatility](/implied-volatility) of an option depends not just on the underlying stock's [historical volatility](/historical-volatility) but also on the strike relative to the spot. Out-of-the-money put strikes typically have higher implied volatility than at-the-money strikes, reflecting the market's fear of crashes. This creates the [volatility smile](/volatility-smile) or [volatility skew](/volatility-smile)—different strikes have different implied volatility levels.

A trader using the [Black-Scholes model](/black-scholes-model) or other pricing models must account for the strike's effect on implied volatility, not just its mathematical effect on [intrinsic value](/intrinsic-value).

## Strikes in bonds, swaps, and other derivatives

The strike concept extends beyond stock options. A [interest-rate-swap](/interest-rate-swap) swaption has a strike rate (the fixed leg rate you have the right to lock in). A [currency swap](/swap) option has a strike exchange rate. The principle is the same: the strike is the level at which the option becomes profitable.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — uses strike to lock in purchase price
- [Put option](/put-option/) — uses strike to lock in sale price
- [Expiration date](/expiration-date/) — the other key contract parameter
- [In-the-money](/in-the-money/) — strike below spot (call) or above spot (put)
- [Out-of-the-money](/out-of-the-money/) — strike above spot (call) or below spot (put)
- [At-the-money](/at-the-money/) — strike equals spot

### Valuation impact

- [Intrinsic value](/intrinsic-value/) — determined by strike vs. spot
- [Time value](/time-value/) — depends on strike position
- [Implied volatility](/implied-volatility/) — varies by strike
- [Volatility smile](/volatility-smile/) — skew in IV across strikes
- [Black-Scholes model](/black-scholes-model/) — takes strike as input

### Greeks

- [Delta](/delta/) — sensitive to strike proximity
- [Gamma](/gamma/) — highest at-the-money
- [Theta](/theta/) — concentrated at-the-money
- [Vega](/vega/) — highest at-the-money

### Deeper context

- [Option](/option/) — the family of derivatives
- Exercise and assignment — uses strike to settle
- [Option premium](/option-premium/) — set in market; depends on strike

</div>

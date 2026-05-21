---
title: "At-the-Money"
description: "At-the-money describes an option whose strike price equals the underlying asset's current price, making it the most sensitive to volatility and direction."
keywords:
  - at-the-money
  - atm
  - option value
  - strike price
  - volatility sensitivity
image: "/svg/derivatives.svg"
---

*An option is **at-the-money (ATM)** when the [strike price](/strike-price/) equals (or is very close to) the underlying [stock](/stock/)'s current market price. An at-the-money option has zero [intrinsic value](/intrinsic-value/) and is worth entirely its [time value](/time-value/). ATM options are the most sensitive to changes in [volatility](/historical-volatility/) and have the highest [gamma](/gamma/) (convexity), making them useful barometers of market uncertainty.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">At-the-Money — key facts</div>

<img src="/svg/derivatives.svg" alt="Stock price exactly aligned with strike level" />

<div class="wiki-infobox-caption">ATM options have zero intrinsic value.</div>

|   |   |
|---|---|
| **Definition** | Stock price ≈ strike price |
| **Intrinsic value** | Exactly zero |
| **Time value** | All of the option's value |
| **Delta** | Approximately 0.5 (for ATM calls; -0.5 for ATM puts) |
| **Gamma** | Maximum; highest sensitivity to stock moves |
| **Theta** | Significant daily decay (negative for long) |
| **Vega** | Maximum; most sensitive to volatility |
| **Probability of profit** | 50% (approximately) |
| **Volatility impact** | Outsized compared to ITM or OTM |
| **Price characteristic** | Pure time value; decays predictably |

</aside>

## The zero intrinsic value point

An at-the-money option sits exactly at the boundary between [in-the-money](/in-the-money/) and [out-of-the-money](/out-of-the-money/). For a [call option](/call-option/), ATM means the stock is at the strike. For a [put option](/put-option/), ATM also means the stock equals the strike.

Since neither the call holder (who wants to buy at the strike) nor the put holder (who wants to sell at the strike) is immediately profitable, the option has no [intrinsic value](/intrinsic-value/). Every dollar of an ATM option's price is [time value](/time-value/)—the market's bet that the option will move into-the-money before expiration.

## Maximum sensitivity to volatility

ATM options are the most sensitive to changes in [implied volatility](/implied-volatility/). All of the option's value depends on the probability of moving [in-the-money](/in-the-money/) before expiration, and that probability is directly proportional to the market's estimate of future volatility.

If [volatility](/historical-volatility/) rises from 20% to 30%, an ATM option can gain 30–50% in value without any move in the stock. If [volatility](/historical-volatility/) falls, the ATM option loses value rapidly.

Conversely, deep [in-the-money](/in-the-money/) or [out-of-the-money](/out-of-the-money/) options are less sensitive to volatility changes because their value is anchored by intrinsic value (for ITM) or so low that volatility changes matter less (for deep OTM).

This is why ATM options are the benchmark for implied volatility quotes. When traders quote the "volatility of the SPX" or the "VIX," they are typically referring to the implied volatility of ATM options.

## The Greeks at ATM

**Delta:** An ATM [call option](/call-option/) has a [delta](/delta/) of approximately 0.5, meaning a $1 move in the stock translates to about $0.50 movement in the option. An ATM [put option](/put-option/) has a [delta](/delta/) of approximately –0.5. This 50–50 split reflects the 50–50 probability of the stock moving up or down from the strike.

**Gamma:** ATM options have the highest [gamma](/gamma/) among all strikes. [Gamma](/gamma/) measures how [delta](/delta/) changes; at-the-money is the inflection point where [delta](/delta/) is most sensitive to stock price moves. A small stock move causes larger [delta](/delta/) changes at ATM than at other strikes.

**Vega:** ATM options have maximum [vega](/vega/) (sensitivity to [volatility](/historical-volatility/) changes). A 1% increase in implied volatility increases an ATM option's price more than it increases the price of an [in-the-money](/in-the-money/) or [out-of-the-money](/out-of-the-money/) option.

**Theta:** ATM options have significant daily decay. The [time value](/time-value/) erodes at a predictable, accelerating rate as expiration nears. For option buyers, this is a headwind; for option sellers, a tailwind.

## Price behavior

An ATM option's price is dominated by [time value](/time-value/), which can be approximated by the [Black-Scholes model](/black-scholes-model/). The formula shows that an ATM option's value is approximately proportional to volatility × √(time). This simple relationship makes ATM options useful for inferring market volatility expectations.

As expiration approaches, the [time value](/time-value/) decays. With 90 days to expiration, an ATM option might be worth 50% of the move needed to reach the strike by the half-time mark. With 1 day to expiration, it might be worth only 1–2% of the same move.

## Use cases and advantages

ATM options are ideal for traders expressing a pure directional view. An ATM call offers the most balanced leverage: you need the stock to move only 1–2% (roughly) to break even by expiration, and the [delta](/delta/) of 0.5 means you share 50% of the stock's upside.

ATM options are also ideal for straddle and strangle strategies, where you buy both a call and a put to bet on volatility. An ATM straddle is the simplest form: you profit if the stock moves sharply in either direction.

Institutions use ATM implied volatility as a reference point for pricing all other derivatives and hedging. The ATM IV becomes the baseline from which they adjust for [volatility smile](/volatility-smile/) and other market effects.

## Distinction from slightly ITM/OTM

Traders sometimes distinguish between ATM and nearby strikes:
- **Near-the-money:** Slightly ITM or slightly OTM (within 1–2% of the strike).
- **Deep ATM:** The stock is within $0.01 of the strike.

For practical purposes, strikes within 1% of the stock price are treated as ATM for pricing purposes.

## See also

<div class="wiki-seealso">

### Closely related

- [In-the-money](/in-the-money/) — above strike (calls) or below strike (puts)
- [Out-of-the-money](/out-of-the-money/) — below strike (calls) or above strike (puts)
- [Strike price](/strike-price/) — equals current stock price for ATM
- [Intrinsic value](/intrinsic-value/) — zero for ATM
- [Time value](/time-value/) — all ATM option value

### Greeks and volatility

- [Delta](/delta/) — ~0.5 for ATM
- [Gamma](/gamma/) — maximum at ATM
- [Theta](/theta/) — significant ATM decay
- [Vega](/vega/) — maximum at ATM
- [Implied volatility](/implied-volatility/) — benchmarked at ATM
- [Volatility smile](/volatility-smile/) — skew relative to ATM

### Strategies

- Straddle — buy ATM call and put
- Strangle — buy OTM call and put
- Butterfly spread — buy ATM, sell wings

### Deeper context

- [Option](/option/) — the family of derivatives
- [Black-Scholes model](/black-scholes-model/) — simplest for ATM pricing
- VIX — implied volatility of ATM S&P 500 options

</div>

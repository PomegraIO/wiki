---
title: "Vega"
description: "Vega measures how much an option's price changes for each 1% change in implied volatility, quantifying sensitivity to market uncertainty."
keywords:
  - vega
  - option greeks
  - volatility sensitivity
  - implied volatility
  - option pricing
image: "/svg/derivatives.svg"
---

*The **vega** of an option is the amount by which its price changes for each 1% increase or decrease in [implied volatility](/implied-volatility/). A vega of 0.2 means a 1% rise in implied volatility increases the option's value by $0.20. Both [call option](/call-option/)s and [put option](/put-option/)s have positive vega; higher [volatility](/historical-volatility/) makes both more valuable because there is greater probability of [in-the-money](/in-the-money/) finish. Vega is highest for [at-the-money](/at-the-money/) options and nearly zero for deep [in-the-money](/in-the-money/) or [out-of-the-money](/out-of-the-money/) options.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vega — key facts</div>

<img src="/svg/derivatives.svg" alt="Volatility chart showing option price sensitivity" />

<div class="wiki-infobox-caption">Vega measures volatility sensitivity.</div>

|   |   |
|---|---|
| **Sign** | Always positive (for long calls and puts) |
| **Range** | Higher for ATM; lower for deep ITM/OTM |
| **Calls** | Positive vega (higher IV = higher call value) |
| **Puts** | Positive vega (higher IV = higher put value) |
| **Short options** | Negative vega (IV rise hurts you) |
| **Interpretation** | Option value change per 1% IV move |
| **Highest at** | At-the-money options |
| **Lowest at** | Deep in/out-of-the-money |
| **Time to expiration** | Longer-dated options have higher vega |
| **Volatility regime change** | Major impact on portfolio value |

</aside>

## How vega works

If you own a [call option](/call-option/) with a vega of 0.3, and [implied volatility](/implied-volatility/) rises from 20% to 21% (a 1% increase), the call's value rises by about $0.30, all else equal.

Vega is always positive for owned options (long calls and puts). Higher [volatility](/historical-volatility/) is good for option buyers because it increases the probability and potential magnitude of [in-the-money](/in-the-money/) finish. Conversely, vega is negative for short options (sold calls and puts). A volatility spike hurts you as a seller.

Both calls and puts have positive vega because both benefit from uncertainty. A call profits if the stock rises sharply; a put profits if it falls sharply. Either way, higher [volatility](/historical-volatility/) increases the odds of a large move that helps the option.

## Vega across moneyness

**At-the-money options** have the highest vega. Their entire value is [time value](/time-value/), which is driven by [volatility](/historical-volatility/). A 1% volatility change can swing an [at-the-money](/at-the-money/) option 10–20% in value.

**In-the-money and out-of-the-money options** have lower vega in dollars but often have higher vega as a percentage of the option's price. An out-of-the-money option worth $0.20 might have a vega of $0.03; a 1% volatility rise is a 15% gain.

**Deep in-the-money options** have low vega; they behave almost like the stock itself (delta ≈ 1.0), and [volatility](/historical-volatility/) changes matter little.

## Vega and time to expiration

Longer-dated options have higher vega. A 6-month call has more vega than a 1-month call on the same stock, because [volatility](/historical-volatility/) has more time to move the underlying and affect the option's payoff.

As [expiration date](/expiration-date/) nears, vega declines. On the final day, vega is near zero; the option's value is nearly deterministic (based on whether it is in or out of the money).

## Implied volatility and vega connection

[Implied volatility](/implied-volatility/) is the market's forecast of future [volatility](/historical-volatility/). It is not directly observable but inferred from option prices using the [Black-Scholes model](/black-scholes-model/) or similar formulas. The relationship runs both ways:

- Higher [implied volatility](/implied-volatility/) → higher option prices → higher vega.
- A volatility spike instantly raises [implied volatility](/implied-volatility/) across all strikes, inflating all option prices.

A trader long vega is betting that [implied volatility](/implied-volatility/) will rise. If it does, the option gains value independent of stock price movement. A trader short vega is betting [implied volatility](/implied-volatility/) will fall, eroding option values.

## Vega trading

Some traders specialize in pure volatility plays, independent of direction. They:
- Buy straddles or strangles (long calls and puts) to bet [volatility](/historical-volatility/) rises.
- Sell straddles/strangles to bet [volatility](/historical-volatility/) falls.

These positions have net-zero [delta](/delta/) (direction-neutral) but large vega exposure.

## Vega and [volatility smile](/volatility-smile/)

Different strikes have different [implied volatility](/implied-volatility/) levels, creating the [volatility smile](/volatility-smile/) or [volatility skew](/volatility-smile/). Out-of-the-money puts typically have higher [implied volatility](/implied-volatility/) (higher vega) than at-the-money options, reflecting crash fears. A volatility skew position (long high-vega OTM puts, short ATM vega) can profit from shifts in this skew.

## Portfolio vega

Like [delta](/delta/), vega can be summed across a portfolio. If your portfolio has +1000 vega (net long volatility), a 1% volatility spike gains you $1000. A volatility crash loses you $1000.

This is why funds carefully track portfolio vega exposure and often hedge it using variance swaps, VIX options, or other [volatility](/historical-volatility/) derivatives.

## See also

<div class="wiki-seealso">

### Closely related

- [Options Greeks](/options-greeks/) — vega is one of the five
- [Implied volatility](/implied-volatility/) — what vega measures sensitivity to
- [Historical volatility](/historical-volatility/) — realized vs. expected moves
- [Call option](/call-option/) — positive vega when long
- [Put option](/put-option/) — positive vega when long
- [At-the-money](/at-the-money/) — maximum vega

### Strategies

- Straddle — pure vega play (long volatility)
- Strangle — long volatility, cheaper than straddle
- Calendar spread — vega gains offset by theta losses
- Iron condor — short vega

### Valuation

- [Black-Scholes model](/black-scholes-model/) — computes vega
- [Volatility smile](/volatility-smile/) — varying vega across strikes
- [Volatility skew](/volatility-smile/) — skew in vega by moneyness
- VIX — index of implied volatility

### Deeper context

- [Option](/option/) — the family of derivatives
- [Volatility trading](/volatility-smile/) — using vega to bet on volatility
- [Risk management](/hedge-fund/) — managing vega exposure

</div>

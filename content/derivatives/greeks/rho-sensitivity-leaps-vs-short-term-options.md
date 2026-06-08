---
title: "Rho Sensitivity in LEAPS vs Short-Term Options"
description: "Why rho—interest-rate sensitivity—is negligible for weekly and monthly options but can be a meaningful P&L driver for multi-year LEAPS when interest rates shift."
keywords:
  - rho sensitivity LEAPS short-term options
  - interest rate options Greeks
  - long-term options interest rates
  - option rho delta
  - LEAPS Greeks
image: "/svg/derivatives.svg"
---

*Rho measures how much an option's price changes when interest rates move. For weekly options, rho is essentially zero. For multi-year options (LEAPS), rho can shift the price by 1–5% per 100-basis-point rate move—a meaningful P&L contributor when the Fed is hiking or cutting.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rho Sensitivity — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and Greeks." />

<div class="wiki-infobox-caption">Rho matters for long-duration options; short-term traders can ignore it.</div>

|   |   |
|---|---|
| **Rho definition** | Change in option price per 1% change in risk-free interest rate |
| **Typical range (ATM call, 1-year to expiration)** | +0.10 to +0.30 per 1% rate move |
| **Typical range (ATM call, 10-year LEAPS)** | +0.50 to +2.50 per 1% rate move |
| **Effect on puts** | Negative rho (puts lose value as rates rise) |
| **Comparable to…** | [Duration](/duration/) in bonds; longer tenors have higher rho |
| **When to hedge** | Multi-year options in a rising-rate environment |

</aside>

## Why Rho Exists: The Time-Value-of-Money Argument

Rho exists because option pricing depends on the [discount-rate](/discount-rate/). When you use the [Black-Scholes-model](/black-scholes-model/) or other pricing frameworks, you discount expected future payoffs to the present. The discount rate is the **risk-free rate**—typically the yield on U.S. Treasury bills or notes corresponding to the option's maturity.

A call option holder has the right to buy the stock in the future. Holding cash to exercise that call is an opportunity cost—the cash could earn the risk-free rate instead. When rates rise, the opportunity cost rises, making the call more valuable (you are giving up more interest by exercising later). When rates fall, the call becomes less valuable.

Conversely, a put option holder has the right to sell. Rising rates make future cash flows less attractive, so the put's value declines. This is why calls have positive rho and puts have negative rho.

## The Math: Rho in Black-Scholes

In the [Black-Scholes-model](/black-scholes-model/), rho for a call option is:

**Rho = K × e^(−r×T) × N(d2) × T**

Where:

- **K** = strike price
- **r** = risk-free rate
- **T** = time to expiration (in years)
- **e** = Euler's number
- **N(d2)** = standard normal CDF of d2

The key term is **T** (time to expiration). The longer the expiration, the larger rho. A 1-week option has T ≈ 0.02 years; a 3-year LEAPS has T ≈ 3. This multiplicative effect makes rho grow dramatically with maturity.

In practical terms:

| Expiration | ATM Call Rho |
|---|---|
| 1 week | ~0.01 |
| 1 month | ~0.05 |
| 3 months | ~0.15 |
| 1 year | ~0.25 |
| 3 years (LEAPS) | ~0.80 |
| 10 years | ~2.50 |

A trader holding a 1-year 10% out-of-the-money (OTM) call might see rho closer to 0.05–0.10. A LEAPS holder on the same underlying might see rho of 0.30–0.80.

## The Practical Impact: A Worked Example

Suppose you buy a 3-year LEAPS call on a stock trading at $100, strike $100, with implied volatility at 25% and interest rates at 5%.

- Call price: ~$15.50
- Rho: ~0.80

If the Fed hikes rates 100 basis points (to 6%) overnight:

- New call price: ~$15.50 + (0.80 × 1.0) = **~$16.30**
- Gain from rho alone: ~$0.80, or ~5% of the option price

That is significant. For a weekly option with rho of 0.01, the same 100-basis-point move would add only $0.01 to its price—noise.

Now suppose you hold 100 contracts (10,000 calls):

- 1-week option: +$100 P&L from rho (negligible)
- 3-year LEAPS: +$8,000 P&L from rho (substantial)

For a directional trader betting on the stock's movement, the LEAPS trade is now carrying an unexpected interest-rate bet. If rates fall instead, the LEAPS loses $0.80 per contract, or $8,000 on the position—a headwind on top of any stock price move.

## Rho vs. Other Greeks for Short-Term Options

For weeklies and monthlies, **[delta](/delta/)** (stock price sensitivity) and **theta** (time decay) dominate P&L.

- Delta for an ATM weekly call: ~0.50 (moves about $0.50 for every $1 stock move)
- Theta for an ATM weekly call: ~−0.02 to −0.05 per day (loses value from decay)
- Rho for an ATM weekly call: ~0.01 (negligible)

If the stock moves $2, delta contributes $1.00 of P&L. Time decay costs $0.14–$0.35 per day. A 100-basis-point rate move contributes $0.01. The rate move is invisible.

## Rho vs. Other Greeks for Long-Term Options

For 3-year and longer options, rho climbs and becomes competitive with [vega](/vega/) (implied volatility sensitivity):

- Delta for an ATM 3-year call: ~0.60 (still the dominant Greek)
- Theta for an ATM 3-year call: ~−0.01 per day (much slower decay than weekly)
- Vega for an ATM 3-year call: ~0.25 per 1% IV move
- Rho for an ATM 3-year call: ~0.80 per 1% rate move

A 50-basis-point rate move contributes $0.40 of P&L. A 1 percentage-point IV drop costs $0.25. A 5% stock move contributes $3.00 (delta). All three Greeks are material.

This is why LEAPS traders must monitor not just the stock but also interest rates and the [implied-volatility](/implied-volatility/) surface.

## In-the-Money vs. Out-of-the-Money

Out-of-the-money (OTM) options have lower rho than at-the-money (ATM) options because OTM options are more sensitive to volatility (vega) than to time value (interest rates). In-the-money (ITM) calls have higher rho than ATM calls, because ITM calls are effectively longer-duration borrowings (the holder is financing the stock position over time).

A deep ITM call with a 3-year expiration might have rho of 1.20 or higher. A far OTM call with the same expiration might have rho of 0.30. The difference is economically meaningful for large positions.

## Hedging Rho Risk in LEAPS Portfolios

A sophisticated trader holding a large long LEAPS call position in a rising-rate environment can hedge rho by:

1. **Selling shorter-dated calls** against the LEAPS (a call spread that reduces overall rho exposure).
2. **Selling Treasury futures** to hedge the rate sensitivity (if rates are expected to rise, short rate futures to offset losses).
3. **Using interest-rate swaps** to lock in the current rate and neutralize future rate moves (though this is more common in institutional portfolios).

Retail traders typically do not hedge rho explicitly; they accept the interest-rate sensitivity as part of the long equity exposure. But institutional options desks managing multi-billion-dollar books will dynamically hedge rho, especially when the Fed is in a cutting or hiking cycle.

## The Fed Cycle and LEAPS Trading

LEAPS trading is often correlated with Fed policy expectations. When the Fed is expected to cut rates, long LEAPS calls become more attractive because rho headwinds are expected to reverse—rates falling will amplify call values. Conversely, in a hiking cycle, LEAPS sellers have an advantage because rising rates will pressure call prices independent of stock performance.

This dynamic adds a macroeconomic layer to LEAPS trading that short-term option traders typically ignore.

## When Rho is Negligible vs. Material

| Option Maturity | Rho Magnitude | Trading Relevance |
|---|---|---|
| 1–2 weeks | 0.001–0.005 | Ignore |
| 1 month | 0.01–0.05 | Minimal; focus on delta and theta |
| 3–6 months | 0.05–0.15 | Monitor if holding large positions; small P&L impact |
| 1 year | 0.15–0.35 | Material; budget rho as 10–20% of P&L variability |
| 2+ years (LEAPS) | 0.40–2.50+ | Major; rho can be 30–50% of volatility-driven P&L |

## Key Takeaway

Rho is a second-order effect for traders focused on weeks and months. It is a first-order effect for anyone building and holding multi-year positions. When analyzing LEAPS P&L, always report rho alongside delta and vega. When the Fed is in motion, rho can be the surprise driver of position losses or gains.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — sensitivity to stock price moves (dominant Greek for short-term options)
- Theta-time-decay-theta — daily time decay (dominant for weeklies and monthlies)
- [Vega](/vega/) — sensitivity to implied volatility changes (material for all expirations)
- [Gamma](/gamma/) — sensitivity of delta to stock moves (higher in short-term options)
- [Black-scholes-model](/black-scholes-model/) — underlying pricing model from which rho derives

### Wider context

- [Option](/option/) — foundational mechanics of call and put options
- [Interest-rate](/interest-rate/) — the underlying rate that rho measures sensitivity to
- [Implied-volatility](/implied-volatility/) — IV surface shifts that compete with rho for P&L
- [Duration](/duration/) — related concept of interest-rate sensitivity in fixed income

</div>

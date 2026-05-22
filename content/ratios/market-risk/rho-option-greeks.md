---
title: "Rho (Option Greeks)"
description: "Sensitivity of option price to changes in interest rates, the least-used Greek in practical trading."
keywords:
  - option greeks
  - interest rate sensitivity
  - option pricing
  - derivatives
---

*A **rho** measures how much an [option](/option/) price changes in response to a 1% change in [interest rates](/interest-rate/), a minor risk factor for most traders but important for long-dated options and fixed-income derivatives.*

<div class="wiki-hatnote">
For the full option Greeks suite, see [Options Greeks](/options-greeks/). For interest-rate sensitivity in bonds, see [Bond Duration Risk](/bond-duration-risk/).
</div>

<aside class="wiki-infobox">

| Item | Value |
|---|---|
| **Definition** | Change in option value per 1% interest-rate move |
| **Units** | Currency (e.g., $0.05 per option) |
| **Typical range** | 0.01 to 0.50 depending on time and moneyness |
| **Importance** | Low for short-dated; material for multi-year options |
| **Call option sign** | Positive rho |
| **Put option sign** | Negative rho |
| **Forgotten Greek** | Rarely hedged; often ignored |

</aside>

## Why interest rates affect option prices

Option values depend on [discount rates](/discount-rate/). When valuing the payoff from an option at expiration using a model like [Black-Scholes](/black-scholes-model/), future cash flows are discounted to present value at the risk-free rate (typically, the short-term treasury yield). Higher interest rates reduce the present value of future payoffs, lowering option value.

A [call option](/call-option/) on a stock has positive rho: if rates rise, the option value falls, and vice versa. A [put option](/put-option/) has negative rho: if rates rise, the option value rises, because the discount rate on the option payoff is higher, but the opportunity cost of holding the put (rather than the underlying stock) also increases, partially offsetting the effect.

## Call vs. put rho

**Call option.** Higher rates reduce option value because the call holder gives up the risk-free rate by investing in the option instead of a bond. A 1% rate increase might reduce a 1-year call's value by $0.03–0.10, depending on moneyness. The effect is larger for out-of-the-money calls (which depend more on future discounting) and smaller for deep in-the-money calls (which behave like the stock).

**Put option.** Higher rates increase put value slightly. A 1% rate increase might increase a 1-year put's value by $0.02–0.05. However, the effect is typically weaker and less stable than for calls.

## Rho and option maturity

Rho scales with time to expiration. A 1-month option has near-zero rho (interest rates barely matter over 30 days). A 10-year option has substantial rho (interest rates matter significantly over a decade). This is why rho is relevant in:

- **Long-dated equity options.** LEAPS (options with years to expiration) can have rho of 0.20 or higher.
- **Dividend-protection options.** Long-dated protective puts used in wealth-management strategies are sensitive to rates.
- **Exotic options.** Lookback, barrier, and American-style options with multi-year horizons can have material rho.

## Why rho is overlooked

In practical trading, rho is the least-watched Greek. Here is why:

**Market-driven hedges dominate.** For a stock trader holding 1,000 shares and buying a 1-month put, the put's value depends almost entirely on stock volatility and the stock's price ([gamma](/gamma-option-greeks/), [delta](/delta-option-greeks/), and [vega](/vega-option-greeks/)). Rho of 0.005 per option is economically irrelevant—100 basis points of rate movement moves the option by $0.05, or $50 for 1,000 options.

**Rates are relatively stable during short-holding windows.** A trader holding an option for days or weeks expects rates to stay roughly constant. [Volatility](/implied-volatility/) changes daily; rates change quarterly at most. In a holding period of 30 days, a 1% rate move is unusual.

**Other Greeks matter more for returns.** [Theta](/theta-option-greeks/) (time decay), [gamma](/gamma-option-greeks/) (convexity), and [vega](/vega-option-greeks/) (volatility) typically dominate option P&L.

## When rho matters

Rho becomes material in a few scenarios:

**Multi-year options.** A 5-year call on a stock can have rho of 0.15–0.25. In a scenario where the Federal Reserve cuts rates 200 basis points, a 5-year call rises in value by $300–500 per contract, purely from the rho effect. For large portfolios, this is material.

**Interest-rate expectations.** A trader who believes rates will rise can benefit from owning puts (positive rho effect) rather than calls. This is a subtle but real alpha source if rates do move unexpectedly.

**Fixed-income derivatives.** In bond options, swaptions, and cap/floor derivatives, rho is critical—in fact, it becomes the primary risk factor, renamed as "vega" (sensitivity to interest-rate [volatility](/volatility-swap/)) or "duration" (sensitivity to parallel rate shifts). A swaption's value moves primarily with rates, not equity-like dynamics.

**Currency options.** Interest-rate [parity](/interest-rate-parity/) means rho is material in FX options. A higher US rate makes the dollar call more valuable and the dollar put less valuable, all else equal.

## Rho in Black-Scholes

The Black-Scholes formula for rho of a European call option is:

**Rho (Call) = K × T × e^(−rT) × N(d2)**

Where:
- K = strike price
- T = time to expiration
- r = risk-free rate
- N(d2) = cumulative normal distribution of d2 term

For a put, rho has opposite sign and magnitude is typically smaller. This formula shows that rho increases with strike price and time to expiration, consistent with intuition.

## Practical hedging of rho

Traders rarely hedge rho explicitly because the cost of doing so (buying or selling a bond or interest-rate swap to offset rho) is usually not justified by the small exposure. However, in large portfolios of long-dated options or when interest-rate changes are expected, hedging rho can be worthwhile.

One simple hedge: if you are long calls (positive rho), you can short a bond or enter a receive-fixed interest-rate swap. If you are long puts (negative rho), you can go long a bond. These hedges are crude but capture the rho exposure.

<div class="wiki-seealso">

### Closely related
- [Options Greeks](/options-greeks/) — The full suite of risk metrics
- [Delta](/delta-option-greeks/) — Directional sensitivity
- [Gamma](/gamma-option-greeks/) — Delta sensitivity (convexity)
- [Vega](/vega-option-greeks/) — Volatility sensitivity
- [Theta](/theta-option-greeks/) — Time decay

### Wider context
- [Option Pricing](/option/) — How options are valued
- [Black-Scholes Model](/black-scholes-model/) — The underlying model
- [Interest Rate Risk](/interest-rate-risk/) — The broader factor
- [Derivatives](/derivative-accounting-hedging/) — Risk-management framework
- Fixed Income — Interest-rate sensitive assets

</div>

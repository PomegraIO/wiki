---
title: "Rho Sensitivity"
description: "The rate of change in an option's price relative to shifts in interest rates, measured as the derivative of option value with respect to the risk-free rate."
keywords:
  - option greeks
  - interest rate sensitivity
  - pricing models
  - rho coefficient
  - bond option valuation
  - carry cost
---

*[Options](/wiki/option/) are sensitive to five main sources of market movement: the underlying price, time decay, volatility, dividends, and—less obviously—interest rates. **Rho sensitivity** (usually called rho, represented as ρ) measures how much an option's price changes when [interest rates](/wiki/interest-rate/) shift by one percentage point. It is the most often-ignored of the option [Greeks](/wiki/options-greeks/), yet it matters significantly in certain contexts.*

<div class="wiki-hatnote">Rho is one of five primary Greeks. The others are [Delta](/wiki/delta-option-greeks/), [Gamma](/wiki/gamma-option-greeks/), [Vega](/wiki/vega-option-greeks/), and [Theta](/wiki/theta-option-greeks/).</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Symbol** | ρ (rho) |
| **Measured in** | Price change per 1% rise in rates |
| **Typical range** | $2–$30 per 1% rate move for equity options |
| **Call rho** | Positive: calls gain value when rates rise |
| **Put rho** | Negative: puts lose value when rates rise |
| **Magnitude** | Generally small vs. delta or vega for near-term options |
| **Volatility relationship** | Higher implied vol slightly increases rho magnitude |

</aside>

## Why interest rates affect option prices

Interest rates enter option pricing through two mechanisms.

**The cost of carry.** If you buy an option on a stock, you are not buying the stock itself—you can hold capital in a risk-free bond earning the [risk-free rate](/wiki/interest-rate/) until expiration, then exercise. The effective cost of deferring capital deployment is the interest rate you sacrifice. When rates are high, deferring is expensive; when rates are low, it is cheap. Calls benefit from high rates (you can put capital to work immediately upon exercise), while puts benefit from low rates (you can wait, keeping capital in bonds).

**The present value of the strike price.** For a [put](/wiki/put-option/), the strike price is cash you will receive upon exercise. When interest rates are high, the present value of that future cash falls; when rates are low, it rises. Conversely, for a [call](/wiki/call-option/), the strike is an obligation to pay. When rates are high, the present value of that obligation falls (you'll pay cheaper dollars later).

## Call rho: positive sensitivity

A call option's rho is **positive**. When interest rates rise:
- The call becomes more valuable. A 1% rate increase might increase a call price by \$5 (or 5 cents for small moves).
- The intuition: you gain the option to lock in today's stock price later, and in a higher-rate environment, deferred capital is more valuable.

For an at-the-money 3-month equity call, rho is typically small—maybe \$1–\$3 per 1% rate move. For a 5-year call (much longer time to expiration), rho can be \$10–\$30 per 1% rate move, because you are deferring capital for a much longer period.

## Put rho: negative sensitivity

A put option's rho is **negative**. When interest rates rise:
- The put loses value. A 1% rate increase might decrease a put price by \$5.
- The intuition: the present value of the strike price you'll receive falls as discount rates rise, making the put less attractive.

This is especially pronounced for in-the-money puts. A 5-year, in-the-money put might have a rho of -\$20, meaning a 1% rise in rates shrinks its value by \$20 per share (or \$2,000 per 100-share contract).

## When does rho matter in practice?

For short-dated options (weeks, a few months), rho is negligible compared to [delta](/wiki/delta-option-greeks/) or [vega](/wiki/vega-option-greeks/). The price sensitivity to interest rate swings is tiny—often under 1% of the option's total value.

Rho becomes material in three cases:

1. **Long-dated options (years).** A 5-year swaption or an employee stock option with multi-year maturity can have meaningful rho. A 0.5% rate move (modest by historical standards) can shift the value by 2–5%.

2. **Interest rate options themselves.** Options on [bonds](/wiki/bond/), [interest rate swaps](/wiki/interest-rate-swap/), or [treasuries](/wiki/treasury-bond/) have enormous rho, sometimes exceeding delta in magnitude. A bond call option's value is almost entirely driven by interest rates; the underlying asset *is* interest-sensitive.

3. **Volatility regimes.** When implied interest rate volatility is very high (as it was in 2022 when the Fed was raising aggressively), rho spikes because the probability distribution of future rates is more dispersed.

## Rho in the Black-Scholes model

The [Black-Scholes option pricing model](/wiki/black-scholes-model/) includes an explicit rho term. For a call:

ρ_call ≈ K × T × e^(-rT) × N(d2)

Where K is strike, T is time to expiration, r is the risk-free rate, and N(d2) is the probability that the option expires in the money.

For a put:

ρ_put = -K × T × e^(-rT) × N(-d2)

These formulas show that rho scales with time to expiration, strike price, and the moneyness of the option. Longer-dated, higher-strike options have larger rho magnitudes.

## Managing rho in a portfolio

Institutional options traders typically do not hedge rho actively on equity options because the sensitivity is too small. A portfolio of 100 short-dated equity calls has rho close to zero in absolute terms.

However, traders in fixed-income options, bond futures, and [swaptions](/wiki/swaption/) do monitor rho carefully. A hedge fund running a large [interest rate swap](/wiki/interest-rate-swap/) portfolio will hedge rho by offsetting with [interest rate futures](/wiki/interest-rate-option/) or additional swaps, because a 0.5% rate move can swing millions of dollars in value.

## Rho and empirical pricing

In practice, traders rely on implied volatility surfaces and historical rate dynamics more than on the rho coefficient itself. When computing what an option should be worth, traders consider the current rate, expected rate paths (from the yield curve), and interest rate volatility. Rho emerges as an output of that analysis, not as a separate input.

If the [Federal Reserve](/wiki/federal-reserve/) signals rate hikes, options markets reprrice immediately—both because market participants update their expectations and because rho becomes larger (volatility of rates increases, and longer-dated options become rho-sensitive).

## Rho vs. duration in bonds

Bonds have "duration"—their price sensitivity to interest rates. A 10-year bond with a 5-year duration falls \$5 in price for every 1% rate rise. This is analogous to rho, but it is not the same. Duration is the weighted average time to cash flows; rho is the specific sensitivity of an embedded option within a derivative.

A callable bond's rho (the rho of the embedded [call](/wiki/call-option/)) is negative: the [call](/wiki/callable-bond/) is worth more when rates fall, which hurts the bondholder. That negative rho reduces the bond's effective duration, which is why callable bonds underperform in a falling-rate environment.

<div class="wiki-seealso">

### Closely related
- [Option Greeks](/wiki/options-greeks/) — The five main sensitivities
- [Delta](/wiki/delta-option-greeks/) — Price sensitivity to the underlying asset
- [Vega](/wiki/vega-option-greeks/) — Price sensitivity to volatility
- [Theta](/wiki/theta-option-greeks/) — Price sensitivity to time decay

### Wider context
- [Black-Scholes Model](/wiki/black-scholes-model/) — Foundation of modern option pricing
- [Interest Rate](/wiki/interest-rate/) — The parameter rho measures sensitivity to
- [Interest Rate Swap](/wiki/interest-rate-swap/) — Fixed-income derivative where rho dominates
- [Swaption](/wiki/swaption/) — Option on an interest rate swap with high rho
- [Yield Curve](/wiki/yield-curve/) — Determines expected future rates and rho magnitude

</div>
---
title: "Implied Volatility"
description: "Implied volatility is the volatility level that makes the Black-Scholes model output equal to the market price of an option, representing the market's expectation of future price movement."
keywords:
  - implied volatility
  - iv
  - option pricing
  - volatility forecast
  - market expectation
image: "https://picsum.photos/seed/implied-volatility/900/600"
---

*The **implied volatility (IV)** of an option is the [volatility](/historical-volatility) level that, when plugged into the [Black-Scholes model](/black-scholes-model) or other pricing formula, produces the option's current market price. IV is not directly observable; it is derived by inverting the pricing formula. High IV means the market expects large price moves; low IV means the market expects calm. IV is the market's consensus forecast of [volatility](/historical-volatility) over the option's remaining life.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Implied Volatility — key facts</div>

<img src="https://picsum.photos/seed/implied-volatility/900/600" alt="Option market prices reflecting future volatility expectations" />

<div class="wiki-infobox-caption">Implied volatility encodes the market's volatility forecast.</div>

|   |   |
|---|---|
| **Derivation** | Inverse of Black-Scholes pricing formula |
| **Unit** | Annualized percentage (e.g., 20% per annum) |
| **Varies by** | Strike, expiration, underlying asset |
| **Computation** | Numerical methods (Newton-Raphson typically) |
| **Market consensus** | Aggregate belief about future movement |
| **Compared to** | Historical volatility for trading signals |
| **High IV** | Expensive options; market expects big moves |
| **Low IV** | Cheap options; market expects calm |
| **Volatility smile** | IV varies across strikes (not flat) |
| **Volatility term structure** | IV varies across expirations |

</aside>

## How implied volatility is derived

The [Black-Scholes model](/black-scholes-model) price a call: C = f(S, K, T, r, σ)

The formula takes volatility σ as an input and outputs the fair call price C. When traders observe a market price in the exchange, they ask: what σ would make Black-Scholes produce this market price?

That σ is the **implied volatility**. There is no closed-form inverse; traders use numerical methods (Newton-Raphson iteration) to solve for IV.

## IV as market expectation

Implied volatility is the market's collective forecast. If a stock has 30-day implied volatility of 25%, the market is saying: "We expect this stock to move around 25% annualized over the next 30 days." If IV is 50%, the market expects higher turbulence.

This is forward-looking, not backward-looking. [Historical volatility](/historical-volatility) measures realized moves over the past (e.g., 60 days). IV measures expected moves over the future. High IV does not mean the stock moved a lot; it means the market thinks it will.

## IV across strikes: the volatility smile

In the real market, options at different [strike price](/strike-price)s have different implied volatilities. An [at-the-money](/at-the-money) call struck at $100 on a $100 stock might have IV of 20%. An [out-of-the-money](/out-of-the-money) put at $90 might have IV of 25%.

This variation across strikes is the [volatility smile](/volatility-smile) (U-shaped curve) or [volatility skew](/volatility-smile) (lopsided curve). It reflects the market's fear of crashes (higher IV on OTM puts) and other [skew](/volatility-smile) effects.

## IV across expirations: the term structure

IV also varies across [expiration date](/expiration-date)s. Near-term options might have IV of 18%; one-year options might have 25%. This "volatility term structure" changes based on expected near-term events and long-term uncertainty.

## Trading with implied volatility

**IV rank and IV percentile:** Traders compare current IV to historical IV levels. If IV is at the 90th percentile (highest in the past year), options are expensive; good time to sell. If IV is at the 10th percentile, options are cheap; good time to buy.

**Mean reversion:** IV tends to revert to long-term averages. Spikes in IV (panic selling, earnings surprises) are often temporary. Traders sell high IV and buy low IV, betting on reversion.

**Volatility dispersion:** Some traders buy options on individual stocks and sell index options (or vice versa), profiting if the correlation between individual stock and index volatility changes.

## Vega and IV changes

The Greek [vega](/vega) measures sensitivity to IV changes. A long call with vega of +0.2 gains $0.20 if IV rises 1%. This makes vega directly relevant: if you believe IV is too low, you buy options (collect long vega) and profit when IV rises.

## IV in exotics and path-dependent options

For [exotic option](/binary-option)s (Asian, barrier, etc.), [implied volatility](/implied-volatility) is less directly used than for [european-option](/european-option)s, but the concept remains: IV embedded in exotic prices reflects market expectations of volatility over the option's path.

## See also

<div class="wiki-seealso">

### Closely related

- [Historical volatility](/historical-volatility/) — realized vs. expected
- [Volatility smile](/volatility-smile/) — IV varies by strike
- [Volatility skew](/volatility-smile/) — asymmetric IV across strikes
- [Black-Scholes model](/black-scholes-model/) — IV inverts this formula
- [Option premium](/option-premium/) — IV drives option value

### Greeks and trading

- [Vega](/vega/) — sensitivity to IV changes
- [Delta](/delta/) — changes with IV levels
- [Theta](/theta/) — IV affects time decay profile

### Market concepts

- VIX — index of S&P 500 implied volatility
- [Volatility trading](/volatility-smile/) — exploiting IV changes
- [Mean reversion](/stock-market/) — IV reverts to long-term average
- [Volatility arbitrage](/alpha/) — comparing IV to realized volatility

### Deeper context

- [Option](/option/) — the instrument being priced
- [Call option](/call-option/) — has implied volatility
- [Put option](/put-option/) — has implied volatility
- [Derivatives pricing](/black-scholes-model/) — foundation of pricing

</div>

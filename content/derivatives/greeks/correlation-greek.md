---
title: "Correlation Greek"
description: "The sensitivity of a multi-asset derivative's value to changes in the correlation between its underlying assets."
keywords:
  - correlation sensitivity
  - multi-asset derivatives
  - basket option
  - correlation greek rho
  - correlation risk
image: "/svg/derivatives.svg"
---

*A **correlation greek** is the rate at which a multi-asset derivative changes value when the correlation between its underlying assets shifts. For [basket option](/basket-option/)s, [spread](/spread/) trades, and other instruments whose payoff depends on the joint behaviour of multiple assets, correlation greek quantifies a real and often hidden source of risk that vanilla-option Greeks cannot capture.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Correlation Greek — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract mark representing derivatives and multi-asset structures." />

<div class="wiki-infobox-caption">The option greeks expanded for linked assets.</div>

|   |   |
|---|---|
| **What it is** | Sensitivity of multi-asset derivative value to changes in correlation between underlyings |
| **Also called** | Correlation rho, correlation exposure, co-movement greek |
| **Applies to** | Basket options, spread options, rainbow options, [convertible bond](/convertible-bond/)s with multiple reference assets |
| **Key insight** | Correlation is often priced implicitly and can move independently of individual [volatility](/historical-volatility/) |
| **Trading impact** | Same assets, same individual prices, different correlation = very different [option](/option/) value |
| **Hedging challenge** | No single traded instrument directly hedges correlation risk |

</aside>

## Why correlation matters for multi-asset options

When a derivative depends on only one asset—say, a vanilla [call](/call-option/) on a stock—the standard Greeks ([delta](/delta/), [gamma](/gamma/), [vega](/vega/)) tell the full story of how value moves. But when a derivative depends on two or more assets, a new risk dimension emerges: the correlation between them.

Consider a simple [basket option](/basket-option/) that pays off based on the average of two stocks. If both stocks move together (high correlation), the payoff is relatively stable and predictable. If they move in opposite directions (low or negative correlation), the basket value is dampened—diversification lowers the volatility of the average. A [call](/call-option/) on this basket is worth *less* when correlation is high (the underlying is more volatile) and *worth more* when correlation is low (the underlying is more stable, reducing tail risk).

This relationship—that higher correlation often means higher value for spread or basket strategies—is the heart of correlation greek. It is the amount by which the derivative value moves when correlation shifts by one percentage point or changes by one standard deviation.

## The pricing dependency

To see the concrete effect, imagine a [spread option](/spread-option/) on the difference between two commodities: crude oil and natural gas. The payoff is max(Oil − Gas − Strike, 0). The spread (Oil − Gas) is what matters, and its volatility depends on both the individual volatilities of oil and gas *and* how tightly they move together.

If oil and gas prices are highly correlated (both driven by global energy demand), the spread is relatively stable—low variance in the difference. If they are uncorrelated, the spread is more volatile. A buyer of a spread option prefers *low* correlation (less spread volatility means lower [option premium](/option-premium/) for the same [strike](/strike-price/)). A seller of a spread option wants *high* correlation (higher variance to capture larger premiums).

Thus, a rise in correlation makes the spread wider in range, raising the value of a short spread position and lowering the value of a long spread position. Correlation greek quantifies exactly this sensitivity.

## Types of correlation exposure

**Two-asset correlation greek** is the simplest case: how does the derivative value change when the correlation between two specific assets moves? This applies to spread options, [convertible bond](/convertible-bond/)s (which depend on stock–bond correlation), and [currency option](/currency-option/)s on cross rates.

**Multi-dimensional correlation greek** arises in basket [option](/option/)s with three or more components. A [basket option](/basket-option/) on five stocks has a correlation matrix of 5×5 unique correlations. The basket's value is sensitive to shifts in *any* of these pairwise correlations. Traders must think in terms of correlation exposure across the entire matrix, not just one number.

**Term structure of correlation** is another subtlety. Short-dated correlations can differ dramatically from long-dated correlations. A three-month [option](/option/) on two assets may price in a correlation of 0.6, while a two-year [option](/option/) on the same assets may assume a correlation of 0.3. Correlation greek for the three-month [option](/option/) is different from that of the two-year [option](/option/).

## How traders calculate it

In practice, there are several approaches:

1. **Numerical bumping**: Shock the correlation matrix by a small amount (e.g., increase one pairwise correlation by 1%) and reprice the derivative using a Monte Carlo or binomial tree. The difference divided by the shock size is the correlation greek. This is the gold standard for complex [option](/option/)s.

2. **Analytical formula**: For simple structures like two-asset [spread option](/spread-option/)s, closed-form formulas exist (extensions of [Black-Scholes](/black-scholes-model/)) that express correlation greek directly. These are fast and precise.

3. **Implied correlation extraction**: Market prices of [basket option](/basket-option/)s and [spread option](/spread-option/)s reveal what the market is assuming about correlation. Traders extract this "implied correlation" and monitor it as they would [implied volatility](/implied-volatility/). Changes in implied correlation feed directly into correlation greek.

## The hedging problem

Here is the challenge: unlike [delta](/delta/) (hedged by buying or selling the underlying) or [vega](/vega/) (hedged by trading [volatility](/historical-volatility/) swaps or other [option](/option/)s), there is no simple instrument to directly hedge correlation risk.

A trader exposed to correlation greek must use indirect hedges:

- **Trade individual [option](/option/)s** on the constituent assets to change the overall correlation sensitivity of the portfolio.
- **Dynamically rebalance** the basket or spread as correlations shift, effectively buying or selling individual components to rebalance the co-movement risk.
- **Trade [variance swap](/variance-swap/)s or [volatility](/historical-volatility/) [swap](/swap/)s** on each underlying, which indirectly adjusts correlation exposure (because [variance](/variance-swap/) and correlation are linked through the portfolio volatility formula).

This opacity is why correlation greek is often neglected or mispriced in dealer books. Unlike [delta](/delta/) or [gamma](/gamma/), which have clear market mechanisms for hedging, correlation greek lives in the shadows—visible to pricing models but hard to eliminate without restructuring the entire position.

## Correlation greek in the crisis

Correlation risk explodes during market stress. In normal times, correlations are stable and traders may assume they are fixed. But in a crash or liquidity crisis, all risky assets tend to move together—correlations spike toward one. A portfolio that was hedged assuming moderate correlations suddenly finds itself overexposed as correlation rises.

This is why risk managers track correlation greek not just as a delta-adjusted greek, but as a stress scenario. They ask: "If correlation jumps to 0.9, how much do we lose?" and ensure the answer is within risk limits.

## Where it shows up in practice

- **[Basket option](/basket-option/)s** on multiple equities or commodities
- **[Convertible bond](/convertible-bond/)s** whose value depends on both stock and interest-rate correlation
- **Cross-currency [swap](/swap/)s** and foreign-exchange [option](/option/)s that depend on currency pair correlations
- **Commodity [spread option](/spread-option/)s** (e.g., crack spreads in energy, crush spreads in agriculture)
- **Equity [basket](/basket-option/) [ETF](/etf/)s** and index products where component correlation matters

For traders and risk managers in these spaces, correlation greek is not a theoretical curiosity—it is a live, material source of exposure that must be monitored and managed just like [delta](/delta/) or [gamma](/gamma/).

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the foundational greek; correlation greek extends it to multi-asset space
- [Vega](/vega/) — sensitivity to [volatility](/historical-volatility/); often confused with or bundled with correlation greek
- [Basket option](/basket-option/) — the prototype structure where correlation greek applies
- [Spread option](/spread-option/) — another multi-asset derivative with significant correlation exposure
- [Implied volatility](/implied-volatility/) — its multi-asset cousin is implied correlation
- [Option](/option/) — the underlying derivative class

### Wider context

- Greeks — the full family of derivative risk sensitivities
- Multi-asset derivative — the broader category of [option](/option/)s and [swap](/swap/)s with linked underlyings
- [Volatility](/historical-volatility/) — often moves together with correlation in crisis scenarios
- Risk management — the practice that must account for correlation greek

</div>

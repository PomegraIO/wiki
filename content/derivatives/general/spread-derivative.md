---
title: "Spread Derivative"
description: "A contract that pays off based on the difference between two underlying prices or rates, enabling hedging or speculation on relative movements."
keywords:
  - spread trading
  - price difference derivatives
  - relative value exposure
  - hedging instrument
---

*A **spread derivative** is a contract whose payoff depends on the difference (or spread) between two underlying prices, rates, or indices, rather than the absolute level of any single one. A trader buys exposure to the spread itself—betting that the gap between two assets will widen or tighten.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Payoff structure** | Function of (Price A − Price B) |
| **Common examples** | Credit spreads, commodity spreads, basis swaps |
| **Use cases** | Hedging relative risk, arbitrage, speculation on convergence |
| **Hedging benefit** | Isolates spread risk, removing dependence on absolute levels |
| **Typical users** | Traders, funds, corporates, banks |

</aside>

## Core concept: the spread as an asset

A traditional [option](/wiki/option/) or [forward](/wiki/forward-contract/) derives value from the absolute price of the underlying. A spread derivative derives value from the *difference* between two underlyings. If crude oil trades at $85/bbl and heating oil at $2.40/gal, a spread derivative might pay based on the ratio or dollar gap between them.

This matters because many traders and hedgers care about the relationship between two prices rather than the prices themselves. A petroleum refiner is long crude oil (it buys as input) and short heating oil (it sells as output). The refinery's profit margin depends on the spread—the "crack spread"—not on absolute oil prices. A spread derivative lets the refiner isolate and hedge just that margin risk.

## Common types of spread derivatives

**Credit spreads** are the difference in yield between a corporate bond and a risk-free [Treasury](/wiki/treasury-bond/). A credit spread of 150 basis points means the corporate bond yields 1.5% more. A [credit default swap](/wiki/credit-default-swap/) is a form of spread derivative paying off if the spread widens (company gets riskier). A spread-trading desk might be long (betting spreads tighten, company improves) or short (betting spreads widen, company deteriorates).

**Commodity spreads** reflect the difference between two related commodities. The **crack spread** (crude oil minus refined products) reflects refinery margins. The **crush spread** (soybeans minus soybean oil and meal) reflects processing margins. A [commodity swap](/wiki/commodity-swap/) can be structured to pay on these spreads, letting processors lock in margins.

**Basis derivatives** trade the difference between a spot price and a [futures price](/wiki/futures-contract/) (the [basis](/wiki/basis/)). If crude spot trades at $85 and the 3-month futures at $84.50, the basis is $0.50. A basis swap or [calendar spread](/wiki/calendar-spread/) allows traders to isolate basis risk and profit from basis convergence near expiration.

**Currency spreads** isolate relative performance of two currencies. A trader might buy EUR relative to GBP (long the EUR/GBP spread) without taking a stance on USD. Central banks use spread derivatives to manage [cross-currency](/wiki/cross-currency-swap/) exposures.

**Index spreads** pay on the gap between two indices. The difference between the S&P 500 and Russell 2000 (large-cap vs. small-cap) is a [style rotation](/wiki/style-rotation/) exposure. A spread derivative lets a fund bet on style without taking absolute market risk.

## Hedging and arbitrage applications

**Margin hedging.** A petroleum refiner produces refined products (heating oil, gasoline) from crude oil. The margin—the spread between output price and input cost—is what matters. The refiner can hedge absolute crude price with a [futures contract](/wiki/futures-contract/) and absolute product prices with another futures contract, but a spread derivative does both at once, isolating the margin.

**Relative value arbitrage.** If two bonds with similar credit profiles have spreads that diverge beyond historical norms, a trader may buy the tighter one and short the looser one, betting the spread converges. This is [relative value](/wiki/relative-valuation/) trading and is often implemented via spread derivatives like [asset swaps](/wiki/basis-swap/).

**Calendar spreads.** If near-term and far-term [futures](/wiki/futures-contract/) prices diverge unusually, a trader might buy the far-term and sell the near-term (or vice versa), betting the [contango](/wiki/contango/) or [backwardation](/wiki/backwardation/) curve reverts. The payoff depends on the spread between the two contract prices.

## Mechanics and pricing

A simple spread derivative might pay:

```
Payoff = max(Spread − Strike, 0) × Notional
```

Or linearly:

```
Payoff = (Price A − Price B) × Notional
```

Pricing uses similar methods to regular [options](/wiki/option/) and [swaps](/wiki/swap/): [Monte Carlo](/wiki/monte-carlo-options-pricing/), [binomial trees](/wiki/binomial-option-pricing/), or closed-form solutions if both underlyings are normally distributed. The key challenge is modeling the **correlation** between the two underlyings. If they are highly correlated, the spread is low-volatility; if uncorrelated, the spread is high-volatility.

## Risk and constraints

Spread derivatives can reduce or misdirect risk:

**Concentrated risk.** A trader might believe spreads are too tight, sell a spread derivative, and expect them to widen. If both underlyings move in the same direction but the spread doesn't widen as expected, the trader can still lose. Spread risk is not "spread-free"—the absolute levels still matter.

**Liquidity mismatch.** Spread derivatives require both legs to be liquid. If one underlying is illiquid or trades infrequently, the spread-derivative price becomes unreliable. A trader might lock in a spread that looks attractive but can't execute when needed.

**Correlation assumption.** Spread derivatives assume the historical correlation between two underlyings continues. In stress or [black-swan](/wiki/black-swan/) events, correlations can break down. Two normally correlated assets might move together, eliminating the spread benefit.

## Spread derivatives vs. relative-value strategies

Spread derivatives are one tool for [relative value](/wiki/relative-valuation/) investing. An alternative is to separately hedge each leg—buy one asset, short the other. A spread derivative bundles the bet into a single contract, simplifying execution and potentially reducing costs. But it also introduces [counterparty risk](/wiki/counterparty-risk/) to the derivative issuer.

<div class="wiki-seealso">

### Closely related
- [Spread Option](/wiki/spread-option/) — option whose payoff is based on the difference between two prices
- [Basis](/wiki/basis/) — the difference between spot and futures prices
- [Calendar Spread](/wiki/calendar-spread/) — trading the difference between near-term and far-term prices
- [Commodity Swap](/wiki/commodity-swap/) — agreement to exchange cash flows based on commodity prices
- [Credit Spread](/wiki/credit-spread/) — difference in yield between a corporate bond and a risk-free benchmark

### Wider context
- [Derivative](/wiki/option/) — financial contract whose value depends on underlying asset(s)
- [Relative Value](/wiki/relative-valuation/) — strategies comparing valuations of related securities
- [Arbitrage](/wiki/arbitrage-defi/) — simultaneous purchase and sale to lock in riskless profit
- [Swap](/wiki/swap/) — exchange of cash flows based on underlying assets or rates
- [Futures Contract](/wiki/futures-contract/) — standardized, exchange-traded derivative contract

</div>

---
title: "Ratio Spread Undefined Risk Explained"
description: "A ratio spread has undefined risk because you sell more option contracts than you buy, leaving a naked (unhedged) leg. Learn how to calculate maximum loss."
keywords:
  - ratio spread undefined risk
  - ratio spread strategy
  - naked short calls
  - option spread risk
  - undefined loss options
image: /svg/derivatives.svg
---

*A **ratio spread** is an options strategy where a trader buys a fixed number of [call options](/call-option/) (or [puts](/put-option/)) at one [strike price](/strike-price/), then sells a *larger* number at another strike. For example: buy 10 calls at $100 strike, sell 15 calls at $105 strike. The 5 extra sold calls form a naked (unhedged) short position. If the stock rallies sharply, those naked calls expose the trader to theoretically unlimited loss, making ratio spreads an advanced strategy suited only to experienced traders with defined risk tolerances.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ratio Spread — Undefined Risk — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Selling more contracts than you buy creates a naked leg and undefined loss potential.</div>

|   |   |
|---|---|
| **Trade structure** | Buy N contracts, sell M > N contracts |
| **Naked leg size** | M − N unhedged short positions |
| **Maximum profit** | Occurs at specific price; known upfront |
| **Maximum loss** | Theoretically unlimited (or to zero) |
| **Risk type** | Undefined; directional |
| **Typical use** | Income generation in neutral markets |
| **Margin requirement** | High, due to naked leg |

</aside>

## Why a Ratio Spread Has a Naked Leg

The risk in a ratio spread arises from asymmetry. Every bought [option](/option/) hedges one sold [option](/option/); any sold options beyond that count are naked—unsecured, running against the trader.

**Example (call ratio spread):**
- Buy 10 calls at $100 strike for $2 each (costs $2,000).
- Sell 15 calls at $105 strike for $0.80 each (collect $1,200).
- Net debit: $2,000 − $1,200 = $800.
- Naked short: 5 calls at $105.

If the stock rallies to $110:
- Your 10 long calls gain $10 × 10 = $100 profit (intrinsic value).
- Your 15 short calls lose $5 × 15 = $75 (they are deep in-the-money).
- Net: $100 − $75 = $25 profit at $110.

But at $115:
- Long calls gain: $15 × 10 = $150.
- Short calls lose: $10 × 15 = $150.
- Net: $0 breakeven.

Beyond $115, losses accelerate. At $120:
- Long calls gain: $20 × 10 = $200.
- Short calls lose: $15 × 15 = $225.
- Net: −$25 loss.

At $200 (an extreme):
- Long calls gain: $100 × 10 = $1,000.
- Short calls lose: $95 × 15 = $1,425.
- Net: −$425 loss (and it worsens further).

## Calculating Maximum Loss

For a **call ratio spread**, maximum loss is not truly "unlimited" in a practical sense (the stock cannot fall below zero), but it is **undefined** because losses expand indefinitely as price climbs above the naked short strike.

**Formula for call ratio spread:**
```
Max Loss = (Short Strike − Long Strike) × Number of Naked Contracts × Contract Multiplier − Initial Credit
```

Using the example above:
- Short strike: $105
- Long strike: $100
- Difference: $5
- Naked contracts: 5
- Multiplier (for equities): 100 shares per contract

Max loss = ($105 − $100) × 5 × 100 − ($800) = $2,500 − $800 = $1,700

This occurs at the short strike ($105) and climbs worse beyond it.

For a **put ratio spread** (buy puts at a lower strike, sell more puts at a higher strike), the logic reverses: losses grow if the stock crashes below the naked short strike (the higher strike in a put spread). Max loss again scales with the strike difference, number of naked contracts, and the contract multiplier.

## Why Traders Use Ratio Spreads Despite Undefined Risk

The undefined risk is offset by **lower initial cost or credit**.

In the example above, you paid only $800 net for a 10-contract hedge against a 5-contract naked short. You reduced the capital needed compared to selling 15 naked calls outright (which would cost $1,200 in margin). The cheaper entry appeals to [income](/income-etf/)-focused traders in neutral or slightly bullish markets.

**Maximum profit is also known and often achieves 50–100% return on the $800 initial cost if the stock stays between the two strikes at expiration.**

Traders who believe a stock will stay in a range and want to extract premium in a capital-efficient way use ratio spreads. They accept the undefined-loss risk in exchange for lower capital outlay and defined maximum profit.

## Managing the Naked Leg

Professional traders do not simply hold ratio spreads to [expiration](/expiration-date/). They actively manage the naked leg:

1. **Close early**: If the stock approaches the naked short strike, the trader closes the entire spread or just the naked contracts, locking in a smaller loss than waiting.

2. **Roll the short contracts**: Sell the exposed calls at a higher strike or a later [expiration](/expiration-date/) to move the risk and extend the profit window.

3. **Buy back the naked leg**: If the stock rises sharply, buy back just the 5 naked calls to eliminate undefined risk, then manage the remaining 10 long minus 10 short (a traditional [spread](/call-option/)).

4. **Set stop-loss levels**: Traders define a price level (e.g., "close all positions if stock hits $110") to cap losses.

## Distinguishing Ratio Spreads from Other Strategies

- **Spread vs. straddle**: A [spread](/call-option/) involves two [strike prices](/strike-price/); a straddle uses one strike but both a call and a put.
- **Ratio spread vs. covered call**: A [covered call](/covered-call/) involves selling calls against a long stock position, which is fully hedged. A ratio spread leaves some calls naked.
- **Defined vs. undefined risk**: A traditional [spread](/call-option/) (buy 10 calls, sell 10 calls at a higher strike) has fully defined risk. A ratio spreads (buy 10, sell 15) does not.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the long leg of a call ratio spread
- [Put option](/put-option/) — the long leg of a put ratio spread
- [Strike price](/strike-price/) — the two prices that define a ratio spread
- [Covered call](/covered-call/) — a fully hedged short-call strategy
- [Option premium](/option-premium/) — the income collected from selling the extra contracts

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — why traders use spreads to limit risk
- [Expiration contracts](/expiration-contracts/) — time decay affecting both legs
- [Volatility smile](/volatility-smile/) — why different strikes have different implied volatilities
- [Theta](/theta/) — time decay, which favors the short leg
- [Greeks (delta, gamma, vega)](/delta/) — tools for managing ratio spread exposures

</div>

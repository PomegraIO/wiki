---
title: "Split-Strike Synthetic"
description: "An options strategy that uses a purchased call and sold put at different strikes to replicate stock ownership while reducing upfront cost and accepting defined gap risk."
keywords:
  - option strategy
  - synthetic position
  - call and put
  - zero-cost collar
  - risk management
image: "/svg/derivatives.svg"
---

*A **split-strike synthetic** is an options strategy that constructs a synthetic long stock position using a call option and a put option at different [strike prices](/wiki/strike-price/), reducing the net cost of entry while accepting a defined zone of unprotected risk between the two strikes.*

## How the mechanics work

The split-strike synthetic begins with buying a call option and selling a put option. The key distinction from a standard synthetic long is that the two legs sit at different strike prices rather than the same strike.

In a typical textbook synthetic, you'd buy an at-the-money call and sell an at-the-money put at the same strike, creating a synthetic long that replicates stock ownership. The split-strike version buys an out-of-the-money call at a higher strike and sells an out-of-the-money put at a lower strike. This misalignment of strikes creates the cost savings—the premium you collect from selling the put at a lower level offsets more of (or may fully subsidize) the call premium you pay.

The trade-off is immediate: you accept a "gap zone" between the two strikes where losses are unprotected. If the stock price falls into that zone—between the put strike and call strike—you own losses without call protection below the put strike and without put support above it.

## Why traders use it

The primary appeal is capital efficiency. If you want synthetic long exposure but cannot justify paying full [option premium](/wiki/option-premium/) for an at-the-money synthetic, the split-strike lets you drastically reduce or eliminate net cash outlay. For traders managing many positions or working with leverage, that cost reduction can unlock otherwise unavailable strategies.

Institutional investors and hedge funds often layer split-strike synthetics into larger hedging programs. By carefully selecting strike widths, they create zero-cost or near-zero-cost synthetic longs that preserve large directional upside while capping downside risk to the gap zone. In volatile markets, the wider the strikes, the lower the cost—but the larger the unprotected window.

## The gap zone and how it limits protection

The gap zone is both the design and the danger. Suppose you buy a call at a 105 strike and sell a put at a 95 strike on a stock trading near 100. Between 95 and 105, your profit or loss is not what owning stock would be; it's whatever the market delivers. If the stock falls to 100, you lose 5 points and have no put protection. If it falls to 95, you're obligated to buy stock at 95 (your put is exercised), locking in a 5-point loss. Below 95, the put shields you from further loss, but you've already taken the full 5-point hit.

In sideways or mildly volatile markets, this gap zone is often dormant. In sudden reversals—market crashes, unexpected company news, or sector rotations—the gap zone can capture significant losses. That trade-off is permanent and built into the entry.

## Variations and context

The split-strike synthetic sits at the intersection of synthetic replication and [collar](/wiki/zero-cost-collar/) structures. A zero-cost collar is often confused with split-strike synthetics, though they differ: a collar is typically applied to a long stock position you already own (you sell a call to pay for a put), whereas a split-strike synthetic creates the long stock replica purely through options from the start.

Traders also stack split-strike synthetics with other derivatives—pairing them with further put spreads below the gap zone to cap losses, or with call spreads above to cap gains. These combinations are common in [hedge fund](/wiki/hedge-fund/) option books and in volatility-focused [exchange-traded funds](/wiki/etf/) that use options to track benchmarks.

## Liquidity and assignment risk

Split-strike synthetics rely on [options liquidity](/wiki/liquidity-risk/). When strikes are far from the [at-the-money](/wiki/at-the-money/) point, bid–ask spreads widen, and slippage can erase your cost savings before you even enter the full position. Traders using tight gap zones (95–105, for example) often find better liquidity than those using wider gaps (90–110), which means executing a very cheap synthetic often means paying more in friction.

Assignment is also a risk. Early [assignment](/wiki/exercise/) on the short put exposes you to ownership risk at an unfavourable moment. Assignment on the long call is less likely but possible, and would lock in gains early. Traders managing split-strike synthetics often hold them to [expiration](/wiki/expiration-date/) to avoid these complications.

## When it fails

The strategy assumes stock price movement is gradual enough to miss the gap zone or exits before disaster strikes. In markets with sudden gaps—earnings announcements, geopolitical shocks, or liquidity crises—the gap zone may be crossed overnight. Unlike a put-protected long stock position, there is no floor in the gap; a 10% overnight drop leaves you fully exposed.

Split-strike synthetics also assume you will actually exit or roll the position. Traders sometimes build positions expecting high volatility to collapse, at which point the options deflate and the position unwinds profitably. But if that volatility collapse never arrives, or if it arrives alongside a price move into the gap zone, the strategy becomes a liability masquerading as a cost saver.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/wiki/option/) — a contract granting the right to buy or sell an underlying asset at a set price
- [Strike price](/wiki/strike-price/) — the fixed price at which an option can be exercised
- Synthetic long — a call bought and put sold at the same strike to replicate stock ownership
- [Zero-cost collar](/wiki/zero-cost-collar/) — selling an upside call to finance downside put protection on owned stock
- [Call option](/wiki/call-option/) — the right to buy an underlying asset at a fixed price before expiration
- [Put option](/wiki/put-option/) — the right to sell an underlying asset at a fixed price before expiration
- [Option premium](/wiki/option-premium/) — the upfront price paid to acquire or received from selling an option

### Wider context

- [Leverage ratio (forex)](/wiki/leverage-ratio-forex/) — using borrowed capital to amplify position size and returns
- [Risk management](/wiki/value-at-risk/) — quantifying and limiting downside exposure
- Derivative — financial instruments whose value is derived from an underlying asset
- [Volatility smile](/wiki/volatility-smile/) — the observed pattern that implied volatility varies across strike prices

</div>
---
title: "Slippage"
description: "Difference between expected and actual execution price when entering or exiting a trade."
keywords:
  - execution cost
  - market impact
  - order timing
  - forex trading friction
---

*[**Slippage**](/wiki/slippage-management/) is the gap between the price a trader intends to enter or exit a trade and the actual price at which an order executes. It arises from three sources: [bid-ask spreads](/wiki/bid-ask-spread/), market impact of the order itself, and adverse price moves during the execution window.*

<div class="wiki-hatnote">
Distinct from commission (explicit broker fees) or [market impact](/wiki/market-impact-cost/), slippage measures the quality of price discovery and execution timing.
</div>

<aside class="wiki-infobox">

| Driver | Typical Magnitude |
|---|---|
| Bid-ask spread cost | 0.1–2 pips (liquid forex pairs) |
| Market impact (large orders) | 0.5–5+ pips (scale-dependent) |
| Adverse move during execution | 0–10+ pips (volatility-dependent) |
| High-frequency period cost | <1 millisecond |
| Daily slippage impact | 5–20 bps annual (active traders) |

</aside>

## How the bid-ask spread drives immediate slippage

Every listed [currency pair](/wiki/currency-pair/) has two prices: the [bid](/wiki/bid-ask-spread/) (what buyers will pay) and the [ask](/wiki/bid-ask-spread/) (what sellers demand). The difference—the spread—is the floor cost of any roundtrip trade. In highly liquid pairs like [EUR/USD](/wiki/eur-gbp-euro-sterling/), the spread might be 1–2 pips (0.0001–0.0002 USD per euro). A retail trader placing a market order to buy immediately "hits the ask" at 1.0850, while a simultaneously placed sell order "lifts the bid" at 1.0849, crystallizing the 1-pip cost.

Slippage from the spread is unavoidable in electronic markets—it is the compensation [market makers](/wiki/market-makers/) require to stand ready with quotes. In less liquid pairs or during low-volume hours, spreads widen. [Exotic pairs](/wiki/exotic-currency-pair/) routinely quote 5–20 pips wide, meaning a retail order slips from intended price by that amount immediately upon execution. The spread is thus a baseline slippage floor that all traders face.

## Market impact: how large orders move prices against the trader

Market impact slippage emerges when a single order is so large that it exhausts [available liquidity](/wiki/liquidity-pool/) at current prices, forcing the trader to access successively worse prices. A $100 million market order in a relatively illiquid [currency pair](/wiki/carry-trade-pairs/) may move the price by several pips as the order "works through" the [order book](/wiki/order-book-depth/). The trader achieves an average execution price worse than the initial quote.

This cost scales with order size and inversely with available liquidity. [High-frequency traders](/wiki/high-frequency-trading/) exploit this by fragmenting large institutional orders across multiple venues and time intervals, using [TWAP](/wiki/twap-order/) or [VWAP](/wiki/vwap-order/) algorithms to minimize market impact. A pension fund moving $500 million across currencies might experience 50–100 bps of slippage if executed in a single block; the same amount executed over several hours costs a fraction as much.

## Price movement during the execution window

The third source of slippage is exogenous: prices move between the time a trader commits to enter and when the order is actually processed. In [volatile](/wiki/volatility-index-futures/) markets or near economic data releases, [implied volatility](/wiki/implied-volatility/) spikes and prices swing sharply. A market order submitted at 9:59 EST seconds before a [Fed announcement](/wiki/federal-funds-rate-target/) may execute at a significantly worse price if the Fed surprise moves the market hard.

This latency-driven slippage is particularly acute for retail traders who experience network delays between their trading platform and the broker's execution system. High-frequency traders mitigate this by colocating computers at exchange data centers, achieving sub-millisecond latency. For casual traders using standard internet connections and third-party trading platforms, slippage from adverse moves can easily exceed the bid-ask spread during volatile periods.

## Slippage in different market conditions and venues

During calm [forex](/wiki/forex-leverage/) conditions, slippage is modest. The USD/JPY pair, one of the most liquid, trades with spreads of 0.5–1.5 pips and minimal market-impact costs for orders under $10 million. [Emerging-market currency pairs](/wiki/emerging-market-currency-pairs/) are far more costly: the [Brazilian Real](/wiki/forex-leverage/) or Turkish Lira trade with spreads of 10–50 pips wide, and even modest orders experience measurable [drawdown](/wiki/drawdown-forex/).

Slippage widens dramatically during [flash crashes](/wiki/flash-crash-2010/) or geopolitical shocks. The 2015 [Swiss Franc](/wiki/swiss-franc/) unpegging saw [bid-ask spreads](/wiki/bid-offer-forex/) explode to 50+ pips in minutes, and limit orders that were in-the-money were simply never filled. During the 2020 COVID crash, [crude oil](/wiki/crude-oil/) futures experienced backwardation and negative prices, leaving many traders with slippage far worse than anything historical data suggested was possible.

## Algorithmic execution to minimize slippage

Professional traders use several strategies to cut slippage. [Arrival price](/wiki/arrival-price/) benchmarking compares final fill prices to the market price when the order was received. [Implementation shortfall](/wiki/implementation-shortfall/) adds market impact, missed-opportunity costs (prices moved favorably after cancellation), and explicit commissions into a single metric. Banks and asset managers employ algorithms that:

- Break large orders into smaller tranches and execute them across multiple time intervals
- Monitor [market microstructure](/wiki/market-impact-cost/) (order-flow imbalances, [open interest](/wiki/open-interest/)) to find moments of lower impact
- Route orders to multiple venues (prime brokers, [alternative trading systems](/wiki/alternative-trading-system/), [crossing networks](/wiki/crossing-network-trading/)) to find hidden liquidity
- Use dark venues ([dark pools](/wiki/dark-pools/)) where order size is not broadcast, reducing information leakage

These tactics reduce slippage from 50–100 bps for naive execution to 5–15 bps for sophisticated orders.

## Slippage as a persistent cost to retail investors

For retail traders in [forex](/wiki/forex-margin/), slippage is a hidden tax. Backtested trading strategies often assume perfect fills at the open or close; in reality, actual executions slip 1–5 pips from intended prices. Over 100 trades, this compounds into 1–5% of account value in friction costs. Many profitable-in-theory retail forex systems become unprofitable once slippage, [margin calls](/wiki/margin-call-forex/), and [overnight fees](/wiki/overnight-rate-mechanism/) are factored in.

The most effective slippage reduction for retail participants is using [limit orders](/wiki/limit-order/) instead of market orders and accepting that some orders simply won't fill. A limit order to buy EUR/USD at exactly 1.0850 may never execute in volatile markets, but it removes the risk of paying 1.0852 or worse. Conversely, during calm conditions, limit orders may sit on the books for hours, meaning missed moves if price gaps past the limit level.

<div class="wiki-seealso">

### Closely related
- [Bid-Ask Spread](/wiki/bid-ask-spread-forex/) — Floor cost of slippage in forex
- [Market Impact Cost](/wiki/market-impact-cost/) — Large-order execution cost
- [Arrival Price](/wiki/arrival-price/) — Benchmark for measuring slippage
- [Implementation Shortfall](/wiki/implementation-shortfall/) — Total execution cost framework

### Wider context
- [High-Frequency Trading](/wiki/high-frequency-trading/) — Exploits slippage through speed
- [Dark Pools](/wiki/dark-pools/) — Venues designed to reduce market impact
- [Order Types](/wiki/order-types/) — Limit, market, and exotic order mechanics
- [Volatility Index](/wiki/volatility-index-futures/) — Elevated volatility increases slippage risk

</div>

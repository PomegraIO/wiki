---
title: "Intermarket Sweep Order"
description: "A special order type that bypasses trade-through protection to simultaneously execute against liquidity across multiple exchanges."
keywords:
  - intermarket sweep order
  - trade-through protection
  - order routing
  - liquidity aggregation
  - exchange rules
image: "/svg/regulation.svg"
---

*An **intermarket sweep order** (ISO) is a special order type that allows a broker to bypass trade-through protection rules by simultaneously routing orders to multiple exchanges to capture available liquidity. It exists because strict trade-through rules, which normally require trading at the best visible price, could prevent efficient execution when that best price exists in small quantities across fragmented markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Intermarket Sweep Order — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A regulatory carve-out designed to balance price protection with execution efficiency in fragmented markets.</div>

|   |   |
|---|---|
| **What it is** | A special order that bypasses trade-through rules by simultaneously routing to multiple venues |
| **Also called** | ISO; sweep order |
| **Governed by** | SEC Regulation SHO (Rule 10b-21); exchange-specific rules |
| **Key requirement** | Must simultaneously route to all better-priced venues to satisfy the sweep |
| **Primary use** | Capturing liquidity fragmented across [multiple stock exchanges](/stock-exchange/) |
| **Advantage over standard orders** | Avoids delays from sequential price-level sweeps |

</aside>

## Why trade-through rules create a demand for ISOs

The fundamental rule of [stock markets](/stock-market/) for decades has been simple: do not execute a trade at a worse price when a better price is visible elsewhere. This trade-through rule prevents a market where prices diverge wildly between venues, protecting investors from receiving second-rate execution.

But modern market structure fragments liquidity. A single stock might trade on the [New York Stock Exchange](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), and a dozen alternative trading systems simultaneously. If 100,000 shares are available at $50.05 on Exchange A and only 500 at $50.04 on Exchange B, strict trade-through rules would seem to require executing all shares at the better price first — even though that quantity is tiny. This created a mechanical problem: how can you route an order efficiently when the best price is scattered in small pockets?

The intermarket sweep order solves this by permitting an exception: a broker can execute a large order across multiple venues *simultaneously*, at varying prices, provided they are sweeping all better-priced liquidity at the same time. The key word is simultaneous. This is not sequential execution; this is coordinated, multi-venue fulfillment in a single moment.

## How an ISO works in practice

Picture a broker with a client order to buy 50,000 shares. Current market data shows:

- Exchange A: 30,000 shares at $50.05
- Exchange B: 15,000 shares at $50.04
- Exchange C: 5,000 shares at $50.03

Under standard [order routing](/order-protection-intermarket-sweep/) rules, the broker would face a tedious sequential sweep: fill 5,000 at $50.03, then 15,000 at $50.04, then 30,000 at $50.05, then hunt for the remaining 5,000. Each leg requires checking whether better prices have appeared.

With an ISO, the broker can route simultaneously to all three venues right now, capturing all visible liquidity at once. The execution blotter might show three trades hitting at the same millisecond — fulfilling the spirit of the rule (no price improvement ignored) while avoiding the mechanical obstruction.

The ISO must be marked as such in the routing system. This label serves as a regulatory flag that tells market operators: this order is permitted to execute across multiple venues because it is sweeping all better prices in parallel.

## The SEC framework and exchange rules

The SEC originally formulated the ISO concept in Regulation SHO, issued in 2004 as part of the broader [short-selling](/short-selling/) framework. The rule specifically permits a broker to route simultaneous orders to multiple exchanges, provided the broker has determined that the sweep captures all quotations (or nearly all quotations, with some technical tolerance) at better prices.

Later, under Regulation SHO Rule 10b-21, the framework expanded slightly. Exchanges like the [NYSE](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) adopted their own ISO mechanics in their rulebooks. NASDAQ, for instance, allows an ISO to ignore a displayed [bid-ask spread](/bid-ask-spread/) at another venue if the order is routed simultaneously to that venue at a more aggressive price. The [Securities and Exchange Commission](/securities-and-exchange-commission/) oversees compliance.

In practice, almost all routing is automated: a trader's order management system identifies the best prices, executes an ISO order type through a broker's routing algorithm, and the algorithm handles the simultaneous transmission to multiple venues. The [market maker](/market-maker-trading/) at each venue either fills the incoming ISO immediately or allows it to rest as a [limit order](/limit-order/) on their book.

## When ISOs matter most

ISOs are most useful in large-cap, highly liquid stocks where volumes fragment significantly across venues. A $50 stock that trades millions of shares per day will often have its available liquidity split: perhaps 40 per cent on the NYSE, 35 per cent on NASDAQ, 15 per cent on an alternative trading system, and 10 per cent on another. An institutional trader buying a block in such a stock would face real friction trying to execute sequentially. An ISO lets them access all pockets at once.

Conversely, in less-liquid stocks or during market stress, the benefit diminishes. If there is only one venue with significant depth, there is nothing to sweep. And during periods of extreme volatility, the window for simultaneous execution shrinks; quotes can change between the time the order is prepared and the time it reaches each venue.

## The regulatory debate

Critics argue that ISOs remain an exception that partly undermines the spirit of trade-through rules. They note that ISOs can incentivize fragmentation: if a broker knows it can sweep via ISO, there is less pressure to consolidate liquidity onto a single venue. Proponents counter that ISOs actually serve price discovery and efficiency, allowing large orders to fill at competitive rates without the friction of sequential routing.

The tension reflects a deeper design question in modern market structure: should rules prioritize transparency and simplicity, or liquidity and speed? The ISO represents a compromise, accepting some added routing complexity in exchange for more efficient capital flow.

## See also

<div class="wiki-seealso">

### Closely related

- Trade-through Rule — the protection that ISOs bypass under defined conditions
- Regulation SHO — SEC ruleset governing short sales and trade-through exceptions
- [Alternative Trading System](/alternative-trading-system/) — off-exchange venues that ISOs often sweep
- [Bid-Ask Spread](/bid-ask-spread/) — the price gap that ISOs help bridge across venues
- [Market Maker](/market-maker-trading/) — dealers who often face incoming ISOs on their books
- Order Routing — the broker process that an ISO initiates

### Wider context

- [Stock Exchange](/stock-exchange/) — the primary venues where ISOs operate
- [Stock Market](/stock-market/) — the broader structure ISOs help fragment and reunify
- [Liquidity Risk](/liquidity-risk/) — the market friction ISOs are designed to reduce
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of ISO frameworks

</div>

---
title: "Exchange Co-location Service Explained"
description: "Exchange co-location is rack space inside an exchange's data center, sold to traders and firms to minimize network latency. It raises fairness questions about market access."
keywords:
  - exchange co-location service
  - colocation data center
  - high-frequency trading latency
  - market access fairness
  - algorithmic trading venue
  - network latency trading
  - exchange infrastructure
image: /svg/markets.svg
---

*An **exchange co-location service** lets a trading firm rent server rack space inside the exchange's own data center, placing their computers inches from the exchange's matching engine. This reduces message latency to microseconds, giving co-located firms an advantage—which is why regulators and non-co-located traders debate whether equal-speed access is achievable.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exchange Co-location — Key Facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Proximity to the matching engine translates into speed, which translates into microsecond trading edges.</div>

|   |   |
|---|---|
| **What is included** | Rack space, power, cooling, direct fiber connection to matching engine |
| **Typical latency from colo** | 100–500 microseconds from order to market feedback |
| **Typical latency from remote** | 10–100+ milliseconds (10,000–100,000 microseconds) |
| **Cost per month** | $1,000–$50,000+ depending on rack size and exchange |
| **Primary users** | [Algorithmic traders](/algorithmic-trading/), [hedge funds](/hedge-fund/), market makers |
| **Fairness debate** | Whether co-location access should be equal and transparent |
| **Regulatory stance** | Allowed but scrutinized; exchanges must disclose availability and pricing |

</aside>

## How Co-location Works

Every stock exchange operates a matching engine—a computer that receives orders, sorts them by price and time, and executes trades when buy and sell orders cross. The matching engine sits in the exchange's data center, a secure facility with redundant power, cooling, and network connections.

When a trader connects remotely—from a brokerage office across town or from a hedge fund overseas—their orders travel over the internet. The order must:

1. Leave the trader's computer
2. Cross multiple routers and network hops
3. Reach the exchange's matching engine
4. Execute
5. Send confirmation back to the trader

Each network hop introduces latency. On a typical internet connection, a round trip takes 10–100+ milliseconds. In [algorithmic trading](/algorithmic-trading/), where profits depend on reacting to price changes in microseconds, this delay is an eternity.

Co-location eliminates most of these hops. A firm rents a server in the exchange's data center and connects it directly to the matching engine via a short, dedicated fiber cable. The latency drops to 100–500 microseconds. The co-located trader's order reaches the engine and receives confirmation in the time it takes less-connected traders to register the *first* price move.

## What's Included in a Co-location Package

An exchange co-location service typically bundles:

- Physical rack space (half rack, full rack, or multiple racks)
- Redundant power feeds and uninterruptible power supplies
- HVAC cooling tailored to server density
- Direct fiber connection to the matching engine
- Dedicated support for hardware issues
- Fire suppression and security

A trader brings their own servers, but the exchange provides the infrastructure. Monthly costs range from $1,000 for a small half-rack on a regional exchange to $50,000+ for a full rack on a major exchange like [NYSE-ARCA](/nyse-arca/) or [NASDAQ](/nasdaq/). Firms using co-location typically justify the cost with trading volume and strategies that depend on speed—[market maker](/market-maker-trading/) operations, [momentum investing](/momentum-investing/) algorithms, or index arbitrage.

## The Latency Advantage and Reality

The latency benefit is real but often overstated. A co-located trader who sends an order in 200 microseconds has a hard advantage over a remote trader at 50 milliseconds—a 250× latency edge. But this doesn't guarantee profit.

The co-located trader may see a stock price move first, but so may thousands of other traders and algorithms all in the same data center, often co-located on the same exchanges. Being first is valuable only if you can profitably capture the movement before others do. If everyone in the colo space sees the same data at near-identical times, the latency edge compresses.

Moreover, latency is only one component of a profitable trading algorithm. Smart order routing, execution quality, and directional accuracy matter too. A co-located firm with a mediocre algorithm makes no money; a remote firm with a superior signal can overcome latency.

## The Fairness Question

The latency advantage has sparked debate. Critics argue that co-location creates a tiered market: those who can afford $50,000/month to rent server space in an exchange data center get a speed edge, while public investors and smaller traders do not. This undermines the principle of equal access to markets.

Exchanges counter that co-location is available to anyone willing to pay and that the service does not distort pricing—it is merely a choice of connection method. A retail investor can still trade; they simply do so at normal latency, same as other remote traders.

Regulators have imposed transparency requirements. Exchanges must disclose:

- The availability and pricing of co-location services
- Any preferential treatment or bandwidth allocation
- Latency benchmarks for co-located versus non-co-located participants

The SEC has also examined whether exchanges offer "paid prioritization"—allowing co-located traders to queue jump or receive data feeds faster. Some early concerns were addressed; today, most exchanges enforce fair queuing (all orders are processed in strict time-priority, regardless of connection speed).

## Latency Arbitrage and Market Quality

Co-location enables strategies that would be impossible or unprofitable for remote traders. A **latency arbitrage** strategy might:

1. Co-located trader sees a large buy order arrive at the home exchange
2. That trader instantly buys the same stock on a competing exchange, aware that the large order will likely move both prices
3. Sells shares back to the original buyer at a profit, all within microseconds

This strategy is profitable only because of latency dominance. Remote traders cannot execute it—by the time they see the initial buy and decide to act, the window has closed.

Whether this is beneficial or harmful depends on perspective. Market makers argue that latency-driven firms provide liquidity and [price discovery](/price-discovery/). Critics argue that latency arbitrage is a tax on slower traders, widening [bid-ask spreads](/bid-ask-spread/) for retail investors.

## Alternatives to Co-location

Not all traders use co-location. Alternatives include:

- **Direct fiber leasing**: Bypassing the internet entirely by leasing a dedicated fiber connection to the exchange. This is more expensive (tens of thousands per month) but offers even lower latency and greater reliability.
- **Cloud proximity services**: Using a cloud provider's server region close to the exchange data center. Less expensive than exchange co-location but typically higher latency.
- **Remote trading with optimized routing**: Smart algorithms and direct market access (DMA) can partially offset latency by choosing the most efficient network path.

For most traders, especially long-term investors, co-location is unnecessary. For ultra-high-frequency strategies or market-making operations, it is essential.

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic Trading](/algorithmic-trading/) — strategies enabled by low latency
- [Market Maker Trading](/market-maker-trading/) — primary user of co-location services
- [Bid-Ask Spread](/bid-ask-spread/) — how latency affects pricing
- [Price Discovery](/price-discovery/) — market transparency and information flow
- [Stock Exchange](/stock-exchange/) — exchange operations and membership

### Wider context

- [Execution Risk](/execution-risk/) — slippage and order impact
- [Fragmented Market](/fragmented-market/) — multi-venue trading and latency arbitrage
- [Alternative Trading System](/alternative-trading-system/) — non-exchange venues and access
- [Market Order](/market-order/) — basic order execution and speed

</div>

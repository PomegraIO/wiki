---
title: "Crossing Network vs Dark Pool"
description: "The distinction between traditional broker-operated crossing networks and modern dark pools, including matching rules, disclosure, and typical participants."
keywords:
  - crossing network vs dark pool difference
  - dark pool vs crossing network
  - dark pool matching rules
  - crossing network execution
image: /svg/trading.svg
---

*Although both **crossing networks** and **dark pools** execute large trades away from lit markets, they differ fundamentally in operation: crossing networks match orders at prices derived from public markets on a pre-trade transparent basis, while dark pools use proprietary matching algorithms and offer less pre-trade visibility, typically serving institutional traders seeking to minimize [market impact](/market-maker-trading/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crossing Networks vs Dark Pools — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two off-exchange venues with different transparency and matching models.</div>

|   |   |
|---|---|
| **Typical operator** | Crossing: major brokers (Goldman, Morgan Stanley, JPMorgan). Dark pools: brokers, independent operators, exchanges |
| **Price formation** | Crossing: derived from public market (midpoint, VWAP, etc.). Dark pools: proprietary algorithms, negotiated |
| **Pre-trade transparency** | Crossing: visible order book at execution price. Dark pools: limited or no pre-trade visibility |
| **Order types** | Crossing: simple VWAP, IS, market orders. Dark pools: complex, conditional, algorithmic |
| **Typical use case** | Crossing: large institutional block orders with minimal slippage. Dark pools: complex execution, reduced market impact |
| **Regulation** | Both require [SEC](/securities-and-exchange-commission/) registration as [alternative trading systems](/alternative-trading-system/) (ATS) |
| **Typical volume** | Crossing: smaller pools with limited daily volume. Dark pools: larger and more liquid |

</aside>

## Origins and Evolution

Crossing networks emerged in the 1980s as a tool for brokers to match internal buy and sell orders without routing them through the public market. A broker's large-cap desk might simultaneously hold a client order to buy 500,000 shares and another client order to sell 500,000 shares of the same stock; crossing the two internally at mid-market price avoided the [bid-ask spread](/bid-ask-spread/) and reduced market impact.

Dark pools appeared later, proliferating in the 2000s as electronic trading accelerated and institutions sought more sophisticated ways to execute large trades with minimal visibility. While crossing networks use transparent, market-derived pricing, dark pools introduced proprietary algorithms, conditional orders, and non-transparent market data — driving a fundamental shift in how large trades were handled.

## Price Formation: Market-Derived vs. Proprietary

The most straightforward distinction is pricing logic. A **crossing network** sets its execution price based on the public market: a VWAP (volume-weighted average price) of the most recent period, the midpoint of the public spread, or the last reported trade price. The trader knows exactly what price will apply because the calculation is mechanical and tied to observable market data.

A **dark pool** uses proprietary algorithms that may incorporate its own order flow, internalizations, or negotiated terms. The matching engine is opaque to participants; the dark pool operator may offer volume incentives, tiered pricing for frequent traders, or conditional orders that execute only under certain market conditions. Traders submit orders without knowing the exact price until execution.

This difference reflects the dark pool's role in managing internalizations (orders matched within the pool rather than on a lit exchange) and in leveraging the broker's proprietary information about client intent.

## Pre-Trade Transparency

A **crossing network** displays a public order book before trades execute (or makes clear that trades will execute at a specific formula price). Participants can see aggregated depth and understand the likely execution price before committing capital.

A **dark pool** does not display pre-trade information to the market or even to all participants. An incoming order is matched against existing pool orders via the dark pool's algorithm, with execution happening without visibility to the broader market. Some dark pools show some liquidity information to members, but this is not standardized and often comes with restrictions on use.

The lack of pre-trade transparency in dark pools is why they are called "dark" — the public market cannot observe the orders resting there.

## Order Types and Complexity

Crossing networks support straightforward order types: market orders at the crossing price, limit orders, and algorithmic orders (like VWAP or IS — "implementation shortfall"). The logic is relatively simple and standardized.

Dark pools offer far more complex order types: iceberg orders (hidden quantity revealed gradually), pegged orders (that move with the public spread), conditional orders (that activate only if certain market conditions are met), and algorithmic variants specific to that pool. A sophisticated trader can program intricate strategies within a dark pool's order system.

## Participant Base and Use Cases

Crossing networks are typically used by large institutional investors (pension funds, mutual funds, insurance companies) placing very large orders that would move the public market. The crossing network allows them to execute a substantial portion internally at a fair, market-derived price, saving the [bid-ask spread](/bid-ask-spread/) and keeping the execution off the tape until after completion.

Dark pools attract a broader participant base, including high-frequency traders, hedge funds, and proprietary desks seeking to exploit the pool's microstructure or to trade against the pool's flow. This diversity of participants can enhance liquidity but also introduces conflicts — for example, a dark pool operator might give certain participants speed advantages or information about incoming order flow, raising questions about [fair dealing](/market-maker-trading/).

## Regulatory Framework

Both crossing networks and dark pools are [alternative trading systems](/alternative-trading-system/) (ATS) and must register with the [SEC](/securities-and-exchange-commission/). The SEC's rules require disclosure of order execution quality, a description of the matching rules, and prohibited conduct (such as trading ahead of customer orders).

However, the SEC's approach to dark pools has been less prescriptive than to traditional [stock exchanges](/stock-exchange/). Regulation SHO and subsequent rules have tightened some dark pool practices (e.g., requiring [short selling](/short-selling/) compliance), but debates continue over transparency and fragmentation.

| Aspect | Crossing Network | Dark Pool |
|---|---|---|
| Price discovery | Based on public market | Proprietary algorithm |
| Order visibility before trade | High | Low or none |
| Typical order size | Very large (blocks) | Varies; can be small to large |
| Speed advantage | Minimal | Often offered |
| Conflict of interest concerns | Moderate | Higher (flow leakage potential) |
| Participant diversity | Limited (mostly buy-side) | Broad (brokers, hedge funds, HFTs) |

## Market Impact and Execution Quality

Crossing networks excel at reducing market impact for very large orders. By matching internally at public prices, an institution avoids moving the public market and keeps the order off the tape, preventing other traders from learning of its intent and front-running.

Dark pools can also reduce market impact, but they introduce a different risk: the execution price may be worse than the public market at the time of trade. A dark pool's algorithms might execute a buy order at a price higher than the public midpoint to attract sellers from the pool, for example. The institution trades reduced market impact for uncertain execution pricing.

## Internalizations and Payment for Order Flow

A critical distinction: crossing networks rarely internalize — they match two incoming orders at a public price. Dark pools routinely internalize — a broker operating the dark pool may match a customer sell order against its own proprietary position or against another customer's buy order, capturing the spread.

This internalization is legal if the broker discloses it and executes the customer order at least as favorably as the public market would. However, it creates a financial incentive for the broker to route order flow to its own dark pool rather than to a competing venue, raising potential conflicts of interest. Payment for order flow (where brokers pay other brokers to send them trades) amplifies this dynamic.

## Modern Evolution and Scrutiny

Crossing networks have remained relatively stable and simple because their value proposition is straightforward and their pricing is objective. Dark pools, by contrast, have faced increasing regulatory scrutiny over concerns about fairness and [market fragmentation](/stock-market/). Questions persist about whether certain dark pool participants (paying premium fees or using specific strategies) enjoy unfair speed or information advantages.

Some institutions have shifted preference toward lit markets and more transparent execution venues, especially for smaller orders. Large block trades remain frequent in crossing networks and dark pools, where the institutional need to minimize market impact outweighs the benefit of public-market transparency.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative Trading System](/alternative-trading-system/) — the regulatory category encompassing both networks and pools
- [Bid-Ask Spread](/bid-ask-spread/) — the spread that crossing networks help traders avoid
- [Market Maker Trading](/market-maker-trading/) — the primary liquidity source on lit exchanges
- [Stock Exchange](/stock-exchange/) — the lit venues with which dark pools compete
- [Short Selling](/short-selling/) — activity subject to rules in dark pools
- [Order Types](/limit-order/) — execution mechanisms used in crossing networks and dark pools

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of alternative trading systems
- [Market Impact](/market-maker-trading/) — institutional concern driving use of both venues
- [High-Frequency Trading](/algorithmic-trading/) — participant type active in many dark pools
- [Market Fragmentation](/stock-market/) — systemic concern related to off-exchange venue growth

</div>

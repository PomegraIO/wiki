---
title: "Crossing Network"
description: "Internal execution venues that match buy and sell orders without displaying them to the public market."
keywords:
  - crossing network
  - dark pool
  - internal matching
  - market impact
---

*A **crossing network** is a private matching engine that pairs buy and sell orders inside a broker or venue without showing them to the public [market](/wiki/stock-market/), reducing [market impact](/wiki/market-impact-cost/) and trading costs.*

Crossing networks are distinct from [dark pools](/wiki/dark-pool/) in their execution model and transparency. While a dark pool may accept orders from external clients and apply its own pricing logic, a crossing network typically operates inside a single broker's ecosystem (e.g., Goldman Sachs' Sigma X) or consortium of members (e.g., Instinet). The core advantage is that large [block trades](/wiki/block-trading-platform/) can be crossed without distorting public-market prices—a client's massive sell order never touches the [order book](/wiki/order-book-depth/), preserving the illusion of [liquidity](/wiki/liquidity-risk/) and avoiding adverse price movement.

<aside class="wiki-infobox">

| Feature | Detail |
|---|---|
| **Visibility** | Hidden from public order book |
| **Matching** | Internal algorithm or broker discretion |
| **Market impact** | Minimal; avoids public disclosure |
| **Execution quality** | Often at midpoint or VWAP |
| **Clients** | Institutional buy-side (funds, pensions) |
| **Regulation** | SEC Rule 10b-5, Reg SHO reporting |
| **Speed** | Varies; not high-frequency driven |

</aside>

## How crossing networks operate

A crossing network accepts orders from clients without immediately publishing them to the public tape or [consolidated quotation system](/wiki/nbbo/). The network's matching engine compares incoming orders and pairs them when execution criteria align. Many networks execute at the midpoint of the current public [bid-ask spread](/wiki/bid-ask-spread/), eliminating [price improvement](/wiki/price-improvement/) haggling while guaranteeing no worse fill than the inside market. Others use [volume weighted average price (VWAP)](/wiki/vwap-order/) or [time weighted average price (TWAP)](/wiki/twap-order/) algorithms to minimize [timing risk](/wiki/timing-option/) over a window.

The operator may also allow direct crossing—a buy side client deposits a giant block, and the crossing network seeks a counterparty within its client base. If a match is found, the trade is executed at a negotiated price (often with [price improvement](/wiki/price-improvement/) vs. the public spread) and then reported to [FINRA](/wiki/finra/) or the relevant [SRO](/wiki/state-securities-regulator/) with a T+0 or T+1 lag.

## Distinction from dark pools and exchanges

A [crossing network](/wiki/crossing-network-trading/) differs from a [dark pool](/wiki/dark-pool/) in governance and scope. A crossing network is typically broker-owned and services that broker's clients; participation is restricted. A dark pool (like Citadel Connect or Goldman's Sigma X) accepts outside flow and has disclosure rules. An [alternative trading system (ATS)](/wiki/alternative-trading-system/) must register with the SEC and follow [Reg SHO](/wiki/regulation-sho/) and [Rule 10b-5](/wiki/rule-10b-5/) enforcement.

Compared to lit exchanges like [NASDAQ](/wiki/nasdaq/) or the [NYSE](/wiki/new-york-stock-exchange/), crossing networks avoid the [maker-taker fee model](/wiki/maker-taker-fee-model/). They also avoid the information leakage: broadcasting a 500,000-share limit order to the NYSE's [order book](/wiki/order-book-depth/) tips off [high-frequency traders](/wiki/high-frequency-trading/) that a large participant is in the market, often triggering [front-running](/wiki/rule-10b-5/) or tactical predation. Crossing networks sidestep this entirely.

## Market impact reduction

The primary value proposition is reducing [market impact](/wiki/market-impact-cost/). Suppose a pension fund needs to sell 2 million shares of a $10 stock with $100k daily volume. Dumping it on the [NYSE](/wiki/new-york-stock-exchange/) would depress the price 5–10%, costing $1–2 million. A crossing network, by internalizing flow from its client base, can match it against a large buy-side buyer (a mutual fund rebalancing or a corporate acquirer) in the dark, executing at the midpoint with zero market impact. The fund pays no [market impact cost](/wiki/market-impact-cost/) but also no [market maker](/wiki/market-makers/) margin—a fair trade when liquidity is scarce.

## Regulatory and transparency concerns

Crossing networks exist in a murky regulatory gray zone. The SEC views them as [alternative trading systems](/wiki/alternative-trading-system/) subject to [Rule 10b-5](/wiki/rule-10b-5/) (antifraud) and [Regulation SHO](/wiki/regulation-sho/) (short-selling restrictions), but many smaller broker-run crossing networks claim exemptions or operate under safe harbors. Major networks like Instinet's Posit or Nomura's dark pool publish summary statistics quarterly (trade counts, volume, price improvement data), but not real-time order flow.

Critics argue that the rise of crossing networks has fragmented [liquidity](/wiki/liquidity-risk/) away from lit exchanges, degrading price discovery for retail investors who see only the public [bid-ask](/wiki/bid-ask-spread/). Others counter that crossing networks are a natural evolution—investors rationally prefer to avoid [market impact](/wiki/market-impact-cost/), and that does not harm retail pricing.

## When crossing networks are used

Institutional investors (funds, pensions, endowments) use crossing networks for multi-block trades, index rebalancing, and block execution. A large [merger arbitrage](/wiki/merger-arbitrage/) fund executing its winning side of an [arbitrage](/wiki/arbitrage-defi/) position might cross half the position internally and execute the remainder on the lit market, optimizing [execution quality](/wiki/execution-quality-analysis/).

<div class="wiki-seealso">

### Closely related
- [Dark Pool](/wiki/dark-pool/) — private matching with broader client base
- [Alternative Trading System](/wiki/alternative-trading-system/) — SEC-regulated off-exchange venues
- [Block Trading Platform](/wiki/block-trading-platform/) — specialized large-trade execution
- [Market Maker](/wiki/market-makers/) — liquidity providers on lit venues

### Wider context
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — cost of trading on public markets
- [Market Impact Cost](/wiki/market-impact-cost/) — price movement from order execution
- [High-Frequency Trading](/wiki/high-frequency-trading/) — predatory behavior in lit markets
- [Consolidated Tape](/wiki/consolidated-tape/) — real-time price reporting

</div>

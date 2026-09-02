---
title: "Order Routing Logic"
description: "Decision algorithm for directing orders to trading venues based on liquidity, cost, and speed requirements."
keywords:
  - order routing
  - execution algorithm
  - venue selection
  - trading venue
  - order flow
---

*An **order routing logic** is the decision framework that directs client orders to specific trading venues — exchanges, market makers, or alternative systems — based on liquidity availability, transaction cost, and speed. The routing system sits between the broker's order entry point and the ultimate execution venue, functioning as an intelligent traffic controller for financial orders.*

<aside class="wiki-infobox">

| Attribute | Detail |
|---|---|
| **Primary Purpose** | Minimize execution cost while meeting speed/liquidity constraints |
| **Decision Inputs** | Order size, stock liquidity, current bid-ask spread, rebates available |
| **Execution Venues** | Lit exchanges, dark pools, market makers, wholesale market |
| **Timing Horizon** | Milliseconds to seconds per routing decision |
| **Regulatory Framework** | SEC Reg NMS best-execution rules; FINRA Rule 5310 |
| **Risk Factor** | Poor routing → missed rebates, adverse pricing, information leakage |

</aside>

## Why order routing matters to total cost

Every order faces a choice at the moment it enters the broker's system: which venue(s) execute it? A [stock](/wiki/stock/) order routed to an exchange with $0.001 per-share rebates costs less than the same order sent to a [market maker](/wiki/market-makers/) paying no rebate, even if both venues show identical bid-ask [spreads](/wiki/bid-ask-spread/). Routing logic captures these economic differences and selects the path with the lowest expected [cost of execution](/wiki/cost-of-carry/).

The core tension: venues with better rebates often have less predictable liquidity. A broker must balance the certain cost saving against the risk that the order misses a partial fill and requires re-routing. [Alternative trading systems](/wiki/alternative-trading-system/) (ATS platforms, [dark pools](/wiki/dark-pools/)) may offer price improvement or reduced [market impact](/wiki/market-impact-cost/), but they lack the transparent [order book depth](/wiki/order-book-depth/) of a lit [exchange](/wiki/nasdaq/).

## Smart order routing algorithms and rebate arbitrage

Modern routing systems run as algorithms that split an incoming order across multiple venues in real time. The decision tree typically follows this sequence:

1. **Check available liquidity at each venue.** Query the most recent [market data](/wiki/market-data-feed-direct/) to see how many shares are offered at the best [bid and ask prices](/wiki/bid-ask-spread/).
2. **Calculate the effective cost of execution at each venue.** Execution price + fees — rebates = true cost.
3. **Rank by execution cost and predicted slippage.** A venue with a better rebate but thin liquidity might slippage an order more, offsetting the savings.
4. **Route the order to the cheapest valid venue.** The system submits the entire order or splits it if multiple venues have comparable advantage.

This is sometimes called **smart order routing** (SOR) or **dynamic venue selection**. Brokers compete on the quality of their routing logic, because a 0.5 basis points improvement in execution cost per trade compounds to millions of dollars annually across a large flow.

## Information leakage and the price of venue selection

Routing decisions reveal order flow patterns. If every time a large [mutual fund](/wiki/mutual-fund/) rebalances, orders consistently arrive at the same three [dark pools](/wiki/dark-pools/) in the same size, sophisticated traders can infer the fund's activity and trade ahead of it. This is a form of information leakage, reducing the fund's [execution quality](/wiki/execution-quality-analysis/).

Many brokers now randomize routing decisions slightly, or route large orders to multiple venues simultaneously (called *smart routing*), to obscure patterns. This trades off a small economic cost — the chance of splitting an order across venues with slightly worse prices — against protection from [front-running](/wiki/order-routing-logic/).

## Rebate structures and perverse incentives

Exchanges pay brokers cash rebates to send order flow, typically $0.0001 to $0.0005 per share. A routing algorithm might be "gamed" to overweight venues offering the highest rebate, even if a different venue is cheaper for the client overall. Regulation forbids this under [SEC best-execution rules](/wiki/best-execution/), but enforcement is uneven.

The economic tension is real: a broker's trading desk may route retail orders to venues paying rebates, while institutional clients get routed to different venues with better [price improvement](/wiki/price-improvement/) but no rebates. Both are technically compliant if the outcomes are demonstrably best for each client type, but the appearance of routing bias persists.

## Regulatory oversight and [Reg NMS](/wiki/reg-nms-detail/)

The SEC's Regulation NMS, enacted in 2006, established the [order protection rule](/wiki/reg-nms-adoption/): a broker cannot route an order to a venue if another venue is showing a better price. This rule eliminated many perverse routing incentives at the time.

However, [Reg NMS](/wiki/reg-nms-detail/) does not mandate a single venue; it permits routers to select among venues tied for the national best price. Brokers retain discretion to route orders to any venue with the best prevailing bid or ask, creating room for rebate-driven routing within the rule. The SEC's Office of Compliance Inspections and Examinations (OCIE) regularly audits broker routing practices but lacks the resources to examine all flows.

## Speed and latency as routing variables

In modern [high-frequency trading](/wiki/high-frequency-trading/), routing decisions happen in microseconds. Brokers maintain direct network connections to major exchanges, [dark pools](/wiki/dark-pools/), and [alternative trading systems](/wiki/alternative-trading-system/), and the routing algorithm selects the fastest path. A difference of 100 microseconds in routing latency can determine whether a [market maker](/wiki/market-makers/) can [hedge](/wiki/hedging-with-futures/) the filled order profitably.

This speed dimension means that routing logic now includes infrastructure decisions: colocation (data center placement), network provider, and exchange connectivity all affect which venue a router "sees" as cheapest in real time. Retail brokers typically use shared routing services from market data vendors, while institutional broker-dealers maintain proprietary routing systems.

## Cross-links and further reading

<div class="wiki-seealso">

### Closely related
- [Best Execution](/wiki/best-execution/) — regulatory requirement to achieve optimal terms for client orders
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — the cost difference that routing systems optimize around
- [Market Maker](/wiki/market-makers/) — counterparty that often receives routed orders
- [Dark Pool](/wiki/dark-pools/) — one type of execution venue routing systems select among

### Wider context
- [Algorithmic Trading](/wiki/algorithmic-trading/) — family of automated execution systems
- [Market Impact Cost](/wiki/market-impact-cost/) — total price degradation from order execution
- [Reg NMS Detail](/wiki/reg-nms-detail/) — regulatory framework constraining routing choices
- [Alternative Trading System](/wiki/alternative-trading-system/) — non-exchange venues brokers route to

</div>

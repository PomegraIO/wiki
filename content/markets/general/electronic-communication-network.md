---
title: "Electronic Communication Network"
description: "Systems that automatically match buy and sell orders directly between traders, bypassing traditional market makers."
keywords:
  - ecn
  - order matching
  - electronic trading
  - direct order routing
image: "/svg/markets.svg"
---

*An **electronic communication network** (ECN) is a computerised system that automatically executes trades by matching incoming buy and sell orders in real time, connecting traders directly without relying on a human market maker to intermediate. ECNs pioneered the shift away from traditional dealer-based markets by bringing retail traders into direct competition with institutional players, lowering spreads and democratising access to equity trading.*

## How ECNs match orders

At its core, an ECN maintains an electronic order book visible to all participants. When a trader submits a buy order, the system automatically searches for a matching sell order at the same price. If one exists, the trade executes instantly. If not, the buy order joins the queue waiting for a seller to arrive. This automated price-matching logic created something novel: small investors could now interact with institutional flow without the intermediary markup that traditional brokers imposed.

The architecture matters. Unlike a stock exchange that operates a single consolidated book, early ECNs operated parallel order books accessible only to their members. A trader's order might sit on one ECN whilst the best available price existed on another—a problem that later solutions like the [National Best Bid and Offer](/national-best-bid-offer/) would partially address.

## The retail revolution of the 1990s

ECNs emerged during the NASDAQ boom as upstart challengers to the dealer-controlled over-the-counter market. Systems like Instinet (founded 1969 but modernised in the 1990s), Island, and SelectNet allowed retail traders to place limit orders into a visible book alongside institutions. For the first time, a retail trader's order could execute against another retail trader's order without any dealer taking the other side—or taking a spread.

This democratisation compressed bid-ask spreads for active stocks. A penny stock on an ECN might have a tighter spread than the same stock on NASDAQ's traditional dealer network, because the liquidity came from direct supply and demand rather than dealer inventory management. Commissions fell as competition intensified.

## ECN pricing models

ECNs needed revenue. Some charged flat per-trade fees to both sides. Others adopted a rebate model: they paid a small rebate to traders who placed passive liquidity (a limit order that sat and waited to be hit), and charged a higher fee to the active side (a market order that hit that limit order). This rebate model incentivised traders to post orders rather than take, fragmenting liquidity further and laying groundwork for the maker-taker fee structure that dominates modern trading.

Still others charged subscription fees for market data access or priority routing. The fee structure choice had profound effects on which orders landed on which platform—a forerunner of today's [market fragmentation](/market-fragmentation/) problem.

## Integration with the broader market

Standalone ECNs worked best for highly liquid stocks. But traders needed to see all available liquidity across venues, not just their preferred ECN. Brokers began offering "smart order routing" that would split a large order across multiple venues to find the best execution. The trader's limit order on Island might execute partially, with the remainder auto-routed to SelectNet or NASDAQ.

The Regulation Fair Disclosure rules of 2000 and the subsequent shift toward decimalisation (from sixteenths to cents in 2001) reshaped the ECN landscape. Smaller spreads meant the rebate model became more important as a revenue source. Brokers began capturing more of the spreads through order routing logic rather than passing them fully to the trader.

## Consolidation and evolution

By the early 2000s, ECNs either merged with larger exchanges or were acquired by them. Island was bought by NASDAQ. Instinet eventually became a dark pool platform. The pure ECN model—an automated matching engine with no market-maker fallback—became less distinct as exchanges themselves adopted electronic matching as their primary function.

Modern exchanges like the NYSE operate ECN-like systems at their core, automatically matching orders on their own books. What once made an ECN revolutionary—automated matching without human intermediation—is now simply how equity markets work. The legacy lies in the structural shift ECNs forced: from dealer-centric to order-driven, and from opaque to transparent order books.

## See also

<div class="wiki-seealso">

### Closely related

- [National Best Bid and Offer](/national-best-bid-offer/) — the consolidated quote requirement that forced ECNs to compete on a visible price level
- [Over-the-Counter Market](/over-the-counter-market/) — the dealer-based system ECNs displaced
- [Alternative Trading System](/alternative-trading-system/) — the regulatory category that evolved to encompass ECNs and dark pools
- [Market Fragmentation](/market-fragmentation/) — the structural consequence of multiple competing venues
- [Price Discovery](/price-discovery/) — how transparent order books improved price formation
- [Stock Exchange](/stock-exchange/) — the regulated venue that adopted ECN-style matching
- [Broker](/broker/) — firms that route orders to ECNs and execute trades

### Wider context

- [Market Maker Trading](/market-maker-trading/) — the dealer role ECNs bypassed
- [NASDAQ](/nasdaq/) — the electronic exchange where ECNs first challenged dealer dominance
- [Bid-Ask Spread](/bid-ask-spread/) — the compression that ECNs delivered to retail traders

</div>

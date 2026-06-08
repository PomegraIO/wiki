---
title: "Payment for Order Flow Mechanics"
description: "Payment for order flow is compensation a market maker pays a broker for retail order routing rights. The broker profits; the market maker gains order predictability. Execution quality may suffer."
keywords:
  - payment for order flow
  - how payment for order flow works
  - order routing incentive
  - broker market maker deal
  - retail order handling
  - rebate structure
  - hidden conflicts
---

*A **payment for order flow** (PFOF) arrangement is a contract where a broker-dealer routes its customers' orders to a specific [market maker](/market-maker-trading/) in exchange for a cash rebate per share. The broker profits immediately; the market maker gains a stream of retail orders, often predictable and easy to execute against. Critics argue that this creates a conflict: the broker is paid to send orders to a specific venue, which may not offer the best execution price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Payment for Order Flow — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Brokers trade order routing for rebates; retail investors don't see the cash.</div>

|   |   |
|---|---|
| **Who pays** | Market makers (citadel, virtu, jane street, etc.) |
| **Who receives** | Brokers (robinhood, charles schwab, fidelity, etc.) |
| **Amount** | 0.001–0.005 per share, or $0.10–$0.50 per 100-share order |
| **Order type** | Mostly retail equities and [options](/option/) |
| **Conflict of interest** | Broker incentivized to route to PFOF provider, not best price |
| **Disclosure** | Quarterly routing reports; not always prominent |
| **History** | Became standard in 1990s; grew as retail trading surged |

</aside>

## The basic deal

Here's how it works at its simplest. You decide to buy 100 shares of Apple at market price. Your broker, say Robinhood, receives your order. Rather than sending it to the [NYSE](/new-york-stock-exchange/) or [NASDAQ](/nasdaq/), Robinhood routes it to Citadel Securities, a major market maker. Citadel executes your order against its own inventory and pays Robinhood $0.002 per share (or $0.20 for your 100 shares).

From Robinhood's perspective, this is a free lunch. The company doesn't charge you a commission—it's already abolished them to compete—so this rebate is pure revenue. If Robinhood routes a million shares a day to Citadel, that's $2,000 a day in PFOF revenue, with no cost to the broker. Robinhood's business model depends on this flow.

Citadel, meanwhile, gains a massive order stream. These are mostly small retail orders: predictable, low-information, often late arrivals to a move that institutional traders spotted hours earlier. Citadel can profit by executing your order, then hedging its inventory on the lit exchange at a better price. Over millions of orders, this spread is free money.

## Execution price vs. rebate incentive

The conflict emerges here: **Robinhood is paid to route your order to Citadel, not to seek the best available price for you.**

Imagine Apple is trading on the NYSE at a bid of $150.00 and an ask of $150.01. That's a penny spread. Your market buy order would ordinarily fill at $150.01. But Citadel, as part of its PFOF arrangement, might quote $150.02—one penny wider. Robinhood still routes to Citadel because the $0.002-per-share rebate ($0.20 on your order) exceeds the cost of that extra penny ($0.01 × 100 = $1.00).

Wait—you lose $1.00, Robinhood makes $0.20. That's a bad trade for you. But Robinhood's incentives point elsewhere. Citadel is a reliable source of rebates; the NYSE is not. If Robinhood sent all retail orders to the NYSE, it would earn zero PFOF revenue and would face pressure to raise commissions or accept lower profit.

Over time, this leads to persistent execution leakage: retail orders, on average, fill at slightly worse prices than they would if brokers routed purely for best execution. The SEC has tried to police this with "best execution" rules, requiring brokers to show that their routing is fair, but the rules are complex and enforcement is sporadic.

## How much is the rebate?

Typical PFOF ranges from **$0.001 to $0.005 per share**. On a 100-share order, that's $0.10 to $0.50 per trade. The exact rate depends on:

- **Order size**: Smaller orders (under 1,000 shares) often command higher rebates per share because they're harder to hedge.
- **Volatility**: During calm markets, rebates are stable. In volatile periods, market makers demand higher rebates to compensate for hedging risk.
- **Stock liquidity**: Highly liquid stocks (large cap) have tighter spreads and lower PFOF. Less liquid stocks carry higher rebates.
- **Order type**: [Limit orders](/limit-order/) sometimes get rebates; market orders often do. Options PFOF is sometimes higher than equities.

Some brokers publish their PFOF rates; others keep them opaque. Citadel, Virtu Financial, Jane Street, and a handful of others dominate the market maker side. A few brokers, notably Fidelity and Charles Schwab, have partially opted out of PFOF for some account types, claiming to route to better prices instead. This is a competitive edge in the zero-commission era.

## The broader ecosystem

PFOF became entrenched in the 1990s when the SEC required brokers to disclose best execution and routing practices. Rather than risk regulatory challenge, many brokers formalized their market maker relationships into PFOF contracts. As retail investing exploded (especially post-2020), PFOF volume surged. Today, PFOF accounts for a significant share of retail order flow.

The model benefits three groups:
1. **Brokers** earn PFOF rebates instead of commissions.
2. **Market makers** get order flow and profit from execution.
3. **Some retail traders** benefit from commission-free trading.

It harms:
1. **Retail traders** who receive worse prices on average.
2. **Institutional traders** whose orders, routed to lit exchanges, compete against market-maker-filled retail orders.

## Regulatory scrutiny and alternatives

The SEC has scrutinized PFOF for decades. In 2020, the agency opened an investigation into whether PFOF violates best-execution rules. The scrutiny intensified after the 2021 GameStop/Meme Stock event, when Robinhood's PFOF relationships (and Citadel's role as both a market maker and Robinhood investor) drew congressional attention.

Some proposals have emerged:
- **Auction-based routing**: Brokers send each order to the market maker offering the best price in real time, not to a contracted counterparty.
- **PFOF caps**: Regulators could cap PFOF rates to reduce the incentive to route away from lit venues.
- **Transparency mandates**: Brokers could be required to publish actual execution prices vs. NBBO (best available bid/ask) for every retail order.

Few of these have become law. The SEC has hinted at stricter oversight, but regulatory momentum is slow. Meanwhile, brokers and market makers continue to profit.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker Trading](/market-maker-trading/) — The counterparty in PFOF arrangements and how they profit
- [Best Execution](/best-execution/) — The regulatory principle that PFOF can conflict with
- [Bid-Ask Spread](/bid-ask-spread/) — The gap PFOF can widen for retail orders
- Order Routing — How brokers decide where to send orders
- [Dark Pool vs Lit Exchange](/dark-pool-versus-lit-exchange/) — Off-exchange venues where PFOF also occurs
- [How Trade Matching Engines Work](/how-trade-matching-engines-work/) — The mechanics PFOF routing bypasses

### Wider context

- [Broker](/broker/) — The intermediary collecting PFOF revenue
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The regulator overseeing PFOF disclosures
- [Market Microstructure](/market-microstructure/) — The broader field studying order routing and execution quality
- Zero-Commission Trading — The trend that made PFOF the primary broker revenue model

</div>

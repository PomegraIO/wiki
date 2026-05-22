---
title: "Electronic Communication Network Market"
description: "Decentralized trading system matching buyers and sellers electronically without traditional centralized exchange infrastructure."
keywords:
  - ecn market
  - electronic communication network
  - decentralized trading
  - alternative trading system
---

*An Electronic Communication Network (ECN) is a computerized system that matches buy and sell orders from traders and investors electronically, without the intermediation of a traditional [broker](/wiki/broker/) or [market maker](/wiki/market-makers/). The ECN displays an order book (bids and asks) and executes trades at the best available prices, operating as an alternative to centralized exchanges like the [NYSE](/wiki/new-york-stock-exchange/) or [NASDAQ](/wiki/nasdaq/).*

<aside class="wiki-infobox">

| Feature | Detail |
|---|---|
| **Market Structure** | Decentralized order matching |
| **Participants** | Retail traders, [institutional investors](/wiki/qualified-institutional-buyer/), [market makers](/wiki/market-makers/) |
| **Order Types** | [Limit orders](/wiki/limit-order/), [market orders](/wiki/market-order/), [stop-loss](/wiki/stop-order/), [iceberg orders](/wiki/iceberg-order/) |
| **Price Discovery** | Real-time order book; prices set by supply/demand matching |
| **Regulation** | [SEC](/wiki/securities-and-exchange-commission/) oversight as [Alternative Trading Systems (ATS)](/wiki/alternative-trading-system/) |
| **Fees** | Varies: maker-taker, per-share, or subscription |
| **Transparency** | Full order-book visibility to participants |
| **Notable Examples** | Instinet, ARCA (now Nasdaq OMX ArcaEdge), BATS (now Cboe) |
| **Market Share (US equities)** | ~30-40% of total equity volume |

</aside>

## How ECNs challenged the exchange monopoly

Before the 1990s, stock exchanges like the [NYSE](/wiki/new-york-stock-exchange/) and [NASDAQ](/wiki/nasdaq/) were the only venues for trading. Trading was fragmented: you called a [broker](/wiki/broker/), the broker called a specialist or [market maker](/wiki/market-makers/), and trades were executed on the exchange floor. This was slow, opaque, and expensive (wide [spreads](/wiki/bid-ask-spread/)).

ECNs disrupted this. Instinet (founded 1969) was the first large ECN, allowing institutional traders to execute against each other electronically without going through an exchange. By the 1990s, as retail internet trading exploded, ECNs became critical infrastructure: they offered faster execution, tighter [spreads](/wiki/bid-ask-spread/), and transparent order books.

The [Securities and Exchange Commission](/wiki/securities-and-exchange-commission/) recognized ECNs as [Alternative Trading Systems (ATS)](/wiki/alternative-trading-system/) under Regulation ATS (adopted 1998), giving them quasi-official status while imposing regulatory requirements. Today, ECNs execute roughly 30-40% of US equity volume, with the remainder split between the [NYSE](/wiki/new-york-stock-exchange/), [NASDAQ](/wiki/nasdaq/), and other venues.

## Order matching and price formation in an ECN

An ECN maintains a real-time order book (visible to all participants) showing all bids and asks. When a buy order arrives, the system automatically matches it with the best available sell order and executes instantly at that price. If no matching sell order exists, the buy order is added to the book and waits for a seller.

Example: The ECN's order book shows:
```
Bids            Asks
$100.05 (500)   $100.10 (300)
$100.03 (200)   $100.12 (500)
$100.00 (100)   $100.15 (200)
```

A new sell order for 400 shares arrives. The ECN matches 300 shares at $100.05 (the best bid) and adds the remaining 100 shares to the order book as a new ask at $100.10 (or a lower price if specified by the order).

This transparent, automated matching is the core innovation of ECNs. There is no [market maker](/wiki/market-makers/) extracting a spread; instead, prices are set by genuine supply and demand, and [spreads](/wiki/bid-ask-spread/) reflect the true liquidity available.

## Regulation and the SEC framework

ECNs must register with the [SEC](/wiki/securities-and-exchange-commission/) as [Alternative Trading Systems (ATS)](/wiki/alternative-trading-system/) and comply with Regulation ATS. Key requirements:

1. **Transparency**: ECNs must display the best bids and asks to all market participants in real-time ([best bid and offer - NBBO](/wiki/nbbo/)).
2. **Order routing**: ECNs must have procedures to route orders to other venues if better prices are available ([best execution](/wiki/best-execution/)).
3. **Fair access**: ECNs must provide fair, non-discriminatory access to all eligible traders.
4. **Surveillance**: ECNs must monitor for manipulation, wash trading, and insider trading.

These rules level the playing field between ECNs and traditional exchanges, though exchanges retain a few regulatory advantages (e.g., they can impose stricter listing standards and have self-regulatory authority).

## Maker-taker fee models and economic incentives

Many ECNs use "maker-taker" fee models:
- **Makers** (traders who add liquidity by placing orders that sit in the book) receive a rebate (e.g., -$0.0005 per share, meaning they earn money for supplying liquidity).
- **Takers** (traders who execute against existing orders) pay a fee (e.g., +$0.001 per share).

This incentive structure encourages traders to post resting orders, building "depth" in the order book. Larger order books mean tighter [spreads](/wiki/bid-ask-spread/) and better execution for everyone.

Critics argue maker-taker models create perverse incentives: traders optimize for rebates rather than genuine trading. They also can discriminate among order types, providing bigger rebates for certain traders or strategies, creating hidden conflicts of interest.

## ECN competition and consolidation

The ECN market has consolidated significantly:
- **Instinet** (founded 1969) was acquired by Nomura in 2010 and is now part of Nomura's institutional trading platform.
- **ARCA** (Electronic Communications Exchange, later Archipelago Group) was acquired by Nasdaq in 2005 and operates as Nasdaq OMX ArcaEdge.
- **BATS** (Better Alternative Trading System, founded 2005) grew rapidly and was acquired by Cboe (formerly CBOE) in 2017, operating as Cboe BZX and Cboe BYX.
- **Direct Edge** merged with Bats in 2013.

Today, the major ECN/ATS players in US equity markets are:
- NASDAQ (including ARCA, various proprietary venues)
- Cboe (including BATS BZX, BYX)
- Instinet (Nomura)
- UBS ATS
- Various smaller dark pools and internalizers

## Dark pools, lit venues, and market fragmentation

Not all ECNs are "lit" (displaying prices publicly). **Dark pools** are ECNs that do not publish real-time order books; instead, orders are matched anonymously against internal liquidity. Dark pools offer:
- **Privacy**: Large orders are not visible to competitors.
- **Lower [market impact](/wiki/market-impact-cost/)**: Orders don't move prices as much.

But dark pools also:
- **Reduce price discovery**: Prices in dark pools are not visible to the broader market.
- **Enable predatory trading**: Unscrupulous traders can use dark-pool order flow to profit at the expense of other participants.

The rise of dark pools (now ~15% of US equity volume) has fragmented the market: prices for the same [security](/wiki/securities-and-exchange-commission/) can differ across lit venues and dark pools. The SEC's [Regulation SHO](/wiki/regulation-sho/) and recent proposals (e.g., to restrict dark-pool order flow) attempt to rein in fragmentation.

## Speed and latency: the technology arms race

ECNs operate at microsecond speeds, executing millions of trades per second. This high speed has enabled algorithmic and [high-frequency trading](/wiki/high-frequency-trading/). But it has also created a technology arms race where firms invest billions in low-latency infrastructure ([colocations](/wiki/colocation-detail/), fiber-optic cables, optimized algorithms) to gain fractions-of-a-microsecond advantages.

This speed advantage is controversial. Supporters argue it reduces [spreads](/wiki/bid-ask-spread/) and improves liquidity. Critics argue it enables predatory "front-running" strategies and advantages wealthy firms that can afford advanced technology.

## ECNs in other asset classes

While ECNs originated in equities, they have expanded to other markets:
- **[Forex](/wiki/forex-leverage/)**: [Forex ECNs](/wiki/crossing-network/) like eSpeed, Hotspot, and FXall match [currency](/wiki/currency-pair/) orders from [banks](/wiki/bank-reserve-injection/) and hedge funds.
- **[Crypto](/wiki/cryptocurrency-exchange/)**: [Decentralized exchanges (DEXs)](/wiki/decentralized-exchange/) like Uniswap, SushiSwap, and Curve are ECNs for crypto assets, using [automated market makers (AMMs)](/wiki/automated-market-maker/) instead of traditional order matching.
- **[Derivatives](/wiki/derivatives-exchange-crypto/)**: Some [futures](/wiki/futures-contract/) and options trading occurs on ECNs, though larger volumes are on regulated exchanges.

## Systemic risks and circuit breakers

The speed and fragmentation of ECN-driven markets created systemic risks, exposed during the May 6, 2010 "Flash Crash." On that day, a large sell order triggered a cascade of algorithmic sell orders across ECNs and exchanges, causing the S&P 500 to fall 9% in minutes. Circuit breakers (automatic trading halts at -7%, -13%, -20% daily declines) were implemented post-crash to prevent similar incidents.

ECNs and traditional exchanges now coordinate circuit breaker halts, and regulators monitor for manipulation across all venues. These safeguards have reduced (but not eliminated) systemic flash-crash risks.

## Conclusion: ECNs as infrastructure, not destination

ECNs have become infrastructure—like utilities—underlying modern markets. They are not destinations for retail traders (most retail investors use brokers, who route to ECNs and exchanges) but rather the plumbing through which prices are discovered and trades executed. The ongoing competition between ECNs, exchanges, dark pools, and [broker-dealers](/wiki/broker/) using internalization drives continuous innovation in speed, pricing, and order types, benefiting final investors through tighter [spreads](/wiki/bid-ask-spread/) and better execution.

<div class="wiki-seealso">

### Closely related
- [Alternative trading system](/wiki/alternative-trading-system/) — Regulatory classification for ECNs
- [Order book](/wiki/order-book-depth/) — Display of bids and asks
- [NBBO](/wiki/nbbo/) — National Best Bid and Offer
- [Dark pool](/wiki/dark-pool/) — Non-lit ECN variant

### Wider context
- [Stock exchange](/wiki/stock-exchange/) — Centralized trading venues
- [Market microstructure](/wiki/market-impact-cost/) — Mechanics of order matching and pricing
- [High-frequency trading](/wiki/high-frequency-trading/) — Ultra-fast algorithmic trading leveraging ECNs
- [Best execution](/wiki/best-execution/) — Regulatory obligation to route orders for optimal prices

</div>

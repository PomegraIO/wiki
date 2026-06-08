---
title: "Effective Spread"
description: "The realized cost to a trade taker, measured as twice the distance between execution price and the midpoint of the quoted bid-ask spread."
keywords:
  - effective spread
  - trading costs
  - bid-ask spread
  - market taker cost
  - price execution
image: "/svg/trading.svg"
---

*The **effective spread** measures what a trade taker actually pays, capturing both the quoted bid-ask gap and any price movement before the trade fills. It is calculated as twice the distance between the execution price and the midpoint of the quoted spread—a standard metric for assessing execution quality and total trading friction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Effective Spread — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and costs." />

<div class="wiki-infobox-caption">The tangible cost paid when a taker hits a bid or lifts an ask.</div>

|   |   |
|---|---|
| **What it is** | Twice the distance between trade price and quote midpoint |
| **Who bears it** | Passive liquidity takers (buyers lifting asks, sellers hitting bids) |
| **Core formula** | For a buy: (execution price − midpoint) × 2 |
| **Also called** | Realized execution cost, taker cost |
| **Measured in** | Basis points (bps) or cents per share |
| **Why it matters** | Reveals true friction; bid-ask alone understates the taker's expense |

</aside>

## Why the quoted spread is just the start

When a trader places a market order to buy, she typically pays the ask price—the price at which a seller is willing to transact. The [bid-ask spread](/bid-ask-spread/) is the difference between the best bid and best ask. But the effective spread goes deeper. It captures not only the static spread at the moment the order arrives, but also any adverse movement in the midpoint between the time the quote was posted and the moment the trade executed.

Consider a stock quoted 50.00 bid / 50.05 ask (a 5-cent spread). The midpoint is 50.025. A trader who sends a market buy order and gets filled at 50.05 pays an effective spread of (50.05 − 50.025) × 2 = 0.05 cents—exactly the quoted spread. But if the stock ticks up to 50.10 / 50.15 before her order reaches the exchange, and she fills at 50.15, her effective spread balloons to (50.15 − 50.125) × 2 = 0.05, measured against the new midpoint. The doubling reflects the two-way friction: she paid the ask, and the midpoint moved against her.

## The doubling convention explained

The multiplication by two deserves clarity. The effective spread is defined symmetrically: it treats a buy at the ask and a sell at the bid as equivalent "unfavorable" fills. When a buyer pays the ask, she is 50% of the quoted spread away from the midpoint on her own side. Multiplying by two normalizes this so the metric reflects the true round-trip cost—what the taker loses to market makers and price adverse movement combined.

In practice, this means an effective spread of 10 basis points on a $100 stock amounts to a $0.10 cost per share. For a $1 million order, that is $1,000 in realized friction.

## How it differs from quoted spread

The [bid-ask spread](/bid-ask-spread/) reported on an exchange is static—it is the gap visible in the order book at a single instant. The effective spread is dynamic and backward-looking; it measures what actually happened. A taker who waits for a moment when the spread widens, or whose order arrives in a news event that moves the midpoint, will see a larger effective spread than the nominal quote.

Conversely, a taker who executes in a highly liquid moment might get filled inside the quoted spread—a "price improvement"—giving a negative effective spread. This is rare but does occur during market maker competition or when a broker internalizes orders and fills them better than the national best bid and ask.

## Who measures and why

Broker-dealers and regulators use effective spread to audit execution quality. The [Securities and Exchange Commission](/securities-and-exchange-commission/) requires periodic disclosure of trade execution data, including effective spreads, so that investors can compare brokers. A broker advertising "tight spreads" might quote a 1-cent spread, but if fills consistently come 2 cents away from midpoint, the effective spread tells the true story.

[Market makers](/market-maker-trading/) also track effective spread as a proxy for their profitability on small orders. If a [market maker](/market-maker-trading/) receives an order to buy 100 shares at the ask, and the stock has moved higher by the time she can hedge her position, her realized effective spread is narrower than the spread she originally quoted. This is why [realized spread](/realized-spread/) is a more nuanced measure of what a market maker truly earns.

## The link to execution quality

Effective spread is one of three pillars in execution quality. The others are price improvement (how much better than the national best bid or ask a trader actually receives) and speed (latency of fill). A broker-dealer that claims low effective spreads but takes weeks to fill orders is not delivering good execution overall.

For retail traders using a [broker](/broker/) with a trading desk, effective spread is usually invisible—the client sees only the final price. But for institutional investors sending large orders through electronic venues or to multiple [market makers](/market-maker-trading/), understanding effective spread is essential to managing costs. Some traders deliberately split orders across venues to reduce effective spread by diversifying [counterparty risk](/counterparty-risk/) and taking advantage of regional liquidity pockets.

## Interpreting effective spread in context

A 5-cent effective spread on a liquid large-cap stock is poor; 1 cent is excellent. On a thinly traded microcap, 50 cents is routine. Effective spread widens during earnings announcements, earnings season, and periods of elevated [implied volatility](/implied-volatility/). It also depends on order size—a 10-million-share order will show a much wider effective spread than a 100-share order, because the taker is moving the market.

Time of day matters too. Effective spreads are tightest during the first hour after open and the last hour before close, when volume is highest. Mid-morning often sees a softening in spreads as opening momentum fades.

## The cost cascade

For a retail trader placing a $5,000 order in a moderately liquid stock, an effective spread of 10 basis points means a $5 cost that never appears as a line item on the confirmation. This is why cumulative trading friction—effective spread plus [market impact](/bid-ask-spread/), slippage, and [commissions](/brokerage-commission-structure/)—can dwarf apparent fee schedules. Over a thousand trades, seemingly tiny per-trade costs compound into a major drag on returns.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the static gap between best buy and sell prices
- [Realized spread](/realized-spread/) — the spread revenue a market maker captures after adverse price movement
- [Market maker trading](/market-maker-trading/) — how firms profit from the bid-ask spread
- [Brokerage commission structure](/brokerage-commission-structure/) — how brokers charge for execution
- [Exchange fee schedule](/exchange-fee-schedule/) — taker and maker fees charged by venues

### Wider context

- [Stock market](/stock-market/) — the exchange ecosystem where these costs occur
- [Price discovery](/price-discovery/) — how spreads relate to efficient pricing
- [Liquidity risk](/liquidity-risk/) — why spreads widen when liquidity evaporates
- [Counterparty risk](/counterparty-risk/) — the risk faced by traders and market makers

</div>

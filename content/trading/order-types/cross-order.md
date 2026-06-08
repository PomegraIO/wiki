---
title: "Cross Order"
description: "A broker-matched transaction pairing a buy order from one client with a sell order from another at a mutually agreed price."
keywords:
  - cross order
  - broker crossing
  - internal match
  - block trading
  - execution efficiency
image: "/svg/trading.svg"
---

*A **cross order** is a securities transaction in which a broker internally matches a buy order from one client with a sell order from another client, executing both sides at an agreed-upon price without routing the orders to an external exchange or market. The broker acts as an intermediary and often principal, facilitating the trade and taking on any residual risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">The broker brings together willing buyer and seller.</div>

|   |   |
|---|---|
| **What it is** | A broker-facilitated internal match of a buy and sell order at an agreed price |
| **Also called** | Crossing order, internal cross, broker cross, principal trade |
| **Parties involved** | Broker (intermediary/principal) and two clients (buyer and seller) |
| **Price determination** | Typically at the mid-point or at a negotiated level |
| **Execution venue** | Inside the broker; not routed to an exchange or [alternative trading system](/alternative-trading-system/) |
| **Regulatory oversight** | Must comply with best-execution rules and disclosure requirements |

</aside>

## The mechanics of matching buy and sell

A cross order arises when a broker has simultaneous or near-simultaneous buy and sell orders for the same security from different clients and identifies an opportunity to match them internally. Instead of routing the buy order to an exchange and the sell order to another venue—incurring routing costs and market impact—the broker crosses the orders internally at a single price.

The price is typically set at or near the mid-point of the current market [bid-ask spread](/bid-ask-spread/), or at a price negotiated between the broker and the clients. For example, if XYZ stock is trading with a bid of 49.50 dollars and an ask of 49.60 dollars, and the broker has a buy order for 1,000 shares at 49.55 dollars and a sell order for 1,000 shares at 49.55 dollars, the broker can cross both sides at that price, completing the transaction without touching an external market.

From the clients' perspectives, this is advantageous: the buyer avoids paying the ask price, the seller avoids accepting the bid price, and both benefit from execution at a fairer level. The broker benefits from executing both sides in a single transaction, capturing the "middle" profit (the spread) without the operational cost of dual routing.

## How crosses fit into the broader trading ecosystem

Broker crosses occupy a specific niche in the trading landscape. They are distinct from **exchange-based matching**, where a [market maker](/market-maker-trading/) or algorithms match buyers and sellers at the exchange level in real time. They are also distinct from **negotiated trades** over the [over-the-counter market](/over-the-counter-market/), where counterparties directly haggle on price.

Instead, a cross is a hybrid: the broker has the information that two clients want to trade in opposite directions, and uses that information to facilitate a transaction. The key advantage over exchange routing is **cost and speed**. A cross order can be executed in milliseconds, without delay or market impact, whereas routing to an exchange and waiting for matching can be slower or result in slippage if prices move.

Crosses are especially valuable in **illiquid or after-hours trading**, where the [bid-ask spread](/bid-ask-spread/) is wide and natural exchange liquidity is sparse. A broker holding both sides of a cross can execute with certainty and precision, whereas attempting to work both sides on the open market might push prices against the clients or result in only a partial fill.

## Legal and regulatory constraints

Cross orders are regulated in most jurisdictions because they pose potential conflicts of interest. If a broker crosses orders, the broker knows prices and quantities on both sides; this information asymmetry could theoretically be exploited. Additionally, a client might object if the price offered in a cross is worse than the current market price, reasoning that the broker should have routed the order to an exchange for a better fill.

In the United States, SEC Rule 10b-1(a), sometimes called the "cross rule," permits brokers to cross orders only under specific conditions:
- **Best execution**: The cross price must be at or better than the current market [best bid and offer](/bid-ask-spread/). If the market is trading at 49.50 bid / 49.60 ask, the cross cannot occur at 49.50 or worse.
- **Disclosure**: The client must be informed that the order was crossed internally and at what price.
- **Non-distortive**: The cross cannot create a false appearance of trading activity or volume. Broker crosses are typically reported to the exchange under specific codes.

Additionally, FINRA Rule 5320 requires brokers to provide best execution, and cross orders are evaluated under that standard. If a client's order could have received a better price on an exchange, routing the order instead of crossing it may violate best-execution obligations.

In some jurisdictions outside the US (e.g., the UK, EU), crosses are explicitly permitted under market conduct rules but are subject to pre-trade and post-trade transparency requirements that vary by market structure.

## Types and motivations for crosses

**Block crosses** are the most common form. An institutional investor wants to buy or sell a large position, and the broker has other institutional clients with opposite interests. Rather than execute both orders through a block trading desk or via negotiation, the broker can facilitate an internal cross at a fair price, reducing market impact and transaction costs for all parties.

**Algorithmic crosses** use matching engines to continuously search for cross opportunities as orders arrive throughout the day. Many brokers operate internal crossing networks (sometimes called dark pools or crossing venues) where client orders are automatically matched when prices align.

**Facilitated crosses** are negotiated by brokers who act as intermediaries between two clients. The broker identifies that one client wants to sell 50,000 shares and another wants to buy that quantity, then proposes a price and facilitates the transaction. This is common in block trading and can occur over the phone or via a trading system.

**Principal crosses** occur when the broker is not merely matching two clients but is using the broker's own capital to take one side of the cross. For example, the broker might cross a client's buy order with an internal inventory position, buying from that inventory and crossing it with the client. This creates additional profit for the broker but also requires the broker to properly disclose the principal nature of the trade.

## Market impact and competitive advantages

From a client's perspective, a cross offers protection against market impact. When a trader wants to buy 100,000 shares of an illiquid name, routing that order to the market might move the price 0.50 dollars or more. A broker cross, if one is available, might eliminate that impact entirely and execute at a single, predictable price.

This advantage is largest in **less liquid securities** and **after-hours trading**. In highly liquid markets (large-cap stocks trading on major exchanges), the advantage is smaller, since exchange liquidity is abundant and spreads are tight. A client might be indifferent between a cross at 49.55 dollars and an exchange execution at 49.55 dollars; the real difference appears when market impact is significant.

## Potential drawbacks and conflicts

The main risk is **information asymmetry**. A broker crossing orders knows the quantity, direction, and urgency of both sides. If the broker uses this information to front-run the orders (e.g., taking a principal position before executing the cross) or to incentivize one side to trade more, the client could be harmed.

Regulators monitor for these abuses. Brokers are prohibited from sharing information about pending client orders with other market participants, and they cannot use cross order information for proprietary trading.

Another drawback: **limited price improvement**. If a cross occurs at the mid-point, one client (typically the buyer) has paid more than the bid, and the other (the seller) has received less than the ask. In a tight, liquid market, this might cost them more than an exchange execution would. Clients are entitled to best execution, and a cross that does not meet that standard should not be executed.

## The future of crosses in modern markets

The rise of [alternative trading systems](/alternative-trading-system/) and dark pools has fragmented where crosses can occur. Some brokers operate ATS venues explicitly designed to match orders from their clients; others route crosses to external crossing networks operated by third parties.

Regulatory scrutiny has also increased. The SEC and FINRA have periodically examined whether brokers are properly evaluating cross execution against external market alternatives and whether clients are being offered the option to decline a cross in favour of exchange routing.

For individual investors, crosses are largely transparent—they occur inside a broker's system and are reported post-trade. Institutional traders, by contrast, often explicitly request cross capability from brokers and monitor the terms under which crosses are permitted.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — immediate execution at best available prices
- [Limit Order](/limit-order/) — execution only at a specified price or better
- [Bid-Ask Spread](/bid-ask-spread/) — the difference between buy and sell prices that crosses can reduce
- [Market Maker Trading](/market-maker-trading/) — how dealers provide liquidity and compete with crosses
- [Not-Held Order](/not-held-order/) — discretionary order allowing broker flexibility in execution
- Block Trading — large institutional trades where crosses are common

### Wider context

- [Alternative Trading System](/alternative-trading-system/) — venues where crosses can be matched
- [Over-the-Counter Market](/over-the-counter-market/) — negotiated trades distinct from crosses
- [Price Discovery](/price-discovery/) — how crosses contribute to or bypass price-finding
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of cross order rules and best execution

</div>

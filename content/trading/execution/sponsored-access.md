---
title: "Sponsored Access"
description: "Arrangement where a broker grants a third party its exchange membership credentials to submit orders directly, bypassing the broker's risk and compliance infrastructure."
keywords:
  - sponsored access
  - direct market access
  - order routing
  - exchange membership
  - algorithmic trading
  - market access
image: "/svg/trading.svg"
---

*In **sponsored access** (SA), a [broker](/broker/) that holds exchange membership allows a client—typically a trading firm, hedge fund, or quantitative trader—to use the broker's exchange seat or credentials to submit orders directly to the exchange. The sponsor broker monitors risk and compliance but does not process every order, allowing the client to execute with minimal latency and direct market connection.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sponsored Access — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and execution." />

<div class="wiki-infobox-caption">Trader submits orders directly to the exchange using the broker's seat; sponsor monitors risk.</div>

|   |   |
|---|---|
| **What it is** | Broker grants client direct exchange access via sponsor's membership |
| **Alternative** | Traditional order routing through broker's systems (slower, higher latency) |
| **Direct access level** | Client's algorithms connect directly to exchange gateway |
| **Risk monitoring** | Sponsor broker maintains pre-trade and post-trade risk controls |
| **Client benefit** | Lower latency, faster order submission, less broker intermediation |
| **Sponsor benefit** | Order flow, sponsorship fees, interest in client success |
| **Regulation** | SEC Rule 15c3-5, FINRA Rule 4511; limited to qualified clients |
| **Risk** | Rogue trading, risk-limit breach, market volatility amplification |

</aside>

## How sponsored access works

In traditional order execution, a trader sends an order to a [broker](/broker/), which validates it, routes it to the exchange, and reports the fill. This process incurs latency—the time between order submission and execution—typically 50–500 milliseconds depending on infrastructure and network distance.

Sponsored access eliminates the broker's middle step. The [broker](/broker/) grants the client a direct connection to the exchange's order entry gateway, authenticated using the broker's exchange member identifier and a set of API credentials. The client's trading system (often a proprietary algorithm or [algorithmic trading](/algorithmic-trading/) platform) sends orders directly to the exchange, bypassing the broker's order management system (OMS). The exchange executes the order at the limit price and returns the execution immediately.

The sponsor broker, however, does not cede all control. Real-time risk filters remain in place: the sponsor monitors the client's open positions, cumulative notional exposure, and daily loss limits. If the client breaches these thresholds, the sponsor's risk system can throttle or reject new orders. This arrangement allows ultrafast execution while maintaining the sponsor's fiduciary and regulatory responsibility.

## Speed as competitive advantage

For [algorithmic traders](/algorithmic-trading/), [market makers](/market-maker-trading/), and quantitative firms, latency—measured in milliseconds—translates directly to profitability. A trader using sponsored access can detect a price movement and execute an order in 2–5 milliseconds; the same trader using traditional routing might face 50–200 milliseconds of latency. Over thousands of orders per day, this difference compounds significantly.

[Algorithmic trading](/algorithmic-trading/) strategies that rely on price signals (mean reversion, momentum, [arbitrage](/alternative-trading-system/)) are especially sensitive to latency. A statistical [arbitrage](/alternative-trading-system/) strategy that detects a mispricing must execute within milliseconds before the market corrects it; a delayed execution may miss the profit window entirely. For market makers, lower latency means they can adjust their quotes faster in response to incoming information, reducing inventory risk.

Sponsored access democratizes this speed advantage to clients of brokers that offer it. Without SA, only the broker itself (trading its own account or high-volume clients it serves directly) would have the speed benefit. SA allows smaller, nimble trading firms and sophisticated hedge funds to compete on latency without building their own exchange membership or collocating servers at multiple exchanges.

## Types of sponsored access

The SEC and FINRA distinguish two models:

**Fully-disclosed sponsored access**: The client's identity is known to the exchange. Orders are stamped with the sponsor's member ID, but the exchange or clearing firm can identify the ultimate client. This model provides better transparency and is required for certain client categories (e.g., registered investment advisers). The sponsor retains direct regulatory responsibility for the client's trading.

**Non-disclosed (or "naked") sponsored access**: The client's identity is not revealed to the exchange; only the sponsor's member ID appears on orders. This model was largely curtailed after the 2010 "flash crash" and the case of Navinder Singh Sarao, a trader using non-disclosed SA to execute the massive trades that contributed to the market dislocation. Regulators found that non-disclosed SA created unmonitored risk. The SEC subsequently tightened Rule 15c3-5, effectively restricting non-disclosed SA to very large, well-capitalized clients and requiring more robust risk monitoring by sponsors.

## Risk and regulatory tightening

Sponsored access concentrates risk in the sponsor broker. If a client loses control of its trading algorithm (malfunction, bug, or intentional manipulation), it can execute enormous quantities of orders before the sponsor's risk filters detect the breach. The Flash Crash of 2010 and Navinder Sarao's erratic trading illustrated this risk. A single rogue algorithm could move prices dramatically and trigger cascading losses across the market.

In response, the SEC adopted Rule 15c3-5 (Compliance with Market Regulation Requirements), requiring brokers offering SA to:

- Implement pre-trade risk controls (maximum order size, notional exposure limits, price reasonableness checks).
- Conduct real-time monitoring of client trading.
- Maintain adequate systems and testing.
- Conduct regular compliance and security audits.
- Establish and enforce written SA agreements with clients.

These requirements increased the cost and complexity of offering SA, leading many brokers to exit the business or restrict it to the largest, most creditworthy clients. Today, major brokers offering SA typically serve hedge funds, registered market makers, and institutional trading firms with minimum capitalisation thresholds.

## Sponsored access versus direct market access (DMA)

The terms are sometimes used interchangeably, but they are not identical. **Direct market access** is a broader term referring to any arrangement where a client's orders reach an exchange with minimal intermediation. DMA can include:

- Sponsored access (orders use the broker's membership).
- Co-located or direct-connected systems (client has its own exchange connection).
- Broker-provided API gateways (client connects to the broker's system, which routes with low latency).

Sponsored access is a specific type of DMA, characterised by use of the sponsor's exchange credentials and membership, combined with the sponsor's risk oversight.

## Modern prevalence and market structure

Sponsored access remains a niche product, available to professional and institutional clients. Retail traders do not have access to SA; retail brokers typically offer no SA tier. For proprietary traders, hedge funds, and market makers, SA is a standard offering from major brokers.

The landscape has evolved. Some brokers have deprecated traditional SA, instead building low-latency API gateways and offering DMA-like functionality without the legal fiction of credential sharing. Others (particularly market-maker-affiliated brokers like Virtu or Citadel Securities) use SA extensively for their own trading and for select institutional clients.

Regulations have also pushed SA toward greater transparency. The shift toward disclosed SA and the tighter risk controls have increased the operational overhead for sponsors but improved market integrity.

## See also

<div class="wiki-seealso">

### Closely related

- [Broker](/broker/) — grants access and monitors risk
- [Algorithmic trading](/algorithmic-trading/) — primary user of sponsored access
- [Market maker](/market-maker-trading/) — uses SA to execute quotes and manage inventory
- [Stock exchange](/stock-exchange/) — destination of sponsored access orders
- [Alternative trading system](/alternative-trading-system/) — competing execution venue
- [Implementation shortfall strategy](/implementation-shortfall-strategy/) — execution algorithm that benefits from low latency
- [Broker internalization](/broker-internalization/) — alternative execution path (via broker's own inventory)

### Wider context

- [Securities and exchange commission](/securities-and-exchange-commission/) — regulates sponsored access (Rule 15c3-5)
- [Trading strategies](/algorithmic-trading/) — strategies for which SA provides competitive advantage
- [Price discovery](/price-discovery/) — how SA and latency affect market efficiency
- [Market structure](/stock-exchange/) — ongoing debate over speed, fairness, and access to markets

</div>

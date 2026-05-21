---
title: "FIX Protocol"
description: "The FIX Protocol is a standardized language used for electronic communication of securities trading information. Brokers, exchanges, and trading systems use FIX to exchange orders, executions, and market data at high speed."
keywords:
  - FIX protocol
  - trading protocol
  - electronic trading
  - market data
  - order routing
  - standardization
image: "https://picsum.photos/seed/fix-protocol/900/600"
---

*The **FIX (Financial Information Exchange) Protocol** is an open, standardized protocol used for electronic communications between market participants — brokers, exchanges, trading systems, and investors. FIX messages convey orders, executions, confirmations, and market data in a machine-readable, standardized format. It has been the de facto standard for electronic trading since the 1990s.*

<div class="wiki-hatnote">

This entry is about the trading communication standard. For market data protocols more broadly, see [market-data-feed-direct](/market-data-feed-direct); for exchange-specific protocols, see [stock exchange](/stock-exchange).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FIX Protocol — key facts</div>

<img src="https://picsum.photos/seed/fix-protocol/900/600" alt="A FIX protocol message showing tag-value pairs for an order" />

<div class="wiki-infobox-caption">FIX Protocol enables standardized trading communication across the market.</div>

|   |   |
|---|---|
| **First version** | 1992 |
| **Current version** | 5.0 (and variants) |
| **Administrator** | FIX Trading Community |
| **Primary use** | Order routing, execution reporting, market data |
| **Speed** | Subsecond message latency |
| **Adoption** | Nearly universal among institutional market participants |
| **Standardization** | Open; publicly documented |

</aside>

## History and purpose

The FIX Protocol was created in 1992 by a group of traders and technologists to standardize electronic communication between trading firms. Before FIX, each firm used proprietary systems, making interoperability difficult.

FIX solved this by defining a standard message format that all market participants could use. A broker's order-routing system could communicate with an exchange's matching engine using FIX; the exchange could report executions back using FIX.

## How FIX works

FIX messages are tag-value pairs, separated by delimiters. Each message type (New Order, Execution Report, Market Data, etc.) has defined fields.

**Example of a simplified FIX New Order message:**

```
8=FIX.4.2 | 9=100 | 35=D | 49=CLIENT1 | 56=EXCHANGE | 34=1 | 55=AAPL | 54=1 | 38=1000 | 40=1 | 44=150.00
```

This message means:
- **FIX version** 4.2
- **Message type** D (New Order - Single)
- **Sender** CLIENT1
- **Target** EXCHANGE
- **Symbol** AAPL
- **Side** Buy (1)
- **Order quantity** 1000 shares
- **Order type** Market (1)
- **Limit price** $150.00

The exchange parses this standardized message and executes the order.

## Message types

**Trade-related messages:**
- **New Order:** Client sends order to broker/exchange.
- **Execution Report:** Exchange sends filled order confirmation.
- **Cancel/Replace:** Client modifies or cancels an order.
- **Order Status Request:** Client queries order status.

**Reporting messages:**
- **Trade Allocation:** Post-trade allocation of executed quantities.
- **Settlement Instruction:** Instructions for settling trades.

**Market data messages:**
- **Market Data:** Quotes and trades published by exchanges.
- **Market Data Request:** Client requests market data.

## Advantages of standardization

**Interoperability.** Any FIX-compliant system can communicate with any other, reducing integration costs.

**Speed.** Standardized, efficient message format minimizes parsing overhead.

**Flexibility.** FIX supports all security types and order types; it is not prescriptive about trading rules.

**Adoption.** Nearly every institutional trading system supports FIX, making it the de facto standard.

## Versions and evolution

FIX has evolved since 1992:

- **FIX 4.0–4.4:** Early versions, still widely used.
- **FIX 5.0:** Modern version with more features.
- **FIX Latest (FIXT):** Module-based version allowing selective feature adoption.

Different venues may support different FIX versions; backward compatibility is generally maintained.

## Direct market access and FIX

Retail brokers and trading firms use FIX to route orders directly to exchanges, bypassing intermediaries. This "direct market access" (DMA) is enabled by FIX standardization.

A proprietary trading firm, using FIX, can connect directly to the NYSE, NASDAQ, and multiple [alternative trading systems](/alternative-trading-system) without custom integration for each venue.

## Market data and FIX

Beyond trade order messaging, FIX is used for market data distribution:

- Exchanges publish [market data](/stock-market) (quotes, trades, order book updates) using FIX messages.
- Trading systems subscribe to FIX market data streams.

This standardization allows a single market data consumer to receive data from multiple venues in a uniform format.

## Alternatives and supplements to FIX

**Exchange-specific protocols.** Major exchanges (NYSE, NASDAQ) often offer exchange-specific protocols (OptiVera, Ouch) that may be faster or more feature-rich than FIX.

**Custom protocols.** Some proprietary platforms use custom protocols for low-latency communication.

**HTTP and web APIs.** Some retail brokers now offer REST APIs or web-based order routing, which bypass FIX but are not standardized.

However, FIX remains the dominant standard for institutional trading.

## FIX and high-frequency trading

High-frequency traders rely heavily on FIX for ultra-low-latency trading:

- Orders are generated by algorithms and sent via FIX.
- Execution reports are received via FIX and parsed in microseconds.
- Latency is critical; shaving milliseconds can mean differences in profitability.

FIX implementations for HFT are optimized for absolute speed, sometimes using direct TCP connections and custom serialization within FIX.

## Governance

FIX is maintained by the **FIX Trading Community**, a non-profit organization. The specification is public and open; any firm can implement FIX without licensing fees.

## See also

<div class="wiki-seealso">

### Closely related

- [Market data](/stock-market) — distributed via FIX
- [Electronic trading](/stock-market) — enabled by FIX
- [Stock exchange](/stock-exchange) — uses FIX for order routing
- [Broker](/broker) — implements FIX for order handling
- [Order routing](/stock-market) — facilitated by FIX

### Wider context

- [High-frequency trading](/stock-market) — relies on FIX
- [Latency](/colocation-detail) — minimized via FIX optimization
- [Standardization](/stock-market) — FIX provides this
- [Interoperability](/stock-market) — enabled by FIX
- [Secondary market](/secondary-market) — dependent on FIX infrastructure

</div>

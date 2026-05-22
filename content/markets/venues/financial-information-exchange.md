---
title: "Financial Information Exchange (FIX)"
description: "Standardized protocol for electronic messaging between market venues and traders, enabling seamless order routing and execution."
keywords:
  - FIX protocol
  - market communication
  - order routing
  - electronic trading
  - venue integration
---

*The **Financial Information Exchange (FIX) Protocol** is an industry-standard language for electronic communication between trading venues, brokers, and traders. It standardizes the format and sequence of messages for order entry, execution, and settlement, allowing different systems to interoperate without custom integration code.*

<div class="wiki-hatnote">For order types and routing mechanics, see [Order Types](/wiki/order-types/) and [Order Routing Logic](/wiki/order-routing-logic/).</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| Purpose | Standard messaging between venues and traders |
| First version | 1992; continuously updated |
| Current version | FIX 5.0 and later, plus custom extensions |
| Message types | Order entry, execution report, cancellation, status |
| Transport | TCP/IP, with encrypted variants |
| Adoption | Nearly universal in institutional markets |
| Latency | Microseconds for local connections |

</aside>

## Why a universal language was needed

Before FIX, each exchange and clearing house used proprietary communication formats. A large investment bank wanting to place orders on NYSE, NASDAQ, and the Chicago Board Options Exchange (CBOE) had to build and maintain separate interfaces for each venue. When a new exchange opened or made system upgrades, the bank's technology team scrambled to adapt.

FIX emerged in 1992 as a collaborative standard: instead of each venue defining its own protocol, the industry agreed on a common message format. An institutional trader could now write once—a FIX message—and send it to hundreds of venues without modification. This dramatically reduced integration costs and accelerated the rise of algorithmic trading and [high-frequency trading](/wiki/high-frequency-trading/), which depend on latency and automation.

## How a FIX message works

A FIX message is a sequence of **tagged fields** separated by delimiters. Each field has a numeric tag and a value. For example:

```
8=FIX.4.4|9=150|35=D|49=CLIENT1|56=BROKER|34=1|52=20250522-14:30:00|
11=ORDER123|55=AAPL|54=1|38=100|40=2|44=150.50|...
```

(Pipes shown for clarity; actual delimiters are SOH—Start of Header, ASCII 0x01.)

Each tag has a defined meaning: `8` is protocol version, `35` is message type (D = New Order), `55` is symbol, `38` is quantity, `40` is order type (2 = limit), `44` is limit price. The recipient (broker or venue) parses this and knows exactly what is being ordered, without ambiguity.

## Message types in FIX

The protocol defines dozens of message types, but the most common are:

- **New Order Single (35=D)**: Client sends a new order to the broker or exchange.
- **Execution Report (35=8)**: Venue confirms a fill, partial fill, rejection, or cancellation.
- **Order Cancel Request (35=F)**: Client asks to cancel an outstanding order.
- **Logon (35=A)**: Establish session; authenticate credentials.
- **Logout (35=5)**: Gracefully close session.
- **Heartbeat (35=0)**: Keep-alive; ensure both sides are still responsive.
- **New Order List (35=E)**: Multi-leg or basket order.

This standardization means that a trader's software can handle fills and rejections from any venue using the same parsing logic.

## FIX and order routing

When a [smart order router](/wiki/smart-order-router/) decides to split a large order across multiple venues, it generates separate FIX New Order messages to each broker or exchange. The routers listen for Execution Report messages coming back and aggregate fills into a single view for the client. [Payment for order flow](/wiki/payment-for-order-flow/) arrangements often ride on FIX—a broker sends orders to a market maker's FIX gateway in exchange for a small rebate.

The [order routing logic](/wiki/order-routing-logic/) itself—which venue gets which slice—is outside FIX; that's the broker's business logic. But once the decision is made, FIX is the transport.

## Latency and transport

FIX runs over TCP/IP (or UDP variants for lower latency). A trader on the East Coast sending an order to a venue in New Jersey might experience sub-millisecond FIX latency over a leased private line. A retail trader routing through a broker to the same venue might experience 50–200 ms of additional latency due to the broker's processing and network routing.

**FIX over ITCH** is a lower-latency variant used by exchanges like NASDAQ, where market data flows over a separate, faster binary protocol (ITCH) while orders come in over FIX.

High-frequency traders optimize every microsecond: custom hardware FIX gateways, colocation servers inside exchange data centers, and even firmware-level optimizations. For retail and most institutional traders, absolute FIX latency matters less; the standardization itself is the win.

## Extensions and customization

While FIX defines a core set of fields and message types, venues and brokers extend it with custom tags for proprietary features. An exchange might add a tag for dark pool order routing, or a broker might add a tag for client-specific margin rules. These extensions are negotiated during the [logon](/wiki/electronic-communication-network-market/) handshake, so both sides know what custom fields to expect.

This flexibility has allowed FIX to remain relevant for 30+ years despite enormous changes in market structure. When new asset classes (crypto, alternative venues) emerged, FIX was extended rather than replaced.

## FIX in regulation and reconciliation

Regulators like the SEC and CFTC require venues and brokers to maintain detailed audit trails of orders and fills. FIX message logs are the canonical record—each message is timestamped, sequence-numbered, and includes counterparty IDs. When a dispute arises (e.g., "why wasn't my order filled?"), the FIX message tape is replayed to reconstruct the event.

Post-trade compliance uses FIX Execution Reports to confirm that all fills are properly matched between broker and venue and routed to clearing houses. The [depository trust company](/wiki/depository-trust-company/) and clearing agents all consume FIX messages to settle trades.

## Evolution and alternatives

FIX has competitors: **STP (Straight-Through Processing)** initiatives in some markets use simpler JSON or XML formats, especially in newer venues or crypto exchanges. However, FIX's ubiquity means that even venues built on different stacks often expose a FIX gateway for compatibility. The protocol is maintained by SIFMA (Securities Industry and Financial Markets Association) and FPL (FIX Protocol Limited).

The arrival of [blockchain](/wiki/blockchain-fundamentals/) and [decentralized exchanges](/wiki/decentralized-exchange/) raised questions about whether FIX would be displaced. In practice, many DeFi venues are now adding FIX gateways or FIX-like APIs to attract institutional traders who expect familiar order mechanics.

<div class="wiki-seealso">

### Closely related
- [Order Types](/wiki/order-types/) — order structure concepts
- [Order Routing Logic](/wiki/order-routing-logic/) — routing decisions
- [Smart Order Router](/wiki/smart-order-router/) — execution strategy
- [Payment for Order Flow](/wiki/payment-for-order-flow/) — FIX-driven arrangements
- [Consolidated Tape](/wiki/consolidated-tape/) — related market data standard

### Wider context
- [Electronic Communication Network](/wiki/electronic-communication-network-market/) — trading venues
- [Market Surveillance](/wiki/market-surveillance/) — FIX-based compliance
- [Settlement Procedures](/wiki/settlement-procedures/) — downstream use
- [Depository Trust Company](/wiki/depository-trust-company/) — settlement hub

</div>

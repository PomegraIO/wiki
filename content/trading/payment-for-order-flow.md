---
title: "Payment for order flow"
description: "Payment for order flow (PFOF) is when a broker sells its customer orders to a market maker (typically in exchange for better prices or rebates). The broker receives payment; the customer may receive modest price improvement, but the arrangement creates potential conflicts of interest."
keywords:
  - PFOF
  - payment for order flow
  - order routing
  - conflicts of interest
image: "https://picsum.photos/seed/payment-for-order-flow/900/600"
---

*Payment for order flow (PFOF) is an arrangement where a broker routes retail customer orders to a [market maker](/market-maker-trading) (like Citadel, Virtu, or others) rather than a [lit venue](/lit-venue), and the market maker pays the broker for the order flow. The customer sees the execution; the broker receives a rebate or revenue share. This is legal but controversial: the customer might get modest price improvement (the market maker offers a slightly better price to compete for order flow), but the broker has a financial incentive to route there even if a lit exchange would be better.*

<div class="wiki-hatnote">

For transparent routing to public exchanges, see [lit venue](/lit-venue). For automated routing optimization, see [smart order router](/smart-order-router).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Payment for order flow — key facts</div>

<img src="https://picsum.photos/seed/payment-for-order-flow/900/600" alt="A diagram showing cash flow from market maker to broker to customer" />

<div class="wiki-infobox-caption">PFOF: broker receives payment, customer receives modest price improvement, conflicts loom.</div>

|   |   |
|---|---|
| **What it is** | Broker sells customer orders to market maker; receives payment |
| **Typical amount** | $0.0001–$0.0005 per share, or rebates |
| **Who benefits** | Broker (payment), customer (slight price improvement), market maker (order flow) |
| **Who loses** | Potentially the customer, if routing is not optimal |
| **Legality** | Legal, but must be disclosed |
| **Market prevalence** | ~40–50% of retail orders routed via PFOF |

</aside>

## How PFOF works

**Traditional model (exchanges):**
- You place an order through your broker.
- Broker routes to NYSE or NASDAQ.
- Order executes on the exchange.
- Broker pays exchange fees ($0.0001–$0.0005 per share).

**PFOF model:**
- You place an order through your broker.
- Broker routes to a market maker (e.g., Citadel, Virtu).
- Market maker fills your order at a price (usually slightly better than the exchange quote).
- Market maker **pays your broker** $0.0001–$0.0005 per share (or more) for the order flow.
- Your broker pockets the payment.

**Result:** The broker makes money instead of paying fees. You might get a slightly better price. The market maker gets order flow to trade against.

## Why market makers pay for order flow

**Profit opportunity:** A market maker buying order flow from a broker can:
- Use the flow to set their own quotes and profit on the spread.
- Hedge risks by trading the flow against other positions.
- Exploit patterns in retail orders (e.g., retail investors tend to chase momentum; a market maker can fade retail buying and fade retail selling).

**Scale:** The more order flow, the more opportunities. Market makers bid aggressively for large-volume order flow.

## The PFOF controversy

**The upside (from the broker/market maker perspective):**
- Brokers can offer commission-free trading (zero commissions became possible partly because of PFOF revenue).
- Retail customers get modest price improvement from market makers' competitive pricing.
- Market makers provide liquidity, reducing bid-ask spreads.

**The downside (from the customer perspective):**
- **Conflict of interest:** Your broker has a financial incentive to route your order to the highest-paying market maker, not to the venue offering the best price for you.
- **Information disadvantage:** The market maker sees your order and can trade against you or other customers. Your retail order is "toxic" (predictable); the market maker exploits this.
- **Reduced retail order book participation:** Your order does not go into the lit public order book, so it does not contribute to price discovery.
- **Opacity:** You do not see the payment your broker receives; the arrangement is disclosed but opaque.

## Real-world example: PFOF in action

You place a market order to buy 100 shares of Apple. Current market:
- NASDAQ ask: $150.02
- Citadel (market maker via PFOF): $150.015

Your broker routes to Citadel. You buy at $150.015 (0.5 cents better than NASDAQ). Citadel pays your broker $0.0002 per share = $20 for the order flow. Your broker pockets $20. You save $0.005 per share = $0.50 total.

Looks good, right? But what if Citadel turns around and shorts Apple immediately, knowing it just bought 100 shares from retail? If Apple falls, Citadel profits at your expense.

## Regulation and disclosure

PFOF is legal but heavily regulated:

**SEC Rule 10b-1:** Brokers must disclose PFOF arrangements and the payments received. However, the disclosures are often buried in fine print.

**Best execution:** Brokers must still comply with best execution rules, meaning the price they route to (even PFOF venues) must be competitive.

**Regular review:** Brokers must periodically audit their PFOF arrangements to ensure customers are getting competitive prices.

Despite these rules, critics argue that PFOF still creates conflicts and harms retail traders.

## Debate about PFOF

**Defenders argue:**
- PFOF enables commission-free trading.
- Market makers offer competitive pricing to compete for order flow.
- Retail investors get better execution (fewer fees) as a result.

**Critics argue:**
- PFOF creates conflicts of interest; brokers prioritize payment, not customer prices.
- Retail orders are exploited by sophisticated market makers (information asymmetry).
- The public order book is starved of retail flow, reducing transparency.
- Competitors like Interactive Brokers (which does not use PFOF) achieve good execution without this revenue model.

## Alternatives to PFOF

**No PFOF (transparent routing):**
- Some brokers (Interactive Brokers, some others) do not use PFOF. They route to lit exchanges and charge small fees or operate via other revenue models.
- Customers see better execution in some cases; in others, they pay slightly higher fees.

**Hybrid models:**
- Some brokers use a mix: PFOF for some orders, lit venues for others, or PFOF only if prices are competitive.

## Current market trends

The debate over PFOF has intensified, especially after the meme stock era (2021), when Robinhood stopped allowing retail investors to buy GameStop and AMC, citing risk management. This sparked discussions about whether PFOF creates conflicts (e.g., the brokerages' incentives to stop a trade that would lose money for their market maker counterparties).

Some regulatory proposals have aimed to restrict or ban PFOF, but these remain contentious.

## See also

<div class="wiki-seealso">

### Closely related

- [Market maker](/market-maker-trading) — the buyer of order flow
- [Smart order router](/smart-order-router) — routes for best execution, avoiding PFOF conflicts
- [Best execution](/best-execution) — regulatory obligation; PFOF must comply
- [Dark pool](/dark-pool) — similar to PFOF in that it is off-lit venues

### Order routing and execution

- [Lit venue](/lit-venue) — public exchange alternative to PFOF
- [NBBO](/nbbo) — best bid-offer; PFOF must be competitive
- Trade-through rule — protects against bad PFOF prices
- Slippage — PFOF can increase this if not carefully managed

### Regulation and compliance

- SEC — regulates PFOF
- [FINRA](/finra) — enforces best execution
- Reg NMS — regulatory framework
- Disclosure — PFOF must be disclosed

### Conflicts of interest

- Information asymmetry — market makers exploit retail order flow
- **Retail investor protection** — PFOF raises concerns about fairness

</div>

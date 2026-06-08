---
title: "Electronic Broking System"
description: "An automated platform that electronically matches foreign exchange spot and derivatives orders between bank dealers, replacing manual telephone negotiation."
keywords:
  - electronic broking
  - forex trading platforms
  - automated order matching
  - interbank fx market
  - dealer networks
  - order routing
image: "/svg/markets.svg"
---

*An **electronic broking system** (EBS) is a centralised automated platform that matches foreign exchange orders between dealers at banks, primarily for spot contracts and derivatives. It replaced the labour-intensive telephone-based broker as the backbone of institutional FX trading, allowing banks to execute large orders with minimal human intervention and dramatically tighter bid-ask spreads.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Electronic Broking System — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A digital engine that matches dealer orders in real time, eliminating the voice broker bottleneck.</div>

|   |   |
|---|---|
| **What it is** | Automated order-matching venue for OTC FX and derivatives among banks |
| **Also called** | EBS, electronic market, interdealer platform |
| **Primary market** | [Over-the-counter market](/over-the-counter-market/) for spot forex and forwards |
| **Key participants** | Large banks, hedge funds accessing via prime brokers |
| **Spread improvement** | Typically 0.5–2 pips vs. voice negotiation |
| **Hours** | 24/5 (Sunday evening through Friday night, all major zones) |
| **Execution model** | [Price discovery](/price-discovery/) via two-way quotes or central limit-order book |

</aside>

## Why the phone became obsolete

Before the late 1990s, interbank FX trading was almost entirely conducted by voice. A trader at Goldman Sachs wanting to sell JPY would call a broker at Tullett Prebon or similar, who would phone his contacts at five other banks to find buyers. This process took minutes. With trillions of dollars in daily FX volume, and hundreds of dealers all competing on the same news simultaneously, the telephone system created vast friction: delays, human error, and spreads that reflected the broker's commission and labour cost.

Electronic broking systems—first with EBS (launched 1993, later acquired by Nasdaq) and the competing [Reuters](#) platform—removed the middleman. Dealers entered two-way prices into a central electronic system. Other dealers saw those quotes in real time and could hit them instantly with a mouse click or a programmatic order. The entire negotiation collapsed from five minutes to milliseconds.

## How matching works today

Modern electronic broking systems operate on one of two mechanisms. **Two-way quoting**, favoured by larger dealers and on major currency pairs, works like an auction: Bank A enters a price to sell 50 million EUR/USD at 1.0950–1.0951 (bid-ask spread). Bank B sees that price on screen and clicks to buy at 1.0951. The trade is done. Bank A has provided liquidity and accepted a small profit from the spread; Bank B has executed immediately without the uncertainty of negotiation.

Some platforms use a **central limit-order book**, familiar to equity traders. Dealers submit buy and sell orders at specified prices and sizes; the system matches them by price-time priority. This works well for less liquid currency pairs and longer-dated forwards, where dealers cannot afford to post continuous two-way quotes.

The critical difference from an [exchange](/stock-exchange/) like the NYSE is transparency and anonymity. EBS platforms often hide the identity of the counterparty until after the trade is done, protecting dealers from signalling their intentions to the broader market. This asymmetry—real-time anonymity—is what makes EBS pricing so tight: a dealer quoted 1.0950–1.0951 does not know if he is dealing with the central bank, a hedge fund, or a rival dealer exiting a large position.

## Tight spreads, high leverage

The elimination of manual brokers has compressed margins in FX trading. Where a dealer might have quoted a two-pip spread in 1995, today the same trade on a major pair like EUR/USD trades at 0.3–0.5 pips on EBS, especially during London and New York hours. This benefits end users: hedge funds access those tight prices through their [prime brokers](/prime-brokerage-venue/), and corporate customers paying for forwards get better fills than their predecessors.

The cost, paradoxically, is leverage. Because spreads are so tight, dealers must trade far larger volumes to achieve the same profit margin. An investment bank's FX desk that made respectable returns on 200 million USD per day in 1995 now needs to move 5 billion USD per day. That capital intensity creates risk concentration. When volatility spikes and dealers all withdraw their quotes simultaneously—a phenomenon called "liquidity evaporation"—the spreads on EBS can widen from 0.5 pips to 5 or 10 pips in seconds, catching leveraged traders off-guard.

## The role of order routers

For hedge funds and asset managers, EBS and other electronic platforms are not directly accessible. Instead, they trade through a [prime broker](/prime-brokerage-venue/) at a large bank, which in turn routes orders to EBS and competing venues like Currenex or internal bank crossing networks. The prime broker adds its own commission (typically 0.5–1 pip) and may execute a customer's order through multiple liquidity sources to achieve the best overall price.

This two-tier structure—dealer-to-dealer on EBS, and client-to-dealer via prime brokers—has hardened the distinction between retail and institutional markets. A currency trader at a small hedge fund orders JPY through his broker's interface. That order might be aggregated with orders from ten other clients, then sent to EBS as a single 500 million JPY order from the prime broker.

## Fragmentation and competition

No single platform dominates as completely as an equity exchange does. EBS, Thomson Reuters Matching, FastMatch, and others coexist, and the largest dealers run their own crossing networks—internal platforms where the bank matches client orders with its own inventory or other clients' orders. This fragmentation means that the true market price is not visible in one place; instead, prices are dispersed across dozens of venues.

Regulators and market infrastructure providers have tried to improve [price discovery](/price-discovery/) through "trade reporting"—the requirement that dealers publish the details of their completed trades to a public source. This does not eliminate fragmentation, but it ensures that no dealer can be wildly out of line with the rest of the market without being noticed.

## See also

<div class="wiki-seealso">

### Closely related

- [Over-the-counter market](/over-the-counter-market/) — Decentralised trading in derivatives where matching happens between bilateral counterparties, not on a central exchange
- [Prime brokerage](/prime-brokerage-venue/) — The service through which hedge funds access electronic platforms and borrow securities
- [Price discovery](/price-discovery/) — The process by which market prices emerge from the interaction of buy and sell orders
- [Voice brokered market](/voice-brokered-market/) — The telephone-based predecessor to electronic matching, still used in less liquid markets
- [Alternative trading system](/alternative-trading-system/) — Regulated non-exchange venues that match securities orders electronically

### Wider context

- [Bid-ask spread](/bid-ask-spread/) — The premium between what buyers offer and sellers ask, tightened by electronic competition
- [Market maker trading](/market-maker-trading/) — The dealer function of posting two-way prices on which EBS systems rely
- [Counterparty risk](/counterparty-risk/) — The danger that the opposite side of a trade fails, managed through clearing in some markets
- [Leverage ratio forex](/leverage-ratio-forex/) — The borrowing ratios common in FX trading, enabled by margin lending from prime brokers
- [Currency volatility](/currency-volatility/) — Exchange-rate swings that drive spreads wider during stressed conditions

</div>

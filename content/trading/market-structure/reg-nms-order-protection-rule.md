---
title: "Reg NMS Order Protection Rule"
description: "The SEC rule requiring brokers to execute orders at any venue displaying the best protected bid or ask price."
keywords:
  - Reg NMS
  - order protection
  - quote protection
  - best execution
  - market regulations
image: /svg/trading.svg
---

*In 2005, the SEC adopted **Regulation National Market System (Reg NMS)**, a sweeping rule designed to unify the US stock market across dozens of exchanges and trading venues. At its core is the **Order Protection Rule**, which forbids any venue from trading at a price worse than the best protected quote anywhere else in the system—and it requires brokers to route orders to satisfy this price guarantee.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg NMS Order Protection Rule — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Ensures no venue can ignore better prices elsewhere in the consolidated market.</div>

|   |   |
|---|---|
| **What it is** | Rule 610 of Reg NMS; requires best execution across all trading venues |
| **Adopted** | 2005 (effective 2007) |
| **Regulator** | US Securities and Exchange Commission (SEC) |
| **Central concept** | "Protected quote" — a quote that all venues must respect |
| **Applies to** | All US equity trading, all venues, all brokers |
| **Key constraint** | Brokers cannot [internalize](/order-internalization/) at worse prices than best available |
| **Exception** | Trade-through allowable if quote moved or was self-help exception |

</aside>

## The fragmented pre-2007 market

Before Reg NMS, US equity trading was highly fragmented. The New York Stock Exchange had enormous market share, but regional exchanges, electronic communication networks (ECNs), and broker [market makers](/market-maker-trading/) operated independently. If an investor's broker routed an order to the NYSE, there was no guarantee that the order would find the best price—which might be sitting on NASDAQ or a smaller regional exchange. Prices for the same stock could differ by a penny or more between venues, and traders with access to multiple feeds could arbitrage these differences.

The lack of a coherent "best price" rule hurt ordinary investors. Brokers had little incentive to route orders to venues with the best displayed prices if they could keep the order in-house or send it to a preferred venue paying them rebates. The market was efficient for sophisticated traders with real-time access to all price feeds but opaque and often worse for retail clients.

## The Order Protection Rule's core principle

Reg NMS Rule 610, the Order Protection Rule, introduced a simple idea: no venue may execute a trade at a price that violates the best protected quote. If NASDAQ is showing the best bid at $50.00 and the best ask at $50.01, no other venue—not the NYSE, not a dark pool, not a broker's internal system—can execute your sell order at $49.99. Someone can only buy it at $50.00 or better.

This rule forces all trading venues to compete on price and to acknowledge each other's quotes in real time. If you place a [limit order](/limit-order/) on the NYSE and a better price appears on NASDAQ, the NYSE's system must send the order to NASDAQ to fill against that better price—or the order will sit on NYSE until NASDAQ's price moves back.

## Protected vs. unprotected quotes

Not every quote displayed counts as "protected." The SEC defined protected quotes to exclude certain situations where prices are stale, locked, or crossed. For instance, if a venue's system experiences a technical glitch and produces outlier prices, other venues do not have to honour those prices. Similarly, if two quotes are "locked" or "crossed" (the bid is at or above the ask), the rule allows certain exceptions so that trading is not paralysed.

The definition of a protected quote is crucial to the rule's effectiveness. A very narrow definition means many quotes escape protection and venues can trade through them. A very wide definition could make the system rigid. The SEC and exchanges have debated the boundaries continuously, particularly around the speeds and sizes at which quotes are protected.

## Broker routing and [order internalization](/order-internalization/) implications

For brokers, Reg NMS means they cannot routinely internalise orders at worse prices than the protected quote. If you place a [market order](/market-order/) to buy and the best protected ask is $50.01, your broker must route to that venue at $50.01 unless it can offer you $50.00 or better from its own inventory. This rule created an immediate tension: brokers love the profits from internalizing order flow, but the rule limits how wide they can price internally.

In practice, many brokers route orders to [market makers](/market-maker-trading/) and rebate a small payment to them in exchange for better internal prices. This rebate system—"payment for order flow"—became the dominant model for retail order routing after Reg NMS. The broker's market maker partner fills the order at or better than the protected quote and gets paid a fraction of a cent per share. The broker is compliant, the client gets decent execution, and the market maker profits on volume.

## Trade-through exceptions and self-help

The rule does allow trade-throughs—executions at worse prices—in narrow circumstances. If a venue believes that another venue's protected quote is erroneous or stale, it can invoke a "self-help" exception and trade through it without routing first. This exception exists to prevent the market from freezing if one venue's quote feed lags or breaks. However, self-help has been controversial. Some critics argue venues use it too aggressively to avoid routing orders to competitors.

## Impact on price improvement and market quality

Empirical studies suggest Reg NMS improved average bid-ask [spreads](/bid-ask-spread/) and reduced the direct costs of trading, especially for retail investors. However, the rule also created new complexities. The need to route orders across venues added latency for some trades, creating opportunities for high-frequency traders to arbitrage tiny price differences between venues. The rule's exceptions around locked and crossed quotes have occasionally been exploited to circumvent the spirit of the rule.

## Ongoing debates and amendments

Since 2007, the SEC has amended Reg NMS several times. Changes have addressed small-order exceptions, quote sizing, and the treatment of certain alternative trading venues. The rise of [dark pools](/alternative-trading-system/) and wholesalers like Citadel Securities and Virtu has reignited questions about whether retail orders are truly getting best execution under Reg NMS. These firms' ability to internalize massive order flow and still show competitive prices suggests the rule is working—or that their scale lets them circumvent its intent.

Some critics argue that Reg NMS, by forcing all venues to show and respect the same best quote, has reduced the incentive for venues to innovate on service, technology, or order types. Others defend the rule as essential to maintaining fair competition and a unified market.

## See also

<div class="wiki-seealso">

### Closely related

- [Order Internalization](/order-internalization/) — the practice the rule constrains
- [Limit Order Book](/limit-order-book/) — where protected quotes reside
- [Market Maker](/market-maker-trading/) — often fills orders under Reg NMS protection
- [Price-Time Priority](/price-priority-time-priority/) — matching rule within venues under Reg NMS
- [Bid-Ask Spread](/bid-ask-spread/) — improved by the protection rule
- [Best Execution](/bid-ask-spread/) — the principle behind order protection

### Wider context

- [Stock Exchange](/stock-exchange/) — regulated under Reg NMS
- [Alternative Trading System](/alternative-trading-system/) — dark pools subject to Reg NMS
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator
- [Market Order](/market-order/) — affected by order routing
- [Broker](/broker/) — required to comply with routing obligations

</div>

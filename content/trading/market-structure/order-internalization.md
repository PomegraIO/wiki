---
title: "Order Internalization"
description: "When a broker-dealer fills a client's order against its own inventory rather than routing it to an exchange."
keywords:
  - order internalization
  - broker inventory
  - order routing
  - market microstructure
  - price improvement
image: /svg/trading.svg
---

*When you place a stock order through a broker, that order doesn't always go to a public exchange. A **broker-dealer** can fill it from its own inventory or from orders it has collected from other clients—a practice called **order internalization**. The broker becomes both the intermediary and the counterparty to your trade, potentially offering better prices and faster execution than the exchange could.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order Internalization — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The broker books both sides of your trade against its own liquidity.</div>

|   |   |
|---|---|
| **What it is** | Filling a client order using the broker's inventory instead of routing to an exchange |
| **Also called** | Internalizer, riskless principal trade, proprietary matching |
| **Regulatory framework** | [Reg NMS](/reg-nms-order-protection-rule/), SEC best-execution rules, state securities law |
| **Execution venue** | Broker's own system, dark pool, or against accumulated client orders |
| **Time to execution** | Often faster than exchange routing—milliseconds |
| **Price discovery** | Can improve on market price; must still comply with protected quotes |
| **Primary users** | Retail investors, proprietary traders |

</aside>

## Why brokers internalize orders

Order internalization is profitable because brokers capture the [bid-ask spread](/bid-ask-spread/)—the difference between the best buy and sell prices. Instead of routing your order to an exchange and paying a fee, the broker can hold both sides in-house and keep that spread. For the broker's other clients trying to sell what you want to buy, internalization offers immediate matching and no exchange latency.

Brokers also use order internalization to manage inventory. A retail [market order](/market-order/) to buy 100 shares arrives; the broker's inventory happens to have exactly 100 shares to sell. Rather than sending that order into the consolidated quote stream, the broker matches buyer and seller internally and books the spread.

## Execution quality and price improvement

Internalization is not automatically worse for the retail client. If the broker is well-capitalized and has robust matching logic, an internalized execution can actually improve on the [national best bid and offer](/bid-ask-spread/) (NBBO)—the legally protected best displayed prices across all exchanges. Many brokers advertise "price improvement," meaning they fill orders at better prices than the NBBO before or instead of routing to exchanges.

However, this quality depends on the broker's incentive structure and technology. A broker managing its own spread has a strong incentive to offer reasonable prices—if they consistently underprice their clients, clients will leave for competitors. But if a broker's internalization desk is primarily a profit center, rather than a client-serving one, internal prices might creep wider, and large orders might face adverse selection.

## The role of Reg NMS and best execution

The SEC's [Reg NMS Order Protection Rule](/reg-nms-order-protection-rule/) constrains what a broker can do with internalization. If another venue is displaying a better protected quote than what the broker's internal system is offering, the broker cannot internalize the trade—it must route to that better venue or wait for that quote to move. This rule prevents brokers from systematically routing orders internally at inferior prices.

"Best execution" rules also require brokers to demonstrate that their order routing and internalization practices are in clients' best interests across several dimensions: price, speed, likelihood of execution, and total cost. A broker that internalizes almost everything at the mid-spread might fail this test if actual exchange prices would have been better.

## Dark pools and internalization

Many brokers operate or own stakes in [alternative trading systems](/alternative-trading-system/) (ATS) and [dark pools](/alternative-trading-system/), which are electronic venues that do not display prices publicly. These venues are another form of order internalization—orders are matched without being exposed to the consolidated quote first. Dark pools can provide [price discovery](/price-discovery/) benefits for large trades that would otherwise move the market, but they can also hide liquidity and make it harder for ordinary investors to see where their orders trade.

## Volume and industry concentration

Order internalization accounts for a significant but contested share of US equity trading. The largest brokers—especially those serving retail investors with low trading costs—internalize a substantial portion of small orders. Fintech brokers and zero-commission platforms often tout their internalization or routing partnerships as a feature that enables low fees. Some of the largest [market makers](/market-maker-trading/), like Citadel Securities and Virtu, have massive order flow payments from brokers in exchange for internalizing and executing retail orders at tight spreads.

## Conflicts of interest

Internalizing brokers face an inherent conflict: their economics improve when they widen internal spreads or delay routing to better external prices. Regulators and independent market observers have periodically scrutinized whether brokers are truly prioritizing best execution or simply keeping profitable trades for themselves. Most major brokerages have faced regulatory inquiries or enforcement actions over order routing practices.

The SEC has also raised questions about order internalization's effect on [price discovery](/price-discovery/) and market transparency. Orders that never touch an exchange do not contribute to the consolidated last sale or quote feeds, which could distort market data and disadvantage institutional traders who rely on tape-based pricing signals.

## See also

<div class="wiki-seealso">

### Closely related

- [Reg NMS Order Protection Rule](/reg-nms-order-protection-rule/) — the rule that sets boundaries on internalization
- [Market Maker](/market-maker-trading/) — dealer that provides continuous liquidity and often internalizes flow
- [Bid-Ask Spread](/bid-ask-spread/) — the spread a broker keeps when internalizing
- [Alternative Trading System](/alternative-trading-system/) — venues like dark pools where internalization often occurs
- [Best Execution](/bid-ask-spread/) — regulatory obligation that constrains internalization practices
- [Price Discovery](/price-discovery/) — how markets find efficient prices; internalization's effect on this is debated

### Wider context

- [Market Order](/market-order/) — typical order type routed or internalized
- [Limit Order](/limit-order/) — preserved in book during internalization
- [Broker](/broker/) — the firm doing the internalizing
- [Stock Exchange](/stock-exchange/) — the venue that brokers route to instead
- [Over-the-Counter Market](/over-the-counter-market/) — related structure for less-liquid securities

</div>

---
title: "Reg NMS Order Protection Rule"
description: "The SEC rule that prohibits brokers from routing trades at prices worse than the best publicly available bid or offer, enforcing best execution."
keywords:
  - Regulation NMS
  - trade-through rule
  - order protection
  - best execution
  - SEC trading rules
  - market structure regulation
image: "/svg/regulation.svg"
---

*Before 2005, a trader's order could be executed at a worse price than the best price available elsewhere in the market, simply because the order was routed to a particular venue. The SEC's **Reg NMS Order Protection Rule** (formally the "trade-through prohibition") banned this practice, requiring [brokers](/broker/) to route orders to venues displaying the best available [bid or ask price](/bid-ask-spread/), or to guarantee equivalent prices themselves. The rule is foundational to modern US equity market structure and directly constrains how much profit can be extracted from [arbitrage](/), flow routing, and [market-making](/market-maker-trading/).*

<div class="wiki-hatnote">

For the broader regulatory framework, see [Reg NMS](/). For price bands that work alongside order protection, see [Limit Up-Limit Down Rule](/limit-up-limit-down-rule/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg NMS Order Protection Rule — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation and governance." />

<div class="wiki-infobox-caption">Enforcing best execution and price priority across competing venues.</div>

|   |   |
|---|---|
| **What it is** | The trade-through prohibition: a broker cannot execute an order at a price worse than the best bid or ask displayed by another venue |
| **Enacted** | 2005 (part of Reg NMS) |
| **Regulator** | [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) |
| **Applies to** | US equities listed on [NYSE](/new-york-stock-exchange/) and [Nasdaq](/nasdaq/), and all [brokers](/broker/) executing those trades |
| **Core requirement** | Orders routed to the best displayed price or broker must internalize at equivalent price |
| **Related concepts** | [Best execution](/), [bid-ask spread](/bid-ask-spread/), [market microstructure](/), [liquidity](/), [alternative trading system](/alternative-trading-system/) |

</aside>

## The problem it solved: execution-quality fragmentation

In the 1990s and early 2000s, the US stock market was fragmented across the [New York Stock Exchange](/new-york-stock-exchange/), [Nasdaq](/nasdaq/), regional exchanges, and Electronic Communication Networks (ECNs). A stock might trade at a [bid](/bid-ask-spread/) of $50.00 on one venue and $50.05 on another at the same instant. A broker could legally route a customer's buy order to the venue with the worse offer—say, $50.10—if that venue paid the broker a rebate or internalized the order (executing it within the broker's own operation) at a profitable spread. The customer paid a worse price, but the broker profited.

This fragmentation was legally permitted because there was no unified "national best [bid](/bid-ask-spread/)" rule before Reg NMS. Market participants knew prices were scattered, and if you wanted the best execution, you had to shop around yourself or hire a sophisticated broker. For retail investors and smaller traders, the burden was impractical. For large institutions, negotiating execution quality was a major expense. The system worked, but it was inefficient and left money on the table for traders who lacked information or leverage.

## How the rule works in practice

Reg NMS requires a broker (the market participant taking the customer's order) to ensure that the customer's execution price is at least as good as the best price publicly displayed on any US venue at the time the order is executed. If the best [bid](/bid-ask-spread/) for a stock is $50.00 on the [NYSE](/new-york-stock-exchange/) and $50.05 on an [alternative trading system](/alternative-trading-system/), a broker routing a customer's buy order cannot execute it at worse than $50.05. The broker must either:

1. **Route to the best venue**: Send the order to whichever exchange or system is displaying the best price.
2. **Internalize at best price or better**: Execute the order within the broker's own system at a price at least as good as the national best bid or offer (NBBO).
3. **Negotiate a simultaneous trade**: Execute at a better price on one venue while simultaneously purchasing shares at the worst displayed price on the venue offering it, capturing the spread and providing the customer the better price.

For sell orders, the logic reverses—the broker cannot execute at a price worse than the best [ask](/bid-ask-spread/) displayed anywhere.

The rule applies at the moment of execution. If prices move and the market shifts while an order is being routed, the broker must act on the best available prices at the time the execution occurs, not the prices that existed when the order arrived at the broker's desk.

## Exceptions and safe harbors

Reg NMS does allow some exceptions. "Odd lots"—orders for fewer than 100 shares—are exempt; the rule applies only to round lots (100 shares or more) and larger. Orders marked "do not reduce" (DNR) or with special execution instructions may have some exemptions. Exchanges can also offer "protected quotations"—best bids and offers that are binding and protected—only for venues that commit to certain technical standards and market-making obligations.

Notably, the rule does not require a broker to route to an [alternative trading system](/alternative-trading-system/) or dark pool if the customer's order can be filled on a traditional exchange at the same price. It ensures the customer gets the best displayed price, but does not mandate access to non-displayed liquidity or hidden orders.

## Impact on market structure and profitability

Reg NMS's trade-through prohibition has been transformative. It eliminated the worst predatory execution practices, improved [bid-ask spreads](/bid-ask-spread/) for most liquid stocks, and created a more unified national market despite multiple trading venues. The [tick size](/), [spread width](/bid-ask-spread/), and liquidity for major stocks improved materially in the years after its adoption.

The rule also reshaped broker and market-maker business models. Brokers can no longer profit simply by executing customers at suboptimal prices; they must earn revenue through commissions, spreads on proprietary trading, or value-added services. Market makers face tighter constraints—they cannot rely on capturing order flow that is obligated to meet a better price elsewhere. Instead, they must compete on the tightness of their quotes and the reliability of their market-making.

For [arbitrage](/), the rule reduces opportunity. An arbitrageur spotting a stock trading at $50.00 on one exchange and $50.10 on another cannot easily exploit the gap if brokers must route to the better-priced venue. The rule does not eliminate arbitrage—prices can still diverge, and executed trades can still move, but it prevents a simple "trade here at worse price" profit.

The rule has also incentivized technological investment. Brokers spend heavily on order-routing systems that scan multiple venues in real time and select the optimal execution. This infrastructure cost has favoured large, well-capitalized brokers and contributed to consolidation in the brokerage industry.

## Criticisms and ongoing debates

Some argue Reg NMS, while beneficial for retail investors, may have gone too far in constraining [market makers](/market-maker-trading/) and innovation. Tighter rules on order routing and execution may reduce the incentive for market makers to provide liquidity, especially for less liquid stocks. The rule is also blamed (by some) for increasing the prevalence of dark pools and non-displayed liquidity, as large traders seek to avoid the "best price" requirement by trading off-exchange.

Others argue that the rule does not adequately address new market microstructure issues—such as the speed advantage of high-frequency traders or the fragmentation caused by the proliferation of dark venues. The SEC has proposed updates to Reg NMS over the years, including requirements for real-time transparency of off-exchange trades and stronger enforcement of best-execution standards, but the core trade-through prohibition remains in place and is widely viewed as essential.

## See also

<div class="wiki-seealso">

### Closely related

- [Best execution](/), — the broker's duty to provide prices and terms no worse than the national best bid-ask
- [Bid-ask spread](/bid-ask-spread/) — the width the rule helps compress
- [Market microstructure](/), — how Reg NMS constrains order flow and routing
- [Alternative trading system](/alternative-trading-system/) — venues that must comply with order protection
- [Market maker](/market-maker-trading/) — liquidity providers affected by the rule's constraints

### Wider context

- [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) — the regulator that issued and enforces Reg NMS
- [New York Stock Exchange](/new-york-stock-exchange/) — the primary venue affected by the rule
- [Nasdaq](/nasdaq/) — the competing venue also protected by the rule
- [Limit Up-Limit Down Rule](/limit-up-limit-down-rule/) — complementary price-protection mechanism
- [High-frequency trading](/), — trading strategy affected by order protection and execution speed

</div>

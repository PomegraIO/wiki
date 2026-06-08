---
title: "Retail Order Routing vs Direct Market Access"
description: "How retail brokers route orders through intermediaries versus direct market access (DMA), affecting execution price, speed, and transparency."
keywords:
  - order routing retail
  - direct market access dma
  - broker routing
  - execution quality
  - trade execution
  - market access
image: "/svg/trading.svg"
---

*In **retail order routing vs direct market access**, the distinction lies in whether a trader's order passes through a broker's internal systems and wholesalers (retail routing) or travels directly from the trader's terminal to the exchange (DMA). Retail brokers route orders to earn rebates and execution rebates; direct market access traders see the order book in real time and are responsible for their own execution at the cost of higher fees.*

## How Retail Order Routing Works

When a retail trader places an order at a standard brokerage, the order does not immediately hit an exchange. Instead, it reaches the broker's order management system. The broker then decides where to send the order—typically to a [market maker](/market-maker-trading/) or wholesaler, an internal broker-dealer affiliate, or a [market maker](/market-maker-trading/) on an exchange. This process is called order routing, and it is regulated under Regulation SHO and Regulation FD by the SEC.

The broker faces a choice: route the order to the venue offering the best execution, or route it to a venue paying the highest rebate to the broker. Brokers are required by [Securities and Exchange Commission](/securities-and-exchange-commission/) rules to route orders to achieve "best execution"—the most favorable terms for the customer in terms of price and speed. However, rebate structures create an incentive alignment problem. If a market maker pays the broker 0.5 cents per share to receive retail flow, the broker profits even if the execution price is not optimal.

Retail orders are typically small (100–1,000 shares) and originate from retail clients, so brokers bundle them and send them to wholesalers like Citadel Securities or Virtu Financial. These wholesalers internalize the order—they buy or sell against their own inventory to fill the retail order—rather than routing it to the exchange. This is called off-exchange routing or the over-the-counter market.

## Price Improvement and Rebate Economics

Market makers who receive retail order flow provide [bid-ask-spread](/bid-ask-spread/) improvements as a competitive tool. If a stock's exchange bid-ask spread is $100.00–$100.01, an internalizing market maker might quote $100.002 bid and $100.008 ask to the broker's customers, pocketing the difference. To the retail trader, this looks like a profit—0.2 cents better than the best exchange quote. In aggregate, data from FINRA (Financial Industry Regulatory Authority) shows retail investors receive price improvement on 30–40% of orders, with an average improvement of 0.5–2 cents per share, depending on the stock's liquidity.

Brokers argue this is a net benefit: the retail trader gets better price, and the market maker profits from volume and the spread. However, some researchers point out that a retail trader using [direct market access](/direct-market-access/) might have routed a larger order to the exchange and discovered hidden depth that would have filled at a better price than both the exchange quote and the market maker's quote.

## What is Direct Market Access?

[Direct Market Access](/direct-market-access/) (DMA) is a service offered primarily to professional or institutional traders, though some brokers now offer it to sophisticated retail clients. In DMA, the trader's order does not pass through a broker's matching engine. Instead, the trader's terminal connects directly to the exchange's order book via a broker's infrastructure. The trader sees real-time [price discovery](/price-discovery/) on the exchange and submits orders that compete with all other market participants.

DMA requires a different operational setup. The trader must use specialized software (often a trading platform or API), have lower latency connectivity, and take on responsibility for order management and execution risk. There is no automatic price improvement; the trader faces the public [bid-ask-spread](/bid-ask-spread/). However, the trader can see all visible [limit order](/limit-order/) depth and trade with full information. Large orders can be submitted during lower-volume periods to discover hidden liquidity that market makers may not offer.

DMA is the standard for [hedge fund](/hedge-fund/) traders, proprietary trading firms, and active day traders. Retail brokers like Interactive Brokers and Lightspeed offer DMA to retail clients, but the cost structure is different—brokers charge a per-share or per-order fee (typically $0.001–$0.01 per share) rather than earning rebates from market makers.

## Execution Quality: Speed and Transparency

Retail order routing offers simplicity and often speed. Because wholesalers are highly capitalized and process millions of orders per day, they fill retail orders in 50–200 milliseconds on average. The trader doesn't need to think about order management. However, the lack of transparency is the tradeoff. The retail trader does not see where their order goes, what prices are available at competitors, or whether a better venue exists.

[Direct market access](/direct-market-access/) offers full transparency and control. The trader can see the entire order book and can optimize order timing and size to minimize market impact. For large orders, DMA allows the trader to split the order across multiple venues, use algorithms to minimize slippage, or hold at a specific price level until conditions improve. The downside is latency sensitivity—a trader on a slow connection may miss price opportunities, and the trader must manage their own order logic.

## Regulatory Oversight and Market Quality

The SEC and FINRA monitor retail order routing through Form ATS (Alternative Trading Systems) disclosures and periodic reviews. Brokers must publish annual reports on the venues to which they route orders and the execution quality achieved at each venue. In recent years, regulatory focus has intensified on wholesaler market making and order internalization, with the SEC examining whether rebates create perverse incentives that harm retail execution.

[Regulation SHO](/securities-and-exchange-commission/) requires brokers to route short-sale orders to a [primary market](/primary-market/) venue (typically an exchange) rather than internalizing them, reducing the wholesaler's ability to profit from internalizing short stock on retail accounts.

## Cost and Accessibility

Standard retail brokerage—with wholesaler routing—is effectively free to retail traders. The market maker pays the broker, so the retail trader pays no direct fee. This democratizes market access; anyone can open an account and trade.

[Direct market access](/direct-market-access/) has explicit costs: per-share fees, platform subscriptions, or monthly minimums. A retail trader doing 100 trades per month at 100 shares per trade would pay 100 × 100 × $0.001 = $10 in execution fees, plus platform costs. For small retail accounts, this is prohibitive. DMA is economical for active traders with account sizes above $10,000–$25,000 or for institutional clients for whom execution quality outweighs the fee.

## See also

<div class="wiki-seealso">

### Closely related

- [Direct Market Access](/direct-market-access/) — full order-book visibility and exchange routing for professional traders
- [Market Maker Trading](/market-maker-trading/) — how wholesalers profit from internalizing retail flow
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of immediate liquidity and how it varies by routing venue
- [Limit Order](/limit-order/) — order type and behavior under different routing models
- [Price Discovery](/price-discovery/) — role of exchange order books and wholesaler internalization

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — U.S. regulator overseeing routing rules and best execution
- [Stock Exchange](/stock-exchange/) — primary trading venues where orders can be routed
- [Over-the-Counter Market](/over-the-counter-market/) — off-exchange trading and wholesaler internalization
- [Algorithmic Trading](/algorithmic-trading/) — how institutional orders optimize routing and timing

</div>

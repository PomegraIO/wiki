---
title: "FX Order Matching: Price-Time Priority Explained"
description: "Understand how electronic forex venues rank and fill orders using price-time priority rules and what it means for execution quality."
keywords:
  - fx order matching price time priority
  - price-time priority
  - order matching rules
  - forex execution
  - limit order queue
image: "/svg/forex.svg"
---

*On electronic currency trading venues, **FX order matching** using price-time priority means that orders to buy or sell are filled in two steps: first, all orders at the best price are considered; second, among orders at that price, the oldest (earliest) order fills first. This rule promotes fairness and predictability, though it differs from how [over-the-counter](/over-the-counter-market/) forex dealers operate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Order Matching: Price-Time Priority — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex." />

<div class="wiki-infobox-caption">Price first, time second — the standard for transparent venues.</div>

|   |   |
|---|---|
| **Primary Rule** | Highest bid or lowest ask fills first |
| **Secondary Rule** | If multiple orders at same price, oldest order fills first |
| **Venue Type** | Electronic communication networks, some forex exchanges |
| **OTC Dealer Model** | No price-time priority; negotiated quotes instead |
| **Impact on Traders** | Queue position affects fill speed and certainty |

</aside>

## The Two-Tier Matching Process

**FX order matching** on electronic platforms applies a strict hierarchy. The first tier is price: all buy [limit orders](/limit-order/) at 1.0900 are worthless if someone is willing to sell at 1.0899, and they will not execute. The sell order at 1.0899 takes priority because it offers better terms (lower price for a buyer).

The second tier is time: once price is equal, the queue is ordered by arrival. If two buy orders both sit at 1.0900 and a sell order arrives at that price, the older of the two buy orders fills first. This is **price-time priority**.

The rule is intuitive for stock exchanges, where it has been standard for decades. On the New York Stock Exchange, an investor who submits a buy order at \$100 cannot jump ahead of another investor who submitted an identical order moments earlier. Fairness and predictability flow from this rule.

## Why Forex Is Different: The OTC Market

Traditional foreign exchange is an over-the-counter market, not an exchange. Banks and dealers do not run transparent order books with published prices and queues. Instead, dealers quote prices (bid and ask) and customers request fills. There is no price-time priority because there is no published queue.

A customer calls a bank's currency desk and says, "I want to sell 10 million euros." The desk quotes a bid price based on its inventory, recent [market maker](/market-maker-trading/) data, and risk. If the customer accepts, the trade happens instantly at the negotiated price. Another customer who called a moment earlier might have gotten a different (better or worse) price simply because market conditions changed in those few seconds.

This OTC model still dominates most high-volume forex trading. It allows dealers to exercise judgment, manage inventory efficiently, and tailor pricing to client relationships. But it sacrifices the transparency and fairness of a queued market.

## Electronic FX Venues and Price-Time Rules

Newer electronic forex venues — particularly [alternative trading systems](/alternative-trading-system/) and some smaller exchanges — do publish order books and apply price-time priority. Examples include some multi-bank electronic communication networks and retail forex platforms.

On these venues, a trader submits a limit order to buy EUR/USD at 1.0900. The platform places that order in a queue. If the price at which the order can execute is 1.0900, the order is queued in time order with all other 1.0900 buy orders. When a seller arrives willing to sell at 1.0900 (or better), the oldest buy order at 1.0900 fills first.

This model is deterministic. Traders know their position in the queue and can predict (barring partial fills) whether they are likely to execute. If a trader places a buy order at 1.0900 and there are already 100 million euros of buy interest at that price ahead of them, they know they are deep in the queue and might fill slowly or not at all if the price moves away.

## Price as the Dominant Factor

The price tier dominates overwhelmingly. A buy [market order](/market-order/) (willing to buy at any price) will fill against the lowest sell offers on the book, regardless of how young or old those sell orders are. Time matters only at the margin — when prices are equal.

Consider an example: on an electronic FX venue, the order book shows:

| Buyers | Price | Sellers |
|--------|-------|---------|
| 50M @ 1.0900 (old) | 1.0900 | — |
| 30M @ 1.0899 | 1.0899 | — |
| — | 1.0898 | 20M @ 1.0898 (old) |
| — | 1.0897 | 40M @ 1.0897 (new) |

If a sell market order arrives for 15M EUR/USD, it will hit the 50M buy interest at 1.0900 (the best price), filling 15M against the oldest buyer at that price, completely filling the 15M sell order. The 50M buy order is reduced to 35M.

If, instead, a buy market order arrives for 25M, it will hit the 20M sell interest at 1.0898 (the best price for the buyer), filling 20M. The remaining 5M of the buy order then moves to 1.0897, hitting the 40M sell interest there. Since the 1.0897 sellers are newer (they arrived after the 1.0898 sellers), this does not matter: the 1.0898 price is better, so they were hit first.

## Queue Position and Execution Certainty

Traders who submit limit orders at high-volume prices face queue risk: their order is in a queue, and they do not know when or if it will fill. If you place a buy order at the current best bid, you are at the back of a queue. If three times the order size in buy interest is ahead of you, you might fill partially or not at all.

This is why some traders submit orders at prices away from the current market ("leaning" on the bid or ask). A trader who is confident that a currency will move upward might place a buy order at 1.0900 even if the current bid is 1.0898. The order sits in the queue, waiting. If the currency does not move, they do not fill and do not incur [slippage](/bid-ask-spread/). If the currency rallies to 1.0900, they fill at their preferred price. But they are now at risk that another buyer submits a limit order at 1.0900 ahead of them and gets priority.

Actively managed traders and algorithms often manage queue position actively, pulling and resubmitting orders to stay at the front of the queue or to shift away from crowded prices. This is a cost of electronic trading: traders who want certainty of execution must be willing to cross the [bid-ask spread](/bid-ask-spread/) (accept a market order) or wait in a queue (accept a limit order that may or may not fill).

## Comparison to Market-Maker Pricing

In the OTC interbank market, there is no queue. A dealer prices EUR/USD at 1.0900 bid / 1.0901 ask. Both are available immediately — the ask is the dealer's offer to sell, and the bid is the dealer's willingness to buy. A customer pays the ask to buy (and is filled immediately) or receives the bid to sell (also immediate).

The difference between the electronic venue (queue, price-time priority) and the OTC market (immediate quotes, negotiated prices) reflects a tradeoff. Electronic venues offer transparency and fairness but require traders to compete in a queue. OTC markets offer immediate liquidity and negotiability but lack transparency.

Many large banks and algorithmic traders operate on both. They use electronic venues for core currency pairs (where liquidity is deep and the queue is fast) and call OTC dealers for exotic pairs or large notional amounts (where publishing an order book would expose the bank to excessive [inventory risk](/counterparty-risk/)).

## Impact on Retail and Institutional Traders

For retail forex traders using platforms like the ones provided by forex brokers, price-time priority is standard because those platforms run electronic order books. A retail trader's limit order is queued fairly against other retail orders (and sometimes institutional orders on the same electronic network).

For institutional traders and corporates executing large trades, the OTC market remains more common. A treasury team handling a \$50 million currency purchase will contact banks, request quotes, and negotiate a price tailored to their credit and relationship. They are not joining a retail queue; they are negotiating with dealers.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — orders that sit in a queue until price is reached
- [Market order](/market-order/) — orders that execute immediately, skipping the queue
- [Bid-ask spread](/bid-ask-spread/) — the cost of crossing the spread vs. waiting in queue
- [Market maker](/market-maker-trading/) — dealers who provide OTC prices
- [Alternative trading system](/alternative-trading-system/) — electronic venues with transparent order books

### Wider context

- [Over-the-counter market](/over-the-counter-market/) — the traditional dealer-based forex market
- [Execution](/algorithmic-trading/) — quality of fills and slippage
- [Counterparty risk](/counterparty-risk/) — why dealers manage inventory carefully
- [Forex mechanics](/forex-value-date-vs-settlement-date/) — broader forex trading structure

</div>

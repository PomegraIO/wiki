---
title: "Trade Execution Quality: Key Metrics Explained"
description: "Standard measures brokers and regulators use to evaluate whether an order was filled well, including effective spread, fill rate, and price improvement."
keywords:
  - trade execution quality
  - execution quality metrics
  - effective spread
  - price improvement rate
  - fill rate trading
  - market impact cost
image: /svg/trading.svg
---

*A broker's job is to fill your order as close to fair value as possible. **Trade execution quality metrics** are the standardized tools used to measure whether that happened, and they matter because sloppy execution can erode returns faster than you notice. Regulators require brokers to report these measures, and smart traders use them to shop between firms.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Execution Quality Metrics — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">How well a broker fills your order, measured objectively.</div>

|   |   |
|---|---|
| **Effective spread** | Actual [bid-ask-spread](/bid-ask-spread/) you paid versus the quoted spread at the time of order entry |
| **Price improvement** | How often your order fills *inside* the best bid/ask, saving you money |
| **Fill rate** | Percentage of your order quantity that executes; low rates signal poor [execution-risk](/execution-risk/) |
| **Order-to-execution time** | Latency between order submission and fill; matters for [market-order](/market-order/) and intraday trading |
| **Partial fill risk** | You intend 100 shares but get 60; rest canceled or filled at worse price |
| **Slow traders** | Small brokers may route to cheaper venues, filling slower but potentially cheaper overall |

</aside>

## Effective Spread: What You Actually Pay

The most common execution quality metric is **effective spread**. It compares what you actually paid to the quoted spread at the moment your order entered the market.

Suppose at 10:00:05 the stock quotes $50.00 bid / $50.10 ask (a 10-cent quoted spread). You enter a [market-order](/market-order/) to buy 100 shares. The broker fills you at $50.08. Your effective spread is 8 cents, better than the quoted 10-cent spread.

This sounds good, but here is the catch: your order may have moved the price. If you are buying a large block, you absorb the cumulative ask prices as supply dries up. The broker may have gotten you $50.08 on the first 50 shares but then paid $50.11 and $50.12 for the remaining 50. Your weighted average was $50.095—giving you a much worse effective spread than the 8 cents at the entry quote.

The effective spread is expressed in cents (or basis points, where 1 basis point = 0.01%), and lower is always better. For liquid stocks, effective spreads should be tight—often a few cents. For illiquid stocks or [over-the-counter-market](/over-the-counter-market/) instruments, they balloon.

## Price Improvement: Beating the Spread

A trader wins when the execution price falls *inside* the best bid-ask at order entry. This is called **price improvement** (or "price enhancement" in some databases).

Example: stock quotes $50.00 bid / $50.10 ask. You enter a buy limit order at $50.05. A seller crosses the spread and hits your limit. You filled at $50.05, which is inside the quoted spread, saving you 5 cents per share compared to the ask price.

Price improvement happens when:
- The broker holds inventory and fills you from it at an internal price.
- The broker routes your order to a [market-maker](/market-maker-trading/) who improves the quote.
- [Algorithmic-trading](/algorithmic-trading/) execution gradually accumulates shares from multiple sources at progressively better prices.

Regulators require brokers to disclose the percentage of customer orders receiving price improvement. A broker claiming 0% price improvement is either trading illiquid instruments or behaving poorly. The industry average for liquid stocks is often 30–60%, though this varies sharply by venue and instrument.

## Fill Rate and Partial Fills

**Fill rate** measures what percentage of your intended order size actually executed. A 100% fill rate means you got all 100 shares. An 80% fill rate means you got 80 and the remaining 20 were canceled (or never reached the market).

Partial fills happen when:
- The market has insufficient liquidity at your limit price, so only some shares crossed.
- The broker times out or cancels the remainder after a set period.
- You set an instruction like "fill-or-kill" (execute immediately in full or cancel entirely).

A consistently low fill rate across many orders signals [execution-risk](/execution-risk/) or poor routing. If you consistently get 60% of your intended quantity, your portfolio is not what you think it is—you are under-positioned. This is especially painful for options traders, where a partial fill can leave you with an unhedged exposure.

For [limit-order](/limit-order/) submissions on illiquid assets, some partial fill is normal. But for liquid stocks on a single exchange, a 100% fill should be expected unless you set a restrictive condition.

## Market Impact and Realized Spread

**Market impact** is the price movement caused by your own order. When you buy, you are (on average) pushing the stock up. When you sell, you are pushing it down. This is separate from the bid-ask spread; it is the cost of moving the market yourself.

The **realized spread** accounts for market impact. It is calculated as:

Realized spread = (Execution price − Midpoint at entry) − (Midpoint at some future time − Midpoint at entry)

In simpler terms: how much better (or worse) than the entry midpoint did you fill, and did the price then move in your direction or against you after you traded?

A trader who buys at $50.05 (midpoint $50.00) but sees the stock fall to $49.95 five minutes later realizes a worse spread ex-post than ex-ante. Conversely, buying at $50.05 and watching the stock climb to $50.15 yields realized gains beyond the execution. Realized spreads matter for managers evaluating their own trading performance over time.

## Venue Comparison and Routing

Execution quality varies across venues. The New York Stock Exchange, NASDAQ, and various electronic communication networks each have different [market-maker](/market-maker-trading/) populations, technology, and order flow patterns. A smart [broker](/broker/) routes your order to the venue where it is most likely to achieve tight execution for your order size and style.

Brokers publish quarterly **execution quality reports** comparing fills across venues. A report might show that on-exchange orders in a stock get an average effective spread of 1.5 cents, while off-exchange (alternative) venues deliver 1.2 cents. This informs the broker's routing algorithm for the next quarter.

Retail brokers often route to market makers who pay for retail order flow, allowing the broker to zero commissions but potentially reducing execution quality. Institutional brokers compete on execution metrics directly, displaying detailed reports and winning business by demonstrating superior fills quarter over quarter.

## Measuring Execution Quality Over Time

A trader or fund evaluates their broker's execution quality by:

1. **Tracking effective spread** on a sample of recent orders, grouping by stock and order size.
2. **Monitoring fill rates** to ensure orders are not quietly being canceled or left unfilled.
3. **Comparing price improvement** percentages against industry benchmarks for that instrument class.
4. **Reviewing order-to-execution time**, especially for time-sensitive trades where speed is a feature, not a bug.
5. **Stress-testing during volatility**, when market impact and partial fills rise; a broker's quality is tested in stress, not calm.

Most institutional brokers now publish these metrics in real-time dashboards or quarterly summaries. A trader switching brokers should request a sample execution report for similar orders in their usual stock and size range.

## The Regulatory Angle

Regulators (like FINRA in the US and the FCA in the UK) require brokers to report execution quality to customers. This stems from the principle of "best execution"—a broker must demonstrate that orders are routed and filled in the customer's best interest, not the broker's profit. Venues must also publish execution quality statistics so traders can see where fills are tightest.

These rules prevent brokers from quietly accepting worse fills if they receive a kickback from a venue, and they let traders see whether their broker is genuinely competing for their order flow or accepting mediocre fills in exchange for higher commissions elsewhere.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the quoted spread your execution quality is measured against
- [Market order](/market-order/) — immediate fills; execution quality depends on liquidity and order size
- [Limit order](/limit-order/) — you control the price; execution quality depends on patience and venue routing
- [Execution risk](/execution-risk/) — why orders may not fill as intended
- [Market maker trading](/market-maker-trading/) — who provides liquidity and how they profit from spreads

### Wider context

- [Broker](/broker/) — your intermediary in execution
- [Stock exchange](/stock-exchange/) — where execution quality is measured
- [Algorithmic trading](/algorithmic-trading/) — techniques to improve execution quality for large orders
- [Price discovery](/price-discovery/) — how markets aggregate information and set fair value

</div>

---
title: "Fill Rate Optimization"
description: "Techniques for maximising the proportion of a limit order that executes without widening the bid-ask spread or triggering adverse price movement."
keywords:
  - fill rate
  - order execution
  - limit order
  - market impact
  - order routing
  - execution algorithm
image: "/svg/trading.svg"
---

*A **fill rate** is the percentage of an order that executes at the specified [limit price](/limit-order/) or better. High fill rates are desirable—they mean your order actually gets done—but they often come with a trade-off: wider spreads, longer waits, or partial executions. **Fill rate optimization** is the discipline of balancing execution certainty against cost, using timing, venue selection, and pricing tactics.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fill Rate Optimization — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">The art of executing more of your order without paying more than necessary.</div>

|   |   |
|---|---|
| **What it measures** | Percentage of an order that executes at the limit price or better |
| **Key trade-off** | High fill rate vs. low execution cost |
| **Limit order fill rate** | Typically 30–80% depending on spread width and order size |
| **Market order fill rate** | 100%, but slips against the [bid-ask spread](/bid-ask-spread/) |
| **Main tactics** | Patience, venue routing, pricing adjustment, time-of-day |
| **Metric tracked by traders** | Partial vs. full execution, execution price vs. VWAP |

</aside>

## The fundamental tension

A trader facing a tight [bid-ask spread](/bid-ask-spread/) who places a [limit order](/limit-order/) to sell at the midpoint might watch the stock move up without executing—the order never fills because the ask price moves higher. A trader who places a [limit order](/limit-order/) 1% below the ask will execute more of the order, but pays 1% in slippage. A trader who hits the bid outright fills immediately but gives up the entire spread.

Fill rate optimization is the search for the sweet spot: the limit price that maximizes the probability of execution without incurring unreasonable market impact or slippage. In liquid names like large-cap equities, the answer is often simple—place orders near the [bid-ask spread](/bid-ask-spread/) and wait. In illiquid securities, there may be no sweet spot: any acceptable limit price results in low fills, and any generous price that ensures a high fill rate costs too much.

## Pricing tactics

The simplest approach is **patience and incremental repricing**. A trader submits a [limit order](/limit-order/) to sell 100,000 shares at the ask price. If it doesn't fill within a few seconds, the trader reprices 1 cent lower. If still no fill, another cent lower. This "walk down" technique gradually moves the order price toward equilibrium, accepting some slippage to achieve a higher fill rate.

Conversely, a trader eager to fill might place an order that "lifts" the offer—placing a sell order above the current ask to signal willingness to trade at a better price. This attracts buyers and increases fill probability at the cost of giving away upside.

**Time-of-day effects** matter. In the opening minutes of trading, spreads are often wide and fill rates are low as liquidity is sparse. Mid-day (9:30 AM to 3:30 PM in U.S. equity markets, with peak liquidity around 10 AM to 2 PM) spreads tighten and fill rates improve. A trader with flexibility might time large limit orders for peak liquidity windows.

**Order sizing** also affects fill rate. A single large order for 500,000 shares will partly scare off the other side; the same order split into five orders of 100,000 fills more readily because it doesn't signal urgency. [Algorithmic trading](/algorithmic-trading/) systems exploit this insight, breaking large orders into smaller child orders and executing them gradually to avoid signalling the full size to the market.

## Venue routing and venue selection

Different trading venues have different liquidity profiles. A large-cap stock trades on [NASDAQ](/nasdaq/) and the [New York Stock Exchange](/new-york-stock-exchange/), but also on regional exchanges and in off-exchange venues. A trader looking to maximize fill rate might route small [market orders](/market-order/) to the venue with the tightest spread (usually determined by rule as part of "best execution" duty), but route [limit orders](/limit-order/) to multiple venues simultaneously—a practice called "order spreading."

[Alternative trading systems](/alternative-trading-system/) (dark pools, ECNs) offer a different calculus. A trader placing a large block order in a dark pool with sparse quotes might achieve lower fill rate but avoid the market impact of showing the full size publicly. The choice between high-visibility venues (best fill rate certainty) and hidden venues (lower cost if you do fill) depends on the trader's priorities.

## Algorithmic approaches

[Algorithmic trading](/algorithmic-trading/) systems optimize fill rate systematically. A **VWAP algorithm** (volume-weighted average price) executes a target order at a rate proportional to market volume throughout the day, aiming to stay under the radar by never appearing to trade more aggressively than the market itself. This typically achieves high fill rates because the algo is never ahead of or behind natural volume.

An **Implementation shortfall algorithm** sets a target price (often a forecast of the day's close or VWAP) and adaptively adjusts urgency: if the order is ahead of schedule, it slows down and places tighter [limit orders](/limit-order/). If it is behind, it accelerates and pays up slightly to catch up. The aim is to minimize the difference between achieved execution and the target benchmark.

Other algorithms monitor the limit order book in real time, detecting pockets of liquidity and routing orders there. If a large bid emerges at a particular price level, an algorithm can execute into it immediately, knowing the fill rate just jumped.

## The cost of high fill rates

A trader pursuing a 90%+ fill rate on a large order is implicitly accepting higher execution costs. Studies of execution quality show that traders paying wider spreads or trading at off-peak times achieve higher fill rates, but the cost per share rises. Conversely, traders willing to accept low fill rates (e.g., a 40% fill rate on a tight [limit order](/limit-order/)) often achieve better average prices on the quantity that does fill.

This has spawned a secondary metric: **execution efficiency**. Rather than measuring fill rate alone, traders compare the cost per share filled against benchmarks like VWAP or the midpoint. A 50% fill rate at an excellent price might be preferable to a 100% fill rate (via [market order](/market-order/)) at a poor price.

## Regulatory and market structure considerations

U.S. regulators require brokers to seek "best execution," which includes fill quality, not just price. A broker routing [limit orders](/limit-order/) to a venue with a very wide spread to maximize rebates (if the venue pays the broker for order flow) may violate best execution obligations. Regulators regularly fine brokers for conflicts between rebate maximization and client interest.

High-frequency traders also affect fill rates. In highly competitive markets, HFT firms rapidly adjust their [bid-ask spreads](/bid-ask-spread/) and can "snipe" incoming limit orders by lifting the opposite side of the book just as a large order arrives. Retail traders and institutional traders have become aware of this, leading to greater use of dark pools and more opaque order routing to avoid such front-running.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — The order type at the heart of fill rate optimization
- [Market order](/market-order/) — An order that guarantees fill but accepts whatever price the market offers
- [Bid-ask spread](/bid-ask-spread/) — The cost of immediacy, which limits fill rate on tight limit orders
- [Algorithmic trading](/algorithmic-trading/) — Automated systems that optimize fill rate systematically
- Order routing — Choosing which venues to send orders to
- [Participation of volume algorithm](/participation-of-volume-algorithm/) — An algo that optimizes fill by matching market volume

### Wider context

- Market impact — How order size affects fill rates and prices
- [Price discovery](/price-discovery/) — The role limit orders play in discovering fair value
- [Execution risk](/execution-risk/) — The risk that an order doesn't fill
- [Liquidity risk](/liquidity-risk/) — The risk that liquidity disappears when you try to trade

</div>

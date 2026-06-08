---
title: "TWAP Order"
description: "An algorithmic execution strategy that splits a large order into equal parcels over fixed time intervals to match the day's time-weighted average price."
keywords:
  - twap order
  - time-weighted average price
  - execution algorithm
  - algorithmic execution
  - order slicing
image: "/svg/trading.svg"
---

*A **TWAP order** (time-weighted average price) is an execution algorithm that divides a large order into smaller tranches released at regular time intervals throughout a trading session or longer period. The goal is to execute at or near the time-weighted average price for the day—not the volume-weighted average, but the simple average price across equal time buckets. A trader who cannot or prefers not to move the market with a single large order uses TWAP to drip inventory into the market steadily.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TWAP Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and order mechanics." />

<div class="wiki-infobox-caption">Steady time-based tranches minimize market impact.</div>

|   |   |
|---|---|
| **What it is** | Algorithmic execution splitting an order into equal parcels at regular time intervals |
| **Target metric** | Time-weighted average price (price × equal time slices, not volume) |
| **Duration** | Intraday, multiday, or custom window set by trader or algorithm |
| **Key advantage** | Predictable, transparent slicing; avoids predatory front-running based on order size |
| **Common use** | Passive rebalancing, fund flows, non-urgent large orders |

</aside>

## Why split by time, not by volume

The market price changes every second. Volume floods in and dries up unpredictably. A trader holding 10 million shares to sell cannot simply release them all at once; the market would crater. One option is to watch volume, selling fast when it swells (this is [VWAP](/guaranteed-vwap-order/), the volume-weighted approach). Another is to ignore volume entirely and sell on a clock: one tranche every 30 minutes, or every hour, or every day, for two weeks. This time-based approach is TWAP.

TWAP does not guarantee you the best prices during busy hours or calm hours. It guarantees you a mechanical, transparent algorithm: equal slices at fixed intervals. This has an underrated benefit: your execution is not correlated with your own order size or market sentiment at any single moment. A savvy trader watching for large blocks cannot front-run a TWAP order because they cannot predict when the next slice will hit, only that it will come on the clock.

## The algorithm in practice

A typical TWAP setup specifies a start time, end time, total quantity, and number of slices. Say you want to sell 2 million shares over five trading days, starting 10 a.m. on Monday. The algorithm divides 2 million by the number of 1-minute intervals (let's say 300 intervals per day) and releases roughly 1,333 shares every minute. It does not adjust these tranches based on market price or volume; it follows the clock rigidly.

In reality, most TWAP algorithms add micro-layers. They might hold slices during extreme volatility, release them during calm periods, or vary slightly around the mechanical target to avoid visible patterns. But the core constraint remains: time, not volume, drives execution. Over a long window, the prices paid average out to the "time-weighted average price"—the simple mean of all prices touched, treated equally regardless of how much volume occurred at each price.

## When a trader chooses TWAP over VWAP

A [guaranteed VWAP order](/guaranteed-vwap-order/) locks in the day's volume-weighted average price; the broker absorbs all tracking risk. TWAP leaves tracking risk with you. Why would you accept that? Speed and transparency. A VWAP order often requires broker negotiation, fees, or a "not held" arrangement where the broker takes discretion. A TWAP algorithm is mechanical: it runs on any exchange or broker system and produces predictable outcomes. If you are not in a hurry and can tolerate day-to-day variance, TWAP avoids broker fees and lets you see exactly what you paid at each execution step.

TWAP also works well for traders who want to avoid leaking information. A VWAP order can attract arbitrageurs and other traders who sniff out large pending orders. A TWAP slice arriving every 30 minutes looks like natural market flow; no one knows when the next tranche arrives.

## TWAP in fund flows and rebalancing

Large mutual funds and pension plans use TWAP routinely. When $500 million flows into a [mutual fund](/mutual-fund/) and needs to be allocated to a new position, the portfolio manager does not buy all at once. They submit a TWAP order: buy a slice of each holding every hour for a week, ensuring they do not overwhelm individual stocks and hit diverse prices across different market conditions. The strategy assumes that over time and a steady pace, they will not lose much versus the time-weighted average.

Index funds and [ETF](/etf/) creators also use TWAP during large redemptions or creations. When a fund is redeemed, the manager must sell baskets of underlying stocks. A TWAP algorithm sells them methodically, reducing the risk of a sudden price crash from liquidation pressure.

## Limitations and alternatives

TWAP is simple but not optimal in a volatile or trending market. If prices are rising steadily, your TWAP algorithm sells at rising prices throughout the period, potentially underperforming. If prices fall, you benefit. TWAP does not adjust; it follows the clock. This passivity is both its strength (no discretion, no surprises) and its weakness (no adaptation to market conditions).

[VWAP orders](/guaranteed-vwap-order/) are more precise on a single day but require broker commitment. [Algorithmic execution](/algorithmic-trading/) can be tuned to balance time and volume. Some algorithms blend time and volume: sell more during heavy volume, less during light volume, but stay within a time window and bounds. These are called "volume-participation" or "adaptive" TWAP variants.

## Cost implications

TWAP algorithms are typically free or bundled with standard trade execution. You do not pay a separate fee to your broker for using TWAP; it is a software feature on most modern trading platforms. The cost you bear is opportunity cost: if the market moves against you while you are slicing, you own that loss. A broker running a VWAP guarantee absorbs this; a TWAP algorithm leaves it with you.

Retail traders rarely encounter TWAP directly; institutional investors and professional traders use it constantly for large orders where speed is not the priority and transparency and predictability are.

## See also

<div class="wiki-seealso">

### Closely related

- [Guaranteed VWAP Order](/guaranteed-vwap-order/) — broker-guaranteed volume-weighted alternative
- [Algorithmic Trading](/algorithmic-trading/) — broader category of automated execution strategies
- [Basis Order](/basis-order/) — fixed-spread alternative for basket trading
- Market Impact — the cost TWAP helps minimize
- Execution Algorithm — technical framework for TWAP

### Wider context

- [Mutual Fund](/mutual-fund/) — common user of TWAP for rebalancing
- [Exchange Traded Fund](/etf/) — uses TWAP during large creations and redemptions
- [Liquidity Risk](/liquidity-risk/) — managed by spreading trades over time
- [Price Discovery](/price-discovery/) — not disrupted by TWAP's steady execution
- Market Microstructure — context for TWAP's role in trading

</div>

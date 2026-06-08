---
title: "Arrival Price Benchmark in Trading"
description: "Arrival price benchmark measures execution quality by comparing filled price to the price when the order entered the market, revealing slippage from market impact."
keywords:
  - arrival price benchmark
  - arrival price trading
  - execution quality benchmark
  - market impact slippage
  - vwap vs arrival price
  - decision price
image: "/svg/trading.svg"
---

*The **arrival price benchmark** measures execution quality by comparing the price at which a trade filled to the price when the order first arrived at the exchange. This metric reveals how much the execution actually cost relative to the immediate market condition, isolating the true slippage from temporary market impact alone.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Arrival Price Benchmark — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A straightforward measure of whether an execution was efficient relative to the market price when the order arrived.</div>

|   |   |
|---|---|
| **Definition** | Execution price minus the mid-quote (or VWAP) at time of order entry |
| **Primary use** | Assessing temporary market impact from a single trade |
| **Measured in** | Basis points or cents per share |
| **Time window** | From order submission to final fill |
| **Key comparison** | VWAP, implementation shortfall, post-trade benchmarks |
| **Regulatory context** | Part of best execution reviews under Reg NMS and MiFID II |

</aside>

## What the Arrival Price Benchmark Actually Measures

The arrival price benchmark captures the cost of executing your order relative to where the market stood the moment you entered it. When a trader submits a large order, the market price typically moves against the order—buyers push prices up, sellers push them down. The arrival price benchmark quantifies exactly how far the execution price deviated from that entry-point price.

To calculate it, take the weighted average execution price (or the mid-quote at order submission) and subtract it from the actual filled price. A negative number means execution was better than the arrival price (an unusual but good sign). A positive number means it cost more to fill—the standard case when a large order moves the market.

The benchmark answers one specific question: given where the market was when I submitted this order, how much did my execution cost in terms of temporary price movement?

## How It Differs From VWAP

The [volume-weighted average price](/price-to-earnings-ratio/) (VWAP) is itself an execution target: fill your order as close as possible to today's VWAP. The arrival price benchmark is different in scope. VWAP looks backward at the historical trading day and asks, "Did I beat the day's average?" Arrival price looks at the market state right now and asks, "How much market impact did I incur?"

A trader might beat VWAP but still underperform the arrival price benchmark if the market moved significantly between entry and fill. Conversely, a trader could outperform arrival price but still lag VWAP if VWAP was unusually favorable on the day.

In practice, VWAP suits longer-term algo strategies that are willing to spread their execution across the full trading session. Arrival price benchmarks work best for orders meant to execute quickly—think a 15-minute window—where you care more about "what was the cost relative to now" than "what was the cost relative to the day's average."

## The Distinction From Implementation Shortfall

[Implementation shortfall](/fair-value/) is broader. It measures the total gap between the decision price (where the stock was when you decided to trade) and the final execution price, including any slippage from market movement during the order-execution period and any delay costs if you spread the order over time.

Arrival price benchmark only captures the slippage from execution itself—it assumes you're comparing the entry price to the fill price over the duration of the order. Implementation shortfall also accounts for how long you waited before submitting the order and for any explicit delay you introduced.

An example: You decide to buy at 10:00 a.m. when the price is $50. You wait five minutes and submit the order at 10:05 when it's $50.50. You fill at $50.75 by 10:06. The arrival price slippage is $0.25 ($50.75 − $50.50). The implementation shortfall is $0.75 ($50.75 − $50.00).

## When Market Impact Reversal Matters

A key assumption underlying arrival price benchmarks is that the market impact is partly temporary. When you sell a large block, you depress the price. After your order clears, other traders may buy, or short-sellers may cover, and the price drifts back up. If you measure arrival price slippage right after your fill closes, you might catch the market at a low point—then watch it recover.

Some traders and brokers adjust arrival price calculations to account for this post-trade reversion, especially for large institutional orders. The idea is to ask, "How much of my slippage was permanent and how much will bounce back?" This nuance is critical for interpreting the benchmark fairly: a high arrival price slippage isn't necessarily a sign of poor execution if a meaningful portion reverts within seconds or minutes.

## Why Brokers Report It

[Broker](/broker/) firms and [market maker](/market-maker-trading/) desks publish arrival price benchmarks in trade reports because it isolates their immediate execution quality from other factors. If a client blames you for poor performance, you can show the arrival price metric and say, "The market moved this much against you during the order; my desk executed you at the best available price within that constraint."

For compliance and Reg NMS [best execution](/fair-value/) reviews, the SEC expects broker-dealers to measure execution quality. Arrival price benchmark is one of several standard metrics (along with VWAP, post-trade [market-order](/market-order/) benchmarks, and others). Firms monitor it by order size, venue, time of day, and security to ensure they're not systematically underperforming.

## When to Use It vs. Other Benchmarks

Use the arrival price benchmark when your question is narrow and tactical: "Did I pay too much market impact for this order in the immediate window?" Use VWAP when you're running a longer-dated intraday program and can spread execution across hours. Use [implementation shortfall](/fair-value/) when you want to account for your entire trading decision—from the moment you decided to trade to the moment you finished.

For high-frequency [algorithmic trading](/algorithmic-trading/) strategies, arrival price is often combined with real-time microsecond-level benchmarks to assess each execution burst. For passive investors checking their broker's quarterly performance, arrival price slippage for routine orders is usually small and not the primary measure; total cost of ownership matters more.

## See also

<div class="wiki-seealso">

### Closely related

- [VWAP (Volume-Weighted Average Price)](/price-to-earnings-ratio/) — the full-session target execution price, contrasted with arrival price
- [Implementation Shortfall](/fair-value/) — the broader measure of total execution cost from decision to fill
- [Market Impact](/market-risk/) — how large orders move prices against you
- [Algorithmic Trading](/algorithmic-trading/) — execution strategies that optimize arrival price and other benchmarks
- [Best Execution](/fair-value/) — the regulatory and competitive standard that drives arrival price monitoring

### Wider context

- [Bid-Ask Spread](/bid-ask-spread/) — the baseline cost of trading before market impact
- [Liquidity Risk](/liquidity-risk/) — how order size and market depth drive execution costs
- [Market Microstructure](/fair-value/) — the mechanics of how prices form and orders interact

</div>

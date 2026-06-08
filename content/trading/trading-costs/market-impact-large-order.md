---
title: "Market Impact of a Large Order"
description: "How a large trade moves the price against you; strategies to break up orders and minimize the cost of executing substantial positions."
keywords:
  - market impact large order
  - price impact execution cost
  - order execution strategy
  - slippage trading
  - block trading
image: /svg/trading.svg
---

*The **market impact** of a large order is the price movement caused by the order itself—the cost of announcing to the market that you want to buy or sell a huge block. A trader seeking to execute 500,000 shares cannot always do so at the mid-market price; the sheer volume pushes price against them. Understanding and minimizing this impact is central to professional execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market Impact — Key Facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The price movement caused by your order, separate from general market moves; larger for less liquid securities and bigger blocks.</div>

|   |   |
|---|---|
| **What it is** | Price movement caused by the order itself, not by news or broader market sentiment |
| **Size of impact** | Grows with order size and inversely with [market liquidity](/liquidity-risk/) |
| **Measured in** | Basis points; a 5 bp impact means you lose 0.05% to execution cost |
| **Affects whom** | Institutional buyers/sellers with large positions; retail trades are negligible |
| **Permanent vs. temporary** | Permanent: long-term price change; temporary: bounce-back within minutes |
| **Mitigated by** | Breaking orders into smaller pieces, using [algorithmic-trading](/algorithmic-trading/), patient execution |

</aside>

## Why large orders move the market

When you place an order to buy 100 shares of a liquid stock, nobody notices. The market has thousands of shares offered at the [ask](/bid-ask-spread/), and your order gets filled instantly at the best available price. But when you place an order to buy 100,000 shares of that same stock, you exhaust the first few price levels entirely. To fill the full order, you must accept progressively worse prices, moving up through the order book until you've bought enough shares. The market has moved against you—and stayed there.

This is **permanent market impact**. You've absorbed all the available supply at the initial price level, so subsequent buyers must bid higher. From the market's perspective, your large order revealed that demand exists, and price equilibrium shifted upward.

There is also **temporary impact**: the immediate slippage as your order hits the book, followed by a partial bounce-back as other traders perceive you as a one-time buyer, not a new structural source of demand. Some temporary impact recovers within minutes; permanent impact usually persists.

## How size affects impact nonlinearly

Market impact does not scale linearly with order size. Doubling your order size does not double your execution cost. Instead, impact typically grows with the square root of size, or worse. This is because liquidity is concentrated at the best bid-ask levels, and you deplete it quickly.

**Illustrative example:**
- Buying 10,000 shares at a $50 mid-price might cost you 1 bp (0.01%) in total market impact.
- Buying 100,000 shares—10× larger—might cost 15 bp (0.15%), not 10 bp.
- Buying 1,000,000 shares might cost 80 bp (0.80%), not 100 bp.

The exact function depends on the security's liquidity and volatility. A mega-cap stock like Apple has deep order books and suffers less impact per share. A small-cap stock or illiquid [bond](/bond/) can suffer severe impact from a large order.

## Measuring market impact before execution

Professional traders estimate market impact before they execute. A few approaches:

**Historical analysis:** Review how the stock's price responded to large orders of similar size in the past. If you're planning to buy 100,000 shares and the stock historically moves 20 bp for 100,000-share buys, expect a 20 bp cost.

**Liquidity models:** Large asset managers use [algorithmic-trading](/algorithmic-trading/) systems with built-in liquidity models. These systems estimate the order book depth ahead of time and forecast impact. A typical model might say: "Executing this 500,000-share order will cost 25 bp."

**Peer discussion:** Institutional traders often discuss execution costs with brokers and other traders. A broker's pre-trade analytics tools (like Instinet's or Morgan Stanley's execution-quality reports) provide impact forecasts.

**Market microstructure data:** Academic and professional firms analyze tick-by-tick trades to build impact surfaces—tables showing expected impact by order size and volatility for each stock.

## Breaking the order into pieces

The standard solution to large market impact is **order splitting**: breaking one large order into many smaller orders over time or across venues. Instead of buying 1,000,000 shares in one go, a trader might buy 100,000 shares per day for 10 days, or use a [VWAP](/vwap-execution-cost-benchmark/) algorithm to split the order across hours.

By splitting, you:

1. **Reduce per-tranche impact:** Each smaller tranche has lower individual impact.
2. **Disguise intent:** The market doesn't know you're planning a 1,000,000-share purchase, so competition is less fierce.
3. **Exploit volatility:** If the stock rallies on day 2, you may fill earlier tranches cheaply and later tranches at the market.

The trade-off is execution risk: if the stock rallies sharply on day 1, your later tranches may miss the move entirely. A patient buyer willing to execute over a week saves impact cost but risks missing an upturn.

## Algorithmic execution strategies

Modern trading floors rely on algorithms to minimize market impact. Common strategies include:

**VWAP (Volume-Weighted Average Price):** Execute the order proportionally to the stock's historical volume pattern. If 20% of daily volume normally trades in the first hour, execute 20% of your order then. This keeps your order in line with natural market rhythm.

**TWAP (Time-Weighted Average Price):** Split the order evenly across time. Execute 1/10 of your order every 6 minutes for an hour. Simple and predictable, though can cause impact during low-volume periods.

**Arrival Price:** Minimize the difference between the price when you decided to trade and the average price at execution. This algorithm is aggressive early (filling quickly when impact is lowest) and patient later (scaling back if the stock moves against you).

**Probabilistic trading:** More sophisticated algorithms model the joint dynamics of the stock, [volatility](/historical-volatility/), and order book depth, then optimize the timing and size of each child order. The algorithm might fire 10 child orders per minute, each sized to maximize participation without excessive impact.

## When market impact dominates execution cost

For liquid stocks, [bid-ask-spread](/bid-ask-spread/) and brokerage commission are small. Market impact is the largest execution cost. A trader buying $10,000,000 of SPY (a mega-cap ETF) might incur $5,000 in impact but only $1,000 in commissions.

For illiquid securities—microcap stocks, emerging-market bonds, or corporate [credit-default-swap](/credit-default-swap/) indices—market impact can exceed 50 bp. Some institutional investors refuse to trade illiquid assets in size because impact is unpredictable and severe.

## Permanent vs. temporary impact in practice

Not all market impact is permanent. If you buy 1 million shares and the price rises 50 bp, but then falls back 20 bp within 5 minutes, your permanent impact was 30 bp and temporary impact was 20 bp. Temporary impact reflects the confusion and risk-aversion of other traders; permanent impact reflects the genuine shift in supply-demand equilibrium from your trade.

Algorithms try to minimize permanent impact—the long-term loss—while tolerating temporary impact. Aggressive execution strategies have high temporary impact but might reduce permanent impact (because you're done trading and the market settles).

## See also

<div class="wiki-seealso">

### Closely related

- [VWAP as an Execution Cost Benchmark](/vwap-execution-cost-benchmark/) — Volume-weighted average price as a benchmark for evaluating execution quality
- [Overnight Financing Cost in CFD and Margin Trading](/overnight-financing-cost-cfd/) — Daily costs of holding leveraged positions
- [Algorithmic Trading](/algorithmic-trading/) — Automated strategies to minimize market impact
- [Bid-Ask Spread](/bid-ask-spread/) — The cost of immediacy separate from market impact
- [Short Sale Borrow Cost](/short-sale-borrow-cost/) — The cost of borrowing stock for short sales
- [Limit Order](/limit-order/) — Patient execution at a specified price to avoid market impact
- [Market Maker](/market-maker-trading/) — Liquidity providers whose actions moderate market impact

### Wider context

- [Market Risk](/market-risk/) — The broader risk that prices move before you execute
- [Volatility Smile](/volatility-smile/) — How implied volatility varies by strike, reflecting skew in market impact
- [Price Discovery](/price-discovery/) — How markets determine fair value; large orders participate in this process
- [Over-the-Counter Market](/over-the-counter-market/) — Where block trading occurs with negotiated execution
- [Alternative Trading System](/alternative-trading-system/) — Venues designed for large trades with less market impact

</div>

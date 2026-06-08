---
title: "Market-on-Close and Limit-on-Close Orders Explained"
description: "How MOC and LOC orders work at the closing auction, what determines fill price, and why institutional traders use them to manage end-of-day execution."
keywords:
  - market on close order
  - limit on close order
  - moc loc order execution
  - closing auction orders
  - end-of-day trading mechanics
  - imbalance auction
image: "/svg/trading.svg"
---

*A **market-on-close (MOC)** order executes at the closing auction price—whatever it is—while a **limit-on-close (LOC)** order only fills if the auction price meets your limit. Both are routed to the closing auction rather than the regular trading session, and both protect against the gap risk and volatility of final minutes of the regular session.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market-on-Close and Limit-on-Close — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">End-of-day orders bypass the regular session and execute in a separate closing auction mechanism.</div>

|   |   |
|---|---|
| **MOC order** | Sell or buy at whatever the official closing price turns out to be |
| **LOC order** | Sell or buy at the closing price, only if it's at or better than your limit |
| **Execution time** | 3:50–4:00 PM ET for most US equities |
| **Price determination** | Driven by the [closing auction](/alternative-trading-system/) imbalance algorithm |
| **Fills** | MOC fills guaranteed (at whatever price); LOC may not fill |
| **Main users** | Institutional traders, index funds, passive rebalancers |
| **Advantage over regular market** | Avoids intra-day volatility; guarantees closing-price reference point |

</aside>

## How the closing auction works

The closing auction is a distinct mechanism from the regular trading session. US equity exchanges (NYSE, NASDAQ) halt normal trading around 3:59:59 PM ET and enter a special closing auction window, typically the final minute of the day.

During this period, all MOC and LOC orders that have been queued come into play. The exchange calculates an **imbalance price**—the price that would equate buy and sell volume if executed alone—and uses that as a starting reference. Then, the closing price is set by the auction algorithm: it is the price that maximizes the number of shares that can execute against standing [limit orders](/limit-order/) in the continuous book.

Put simply:
1. Buyers and sellers submit MOC and LOC orders into the queue.
2. The exchange calculates what price would clear the most volume between auction orders and regular limit orders still in the book.
3. All MOC orders (and LOCs at or better than that price) execute at the official close.
4. The closing price becomes the official settlement price for the day, used by funds, indices, and corporate actions.

## MOC orders: guaranteed execution, unknown price

A **market-on-close** order guarantees you will sell or buy at the close, but you accept whatever price the closing auction produces.

**Advantages:**
- Certainty of execution (fills are guaranteed, barring a halted stock or administrative error)
- Reference to the official closing price (used by [index funds](/index-fund/), rebalancers, and corporate indices)
- Avoids the chaos of the final minute of regular trading
- Cost certainty for large traders (no guessing about intra-day volatility)

**Risks:**
- You have no control over price; if imbalance is large, the close could be far from your expectation
- If the stock is highly illiquid, the closing price might swing dramatically
- You cannot cancel an MOC order in most systems once it enters the queue (typically 30 minutes before close)

**Example:** You manage a $500 million index fund and must replicate the S&P 500 at the end of the day. You use MOC orders to sell shares you're removing from the portfolio, guaranteeing that your trade settles at the official close price used by the index itself. The actual fill might be 2–3 cents worse than intra-day prices, but that's acceptable given the certainty and the reference-price benefit.

## LOC orders: conditional execution

A **limit-on-close** order says: "Execute at the closing price, but only if that price is at or better than my limit."

**Advantages:**
- You set a floor (for sells) or ceiling (for buys), protecting against extreme imbalances
- Still avoids intra-day volatility
- Combines the reference-price benefit of the closing auction with a safeguard

**Risks:**
- If the closing price misses your limit, you don't execute (and may have to resubmit the order for tomorrow's close)
- Partial fills are possible in some systems (if you submit LOC for 10,000 shares and only 6,000 execute, you're stuck with the mismatch)

**Example:** You're selling a block of 100,000 shares of a thinly traded biotech stock. You believe a fair price is $28.50. You submit an LOC sell order with a limit of $28.50. If the closing auction imbalance pushes the close to $28.60, you sell at $28.60. If it drops to $28.40, your order does not execute, and you try again tomorrow.

## When institutional traders prefer end-of-day crossing

Large institutional traders often favor MOC and LOC orders over intra-day execution for several reasons:

**Market impact:** A massive order can move the intra-day price significantly. By waiting for the close, the trader executes against the full closing-auction volume and a reference price that many other market participants are already accepting.

**Passive rebalancing:** [Index funds](/index-fund/) and passive managers must match the closing price of their benchmark. MOC and LOC orders let them align trades with that official close, ensuring their portfolio's valuation matches their reported NAV.

**Cost averaging:** If a trader executes throughout the day, she captures only the day's prices. By using the closing auction, she gets a single decisive price point, which some strategies prefer for accounting or attribution purposes.

**Regulatory simplicity:** Some regulations or internal compliance rules require traders to execute at the official close. MOC and LOC orders guarantee this.

## Imbalance risk and auction mechanics

The closing-price discovery mechanism can sometimes move sharply if there's a large imbalance of buy orders versus sell orders (or vice versa). The exchange publishes the **closing-imbalance indicator** (usually 15 minutes before close) to warn traders.

A buy imbalance of 5 million shares might push the closing price up from the last regular-session trade. Savvy traders use this information: a seller might submit an LOC order at a slightly lower limit, betting the imbalance will push the close higher. Conversely, a buyer might lower their limit, expecting the imbalance to attract sellers.

However, the auction mechanism is designed to be fair—the official close is set to maximize fill volume, not to benefit any particular participant. Exchanges have rules against manipulating the imbalance, and surveillance is active.

## Differences from other end-of-day strategies

MOC and LOC are distinct from other final-minute approaches:

- **VWAP algorithms** execute gradually throughout the day, trying to match volume-weighted average prices—they do not wait for the close.
- **[Dark pools](/alternative-trading-system/)** and **block crosses** execute large trades off-exchange, often at negotiated or mid-point prices, and are not tied to the official close.
- **Regular limit orders** entered during the session execute whenever they're matched in the continuous book; they may or may not execute at the close.

MOC and LOC are specifically auction-based, with all execution happening in that final compressed window.

## Cancellation and timing rules

Most brokers require that MOC and LOC orders be entered by a cutoff time—typically 3:45 PM ET or later, but not after the official 3:50 PM cutoff. Once in the queue, you usually cannot cancel an MOC; LOCs are more flexible.

Different exchanges and brokers have slightly different rules. Some allow conditional orders (e.g., "MOC only if this other stock doesn't hit a price target"), but the basic mechanics are the same.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — how price limits work in regular continuous trading
- [Market Order](/market-order/) — execution without a price condition
- [Market Maker](/market-maker-trading/) — who supplies liquidity at the close
- [Alternative Trading System](/alternative-trading-system/) — off-exchange venues and mechanisms
- [Price Discovery](/price-discovery/) — how market prices emerge from order flow
- [Execution Risk](/execution-risk/) — what can go wrong when orders fail to fill

### Wider context

- [Stock Exchange](/stock-exchange/) — how auction mechanics differ by venue
- [Liquidity Risk](/liquidity-risk/) — why imbalances create price gaps
- [Market Cycle](/market-cycle/) — intra-day patterns and end-of-day dynamics
- Settlement and Clearing — how closing prices drive settlement processes

</div>

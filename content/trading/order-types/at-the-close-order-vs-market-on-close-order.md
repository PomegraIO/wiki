---
title: "At-the-Close Order vs Market-on-Close Order"
description: "How at-the-close orders and market-on-close orders differ: broker instructions vs. exchange-native routes, execution timing, and cancellation rules."
keywords:
  - at the close order vs market on close order
  - market on close
  - at the close order
  - order execution
  - closing orders
  - order routing
---

*An at-the-close (ATC) order is a broker instruction to execute as close to the market close as possible; a Market-on-Close (MOC) order is an exchange-native order type that routes directly to the exchange's close auction. Though both aim for closing-price execution, MOC orders are faster, more reliable, and subject to firm cutoff times, while ATC orders offer more flexibility but less priority.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">At-the-Close Order vs Market-on-Close Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">MOC is exchange-native and guaranteed closing-price execution; ATC is broker-managed and best-effort.</div>

|   |   |
|---|---|
| **Order origin** | ATC: broker instruction; MOC: exchange-native order type |
| **Execution venue** | ATC: broker's discretion; MOC: designated exchange closing auction |
| **Execution speed** | MOC: immediate at official close; ATC: typically within last minute |
| **Cancellation deadline** | MOC: 3:50 PM ET (US); ATC: often 3:55–3:58 PM ET |
| **Priority in auction** | MOC: ranked by size and arrival; ATC: no guaranteed priority |
| **Execution certainty** | MOC: near-certain (if market open); ATC: best-effort only |
| **Typical use case** | MOC: index rebalancing, fund flows; ATC: manual trader discretion |
| **Cost/fees** | MOC: standard commission; ATC: often no additional fee, but execution quality varies |

</aside>

## Why close-of-day orders matter

The stock market close—4:00 PM ET for US equities—is the reference point for price discovery, portfolio valuation, and regulatory compliance. A pension fund rebalancing its holdings wants to execute at the official closing price to match its valuation baseline. An active trader who decides to exit a position late in the day wants to capture the day's full price action before closing.

For these reasons, traders use orders specifically designed for execution at or near the close. The two most common mechanisms are at-the-close (ATC) orders and Market-on-Close (MOC) orders. They sound similar—both aim to execute near 4:00 PM—but they operate through different channels and have different guarantees.

## Market-on-Close (MOC) orders: exchange-native

A **Market-on-Close (MOC) order** is a formal order type defined by the exchange itself—not a broker instruction, but a native routing mechanism. In the US equity market, the New York Stock Exchange (NYSE) and NASDAQ each operate a closing auction where all MOC orders are pooled and executed at a single price—the official closing price.

Here's how it works:

**Submission**: A trader submits an MOC order to their broker. The broker routes it to the exchange (NYSE, NASDAQ, or another venue) where the stock trades. The order sits in the exchange's MOC queue.

**Accumulation period**: All MOC orders accumulate during the trading day. No execution happens yet. The exchange does not match them against incoming buy and sell interest. They wait passively.

**Imbalance disclosure**: At 3:45 PM ET, the exchange publishes the **order imbalance**—the net quantity of buy MOC orders versus sell MOC orders. This allows traders to adjust their strategy if they see a lopsided imbalance.

**Cancellation deadline**: MOC orders can be cancelled until 3:50 PM ET on NYSE and NASDAQ. After 3:50 PM, the order is locked in and cannot be withdrawn.

**Closing auction**: At the official market close (4:00 PM ET), the exchange runs the closing auction. All MOC orders are filled at a single price—the closing price. If there are more buy MOC orders than sell MOC orders, the price adjusts upward to clear all orders. The goal is to find a price where supply meets demand.

**Execution and confirmation**: The order is filled at the official closing price, and confirmation is sent to the trader's broker. This typically occurs within seconds of the close.

## At-the-Close (ATC) orders: broker instruction

An **at-the-close (ATC) order** is not an exchange order type. It is a broker instruction—a way for a trader to tell their broker, "Execute this order as close to the close as you can." The broker holds the order and decides how and when to execute it in the final minutes of the trading day.

**Submission**: A trader enters an ATC order with their broker, specifying a stock, size, and direction (buy or sell). The order does not route to the exchange; it stays with the broker.

**Broker discretion**: The broker's trading desk manages the execution. In the final minutes (often the last 5–10 minutes of trading), the broker begins to execute the order. It might:
- Route it to the exchange as a regular limit order, which could be filled by incoming market orders.
- Break it into smaller pieces and execute them progressively to minimize market impact.
- Route it to an [alternative trading system](/alternative-trading-system/) (ATS) that also has closing activity.
- Execute it partially at-the-close (via an exchange MOC route) and partially in regular late trading.

**Execution window**: ATC execution typically happens in the last 1–5 minutes of trading, not necessarily at the official closing price. The exact timing depends on the broker's algorithm and market conditions.

**Cancellation**: Because ATC is a broker order (not exchange-native), it can typically be cancelled until 3:55 PM or 3:58 PM ET, later than the 3:50 PM MOC cutoff. The exact deadline varies by broker.

**Execution certainty**: Execution is **best-effort**. If the market is thin near the close, the broker may not fill the entire order at the closing price. Part of the order might execute, or the order might be left open and filled early the next trading day.

## Key differences in practice

| Aspect | MOC | ATC |
|--------|-----|-----|
| **Routing** | Direct to exchange closing auction | Through broker's trading desk |
| **Execution price** | Official closing price (guaranteed if filled) | Often near closing price, but not guaranteed |
| **Cancellation deadline** | 3:50 PM ET (firm) | 3:55–3:58 PM ET (broker-dependent) |
| **Execution speed** | Instantaneous at close | Within last few minutes |
| **Certainty of fill** | Very high if liquidity exists | Moderate; depends on broker execution |
| **Best for** | Index funds, large passive rebalancing | Active traders, discretionary positions |
| **Regulatory transparency** | Published imbalance data available | Execution details vary by broker |

## When to use MOC

MOC orders are the choice for:

- **Index rebalancing**: Pension funds and ETFs rebalancing into or out of holdings on a specific date use MOC to guarantee execution at the published closing price for consistent NAV reporting.
- **Systematic trading**: Traders following algorithmic or rules-based strategies that must execute at close use MOC for the certainty of timing and price.
- **Large passive orders**: Institutional investors moving significant capital out of or into a stock prefer MOC's guaranteed execution over trying to execute gradually during the day.
- **Regulatory compliance**: Portfolio managers adhering to specific valuation baselines or index-following mandates use MOC to ensure prices match published close prices.

## When to use ATC

ATC orders suit:

- **Discretionary trading**: Active traders who wait until late in the day to decide whether to exit a position benefit from ATC's flexibility and later cancellation window.
- **Smaller orders**: Traders executing smaller quantities that can be absorbed by regular market activity near the close may prefer the discretion ATC provides.
- **Tactical execution**: Traders who want flexibility to adjust size or direction based on intraday price action use ATC over MOC's locked-in approach.
- **Brokers without MOC connectivity**: Some brokers, particularly smaller firms or non-US venues, may not support direct MOC routing, so ATC is the fallback.

## Execution outcomes and costs

In normal market conditions, both MOC and ATC typically execute at or within 1–2 cents of the closing price. The difference becomes visible in stressed or imbalanced markets.

During a market crash or heavy selling near the close, MOC orders are all executed at a single price—the clearing price that balances supply and demand. This can result in a large gap from the last printed trade price, if the imbalance is large. ATC orders have more flexibility; the broker can attempt to execute gradually or route to multiple venues, potentially achieving a better average price.

Conversely, if the close is orderly and liquid, MOC orders often execute at the published closing price, which is often the "fairest" price of the day. ATC orders may execute slightly before the official close or slightly after, depending on market depth.

**Fees and costs** are typically the same for both: standard commission rates apply. Some brokers charge a small premium for ATC execution (a few cents per share), but most do not.

## Technical considerations

**Partial fills**: MOC orders are all-or-nothing at the auction price. If there is insufficient liquidity to fill the entire MOC order at the closing price, the unfilled portion is cancelled. ATC orders can be partially filled at different prices if the broker breaks them into pieces.

**Liquidity sources**: MOC orders tap into the exchange's closing auction, which includes all exchange participants. ATC orders are executed by the broker's trading desk, which may use internal flow, market makers, or ATS venues. The liquidity sources are different.

**Dark pool accessibility**: MOC orders cannot be routed to dark pools or off-exchange venues; they are exclusively for the exchange closing auction. ATC orders can be routed to alternative trading systems or dark pools if the broker chooses.

## Order type confusion and best practices

The term "at-the-close" is sometimes used loosely to describe any order meant to execute near the close. Traders should verify with their broker:

1. **Is it a true MOC order?** If the broker is routing the order to the exchange's native closing auction, it is a true MOC.
2. **What is the cancellation deadline?** Confirm whether the order can be cancelled until 3:50 PM (MOC) or later (ATC).
3. **What is the execution guarantee?** Does the broker guarantee execution at the closing price, or is it best-effort?
4. **Where is it routed?** Will it be routed to the primary exchange where the stock's largest volume is, or to an alternative venue?

For automated systems and large institutional orders, MOC is the standard and safest choice. For discretionary traders, ATC offers flexibility—but requires understanding the broker's exact algorithm and execution guarantees.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — baseline order type executed immediately at available price
- [Limit Order](/limit-order/) — alternative order type with a price constraint
- [Order Types](/order-types/) — broader taxonomy of order execution mechanisms
- [Stock Market](/stock-market/) — venue where closing orders execute
- [Bid-Ask Spread](/bid-ask-spread/) — dynamic that affects closing order pricing
- [Price Discovery](/price-discovery/) — how closing orders contribute to final market price

### Wider context

- [Stock Exchange](/stock-exchange/) — institution operating the closing auction
- [Execution Risk](/execution-risk/) — risk that closing orders face in volatile markets
- [Volatility](/volatility-smile/) — market condition that affects close-of-day order fill quality
- [Market Maker Trading](/market-maker-trading/) — counterparty providing liquidity to closing orders
- [New York Stock Exchange](/new-york-stock-exchange/) — primary venue for US equity closing auctions
- [NASDAQ](/nasdaq/) — alternative venue with its own MOC closing auction

</div>

---
title: "Slippage in Trading"
description: "What slippage is in trading, why positive and negative slippage occur, and how to reduce it when executing large orders or trading fast markets."
keywords:
  - slippage
  - slippage in trading
  - what is slippage trading
  - negative slippage
  - execution quality
image: "/svg/trading.svg"
---

*In trading, **slippage** is the difference between the price you expected to pay or receive and the actual fill price. Negative slippage is a worse fill (higher for a buy, lower for a sell); positive slippage is a better fill. Slippage occurs when prices move between order submission and execution, or when you must cross a wide [bid-ask spread](/bid-ask-spread-explained/) to fill immediately.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Slippage — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Slippage is the gap between your intended price and your actual fill price—a hidden cost or gain on every trade.</div>

|   |   |
|---|---|
| **Negative slippage** | Filling worse than expected (higher price for a buy, lower for a sell) |
| **Positive slippage** | Filling better than expected; also called [price improvement](/price-improvement-order-execution/) |
| **Main causes** | Fast markets, large orders, wide [bid-ask spreads](/bid-ask-spread-explained/) |
| **Measured as** | Per-share cents, basis points, or percentage of order |
| **Typical range** | 0.01 to 1.00 per share, depending on liquidity and volatility |
| **How to reduce** | Limit orders, smaller order size, trading liquid securities, off-peak hours |

</aside>

## What slippage is and why it matters

Imagine you decide to buy a stock trading at \$50.00. You open your trading platform and submit a [market order](/market-order/) to buy 1,000 shares. By the time your order reaches the exchange—a process that takes milliseconds but is not instantaneous—the best offer has moved to \$50.10. Your order fills at \$50.10 instead of \$50.00. You have experienced \$0.10 per share in negative slippage, or \$100 total on this trade.

Slippage is invisible in your account—your fill price is simply reported as \$50.10, not as "\$50.00 expected, \$50.10 actual." But it is real money. The larger your order or the faster the market moves, the more slippage accumulates.

For a day trader or [algorithmic system](/algorithmic-trading/) executing dozens of trades per day, slippage can be a significant drag on returns. For a long-term investor rebalancing a portfolio once a quarter, a few cents of slippage per trade is usually immaterial.

## Causes of slippage

**Market movement between order submission and execution.** The most common cause. The price you see on your screen is the last traded price or the current best bid-ask. But by the time your order travels from your computer to the exchange, prices may have moved. If the market ticks up while your buy order is in transit, you fill higher. If it ticks down, you fill lower (relative to your expectation).

**Wide bid-ask spreads.** When you submit a [market order](/market-order/), you accept whatever the best current offer is. In a tightly traded stock with a \$0.01 spread, you might expect \$50.00. In a less liquid stock with a \$0.50 spread, you might expect \$50.00 but fill at \$50.50. That \$0.50 is slippage, though some of it is also the fundamental [bid-ask spread](/bid-ask-spread-explained/).

**Large order size.** When you submit a large order relative to available liquidity, you exhaust the [best bid-ask](/bid-ask-spread-explained/), and your order walks through multiple price levels. You might buy 10,000 shares, but only the first 2,000 fill at \$50.00, the next 3,000 at \$50.05, the next 3,000 at \$50.10, and the final 2,000 at \$50.15. Your average fill is \$50.075, not \$50.00. That gap is order slippage.

**Market volatility.** In fast-moving markets, quotes are changing rapidly. A market maker may pull their quote before you can execute against it. The next best quote is further away, and you cross a wider spread to fill.

**News or data releases.** When economic data or company news hits, market participants re-evaluate prices instantly. If your order enters the market just before a big announcement, you may hit the old price, but the fill reflects the post-announcement market.

## Positive versus negative slippage

Slippage cuts both ways. If you expect to pay \$50.00 but the market rallies and you fill at \$49.90, you have positive slippage—a better fill than expected. This is also called [price improvement](/price-improvement-order-execution/).

Over many trades, positive and negative slippage do not cancel out evenly. Statistically, traders who use [market orders](/market-order/) experience slightly negative slippage on average because:

1. You are always selling at the bid and buying at the ask (both unfavorable by definition).
2. Large orders trigger the worst slippage (walking the book), while small orders sometimes benefit from price ticks.
3. Algorithms and market makers detect large orders and pull liquidity, forcing you to cross wider spreads.

Institutional traders and [market makers](/market-maker-trading/) actively manage slippage by breaking large orders into smaller pieces, using algorithms that execute over time, and negotiating block prices with dealers.

## Slippage in fast markets

During high-volatility episodes—such as earnings announcements, Fed decisions, or flash crashes—slippage can exceed dollars per share. Consider a stock that normally has a \$0.01 spread. During a volatility spike, the spread blows to \$1.00 or wider. If you submit a 10,000-share market order to buy during that moment, you might fill 1,000 shares at the offer (\$50.00), then 2,000 at \$51.00, then 2,000 at \$52.00, then 2,000 at \$53.00, then the remaining 3,000 at \$54.00—an average fill of \$52.40. That is \$2.40 of average slippage, or \$24,000 on the full order.

Large institutional traders know this and either avoid trading during volatile moments or use special algorithms and block desk negotiations to minimize market impact.

## How to reduce slippage

**Use limit orders.** A [limit order](/limit-order/) specifies a maximum price you will pay (or minimum price you will accept). You cannot get worse slippage than your limit. The tradeoff is that you may not fill if the market moves away from your price. But limit orders are the most powerful tool against slippage.

**Trade smaller quantities.** The more shares you try to execute at once, the more you walk the order book and trigger slippage. Breaking a large order into smaller tranches, executing them over hours or days, reduces the per-trade slippage (though total cost depends on market movement).

**Trade the most liquid securities.** Stocks in the [S&P 500](/sp-500-index/) index, especially mega-caps, have tight [bid-ask spreads](/bid-ask-spread-explained/) and deep liquidity. Slippage is minimal. Micro-cap stocks, bonds, and options typically have wider spreads and more slippage.

**Avoid trading around major announcements.** Economic data releases, [Federal Reserve](/federal-reserve/) meetings, or earnings announcements trigger volatility and slippage. Wait until the market settles if your trade is not time-sensitive.

**Trade during peak hours.** Mid-session (9:45 AM to 3:00 PM ET) usually has the tightest spreads and deepest liquidity. Avoid the open (9:30–9:45 AM) and close (3:45–4:00 PM), when volatility and spreads often widen.

**Use execution algorithms.** Institutional traders use algorithms—such as Volume Weighted Average Price (VWAP) or Time Weighted Average Price (TWAP)—that execute orders in small slices over time, reducing market impact and slippage. Some brokers offer these to retail clients.

**Choose a broker with good execution quality.** Compare the [price improvement](/price-improvement-order-execution/) statistics of different brokers. Brokers that internalize orders or route to venues with tight spreads tend to deliver lower slippage.

## Slippage and strategy

For day traders and algorithmic systems, slippage is a first-order cost. A high-frequency trader might structure their strategies around slippage expectations, accepting that they will pay a small slippage tax on entry and exit. The expectation is that their edge—identifying temporarily mispriced securities—is large enough to overcome slippage costs.

For long-term investors, slippage is secondary. Rebalancing quarterly and using limit orders, a buy-and-hold investor might experience only a few pennies of slippage per trade, which is negligible over decades.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread Explained](/bid-ask-spread-explained/) — the structural source of much slippage
- [Price Improvement in Order Execution](/price-improvement-order-execution/) — positive slippage and how to achieve it
- [Limit Order](/limit-order/) — the best defense against negative slippage
- [Market Order](/market-order/) — instant fill but highest slippage risk
- [Fill-or-Kill Order](/fill-or-kill-order/) — all-or-nothing execution that avoids partial-fill slippage

### Wider context

- [Market Maker Trading](/market-maker-trading/) — who benefits from your slippage
- [Algorithmic Trading](/algorithmic-trading/) — systematic ways to reduce slippage through VWAP, TWAP, and other algorithms
- [Stock Exchange](/stock-exchange/) — where price discovery and execution happen
- [Broker](/broker/) — responsible for routing and execution quality
- [Volatility Smile](/volatility-smile/) — how [bid-ask spreads](/bid-ask-spread-explained/) widen in fast markets

</div>

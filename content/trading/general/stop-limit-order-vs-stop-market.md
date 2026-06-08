---
title: "Stop-Limit Order vs Stop-Market Order"
description: "Learn the difference between stop-limit and stop-market orders: how they trigger, what guarantees they offer, and when to use each one."
keywords:
  - stop limit vs stop market order difference
  - stop limit order explained
  - stop market order execution
  - stop order types
image: /svg/trading.svg
---

*A **stop-limit order** triggers at a specified price, then executes only within a limited price range—guaranteeing price but risking missed execution. A **stop-market order** triggers at a specified price, then sells or buys at the market—guaranteeing execution but not price. The choice hinges on whether you want certainty of selling at a reasonable price or certainty of getting out of the trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop Orders — execution tradeoffs</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Stop orders convert on price movement; what they guarantee depends on which variant you choose.</div>

|   |   |
|---|---|
| **Stop-Limit** | Converts to limit order; price guaranteed, execution not |
| **Stop-Market** | Converts to market order; execution guaranteed, price not |
| **Trigger condition** | Both activate when underlying hits stop price |
| **Best for downside** | Limit order when you won't accept below a floor price |
| **Best for exits** | Market order when you must exit regardless of price |
| **Risk in gaps** | Limit order may not fill; market order may overshoot |
| **Common role** | Limit used to defend a profit; market used for emergency stop |

</aside>

## How stop orders work

Both order types share a common mechanism: you set a **stop price** (the trigger), and when the market reaches that price, the order activates. The difference is what happens after activation.

With a stop-market order, once the stock hits your stop price, it immediately becomes a market order. It will execute at the next available price—which might be significantly away from your stop price if there's a gap in the market or the stock is moving fast. You get out of the trade almost certainly, but possibly at a much worse price than you intended.

With a stop-limit order, the stop price acts as a trigger, but a second price range—the limit price—constrains execution. Once triggered, it becomes a limit order that will only fill at your limit price or better. You stay in control of the worst price you'll accept, but the order may never fill if the price gaps past your limit.

## The execution guarantee versus price guarantee tradeoff

The core tension is this: **which is worse for you—not selling at all, or selling at a bad price?**

A stop-market order prioritizes execution. You're saying: "If this stock drops to $45, I want out—whatever the price is." This protects you from further free-fall. If bad news hits overnight and the stock opens at $38, a stop-market order placed at $45 will execute at or near the open. You've exited, even though the price is painful.

A stop-limit order prioritizes price. You're saying: "If the stock drops to $45, I want to sell—but only if I can get $44 or better." If the stock opens at $38, your stop-limit order with a $44 limit will not fill, and you're still holding. If the stock climbs back to $50 the next day, you're relieved. If it drops to $30, you're ruined, but at least you didn't sell the bottom.

## When to use stop-limit for downside protection

A stop-limit order makes sense when you're protecting a gain or defending against a moderate loss, and the price you're willing to accept is realistic given normal market spreads.

Example: You buy a stock at $50. It runs to $72. The market is stable, bid-ask spreads are tight (pennies), and you don't want to give back more than $5 of your gain. You set a stop-limit order: if the stock drops to $67, sell at $66 or better. In normal conditions, that order will fill quickly because $66 is close to fair value if the stock is trading at or near $67. The risk is low.

By contrast, if you set a stop-limit order during a slow, illiquid period—or if your limit is too aggressive (e.g., stop at $67, limit at $70)—the order can sit unfilled while the stock craters.

Stop-limit is most appropriate when:
- You're defending a profit in a liquid, stable-volatility security.
- The gap between stop price and limit price is 1–3% at most (in normal markets).
- You can afford to be wrong (i.e., staying in the position a little longer is acceptable).

## When to use stop-market for emergency exits

A stop-market order is the choice when you absolutely need to exit, regardless of price—because the risk of being trapped is worse than the risk of slippage.

Example: You bought a biotech stock ahead of FDA approval. News emerges that the approval was denied. The stock plummets on the open. You set a stop-market order at $30 (the stock was $60 yesterday). When the market opens, the order executes, perhaps at $28. You've taken a big loss, but you're out. If you'd used a stop-limit order at $30, you might still be holding at $18 by midday.

Stop-market is essential when:
- You're in a highly volatile or thinly traded security where gaps are common.
- You need to protect yourself from [tail risk](/tail-risk/) (extreme moves).
- Overnight news or geopolitical shocks could crater the stock before you can react.
- You're managing a position that must be exited because the original thesis has broken.

## Practical scenarios and pitfalls

**Scenario 1: Morning gap**
You hold a stock at $80. Earnings are tomorrow. You set a stop-limit: stop $70, limit $68. At the open, the company announces terrible results. The stock opens at $45. Your stop-limit order doesn't trigger (it's already below $70), so your conditional doesn't apply—you still own the stock. You scramble to sell at market. Lesson: In volatile situations, a stop-market order at or above the current price may execute faster when news hits.

**Scenario 2: Slow drift with limit too tight**
A stock declines steadily from $100 to $60, with your stop-limit at $70 (stop) and $68 (limit). It hits $70, your limit order is posted at $68, but the stock is falling fast. You fill maybe 20% of your shares at $68, the rest at $65, $60, etc. You've had partial execution and slippage. Lesson: Don't set your limit price too far away from your stop price, or you risk partial fills at worse prices.

**Scenario 3: Overnight gap at market open**
A stock you own at $50 is hit with a lawsuit. You have a stop-market order at $45. The stock opens at $32. Your order fills at $32 or close to it. You lost $18 per share from your entry, not the $5 you "planned" to lose. Lesson: Stop orders are not price guarantees; they only trigger execution. They don't protect you from the market moving past your stop price.

## Order types and variations

Most brokers offer both stop-limit and stop-market orders through their standard [order entry](/market-order/) interface. Some allow trailing stops, which automatically adjust the stop price as the stock rises (protecting a gain dynamically). Trailing stops are often used with market execution, since the goal is to lock in gains without leaving money on the table.

Very large institutional traders sometimes use algorithmic or iceberg orders to minimize slippage, but for typical retail and professional traders, the choice between stop-limit and stop-market is the primary lever.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — buy or sell at the best available price immediately
- [Limit Order](/limit-order/) — execute only at your specified price or better
- Stop Order Basics — how stop prices trigger orders
- Trailing Stop — automatically adjust your stop price as the stock rises
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between buy and sell prices that can cause slippage
- [Execution Risk](/execution-risk/) — the risk of unfavorable fills in volatile markets

### Wider context

- [Order Types](/order-types/) — comprehensive overview of order entry methods
- Risk Management — position sizing and stop placement strategies
- Volatility — how price swings affect stop-order fills
- [Market Hours and After-Hours Trading](/after-hours-trading/) — when gaps and fast executions occur
- [Slippage](/slippage/) — difference between expected and actual execution price

</div>

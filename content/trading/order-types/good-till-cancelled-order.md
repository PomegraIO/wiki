---
title: "Good Till Cancelled Order"
description: "A standing limit order that persists until the trader explicitly cancels it, allowing resting buy or sell bids at chosen price across multiple trading sessions."
keywords:
  - good till cancelled
  - GTC order
  - limit order
  - standing order
  - order management
image: "/svg/trading.svg"
---

*A **good till cancelled (GTC) order**, also called a **standing order**, is a [limit order](/limit-order/) placed by a trader to buy or sell a security at a specified price that remains active across multiple trading sessions until the trader cancels it. Unlike a day order (which expires at market close), a GTC order can sit on the order book for weeks or months, executing whenever the market price touches the specified level.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Good Till Cancelled Order — key facts</div>

<img src="/svg/trading.svg" alt="An editorial mark representing trading orders and execution." />

<div class="wiki-infobox-caption">A patient trader's tool: a limit order that waits indefinitely for your price.</div>

|   |   |
|---|---|
| **Definition** | Limit order persisting until manually cancelled |
| **Duration** | Continues across trading days (sometimes months) until cancelled or filled |
| **Execution** | Only fills if market price meets or exceeds the limit |
| **Alternative names** | Standing order, open order, persistent order |
| **Primary use** | Scaling into positions over time without active monitoring |
| **Counterparty risk** | Issuing broker could close account or face insolvency during the order's life |
| **Regulatory variation** | Some jurisdictions allow GTC; others require renewal within 30–90 days |

</aside>

## Mechanics: setting and forgetting (carefully)

When you place a GTC buy order, you specify a price you are willing to pay. If a seller is willing to transact at that price, the order fills. If nobody is willing, the order sits unfilled on the order book, waiting. You do not have to monitor it every day. You do not have to reset it after the market closes. It simply persists.

Similarly, a GTC sell order waits at a price you name, ready to execute if a buyer arrives at that level.

The advantage is obvious: you set your price, go about your business, and the order executes whenever conditions align. For a trader who wants to buy more of a stock but only at a certain valuation, or sell after a price target is hit, a GTC order is far more convenient than placing fresh orders each day. It is also cheaper in terms of time and attention.

## Comparison to day orders and other timeframes

A **day order** expires at the end of the trading session if unfilled. After the market closes, the order vanishes and you must resubmit it the next day if you still want it. Day orders are the default for most retail brokers and are simple to manage because they do not persist.

A **GTC order** persists until cancelled or filled, potentially for months.

Some brokers also offer intermediate timeframes: a **week** order (good through Friday), a **month** order, or a custom duration (e.g., good for 30 days). These are less common than day and GTC but offer middle ground for traders who want a longer window without indefinite waiting.

The choice depends on your strategy. A day trader using intraday momentum will use day orders exclusively. A value investor who is patient about entry price may use GTC to avoid missing a fleeting opportunity to buy during a drawdown.

## The patience play and scaling in

GTC orders are popular among traders who want to **scale into** or **scale out of** a position over time. Rather than buying all shares at once (risking a bad fill if you buy right before the price drops), you place multiple GTC buy orders at different price levels. If the stock declines to USD 45, your first order fills. If it declines further to USD 43, your second order fills. If it rallies instead, none of your orders fill and you buy nothing.

This approach reduces the risk of a bad entry at a single price, though it also means you may miss the bottom if the stock recovers before hitting all your target prices.

Similarly, a trader exiting a position might place GTC sell orders at multiple profit targets, letting the market do the work of trimming the position as the stock rises.

## Hidden risks and operational gotchas

For all their convenience, GTC orders carry overlooked risks.

**Broker insolvency.** Your GTC order lives on the broker's system. If the broker is acquired, goes bankrupt, or transfers your account, what happens to long-standing orders? Most brokers have systems to migrate them, but it is not automatic, and edge cases exist. You should periodically review your GTC orders to ensure they are still active on your current broker.

**Account closure.** If you close a margin account or transfer to a new broker, GTC orders may be cancelled without notice. This is rarely a problem if you monitor your account, but it is easy to forget an old GTC order and assume it is still waiting to execute.

**Price gap risk.** A GTC order is a limit order: it will not fill at a worse price than your limit. But if the stock gaps past your order—say, it jumps from USD 46 to USD 40 in the morning due to bad news—your buy order at USD 43 will not fill during the gap. You miss the opportunity and remain out of the position. Some traders use stop orders or [market orders](/market-order/) to catch moves, but those sacrifice price discipline.

**Corporate actions.** If a company splits shares, pays a large dividend, or undergoes a merger, your GTC order may need adjustment. A buy order to purchase 100 shares at USD 50 is not the same if the company executes a 2-for-1 split; the price should be halved. Most brokers handle this automatically, but always verify.

**Regulatory sunset.** Some jurisdictions require brokers to expire GTC orders periodically—often every 30, 60, or 90 days—forcing you to renew them. This is a safeguard against stale, forgotten orders, but it also means you cannot truly "set and forget" indefinitely. Check your broker's policy.

## GTC orders and bid-ask spreads

A GTC limit order is only as good as the [bid-ask spread](/bid-ask-spread/) at that price. If you place a GTC buy order at USD 50 and the stock is trading at USD 51 (with an ask of USD 51.05), your order will not fill—you are not meeting the sellers. As the stock falls, if it reaches USD 50, the order fills.

For illiquid stocks with wide spreads, a GTC buy order at a nice round number (like USD 50) may sit unfilled for months even though the stock came close to that level. The [market maker](/market-maker-trading/) bid might have been USD 49.95, never quite touching your USD 50 limit.

This is why limit orders are sometimes paired with a willingness to adjust: if the stock languishes near your price but does not cross it, you might lower your limit slightly to improve the odds of a fill, or you might cancel and wait for a better opportunity.

## Institutional and algorithmic use

Institutional traders and [algorithmic trading](/algorithmic-trading/) systems use GTC and other persistent order types extensively. An algorithm might slice a large order into smaller GTC limit orders across multiple price levels, executing a gradual accumulation or distribution over days without revealing the full intent to the market.

For retail traders, GTC orders are a way to participate in that same "patient" approach without sophisticated algorithms—you set the rules and the market executes them.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — order type that specifies maximum buy or minimum sell price; GTC is a persistence variant
- [Market order](/market-order/) — immediate execution at current market price; no price control
- [Stop order](glossary-link-not-included) — order triggered when price crosses a threshold, complementary to GTC for risk management
- [Bid-ask spread](/bid-ask-spread/) — difference between buy and sell prices; affects GTC fill likelihood
- [Order book](glossary-link-not-included) — central record of all resting limit orders including GTC orders

### Wider context

- [Market maker](/market-maker-trading/) — provides liquidity that GTC orders rely on to execute
- [Price discovery](/price-discovery/) — process in which GTC orders participate as standing interest
- [Algorithmic trading](/algorithmic-trading/) — systematic approach to order execution that often uses GTC-like logic
- [Liquidity risk](/liquidity-risk/) — risk that GTC orders cannot fill if market volume dries up

</div>

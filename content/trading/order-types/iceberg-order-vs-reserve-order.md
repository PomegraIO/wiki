---
title: "Iceberg Order vs Reserve Order"
description: "Both hide order size but work differently. Iceberg reveals visible tranche in stages; reserve order keeps size hidden until a portion fills. Compare visibility and mechanics."
keywords:
  - iceberg order
  - reserve order
  - hidden order
  - order size
  - trading tactics
---

*An **iceberg order** shows only a small "tip" of your total order on the book, then automatically refreshes with a new visible tranche as each fills; a **reserve order** hides its full size but releases it only after a partial fill is triggered, or according to a pre-set reveal schedule. Both obscure size to avoid market impact, but their visibility and refresh mechanics differ fundamentally.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Iceberg vs Reserve — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two strategies for hiding large orders in plain sight.</div>

|   |   |
|---|---|
| **Iceberg order** | Shows visible tranche; replenishes automatically as fills occur |
| **Reserve order** | Hides total size; reveals on trigger (fill or time-based) |
| **Visibility** | Iceberg: tip visible, rest hidden; reserve: all hidden until trigger |
| **Refresh** | Iceberg: continuous auto-refresh; reserve: conditional reveal |
| **Typical use** | Iceberg: large passive orders; reserve: block trades, protection |
| **Broker support** | Both widely supported on major exchanges |

</aside>

## Iceberg order: the tip and the berg

An **iceberg order** is a single large order subdivided into visible and hidden portions. You specify a total quantity (say, 50,000 shares) and a "display size" or "visible quantity" (e.g., 5,000 shares). The exchange shows the 5,000-share tip on the order book; the remaining 45,000 shares are hidden.

As the visible 5,000 shares fill, the system automatically refreshes and shows another 5,000 shares. When those fill, another 5,000 appear. This continues until the entire 50,000-share order is filled or cancelled. To observers watching the order book, they see repeated 5,000-share orders coming and going—but they don't realize a single giant iceberg order is behind them.

**Why the metaphor works:** The visible portion (the tip) is all anyone sees on the surface; the bulk (the berg) lies beneath, unknown.

**Mechanics:** The visible tranche sits at your specified limit price and price level in the queue. If you place a buy order, the first 5,000 shares queue at your price alongside other buy orders at that same price; the next 5,000 sits hidden, waiting. As the first tranche executes (partially or fully), the hidden tranche automatically moves forward into the visible queue, refreshing your position.

This refresh can either preserve or lose your original queue position, depending on the exchange's rules. Some exchanges reset your queue priority each time a new visible tranche appears; others maintain your original timestamp. Confirm your broker's behavior.

## Reserve order: the hidden block

A **reserve order** takes a different approach: your entire order quantity is hidden from the order book. Unlike an iceberg, nothing is visible initially. Instead, you specify a "display" or "working" quantity that will be revealed only when a condition is met—typically, when a partial fill occurs.

For example, you place a reserve buy for 50,000 shares at $100, with a display quantity of 5,000. The order book shows no sign of your order at all. If someone sells 3,000 shares at $100, those fill against your hidden reserve order. Immediately after, the system displays 5,000 shares at your price (to refresh the working inventory). As those fill, another 5,000 display, and so on.

**The key difference:** The reserve order reveals its presence *only after a fill occurs*. An iceberg shows a tip from the start; a reserve hides entirely and then surfaces.

Some brokers and platforms also offer time-based release schedules for reserve orders: "Reveal 2,000 shares every 30 seconds" or "Show 5,000 shares if the stock moves 2 cents." These conditional reveals let you slowly disclose size in a controlled manner without triggering a sudden wave of selling interest.

## Visibility and market impact

**Iceberg orders** are partially visible from the moment they're placed. The market sees the tip and infers there may be more beneath. Sophisticated traders and algorithms recognize the pattern of recurring visible tranches and sometimes deduce the full hidden size by watching the refresh pattern. This makes icebergs effective for moderately large orders but imperfect for truly discrete execution.

**Reserve orders** offer greater initial discretion: the order book shows nothing. This is valuable if you want to place a large block without alerting the market before any shares have moved. Once a fill occurs and the reveal happens, the pattern becomes visible—but the damage (in terms of telegraphing intent) may already be done: you've already established a foothold on the order book.

## When to use each type

**Iceberg orders** suit traders placing large passive resting orders that will live for hours or days. The automatic refresh keeps you in the hunt without requiring manual re-entry. Institutional traders often use icebergs to accumulate or distribute large positions across a session while keeping the visible quantity small (and thus less threatening to the spread and the quoted price).

A buy-side trader wanting to accumulate 100,000 shares of a mid-cap stock might use an iceberg with a 10,000-share tip, allowing the order to fill gradually without signaling "I'm a big buyer" to every market participant.

**Reserve orders** are popular for:
- **Block trades** where you want to initiate a large trade without pre-announcing it
- **Situations where the first fill is the hardest:** place a reserve order, get the first tranche to execute, then let the reserve reveal itself as working inventory
- **Discrete entry or exit:** if you're a fund manager entering a position, a reserve order lets you probe the market without broadcasting your intent
- **Protection against front-running:** by hiding the full size, you reduce the chance an algorithm detects and front-runs your order

## Queue position and fairness

Iceberg orders trigger debate around fairness. When the system refreshes a new visible tranche, should your order rejoin the back of the queue at that price, or retain its original timestamp position?

- **FIFO (first-in-first-out) queues with strict timestamp:** Your tranche refreshes and goes to the back. This is "fairest" but makes icebergs less efficient; you might never fully execute if the price is constantly moving.
- **Refresh at original position:** Some systems refresh you at your original queue slot. This favors the iceberg holder and may be seen as unfair to other resting orders.

Exchange rules vary. NYSE, NASDAQ, and most major venues have specific rules governing refresh treatment. Always check your platform's documentation.

## Iceberg order mechanics: display options

Most brokers let you specify the visible tranche size and sometimes the refresh interval:
- **Display size:** how many shares show each time
- **Iceberg quantity:** total order size (hidden + visible)
- **Order type:** limit (most common) or pegged orders can also be icebergs

Some platforms allow you to set a "minimum" visible size, ensuring that even as the order shrinks near completion, a certain minimum stays visible. This prevents the last 100 shares from being shown as a tiny odd-lot, which might trigger algorithms designed to spot small orders.

## Partial fills and remainder behavior

Both iceberg and reserve orders handle partial fills the same way: the unfilled remainder persists. An iceberg that partially fills will continue to refresh visible tranches. A reserve order that partially fills will continue to reveal hidden size according to its release schedule.

If the order is not fully filled by market close and is set as a day order, the entire unfilled remainder is cancelled. If it's a [good-till-cancelled order](/day-order-vs-good-till-cancelled/), it persists into the next session, continuing its iceberg or reserve logic.

## Execution price and transparency

Neither iceberg nor reserve orders guarantee a single execution price. A 50,000-share iceberg might fill in tranches at $100.00, $100.01, and $100.02 as the price moves during the session. The average price across all fills may differ from your original limit. This is expected and built into the strategy; you're accepting execution uncertainty to minimize market impact.

For regulatory reporting and tax purposes (e.g., [cost basis](/cost-basis/)), each tranche's fill price and quantity are tracked separately.

## Broker and exchange support

Icebergs are supported on virtually all major U.S. exchanges (NYSE, NASDAQ, regional exchanges) and most brokers (Fidelity, Schwab, Interactive Brokers, Morgan Stanley, Goldman Sachs platforms). Reserve orders are similarly widespread but may have different naming conventions or configuration options. Some platforms call them "work orders," "hidden orders," or "reserve size orders." Verify your broker's terminology and capabilities before designing a trade around either type.

## See also

<div class="wiki-seealso">

### Closely related

- [Day Order vs Good-Till-Cancelled Order](/day-order-vs-good-till-cancelled/) — time-in-force rules apply to iceberg and reserve orders
- [Limit Order](/limit-order/) — base order type for icebergs and reserves
- Order Book — where visible tranches are queued and executed
- [One-Triggers-Other Order](/one-triggers-other-order/) — another complex order type for conditional execution

### Wider context

- Market Impact — why traders use hidden orders
- [Algorithmic Trading](/algorithmic-trading/) — field heavy with iceberg and reserve order use
- [Bid-Ask Spread](/bid-ask-spread/) — how hidden orders affect quote formation
- [Price Discovery](/price-discovery/) — market impact of order visibility

</div>

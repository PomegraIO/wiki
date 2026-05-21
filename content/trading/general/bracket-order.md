---
title: "Bracket order"
description: "A bracket order is a bundle of three linked orders: an entry order (primary) plus two exit orders (profit-taking and stop-loss, as children). When the entry fills, both exit orders become active; when either exit fills, the other is canceled."
keywords:
  - bracket order
  - order types
  - entry and exit
  - conditional orders
image: "/svg/trading.svg"
---

*A **bracket order** is a bundle of three linked orders: a primary entry order plus two child orders for exits. Once the entry fills, both exit orders (a profit target and a stop-loss) become active simultaneously. Whichever exit fills first automatically cancels the other, ensuring you exit the position with a defined profit or loss. The most popular way to automate entry and exit risk management.*

<div class="wiki-hatnote">

For manually linking two exit orders to an entry, see [one-triggers-other](/oto-order/). For two exit orders that pre-exist, see [one-cancels-other](/oco-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bracket order — key facts</div>

<img src="/svg/trading.svg" alt="A bracket order diagram showing entry with take-profit and stop-loss" />

<div class="wiki-infobox-caption">Entry order surrounded by profit target (upper) and stop-loss (lower) — the bracket.</div>

|   |   |
|---|---|
| **What it is** | One entry order + two exit orders, linked |
| **Entry** | Market order, limit order, or stop order |
| **Exits** | Profit-taking limit + stop-loss stop (or both stops, or both limits) |
| **Benefit** | Simple, automatic; both exits placed at once the entry fills |
| **Risk** | Requires defining profit target and stop loss before you enter |
| **Cancellation rule** | First exit to fill cancels the other; order is complete |

</aside>

## The three-part structure

A bracket order has three components:

1. **Entry (primary order).** A [market](/market-order/), [limit](/limit-order/), or [stop order](/stop-order/) to enter the position. You specify size and conditions.
2. **Profit-taking (upper child).** Usually a [limit order](/limit-order/) above the entry price (for a long) to take profits at a target.
3. **Stop-loss (lower child).** Usually a [stop order](/stop-order/) below the entry price (for a long) to cut losses at a threshold.

You submit the entire bracket as a single instruction. The entry order goes active immediately. Once the entry fills, both child orders are placed simultaneously, and they race to fill. The first to fill automatically cancels the second.

## Example: a typical long bracket

You want to buy a stock with a clear plan:
- **Entry:** Limit order to buy 100 shares at $100 (or better).
- **Profit target:** Limit order to sell 100 at $105.
- **Stop-loss:** Stop order to sell 100 at $95.

You submit the bracket. The buy limit sits at $100. When it fills:
- Both the sell limit ($105) and sell stop ($95) are placed.
- If the stock rises to $105, you sell and lock in a $5 gain; the stop is canceled.
- If the stock falls to $95, the stop is triggered and you are sold out; the profit target is canceled.

You have defined your exit before you entered, so there is no emotional decision-making during the trade.

## Bracket orders for shorts

For a short position, the bracket inverts:

- **Entry:** Short 100 at $100.
- **Profit target:** Buy (cover) 100 at $95 (lower price is profit).
- **Stop-loss:** Buy (cover) 100 at $105 (higher price is loss).

The same logic applies: the first exit to fill cancels the other.

## Variants: stop-stop, limit-limit, and others

While the standard bracket is a limit profit target and a stop-loss, you can mix-and-match:

- **Stop-stop bracket:** Both exits are stop orders. Used in certain option strategies or when volatility makes limits impractical.
- **Limit-limit bracket:** Both exits are limit orders. Used when you want to avoid slippage on both sides (but then neither order might fill).
- **Market entry, limit/stop exits:** Most common. You use a market order to enter fast, then limit/stop to exit.

## Advantages of bracket orders

**Automation.** You do not have to manually place the second order after the entry fills. Both are placed atomically.

**Discipline.** You are forced to decide your exit (profit target and stop) *before* you enter. This removes emotional decision-making once the position is live.

**No exposed window.** The two exits are placed simultaneously, so there is no gap in risk coverage. Contrast this with [one-triggers-other](/oto-order/), where there is a tiny delay between fill and second order placement.

**Simplicity.** One command places three orders. Most brokers support bracket orders; they are a standard feature.

## Limitations and risks

**Pre-defined targets.** You have to guess your profit target and stop-loss before you know what price you will actually enter at. If the entry is a market order, you might not know the exact price until after you have already submitted the bracket.

**Cancellation behavior.** If the entry order is partially filled, different brokers handle the exit orders differently. Some adjust the exit quantities; others do not. Understand your broker's logic.

**Order placement delay.** After your entry fills, there is a tiny delay (milliseconds to seconds, depending on the broker) before the exits are placed. In that window, the price could move.

**Partial exit fills.** If the profit target limit partially fills (e.g., 60 of 100 shares), does the entire bracket cancel? Broker rules vary; check your documentation.

## Bracket orders vs. manual entry and exits

| Approach | Speed | Discipline | Flexibility |
|---|---|---|---|
| **Manual** | Slower (you place 1, then 2) | Depends on you | High (adjust exits based on entry price) |
| **Bracket order** | Faster (one command) | Forced | Lower (exits defined in advance) |
| **OTO order** | Medium | Forced | Medium |

## Common use cases

**Day trading.** A [day trader](/day-order/) enters a stock at market, sets a profit target ($1 higher) and a stop-loss ($0.50 lower), and lets the bracket run. Quick, disciplined, automatic.

**Swing trading.** A [swing trader](/swing-trading/) places a limit order to enter a stock, with profit target at a technical resistance and a stop-loss at a broken support level.

**News trading.** After a company announcement, a trader enters with a market order and immediately places a bracket for a quick profit-taking target and a stop-loss in case the news reversal is temporary.

**Risk-defined trades.** Any trade where you know in advance the maximum you are willing to lose and the target profit you want to achieve.

## See also

<div class="wiki-seealso">

### Closely related

- [One-triggers-other](/oto-order/) — sequential orders; more flexible but slower
- [One-cancels-other](/oco-order/) — two mutually exclusive orders
- [Stop order](/stop-order/) — the stop-loss leg
- [Limit order](/limit-order/) — the profit-taking leg
- [Market order](/market-order/) — fast entry

### Order types and variants

- [Stop-limit order](/stop-limit-order/) — stop-triggered limit
- [Trailing stop order](/trailing-stop-order/) — dynamic stop
- Time in force — how long the orders last

### Strategy and context

- Risk management — defining upside and downside
- Position management — entering and exiting trades
- [Day trading](/day-order/) — common user of bracket orders
- [Swing trading](/swing-trading/) — another common use case

</div>

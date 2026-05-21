---
title: "MIT order"
description: "An MIT (market-if-touched) order is a hybrid that becomes a market order only after the price reaches a trigger level. Once triggered, it executes at whatever price the market offers, with no price protection."
keywords:
  - MIT order
  - market-if-touched
  - order types
  - conditional order
image: "/svg/trading.svg"
---

*An **MIT order** (market-if-touched) is a conditional order that becomes a [market order](/market-order) once a trigger price is reached. Unlike a [stop order](/stop-order) (which is also price-triggered), an MIT order is typically used to *enter* a position on a pullback in an uptrend, rather than to exit on a breakdown. Once triggered, it executes at the market, with no price protection.*

<div class="wiki-hatnote">

For price protection when triggered, see [stop-limit order](/stop-limit-order). For automatic reversal in the opposite direction, see [stop order](/stop-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">MIT order — key facts</div>

<img src="/svg/trading.svg" alt="A price chart showing an MIT order trigger point" />

<div class="wiki-infobox-caption">An MIT order waits dormant until price crosses the trigger, then becomes a market order.</div>

|   |   |
|---|---|
| **What it is** | Price-triggered market order |
| **Trigger event** | Price touches your specified level |
| **After trigger** | Executes as a market order at the best available price |
| **Typical use** | Buy on a pullback within an uptrend |
| **Execution certainty** | High (market order usually fills) |
| **Price certainty** | Low (market order at current market) |
| **Difference from stop** | MIT often used for entries; stop for exits |

</aside>

## MIT vs. stop order: the subtle difference

An MIT order and a [stop order](/stop-order) sound similar — both trigger when price touches a level — but they differ in typical use and psychology.

**Stop order:** Typical use is protective. You own a stock at $100 and place a stop at $95 to cut losses. If the stock falls to $95, the stop is triggered and you sell (exit) at a market price.

**MIT order:** Typical use is speculative entry. The stock is in an uptrend around $100. You want to buy a pullback but do not want to set a limit order (which might never fill). You place an MIT at $98. If the stock falls to $98, the MIT triggers and you buy at the market.

In both cases, the order triggers and becomes a market order. The difference is semantic: a stop is used for exits; an MIT is used for entries. But some brokers and traders use the terms interchangeably — just understand the logic and you are fine.

## How an MIT order works

1. **Dormant phase.** You place an MIT order to buy 100 shares at $98 (trigger) while the stock is trading at $100.
2. **Trigger phase.** The stock falls to $98 and the MIT is triggered.
3. **Execution phase.** The order immediately becomes a [market order](/market-order) to buy 100 at the best available price (currently around $98, but could be lower if the stock is still falling).

The execution happens almost instantly — there is no delay between trigger and market execution.

## MIT orders and liquidity

Because an MIT becomes a market order after trigger, execution is nearly guaranteed (unlike a [limit order](/limit-order) that might never fill). This is the upside. The downside is that in a fast market, the price at execution could be far from your trigger price.

**Example:** The stock triggers your MIT at $98. By the time the market order executes, the price has fallen to $97.50. You buy at $97.50, not $98.

This is the opposite of the [stop order](/stop-order) risk, where you might expect a fill at $95 but get $85 instead.

## MIT orders in breakout vs. pullback strategies

**Breakout traders** might use a MIT (or more commonly, a [stop order](/stop-order)) to buy on a breakout above resistance. "If it breaks $105, buy at the market."

**Pullback traders** might use an MIT to buy dips in an uptrend. "If it pulls back to $98, buy at the market."

Both work the same way mechanically; the strategy logic is different.

## MIT orders with limit orders: a hybrid

Some traders use both. For example:
- Place a [limit order](/limit-order) to buy at $98.
- Place an MIT to buy at $98 as well.

If the limit order does not fill (price bounces before reaching $98), the MIT never triggers. If the limit order fills, you are bought. But if the price falls past $98 without ever trading exactly at $98 (a gap), the limit will not fill, but the MIT will trigger and you will buy at the market at the lower price.

This hybrid covers both cases: patient entry (limit) plus panic entry (MIT) on a gap.

## Practical scenarios

**Scenario 1: Reversal entry.** A stock has been falling. Technical analysis suggests support at $50. You place an MIT at $50. If the stock truly bounces at $50, the MIT triggers and you buy at the market (likely $50.00-$50.10). If the stock breaks below $50, the MIT still triggers and you buy at $49.50 or $49.00, depending on how fast it falls. The MIT ensures you do not miss the entry if support breaks.

**Scenario 2: Confirmation entry.** The stock is around $100 and you expect a move. You do not want to chase it higher, so you place an MIT at $100.10 (a small confirmation above current price). If the stock rallies past $100.10, the MIT triggers and you enter the momentum at market.

## MIT orders with poor broker support

Not all brokers explicitly label or support an MIT order. Some treat an MIT as a variant of a [stop order](/stop-order) and call it a "buy stop" (as opposed to a "sell stop"). The logic is the same; the terminology is just different.

If your broker does not support MIT, you can often achieve the same result with a [stop order](/stop-order) configured for an entry (buy stop at a level above the current price, or sell stop at a level below) rather than an exit.

## MIT vs. stop-limit

An MIT becomes a market order after trigger; a [stop-limit order](/stop-limit-order) becomes a limit order. The MIT is more certain to execute; the stop-limit protects price but risks not filling.

| Order type | Trigger | After trigger | Execution risk | Price risk |
|---|---|---|---|---|
| **MIT** | Price threshold | Market order | Low | High |
| **Stop-limit** | Price threshold | Limit order | High (no fill) | Low |

Choose MIT when execution is critical. Choose stop-limit when price protection is critical.

## See also

<div class="wiki-seealso">

### Closely related

- [Stop order](/stop-order) — very similar; typically used for exits
- [Market order](/market-order) — what MIT becomes after trigger
- [Stop-limit order](/stop-limit-order) — adds price protection to a triggered order
- [Limit order](/limit-order) — an alternative entry mechanism

### Order types and variants

- [Trailing stop order](/trailing-stop-order) — dynamic trigger level
- [One-cancels-other](/oco-order) — two mutually exclusive orders
- [One-triggers-other](/oto-order) — sequential orders

### Context and strategy

- Position management — entering on confirmation
- Technical analysis — support and resistance levels
- [Breakout trading](/breakout-trading) — confirming moves past key levels

</div>

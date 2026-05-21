---
title: "Order Types"
description: "Instructions to buy or sell securities with specified conditions (price, timing, size). Different types serve different trading needs."
---

*An order is an instruction to buy or sell a security, but the instruction can take many forms. A [limit order](/wiki/limit-order/) waits for a specific price; a [market order](/wiki/market-order/) buys immediately at the best available price; a [stop order](/wiki/stop-order/) triggers only if the price moves in a particular direction. Traders choose order types to manage execution risk, slippage, and market impact.*

## Market orders: instant execution at any price

A [market order](/wiki/market-order/) says, "Buy 100 shares of Apple right now, whatever the price." It is the simplest and most aggressive order type. The order is guaranteed to fill immediately at the best available prices from [market makers](/wiki/market-makers/) and other sellers. For illiquid stocks, a [market order](/wiki/market-order/) can slip by several percentage points. For highly liquid stocks like Microsoft, it might slip by a fraction of a penny.

Traders use [market orders](/wiki/market-order/) when execution speed matters more than price—for instance, when they are trying to establish a position quickly or respond to breaking news. The tradeoff is that they accept whatever price prevails at the moment of execution.

## Limit orders: specify the price

A [limit order](/wiki/limit-order/) says, "Buy 100 shares of Apple, but only at $150 or lower." The order sits in the exchange's order book, waiting. If the price drops to $150 or below, the order fills automatically. If the price never falls that low, the order may expire unfilled at the end of the trading day (a [day order](/wiki/day-order/)) or remain active until cancelled ([good-till-cancelled](/wiki/gtc-order/) or GTC).

[Limit orders](/wiki/limit-order/) guarantee the price but not the execution. A trader who sets a limit might never get filled, especially if they set the limit far below the current market price. However, they protect against slippage and are the preferred tool for patient traders and large institutional orders that would suffer significant market impact if executed all at once.

## Stop orders: trigger on price movement

A [stop order](/wiki/stop-order/) activates only when the price touches a specified trigger level. A common example: "Sell 100 shares if the price falls to $140"—this is a stop-loss order. Once the stock reaches $140, the stop order converts into a [market order](/wiki/market-order/) and fills at the next available price, which may be lower than $140 if the market is moving quickly.

[Stop orders](/wiki/stop-order/) are popular for risk management and technical trading. The risk is that in a fast market, the fill price can be far from the trigger price, especially if liquidity dries up suddenly.

## Stop-limit orders: combine both protections

A [stop-limit order](/wiki/stop-limit-order/) combines a stop and a limit. Example: "When the price reaches $140, activate a limit order to sell at $138 or higher." This guarantees the worst price you'll accept (the limit), but also risks no fill if the market gaps through the trigger level without pausing in the limit zone.

## All-or-none and fill-or-kill orders

An [all-or-none](/wiki/all-or-none/) (AON) order says, "Fill the entire order or reject it—no partial fills." This is useful for traders who need a specific quantity or nothing.

A [fill-or-kill](/wiki/fill-or-kill/) (FOK) order is more aggressive: "Execute immediately at the best available prices. If you can't fill the entire order in the next few seconds, cancel the whole thing." FOK orders are often used in algorithmic trading to avoid leaving partial fills on the book.

## Time-based order conditions

Orders can have time qualifiers. A [day order](/wiki/day-order/) (the default on most exchanges) cancels at the end of the trading day if not filled. A [good-till-cancelled](/wiki/gtc-order/) (GTC) order remains active indefinitely until the trader cancels it or the broker's system expires it (typically after 30–90 days). A [good-till-date](/wiki/gtd-order/) (GTD) order remains active until a specific calendar date.

For options and other derivatives, [good-for-opening](/wiki/opening-auction/) (GFO) orders only execute in the [opening auction](/wiki/opening-auction/), and [at-the-opening](/wiki/at-the-market-offering/) (ATO) orders execute only at the [opening cross](/wiki/opening-cross/).

## Pegging and algorithmic orders

Advanced traders use orders that adjust dynamically. A [mid-point peg](/wiki/midpoint-peg/) order adjusts its limit price to always sit at the midpoint between the current [bid](/wiki/bid-ask-spread/) and ask. A [peg order](/wiki/peg-order/) pins itself to the [bid](/wiki/bid-ask-spread/) or ask, moving as those prices change.

[TWAP](/wiki/twap-order/) (time-weighted average price) and [VWAP](/wiki/vwap-order/) (volume-weighted average price) orders are algorithmic—they break a large order into smaller pieces over time or volume, trying to execute near the market's typical price without causing large price movements.

## Hidden and iceberg orders

Traders who fear [market impact](/wiki/market-risk/)—the risk that announcing their large order will move the market against them—can use [hidden orders](/wiki/hidden-order/) or [iceberg orders](/wiki/iceberg-order/). A hidden order is invisible to other traders until it fills. An [iceberg order](/wiki/iceberg-order/) shows a small visible portion (say, 1,000 shares) and refreshes it automatically as it fills, hiding the true size until the end.

The cost of anonymity is that [hidden orders](/wiki/hidden-order/) and [icebergs](/wiki/iceberg-order/) do not enjoy the same priority rules as visible orders. If two visible orders arrive at the same price at the same time, the first one wins. A hidden order that arrives at the same time is queued behind both visible orders.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/limit-order/">Limit order</a> — wait for a specific price.</li>
  <li><a href="/wiki/market-order/">Market order</a> — execute immediately.</li>
  <li><a href="/wiki/stop-order/">Stop order</a> — trigger on price movement.</li>
  <li><a href="/wiki/iceberg-order/">Iceberg order</a> — hide size to avoid market impact.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/market-makers/">Market makers</a> — intermediaries who execute orders.</li>
  <li><a href="/wiki/opening-auction/">Opening auction</a> — special order handling at the market open.</li>
  <li><a href="/wiki/best-execution/">Best execution</a> — rules ensuring fair order handling.</li>
</ul>
</div>

---
title: "Opening Cross"
description: "The mechanism for setting the opening price at the start of each trading day by matching buy and sell orders at a single price."
---

*The opening cross is the process that determines the first price of a stock each trading day. Traders submit orders before the market opens; the exchange collects them and finds a single price at which the maximum number of shares can be bought and sold simultaneously. This process discovers a fair opening price without the chaos of a free-for-all auction.*

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Opening cross — key facts</div>
  <table>
    <tr><th>When it occurs</th><td>9:30 a.m. ET for U.S. stocks</td></tr>
    <tr><th>Input</th><td>All orders submitted before open (limit and market)</td></tr>
    <tr><th>Output</th><td>Single opening price; all matched orders execute</td></tr>
    <tr><th>Goal</th><td>Fair price discovery; maximum participation</td></tr>
    <tr><th>Participation</th><td>Institutional and retail traders, market makers</td></tr>
  </table>
</aside>

## How it works

In the pre-market phase (typically 4 a.m. to 9:30 a.m. for U.S. stocks), traders submit [limit orders](/wiki/limit-order/) and [market orders](/wiki/market-order/). The [limit orders](/wiki/limit-order/) are priced—"Buy at $150 or less" or "Sell at $151 or higher." [Market orders](/wiki/market-order/) have no price restriction; they are willing to trade at any price.

At 9:30 a.m., the exchange's computer algorithm runs the opening cross. It starts with the [market orders](/wiki/market-order/), which will trade at any price. Then it tries to find a single price where the number of buy [limit orders](/wiki/limit-order/) at or above that price equals the number of sell [limit orders](/wiki/limit-order/) at or below that price. That's the opening price.

Example: Suppose at the opening, there are 100,000 shares of demand (willing to buy at $150 or higher) and 80,000 shares of supply (willing to sell at $150 or lower) at $150. The opening cross sets the price at $150. All orders—buy and sell—execute at $150. The 100,000 buyers get 80,000 shares filled, and the remaining 20,000 shares of buy interest waits for post-opening trading.

## Who participates?

The opening cross is not exclusive to [market makers](/wiki/market-makers/). Any trader can submit a [pre-market order](/wiki/pre-market-trading/). Retail traders often participate through their brokers. Institutional traders submit orders directly to exchanges. [Algorithmic traders](/wiki/algorithmic-trading/) submit pre-calculated order sizes based on overnight news and [futures](/wiki/futures-contract/) prices.

The opening cross is usually the most liquid moment of the day. Trillions of dollars of volume execute in the first few minutes. This concentrated liquidity makes the opening an ideal time for large institutions to enter or exit positions without moving the price.

## Opening price discovery advantages

Setting one price (rather than executing a series of small trades at varying prices as the market opens) has several benefits:

**Fairness:** All traders at the opening price get the same execution, whether they submitted their order a minute before the open or an hour before.

**Efficiency:** By batching all pre-market orders and finding a single clearing price, the exchange eliminates the need for individual price negotiation.

**Information aggregation:** The opening price reflects all the information available to traders before the market opens (overnight news, Asian and European market moves, [futures](/wiki/futures-contract/) prices).

## The opening auction detail

Exchanges publish an "opening auction detail" in the seconds before 9:30 a.m., showing the projected opening price, the quantity of shares likely to trade, and whether the cross is "balanced" or if there are excess buy or sell orders. Traders use this information to adjust their orders if they wish—a final chance to reprice before the cross executes.

The [opening auction detail](/wiki/opening-auction-detail/) is important for large traders who are trying to execute significant volume. If there is an excess of buy orders, the opening price may be higher than expected, and a buyer might increase their [limit order](/wiki/limit-order/) price to be sure to get filled. Conversely, an excess of sell orders suggests the opening price will be lower.

## Post-opening trading

After the opening cross, the market transitions to continuous [post-market trading](/wiki/regular-trading-hours/). New [limit orders](/wiki/limit-order/) are matched one at a time against each other or against [market makers](/wiki/market-makers/). Prices can move any direction as new information arrives or trader demand shifts.

Some traders specialize in the opening: they accumulate positions at the opening price and liquidate them in the first hour when liquidity is concentrated and [bid-ask spreads](/wiki/bid-ask-spread/) are tight. Others avoid the opening because it often has high volatility—overnight news can cause large price swings.

## Electronic implementation

The opening cross is handled entirely by electronic systems. The exchange's computer collects orders from all [brokers](/wiki/broker/) in real-time and runs the matching algorithm at precisely 9:30 a.m. (or 9:31 for NASDAQ, which has two opening auctions). The entire process takes milliseconds. Traders learn the opening price and their fill status through their broker's trading systems.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/opening-auction/">Opening auction</a> — the general concept.</li>
  <li><a href="/wiki/closing-auction/">Closing auction</a> — the corresponding process at end-of-day.</li>
  <li><a href="/wiki/opening-auction-detail/">Opening auction detail</a> — market imbalance information before the open.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/stock-exchange/">Stock exchange</a> — where the opening cross runs.</li>
  <li><a href="/wiki/pre-market-trading/">Pre-market trading</a> — orders submitted before the cross.</li>
  <li><a href="/wiki/limit-order/">Limit order</a> — priced orders used in the cross.</li>
</ul>
</div>

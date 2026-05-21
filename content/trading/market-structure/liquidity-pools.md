---
title: "Liquidity Pools"
description: "Pools of buy and sell interest that traders can tap to execute orders, found in exchanges, dark pools, and decentralized finance venues."
---

*A liquidity pool is a concentration of executable buy and sell interest at a given price. If an exchange shows "500,000 shares bid at $150," that's a liquidity pool—you can sell 500,000 shares at that price instantly. Pools form when many traders converge on the same price. Traders value size and tightness of pools; tight pools with large volume indicate efficient markets where it's easy to transact.*

<div class="wiki-hatnote">
For the broader concept of market liquidity, see <a href="/wiki/liquidity-risk/">/liquidity-risk/</a>.
</div>

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Liquidity pools — key facts</div>
  <table>
    <tr><th>Definition</th><td>Buy and sell interest available at a specific price</td></tr>
    <tr><th>Where they form</th><td>Exchanges, dark pools, market makers, DeFi protocols</td></tr>
    <tr><th>Measured by</th><td>Price level and size (share volume)</td></tr>
    <tr><th>Depth</th><td>How much volume can execute before price moves significantly</td></tr>
    <tr><th>Fragmentation</th><td>Pools split across venues makes execution harder</td></tr>
  </table>
</aside>

## How liquidity pools form

At any given moment, every [market maker](/wiki/market-makers/) and trader has a [bid and ask](/wiki/bid-ask-spread/). A [market maker](/wiki/market-makers/) might bid $150.00 for 100,000 shares and ask $150.01 for 100,000 shares. That bid represents a liquidity pool: if you want to sell now, you can hit the bid and sell up to 100,000 shares at $150.00.

When multiple [market makers](/wiki/market-makers/) quote the same bid price (or prices very close), their orders in the exchange's order book stack up, creating a larger pool. A stock with 10 [market makers](/wiki/market-makers/) each bidding $150.00 for 50,000 shares has a liquidity pool of 500,000 shares at the bid.

## Order book depth

The order book shows the "depth" of liquidity pools at multiple price levels. When you open a trading terminal, you see:

**Ask side (sell orders):**
- 100,000 shares at $150.05
- 50,000 shares at $150.10
- 200,000 shares at $150.15

**Bid side (buy orders):**
- 75,000 shares at $150.00
- 150,000 shares at $149.95
- 100,000 shares at $149.90

These are liquidity pools. A buyer can purchase 100,000 shares immediately at $150.05 (hitting the first ask pool), or if they submit a [market order](/wiki/market-order/) for 200,000 shares, they'll buy 100,000 at $150.05 and 50,000 at $150.10, consuming two pools and moving the price up.

## Liquidity fragmentation and market impact

One of the challenges in modern markets is that liquidity is fragmented. A stock might have order books on the NYSE, NASDAQ, multiple regional exchanges, and several [dark pools](/wiki/dark-pools/). The liquidity pools are split across venues, so a trader trying to buy a large quantity must "peel the book"—execute at multiple levels and venues to get the full quantity, paying a worse average price than if all liquidity were in one place.

This is why [smart order routers](/wiki/smart-order-router/) exist: they search for liquidity across all venues and route the order to achieve the best execution. A [smart router](/wiki/smart-order-router/) might split a 500,000-share order: 100,000 to NYSE, 150,000 to NASDAQ, 200,000 to a [dark pool](/wiki/dark-pools/), and 50,000 to a [market maker](/wiki/market-makers/).

## Liquidity pools in dark pools

[Dark pools](/wiki/dark-pools/) advertise liquidity pools to attract traders. An exchange or broker might publish, "We have a 500,000-share pool of Microsoft available to buy." This is meant to indicate that counterparty interest exists. A trader can then route an order to the [dark pool](/wiki/dark-pools/) knowing there is likely a match.

Unlike lit exchanges, [dark-pool](/wiki/dark-pools/) liquidity pools are often indicative (not guaranteed). The advertised pool might fill only partially, or the price might be worse than advertised.

## Liquidity pools in DeFi

In decentralized finance (DeFi), liquidity pools have a specific meaning: a pool of cryptocurrencies deposited by liquidity providers, used by the protocol to execute trades. A Uniswap liquidity pool might hold 1,000 Ethereum and 3 million USDC. Traders can buy Ethereum by trading USDC into the pool and withdrawing Ethereum.

The larger the pool, the lower the "slippage"—the price impact of a large trade. A trader buying $100,000 of Ethereum in a 1,000 ETH pool might suffer significant slippage. The same trade in a 10,000 ETH pool would have much lower slippage.

## Liquidity pool quality

Not all pools are equal. A pool that can execute quickly is worth more than a pool with execution delays. A pool at a fair price is worth more than a pool that is consistently wide. Traders evaluate pools based on:

**Size:** How many shares or units can execute at the quoted price?

**Tightness:** How wide is the [bid-ask spread](/wiki/bid-ask-spread/) at the pool?

**Speed:** How fast can the order execute?

**Counterparty quality:** Will the order be filled, or is there counterparty risk?

## Dry liquidity pools

Sometimes a pool appears on the order book but isn't real—a trader posts a large order intending to cancel it if it gets close to execution. This "dry" liquidity is used to manipulate perception of demand or supply. Regulators prohibit this practice (it's called "layering" or "spoofing"), but it still happens, especially in markets with less surveillance.

Dry pools create false signals and can trap uninformed traders into believing there is more liquidity than actually exists.

## Importance for market quality

The breadth and depth of liquidity pools in a security are crucial to market quality. A stock with deep liquidity pools can be traded in large size without significant price movement. A stock with shallow pools is hard to trade in size and suffers high [market impact](/wiki/market-risk/).

This is why [high-frequency traders](/wiki/high-frequency-trading/) and [market makers](/wiki/market-makers/) compete to provide liquidity: the larger and deeper the pools they can create, the more they benefit from the bid-ask spread.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/order-book/">Order book</a> — displays liquidity pools at each price level.</li>
  <li><a href="/wiki/bid-ask-spread/">Bid-ask spread</a> — width of the liquidity pool.</li>
  <li><a href="/wiki/dark-pools/">Dark pools</a> — advertise liquidity pools away from exchanges.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/market-makers/">Market makers</a> — create and maintain liquidity pools.</li>
  <li><a href="/wiki/smart-order-router/">Smart order router</a> — finds liquidity across venues.</li>
  <li><a href="/wiki/liquidity-risk/">Liquidity risk</a> — broader concept of market liquidity.</li>
</ul>
</div>

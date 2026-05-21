---
title: "Bid-Ask Spread"
description: "The difference between the highest price a buyer is willing to pay and the lowest price a seller is willing to accept. A measure of liquidity and transaction cost."
---

*The bid-ask spread is the cost of transacting. When you buy a stock, you pay the asking price; when you sell, you receive the bid price. The gap between them—usually measured in cents or fractions of a cent—is the fee that [market makers](/wiki/market-makers/) and exchanges earn in exchange for standing ready to trade.*

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Bid-ask spread — key facts</div>
  <table>
    <tr><th>Bid</th><td>Highest price buyers are currently offering</td></tr>
    <tr><th>Ask</th><td>Lowest price sellers are currently offering</td></tr>
    <tr><th>Spread</th><td>Ask minus bid (always non-negative)</td></tr>
    <tr><th>Measurement</th><td>Dollars, cents, basis points, or percentages</td></tr>
    <tr><th>Drivers</th><td>Liquidity, volatility, inventory risk, adverse selection</td></tr>
  </table>
</aside>

## How the spread works

At any given moment, an exchange publishes the [national best bid and offer](/wiki/nbbo/) (NBBO)—the highest bid and lowest ask across all connected trading venues for a security. If Apple is trading with a bid of $150.00 and an ask of $150.01, the spread is 1 cent per share. If you buy 1,000 shares, you pay $150,010 for a security whose midpoint price is $150.005. Your cost of buying is effectively 0.5 cents per share—you've bought 500 shares worth at the midpoint and paid a $5 spread to get filled.

The buyer and seller don't always negotiate the spread directly. Instead, [market makers](/wiki/market-makers/) quote both sides simultaneously. When you place a [market order](/wiki/market-order/) to buy, you hit the ask—the market maker sells to you. When you place an order to sell, you hit the bid—the market maker buys from you. The market maker keeps the spread as compensation.

## Why spreads exist

[Market makers](/wiki/market-makers/) face uncertainty. When they post a bid and ask, they don't know which side will trade next. If they quote $150.00 bid and $150.01 ask, and only buyers arrive, they accumulate inventory. That inventory is marked-to-market daily; if the stock price drops, they lose. The spread is their compensation for bearing this inventory risk and the cost of adverse selection—the risk that the next trader to hit their quote is better-informed and will profit at their expense.

Spreads also compensate for the cost of complying with regulations, maintaining technology, and competing for order flow. A [market maker](/wiki/market-makers/) who quotes a 1-cent spread might earn 10 basis points per share on volume, but only after paying exchange fees, regulatory fines, and the cost of hedging inventory risk.

## Spreads vary by liquidity

High-volume stocks like Apple or Microsoft have tight spreads—often 1 or 2 cents ($0.01–$0.02) even for large orders. Spreads on illiquid or volatile stocks can be 10 cents or wider. A penny stock might have a spread of several dollars.

Likewise, spreads widen during periods of uncertainty. When the market is in [circuit breaker](/wiki/circuit-breaker/) halt, volatility spikes, or a company announces major news, [market makers](/wiki/market-makers/) widen their spreads to compensate for increased inventory risk. During the 2020 COVID crash, spreads on U.S. equities widened 5–10 times wider than normal.

## Measuring spreads

The "spread" can be quoted in multiple ways:

**Absolute spread:** The difference in dollars: $150.01 − $150.00 = $0.01.

**Percentage or basis-point spread:** $0.01 / $150.005 ≈ 0.67 basis points, or 0.0067%. Basis points are standard for bonds and foreign exchange.

**Effective spread:** The average cost per share paid by traders buying and selling over a period. It accounts for the fact that a [limit order](/wiki/limit-order/) sitting at the bid may not execute at exactly the quoted bid—it might execute at a worse price in a fast market.

## The spread and algorithm execution

When a large trader wants to buy or sell a large quantity without moving the market, they use an algorithm that breaks the order into smaller pieces over time or volume. The goal is to minimize the total cost, including the spread on each piece. A trader buying a million shares might employ a [VWAP](/wiki/vwap-order/) algorithm that buys in proportion to the day's trading volume, spreading the execution over hours.

The wider the spread, the longer the algorithm must work to avoid moving the market. A bid-ask spread of 10 cents on a low-volume stock might add 5–10% to the total cost of a million-share trade.

## Spread compression over 30 years

Since the 1990s, spreads have compressed dramatically. Electronic markets, [decimal pricing](/wiki/decimal-pricing/) (moving from 1/8-inch increments to pennies), and competition from [high-frequency traders](/wiki/high-frequency-trading/) have all contributed. On major stocks, the spread is rarely more than a few cents. For exchange-traded funds ([ETFs](/wiki/etf/)), spreads on the largest, most liquid funds are often under a penny.

This compression has benefited retail traders enormously. But it has also tightened profit margins for traditional [market makers](/wiki/market-makers/), who now compete with [algorithmic traders](/wiki/algorithmic-trading/) and must process orders at higher speeds and lower costs to survive.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/market-makers/">Market makers</a> — intermediaries who quote spreads.</li>
  <li><a href="/wiki/nbbo/">National best bid and offer</a> — the widest spread across all venues.</li>
  <li><a href="/wiki/high-frequency-trading/">High-frequency trading</a> — competition that narrows spreads.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/market-order/">Market order</a> — trades that hit the spread immediately.</li>
  <li><a href="/wiki/limit-order/">Limit order</a> — trades that sit on the book at bid or ask.</li>
  <li><a href="/wiki/stock-exchange/">Stock exchange</a> — venues where spreads are quoted.</li>
</ul>
</div>

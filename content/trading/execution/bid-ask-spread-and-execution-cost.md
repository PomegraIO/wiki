---
title: "Bid-Ask Spread as an Execution Cost"
description: "The bid-ask spread is a direct execution cost—the difference between the buy and sell prices—quantified as a percentage or basis points, separate from commissions and market impact."
keywords:
  - bid ask spread execution cost
  - bid-ask spread
  - execution cost trading
  - round-trip transaction cost
  - spread cost calculation
---

*The **bid-ask spread** is the most visible component of execution cost. It is the gap between the highest price buyers will pay (the bid) and the lowest price sellers will accept (the ask). Every trade you execute incurs this spread as a friction cost: a round-trip buy-and-sell transaction costs you twice the spread, regardless of which direction you are moving.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bid-Ask Spread as Execution Cost — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The spread is pure friction: paid on every trade, quantified instantly.</div>

|   |   |
|---|---|
| **Definition** | Difference between ask price and bid price |
| **Round-trip cost** | Twice the spread (buy at ask, sell at bid) |
| **Measurement** | Basis points or percentage of mid-price |
| **Determinants** | Volatility, liquidity, order book depth |
| **Impact on returns** | Cumulative across high-frequency trading; negligible for buy-and-hold |
| **Separate from** | Commissions, market impact, borrowing costs |

</aside>

## The spread as half the round-trip cost

When you buy a stock, you pay the ask price. When you sell the same stock, you receive the bid price. The difference—the spread—is a cost you incur both ways.

Imagine Apple shares with a bid of $210.00 and an ask of $210.05. The spread is $0.05 per share. If you buy 1,000 shares, you pay $210,050. If you immediately sell those 1,000 shares, you receive $210,000. The $50 loss is not because the price moved; it is purely the cost of the spread, paid round-trip.

In percentage terms, the spread is $0.05 / $210.025 (the mid-price) = 0.024%, or about 2.4 basis points. For a trader making a round trip, the total cost is 4.8 basis points. For passive investors holding long-term, a single entry and exit over years means the round-trip spread is amortized over the holding period. For active traders or algorithms making dozens of trades per day, the spread compounds quickly.

## How spreads vary by liquidity and volatility

The [bid-ask spread](/bid-ask-spread/) is tightest (smallest) for the most liquid securities and widens when conditions worsen. 

In the most liquid markets—mega-cap stocks on the NYSE, major currency pairs on FX venues, the S&P 500 futures contract—the spread often narrows to a single tick or cent: $0.01 per share for equities, $0.0001 per currency unit. At massive scale, the spread becomes effectively a few basis points or less.

In thin or less-traded securities, the spread widens. A micro-cap stock or an obscure corporate bond might have a spread of $0.50 or more, representing hundreds of basis points. This is why trading less-liquid assets incurs a hidden tax that compounds: not only is the spread wider, but the order depth (the volume available at the best prices) is shallow, meaning large orders suffer additional market impact.

Volatility also expands spreads. During market stress or earnings announcements, [market makers](/market-maker-trading/) widen the spread to compensate for the increased risk that the price will move sharply against them. A stock with a usual spread of $0.02 might widen to $0.10 during the first minutes after earnings.

## Calculating spread cost over time and portfolio size

To quantify the impact of bid-ask spread on your returns, multiply the percentage spread by the dollar volume traded, accounting for round trips.

**Example 1: Single trade.** You trade 10,000 shares of a stock at a mid-price of $100. The bid-ask spread is $0.10, or 10 basis points of the $100 price. Your round-trip cost is 20 basis points, or 0.20%, which is 0.0020 × $1,000,000 = $2,000.

**Example 2: Multiple round trips.** An algorithm makes 100 round-trip trades per day on 1,000 shares each, trading stocks with an average spread of 2 basis points. Each round trip costs 4 basis points; 100 round trips accumulate 400 basis points, or 4%, of the daily trading volume. If the daily trading volume is $10 million, the spread cost is $400,000 per day—a massive drag on profitability.

**Example 3: Long-term investor.** You buy $100,000 of an index fund at an average spread of 1 basis point and sell 30 years later at a 1 basis point spread. Total spread cost: 2 basis points, or $20. Over 30 years, this is immaterial to long-term returns.

## Spread vs. commission and market impact

The bid-ask spread is only one layer of execution cost. It is separate from commissions (the fees you pay to your broker) and market impact.

**Commissions** are direct broker fees: $5 per trade, a percentage of volume, or zero for certain brokers. They are distinct from the spread and are sometimes waived entirely.

**Market impact** is the effect of your order on prices. When you submit a large buy order, you move the market up slightly; when you sell, you move it down. The difference between your expected execution price and the actual price you achieve is market impact. This is especially significant for large trades or in less-liquid assets. Market impact is paid on top of the spread.

A trader executing a small order in a highly liquid stock pays mostly spread cost. A trader executing a multi-million-dollar block in a thinly traded bond pays spread plus substantial market impact.

## Spread compression and technology

Over the past two decades, spreads have compressed dramatically in equities and FX, driven by electronic trading, competition among venues, and co-location. The average spread in a mega-cap stock on a U.S. exchange is now a penny or less. In contrast, before electronic trading, spreads in less-liquid stocks were measured in multiples of cents.

This compression benefits all traders but especially retail and smaller institutional investors who now can trade at prices that were previously available only to large institutional traders. Conversely, as spreads compress, the returns available to [market makers](/market-maker-trading/) from passive spread capture shrink, pushing them toward more active strategies.

Technology also enables [pegged orders](/pegged-order-types/), which automatically track the best bid or ask and allow traders to access better prices without manually adjusting their limit orders.

## The irrelevance of spread for buy-and-hold investors

For a traditional investor buying a diversified portfolio and holding for decades, bid-ask spreads are negligible. A 2 basis point spread on a 7% annual return compounds to a trivial impact over 30 years. The investor's real costs are fund expense ratios, taxes, and market impact on large initial and final trades.

For active traders, algorithms, and [hedge funds](/hedge-fund/) making dozens of trades per day, the spread is a critical performance metric. A fund with a spread cost of 50 basis points per trade and 200 trades per year can easily return negative 10% before any [alpha](/alpha/) is generated.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the definition and measurement of the spread itself
- Market Impact — the additional cost from your order moving prices
- [Market Order](/market-order/) — an order that fills immediately at the current ask (for buys) or bid (for sells)
- [Fill-or-Kill Order Explained](/fill-or-kill-order-explained/) — execution instruction with no partial fills and no queue resting
- [Pegged Order Types](/pegged-order-types/) — orders that automatically track the best bid or ask

### Wider context

- [Broker](/broker/) — intermediary who executes orders and charges commissions
- [Market Maker](/market-maker-trading/) — trader who profits from the bid-ask spread by posting liquidity
- [Algorithmic Trading](/algorithmic-trading/) — systematic trading using execution logic and order types
- [Stock Exchange](/stock-exchange/) — venue where buyers and sellers interact via the order book

</div>

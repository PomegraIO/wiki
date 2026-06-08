---
title: "Slippage and Market Impact for Large Order Traders"
description: "How institutional traders face slippage and market impact when orders are large relative to daily volume, and how professionals mitigate costs."
keywords:
  - trader slippage market impact large orders
  - slippage institutional trading
  - market impact trading
  - large order execution costs
  - algorithmic execution traders
  - impact costs trading
image: "/svg/people.svg"
---

*A retail trader buying 100 shares of a liquid stock executes instantly at the [bid-ask spread](/bid-ask-spread/); an institutional manager buying 500,000 shares moving against its own trade—the market absorbs the first 10,000 shares at the offered price, then requires higher prices to pull in the next 10,000, and so on, until the full order is filled. That price slippage—the difference between the price you wanted and the price you got—plus the permanent *market impact* (the fact that the stock is now 2% higher because of your buying) are costs that gnaw on returns for large traders. Professionals mitigate through algorithm execution, [dark pools](/over-the-counter-market/), and careful sizing, but some impact is unavoidable.*

<div class="wiki-hatnote">

This article addresses execution slippage and market impact for traders and fund managers, not volatility or intraday price swings. For the mechanics of the [bid-ask spread](/bid-ask-spread/), see that entry; for [algorithmic trading](/algorithmic-trading/) strategy, see its dedicated page.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Slippage & Market Impact — key facts</div>

<img src="/svg/people.svg" alt="An abstract editorial mark for traders." />

<div class="wiki-infobox-caption">Large orders move markets against themselves; costs scale with size and illiquidity.</div>

|   |   |
|---|---|
| **Slippage definition** | Price paid vs. reference price (often opening or current midpoint) |
| **Market impact** | Price movement caused by your order itself |
| **Cost scaling** | Rises with order size relative to average daily volume |
| **Volume ratio threshold** | >5% of daily volume = material impact; >10% = severe |
| **Liquidity drag** | Illiquid stocks amplify impact; liquid stocks dampen it |
| **Timing cost** | Urgent execution trades worse than patient execution |
| **Mitigation tools** | Algorithms, [VWAP](/algorithmic-trading/), [TWAP](/algorithmic-trading/), dark pools, block trades |

</aside>

## Why Size Creates a Cost Problem

Imagine a stock with an average daily volume of 1 million shares. The [bid-ask spread](/bid-ask-spread/) is 2 cents, and the current mid-price is $50. A retail buyer submitting a market order for 1,000 shares gets filled at roughly the ask ($50.01) in milliseconds. Total slippage: $10 on a $50,000 order—0.02%.

Now suppose a large mutual fund wants to buy 500,000 shares (half the daily volume) at or near the open. It submits a market order. The first 50,000 shares fill at $50.01. The next 50,000 shares are at $50.02, then $50.03, then $50.05, and so on. By the time the fund has bought 500,000, the stock is $50.15, and the fund has paid an average of $50.08. The slippage is $40,000 on a $25 million order—0.16%. Multiply that across 20 trades per quarter and the fund is leaving hundreds of thousands on the table each year.

The slippage arises because the order exhausts the available supply at each price level. [Market makers](/market-maker-trading/) and other liquidity providers are willing to sell 50,000 shares at $50.01, but selling 500,000 at that price is not in their interest—they'd be absorbing massive short-term inventory. So they raise their ask price, moving up the supply curve as the large buyer pulls more shares. This is the literal definition of *market impact*: the stock's price moves *because* of the order, not because new information arrived.

## Decomposing Slippage: Temporary and Permanent

Professionals split slippage into two pieces:

1. **Temporary impact**: The bid-ask spread and immediate temporary price pressure. If you buy 500,000 shares and the stock rises $0.14 during your execution, but falls back to $50.01 within an hour after you're done, the $0.14 temporary impact is the cost of moving through the order book quickly. Stop, and the temporary impact shrinks.

2. **Permanent impact**: The new equilibrium price after your order. If the stock was $50.00, you bought 500,000 shares, and the stock now settles at $50.05 permanently—reflected in the next trades from unrelated buyers and sellers—then you've permanently shifted the price. Your buying was information-like: it signaled demand to the market, and the market repriced upward.

Institutional traders minimize temporary impact by executing slowly (spreading the order over hours or days), but permanent impact is harder to avoid. If you need to buy 500,000 shares because your fund is growing or because a researcher believes the stock is undervalued, the market will reprice it up as you accumulate. That's a real cost of capital accumulation.

## How Order Size Relative to Liquidity Matters

Slippage scales nonlinearly with order size. A 1% order (10,000 shares of a 1 million daily volume stock) has negligible impact. A 5% order has material impact. A 10% order can move the market 0.5–1%. A 20% or larger order can shift the stock 1–3% or more, depending on how aggressive the execution is and how illiquid the stock is.

The key metric is **order imbalance relative to liquidity**. A $10 million order in Microsoft (which trades $30+ billion daily) is a rounding error; a $10 million order in a small-cap stock trading $5 million daily is catastrophic.

Illiquid stocks amplify impact. A stock with $2 million average daily volume has maybe $500,000 of resting bids at any instant. A $5 million order will drain all visible bids, trigger [stop-loss](/loss-aversion/) cascades, and force sellers to take ever-worse prices. The impact can be 2–5% or higher. Liquid stocks with deep order books absorb large orders with modest impact.

## The Execution Algorithm Solution

Professionals address slippage through **execution algorithms**, which break large orders into smaller child orders and execute them over time. Common algorithms include:

- **VWAP (Volume-Weighted Average Price)**: Execute child orders proportional to expected volume throughout the day, aiming to hit the day's volume-weighted average price. If 30% of daily volume trades in the first hour, execute 30% of your order then.
- **TWAP (Time-Weighted Average Price)**: Execute uniformly throughout a time period, aiming for the time-weighted average price.
- **Implementation Shortfall**: Optimize execution by balancing the cost of urgency (fast execution = higher slippage) against the cost of delay (waiting = risk that the price moves against you).

These algorithms reduce *temporary* impact by spreading execution and avoiding visible market pressure at any single moment. The fund might announce its large buy implicitly (other traders notice gradual accumulation over the day), but at least the fund isn't hammering a single large market order into the spread.

The trade-off is *timing risk*: while the fund is executing its algorithm, the stock could rally, leaving the fund with a filled portion at $50.03 and the rest still unexecuted at a worse $50.08. Patience in one moment is urgency in another.

## Dark Pools and Block Trades

Large traders also use [dark pools](/over-the-counter-market/) (private exchanges) and block trading to sidestep public market impact. A fund can negotiate a 500,000-share block trade with another institution through a broker, settling the entire trade without displaying it on a public exchange. The price might be negotiated as a small discount to the public market price (say, 2–4 cents), but the buyer avoids the impact of sending 500,000 shares through the public order book.

This works if a natural counterparty exists (another fund wanting to sell). If no dark pool counterpart is available, the trader falls back to public-market algorithms.

## The Permanent Cost: Information and Herding

A subtler cost is *permanent impact*—the signal your large order sends. If you're buying aggressively, other traders notice (or learn from algorithms tracking your order), and they buy alongside you, pushing the price higher. Your 500,000-share buy lifts the stock, and the next trader considering the same stock faces higher prices because of your order.

This is particularly acute in small-cap or thinly traded sectors. A research fund's large buy in a neglected stock can permanently shift valuation, and while that's good for the fund's existing holdings, it's bad for future accumulation. The fund pays for discovery; later arrivals enjoy the higher price.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the friction cost of immediate execution
- [Algorithmic Trading](/algorithmic-trading/) — execution algorithms that reduce temporary impact
- [Market Maker, Trading](/market-maker-trading/) — how liquidity providers absorb orders
- [Over-the-Counter Market](/over-the-counter-market/) — dark pools and block trades
- Market Impact — permanent price shift from order flow
- [Execution Risk](/execution-risk/) — timing risk and adverse market moves during execution

### Wider context

- [Broker](/broker/) — intermediaries managing large orders
- [Alternative Trading System](/alternative-trading-system/) — venues beyond public exchanges
- [Liquidity Risk](/liquidity-risk/) — inability to sell without price impact
- [Price Discovery](/price-discovery/) — how markets find fair value
- [Market Cycle](/market-cycle/) — how information and order flow reshape prices

</div>

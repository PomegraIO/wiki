---
title: "Half-Spread Cost"
seo_title: "Half-Spread Cost: The Hidden Price of Market Orders"
description: "The half-spread cost is the gap between mid-price and the bid or ask you trade at—the minimum cost of a market order. How to size and reduce it."
keywords:
  - bid-ask spread
  - half spread
  - market order cost
  - trading slippage
  - execution cost
image: /svg/trading.svg
---

*The half-spread cost is the smallest unavoidable expense when you trade immediately at market prices. When you buy, you pay the asking price instead of the mid-point between bid and ask; when you sell, you receive the bid price. This one-way cost—half the total spread—is the minimum price of immediate liquidity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Half-Spread Cost — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and market mechanics." />

<div class="wiki-infobox-caption">The mathematical minimum cost of crossing the market instantly.</div>

|   |   |
|---|---|
| **What it is** | Half the bid-ask spread; the cost of one market order executed at the best available price |
| **Formula** | (Ask − Mid) or (Mid − Bid) = one half the spread |
| **Example (5¢ spread)** | Buy at $100.05 instead of $100.025 mid-price (2.5 cents per share) |
| **Typical magnitude** | 0.5–20+ basis points, depending on security liquidity |
| **Round-trip cost** | Two half-spreads (buy then sell) = one full spread |
| **Who incurs it** | Every trader using market orders; avoidable only with limit orders or off-market trades |

</aside>

## Definition and mechanics

The [bid-ask-spread](/bid-ask-spread/) is the difference between the highest price a buyer will pay (the bid) and the lowest price a seller will accept (the ask). For Apple stock, the spread might be $150.10 bid to $150.11 ask, a 1-cent spread. The mid-price (also called fair value or mid-quote) is the arithmetic average: $150.105.

When you place a [market-order](/market-order/) to buy, you execute at the ask: $150.11. You pay 0.5 cents more than the mid-price — a cost of half the spread. When you sell via market order, you execute at the bid: $150.10, receiving 0.5 cents less than mid-price.

This half-cent on a $150 stock is roughly 0.33 basis points — nearly invisible. But on a thinly traded stock with a 50-cent spread, half-spread cost is 25 basis points or more, a meaningful drag on returns.

## Why the spread exists

The spread compensates [market-maker-trading](/market-maker-trading/) firms and individual market makers for holding inventory and managing risk. A market maker buys from sellers and sells to buyers, holding a temporary position that exposes them to price moves. If a market maker buys 1,000 shares at $150.10 and the price falls to $149.90 within seconds, they lose $200 on that 1,000-share block. The spread is their compensation for this inventory and timing risk.

The width of the spread reflects:

**Competition** — More market makers competing for order flow means tighter spreads. Apple has dozens of market makers; a microcap stock might have one. Tighter spreads reduce half-spread cost for traders.

**Volatility** — More volatile stocks have wider spreads because market makers need larger cushion. A stock swinging 5% per day merits a wider spread than a stable utility.

**Trading volume** — Higher trading volume allows market makers to rotate inventory faster, reducing their risk holding period. Liquid stocks have narrower spreads.

**Information asymmetry** — If a market maker fears a trader knows something they don't, they widen the spread. Adverse selection widens spreads; this is why spreads widen after earnings announcements.

## Half-spread cost versus full trading cost

A trader's total cost is not simply the half-spread. A [market-order](/market-order/) that buys then later sells incurs two half-spreads (one full spread). But the trader also bears [market-impact](/implicit-trading-costs/) cost if the order is large, and timing cost if the trade is delayed.

For a retail trader buying 100 shares of Apple (half a million cents notional), half-spread cost is $33. Invisible, but real.

For an institution buying 1 million shares, half-spread cost is a negligible baseline. The dominant cost is market impact — the price move caused by bidding up the market with a large order. Market impact can easily eclipse half-spread cost by 10-to-1 for large orders.

This is why institutional traders obsess over execution quality and use algorithms: they are trying to minimize market impact, which dwarfs the spread cost they pay. Retail traders, transacting in small sizes, face opposite economics: market impact is zero (no one notices their order), so half-spread cost is their main invisible drag.

## How spreads vary across markets

**Equities (US large-cap)** — Spreads as tight as 1 cent ($0.01) or even a fraction of a cent (sub-penny) for mega-cap stocks. Half-spread cost < 1 basis point.

**Equities (US small-cap)** — Spreads of 5–50 cents typical. Half-spread cost 5–50+ basis points.

**Bonds** — Not quoted in spreads; instead transacted over-the-counter with dealer markups. Effective spreads equivalent to 10–100+ basis points depending on liquidity.

**Options** — Spreads typically 5–50 cents depending on moneyness and time to [expiration-date](/expiration-date/). Half-spread cost 5–30 basis points.

**Futures** — Tight spreads (1 tick = $12.50 on ES, the S&P 500 e-mini contract). Half-spread cost < 1 basis point.

**Crypto** — [Cryptocurrency-exchange](/cryptocurrency-exchange/) spreads vary widely; 0.1–1% spreads common on smaller exchanges, tighter on larger ones.

## How traders minimize half-spread cost

**Limit orders** — The most direct method. By placing a [limit-order](/limit-order/) at the best bid (if selling) or best ask (if buying), you pay zero spread cost if the market moves to your price. The tradeoff: your order may not fill.

**Trade during high-volume hours** — Spreads tighten during market open and lunch hour when volume surges and competition intensifies. A trader can reduce half-spread cost 20–50% by executing during peak hours instead of in the final hour of the day when liquidity dries up.

**Use patient algorithms** — For large orders, [algorithmic-trading](/algorithmic-trading/) systems break the trade into smaller pieces and execute over time, allowing execution at better average prices.

**Dark pools** — [Alternative-trading-system](/alternative-trading-system/) venues such as dark pools can execute large blocks at the mid-price if they find a crossing partner, eliminating half-spread cost entirely. Drawback: lower certainty of execution.

**Improve settlement and infrastructure** — Institutions with multiple execution venues can use smart order routing to find the best available price, shaving basis points from half-spread cost.

## Half-spread cost as a benchmark for trading skill

For professionals, half-spread cost is a baseline. A skilled trader tries to beat it by executing limit orders that get filled, or by finding off-market crossings through dark pools. An unskilled trader might pay the full spread (two half-spreads on round-trip trades) by using market orders carelessly.

The expression "beating the spread" means executing at a better price than the current mid-market quote — a form of alpha generation through execution excellence, not market insight.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask-spread](/bid-ask-spread/) — the full spread, whose half comprises this cost
- [Implicit-trading-costs](/implicit-trading-costs/) — the broader hidden costs of trading, of which half-spread is a component
- [Explicit-trading-costs](/explicit-trading-costs/) — commissions and fees, now often zero but historically larger than half-spread cost
- [Market-order](/market-order/) — the trade type that incurs half-spread cost immediately
- [Limit-order](/limit-order/) — the alternative order type that avoids half-spread cost

### Wider context

- [Market-maker-trading](/market-maker-trading/) — the liquidity providers who receive half-spread profit
- [Alternative-trading-system](/alternative-trading-system/) — venues where large orders can cross at mid-price
- [Liquidity-risk](/liquidity-risk/) — the broader framework for understanding trading friction
- [Price-discovery](/price-discovery/) — how orders and spreads aggregate information
- [Algorithmic-trading](/algorithmic-trading/) — execution methods designed to minimize implicit costs

</div>

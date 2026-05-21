---
title: "Market order"
description: "A market order is an instruction to buy or sell a security immediately at whatever price the market is currently offering. The fastest way to execute, but the price you actually pay can slip away from the quoted price in fast-moving markets."
keywords:
  - market order
  - execution
  - immediate
  - instant execution
  - order types
image: "/svg/trading.svg"
---

*A **market order** is an instruction to buy or sell a security as fast as possible, at whatever price the market is currently willing to offer. You sacrifice control over price in exchange for certainty of execution and speed. It is the quickest way in or out of a position, but in volatile markets or illiquid securities, the price you actually receive can be meaningfully worse than the price you saw on screen.*

<div class="wiki-hatnote">

For deliberate control over price, see [limit order](/limit-order/). For a hybrid approach, see [stop-limit order](/stop-limit-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market order — key facts</div>

<img src="/svg/trading.svg" alt="A trading terminal showing a market order execution" />

<div class="wiki-infobox-caption">Market orders execute instantly at the best available price, accepting whatever the market offers.</div>

|   |   |
|---|---|
| **What it is** | An instruction to trade at best available price now |
| **Speed** | Immediate (typically sub-second) |
| **Price certainty** | None; you get whatever the market offers |
| **Cost in liquid markets** | Negligible slippage |
| **Cost in illiquid markets** | Can be severe (pennies to dollars per share) |
| **Best for** | Urgent exits, liquid securities, acceptable worst-case price |
| **Worst for** | Large orders in thin markets, size-sensitive execution |
| **Fills** | Partial fills possible if liquidity scattered across multiple price levels |

</aside>

## How a market order executes

When you place a market order, your [broker](/broker/) immediately routes it to the [stock exchange](/stock-exchange/) or market-maker for execution. The order matches against whatever liquidity is available at the best prices — starting with the bid (for a sale) or the ask (for a purchase).

For highly liquid securities like the largest [stocks](/stock/) or [ETFs](/etf/), this takes milliseconds and the price you get is almost exactly what you saw on screen. The [market maker](/market-maker-trading/) or exchange quotes a bid and ask; your market order hits one of them instantly.

For less liquid securities — smaller-cap stocks, certain [bonds](/bond/), options, or thinly traded futures — there may be a much wider gap between bid and ask. Your market order will fill at the ask (if buying) or bid (if selling), and you will face **slippage**: a gap between the price you expected and the price you actually received. In extreme cases — a pre-market trade in a low-volume stock, or a large order hitting a thin order book — slippage can eat several percentage points of the trade's value.

## Speed vs. price precision

The fundamental trade-off in market orders is speed for price precision. You win on speed; you lose on price.

**When a market order makes sense:**

- You need to **exit a position immediately** — the stock is about to be halted, news is breaking, or [circuit breakers](/circuit-breaker/) are firing.
- The security is **highly liquid** (say, a large-cap stock or popular ETF) and slippage is measured in cents.
- You are day-trading or [scalping](/scalping/), and the cost of delay (price moving against you, missing the move entirely) far exceeds the cost of slippage.
- You are **small size**, so you move to the front of the queue without waiting for liquidity.

**When it makes no sense:**

- You are trading a **large block** that will move the market against you. Use an [algorithmic order](/algorithmic-trading/) or dark-pool route instead.
- The security is **illiquid** or thinly traded. A [limit order](/limit-order/) or [VWAP order](/vwap-order/) is safer.
- You have **time** and are willing to wait for a better price. A [limit order](/limit-order/) costs nothing to place and can sit waiting for hours or days.

## Partial fills and order routing

A market order can fill in multiple pieces. Suppose you place a market order to buy 1,000 shares of a stock, but only 600 shares are available at the best ask. The first 600 will fill immediately; the remaining 400 may fill at the next price level up (higher), or a few hundred at that level and the rest at yet another level.

If your [broker](/broker/) routes your order to multiple venues (a [smart order router](/smart-order-router/)), the algorithm will execute across the best available prices at multiple [exchanges](/stock-exchange/). This is good for you on average — you avoid getting stuck in the worst liquidity pocket — but it means your effective execution price is a weighted average across all the prices you hit.

## Slippage in fast markets

In volatile markets — large [dividend](/dividend/) ex-dates, [earnings announcements](/earnings-per-share/), or broader [circuit breaker](/circuit-breaker/) events — bid-ask spreads widen and liquidity evaporates. A market order placed at 10:30 a.m. in a quiet market (where the spread is 1 cent) can hit a 50-cent spread by 11 a.m. if the market is in upheaval.

The larger the order, the worse this becomes. Professional traders limit market order size to what they know will fill in a single liquidity tier, and use [algorithmic execution](/algorithmic-trading/) or patient [limit orders](/limit-order/) for larger block trades.

## Market orders in derivatives

In [options](/option/) and futures markets, market orders are riskier still. These instruments are far less liquid than equities; bid-ask spreads are measured in pennies and dollars, not cents. A single market order can push you deep into the order book, hitting prices that are 5–10% worse than the quoted bid or ask.

Options traders routinely use [limit orders](/limit-order/) instead, even at the cost of a risk that the order never fills. The cost of a bad fill (slippage) is often worse than the cost of no fill at all (missing the trade).

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — trade only at a price you specify
- [Stop order](/stop-order/) — enter or exit at a threshold price
- [Stop-limit order](/stop-limit-order/) — stop-triggered limit order
- Bid-ask spread — the gap between buying and selling prices
- Order types — taxonomy of all order variants

### Execution and routing

- [Smart order router](/smart-order-router/) — algorithm to find best prices across venues
- [Best execution](/best-execution/) — regulatory requirement to get you the best price
- [Market maker](/market-maker-trading/) — the counterparty to your market order
- [Lit venue](/lit-venue/) — public exchange where orders are visible
- [Dark pool](/dark-pool/) — private venue where large orders hide

### Context

- Slippage — the gap between expected and actual price
- Liquidity — the ease with which you can trade
- Volatility — price movement; wider spreads in volatile times
- [Stock exchange](/stock-exchange/) — where most market orders land

</div>

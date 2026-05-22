---
title: "Pegged Order (Exchange)"
description: "Order price automatically tracks bid-ask spread, moving in tandem with market quotes."
keywords:
  - pegged order
  - order types
  - bid ask tracking
  - exchange trading
  - limit order
  - dynamic pricing
---

*A **pegged order** is a limit order whose price automatically adjusts as the market's [bid-ask spread](/wiki/bid-ask-spread/) shifts. If you peg a buy order to the midpoint, it moves up and down with the market in real time, never trading stale, but also never guaranteed to fill.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Base Price** | Bid, ask, or midpoint (user chooses) |
| **Adjustment** | Moves tick-for-tick with market quote |
| **Execution** | Only if market swings through peg level |
| **Best For** | Reducing [market impact](/wiki/market-impact-cost/) in large orders |
| **Risk** | Never fills if market moves away; slippery in volatile markets |
| **Exchange Support** | NASDAQ, NYSE, many ECNs |
| **Variant** | Midpoint peg (Reg SHO); offset peg |

</aside>

## How a pegged order stays current

A pegged order is a [limit order](/wiki/limit-order/) with a moving target. Instead of saying "buy at $50.00," you say "buy at the current midpoint" or "buy at the current bid." As the stock's market quote ticks, your order price ticks with it.

**Example sequence:**
- Market is 100.05 bid / 100.10 ask. Midpoint = 100.075.
- You submit a pegged buy order: "buy at midpoint."
- Your order instantly becomes a limit buy at 100.075.
- Stock ticks: 100.06 bid / 100.11 ask. Midpoint = 100.085.
- Your order automatically reprices to 100.085.
- This repeats every quote update, keeping your order always at the peg level.

The exchange's matching engine manages the repricing; you don't manually adjust.

## Why traders use pegged orders

The appeal is **immediacy without market impact**. A large buyer who posts a [market order](/wiki/market-order/) for 50,000 shares may trigger a wall of sells that move the stock down, resulting in bad [execution](/wiki/best-execution/). A pegged limit order sits at a competitive price — the midpoint or the bid — without pushing the market against you.

Alternatively, a pegged order lets you "work" a large order gradually. Instead of one hit, you post 5,000 shares on a peg and let it fill as the stock moves through your price. If the market rallies, you eventually get hit. If it falls, you follow the bid down and don't overpay.

## Midpoint peg under Reg SHO

The most common variant is the **midpoint peg**, which became popular after [Regulation SHO](/wiki/regulation-sho/) encouraged it. A midpoint-pegged buy order sits between the bid and ask, never trading "inside the spread" (which would be illegal in some contexts). This mechanism:

- **Reduces market impact**: You're not aggressively hitting the ask or undercutting the bid.
- **Fills gradually**: Your order only executes if the market moves through the midpoint.
- **Protects the [bid-ask spread](/wiki/bid-ask-spread/)**: [Market makers](/wiki/market-makers/) still earn their spread; you don't cut it.

This made midpoint pegs popular with large institutional traders and [algorithmic traders](/wiki/algorithmic-trading/) executing block orders over minutes or hours.

## Variants: offset pegs and trailing pegs

**Offset peg:** Instead of pegging to the exact bid/ask/midpoint, you offset by a number of cents. "Buy at midpoint + 0.5 cents" means your order is always half a cent above the true midpoint, improving your odds of filling but not eliminating slippage if the market falls.

**Trailing peg:** Some order types let you "trail" the peg — your order follows the bid up, but if the bid falls, your order doesn't follow down. This caps your risk: you won't chase a falling market forever.

## When pegged orders fail to fill

The chief risk: **no fill if the market doesn't move.** If you peg a buy order to the midpoint and the stock stays flat, your order never trades because it's always at a price no one is hitting. You're left with a "ghost" order that does nothing, wasting time.

Volatile markets are friendlier to pegs — constant quote updates mean constant repricing and occasional fills. Thin stocks or quiet hours may see pegged orders sit untouched for hours. A trader who expects a 50% fill rate on a pegged order and gets 20% is disappointed.

## Execution quality and ["best execution"](/wiki/best-execution/)

Brokers are obligated to route orders to venues offering the best execution. A pegged order doesn't sidestep that. The broker must still match your limit to the best available bid/ask at the exchange where you route the order. If you use a pegged order on a slow trading venue, you may fill worse than if you'd sent a market order to a busy one.

Institutional traders often compare pegged-order performance on NYSE vs. NASDAQ; the higher volume on NASDAQ may result in more frequent repricing and better fills, despite different [market maker](/wiki/market-maker-trading/) structures.

## Comparison to other smart order types

- **[Limit order](/wiki/limit-order/)**: Static price; you're responsible for management. Simpler but requires vigilance.
- **[Stop order](/wiki/stop-order/)**: Triggers a market order once a threshold is breached. Reactive, not proactive price-tracking.
- **[Pegged order](/wiki/pegged-order-exchange/)**: Dynamic; follows the market passively. No interaction needed after submission.
- **[Algorithmic execution](/wiki/algorithmic-execution-benchmark/)**: Advanced micro-execution using time-weighted average price (TWAP) or volume-weighted average price (VWAP). More sophisticated than pegging.

Pegged orders are the middle ground — smarter than static limits, simpler than full algorithms.

## When not to use a pegged order

- **Fast-moving markets:** If the stock is gapping, repricing won't help; you need a market order or be ready to adjust manually.
- **Illiquid securities:** Sparse quotes mean infrequent repricing; your order may not fill.
- **Very large orders:** For 500,000+ shares, an institutional algo (TWAP, VWAP, [implementation shortfall](/wiki/implementation-shortfall/)) often outperforms simple pegging.
- **Overnight gaps:** If you peg a buy order to the midpoint and the market opens down 5%, your order is stuck waiting for the midpoint to fall — you don't get the gap.

<div class="wiki-seealso">

### Closely related
- [Limit Order](/wiki/limit-order/) — Static-price relative; manual adjustments
- [Stop Order](/wiki/stop-order/) — Triggers execution once threshold is hit
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — Foundation of peg pricing
- [Best Execution](/wiki/best-execution/) — Broker obligation in order routing
- [Market Maker](/wiki/market-maker-trading/) — Beneficiary of stable spreads with pegged orders

### Wider context
- [Order Types](/wiki/order-types/) — Full spectrum of order instructions
- [Algorithmic Trading](/wiki/algorithmic-trading/) — More advanced order execution
- [Regulation SHO](/wiki/regulation-sho/) — Regulatory context for midpoint pegs
- [Execution Quality](/wiki/execution-quality-analysis/) — Measuring order performance
- [Market Impact](/wiki/market-impact-cost/) — Cost that pegged orders help minimize

</div>

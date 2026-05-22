---
title: "Calendar Spread (Commodity)"
description: "Paired trade exploiting differences between contract months in commodity futures."
keywords:
  - calendar spread
  - commodity futures
  - term structure
  - spread trading
---

*A **calendar spread** in commodities is a paired trade buying one [futures contract](/wiki/futures-contract/) month while selling another, typically to profit from changes in the [term structure](/wiki/commodity-term-structure/) or the relative [basis](/wiki/basis/) between months. It captures the premium or discount one contract month trades relative to an adjacent month, exploiting [contango](/wiki/contango/) or [backwardation](/wiki/backwardation/) dynamics.*

<div class="wiki-hatnote">
Also called a "time spread," "straddle," or "curve trade" depending on context and the months involved.
</div>

<aside class="wiki-infobox">

| Feature | Detail |
|---|---|
| Structure | Long one month, short another (usually adjacent) |
| Common pair | Buy front month, sell back month (or vice versa) |
| Profit source | Convergence of contracts as time passes |
| Risk | Curve steepening (if front-weighted) or flattening (if back-weighted) |
| Capital required | Lower than outright long or short (offsetting positions) |
| Common commodities | Oil, natural gas, grains, metals |
| Time horizon | Days to months |

</aside>

## How calendar spreads work: the term-structure thesis

A commodity's [forward curve](/wiki/forward-yield-curve/) plots prices for different delivery months. In [contango](/wiki/contango-backwardation-impact/), the curve slopes upward: March crude oil trades higher than February, April higher than March, etc. In [backwardation](/wiki/backwardation/), the curve slopes downward: January gold trades higher than February, February higher than March.

A calendar spread exploits the fact that contracts will converge over time. Consider crude oil: February 2024 contracts trade at $80/barrel, while March 2024 trades at $82/barrel (a $2 contango spread). A trader buys March and shorts February. If both prices stay proportionally the same, the spread converges to zero as February approaches expiry and merges with spot. The trader profits on the convergence.

Alternatively, the trader can exploit curve steepening or flattening. If the trader believes the curve will flatten (back months falling relative to front months), he shorts the back month (March) and longs the front month (February). If the curve flattens as expected, the spread compresses and the trader profits.

## The contango arbitrage case

In commodity markets, [contango](/wiki/contango/) often exists because of [storage costs](/wiki/commodity-storage-costs/). A barrel of crude stored for a month costs roughly $0.30–$0.50 in carrying costs (tank space, insurance, financing). So March crude should trade about $0.30–$0.50 higher than February to compensate the storage operator for the carrying cost.

If the spread widens beyond the carrying cost (say, March is $3 higher), a profitable arbitrage emerges. A trader can buy February crude, store it, and sell it as March crude (or sell March futures and hold the physical), locking in the excess $2.50 spread minus carrying costs. This is a self-liquidating trade: the physical flows logically from February to March delivery.

The calendar spread captures this arbitrage without requiring actual physical storage. A trader buys March futures and sells February futures. As time passes, February contracts approach expiry and converge with spot; March contracts mature toward the March delivery date. If the contango is in excess of carrying costs, the spread compresses and the trader profits.

## The backwardation case and supply stress

When commodities are in tight supply ([backwardation](/wiki/backwardation-definition/)), the curve inverts. Near-month contracts trade higher than forward months. This signals scarcity: spot supply is valued more than future supply.

Calendar spreads in backwardation are short-front, long-back. The trader sells the expensive near month and buys the cheaper forward month. If the curve normalizes (supply relief occurs, spot prices fall), the spread widens and the trader profits.

During the 2022 energy crisis (Russian supply disruptions), crude and natural gas exhibited severe backwardation. Front-month contracts traded at substantial premiums. Traders who shorted front-month and long-back-month benefited as the curve eventually normalized.

## Curve flattening and steepening strategies

Traders can take explicit views on curve shape. If the trader believes the curve is too steep (far months are overpriced relative to spot), he shorts back months and longs front months. If the curve is too flat and a resteepening is expected, he does the opposite.

[Curve flattening](/wiki/curve-flattening/) strategies work by selling longer-dated contracts and buying shorter-dated ones. For example, in oil: sell May, buy March. As the curve flattens, May prices fall relative to March, and the spread compresses.

[Curve steepening](/wiki/curve-steepening-commodity/) strategies do the reverse: buy back months, sell front months. This is a bet that the curve will slope upward, widening the spread between front and back.

The optimal calendar spread depends on the trader's view of curve dynamics. If economic growth is expected (boosting near-term demand), the trader might flatten the curve (buy spot, sell forward). If a supply disruption is expected to ease, the trader might steepen (sell spot, buy forward on speculation that future supply will be abundant).

## Multi-leg spreads and complex curve trades

Professional traders don't limit themselves to two-leg spreads. A ["butterfly" or "condor"](/wiki/butterfly-spread/) spread might buy March, sell June (short two contracts), and buy September. This isolates different parts of the curve: the March-June leg captures near-term dynamics; the June-September leg captures longer-term dynamics.

These multi-leg trades are especially common for widely traded commodities with many contract months (crude oil, natural gas, grains). A trader might have strong views on the near-term curve shape but be neutral on the long-term curve, justifying a focused spread that profits from near-term convergence while hedging long-term risk.

## Risks and convergence timing

The main risk in calendar spreads is that the curve doesn't converge as expected. If the trader is long March and short February, but a supply disruption occurs in February, the front month can rally sharply while the back month lags. The spread widens against the trader.

Additionally, commodity [term structure](/wiki/commodity-term-structure/) changes can surprise. A trader shorting contango in normal times can be hit hard if backwardation suddenly emerges (supply shock) or if the curve inverts unexpectedly.

Timing is also critical. The convergence between contracts happens automatically, but the *speed* of convergence and any interim price moves create slippage. A trader might be profitable on a long-term basis but hit a margin call or stop-loss during interim adverse moves.

Finally, basis risk exists. The trader assumes that both contract months move in lockstep to underlying spot prices. But if one month becomes illiquid (say, the back month has minimal open interest), it may not track the underlying commodity precisely, introducing basis risk.

## Calendar spreads as synthetic betting tools

Calendar spreads can approximate synthetic positions. A long-front/short-back spread is roughly like being long the commodity (you profit if near-term prices strengthen). A short-front/long-back is like being short.

However, they require much less [margin](/wiki/forex-margin/) than outright long or short positions because the two legs are offsetting. A trader with limited capital can express curve views efficiently using calendar spreads.

Sophisticated traders also use calendar spreads for [arbitrage](/wiki/arbitrage-defi/) against [physical commodity](/wiki/commodity-price-hedging/) holdings. A producer with physical inventory can hedge it by selling front-month futures and buying back-month futures, locking in the curve and storage costs. A processor (like a refinery) can use calendar spreads to hedge processing margins: long crude oil back month (future feedstock) while shorting refined-product back months (future output).

<div class="wiki-seealso">

### Closely related
- [Contango](/wiki/contango/) — Upward-sloping term structure favoring calendar spreads
- [Backwardation](/wiki/backwardation/) — Inverted term structure; different spread mechanics
- [Commodity Term Structure](/wiki/commodity-term-structure/) — The curve being traded
- [Futures Contract](/wiki/futures-contract/) — The underlying instruments

### Wider context
- [Commodity Storage Costs](/wiki/commodity-storage-costs/) — Fundamental driver of contango
- [Basis](/wiki/basis/) — Relationship between spot and forward prices
- [Spread Trading Futures](/wiki/spread-trading-futures/) — Broader context
- [Commodity Hedging](/wiki/commodity-price-hedging/) — Industrial use of spreads

</div>

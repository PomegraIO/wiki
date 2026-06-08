---
title: "Tick Size and Its Effect on Trading"
description: "How minimum tick increments affect bid-ask spreads, liquidity, and market efficiency. Tick size varies by price and security type."
keywords:
  - tick size effect on trading
  - minimum price increment
  - bid-ask spread
  - market microstructure
  - price discretization
image: /svg/markets.svg
---

*A **tick size** is the smallest price increment at which a security can trade—the granularity of the price ladder. It sounds technical, but it shapes spreads, profitability for market makers, and how easily you can buy or sell. The tick size effect on trading cuts both ways: tighter ticks mean finer price discovery but can widen spreads; wider ticks simplify trading but leave gaps in execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tick Size — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for financial markets." />

<div class="wiki-infobox-caption">The smallest price movement in a market determines bid-ask structure and liquidity flow.</div>

|   |   |
|---|---|
| **Definition** | Minimum allowable price change between consecutive trades |
| **U.S. stocks** | $0.01 (1 cent) for most shares; $0.05 for some low-priced stocks |
| **Bonds** | Often 1/32 of a point (0.03125); treasury bills trade in basis points |
| **Foreign exchange** | Pips vary by currency pair (typically 0.0001 for major pairs) |
| **Effect on spreads** | Narrower tick → tighter spreads but lower market-maker profit margin |
| **Wider tick example** | $0.05 increments force larger minimum spreads, reduce competition |
| **Key trade-off** | Precision vs. liquidity provision incentives |

</aside>

## What tick size actually controls

A tick is not an opinion—it's a rule baked into the market. On the Nasdaq or NYSE, a stock trading at $50 can next move to $50.01 or $49.99, but not $50.003. That discrete jump is the tick. In foreign exchange, the EUR/USD might jump from 1.0850 to 1.0851 (a pip), but never 1.08505.

The granularity matters because it determines the smallest profit a market maker can claim. If you bid $50.00 and a market maker offers $50.01, they've pocketed $0.01 per share—the spread. If the tick were $0.05, the offer would be $50.05, and they'd earn five times as much per transaction. Conversely, a tighter tick means more possible price levels and theoretically sharper competition, but it also means thinner margins for the dealers standing ready to trade.

Tick sizes are not uniform across markets. The U.S. SEC has tweaked them repeatedly. Most liquid stocks trade in one-penny increments. Very low-priced stocks (under $1) often trade in $0.05 ticks. Corporate bonds, barely liquid, trade in 1/32-point increments. Forex uses pips. Futures on crude oil use quarter-cent increments. Every market has its own logic.

## Why regulators and markets choose different tick sizes

The choice of tick size is a tension between two forces that pull in opposite directions.

**In favor of wider ticks:** A wider tick means a wider forced spread. If you're a market maker, you face less competition at each price level. A dealer who posts a quote gets a guaranteed profit floor—the bid-ask gap. Wider ticks protect dealers' margins, make market-making profitable, and encourage more dealers to show up. With more competing market makers, you get better execution because even though the spread is bigger, there's ample liquidity at that spread.

**In favor of narrower ticks:** Tighter ticks allow price discovery to happen at finer resolution. Buyers and sellers get closer to a true equilibrium price. Narrower spreads cost the buyer or seller less per transaction. More price levels mean more potential "hang-out spots" for orders—the order book becomes more granular, and traders can find more nuanced execution prices. Especially in high-frequency trading and active stocks, narrower ticks promote algorithm-friendly continuous competition.

The U.S. regulatory debate has swung both directions. In 2001, the SEC mandated decimalization (moving from fractions to ticks of $0.01), celebrating finer price discovery and lower spreads. But in 2010, amid concerns about market fragmentation and low market-maker profitability, the SEC imposed a $0.05 minimum tick on small-cap stocks and ran pilots allowing $0.05 ticks on larger issues. The evidence was mixed: spreads widened, but so did quoted depth, and trading volume fell on wider-tick test stocks.

The finding that tick size affects not just spreads but also participation echoes across asset classes. Wider ticks in certain corporate bonds correlate with fewer trades but less frequent microprice-levels. Forex dealers tolerate tiny pips (0.0001 for EUR/USD) only because volumes are so vast that thin margins still yield profit at scale.

## How tick size influences bid-ask spreads

The bid-ask spread is not purely a function of tick size—volatility, liquidity, and competition matter too. But tick size sets the floor and sometimes the ceiling.

In a one-penny stock market, the minimum spread is $0.01. The mean spread on Apple is often 1–2 cents, but on a penny stock or a thinly-traded security, it can be the minimum tick itself. If you own a stock where no bid-ask width is allowed below $0.01, you cannot get filled in the middle.

On a security with a wider tick, say $0.05, the minimum spread becomes $0.05. Trading one share at that width is inconvenient, but traders moving size will accept it—the cost of a $0.05 spread on a 1,000-share block is $50, which may be worth paying for certainty of execution.

Here is a simplified table:

|   | **Narrow tick (e.g., $0.01)** | **Wide tick (e.g., $0.05)** |
|---|---|---|
| **Minimum spread** | $0.01 | $0.05 |
| **Liquidity incentive for dealers** | Thin margin; many dealers needed to compete | Wider margin; fewer dealers may suffice |
| **Order-book depth** | More price levels; scattered orders | Fewer levels; orders may cluster at round prices |
| **Typical retail spread cost** | Lower per-share cost | Higher per-share cost |

The table oversimplifies—a 1-cent tick stock can still have a 10-cent spread in a crisis, and a 5-cent tick stock might have a 1-cent effective spread if dealers are motivated. But tick size does constrain the minimum and influences the natural resting points where market makers post bids and offers.

## The market-maker perspective: margin and incentives

Market makers earn money on the spread. If your stock has a one-penny tick, the smallest width you can quote is $0.01. If you trade 10,000 shares a day at a $0.01 spread, you make $100. If you trade 10,000 shares a day on a stock with a $0.05 tick, you make $500. Unsurprisingly, market-maker participation tends to be higher when ticks are wider.

Conversely, when ticks are too narrow relative to volatility or order flow, dealers may widen their spreads (post a bid 2–3 ticks away from the offer, creating a gap). Or they may simply leave the market. This is why the SEC observed lower participation in market-making when tick size narrowed across the board.

The technological arms race in market-making—faster execution, lower-latency data feeds—has been partly driven by the need to compete on volume when spreads are thin. A dealer who can execute a 1-cent-wide trade in 10 microseconds can profit if they do it 100,000 times a day. But that requires infrastructure. Smaller dealers or traditional market makers cannot keep pace, so they may exit or specialize in less-liquid, less-competitive securities.

## Historical effect on trading behavior

When the SEC moved to decimal ticks in 2001, spreads fell dramatically. The average bid-ask spread on S&P 500 stocks dropped from 1.4 cents to under 1 cent. Investors celebrated lower execution costs. But market-maker profitability also fell, and the number of registered market makers declined. Within a few years, the rise of electronic trading and algorithm-based execution offset some of the dealer exodus, but the transition was real.

The 2010 pilot program for wider ticks on small-cap stocks produced nuanced results. On test stocks assigned a $0.05 tick, spreads widened by 10–15%, but quoted depth (the number of shares available at the bid and offer) often increased. Trading volume fell, but so did the frequency of tiny price moves that appeared to be algorithmic noise rather than information.

The practical lesson: lowering tick size does not automatically improve trading conditions. It depends on the security's liquidity, volatility, and whether the market can absorb the increase in competitive pressure on dealers. For highly liquid stocks (Apple, Microsoft), a 1-cent tick is fine because volume supports many dealers. For illiquid bonds or low-volume stocks, a wider tick may be necessary to preserve market-making.

## Tick size in different asset classes

**U.S. equities:** Most trades at $0.01. Sub-penny trading (0.001, 0.0001) exists but is restricted to institutions and algorithmic traders. Penny stocks may trade at $0.05 or larger ticks.

**Bonds:** Corporate and government bonds trade in fractions or basis-point increments. Treasury bonds use 1/32 of a point; this wide tick reflects lower dealer participation and less competition than stocks.

**Forex:** Major currency pairs (EUR/USD, GBP/USD) trade at pips of 0.0001. Exotic pairs may use wider increments. The massive scale of forex volume allows tight ticks.

**Futures:** Commodity and equity index futures have tick increments set by the exchange. Crude oil is often 0.01 cents per barrel; the S&P 500 e-mini futures tick is $12.50 (0.25 index points).

Each asset class reflects its own balance between liquidity, volatility, and the market structure needed to attract dealers.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the practical cost of trading created by tick size constraints
- [Market Maker Trading](/market-maker-trading/) — how dealers profit from tick increments and spread capture
- [Market Microstructure](/market-microstructure/) — the mechanics of order flow and price formation
- [Limit Order](/limit-order/) — how traders use price levels determined by ticks
- [Fragmented Market](/fragmented-market/) — how multiple venues with the same tick can segment execution

### Wider context

- [Stock Exchange](/stock-exchange/) — how venues set and enforce trading rules including ticks
- [Price Discovery](/price-discovery/) — how tick size affects the efficiency of price formation
- [Algorithmic Trading](/algorithmic-trading/) — how tight ticks enable rapid execution strategies
- [Nasdaq](/nasdaq/) — a major venue with decimal tick structure

</div>

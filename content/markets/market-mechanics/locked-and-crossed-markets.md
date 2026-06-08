---
title: "Locked and Crossed Markets"
description: "Market states where bid prices equal or exceed ask prices across trading venues, creating arbitrage opportunities and breaching the no-trade-through principle."
keywords:
  - locked market
  - crossed market
  - bid-ask inversion
  - reg nms
  - trade-through
  - market fragmentation
image: "/svg/markets.svg"
---

*A **locked market** occurs when the best bid price (what buyers will pay) equals the best ask price (what sellers will take) across different venues, eliminating the [bid-ask spread](/bid-ask-spread/). A **crossed market** is the more extreme condition where the best bid *exceeds* the best ask—an impossible state that should trigger immediate buying at the lower ask and selling at the higher bid. Both conditions expose latencies in price dissemination and fragmentation across [stock exchanges](/stock-exchange/), creating arbitrage opportunities and complicating [price discovery](/price-discovery/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Locked and Crossed Markets — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure and mechanics." />

<div class="wiki-infobox-caption">Pricing anomalies that expose latency and fragmentation; locked and crossed markets violate the principle of unified price discovery.</div>

|   |   |
|---|---|
| **What it is** | Best bid ≥ best ask across venues; bid > ask in a crossed market |
| **Root cause** | Latency in quote dissemination; market fragmentation across exchanges |
| **Market state** | Locked: bid = ask; Crossed: bid > ask |
| **Duration** | Milliseconds to seconds; typically resolved by [market makers](/market-maker-trading/) or arbitrageurs |
| **Regulatory response** | Regulation NMS requires [trade-through protection](/trade-through-protection/); exchanges must prevent execution at inferior prices |
| **Opportunity** | Riskless arbitrage: buy at ask, sell at bid |

</aside>

## The problem of fragmented venues

Before [electronic trading](/stock-exchange/) and market fragmentation, a single [stock exchange](/stock-exchange/)—say, the [NYSE](/new-york-stock-exchange/)—held a monopoly on a company's listed securities. Everyone who traded that stock used the same venue, saw the same [bid-ask spread](/bid-ask-spread/), and executed at the same queue. Price discovery was unified.

Beginning in the 1990s and accelerating through the 2000s, that unity fractured. [SEC](/securities-and-exchange-commission/) rules allowed new exchanges ([NASDAQ](/nasdaq/), regional exchanges, ECNs, and [alternative trading systems](/alternative-trading-system/)) to list the same securities. Now Company X's stock trades on NYSE, NASDAQ, CBOE, [ARCA](/alternative-trading-system/), and dozens of smaller venues simultaneously. Each venue has its own [market makers](/market-maker-trading/), its own order flow, and its own refresh rate for posting bid and ask prices.

This fragmentation created a new problem: because price data from all venues is transmitted over networks with slightly different latencies, an observer—or worse, a trader—might see contradictory prices at the same instant. Venue A might show a bid of $100.00, while Venue B (unknown to the observer at that microsecond) has an ask of $99.99. That observer could legally place a buy order at Venue A's asking price of, say, $100.02, entirely unaware that they could have bought at $99.99 just across the network. The result: a market state that appears locked or crossed.

## Locked markets: bid equals ask

In a locked market, the national best bid (NBB) from one venue equals the national best ask (NBA) from another. For example:

- Venue A quotes: bid $50.00, ask $50.05
- Venue B quotes: bid $49.95, ask $50.00

The NBB is $50.00 (from Venue A); the NBA is $50.00 (from Venue B). The spread is zero—locked. 

Locked markets persist for seconds or minutes when one venue's [price discovery](/price-discovery/) lags behind another's. If Venue A sees fresh selling, it might drop its ask from $50.10 to $50.00. But Venue B's quote, still in transmission or briefly stale, shows $50.00 / $50.05. The network reflects a lock.

From a trader standpoint, a locked market offers no [spread](/bid-ask-spread/) for profit. If you buy at the ask of $50.00 and immediately sell at the bid of $50.00, you break even (ignoring fees and latency). [Market makers](/market-maker-trading/) hate locked markets because they imply no edge. They typically widen quotes to unlock the market: Venue B might adjust to $49.95 / $50.05 to create daylight between itself and Venue A. That widening restores the spread and removes the temptation to arbitrage.

## Crossed markets: bid exceeds ask

A crossed market is a more jarring condition: the best bid from one venue exceeds the best ask from another. Example:

- Venue A (trading desk sees): bid $50.02, ask $50.10
- Venue B (trading desk sees): bid $49.95, ask $50.00

The NBB is $50.02; the NBA is $50.00. The bid is *higher* than the ask. This is not just a zero spread; it's an inverted spread, an arbitrage opportunity, and a violation of basic market logic.

In theory, a crossed market should last only milliseconds. Any observer seeing this state can immediately buy at the NBA ($50.00) and sell at the NBB ($50.02), pocketing $0.02 per share with zero risk. The flood of such arbitrage should instantly widen Venue A's ask or narrow Venue B's bid, uncrossing the market. But latency is real. That $0.02 profit, multiplied by a billion shares, can tempt flash trades and HFT (high-frequency trading) strategies.

More importantly, a crossed market signals that at least one venue is quoting stale or erroneous prices. If Venue B's $50.00 ask is from 3 seconds ago, and the true market has moved to $50.10, then Venue B's quote is a trap for the unwary. Buyers who execute there are buying at $0.10 below fair value.

## Why locked and crossed markets happen

The root cause is latency in the network that distributes quotes. [SEC](/securities-and-exchange-commission/) [Regulation SHO](/securities-and-exchange-commission/) and [Regulation NMS](/securities-and-exchange-commission/) require all exchanges to broadcast their best bid and ask to the [Securities Information Processor](/securities-and-exchange-commission/) (SIP), a central hub that aggregates them into a "National Best Bid and Offer" (NBBO). But that aggregation takes time—typically tens to hundreds of milliseconds—to reach all traders.

During that window, a trader with a direct connection to Venue A sees Venue A's quote in real-time, while their feed of the NBBO (which includes Venue B) is slightly stale. If Venue A has just dropped its ask, but Venue B's quote (on the NBBO feed) is one or two ticks old, the observer might see Venue B's ask as the current national best—when in fact Venue A is now lower.

In practice, professional traders mitigate latency by running direct connections to as many venues as possible, building their own view of the market rather than relying on the SIP. But the SIP is *the* official NBBO, and the [SEC](/securities-and-exchange-commission/) and exchanges reference it for enforcement and regulation.

## Regulation NMS and trade-through protection

When [Regulation NMS](/securities-and-exchange-commission/) (Reg NMS) took effect in 2007, it introduced [trade-through protection](/trade-through-protection/): a broker may not execute a customer's order at a price worse than the current NBBO. If the NBBO is $50.00 / $50.05 (best bid $50.00 on Venue X, best ask $50.05 on Venue Y), your broker cannot fill your buy order at $50.06 without first attempting to route to Venue Y to get the $50.05 price.

This rule directly addresses locked and crossed markets. It says: if your order would trade through (i.e., buy at a higher ask or sell at a lower bid than the NBBO), the [broker](/broker/) must route to the best-price venue, not execute locally at an inferior price.

The [Order Protection Rule](/securities-and-exchange-commission/) under Reg NMS also allows exchanges to enforce locked or crossed markets. If Venue B is quoting $50.00 / $50.05 while Venue A has $50.02 / $50.00, Venue A must prevent Venue B's quote from trading through its own (crossing the bid-ask). The mechanics vary, but the intent is clear: no trader should pay more than the best available offer, and no seller should receive less than the best available bid.

## Practical impact

For most retail investors and larger institutions, locked and crossed markets are invisible. Brokers route orders to secure the best price automatically, and the latency windows close in milliseconds. But for [high-frequency traders](/algorithmic-trading/) and market makers, these states are bread and butter. A crossed market is a pure arbitrage opportunity; a locked market is a signal to adjust quotes and avoid losses.

Locked and crossed markets also reveal the tension between "fast" (high-frequency, venue-specific) and "fair" (unified, NBBO-compliant) [price discovery](/price-discovery/). The more fragmented the market, the wider the window for stale quotes and the greater the latency cost. Some argue that consolidation would reduce locked and crossed states; others counter that more venues, with more [market makers](/market-maker-trading/), increase [liquidity](/liquidity-risk/) and competition, which is worth the latency cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Trade-Through Protection](/trade-through-protection/) — The Reg NMS rule that prohibits execution at inferior prices when a better price is displayed elsewhere.
- [Price-Time Priority](/price-time-priority/) — The queue logic that determines which orders execute first once prices align.
- [Bid-Ask Spread](/bid-ask-spread/) — The gap between best bid and best ask, which locked markets collapse and crossed markets invert.
- [Market Maker Trading](/market-maker-trading/) — The professionals who quote on multiple venues and profit from spread arbitrage.
- [Circuit Breaker and Trading Halt](/circuit-breaker-trading-halt/) — The automatic pause rule that halts trading when conditions become disorderly.
- [Alternative Trading System](/alternative-trading-system/) — ECNs and other non-exchange venues that fragment the market.
- [Algorithmic Trading](/algorithmic-trading/) — High-speed strategies that exploit latency and locked/crossed states.

### Wider context

- [Stock Exchange](/stock-exchange/) — The venue operators that broadcast quotes and enforce order protection.
- [SEC](/securities-and-exchange-commission/) — The regulator that set Reg NMS and trade-through rules.
- [Price Discovery](/price-discovery/) — The continuous process of finding equilibrium across venues.
- [Market Capitalization](/market-capitalization/) — The value of listed companies, priced in these fragmented markets.
- [Broker](/broker/) — The intermediary that routes orders to comply with Reg NMS.

</div>

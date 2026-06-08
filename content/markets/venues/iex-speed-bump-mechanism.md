---
title: "IEX Speed Bump Mechanism"
description: "How IEX's 350-microsecond delay levels the playing field between algorithmic and human traders by slowing latency arbitrage."
keywords:
  - how iex speed bump works
  - iex exchange mechanism
  - latency arbitrage prevention
  - speed bump 350 microseconds
  - high-frequency trading defense
image: "/svg/markets.svg"
---

*The **IEX speed bump** is an intentional 350-microsecond delay built into the order matching engine that gives ordinary traders a moment to react before high-frequency traders can exploit stale quotes. Unlike other exchanges that tout infinite speed, IEX chose to slow orders slightly—a design choice that reduces latency-driven arbitrage while preserving fair price discovery.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">IEX Speed Bump — how it works</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market venues and structure." />

<div class="wiki-infobox-caption">A 350-microsecond delay shields small traders from being picked off by faster algorithms.</div>

|   |   |
|---|---|
| **Delay duration** | 350 microseconds (0.00035 seconds) |
| **What it protects against** | Flash arbitrage and latency-driven order predation |
| **Venue** | IEX, registered alternative trading system (ATS) |
| **Order flow affected** | All non-routable orders entering the IEX limit order book |
| **Mechanism** | Orders queued, matched, and published to all participants after the delay |
| **Hidden order caveat** | Crumbing (tiny fills) still possible but far harder |
| **Regulatory approval** | SEC-approved innovation in market structure design |

</aside>

## Why IEX introduced the speed bump

High-frequency traders use sophisticated technology—co-located servers, optimized networks, specialized algorithms—to profit from the tiny gaps between what different exchanges publish. When a stock ticks up on the Nasdaq, a fast trader can see the move in microseconds and race to the New York Stock Exchange to buy or sell before the rest of the market reacts. This is latency arbitrage: the traders are not adding information; they are exploiting the delay in how quickly prices propagate across venues.

Traditional investors and algorithms that do not invest in expensive low-latency infrastructure are left behind. They see a price move and decide to act, but by the time their order reaches the exchange, faster traders have already identified the same opportunity and grabbed a better price. The slower trader pays more to buy or receives less to sell—a friction cost that latency arbitrage extracts.

IEX's founder, Brad Katsuyama, observed this dynamic while working as a trader at RBC Capital Markets. Large trades he tried to execute would mysteriously move away, as if invisible hands had seen them coming. After investigation, he discovered high-frequency traders were racing to intercept his orders by routing ahead on other venues. The speed bump was designed as a remedy: by intentionally slowing the match slightly, IEX gives ordinary traders and passive order flow a moment to react or cancel before ultra-fast algorithms can exploit a quote.

## How the speed bump is implemented

The speed bump operates at the core of IEX's order-matching logic. When a trader submits an order—buy or sell—to the IEX limit order book, the order does not match immediately against resting orders. Instead, IEX:

1. **Queues the incoming order** for 350 microseconds.
2. **Continues to accept cancellations and new orders** from other market participants during this window.
3. **Performs the match** once the delay expires, using the final order queue and resting book.
4. **Publishes the execution** and updated book to all participants simultaneously.

This means all market participants—whether they are on IEX or not—receive news of the trade and updated quotes at nearly the same instant. A trader with a slow connection is no more disadvantaged by IEX's delay than by the inherent physics of light traveling across fiber-optic cables.

The speed bump does **not** slow down the core function of price discovery. Instead, it harmonizes the speed at which different participants can act on the same information. Passive orders sitting in the IEX book have 350 microseconds to be repriced, cancelled, or supplemented before they can be hit by a new aggressor.

## Latency arbitrage and the crumbing problem

Before the speed bump, latency arbitrage traders employed a tactic called **crumbing**: buying or selling just a handful of shares at a better price elsewhere, watching to see if the rest of the market would follow, and then executing the bulk of their own trade. This allowed them to scalp a few cents from retail investors or algorithms that were unaware their orders were being broken apart by a faster participant.

The speed bump does not eliminate crumbing entirely, but it makes it far less profitable. A high-frequency trader cannot use a sub-microsecond view of IEX's order flow to run ahead on another exchange and front-run a large order. By the time the trader could exploit the gap, IEX has already matched the orders and published the result.

## Speed bump vs. pure speed advantage

IEX is explicit: it is not the fastest exchange, and it does not advertise to be. Exchanges like Nasdaq and the New York Stock Exchange prioritize sub-microsecond latency for co-located participants, intentionally giving them a speed advantage. IEX explicitly sacrifices that advantage in favor of fairness.

Some traders and exchanges argue that speed bumps distort price discovery—that the fastest traders are responding to genuine supply-and-demand signals, and slowing them down delays information incorporation. IEX's counter-argument is that latency-driven profits are extraction, not discovery. A trader who sees a signal and races to another venue before the original venue knows the price has moved is not revealing new information; they are exploiting the fact that light travels at a finite speed.

## Regulatory context and SEC approval

IEX launched in 2013 as an alternative trading system (ATS) under Regulation SHO and Regulation ATS, which do not prohibit intentional delays. The SEC reviewed IEX's speed bump and approved it as compliant with market structure rules. The exchange later filed to become a registered national securities exchange, and the SEC approved that application in 2016, clearing the way for IEX to list companies.

The speed bump was not novel from a technical perspective—dark pools and crossing networks had employed similar mechanisms. But IEX brought it to a public, regulated venue and made it central to its brand. The regulatory blessing signaled that deliberate latency was a permissible, even desirable, market structure innovation.

## Why not all exchanges adopt a speed bump

Other exchanges have not rushed to adopt speed bumps, despite IEX's success. The reason is partly cultural and partly economic. Nasdaq and NYSE built their business models around co-location and selling premium services to low-latency traders. Advertising sub-microsecond latency is a competitive advantage for their data feeds and order placement services. Introducing a speed bump would anger their most profitable customers.

Additionally, there is a network effect: traders and algorithms optimize their entire systems for the fastest exchange. If every exchange imposed a speed bump, the optimization would flatten. But as long as some exchanges prioritize pure speed, traders must choose between venues—and latency-sensitive traders naturally gravitate to the fastest ones.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative Trading System](/alternative-trading-system/) — the regulatory framework under which IEX operates
- [Market Maker Trading](/market-maker-trading/) — the core function of managing liquidity and spreads
- [Limit Order](/limit-order/) — the type of order sitting in IEX's book awaiting the speed bump
- Latency Arbitrage — the practice IEX's design directly counters
- [Bid-Ask Spread](/bid-ask-spread/) — how speed advantages have traditionally been monetized

### Wider context

- [Stock Exchange](/stock-exchange/) — the broader ecosystem of trading venues
- [Algorithmic Trading](/algorithmic-trading/) — the strategies IEX's design aims to constrain
- [Price Discovery](/price-discovery/) — the central market function affected by speed bump design
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator that approved IEX's structure

</div>

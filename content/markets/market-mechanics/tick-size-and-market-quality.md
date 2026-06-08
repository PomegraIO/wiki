---
title: "Tick Size and Market Quality"
description: "How the minimum price increment for a security influences bid-ask spreads, liquidity provision, and overall trading costs."
keywords:
  - tick size
  - minimum price increment
  - bid-ask spread
  - market quality
  - trading costs
  - price granularity
image: /svg/markets.svg
---

*The **tick size** is the minimum price increment at which a security can trade. For most U.S. equities, this is one cent; for others, it may be five cents or one dollar. Tick size directly influences the [bid-ask spread](/bid-ask-spread/) and the incentives of liquidity providers. A smaller tick size can tighten spreads but may fragment liquidity; a larger tick size widens spreads but can improve market maker profitability. The relationship between tick size and overall market quality—the trade-off between tight pricing and robust liquidity—has been a subject of intense regulatory and academic debate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tick Size and Market Quality — Key Facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Minimum price increments shape how tightly prices can be quoted and how much brokers are willing to facilitate trades.</div>

|   |   |
|---|---|
| **Standard U.S. tick** | $0.01 (one cent) for stocks priced $1 and above |
| **Alternative ticks** | $0.0001 for certain securities; $0.05 or $1.00 for others |
| **Primary tradeoff** | Tighter spreads vs. market maker profitability and depth |
| **Fragmentation risk** | Sub-penny pricing can reduce order consolidation and liquidity |
| **Regulatory body (U.S.)** | SEC oversees tick size rules; self-regulatory organizations enforce |
| **Pilot programs** | SEC has tested larger tick sizes for small-cap and illiquid stocks |

</aside>

## How Tick Size Affects Bid-Ask Spreads

The [bid-ask spread](/bid-ask-spread/) is the difference between the highest price a [market maker](/market-maker-trading/) will pay (bid) and the lowest price at which they will sell (ask). The spread compensates the market maker for inventory risk and the cost of immediacy.

Tick size constrains how finely a market maker can adjust these prices. If the tick is one cent and a market maker wants to widen the spread from 1 cent to 2 cents, they move the ask up by exactly one tick or the bid down by exactly one tick. They cannot split the difference at 0.5 cents.

In a one-cent tick environment, competition between market makers pushes spreads toward one cent on highly liquid securities: if a market maker quotes a 2-cent spread, a competitor can undercut by 1 cent and capture the order flow. The market maker is forced to narrow or lose business.

But suppose the tick size is five cents. A market maker quoting a 5-cent spread faces less competitive pressure: a competitor cannot undercut by just 1 cent. The minimum adjustment is 5 cents, which may not be worth it. As a result, spreads tend to be at least one tick wide, and often wider. A five-cent tick almost guarantees 5-cent spreads even on liquid securities.

Empirically, tighter tick sizes correlate with tighter spreads in the short run. Reducing the tick size from 1 cent to 0.0001 (four decimal places) would allow spreads to compress further. But this creates a second-order problem.

## Tick Size and Liquidity Fragmentation

A very small tick size makes it cheap for multiple market makers to quote at slightly different prices. If the tick is $0.0001, a market maker can undercut a competitor's offer by $0.0001 and gain market share. This creates an incentive to post many small orders at many slightly different prices, fragmenting the visible liquidity.

Instead of one deep order at $50.00, liquidity is scattered across dozens of venues and price levels at $50.0000, $50.0001, $50.0002, etc. A buyer looking to execute a large block must pick off orders across multiple prices, paying the aggregate cost of many small crossing. This is called fragmentation.

Fragmentation reduces the *depth* of liquidity—the number of shares available at a given price. A trader may see tight spreads but discover that only a handful of shares are available at the best price, and the next tier is far away. The effective cost of executing a large trade rises.

## The Sweet Spot: Balancing Price and Depth

Regulators and exchanges grapple with finding the optimal tick size. Too small, and liquidity fragments and execution becomes costly for large orders. Too large, and the spread is wide for everyone, hurting retail traders and price efficiency.

The U.S. has converged on a one-cent tick for most equities as a compromise. It allows competitive market makers to quote tightly without fragmenting excessively. For highly liquid mega-cap stocks, the bid-ask spread is often a single cent, and depth is deep enough that large institutional orders can execute in full at or near the quoted price.

But for illiquid securities—small-cap stocks, illiquidity bonds, or newly listed companies—a one-cent tick is relatively large. The spread widens, and market makers are less willing to trade, because the one-cent increment is a material fraction of their profit margin. A market maker might require a 5-cent or 10-cent spread to justify holding inventory in a low-volume security.

## The Pilot and Regulatory Debate

In 2010–2014, the SEC conducted a pilot program testing larger tick sizes (5 cents, 20 cents, or $1.00) for small-cap stocks. The results were mixed:

- **Spreads widened** significantly, especially for the 5-cent and larger tick groups. The average spread tripled in some cases.
- **Depth increased** in some cohorts; market makers posted larger order sizes at each price, knowing they would earn more per trade.
- **Trading volume fell** in the larger-tick securities; some traders migrated to off-exchange venues or simply avoided trading.
- **Prices became less efficient**: prices moved less frequently and less nimbly, lagging changes in fundamental value.

The SEC concluded that the benefit of wider spreads (which theoretically incentivizes market makers to hold inventory) was outweighed by the cost of wider quoted spreads and lower trading efficiency. The pilot was allowed to expire, and the one-cent tick remained standard.

However, the debate continues. Some market makers argue that small-cap liquidity would improve if they were assured of a wider tick, and some academics contend that the pilot did not account for dynamic market maker behavior over time. Regulators periodically revisit the question but have not adopted large-tick-size regimes wholesale.

## Tick Size and Market Maker Profit

Market makers earn money on the [bid-ask spread](/bid-ask-spread/), and tick size affects their profitability directly. In a one-cent tick environment on a liquid stock, a market maker might execute 1,000 shares per minute at a 1-cent spread, earning $10 per minute in gross profit (before costs). Scaling up requires taking on inventory risk and managing position limits.

If the tick were widened to 5 cents, a market maker could earn $50 per 1,000 shares executed. But execution volume might fall because traders would face wider spreads and look elsewhere. The net effect on profit depends on whether the higher margin per trade offsets the lower volume.

For illiquid securities, market makers often struggle to profit at a 1-cent tick because of the volatility and inventory risk. Widening the tick would improve their risk-adjusted returns, but the regulatory concern is that it would harm retail traders and impair price discovery.

## Historical Context: The Shift from Eighths to Cents

Before 2001, U.S. stocks were quoted in eighths of a dollar (12.5 cents). This was standard for over a century. The Securities and Exchange Commission ordered exchanges to shift to cents (a 100x finer granularity) to improve price competition and tighten spreads.

The shift was dramatically successful. After decimalization, average spreads narrowed from 12.5 cents to 1 cent or less on most stocks. Retail traders benefited immediately from tighter pricing. But it also accelerated the rise of algorithmic trading, as the finer tick size made automated order splitting and fragmentation more profitable.

The historical lesson is that once a tick size is established, reversing it is politically difficult and markets adapt quickly.

## Tick Size in Other Markets

- **Forex**: Currency pairs typically quote in 4 or 5 decimal places (much finer than equities), reflecting the high volume and tight competition.
- **Bonds**: Corporate and government bonds often trade with implied tick sizes of 1/32 of a point ($0.3125) or narrower, depending on liquidity.
- **Futures**: Tick sizes vary by contract; corn futures, for instance, move in quarter-cent ($0.0025) increments.
- **Options**: Strike prices are typically one-cent increments; tick sizes for the option price itself vary.

Each market finds its own equilibrium based on liquidity, regulatory requirements, and venue competition.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — How tick size constrains the narrowest possible spread
- [Market Maker Trading](/market-maker-trading/) — How market makers profit from spreads and manage inventory risk
- [Price Discovery](/price-discovery/) — How tight ticks and high-frequency trading affect the efficiency of price formation
- [Liquidity Risk](/liquidity-risk/) — How tick size influences the cost of trading large blocks
- [Algorithmic Trading](/algorithmic-trading/) — How sub-penny quoting and fragmentation emerge from small tick sizes

### Wider context

- [Stock Market](/stock-market/) — Overview of market structure and trading rules
- [Stock Exchange](/stock-exchange/) — Venues that set and enforce tick size rules
- [Opening Auction and Price Discovery](/opening-auction-price-discovery/) — How tick size interacts with opening price calculation

</div>

---
title: "Tick Size"
description: "The minimum allowable price increment for a security, set by exchange rules; affects spreads, liquidity, and the ability to improve on the best bid or ask."
keywords:
  - tick size
  - minimum price increment
  - bid-ask spread
  - market liquidity
  - tick value
  - exchange rules
image: "/svg/trading.svg"
---

*A **tick** is the smallest unit of price movement allowed in a security. **Tick size** is that minimum increment—set by the [stock exchange](/stock-exchange/) and regulators—that all prices must respect. For US equities, most stocks trade in ticks of $0.01 (one cent), though some lower-priced stocks tick in larger increments. Tick size is not mere technical detail; it shapes [spreads](/bid-ask-spread/), [liquidity](/liquidity-risk/), and the economics of trading itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tick Size — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">The rung on the price ladder that traders must use.</div>

|   |   |
|---|---|
| **What it is** | Minimum price increment allowed on a particular security or market |
| **For US equities** | Usually $0.01 per share; larger for penny stocks |
| **For other markets** | Varies: forex in pips, futures in contract-specific ticks |
| **Set by** | [Securities and Exchange Commission](/securities-and-exchange-commission/) and exchange rules |
| **Affects** | [Bid-ask spread](/bid-ask-spread/), [market maker](/market-maker-trading/) economics, trade execution |
| **Related concept** | [Pip](/pip/) in currency markets; contract specifications in futures |

</aside>

## The price ladder

In a market where prices must move in $0.01 increments, the tradeable prices form a discrete ladder: $50.00, $50.01, $50.02, and so on. A buyer cannot bid $50.005; that rung does not exist. A seller cannot offer $50.015. Both must pick the nearest allowed tick.

This is not arbitrary. Before the 1990s, US stock [markets](/stock-exchange/) quoted prices in eighths of a dollar (twelve and a half cents). Then sixteenths (6.25 cents). In April 2001, the shift to "decimalization"—a tick of $0.01—was mandated to modernise US trading. The goal was transparency and tight spreads. It largely succeeded, though it also changed who profits and who bleeds in the market microstructure.

## How tick size affects the spread

The [bid-ask spread](/bid-ask-spread/) is the gap between the highest price a buyer will pay (the bid) and the lowest price a seller will accept (the ask). If the bid is $50.10 and the ask is $50.11, the spread is one tick, one cent. A spread of one tick is tight; one of five ticks ($0.05) is looser.

Tick size acts as a floor on the spread. If tick size is $0.01, the smallest possible spread is $0.01—a single cent. If tick size were $1.00, the smallest spread would be a dollar. Larger ticks make markets wider and more expensive for traders to cross. Smaller ticks allow [market makers](/market-maker-trading/) and traders to undercut each other more finely, driving spreads tighter.

Smaller ticks are generally good for buyers and sellers (tighter costs) but challenging for market makers, who earn less per trade. This tension has driven debate over tick size in regulation for years.

## Tick value and notional exposure

Tick value—the dollar amount of a one-tick move—depends on the contract size or share count. For a single share of stock, a one-tick move of $0.01 is worth one cent. For a stock [futures contract](/futures-contract/) on 100 shares, one tick might move the contract by $1.00. For a currency pair in pips, a one-pip move in EUR/USD is worth differently than in USD/JPY.

A trader's profit and loss from a price move is always tick value multiplied by the number of ticks moved. Understanding tick value is essential for position sizing and [risk management](/market-risk/).

## Tick size and market structure

Smaller tick sizes encourage tighter competition. [Market makers](/market-maker-trading/) can profit from trading more frequently at narrower margins. [Algorithmic traders](/algorithmic-trading/) can build strategies that profit from the rapid arrival and cancellation of orders in a finely graded price ladder. Liquidity pools deepen at each price level, and the market becomes more efficient at [price discovery](/price-discovery/).

But smaller ticks also increase [latency](/high-frequency-trading/) sensitivity. If tick size is $0.01, the difference between buying at $50.00 and $50.01 is $100 per 10,000 shares—a huge amount in the context of high-frequency trading. Firms that can shave a few milliseconds of delay can systematically outrun competitors.

Larger tick sizes, by contrast, reduce the incentive for ultra-low-latency competition. They also make it easier for [market makers](/market-maker-trading/) to stay profitable because the spread is wider and tighter competition is harder. For less liquid stocks, a larger tick size may actually improve displayed liquidity by reducing the cost of posting firm orders.

## Tick sizes across markets

US equities mostly use $0.01 ticks, but very low-priced stocks ("penny stocks") may trade in $0.001 or even $0.0001 increments. The [NASDAQ](/nasdaq/) and [New York Stock Exchange](/new-york-stock-exchange/) enforce minimum bid rules—no stock can trade below $1 on a regular exchange, and bid prices must be realistic—to prevent abuse.

Currency markets use pips (percentage in point), typically four decimal places for major pairs like EUR/USD: a pip is $0.0001. Precious metals often trade in cents per ounce. [Futures contracts](/futures-contract/) have their own tick sizes, set by the exchange and the contract specification.

## The tick-size debate

Since decimalization, the spread on US equities has narrowed dramatically. A stock that once traded with an eighth-dollar spread ($0.125) now trades at a single cent or less. This has reduced execution costs for retail and institutional traders alike.

However, [market makers](/market-maker-trading/) have seen their spread revenue shrink. Some argue that in order to maintain profitability, tick sizes for less liquid stocks should be raised, allowing wider spreads. The [Securities and Exchange Commission](/securities-and-exchange-commission/) has run pilot programmes testing this. A modest increase in tick size, the argument goes, would encourage market makers to post tighter spreads and deeper liquidity, benefiting retail investors on balance.

Others counter that larger tick sizes are regressive—they widen the bid-ask spread that ordinary traders pay when they buy and sell, concentrating profits with market makers. The debate remains unresolved.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the cost of crossing the market immediately
- [Market maker](/market-maker-trading/) — provider of liquidity at posted prices
- [Market order](/market-order/) — buy or sell at the best available price
- [Limit order](/limit-order/) — buy or sell at a specified price or better
- [Pip](/pip/) — tick size in currency markets
- [Price discovery](/price-discovery/) — the process by which markets arrive at fair prices
- [Liquidity risk](/liquidity-risk/) — inability to trade at the posted price without moving it
- [VWAP execution](/vwap-execution/) — benchmark algorithm sensitive to precise price placement

### Wider context

- [Stock exchange](/stock-exchange/) — organised venue for trading securities
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — US regulator of equities and exchanges
- [Algorithmic trading](/algorithmic-trading/) — systematic execution strategies
- Market impact — the price movement caused by large trades
- [High-frequency trading](/algorithmic-trading/) — rapid execution strategies exploiting tick-scale opportunities

</div>

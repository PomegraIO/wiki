---
title: "Minimum Price Increment and Tick Size Rules"
description: "How regulators set minimum price increments, why tighter ticks narrow spreads but reduce displayed liquidity, and what the SEC Tick Size Pilot revealed."
keywords:
  - tick size rules
  - minimum price increment
  - regulatory tick sizes
  - bid-ask spread narrowing
  - market liquidity
  - sec tick size pilot
image: "/svg/trading.svg"
---

*Regulators set **minimum price increments (tick sizes)** to balance two competing goals: narrower spreads improve execution for investors, but too-tight increments can reduce the displayed liquidity available. The SEC Tick Size Pilot (2013–2015) showed that smaller ticks do compress bid-ask spreads but can harm displayed order flow and market depth, creating a tradeoff that has shaped policy debates and pilot programs across exchanges.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Minimum Price Increment and Tick Size — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The smallest price move allowed by rule shapes both spreads and liquidity depth.</div>

|   |   |
|---|---|
| **Definition** | The minimum amount a stock price can move; e.g., $0.01 for most U.S. equities (penny tick). |
| **Tradeoff** | Smaller tick = tighter [bid-ask-spread](/bid-ask-spread/) but sometimes less displayed depth. |
| **U.S. equity tick** | $0.01 (one cent) for stocks above $1; ticks in sub-$1 stocks are $0.0001 in some venues. |
| **Regulatory body** | SEC sets rules; exchanges and alternative venues implement and compete via tick policies. |
| **Key pilot finding** | Stocks with relaxed ticks (wider allowable increments) showed higher spreads but more displayed liquidity. |
| **Current practice** | Pilots have concluded; penny ticks remain standard for large-cap equities. |

</aside>

## How Tick Size Rules Govern Price Discovery

A **tick size** (or minimum price increment) is the smallest amount a security's price can move. In U.S. equities, the standard is $0.01 (one penny) for stocks quoted above $1 per share, set by SEC regulation in 2001. A stock cannot trade at $50.001; the next price is $50.01. This granularity affects how the [bid-ask-spread](/bid-ask-spread/) forms.

If the **[bid-ask-spread](/bid-ask-spread/)** is one tick wide, the bid might be $50.00 and the ask $50.01—a spread of one cent. If the tick size were $0.10, the bid could only be $50.00 and the ask $50.10, making the spread a dime. Tighter ticks, therefore, mechanically allow tighter spreads.

But tick size also affects how much volume displays at the best bid and ask prices. If I want to sell 10,000 shares, I might post my limit order at the ask price. If the tick is wide, few sellers may post at the same ask price, so total displayed depth at that price is shallow. If the tick is tight, more sellers can stack at the same ask price, making depth deeper—or, conversely, sellers might undercut aggressively, fragmenting liquidity across multiple prices.

## The Spread Narrowing Effect

Before 2001, U.S. equities traded in eighths and sixteenths of dollars (a tick of $0.125 or $0.0625). When the SEC mandated a move to penny increments ("decimalization"), bid-ask spreads collapsed. The average spread for the smallest NASDAQ stocks narrowed from 30 cents to a few cents almost instantly.

Spreads tightened for three reasons:
1. **Mechanical reduction**: Dealers could now quote $50.01 rather than $50.10.
2. **Price competition**: Brokers and dealers could undercut each other by smaller increments, so the incentive to narrow spreads intensified.
3. **Retail flow attraction**: With penny increments, [market-maker](/market-maker-trading/) competition for small orders heated up, pushing spreads tighter.

This spread compression was widely celebrated as a win for price efficiency. Investors paid less per trade, and [price-discovery](/price-discovery/) improved—more prices crowded closer together, revealing market opinion more finely.

## The Liquidity Depth Puzzle

The downside of penny ticks, however, appeared over time. Some evidence suggests that very tight tick sizes reduce the amount of liquidity at the best prices.

The logic is indirect. With wider ticks, if you want to buy stock at the best bid, you must accept a wide spread. But dealers know that few will accept such a spread, so they post more depth—more shares available—at that best price, hoping to grab the order. With penny ticks, a dealer might post just a few shares at the best bid/ask, then undercut or pull the order quickly, because the cost of being aggressively undercut is only a penny. This "flickering" liquidity can harm execution for large orders.

Additionally, with tighter ticks, dealers must work harder to recoup the cost of providing liquidity. If the spread is one penny on a $100 stock, the gross profit per share is minimal. Dealers may respond by posting less visible depth and relying more on [high-frequency trading](/algorithmic-trading/) strategies to eke out profits through volume. This can leave large institutional investors with less displayed depth than they would encounter under wider ticks.

## The SEC Tick Size Pilot (2013–2015)

To test the spread-versus-depth tradeoff empirically, the SEC ran a **Tick Size Pilot** from October 2013 to September 2015. The SEC selected about 400 small-cap stocks and assigned them randomly to treatment groups. Some got their tick size widened from $0.01 to $0.05; control stocks remained at penny ticks.

**Key findings:**
- **Spreads widened**: Pilot stocks saw average spreads increase by roughly 0.5–1.0 cents, as expected. Executions became marginally worse for small orders.
- **Displayed depth increased**: Stocks with $0.05 ticks showed more shares displayed at the best bid and ask prices—20–30% higher depth in some studies.
- **Order routing improved**: Large institutional orders found more liquid depth on the wider-tick stocks, especially during stressed market conditions.
- **No clear winner**: The pilot revealed that wider ticks help large orders but hurt small retail orders, creating a stark tension.

The pilot did *not* show a broad improvement in market quality from wider ticks. Fragmentation and high-frequency trading remained dominant; the $0.05 increment did not reverse those trends. The SEC ultimately let the pilot expire without implementing a permanent widening of the tick, leaving the penny tick in place.

## Tick Sizes Across Market Segments

Different market segments operate under different tick rules:

**Large-cap equities (NYSE, NASDAQ)**: Penny tick ($0.01) for all listed stocks above $1. The [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) enforce this.

**Penny stocks and sub-$1 issues**: Some are quoted in penny increments; others trade over-the-counter at larger ticks or with no fixed increment.

**Bonds**: Treasury and corporate bonds often trade in thirty-seconds or sixty-fourths of a point (1/32 or 1/64), much wider than equities. This reflects lower trading volume and higher bid-ask spreads.

**Options**: Quotes are usually in nickels ($0.05) or dimes for out-of-the-money options, creating wider ticks than the underlying stock.

**International markets**: London Stock Exchange (LSE) and other venues use tick schedules that vary by price level. Lower-priced stocks might have wider ticks; higher-priced stocks, tighter ticks.

## Modern Debates and Alternatives

Post-pilot, regulators and industry have explored alternatives to outright tick widening:

**Tick schedules by price level**: Widen the tick for lower-priced or less-liquid stocks while keeping penny ticks for high-liquidity names. This targets relief where liquidity is most fragile.

**Batch auction mechanisms**: Some alternative venues use periodic batch auctions instead of continuous trading, sidestepping the fragmentation problem. In a batch auction, all orders execute at a single price every N seconds, eliminating the incentive to undercut by one tick.

**Minimum order size thresholds**: Require larger minimum orders to post at the best prices, protecting large displayed depth from high-frequency undercutting.

The central tension—that spreads and depth move in opposite directions—has no perfect solution. Regulators must weigh the cost to retail (wider spreads) against the benefit to large institutional orders (deeper visible liquidity).

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the tightest mechanism by which tick size affects transaction costs.
- [Market Maker Trading](/market-maker-trading/) — dealers who quote the bid and ask, shaped by tick size incentives.
- [Price Discovery](/price-discovery/) — how tick size and spread affect the efficiency of price formation.
- [Algorithmic Trading](/algorithmic-trading/) — high-frequency strategies that exploit small tick increments.
- [Alternative Trading System](/alternative-trading-system/) — venues that offer different tick and execution rules.

### Wider context

- [Stock Exchange](/stock-exchange/) — where tick rules are enforced and compete.
- [Liquidity Risk](/liquidity-risk/) — wider ticks can reduce the liquidity available in a crisis.
- [Order Routing](/market-order/) — how tighter ticks affect the choice between limit and market orders.
- [SEC](/securities-and-exchange-commission/) — the regulator setting tick policy.
- [Fragmented Market](/fragmented-market/) — how narrow ticks contribute to splitting of volume across venues.

</div>

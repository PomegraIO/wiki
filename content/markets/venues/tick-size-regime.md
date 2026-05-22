---
title: "Tick Size Regime"
description: "How minimum price increments change market structure, liquidity, and trading mechanics."
keywords:
  - tick size
  - minimum price increment
  - market microstructure
  - bid-ask spread
  - liquidity
---

*A **tick size regime** is the minimum price increment (the "tick") allowed for quotes in a given security or market. A $0.01 tick in US equities means prices move in one-cent increments; changing the tick size alters [bid-ask spreads](/wiki/bid-ask-spread/), [order-book depth](/wiki/order-book-depth/), and which [trading strategies](/wiki/swing-trading/) are profitable.*

<aside class="wiki-infobox">

| Market | Typical Tick | Effective Spread | Notes |
|---|---|---|---|
| **US large-cap stocks** | $0.01 | 1–3 cents | Tight; high liquidity |
| **US small-cap stocks** | $0.01 (nominal) | 5–50 cents | Effective spread widens due to low volume |
| **[Forex](/wiki/forex-leverage/)** | 0.0001 (pip) | 0.1–0.5 pips | Highly fragmented across venues |
| **[Futures](/wiki/futures-contract/)** | Varies by contract | Often $0.01 or $0.10 | Fixed by [CBOT](/wiki/cme-group/) or [CME](/wiki/cme-group/) |
| **[Options](/wiki/option/)** | $0.01 (under $3) or $0.05 | 1–10 cents | Reflects underlying tick |
| **Penny stocks** | $0.01 | Often 2–5 cents | Illiquid; wide effective spreads |

</aside>

## How tick size affects spread and volume

A finer (smaller) tick—such as moving from $0.05 to $0.01—allows [market makers](/wiki/market-makers/) to quote more granular prices. In theory, this helps them compete for order flow and narrow the [bid-ask spread](/wiki/bid-ask-spread/). In practice, the effect depends on:

1. **Liquidity level** — if the market is already deep and tight, reducing tick size may do little. If volume is thin, finer ticks often do nothing because the true spread is driven by uncertainty, not mechanical rounding.

2. **High-frequency traders' response** — faster [algorithmic traders](/wiki/algorithmic-trading/) can layer orders more finely with a tighter tick, potentially narrowing spreads in liquid names but also creating fragmented [order-book depth](/wiki/order-book-depth/).

3. **Price discovery** — finer ticks allow more transparent price competition and faster movement toward the true [fundamental value](/wiki/intrinsic-value/).

## The US equity tick evolution

Until 2001, US stocks traded in eighths (1/8 = $0.125) or sixteenths (1/16 = $0.0625). The switch to **decimalization** (pennies, $0.01) was a watershed:

- **Spreads collapsed** — average bid-ask spread on large-cap stocks fell from ~2 cents to under 1 cent.
- **Volume surged** — lower friction encouraged more trading and [day trading](/wiki/day-trading/).
- **[High-frequency trading](/wiki/high-frequency-trading/) emerged** — sub-millisecond advantages became profitable with tighter ticks.
- **Market maker profitability fell** — the old model of wide spreads + steady order flow no longer worked; new firms built automation.

## Sub-penny tick trading and regulation

After decimalization, some [dark pools](/wiki/dark-pool/) and [alternative trading systems](/wiki/alternative-trading-system/) began accepting trades in sub-penny increments (0.001 cents). This created a two-tiered market:

- **Lit venues** (public exchanges): tick size = $0.01
- **Off-exchange venues**: sub-penny prices (0.001 or smaller)

This fragmentation allowed sophisticated traders to find better prices away from public quotes, but it also widened the informational gap. Retail investors saw the public spread, but institutions transacted at better prices elsewhere. The **SEC's Regulation SHO** and subsequent rules tightened sub-penny quoting in 2005, but the fragmentation persists.

## Tick size and profitability of scalping

[Scalping](/wiki/scalping/) (buying and selling within seconds for small profits) depends on tight tick sizes. With $0.05 ticks, scalping is nearly impossible—transaction costs are too high relative to the move. With $0.01 ticks, a scalper can profit from 1–2 cent moves if they execute fast enough.

Widening tick sizes (moving from $0.01 to $0.05) makes scalping harder, while tightening tick sizes (adding sub-penny increments) makes it easier. Regulations sometimes adjust tick size for specific securities as a tool to encourage or discourage certain trading behaviors.

## Tick size and small-cap stocks

In 2016, the SEC ran a pilot program on small-cap stocks, widening tick sizes from $0.01 to $0.05 for some pilot names. The experiment found:

- Spreads actually *widened* on some stocks (contrary to the hypothesis that wider ticks would reduce competition and narrow spreads in illiquid names).
- [Order-book depth](/wiki/order-book-depth/) did not consistently improve.
- Small retail traders and smaller brokers were disadvantaged relative to large market makers.

The pilot was controversial and largely rolled back. The lesson: tick size changes have complex, often counterintuitive effects on market quality.

## Tick size in different asset classes

**[Options](/wiki/option/)** — tick sizes are $0.01 for [option premium](/wiki/option-premium/) under $3, and $0.05 above $3. This reflects [moneyness](/wiki/moneyness/): in-the-money [call](/wiki/call-option/) contracts need finer ticks; far out-of-the-money contracts, which move in larger blocks, use coarser ticks.

**[Commodities](/wiki/commodity-futures-rolling/)** — [futures](/wiki/futures-contract/) ticks are set by the exchange (e.g., [CME](/wiki/cme-group/)) and vary by contract. [Crude oil](/wiki/crude-oil/) trades in $0.01 increments; [corn](/wiki/corn/) in $0.0025. The granularity reflects typical daily [volatility](/wiki/implied-volatility/) and contract size.

**[Forex](/wiki/forex-leverage/)** — the foreign exchange market uses "pips" (usually 0.0001 of the major pairs like EUR/USD). This is effectively a 0.01% tick. [Currency pairs](/wiki/currency-pair/) with lower volatility (e.g., EUR/GBP) sometimes quote in 0.00001 increments (fractional pips).

## Microstructure consequences

Finer tick sizes:
- ✓ Narrow [bid-ask spread](/wiki/bid-ask-spread/) for highly liquid assets
- ✓ Enable more [price discovery](/wiki/price-discovery/) (less rounding error)
- ✗ Increase [order-book fragmentation](/wiki/order-book-depth/) (more quotes to track)
- ✗ Favor [high-frequency trading](/wiki/high-frequency-trading/) over passive investors

Coarser tick sizes:
- ✓ Reduce noise and computational load
- ✓ May restore [market maker](/wiki/market-makers/) margins (wider spreads)
- ✗ Reduce price discovery precision
- ✗ Discourage [retail participation](/wiki/day-trading/) (spreads are too wide)

<div class="wiki-seealso">

### Closely related
- [Bid-ask spread](/wiki/bid-ask-spread/) — the practical cost of tick size choices
- [Order-book depth](/wiki/order-book-depth/) — how tick size affects liquidity display
- [Pip](/wiki/pip/) — tick-size equivalent in foreign exchange
- [Price discovery](/wiki/price-discovery/) — how tick size affects true value detection
- [High-frequency trading](/wiki/high-frequency-trading/) — benefits from tighter tick sizes

### Wider context
- [Market microstructure](/wiki/market-maker-obligations/) — broader study of trading mechanics
- [Alternative trading system](/wiki/alternative-trading-system/) — off-exchange venues with different tick rules
- [Regulation SHO](/wiki/regulation-sho/) — regulatory framework for short selling and quoting
- [Execution quality analysis](/wiki/execution-quality-analysis/) — measuring the impact of tick size on traders
- [Market maker liability](/wiki/market-maker-liability/) — how tick size affects inventory risk

</div>

---
title: "Rollover Cost in Futures Contracts"
description: "The bid-ask spreads and price differences incurred when traders close an expiring futures position and open a new one in the next contract month."
keywords:
  - rollover cost futures
  - futures contract expiration cost
  - contango backwardation trading cost
  - futures roll yield
  - next contract month spread
---

*A **rollover cost** is the transaction expense and market slippage incurred when a trader closes an expiring [futures contract](/futures-contract/) and simultaneously opens a new position in the next monthly contract. The cost comprises [bid-ask spread](/bid-ask-spread/) and the price premium or discount between contracts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rollover Cost — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Every roll incurs both mechanical spreads and curve-driven slippage.</div>

|   |   |
|---|---|
| **The cost** | Sum of bid-ask spread and the price difference between contracts |
| **When it occurs** | As a contract nears expiration (typically last 1–2 weeks before delivery date) |
| **Contango impact** | New contract costs more; trader pays the difference on entry |
| **Backwardation impact** | New contract costs less; trader gains on entry but paid more to exit old contract |
| **Typical magnitude** | 0.01–0.50% of contract value, depending on liquidity and curve shape |
| **Example** | Crude oil contract 6 months out may trade 2–5% below spot; rolling incurs that differential |

</aside>

## The mechanics of rolling a position

Futures contracts have fixed [expiration dates](/expiration-date/). An oil trader holding December crude oil futures cannot hold them indefinitely; they expire in December. To maintain a position beyond that date, the trader must simultaneously sell the December contract and buy the January contract. This simultaneous action is called a "roll."

A clean roll looks simple on paper: close one and open another. In practice, two frictions appear. First, the trader hits the [bid-ask spread](/bid-ask-spread/) on both trades — selling the December contract at the bid (a lower price) and buying January at the ask (a higher price). For illiquid contracts, spreads widen; for active contracts like S&P 500 futures, spreads are tight.

Second, the December and January contracts trade at different prices, reflecting expectations about future supply, demand, or storage costs. The difference between the two is the **roll yield** — the gain or loss from the price difference alone. When January costs more than December (a situation called [contango](/contango/)), rolling incurs a cost; when January costs less ([backwardation](/backwardation/)), rolling generates a gain.

## Contango and the cost of storage

In [contango](/contango/), forward contracts trade at progressively higher prices than the spot contract. This is the normal state for commodities with positive carrying costs — oil, grain, metals — where storage, insurance, and financing must be paid to hold the physical good.

When a crude oil trader rolls from the nearby expiring contract to the next month, she sells the near contract (which has tightened toward spot) and buys the far contract (which reflects the full cost of carry). If spot crude is $80 per barrel and the January contract is $82, the trader pays a 2-dollar premium, or 2.5%, to roll. Multiply this across the year (rolling monthly), and it compounds.

A trader holding long oil futures for a full year in a steeply contango market can lose 10% or more to rollover costs before any price movement. Commodity funds and exchange-traded products that mechanically roll their positions incur this drag month after month. It is why [commodity ETFs](/etf/) sometimes significantly underperform the spot price of the underlying commodity; rolling costs eat returns.

## Backwardation and roll profits

[Backwardation](/backwardation/) reverses the picture. In backwardation, nearby contracts trade higher than deferred ones, typically a sign of near-term scarcity or high demand. When rolling in backwardation, the trader buys a contract that is cheaper than the one being sold.

For example, if December crude is $82 and January is $80, the trader receives a 2-dollar gain (or 2.5% roll yield) on the position shift. In a strongly backwardated market—such as oil during a supply disruption—rolling can be profitable. A speculator positioned long benefits from the shape of the [futures curve](/futures-contract/); the roll is a tailwind rather than a drag.

However, backwardation is typically temporary. It signals an imbalance that is often resolved by delivery or production response. A trader banking on positive roll yield in backwardation is exposed to the risk that the curve flattens or inverts into contango as the market rebalances.

## Bid-ask spread as a component

Beyond the price difference, the mechanical [bid-ask spread](/bid-ask-spread/) is a direct and unavoidable cost. A trader selling the near contract receives the bid price and buying the far contract pays the ask price. On each, the spread is a small loss.

For the most liquid contracts—crude oil, S&P 500 futures, Treasury bond futures—spreads are often one or two ticks (the minimum price increment, often $10–$25 per contract). On an oil contract worth $100,000 notional value, a two-tick spread of $20 is 0.02%. But in less-liquid months or during volatile market conditions, spreads can widen to 5–10 ticks, materially increasing the rollover cost.

Institutional traders and market makers exploit this. They know when large traders must roll and often widen spreads as roll dates approach. A manager rolling a billion-dollar oil position across hundreds of contracts cannot execute instantly; the market observes the order flow and pushes prices against them.

## The cumulative impact on long-term strategies

For a trader or fund holding a continuous position in a commodity or index, rollover costs compound annually. An investor in a broad commodity index might pay 0.5% per roll across multiple markets—some in steep contango, others in mild backwardation. Rolling monthly across 10 commodities, that's roughly 5–6% per year in pure rollover drag, before any price appreciation or depreciation.

This is why buy-and-hold investors often prefer spot positions, forwards, or physical holding when feasible. A direct [crude oil](/crude-oil/) purchase funded at the current [interest rate](/interest-rate/) may cost less than rolling futures month after month. For some commodities, futures-based strategies are necessary (no retail access to physical holdings), but the rollover cost is always factored into expected returns.

## Timing the roll: early vs. late

Traders have some discretion in when to roll. Rolling too early—when the calendar spread is wide—incurs a larger cost. Rolling too late—right before expiration—risks liquidity crunch and wider spreads. Most professionals roll during the 1–2 weeks before expiration, when both nearby and deferred contracts have deep liquidity and the spread between them has stabilized.

Some algo strategies use price patterns to optimize roll timing, selling the near when it is relatively expensive and buying the far when it is relatively cheap. These micro-optimizations save a few basis points per roll, but they require speed and careful execution.

## Impact on ETFs and index replication

Exchange-traded funds that replicate commodity or [futures-contract](/futures-contract/) indices must roll continuously. A fund tracking oil prices via futures will incur the full cost of carry in contango. A fund tracking natural gas might benefit from backwardation during winter demand. Over years, the impact is substantial.

Fund sponsors disclose expected "roll yield" in prospectuses and fact sheets. In contango markets, this is negative; the fund expects to lose to the roll. In backwardation, it is positive. Some funds use "optimized" roll schedules or own a mix of contract months to minimize costs, but the core physics—that rolling has a cost determined by the curve shape—cannot be avoided.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — standardized agreement to buy/sell an asset at a future date with fixed expiration
- [Contango](/contango/) — situation when forward prices exceed spot price; incurs rollover costs
- [Backwardation](/backwardation/) — situation when forward prices are below spot price; can generate roll profits
- [Bid-ask spread](/bid-ask-spread/) — the transaction cost between buy and sell prices in any market
- [Crude oil](/crude-oil/) — the commodity most heavily traded via futures, with significant rollover costs

### Wider context

- [Cost of debt](/cost-of-debt/) — cost of financing, which underlies carry costs
- [Derivatives hedging](/derivatives-hedging/) — using futures to reduce risk; rollover costs reduce hedging efficiency
- Trading costs — all costs incurred in executing trades, of which rollover is one
- [ETF](/etf/) — investment fund that may use futures and bear rollover costs

</div>

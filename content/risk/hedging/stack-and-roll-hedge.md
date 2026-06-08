---
title: "Stack-and-Roll Hedge"
description: "A hedging strategy using repeated short-dated futures contracts rolled forward to manage long-term price exposure."
keywords:
  - futures hedging
  - roll strategy
  - commodity hedging
  - price risk management
  - stack and roll
image: "/svg/risk.svg"
---

*A **stack-and-roll hedge** uses a series of short-dated [futures contracts](/futures-contract/) that are repeatedly rolled forward to hedge a long-term price exposure. Instead of buying a single long-dated futures contract, a hedger sells multiple near-term contracts, then closes them and sells the next maturity as each contract approaches expiration, creating a rolling series of shorter-term positions that collectively protect against price movement over a multi-year horizon.*

## Why hedgers choose short-dated contracts over single long-dated ones

A hedger with a multi-year exposure—say, a manufacturer locked into fixed pricing through 2028—might seem to want a single futures contract expiring in 2028. In practice, this is often impossible or prohibitively expensive. Exchanges list only a handful of contract expirations at any time; a contract three years out may have little trading volume and a wide [bid-ask spread](/bid-ask-spread/). The cost of executing and unwinding such a sparse contract is severe.

By contrast, the nearest-dated contracts are highly liquid. A stack-and-roll strategy sells, say, five near-term contracts (each expiring in the next quarter), then as the first expires, the hedger closes it and sells the next quarterly contract out, repeating this cycle. Because each leg trades in a deep, tight market, execution costs remain low throughout the hedge lifetime.

## The mechanics of rolling

Rolling is straightforward in principle. Suppose a corn farmer wants to lock in prices for next year's crop. In Month 1, she sells 10 December corn futures contracts (expiring in 3 months). As December arrives, she buys back those 10 contracts to close the position, simultaneously selling 10 March contracts (the next quarterly expiration). When March approaches, she repeats: buy March, sell June. This continues until harvest.

The transition between contracts is typically done "on the calendar spread"—both legs execute together as a package order. The cost of rolling is the price difference between the two expirations, called [contango](/contango/) or [backwardation](/backwardation/), depending on the commodity market structure. In normal supply conditions, near-term prices are cheaper than forward prices (backwardation), so each roll captures a small premium. In surplus conditions, rolling incurs a cost as far prices are cheaper than near prices.

## When costs compound and execution risk emerges

Stack-and-roll hedges appear cheaper upfront but carry hidden expenses. If a hedger must roll a 60-contract position every quarter for five years, that is 20 rolling events. Even a quarter-point slippage per roll—seemingly trivial in a single transaction—compounds to meaningful cost over the horizon. Market dislocations near contract expiry, gaps in liquidity, or algorithmic slippage during execution can erode returns unexpectedly.

Moreover, the hedger is exposed to **roll risk**: the risk that market conditions shift unfavorably when rolling time arrives. If a drought suddenly spikes backwardation, rolling may incur unexpectedly steep costs. Conversely, a glut might create extreme contango, making rolls profitable but creating balance-sheet volatility as unrealised gains on the short positions spike and crash month to month.

## Suited to commodity and currency hedges

Stack-and-roll is standard in commodity hedging because commodities trade in seasonal patterns with pronounced contango and backwardation. Airlines, for instance, routinely stack-and-roll [crude oil](/crude-oil/) or [natural gas](/natural-gas/) hedges quarterly or monthly, adjusting hedge ratios as fuel consumption forecasts change. Multinational firms use stack-and-roll for [currency risk](/currency-risk/) management, rolling forward near-term [forward contracts](/forward-contract/) to hedge foreign revenues or payables over multi-year budgeting cycles.

The strategy is far less common in equity [index](/sp-500-index/) hedging, where long-dated [options](/option/) or variance swaps offer more direct protection, and where rolling costs are smaller relative to the notional exposure.

## Trade-offs: flexibility versus conviction

The rolling structure offers flexibility that a single long-dated contract cannot. A farmer can adjust hedge ratios as crop expectations change—selling fewer contracts if yields improve, or layering in additional hedges if prices move adversely. This adaptability is valuable under uncertainty.

The downside is that rolling requires ongoing attention and execution discipline. It is also a form of market timing: by choosing when and how much to roll, the hedger implicitly bets on the near-term price structure. A hedger who loses nerve and rolls too late, or who over-commits to early rolls, can amplify losses during volatile roll periods.

## The yield pickup from rolling in backwardated markets

In commodity markets that are in structural backwardation—where near-term prices exceed forward prices—stack-and-roll hedges can generate small but consistent income. Each roll incurs a positive cash flow as the hedger closes a higher-priced near contract and sells a lower-priced forward contract. Over decades, this yield pickup has been measurable, particularly for oil and agricultural hedges. However, backwardation is cyclical; when it reverses to contango, rolling becomes a drag on performance.

Institutional funds sometimes run synthetic commodity indices that deliberately stack-and-roll, harvesting the roll yield as a return source. The practice has become commoditized, leading to crowding and reduced margins.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — standardized agreement to buy or sell at a future date; the underlying instrument in stack-and-roll strategies
- [Contango](/contango/) — forward prices exceed spot prices; influences rolling costs and profitability
- [Backwardation](/backwardation/) — forward prices fall below spot prices; typical in stressed commodity markets
- [Forward Contract](/forward-contract/) — customized alternative to futures; less liquid but avoids rolling
- [Hedge Fund](/hedge-fund/) — professional managers often employ stack-and-roll techniques in commodity strategies
- [Expiration Contracts](/expiration-contracts/) — mechanics of settlement and contract death that necessitate rolling

### Wider context

- [Currency Risk](/currency-risk/) — major use case for stack-and-roll in FX hedging programs
- [Operational Risk](/operational-risk/) — rolling introduces execution and monitoring risk
- [Price Discovery](/price-discovery/) — why near-dated contracts are more liquid than far-dated
- [Volatility Smile](/volatility-smile/) — related to term structure of derivatives
- [Counterparty Risk](/counterparty-risk/) — exchanges mitigate this; alternative structures may not

</div>

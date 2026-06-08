---
title: "Strike Price Pinning"
description: "The tendency for stock prices to gravitate toward heavily-traded option strike prices on expiration day due to gamma hedging and market maker positioning."
keywords:
  - option expiration
  - gamma hedging
  - strike price
  - market maker
  - options trading
  - price discovery
image: "/svg/trading.svg"
---

*On the Friday that options expire, stock prices often cluster near round, heavily-traded [option](/option/) strike prices as if drawn by an invisible magnet. This phenomenon—known as strike price pinning—reflects the mechanics of how market makers and option sellers hedge their [gamma](/gamma/) risk, occasionally overriding the ordinary forces of price discovery.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Strike Price Pinning — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for options trading mechanics." />

<div class="wiki-infobox-caption">A documented end-of-week pattern shaped by the incentives of option hedgers.</div>

|   |   |
|---|---|
| **What it is** | Stock price clustering at heavily-traded [option strike prices](/strike-price/) on expiration dates |
| **Key driver** | Gamma hedging by option sellers and [market makers](/market-maker-trading/) |
| **When it occurs** | Near options expiration (typically Friday for weekly or monthly expirations) |
| **Strength** | Pronounced for liquid stocks with large open interest |
| **Also called** | Gamma pinning, pinning effect |

</aside>

## How gamma hedging creates the magnet

To understand strike price pinning, you must first grasp gamma. When a [market maker](/market-maker-trading/) sells a [call option](/call-option/), they assume the obligation to deliver shares at the strike price. To hedge this liability, they buy shares now—and as the stock price approaches the strike, the [delta](/delta/) of their short call changes, requiring them to adjust their hedge. On expiration day itself, the [gamma](/gamma/) (rate of delta change) becomes extreme near the strike, forcing rapid hedging trades.

A short call holder who has hedged by long stock will be long gamma—meaning they profit if the stock price stays near the strike, because it minimises their losses. If the stock threatens to move away from the strike, the [market maker](/market-maker-trading/) trades to pull it back. When many dealers are in similar positions at the same strike price, their collective hedging can exert meaningful pressure on the order book, effectively pinning the stock.

The effect is strongest at round strikes (100, 110, 120) and strikes where open interest is high, because these are where gamma concentration is largest. At a sleepy, illiquid strike, there is no pinning force.

## The battle between hedging and fundamentals

Strike price pinning is not universal. Its strength depends on a tug-of-war between two forces: the hedging demand of option dealers (which pulls toward the strike) and the underlying supply and demand for the stock itself. On a normal trading day, fundamentals dominate. But in the final hours of expiration, when time decay accelerates and gamma becomes overwhelming, the hedging mechanics can briefly overpower ordinary [price discovery](/price-discovery/).

This does not mean the stock's "true" price is being suppressed or artificially elevated. Rather, the equilibrium price reflects both the economic value and the temporary hedging flows. Once expiration passes, the magnet vanishes, and the stock is free to move again.

For stocks with massive options volume and deep open interest (think major technology stocks or large-cap indices), the effect can be visible: a stock will approach a round strike and seem to "stick" there despite news or order flow that might otherwise push it further. Retail traders sometimes observe this and conclude they are witnessing market manipulation. In a narrow technical sense, they are observing demand from hedging flow—which is a form of price pressure—but it is not manipulated in the sense of being intentionally engineered by one party. It is an emergent outcome of rational individual hedging decisions.

## Liquidity and concentration of open interest

Not every stock exhibits strike price pinning with equal intensity. The effect is strongest when open interest is concentrated at a single strike and the stock is large and liquid enough to absorb hedging flows without moving far. A small-cap stock with thin options trading might see zero pinning effect; the fundamentals and retail flow will push it wherever they wish.

Conversely, mega-cap stocks with deep options markets—particularly the [S&P 500 index](/sp-500-index/) and its [ETFs](/etf/)—sometimes show striking examples of pinning. On index expiration days, the [SPY ETF](/etf/) will sometimes sit uncannily close to a round strike (say, 450.00) in the final minutes, despite large equity orders in the broader market.

Market makers have also become more sophisticated at exploiting pinning for profit. Some use dynamic hedging algorithms that anticipate gamma clustering and adjust positioning in advance. Others use micro-structure strategies to detect whether the stock is "pinned" and trade the mean reversion when expiration passes.

## Is pinning predictable or exploitable?

Empirical research confirms that strike price pinning is real and statistically measurable, especially for equity index options. Studies show that stocks are disproportionately likely to close at or very near heavily-traded strikes on expiration dates, more often than would be expected by chance.

Whether this is exploitable is another question. Once a phenomenon becomes widely known, traders build it into their models. If a stock is pinned at 450.00, sophisticated traders anticipate the pin and adjust their own bids and offers. The edge that once existed by simply betting on the clustering effect gradually erodes. Modern option analytics platforms now explicitly flag when a strike is "pinned," turning what was once a subtle mispricing into a transparent fact that is already priced in.

For retail traders, the lesson is simpler: on options expiration days, be aware that normal price dynamics shift. A stock may behave in ways that seem disconnected from news or fundamental catalysts, because gamma hedging flows are temporarily large. This is not a conspiracy. It is predictable, transparent, and quickly reversed when expiration passes.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — the rate at which delta changes as stock price moves
- [Delta](/delta/) — the sensitivity of an option's value to a small move in the underlying stock
- [Option expiration](/expiration-date/) — when an option contract ceases to exist
- [Market maker](/market-maker-trading/) — dealers who provide liquidity by quoting bids and asks
- [Call option](/call-option/) — the right to buy a stock at a fixed price
- [Open interest](/expiration-contracts/) — the number of active contracts outstanding

### Wider context

- [Volatility smile](/volatility-smile/) — how implied volatility varies across strike prices
- [Options trading](/option/) — the broader market in derivative contracts
- [Intraday momentum](/intraday-momentum/) — short-term price patterns within the trading day
- [Monday effect](/monday-effect/) — systematic return patterns on Mondays
- [Price discovery](/price-discovery/) — how markets establish fair value for an asset

</div>

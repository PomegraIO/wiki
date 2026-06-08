---
title: "Weather Derivatives and Futures"
description: "Weather derivatives are contracts that pay based on temperature, rainfall, or other climate measurements, allowing energy and agriculture firms to hedge weather risk."
keywords:
  - weather derivatives
  - weather futures
  - degree-day contracts
  - heating cooling degree days
  - agricultural weather risk
  - energy hedging
---

*Weather derivatives and futures are financial contracts that pay out according to measurable weather outcomes—typically temperature or precipitation—rather than price movements. They let energy utilities, agricultural producers, and other weather-sensitive businesses lock in revenues or guard against climate-driven losses without buying or selling the underlying commodity.*

<div class="wiki-infobox">

<div class="wiki-infobox-title">Weather Derivatives — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Insurance against climate outcomes embedded in standardized contracts.</div>

|   |   |
|---|---|
| **Main types** | Degree-day futures, precipitation futures, wind speed contracts |
| **Primary users** | Utilities, agricultural firms, ski resorts, beverage companies |
| **Settlement** | Cash settlement based on government weather data |
| **Key index** | Heating degree days (HDD), cooling degree days (CDD) |
| **Exchanges** | CME Group, European Climate Exchange, OTC markets |
| **Typical payoff** | Fixed payout per degree above or below a strike threshold |

</aside>

## The Weather Risk Problem

A natural gas utility expects demand to rise when temperatures drop in winter. If the winter is unusually warm, heating demand collapses—revenue plummets even though the utility's costs stay fixed. An agricultural firm depending on corn sales faces the opposite exposure: a cool, wet summer boosts yields, but soft demand crushes prices; a hot, dry summer shrinks yields and can lift prices, but can't offset the lost bushels.

Neither firm can easily hedge these exposures with standard commodity futures or options, because the payoff depends on climate, not price. A corn farmer can sell [futures](/futures-contract/) to lock in a price, but a hot drought that halves yields while tripling prices leaves her worse off, not better. She wanted insurance against the yield collapse, not a leveraged bet on prices.

Weather derivatives exist to solve exactly this problem: they create a direct payoff tied to the weather itself, independent of commodity prices.

## Degree-Day Futures and How They Work

The most liquid weather contracts are **heating degree day (HDD)** and **cooling degree day (CDD)** futures traded on the [CME Group](/cme-group/). These measure cumulative deviations of daily average temperature from a 65 °F baseline.

- **Heating degree day:** If the daily average temperature is 50 °F, that day counts as 15 HDD. If it's 70 °F, no HDD accrues.
- **Cooling degree day:** If the daily average is 75 °F, that day counts as 10 CDD. If it's 60 °F, no CDD accrues.

Over a month or season, you sum all the daily degree days. A typical winter in Chicago might total 1,200 HDD; an exceptionally mild winter might deliver only 800. An HDD futures contract might specify a notional value of \$100 per degree day, so a 400-degree shortfall costs a hedger \$40,000.

A utility expecting to earn less revenue in a warm winter can buy HDD futures. If winter is warmer than expected and HDD come in low, the futures payout offsets the revenue loss. Conversely, if winter is cold and HDD run high, the utility loses on the hedge but gains on higher heating demand—the two move in opposite directions and create a natural hedge.

## Precipitation and Crop-Yield Contracts

Degree-day contracts work well for energy, but agriculture needs precipitation. Rainfall-indexed insurance and futures have proliferated, especially in the Midwest and Great Plains. A contract might specify a payout structure linked to seasonal precipitation at a specific weather station.

Example: A corn-growing operation buys a rainfall futures contract struck at 18 inches for the May-August season in central Iowa. Settlement is cash, based on NOAA precipitation data from a designated station. If rainfall turns out to be 15 inches, the grower receives compensation proportional to the 3-inch shortfall—perhaps \$500 per inch short, totaling \$1,500. The payout is independent of corn prices; it's purely weather risk.

Comparable contracts exist for frost dates, hail, wind speed, and snowfall. A ski resort buys snow futures; a harvesting equipment manufacturer buys rain contracts. The payoffs are stylized—a binary trigger (either it snows or it doesn't) or a continuous payout function—but the core logic is the same: paying for a climate outcome, not a market price.

## Why Settlement on Government Data Matters

Weather derivatives are cash-settled against official government measurements—typically NOAA weather station data in the US, or equivalent national services abroad. This eliminates counterparty risk on the weather itself: no one can dispute whether it actually rained 16 inches at Des Moines on July 15th. The number is public and immutable.

This also means weather contracts are not insurance in the regulatory sense, even though they function like insurance. The payout doesn't require proof of loss; the contract pays if the weather falls outside the specified band, period. A business with zero physical exposure to rain could theoretically buy rain contracts as a pure speculation.

## Basis Risk and Imperfect Hedges

The main limitation of weather derivatives is *basis risk*: your facility's weather might not match the index perfectly. A grain elevator at the edge of a county might experience a 2-inch rainfall that stations 15 miles away miss entirely. If your contract settles on the nearest official station but your property sits in a microclimate, you're exposed to that spatial mismatch.

This is why index insurance and derivatives work best for large, geographically diverse operations. A national utility serving multiple states can buy HDD contracts across several cities and smooth out local mismatches. A single farm at the edge of a weather station's coverage area faces more basis risk.

Some firms supplement weather derivatives with parametric insurance—policies that pay according to an index (like HDD), not actual loss. Others buy layered contracts: one on the primary station, another on a backup. The more localized the operation, the more basis risk bleeds through.

## Pricing Weather Derivatives

Weather derivatives aren't priced like commodity futures. There's no underlying physical asset to buy and store. Instead, prices reflect historical distributions and forward-looking forecasts. A winter HDD contract's price reflects expected HDD based on 30-year climate normals, adjusted for any current La Niña or El Niño pattern that might signal unusual temperatures.

The CME publishes standardized weather contracts with published settlement prices and open interest, making them transparent. But many weather derivatives trade [OTC](/over-the-counter-market/)—customized by maturity, geography, and payoff structure—and are priced by dealers using stochastic temperature models and historical volatility.

A utility might pay a higher price for an HDD floor (guaranteed minimum degree days) in a year when climate forecasters expect warmth; the dealer embedding that risk will demand a premium. Conversely, in a year with frost warnings, CDD contracts trade cheap because heating is expected.

## Real-World Use Cases

**Energy utilities** use HDD/CDD futures to lock in revenue. A power plant that generates more revenue on cold days buys HDD contracts; a generator serving summer air-conditioning demand buys CDD futures. The hedge is not perfect—electricity prices and fuel costs also move—but it removes the pure climate surprise.

**Agricultural cooperatives** pool rainfall contracts to protect member farmers. Instead of every farmer buying individual contracts (expensive, with high basis risk), the coop buys larger regional rainfall indices and passes payouts to members whose crops underperformed.

**Beverage and food companies** use weather derivatives to hedge commodity input risk. Coca-Cola's volume depends partly on warm summer temperatures; they can buy CDD calls to offset poor sales in an unusually cool summer. A beer maker faces opposite risk: demand drops in summer if it's too hot; they might buy CDD puts or HDD calls.

**Ski resorts and tourism** operators directly hedge snow and temperature. A resort buys snowfall futures; a tropical resort buys tropical cyclone derivatives. The payoff protects the business from seasonal shocks beyond management control.

## The Thin Liquidity Problem

Unlike commodity futures, which trade millions of contracts daily, weather derivatives have modest liquidity. Only a handful of CME contracts (HDD and CDD on major US cities, seasonal contracts) see consistent trading. Anything exotic—a precipitation contract on a small town, a hail derivative for a specific county—is a bespoke OTC deal with wider bid-ask spreads and higher dealer margins.

This illiquidity makes it expensive for small users to hedge. A small farm can't easily buy micro-precipitation contracts; the transaction costs would eat away the benefit. This is why parametric insurance and index insurance have grown alongside derivatives—they offer broader coverage without requiring direct participation in derivatives markets.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — standardized exchange-traded derivatives; weather futures follow the same settlement logic
- [Option](/option/) — weather caps and floors work similarly to options on temperature
- [Derivatives Hedging](/derivatives-hedging/) — using derivatives to manage non-price risks
- [Over-the-Counter Market](/over-the-counter-market/) — where customized weather derivatives trade
- [Basis Risk](/basis-risk/) — spatial and temporal mismatches between index and actual exposure

### Wider context

- Commodity Markets — energy and agricultural firms are the primary hedgers
- [Forward Contract](/forward-contract/) — OTC weather forwards precede standardized futures
- [Securitization](/securitization/) — catastrophe bonds and parametric insurance products bundle weather risks
- [Volatility Smile](/volatility-smile/) — weather volatility patterns similar to equity options
- Exchange-Traded Fund — some commodity ETFs embed weather derivatives

</div>

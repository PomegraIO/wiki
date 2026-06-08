---
title: "Futures Strip Pricing"
description: "Averaging commodity prices across consecutive futures expirations to lock in a multi-month or multi-year commodity cost."
keywords:
  - commodity hedging
  - futures strip
  - price averaging
  - rolling hedge
  - natural gas
  - crude oil
image: "/svg/commodities.svg"
---

*A **futures strip** is a sequence of consecutive [futures contracts](/futures-contract/) in the same commodity, purchased or sold together as a single package to hedge or project the cost of consuming (or producing) that commodity over multiple months or years. Instead of buying one crude futures contract, a refiner might buy January crude, February crude, March crude, and so on—the strip—locking in an average price path.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Strip Pricing — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodity trading and price formation." />

<div class="wiki-infobox-caption">A ladder of contracts rolled forward in time, averaging price risk across a production or consumption season.</div>

|   |   |
|---|---|
| **What it is** | Sequential contracts (Jan, Feb, Mar …) bought/sold together for continuous cover |
| **Also called** | "Stack", "strip hedge", "rolling contract" |
| **Typical span** | 12 months (annual strip), sometimes 3–5 years |
| **Pricing method** | Average of all constituent contract prices (simple mean, volume-weighted, or settlement basis) |
| **Used by** | Refiners, power plants, manufacturers, farmers, merchants |
| **Advantage** | Smooths price volatility, removes bet-on-one-month risk |

</aside>

## Why strips matter more than spot contracts

A refiner burning crude oil doesn't need crude just in January. It needs crude every month of the year. If it hedges by buying only the January contract, it is exposed to price moves in February, March, and beyond. A natural gas utility serving winter heating demand across December, January, and February can't hedge by buying only the December contract and hoping March warming arrives—its customers need gas heat all winter.

A strip solves this by linking multiple contracts into a single economic package. The refiner buys January crude, February crude, March crude, … December crude; the strip price is the simple average of all twelve monthly prices, or a weighted average reflecting how much crude the refiner expects to burn each month. The utility buys December, January, and February natural gas futures, locking in a winter-average gas price. Over a full year, consumption is smooth; the strip is the natural hedging instrument.

The beauty of strip pricing is that it removes a subtle speculative bet. A refiner that buys only January crude and waits to buy February contracts next month is betting that February crude will be cheaper than January; if it's more expensive, the refiner is caught short, pays more, and erodes profit margins. By buying the entire annual strip now, the refiner locks in an average and removes that timing risk.

## The strip as a valuation anchor

Industries that consume commodities continuously—utilities, refiners, chemical makers, flour mills—use the futures strip as a transparent market-based cost forecast. A power plant can calculate its cost of operations for next year by summing (or averaging) the prices in the 12-month electricity and natural gas futures strips. A fertiliser maker can estimate its ammonium nitrate margin by knowing the natural gas strip cost (its main raw material) and checking where customers will buy the finished product.

The strip price becomes the industry's baseline for negotiations. A refiner bidding to supply gasoline to an oil company for next year will quote a price tied to the crude strip, plus a fixed margin. A utility negotiating long-term customer rates will often reference the gas strip to justify rate increases or decreases. The strip is not a perfect forecast—it reflects current market sentiment, which can be wrong—but it's transparent, forward-looking, and market-made by thousands of traders.

## Building and trading the strip

A futures strip is built by accumulating contracts. If a refiner needs 100,000 barrels of oil per day for the next twelve months, it might:
- Buy 100,000 barrels of January WTI crude futures
- Buy 100,000 barrels of February WTI crude futures
- Buy 100,000 barrels of March WTI crude futures
- … and so on through December

If January WTI is $75/barrel, February is $74, March is $75.50, the refiner's 12-month average cost (before any seasonal adjustments) is close to $75. That's the strip price.

Traders also trade the strip itself as a single instrument. Some exchanges (the Chicago Mercantile Exchange, London Metal Exchange) quote 12-month energy and commodity strips directly. Buying or selling the "crude strip" is shorthand for simultaneously transacting a calendar spread (calendar spreads are the price differences between contracts, which together define the strip). If the strip price is $75 but a trader thinks the market is mispricing the out-months (believing February should be $73, not $74), she can buy the strip and simultaneously sell only February contracts, capturing her view on that one month while hedging the rest of the year.

This trading deepens the market and keeps strip prices efficient.

## Seasonal strips and rolling strips

Not all consumption is flat across a year. A natural gas utility consumes far more in winter (December, January, February) than summer. Its optimal hedge is a **seasonal strip**—buy more winter contracts (4 units) and fewer summer contracts (1 unit), reflecting actual demand. The average price of a seasonal strip is weighted toward winter months, which accurately reflects the utility's true cost of capital.

Many hedgers use a **rolling strip**, buying a 12-month strip and then, each month, selling the nearest expiring contract and buying one new contract 12 months out. This keeps the refiner or utility always hedged 12 months forward without constantly rebalancing. The rolling strip is elegant: the hedger is always executing the same strategy (buy and hold one year's worth) but the economic effect is continuous coverage that moves like a treadmill.

## Strip pricing dynamics

The shape of a [futures curve](/forward-curve-inversion/)—whether it's in [contango](/contango/) or [backwardation](/contango/)—determines whether a strip is expensive or cheap. If the market is in steep contango (far-month contracts much higher than nearby), the strip average will be pulled up; an annual strip will be pricier than a 12-month average of today's spot prices. If backwardation is deep (nearby contracts much higher than far months), the strip will be cheaper.

A refiner timing its hedging can sometimes benefit from curve shape. If crude is in steep backwardation (a supply crisis driving nearterm prices high), the refiner might delay hedging, betting that the crisis eases and the curve normalizes to contango. But this is speculation, not hedging; most responsible operators hedge against the consensus strip price and don't gamble on curve normalization.

Strip prices also compress and expand with volatility. In calm markets, the strip is narrow—each monthly contract is close to its neighbor, and the average is tight. In volatile markets (supply shocks, geopolitical crises), the strip widens: some months spike, others stay calm, and the average is less certain. Traders use the strip width as a rough gauge of market uncertainty.

## Strips and producer risk

Farmers and commodity producers use strips in the opposite direction. A corn farmer knows she will harvest 100,000 bushels in September. Rather than selling all at harvest and hoping spot prices are good, she can sell a spring/summer strip now, locking in an average price. Or she might sell September futures (the harvest contract) and also sell August futures to start de-risking before harvest. These sales are the farmer's strip hedge.

Miners, oil producers, and timber companies follow similar logic: sell a production strip forward, locking in multi-year revenue and allowing the business to forecast cash flow, refinance debt, and invest in capacity. A gold mine selling a three-year strip of future production at an average price of $1,900/oz can borrow against that locked revenue and finance expansion knowing the revenue stream is secure.

## Limitations and basis risk

A strip hedge assumes the refiner or utility will actually consume commodity evenly over twelve months. If demand collapses in month three (an economic downturn, a competitor's outage reducing local demand), the hedger is stuck with excess strip contracts, which it must unwind at market prices. Similarly, if a producer's output falls short (a mine fills with water, a farm weathers a drought), it owns strip contracts it can't fully deliver. This is basis risk—the mismatch between the hedge and the underlying economic reality.

Also, strips are based on standardised contracts at standardised locations. A milk processor might buy a natural gas strip for the Chicago Mercantile Exchange, but its actual gas is sourced from local utilities at regional pricing that doesn't perfectly track the CME strip. The difference—local basis—can cost or save money over a year.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the individual contracts that make up a strip
- [Spot-Futures Basis (Commodities)](/spot-futures-basis-commodity/) — the gap between cash and front-month futures, a component of strip economics
- [Nearby-deferred spread](/nearby-deferred-spread/) — the price gap between consecutive months, building blocks of the strip curve
- [Forward curve](/forward-curve-inversion/) — the full term structure of prices across all expirations
- [Contango](/contango/) — a normal curve where farther-out contracts cost more, raising strip averages
- [Backwardation](/contango/) — an inverted curve where nearby is expensive, lowering strip averages

### Wider context

- [Crude oil](/crude-oil/) — energy commodity frequently hedged via strips by refiners
- [Natural gas](/natural-gas/) — utilities and power plants routinely hedge via seasonal strips
- [Hedging](/interest-rate-risk/) — the core purpose of strip purchasing and selling
- [Price discovery](/price-discovery/) — how strips reveal market expectations of multi-month costs

</div>

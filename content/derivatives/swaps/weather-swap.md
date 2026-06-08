---
title: "Weather Swap"
description: "A derivative contract paying out based on temperature or precipitation, allowing weather-sensitive businesses to hedge revenue and cost volatility."
keywords:
  - weather derivative
  - temperature hedge
  - energy hedging
  - agricultural hedge
  - weather risk management
  - parametric insurance
image: "/svg/derivatives.svg"
---

*A **weather swap** is a derivative that exchanges a fixed payment for a floating payment based on a published temperature, precipitation, or other weather index, allowing utilities, insurers, farmers, and energy traders to insulate revenues and costs from climate volatility. Unlike insurance, which reimburses losses after they occur, a weather swap pays out whenever conditions breach a trigger, making it pure financial risk transfer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Weather Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A financial contract that decouples weather outcomes from business cash flows through index-based settlement.</div>

|   |   |
|---|---|
| **What it is** | [Swap](/swap/) on weather metrics, typically degree-days or rainfall; cash-settled |
| **Trigger metrics** | Heating degree-days (HDD), cooling degree-days (CDD), total precipitation, wind speed, snowfall |
| **Settle mechanism** | Cash only; pays out based on published weather station data |
| **Common users** | Utilities, energy retailers, farmers, ski resorts, outdoor event promoters, insurance firms |
| **Geography** | Defined by weather station or region—often major cities (NYC, Chicago, London) |
| **Duration** | Typically 1 winter or 1 summer season, or multi-year for long-term strategies |
| **Price driver** | Seasonal forecasts, climate patterns, historical volatility of the metric |

</aside>

## Degree-days and the core mechanic

The heart of most weather swaps is the degree-day: a measure of how far daily temperature deviates from a baseline (usually 65°F or 18°C). A heating degree-day (HDD) counts each degree the daily average falls below that baseline; a cooling degree-day (CDD) counts each degree it rises above. Over a winter, total HDDs in a region can range from 3,000 to 8,000 depending on whether it's mild or brutal. A swap on winter HDDs exchanges a fixed payment for a floating payment tied to the actual degree-days reported by a designated weather station (or an average of several stations).

The maths is straightforward. A utility might agree to pay a fixed 4,000 HDDs at US$10 per degree-day; the counterparty pays based on actual HDDs. If the winter is mild (2,500 actual HDDs), the utility owes 4,000 × $10 = $40,000 but receives 2,500 × $10 = $25,000, netting a $15,000 cost. If the winter is brutal (6,500 actual HDDs), the utility receives (6,500 − 4,000) × $10 = $25,000. The swap thus caps losses in a mild winter (when heating oil demand collapses and revenue drops) and caps gains in a cold winter.

## Why utilities and energy companies use them

An electricity retailer sells power at a fixed rate to customers. In a mild winter, heating demand evaporates, revenue falls, yet fixed costs remain. The retailer loses money. In a harsh winter, demand surges, revenue climbs, and the retailer profits—but only if it has hedged its wholesale power costs. A CDD swap on summer electricity provides the opposite hedge: a hot summer drives air-conditioning demand, boosting revenue, while a cool summer sinks it.

By purchasing a weather derivative, a utility locks in a minimum revenue floor regardless of temperature swings. This is not quite insurance (which pays only after a loss is realized and quantified); instead, a weather swap is parametric—it pays automatically based on a published index, the moment the weather station reports the data. There is no claims adjustor, no documentation of actual losses. This speed and transparency appeal to energy firms that cannot wait weeks for a claims settlement.

Natural gas distribution companies similarly use HDD swaps. A warm winter cuts gas sales and margin. A fixed payoff based on low actual HDDs compensates for the shortfall. The swap premium (the price the utility pays upfront) is far less than an equivalent insurance policy because there is no uncertainty about the loss—only about the trigger.

## Agricultural and seasonal businesses

Farmers and agricultural processors face yield and revenue volatility from rainfall, frost, and heat. A maize farmer might buy a swap on June rainfall in the US Corn Belt: if rainfall falls below a trigger (say, 3 inches for the month), the swap pays out, offsetting lost yields. A ski resort buys swaps on snowfall; a wine region on spring frost days. These are all revenue hedges: the business knows that a bad weather outcome will hurt sales, so it trades that financial risk to someone willing to take it.

Farmers cannot easily buy a futures contract on the price of rain itself (though precipitation futures do exist on a few exchanges). Weather swaps, instead, offer customizable indices and locations. A farm in Iowa can buy a swap on the National Weather Service station in Des Moines; one in Argentina can buy a rainfall swap for a Buenos Aires station. This geographic and metric flexibility makes swaps the primary tool for weather risk among smaller or regional players.

## Speculation and relative value

Just as with freight or interest rate swaps, weather swaps attract traders. A meteorologist or climate analyst might believe the consensus forecast for winter HDD is too low, implying mild conditions are overpriced in the swap market. The trader buys the swap (betting on more cold days) or sells it (betting on fewer). The swap becomes a pure financial bet on the accuracy of weather models, decoupled from any actual business exposure.

Large hedge funds and prop desks build weather models and trade swaps on systematic bases: mean-reversion (extreme winters are rare, so you sell weather protection betting on average winters), seasonal patterns, and climate trends. This speculative activity provides liquidity—counterparties to genuine hedgers—but it can also be destabilizing if model consensus breaks down during unusual weather events.

## Basis risk and location specificity

A swap is settled against a single weather station or an average of a few. If the contract references the Chicago airport station but your farm is 200 miles away, the local conditions might differ materially. This is basis risk: the hedge does not perfectly align with the underlying exposure. A mild winter in Chicago might be harsh 100 miles south, leaving your farm with low yields but no swap payout.

Choosing the settlement location is critical. Most swaps on major cities offer liquid markets; rural or smaller cities have thinner markets and wider bid–ask spreads. A firm in a remote area might have to accept poorer hedging efficiency or abandon the protection altogether. Additionally, weather data can be revised or corrected after the settlement date (a weather station might recalibrate), occasionally leading to disputes, though published indices mitigate this risk.

## The swap curve and seasonal structure

Weather swaps have a seasonal calendar structure: one for winter (November–March in the Northern Hemisphere), one for summer (May–September), and sometimes shoulder seasons. The "curve" is not a continuous yield curve like bonds; instead, it is a series of seasonal prices. A utility might buy a five-year strategy by purchasing swaps on five successive winters, each with its own premium.

The pricing reflects historical volatility and long-term climate patterns. A region with historically volatile winters (Minnesota) will have more expensive HDD swaps than a stable region (southern California). Climate change and long-term warming trends also factor in: as regions experience milder winters on average, HDD swaps become more expensive and CDD swaps cheaper, reflecting the shifting risk profile.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — the foundational derivative exchanging fixed for floating cash flows
- [Freight-swap](/freight-swap/) — a similar commodity-indexed swap for shipping costs
- [Forward-contract](/forward-contract/) — a non-standardized agreement for future delivery or cash settlement
- Parametric insurance — insurance that pays based on a pre-defined trigger rather than actual loss assessment
- Risk management — the broader framework of hedging operational and financial exposure
- [Carbon-swap](/carbon-swap/) — another commodity swap for environmental compliance costs

### Wider context

- Derivatives market — structure and regulation of weather and other swaps
- Commodity hedging — non-financial firms' use of derivatives to stabilize earnings
- Climate risk — the physical and financial risks of climate volatility to businesses

</div>

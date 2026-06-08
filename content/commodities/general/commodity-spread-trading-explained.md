---
title: "Commodity Spread Trading Explained"
description: "Commodity spread trading isolates relative value between two contracts by going long one and short another, avoiding directional bets on price levels."
keywords:
  - commodity spread trading
  - calendar spread
  - inter-commodity spread
  - crack spread
  - spread trading strategy
  - relative value trading
  - futures spreads
---

*A **commodity spread trade** profits from price differences between two related contracts—going long one and short another—rather than betting on absolute price direction. Common structures include calendar spreads (same commodity, different months), inter-commodity spreads (different commodities linked by economics), and crack spreads (refined products versus crude), all designed to isolate relative value when directional conviction is absent or when hedging a position.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Commodity Spread Trading — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Spreads reduce directional risk by pitting two contracts against each other.</div>

|   |   |
|---|---|
| **What it means** | Simultaneous long and short position in related commodity contracts |
| **Main types** | Calendar spreads, inter-commodity spreads, crack spreads, crush spreads |
| **Goal** | Capture relative-value differences, not absolute price direction |
| **Risk reduction** | Volatility lower than outright futures; basis risk remains |
| **Who uses it** | Hedgers, fund managers, commercial traders, retail speculators |
| **Where traded** | [Futures](/futures-contract/) exchanges (CME, ICE, NYMEX, etc.) |

</aside>

## Why Commodity Spreads Matter

Commodity spread trading exists because not all price moves are created equal. If you believe crude oil will rally but are uncertain about the timing or magnitude, an outright long crude position exposes you to unlimited downside. A spread—say, buying June crude and selling December crude—removes the directional bet almost entirely. You profit if the calendar relationship shifts (June strengthens relative to December), regardless of whether crude rises to $100 or falls to $60 overall.

This structure appeals to commercial traders hedging inventories, financial investors avoiding overnight risk, and funds seeking *relative-value* strategies uncorrelated to broad market direction. It also requires less capital and margin than outright positions, since the broker offsets the long and short legs.

## Calendar Spreads: Capturing Contango and Backwardation

A calendar spread—also called an **intramonth** or **time spread**—buys and sells the same commodity in different expiry months. In crude oil, you might buy June and sell September contracts simultaneously.

The trade profits from changes in the [forward curve](/forward-contract/). If the market is in [contango](/contango/) (near-term prices lower, far-out prices higher), a trader might sell the near month and buy the far month, betting the contango will flatten—a reversion to normal storage-cost relationships. If [backwardation](/backwardation/) exists (near-term higher, far-out lower), the opposite makes sense: buy near, sell far, expecting the curve to steep again.

These trades are often self-financing or low-margin because the long and short legs largely cancel in volatility terms. The profit or loss depends entirely on curve shape, not whether the commodity rises or falls.

## Inter-Commodity Spreads: Linked Economics

Inter-commodity spreads exploit economic relationships between two different commodities. The most famous is the **[crack spread](/commodity-spread-trading-explained/)** in energy:

- **3-2-1 crack spread**: Buy 3 barrels of crude, sell 2 barrels of gasoline + 1 barrel of heating oil, capturing the refinery margin (the profit refiners earn turning crude into products).

**Other common spreads:**

- **Crush spread** (soybeans): Buy soybean futures, sell soy oil + soy meal futures—reflecting the crush-plant margin.
- **Spark spread** (power and gas): Buy electricity contracts, sell natural gas contracts—the margin a power plant earns.
- **Heating oil vs. crude**: Refined product spreads that reflect transportation and processing costs.

These spreads are economically meaningful because they isolate the margin or value-add of a processing step. A refinery or crushing plant naturally hedges via crack or crush spreads to lock in operating margins.

## Basis Risk and Execution

Spread traders face **basis risk**—the risk that the two legs do not move in perfect correlation. A calendar spread might move against you if the curve steepens unexpectedly. An inter-commodity spread exposes you to idiosyncratic shocks in one commodity (e.g., crude surges on geopolitics while gasoline lags).

Execution is also non-trivial. Buying and selling two contracts at the same instant requires algorithms or broker assistance; slippage can erode thin margins. On less-liquid months or commodities, bid-ask spreads widen, making small trades uneconomical.

## When Spreads Outsmart Outright Bets

Consider a fund that believes oil inventories will decline but wants to avoid betting that crude prices will rise. An outright long is directional: it only profits if price appreciates. A calendar spread—buying near-month, selling far-month—profits if inventory declines and the curve flattens (near-month strengthens relative to far-out). If crude rallies on geopolitical shock, the spread lags but still holds; if crude falls on recession fears, the spread cushions the downside better than an outright long.

This is the strategic case for spreads: they transform a thesis from "crude will rise" into "the curve will flatten because of inventory dynamics." The latter is often more defensible and less exposed to unexpected macro shocks.

## Leverage and Drawdowns

Spreads require less [margin](/margin-call-forex/) than outright positions, tempting traders to layer on leverage. This can amplify losses if the correlation breaks—the very basis risk that spreads are supposed to minimize. A trader might use 5x leverage on a tight spread, then face a 20% drawdown in a day if one leg gaps against them.

Professional spread traders set tight [stop-losses](/support-and-resistance/) and size positions carefully, respecting that correlation is not causation.

## Seasonality and Mean Reversion

Many commodity spreads exhibit seasonal patterns. Heating oil, for instance, trades at a premium to crude in winter (fuel demand rises); the premium compresses in summer. A trader might sell the heating oil premium in autumn, betting it will compress, and reverse the position in spring. These trades profit from predictable rhythm rather than fundamental surprise.

Calendar spreads in agricultural commodities—corn, wheat, soybeans—also reflect planting cycles and harvest timing. Trading these patterns requires domain knowledge and patience.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — standardized agreement to buy or sell at a future date
- [Contango](/contango/) — forward prices higher than spot, typical for commodities with storage costs
- [Backwardation](/backwardation/) — forward prices lower than spot, common for peak-demand commodities
- [Forward Contract](/forward-contract/) — over-the-counter agreement to exchange commodity at future date
- [Basis Risk](/basis-risk/) — mismatch between price movements of hedging instruments and position being hedged
- [Hedging](/derivatives-hedging/) — offsetting risk in one position by taking opposing position in related instrument

### Wider context

- [Crude Oil](/crude-oil/) — petroleum benchmark and major energy commodity
- [Natural Gas](/natural-gas/) — gaseous hydrocarbon fuel, heavily traded in spreads
- [Corn](/corn/) — agricultural staple, liquid futures market
- [Market Timing](/market-timing/) — attempt to predict price direction, versus spreads' relative-value approach
- [Volatility Smile](/volatility-smile/) — options-pricing phenomenon relevant to spread-option strategies

</div>

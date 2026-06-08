---
title: "Contango vs Backwardation in Futures Markets"
description: "Contango vs backwardation futures explained: understand how futures prices curve up or down the contract term, and what it means for rolling positions."
keywords:
  - contango futures
  - backwardation futures
  - futures term structure
  - contango vs backwardation
  - rolling futures contracts
  - futures pricing
image: "/svg/derivatives.svg"
---

*The term structure of a **futures contract** is the shape of prices across expiration dates. In **contango**, distant months are more expensive than near months—a normal state driven by [storage costs](/futures-contract/) and [interest rates](/interest-rate/). In **backwardation**, near months are expensive and distant months cheaper, often signaling immediate supply tightness. For traders who roll contracts forward, the choice between the two determines whether each roll costs money or makes it.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Term Structure Shapes — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Whether you profit or lose money rolling forward depends on which structure you inherit.</div>

|   |   |
|---|---|
| **Contango** | Far months cost more than near months |
| **Backwardation** | Near months cost more than far months |
| **Driver of contango** | [Storage costs](/futures-contract/), [interest rates](/interest-rate/), financing |
| **Driver of backwardation** | Supply tightness or convenience yield; imbalance of supply and demand |
| **Roll cost in contango** | Investor sells cheap contract, buys expensive one; loses money |
| **Roll benefit in backwardation** | Investor sells expensive contract, buys cheap one; gains money |
| **Typical market state** | Most [futures](/futures-contract/) spend most of the time in contango |

</aside>

## What Is Term Structure?

Every [futures contract](/futures-contract/) has an expiration date. Crude oil trades December, January, February contracts and beyond. Corn futures span twelve months. At any given moment, the price of the December contract differs from the price of June, which differs from the December-of-next-year contract. This curve of prices across expiration months is called the **term structure** or the **forward curve**.

The shape of this curve determines whether an investor holding a position and rolling forward (closing the near-term contract and buying the next month) makes or loses money just from the mechanics of rolling, independent of actual price moves.

## Contango Defined

**Contango** occurs when futures prices increase with time to expiration. If December crude costs $50 and June costs $52, the market is in contango. The curve slopes upward.

Contango is economically rational and the default state. It reflects the cost of storing the commodity from now until the distant expiration. Crude oil sitting in a tank costs money: facility rent, safety measures, insurance, and financing. A refinery or trader who commits to buying the commodity today and holding it six months must pay that storage bill. The [futures](/futures-contract/) buyer implicitly accepts this cost, so the June contract must price higher than December.

The same logic applies to financial [futures](/futures-contract/). A Treasury bond [futures](/futures-contract/) contract trades at a price implied by the current bond price plus the [interest cost](/interest-rate/) of financing the bond for months. A long-term bond [futures](/futures-contract/) will typically price higher than a short-term bond [futures](/futures-contract/) because you are financing longer.

Contango is the norm. Commodities, equities, and [interest rates](/interest-rate/) typically trade in contango across expiration dates.

## Backwardation Defined

**Backwardation** is the opposite: near-term futures are expensive, and distant futures are cheap. If December crude costs $52 and June costs $50, the market is in backwardation. The curve slopes downward.

Backwardation signals immediate scarcity or urgency. A refinery with a sudden production breakdown and an empty inventory needs crude oil right now. It will pay a premium for near-term delivery rather than wait six months, pushing December prices above June. A farmer facing drought may need to hedge crop damage immediately, willing to pay dearly for near-term futures to lock in sales.

Backwardation often appears in commodity markets during supply disruptions. After a geopolitical shock that cuts oil production, crude futures go into backwardation. When an agricultural crop fails, grains enter backwardation as buyers scramble to secure near-term supplies.

## Rolling in Contango: The Negative Cost

Imagine you are a [hedge fund](/hedge-fund/) holding a long position in December crude at $50, and June is trading at $52. As time passes and December approaches expiration, you must close your December position and roll to June to maintain your exposure. You sell the December contract at $50 (let's say it stays there) and buy June at $52. On this roll alone, you lose $2 per barrel—without any move in the underlying market.

This cost is called the "roll yield" or "roll drag" in contango. Every month you roll, you sell a contract closer to expiration (cheaper) and buy one further out (expensive), pocketing a loss on the spread. Over a full year, rolling a long position in a steeply contangoing market can wipe out significant gains if the actual commodity price rises only modestly.

This is why the crude oil [ETF](/etf/) that tracks the front-month [futures](/futures-contract/) contract underperforms the actual spot commodity price during prolonged contango. The [ETF](/etf/) is constantly rolling into a steeper curve, bleeding value.

## Rolling in Backwardation: The Positive Yield

The reverse happens in backwardation. If December crude costs $52 and June costs $50, you sell expensive December and buy cheap June. The roll works in your favor; you pocket $2 per barrel without the commodity moving. This is a reward for holding the near-term contract and rolling forward.

Speculators and hedgers love rolling in backwardation markets. A producer of oil (who naturally holds a short position relative to the market) wins on every roll; the economics of the market push prices in its favor. A speculator long crude also benefits: the roll mechanics add return above any actual appreciation.

Over time, the market typically prices in this reward. If backwardation persists, traders will position themselves accordingly, and the magnitude of the roll benefit will shrink.

## Why Backwardation Reverses

Backwardation is often temporary. When supply disruptions ease, near-term scarcity diminishes, and the market reverts to contango. The December-expensive, June-cheap curve flips; near-month futures stop commanding a premium, and distant months become expensive again.

This reversion creates a profitable opportunity for contrarian traders. Buying far-month [futures](/futures-contract/) when they are deeply discounted (backwardation) and holding until the market normalizes can generate outsized returns once the curve flips back to contango.

Conversely, a hedge fund that shorts contangoing markets (selling near, buying far) when backwardation starts to emerge can capture the steepening curve before it fully plays out.

## Examples Across Commodities

**Crude oil** commonly trades in contango because storage is expensive and oil markets are usually well-supplied. However, during the 2022 energy crisis in Europe and the 2020 pandemic shock, crude dipped into backwardation as near-term demand surged and supplies tightened.

**Natural gas** is even more prone to backwardation because storage is costly and seasonal demand swings are violent. In winter, heating demand spikes and nearby futures soar above distant months. In summer, the curve inverts to contango.

**Agricultural commodities** ([corn](/corn/), wheat, soybeans) flip between contango and backwardation with crop cycles. Before harvest, when old-crop supplies are tight, backwardation often emerges. After harvest, ample new supplies push the market back into contango.

**Equity index [futures](/futures-contract/)** ([S&P 500](/sp-500-index/), Nasdaq) almost always trade in contango because you must finance the stock from now to settlement, and [interest rates](/interest-rate/) are positive (most of the time). Backwardation in equity [futures](/futures-contract/) is vanishingly rare and signals market distress or inverted [interest rates](/interest-rate/).

## The Convenience Yield

Economists use the term **convenience yield** to explain backwardation. It is the implicit benefit (like the "yield" on a bond) of holding the physical commodity right now rather than waiting for delayed delivery. A factory with zero inventory and desperate customer orders gets convenience from having crude today that is worth, say, $2 per barrel above the financial cost. This convenience is the spread between near and far [futures](/futures-contract/) prices.

Convenience yield is highest when the commodity is scarce or critical to immediate operations. It approaches zero in stable, well-supplied markets.

## Investors and Traders: Strategic Implications

For a pension fund using [futures](/futures-contract/) to [hedge](/derivatives-hedging/) long-term energy or commodity exposure, rolling in contango is a steady cost of [hedging](/derivatives-hedging/). Over decades, it compounds.

For a trader or speculator, contango and backwardation are profit opportunities. Curve trading—betting on the shape of the term structure rather than absolute price moves—is a major strategy. Traders buy the cheap (distant) and sell the expensive (near) contracts, locking in a spread regardless of price direction. When the curve flattens or inverts, the positions pay off.

For the producer of a commodity (a farmer, oil driller, or refiner), backwardation is a gift: the market rewards them for holding inventory now rather than selling far forward. In contango, it penalizes them.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — standardized derivative with multiple expiration months
- [Derivatives hedging](/derivatives-hedging/) — using [futures](/futures-contract/) to manage commodity or price risk
- [Backwardation](/backwardation/) — near-term premium; signals scarcity
- [Contango](/contango/) — far-term premium; reflects [storage costs](/futures-contract/) and financing
- [Interest-rate](/interest-rate/) — affects financing cost of holding commodities and bonds
- [Roll yield](/contango/) — gain or loss from closing one [futures](/futures-contract/) contract and opening the next month
- [Spot rate](/spot-rate/) — current price of the underlying commodity, as distinguished from [futures](/futures-contract/) prices

### Wider context

- [Crude oil](/crude-oil/) — energy commodity with pronounced contango and backwardation cycles
- [Natural gas](/natural-gas/) — volatile commodity with sharp seasonal curves
- [Corn](/corn/) — agricultural commodity with backwardation around harvest disruptions
- [S&P 500 index](/sp-500-index/) — equity [futures](/futures-contract/) typically in mild contango
- [Hedge fund](/hedge-fund/) — institutional investor that often trades commodity [futures](/futures-contract/) and curve shapes
- [ETF](/etf/) — exchange-traded fund tracking [futures](/futures-contract/); suffers roll drag in contango

</div>

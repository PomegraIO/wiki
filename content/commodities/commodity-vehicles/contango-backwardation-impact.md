---
title: "Contango & Backwardation Impact"
description: "How the shape of the commodity futures curve—with near-term contracts at higher (contango) or lower (backwardation) prices than distant contracts—erodes or boosts commodity ETF returns."
keywords:
  - contango
  - backwardation
  - commodity curve
  - ETF returns
---

*The **Contango & Backwardation Impact** describes how commodity [futures curve](/wiki/commodity-term-structure/) shapes determine whether a [commodity ETF](/wiki/commodity-etf/) experiences roll losses or roll gains. When the curve is in *contango* (near-term contracts cheaper than far-term), an ETF holding near-term contracts will face continuous losses as it rolls forward into more expensive contracts at expiration—a drag on returns that compounds over months and years. When the curve is in *backwardation* (near-term contracts more expensive than far-term), rolling into cheaper future contracts creates gains. For investors, understanding this mechanics is essential because curve shape alone can generate 2–5% annual headwinds or tailwinds, independent of the actual physical commodity price.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Contango** | Near contracts cheaper than far; rolling forward incurs loss |
| **Backwardation** | Near contracts more expensive than far; rolling forward incurs gain |
| **Commodity example** | Crude oil often in contango (storage + financing costs); natural gas often backwardated (supply-demand urgency) |
| **Roll yield** | The P&L impact of rolling from near to far contract at expiration |
| **Typical impact** | 2–5% annual headwind (contango) or tailwind (backwardation) |
| **Curve slope** | Steep contango (>5% curve) is especially punitive; steep backwardation (>5%) is generous |
| **Seasonal patterns** | Many commodities switch between contango/backwardation seasonally |

</aside>

## The mechanics: why the curve shape matters

A commodity ETF must hold a physical commodity position to deliver returns. Since physical storage is impractical at scale, ETFs hold [futures contracts](/wiki/futures-contract/) instead, typically the nearest-expiring contract (greatest liquidity). As that contract approaches expiration, the ETF must "roll" into the next-month contract by selling the expiring contract and buying the further-out contract.

The roll happens at different prices. Suppose crude oil trades at:
- 1-month contract: $75/barrel
- 2-month contract: $76/barrel

The ETF sells at $75 and buys at $76, locking in a $1/barrel loss on the roll. If the curve stays the same shape next month (2-month contract still $1 above 3-month), the next roll will again incur a $1 loss. Over a year of monthly rolls, that $1-per-month loss compounds to a meaningful drag.

## Contango environments and the historical norm

For most commodities, especially those with storage costs (crude oil, heating oil, copper, grain), the futures curve slopes upward: *contango*. Far-term contracts are more expensive because they embed:
- **Storage costs**: Warehousing, insurance, spoilage risk.
- **Financing costs**: The cost of borrowing capital to buy and hold the spot commodity for future delivery.
- **Convenience yield**: The benefit of holding the physical commodity (available for immediate sale, no delivery date risk).

In a normal contango environment (e.g., crude oil: 1-month at $70, 6-month at $76, 12-month at $80), the curve is gradually upward-sloping. A commodity ETF using monthly rolls will bleed 0.5–1.5% per month rolling from near to far, or 6–18% annualized. This is a *tax on leverage*: the higher price at which you must buy far-term contracts is the market's way of charging for storage and financing.

The most notorious contango drag occurred in [commodity ETFs](/wiki/commodity-etf/) around 2010–2011, when structural contango in crude oil and natural gas was exacerbated by a glut of investment inflows. Investors noticed that the [USCI index](/wiki/commodity-etf/) (US Commodity Index) and similar trackers were declining even as physical commodity prices were stable or rising. The culprit: contango roll losses dwarfed any spot-price gains. A crude oil ETF down 10% in a year when crude prices were flat would have experienced ~10% roll losses from contango.

## Backwardation and the roll gain

Occasionally, the futures curve inverts: *backwardation*. Near-term contracts trade at a *premium* to far-term contracts. This happens when:
- **Supply urgency**: Immediate demand (a refinery or industrial customer) is willing to pay a premium to have the commodity now rather than waiting for future delivery.
- **Crisis or dislocation**: A sudden supply shock (war, hurricane, pipeline sabotage) creates hoarding behavior and spot-market tightness.
- **Low stock levels**: Inventory is depleted, making spot commodity scarce and valuable.

In backwardation (e.g., natural gas: 1-month at $4, 2-month at $3.50), the ETF sells the near contract at $4 and buys the far at $3.50, *gaining* $0.50/contract on the roll. Repeated monthly over a steep backwardation curve, this generates 1–3% monthly tailwinds, or 12–36% annualized gains *just from rolling*.

The oil market experienced dramatic backwardation in April 2020 when demand collapsed (COVID lockdowns) but storage filled up, and then again in 2022 when Russia's invasion of Ukraine created supply panic and backwardation spiked. Commodity ETFs holding positions through deep backwardation experienced stellar returns partially independent of physical oil prices rising.

## Seasonal patterns in curve shape

Many commodities exhibit *seasonal* shifts in curve shape:

- **Agricultural commodities** (wheat, corn, soybeans): Backwardation after harvest (abundant supply) then gradual shift to contango as the crop is consumed and storage builds; sharp contango just before the next harvest.
- **Natural gas**: Backwardated in winter (heating demand, cold snaps) and contango in summer (cooling demand muted, production abundant).
- **Crude oil**: Typically gentle contango, but can swing to backwardation during OPEC supply cuts or geopolitical events.

Sophisticated commodity traders exploit these seasonal patterns: buying into mild contango in summer when it is relatively flat, and selling into steeper contango before winter demand tightens the curve.

## Curve shape and spot price movement: which dominates?

An ETF's return has two components:
1. **Spot-price return**: If crude goes from $70 to $75, that is +7%.
2. **Roll yield**: The P&L from rolling forward through contango or backwardation.

In strong commodity bull markets (spot up 20%+), roll yield is often secondary; the price move dominates. But in trendless or consolidating markets, roll yield can dominate returns. An ETF in a flat-price year but steep contango year could finish down 5–8%, while an ETF in a flat-price year but steep backwardation could finish up 3–5%.

The relationship is not always additive. In severe contango, large inflows to commodity ETFs can exacerbate the curve slope by creating supply-demand imbalances in futures markets. Conversely, steep backwardation attracts commercial hedgers and reduces ETF demand, sometimes flattening the curve.

## Impact on different commodity ETFs

**Broad commodity index funds** (holding gold, oil, gas, agriculture, metals) experience diversified curve impacts: gold and silver have little storage cost (backwardation rare), while crude and natural gas experience larger contango/backwardation swings.

**Single-commodity ETFs** (just crude oil, just natural gas) amplify the curve effect. A 3-month rolling crude ETF in a 5% annualized contango environment will underperform spot crude by roughly that 5% (minus fees), all else equal.

**Inverse commodity ETFs** benefit from steep contango (they profit from downward roll losses) and suffer in backwardation. A 3x inverse crude oil ETF during the 2020 spike in backwardation was wiped out, not because crude prices fell, but because it was short the backwardated curve and losing money on every roll.

## Strategic responses: curve-aware investing

Institutional investors manage contango/backwardation risk by:

- **Switching roll strategies**: Shifting to *longer-dated* contracts (rolling every 3–6 months instead of monthly) to reduce roll frequency and compress the curve's impact.
- **Spot market alternatives**: Holding physical commodity (gold, oil in storage) or sourcing from suppliers rather than futures if contango is too steep.
- **Curve overlays**: Using [options](/wiki/barrier-option/) or [swaps](/wiki/commodity-swap/) to hedge curve risk separately from spot risk.
- **Seasonal timing**: Shifting exposure into periods of favorable curve shape (backwardation) and reducing into steep contango.

The recognition of contango/backwardation impact has also led to the growth of *customized commodity indices* that use different roll rules (e.g., 30% weight to the front month, 30% to the 2nd month, 20% to the 3rd month) to reduce concentration on the single rollover date and smooth out curve impacts.

<div class="wiki-seealso">

### Closely related
- [Contango](/wiki/contango/) — Near-term contracts cheaper than far-term; roll losses
- [Backwardation](/wiki/backwardation/) — Near-term contracts more expensive than far-term; roll gains
- [Commodity Term Structure](/wiki/commodity-term-structure/) — The shape of the futures curve and its drivers
- [Commodity Futures Rolling](/wiki/commodity-futures-rolling/) — How ETFs and traders manage expiration and rolls

### Wider context
- [Commodity ETF](/wiki/commodity-etf/) — Funds that track commodity price indices
- [Commodity Swap](/wiki/commodity-swap/) — An alternative to futures for commodity exposure
- [Roll Yield](/wiki/roll-yield/) — The P&L impact of rolling futures contracts forward
- [Basis Risk](/wiki/basis-risk/) — Mismatch between futures prices and spot prices

</div>

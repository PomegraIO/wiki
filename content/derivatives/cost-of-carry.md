---
title: "Cost of Carry"
description: "Cost of carry is the total cost of holding an underlying asset from today until a future date, including storage, financing, and insurance, which determines futures prices."
keywords:
  - cost of carry
  - carrying cost
  - futures pricing
  - storage
  - financing
image: "/svg/derivatives.svg"
---

*The **cost of carry** is the sum of all costs (and sometimes benefits) of owning and holding an underlying asset from today until a future settlement date. It includes storage fees, insurance, financing costs (interest), and may subtract convenience yield or dividend income. The cost of carry directly determines the [forward-contract](/forward-contract) price and the [basis](/basis/) between spot and [futures contract](/futures-contract) prices. Higher cost of carry raises futures prices above spot prices, creating [contango](/contango/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Carry — key facts</div>

<img src="/svg/derivatives.svg" alt="Components of holding an asset over time" />

<div class="wiki-infobox-caption">Cost of carry determines futures premium.</div>

|   |   |
|---|---|
| **Components** | Storage, insurance, financing, convenience yield |
| **Pricing formula** | Fwd = Spot × e^(r×T + storage) |
| **Applies to** | Commodities, bonds, currencies, stocks |
| **Positive carry** | Costs exceed benefits → contango |
| **Negative carry** | Benefits exceed costs → backwardation |
| **Financing rate** | Key component for stocks, currencies |
| **Storage** | Oil, metals, agricultural commodities |
| **Convenience yield** | Subtracted from cost (benefit of immediate supply) |
| **Dividend yield** | Subtracted for dividend-paying stocks |

</aside>

## Components of cost of carry

**Storage:** Physical cost of holding the asset. Oil in a tank, gold in a vault, wheat in a silo. Typically a fixed percentage of asset value per year or a fixed absolute fee.

**Insurance:** Risk of loss or damage during storage. As a percentage of value.

**Financing:** Interest cost of borrowing money to purchase the asset. If you buy oil at $70 and borrow at 2% annual rate for 6 months, the financing cost is roughly $0.70.

**Convenience yield:** Benefit of holding the physical asset (not applicable to all assets). A refinery benefits from immediate oil supply; this reduces the effective cost of carry.

**Dividend yield:** For stocks paying dividends, the [dividend](/dividend) reduces the cost of carry. Owning stock instead of buying a [future](/futures-contract) lets you collect the dividend.

## Futures pricing and carry

The relationship is:

Futures Price = Spot Price × e^(r×T + storage − convenience_yield − dividend)

For a stock with 2% annual financing cost, 0% storage, 2% dividend yield, and T = 0.5 years:

Futures = Spot × e^((0.02 − 0.02) × 0.5) = Spot

The futures price equals spot; no [contango](/contango/) or [backwardation](/backwardation/) because carry components cancel.

For crude oil with 2% financing and 1% annual storage:

Futures = Spot × e^((0.02 + 0.01) × 0.5) = Spot × e^(0.015) ≈ Spot × 1.0151

Futures are 1.51% higher than spot—[contango](/contango/).

## Carry trade: arbitrage opportunity

When the [basis](/basis/) (futures − spot) exceeds the cost of carry, an arbitrage is available:

1. Buy spot (e.g., crude at $70)
2. Store and finance for 6 months
3. Sell 6-month futures at $71.50
4. Total cost: $70 + storage + financing = ~$70.70
5. Revenue: $71.50
6. Profit: $0.80/barrel (riskless)

Sophisticated traders exploit these missprices, keeping futures prices aligned with cost-of-carry.

## Negative carry and backwardation

When convenience yield exceeds financing + storage, carry is negative. This creates [backwardation](/backwardation/): futures prices fall as you move forward in time.

Example: Oil crisis; immediate oil is scarce and commands a premium. Convenience yield (value of immediate supply) is $5/barrel. Financing + storage is $1/barrel. Net carry is -$4/barrel. Backwardated prices reflect this.

## Stocks vs. commodities

**Stocks:** Cost of carry is mostly financing cost minus [dividend](/dividend) yield. No storage or convenience yield.

**Commodities:** Cost of carry includes storage and convenience yield, creating [contango](/contango/) or [backwardation](/backwardation/) depending on supply-demand.

## See also

<div class="wiki-seealso">

### Closely related

- [Basis](/basis/) — spot-futures difference; driven by carry
- [Contango](/contango/) — positive carry → higher futures
- [Backwardation](/backwardation/) — negative carry → lower futures
- [Futures contract](/futures-contract/) — prices reflect carry
- [Forward contract](/forward-contract/) — carry in forward pricing

### Components

- Storage — physical holding cost
- [Financing](/interest-rate/) — borrowing cost
- Insurance — risk cost
- [Convenience yield](/backwardation/) — benefit of immediate ownership
- [Dividend](/dividend/) — benefit for stock carry

### Arbitrage and trading

- [Cash-and-carry](/basis/) — exploit carry mispricing
- [Curve trades](/alpha/) — betting on carry changes
- [Rolling](/basis) — managing carry in positions
- [Spread trading](/alpha) — comparing carry across maturities

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Futures contract](/futures-contract/) — where carry manifests
- [Market efficiency](/stock-market/) — carry arbitrage enforces fairness

</div>

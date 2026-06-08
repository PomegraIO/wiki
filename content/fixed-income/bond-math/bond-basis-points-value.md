---
title: "Basis Point Value of a Bond: Definition and Calculation"
description: "Basis point value (BPV) or DV01 measures the dollar price change for a one-basis-point yield move, essential for hedging and risk management."
keywords:
  - basis point value bond
  - DV01 calculation
  - bond price sensitivity
  - basis point value formula
  - fixed income risk
image: "/svg/fixed-income.svg"
---

*The **basis point value** of a bond—also called DV01 (dollar value of one basis point) or price value of a basis point (PVBP)—is the dollar amount the bond's price changes when its yield moves by exactly one basis point. For a $10 million position in a 10-year bond with a basis point value of $850, a one-basis-point yield rise costs the bondholder $8,500. It is the primary metric traders use to quantify price risk and to dimension hedges.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis Point Value — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One basis point of yield move, scaled to the position size, reveals the daily risk.</div>

|   |   |
|---|---|
| **Abbreviations** | DV01, PVBP, basis point value, BPV |
| **Definition** | Dollar loss per 1 bp yield rise (or gain per 1 bp fall) |
| **Formula** | BPV ≈ Price × [Duration / 10,000] |
| **For $1M position** | Multiply the bond's BPV by the notional position size in millions |
| **Usage** | Hedging, position sizing, portfolio risk reporting |

</aside>

## Definition and intuition

A **basis point value** translates the [duration](/duration/) of a bond into a dollar amount. Duration tells you the percentage change in price per 1% yield move; basis point value tells you the absolute dollar change per 0.01% (one basis point) yield move.

If a bond has a [duration](/duration/) of 5 years and you own $1 million face value, then a 1% (100 basis point) yield fall lifts the price by approximately 5%, or $50,000. Dividing by 100 basis points, each basis point is worth about $500. That is the basis point value for a $1 million position.

The term **DV01** (dollar value of one [basis point](/basis/)) is synonymous and is the standard in trading floors and risk management teams. Some firms prefer PVBP (price value of a basis point), but the concept is identical.

## The calculation

For a bond with price P and [duration](/duration/) D (in years), the basis point value per $1 notional is:

**BPV = P × D / 10,000**

where 10,000 is the conversion factor from percentage basis points (1% = 100 bp, so 0.01% = 1 bp = 0.0001 in decimal) to dollars.

**Example**: A 10-year Treasury note is priced at 98.50 with a [duration](/duration/) of 8.2 years.

BPV per $1 notional = 98.50 × 8.2 / 10,000 = 0.008077, or about $0.008077 per dollar of face value.

For a $10 million position: BPV = $0.008077 × 10,000,000 = $80,770.

If yields rise one basis point, the position loses approximately $80,770.

## Why "approximately"

The formula is an approximation because it assumes the price-yield relationship is linear—exactly what [duration](/duration/) does. For very small yield moves (1–5 basis points), the approximation is excellent. For larger moves, [convexity adjustment](/bond-convexity-adjustment/) becomes material.

In practice, traders use the BPV formula for daily risk reporting and for rough hedging. For precisely hedged positions or for moves larger than 50 basis points, they recalculate BPV using the exact price formula or account for [convexity](/bond-convexity-adjustment/).

## DV01 vs. basis point value: no real difference

The terms are interchangeable. DV01 emphasizes the "dollar value" perspective and is common in quantitative finance and bank trading. Basis point value or PVBP is more common in insurance and pension fund contexts. Both mean the same thing: the price change per one basis point.

## Practical use: hedging and position sizing

A portfolio manager holding a large position in 10-year bonds knows the [duration](/duration/) is about 8 years. To hedge interest-rate risk, the manager might short 10-year Treasury futures. Each Treasury future contract has its own DV01.

If the bond position has a DV01 of $100,000 and each futures contract has a DV01 of $8,000, the manager shorts 100,000 / 8,000 = 12.5 contracts to neutralize interest-rate risk. A rise or fall in yields moves the bond position and futures position by roughly equal and opposite dollar amounts.

This [duration](/duration/)-matching strategy is called a **DV01-neutral hedge** and is the foundation of fixed-income portfolio management.

## Bond basis point value vs. other instruments

**Treasury futures**: Each contract represents $100,000 notional (or $200,000 for some contracts). The DV01 of a contract is published daily by exchanges.

**Bond ETFs**: The fund publishes average [duration](/duration/), and you multiply by the fund's price and holdings to get the DV01 per share.

**Interest-rate swaps**: The notional is typically $1–10 million. A 5-year swap with $1 million notional and a [duration](/duration/) of 4 years has a DV01 of about $400.

**Options on bonds**: The DV01 of a bond option is its [delta](/delta/) times the DV01 of the underlying bond.

## Relationship to yield-to-maturity and convexity

A bond's basis point value depends on:
1. **Price**: higher prices mean higher DV01
2. **[Duration](/duration/)**: longer [duration](/duration/) means higher DV01
3. **Yield level**: lower yields (lower discount rates) mean longer [duration](/duration/) and higher DV01

For two bonds with the same maturity but different coupons, the lower-coupon bond has a longer [duration](/duration/) and thus higher basis point value. A zero-coupon bond (all cash at maturity) has the longest [duration](/duration/) for its maturity and the highest basis point value.

[Convexity](/bond-convexity-adjustment/) becomes material when yields move by 50+ basis points. For a 200-basis-point yield rise, the actual price change exceeds the DV01-based forecast, but traders still use DV01 for first-order hedging and reporting.

## Real-world example: a $10 million corporate bond trade

**Position**: $10 million face value of a 7-year corporate [bond](/bond/).
**Price**: 99.50
**[Duration](/duration/)**: 6.5 years

Basis point value per $1: 99.50 × 6.5 / 10,000 = 0.0064675
Basis point value for $10 million: $64,675

If yields on this bond class rise 5 basis points, the position loses approximately $64,675 × 5 = $323,375.

If the trader wants to hedge this, they might short Treasury futures or enter a pay-fixed [interest-rate swap](/interest-rate-swap/). The hedge size is chosen so that the hedge's basis point value matches the bond's basis point value—then the combined portfolio has a near-zero DV01 and is insulated from small yield moves.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — effective maturity measure; the foundation for basis point value
- [Bond](/bond/) — coupon, maturity, and price mechanics
- [Convexity-Adjustment](/bond-convexity-adjustment/) — corrects basis point estimates for large yield moves
- [Yield-to-Maturity](/yield-to-maturity/) — the discount rate that determines duration and basis point value
- [Interest-Rate-Risk](/interest-rate-risk/) — basis point value quantifies this risk

### Wider context

- [Par-Yield-vs-Spot-Rate](/par-yield-vs-spot-rate/) — discount rate concepts that drive basis point value
- [Flat-Price-vs-Full-Price](/flat-price-vs-full-price/) — pricing conventions; basis point value uses clean prices
- [Bond-Etf](/bond-etf/) — ETF shares have per-share basis point values
- [Hedge-Fund](/hedge-fund/) — use basis point value to size relative-value trades and hedges
- [Treasury-Bond](/treasury-bond/) — the most liquid bond market; basis point values are highly standardized

</div>

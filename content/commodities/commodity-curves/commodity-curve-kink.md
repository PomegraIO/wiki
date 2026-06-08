---
title: "Commodity Curve Kink"
description: "A sharp discontinuity in a commodity forward curve at a specific maturity, caused by seasonal storage transitions or contract structural changes."
keywords:
  - commodity forward curve
  - curve discontinuity
  - seasonal storage
  - contango kink
  - futures curve structure
image: /svg/commodities.svg
---

*A **commodity curve kink** is a sharp, localized bend or discontinuity in the [forward curve](/forward-contract/) at a particular delivery month, where the slope abruptly changes—often steepens or flattens. It reflects real supply–demand transitions (seasonal inventory shifts, harvest cycles, production shutdowns) or trading mechanics (contract rollover, storage cost cliffs). Rather than a smooth upward [contango](/contango/) or downward [backwardation](/backwardation/), the curve stutters.*

## Why kinks appear: the storage calendar

The most vivid kink arises from seasonal shifts in the cost of holding physical inventory. Crude oil stored through winter months may cost significantly more to hold than summer supply, because heating-fuel demand and refinery capacity constraints raise storage premiums. In agricultural markets, a harvest in autumn creates a glut; storage costs peak as grain houses fill to bursting, then fall sharply after drawdown. The forward curve "kinks" at the month where storage necessity flips from acute to mild—the curve steepens into that month, then flattens beyond it.

This is not arbitrary pricing error. It reflects [implied storage rates](/implied-storage-rate/) backed out from the curve slope. When storage becomes cheaper, the contango (the price rise between months) contracts. The kink is where that transition happens, visible as a visible shoulder or elbow in the curve.

## Contract structure and roll mechanics

Kinks also arise from the mechanics of how futures are quoted and traded. Many commodity markets have a single liquid benchmark contract—say, Brent crude delivery in three months—with thinner trading and wider [bid-ask spreads](/bid-ask-spread/) in further-out months. When traders rotate positions between two contracts at quarter-end, or when one contract approaches expiration and trading "rolls" to the next month, the curve can bend.

In some markets, contract size or specifications change at certain maturities. A kink may mark the boundary between, say, a heavily traded quarterly contract and thinly traded monthly contracts beyond it, creating a mechanical supply-and-demand kink in liquidity rather than in true storage economics.

## Reading the kink: what it tells you

A sharp kink is a gift to the [curve-aware trader](/contango/). It identifies inflection points where the market's supply–demand story shifts. 

- **Steepening into a month**: shortage fears, capacity constraint, or mandatory storage accumulation. Hedgers willing to pay a premium to secure distant supply.
- **Flattening beyond a month**: oversupply, unwinding of seasonal bulges, or a drop in marginal storage cost. Far-dated supply is plentiful.

Algorithms that trade [calendar spreads](/commodity-forward-curve-bootstrapping/) watch for kinks—they are opportunities to monetize the curve's shape or to hedge inventory-roll risks. A producer worried about a seasonal storage crunch can sell the steep part of the curve and buy the flat part, locking in a storage-cost saving if the kink shifts.

## Distinguishing kinks from other curve shapes

A kink is not the same as a simple [inverted curve](/yield-curve/) (backwardation). Backwardation is a market-wide phenomenon—all months trade below spot or in steady decline. A kink is a *local* bend within a broader shape. You might see a gently upward contango that suddenly *steepens* at month 6, then flattens again by month 9—that's a kink, not an inversion.

Nor is a kink necessarily a [curve discontinuity](/forward-contract/) in price per se. It is a discontinuity in *slope*—a point where the first derivative (change in price per month) jumps. Seasoned traders spot kinks in curve charts as the visual equivalent of a corner or elbow in what would otherwise be a smooth line.

## Why risk managers care

The kink matters because it tells you where the marginal unit of supply or storage becomes constraining. If you [hedge](/hedge-fund/) a commodity position and the kink moves—storage costs drop, harvests flush supplies, or production restarts—the curve's shape can shift, and your [hedge ratio](/delta/) must adjust. A calendar spread that looked profitable can evaporate if the kink flattens.

This is particularly acute in [options](/option/) on spreads. An option on the calendar spread between two maturities can be worth a great deal if a kink is near the strike. If fundamentals shift and the kink moves, the option's value may swing wildly, even if the overall curve level is stable.

## Kinks in [bootstrapping](/commodity-forward-curve-bootstrapping/) and curve fitting

When building a smooth [forward curve](/forward-contract/) from discrete futures prices, practitioners face a choice: fit a smooth spline, or preserve the kink? A smooth spline erases the discontinuity, which is aesthetically pleasing but obscures real market information. Some risk systems preserve known kink points (e.g., contract rollover dates or seasonal calendar dates) as anchor nodes in the fit, allowing the curve to bend at those points while remaining smooth elsewhere.

The kink is not an error in the data—it is often the most honest part of the curve. Ignoring it means missing a significant trade opportunity or hedging subtlety.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — persistent upward slope in the forward curve, where further months trade at a premium
- [Backwardation](/backwardation/) — inverted curve where near months trade above far months
- [Implied Storage Rate](/implied-storage-rate/) — the physical storage cost backed out from observed contango slopes
- [Forward Curve Bootstrapping (Commodities)](/commodity-forward-curve-bootstrapping/) — methods for constructing continuous curves from discrete futures prices
- [Time Spread Option (Commodities)](/time-spread-option-commodity/) — an option on the calendar spread, sensitive to curve kinks
- [Commodity Forward Curve](/forward-contract/) — the full shape of commodity prices across delivery months

### Wider context

- [Futures Contract](/futures-contract/) — standardized exchange contracts at discrete expiration months
- [Forward Contract](/forward-contract/) — the underlying economic concept of future delivery
- [Volatility Smile](/volatility-smile/) — analogous local distortion in the options implied-volatility surface
- [Sensitivity Analysis (Valuation)](/sensitivity-analysis-valuation/) — assessing how curve shifts affect portfolio value

</div>

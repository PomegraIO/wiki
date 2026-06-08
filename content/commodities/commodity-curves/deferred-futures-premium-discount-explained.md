---
title: "Why Deferred Futures Trade at a Premium or Discount to Spot"
description: "Understand why distant commodity futures trade above or below spot price. Learn how financing, storage, convenience yield, and seasonality set the forward premium."
keywords:
  - deferred futures premium discount
  - commodity forward premium
  - contango backwardation spot price
  - storage costs convenience yield
  - distant futures pricing
image: /svg/commodities.svg
---

*Distant commodity [futures](/futures-contract/) contracts do not trade at today's spot price; they trade higher (a **premium**) or lower (a **discount**). That difference is determined by the cost of financing, the charge for physical storage, the **convenience yield** from holding the commodity itself, seasonality, and expected supply-demand shifts. Understanding these drivers explains why a crude oil forward might be $2 above today's price while a grain forward is $1 below.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Premium & Discount — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Forward price = Spot + Storage + Financing − Convenience Yield ± Seasonality ± Risk Premium</div>

|   |   |
|---|---|
| **Premium** | Forward price above spot (typical in [contango](/contango/) markets) |
| **Discount** | Forward price below spot (typical in [backwardation](/backwardation/) markets) |
| **Storage cost** | Rent, insurance, spoilage for holding the physical good |
| **Financing cost** | Interest rate to fund the purchase and carry; often moves with central bank rates |
| **Convenience yield** | Benefit of holding physical (emergency supply, operational flexibility, avoided shortages) |
| **Seasonality** | Winter heating demand, harvest cycles, industrial patterns push seasonal prices higher or lower |

</aside>

## The cost-of-carry framework

The fundamental pricing rule for commodity forwards is called **cost of carry**. It states:

**Forward Price = Spot Price + Financing + Storage − Convenience Yield**

If you agree today to buy crude oil for delivery three months hence, you must account for three costs:

1. **Financing.** You need to fund the purchase. If you borrow at 4% annual interest, three months of interest on a $75/barrel purchase (for a small barrel cost) is real money.

2. **Storage and insurance.** The physical barrel must be stored, insured, and protected against spoilage or theft.

3. **Convenience yield (offset).** Conversely, the seller—or whoever holds the physical—gets a benefit: the ability to access the commodity immediately if an emergency arises, or to sell it opportunistically if prices spike. This benefit is the **convenience yield**, and it reduces the forward price.

The forward price is not arbitrary; it must equal spot plus net carry costs, or traders can arbitrage it away.

## Contango: forwards trading at a premium

When forward prices rise as you move farther into the future, the market is in **[contango](/contango/)**. This is the normal state of most commodity markets.

**Why?** Because financing and storage typically exceed convenience yield. If you lock in a purchase three months forward at a premium, you are paying for:

- Three months of interest to finance the purchase.
- Three months of warehouse rent, insurance, sampling, and spoilage allowance.

The convenience yield (the value of having physical on hand) is usually small relative to these costs, so forwards rise above spot.

**Example:** Crude oil spot is $75/barrel. Three-month financing at 4% annual = ~$0.75. Storage and insurance = ~$0.20. Convenience yield = ~$0.10. Three-month forward = $75 + $0.75 + $0.20 − $0.10 = **$75.85/barrel**.

The forward is a premium of $0.85 to spot, reflecting net carry cost.

This is common for:

- **Metals** (gold, copper) where storage is abundant and convenience yield is minimal.
- **Crude oil and refined products** where storage capacity is plentiful and operational demand is steady.
- **Grains** after harvest, when inventory is full and carry-forward to next season is merely a storage exercise.

## Backwardation: forwards trading at a discount

When forward prices fall as you move farther into the future, the market is in **[backwardation](/backwardation/)**. Forwards trade at a **discount** to spot.

**Why?** Because convenience yield exceeds financing and storage costs. The immediate availability of physical is so valuable—because supply is tight, demand is urgent, or a disruption is feared—that the forward price collapses below spot.

**Example:** Natural gas in January (peak heating season). Spot (the very-near prompt) might be $2.50/MMBtu because furnaces need it now. But February is $2.30 because the crisis eases; March is $2.10 as winter wanes; summer months are $1.50 as demand evaporates. The market is in steep backwardation because immediate supply is scarce and expensive. Traders are willing to pay a premium to take delivery today, not three months hence.

Backwardation is common for:

- **Energy markets in winter** (heating oil, natural gas) when demand is urgent and inventories are drawn.
- **Commodities in shortage** (food during a crop failure, oil during a geopolitical crisis).
- **Agricultural commodities at planting** when farmers need to sell their old-crop inventory and buy new-crop futures to hedge production.

## The convenience yield driver

**Convenience yield** is the least obvious but perhaps most important term. It represents the **economic benefit of holding the commodity physically rather than owning a futures contract**.

Why might you prefer to hold physical copper rather than own a copper futures contract three months out?

1. **Operational need.** A copper refiner needs copper on hand to keep production running. A disruption in supply could shut down the factory. Physical copper provides insurance.

2. **Price optionality.** If you hold physical and prices spike, you can sell immediately at the spike price. A futures contract locks you in at the forward price; you miss the spike upside.

3. **Shortage premium.** In tight markets, the spot price is inflated relative to the forward because physical is scarce. The convenience yield captures that scarcity rent.

4. **Operational flexibility.** In a crunch, a refiner with physical inventory can negotiate better terms with downstream customers (e.g., guarantee supply). A paper futures position offers no such leverage.

In quantitative terms, convenience yield is the dividend-like return to holding the physical commodity. When it is high (tight supply, urgent demand), forwards trade at steep discounts (backwardation). When it is low (ample supply, no urgency), forwards trade at premiums (contango).

## Seasonality and forward curves

Commodity demand and supply are often seasonal. This layers onto the cost-of-carry formula.

**Natural gas** is a classic example. Winter demand is double or triple summer demand (heating, power generation). Convenience yield is highest in December–January (when physical is most needed) and lowest in June–August (when storage is built and demand is dormant). This creates a seasonal curve: winter forwards trade at steep premiums (or in backwardation), while summer forwards trade at discounts. See the [winter-summer spread](/energy-curve-winter-summer-spread/) article for depth.

**Agricultural commodities** (corn, wheat) show the inverse: they are harvested in fall, inventory is full, carry-forward to spring is ordinary storage, and forwards are in contango. But by spring, pre-harvest inventory is tight, and old-crop futures begin to trade at a backwardation to new-crop (soon-to-be-harvested) futures.

These seasonal patterns are baked into the forward curve. A trader analyzing a grain curve in August sees the contango; a trader in May sees a sharper, smaller contango or even a backwardation in old-crop months.

## Interest rates and financing costs

Financing cost is simply the **risk-free interest rate** (often the central bank rate or a bank lending rate) times the spot price times time. When central banks raise rates sharply, the financing component of the forward rises, widening the contango.

Conversely, in a low-rate environment, financing is cheap, and the forward trades closer to spot (or even at a discount if convenience yield is strong).

This is why commodity forward curves can shift materially on central bank announcement days. A surprise rate cut makes financing cheaper and can flatten or invert a contango curve.

## Risk premium and market expectations

The cost-of-carry formula is mechanical, but traders also layer in **supply-demand expectations and risk premiums**.

If a major producing country faces political unrest, traders may bid up distant futures even though carry costs have not changed. This is a risk premium—the market pricing in scarcity.

Similarly, if demand expectations shift (e.g., a recession forecast), distant futures can fall below the carry-cost prediction because traders expect lower consumption.

These expectations are embedded in the forward curve's **drift** or **slope**, and they evolve continuously as new information arrives.

## Practical implications for hedgers and speculators

**Hedgers** (producers or consumers locking in prices) must understand the forward premium or discount because it affects the true cost or revenue of their hedge. A farmer pre-selling corn at a forward discount to current spot is implicitly accepting a storage and financing cost; a refiner pre-locking crude at a forward premium is paying for carry.

**Speculators** trade the forward curve itself. They may bet that convenience yield will rise (going long physical, shorting futures, capturing the backwardation). Or they may bet that carry costs will fall (e.g., rates drop), compressing the contango.

**Physical arbitrageurs** (those buying spot, storing, and selling forward) earn the net carry cost. If the forward is $80 and spot is $75, plus carry is $3, they lock in a $2 loss—an economic loss that must be covered by other revenues (e.g., a refinery crack spread, a liquidity premium, or ancillary trading gains).

## See also

<div class="wiki-seealso">

### Closely related

- [Contango and Backwardation](/contango/) — Forward curves sloping upward vs downward
- Convenience Yield — Economic benefit of holding physical vs owning futures
- [Winter-Summer Spread](/energy-curve-winter-summer-spread/) — Seasonal variation in forward curves
- Commodity Forward Curve — The sequence of forward prices across contract months
- [Basis Risk](/basis-risk/) — Risk from widening or narrowing cash-forward gap
- [Marked to Market](/commodity-curve-marking-to-market/) — Repricing forward positions to current curve

### Wider context

- [Forward Contract](/forward-contract/) — Over-the-counter bilateral commodity agreements
- [Futures Contract](/futures-contract/) — Exchange-traded commodity contracts
- [Spot Rate](/spot-rate/) — Immediate cash price for delivery
- Cost of Capital — Interest and financing charges
- Supply and Demand — Economic forces driving commodity prices

</div>

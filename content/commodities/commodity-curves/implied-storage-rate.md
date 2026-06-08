---
title: "Implied Storage Rate"
description: "The marginal physical storage cost extracted from the observed contango slope in a commodity forward curve, assuming known financing rates."
keywords:
  - storage cost
  - contango
  - convenience yield
  - commodity curve
  - cost of carry
image: /svg/commodities.svg
---

*The **implied storage rate** is the market's embedded estimate of the cost to physically hold a commodity, backed out from the shape of the [forward curve](/forward-contract/). When you observe [contango](/contango/)—a premium for future delivery over spot—part of that premium reflects [interest costs](/interest-rate/) (financing); the remainder is storage. By subtracting financing from the observed spread, traders extract the physical storage component, revealing what the market implicitly "thinks" storage will cost.*

## The cost-of-carry framework

The foundation of all commodity curve pricing is the **cost-of-carry** model:

Forward Price = Spot Price + Storage + Financing − Convenience Yield

In its simplest form, if you know spot price, storage cost, and interest rate, you can calculate the "fair" forward price. But the market quotes forwards directly, often with observable [bid-ask spreads](/bid-ask-spread/) that imply traders disagree on storage cost. By rearranging the formula, you solve for the unknown:

Implied Storage = Forward Price − Spot Price − Financing + Convenience Yield

This is what traders call the **implied storage rate**—a backed-out cost, not a directly observed invoice.

## Why it matters

Physical storage is the glue holding the [forward curve](/forward-contract/) together. A tank of crude oil sitting in a Cushing terminal costs money to maintain: rent for the tank, insurance, security, monitoring equipment, inventory shrinkage or evaporation. For grain in a silo, you pay for climate control, pest management, and working-capital financing. For precious metals in a vault, you pay the depository's fee.

The forward curve reflects these real costs. When you see a steep [contango](/contango/)—say, crude trading at $5 per barrel premium from month to month—you are partly looking at storage costs embedded in prices. Traders who understand storage can identify when the curve is "rich" (storage premium too high) or "cheap" (storage scarcity not priced in), creating [hedging](/hedge-fund/) or trading opportunities.

## Separating storage from convenience yield

The trick is isolating storage from the **convenience yield**—the benefit of holding physical inventory. A refinery values crude on hand because it can immediately convert it to gasoline; a flour mill values wheat in the bin because it can grind it today. That benefit is a "negative cost" (a benefit), which compresses the forward price below what pure storage costs would predict.

Traders estimate convenience yield from supply–demand fundamentals. In times of inventory shortage (a supply crunch), convenience yield spikes—the curve flattens or inverts ([backwardation](/backwardation/)) even though storage costs are objectively high. In glut conditions, convenience yield approaches zero and the curve steepens (pure storage cost dominates).

So the true formula is:

Implied Storage = [Forward − Spot] − Financing + Convenience Yield

Estimating convenience yield requires judgment—it is not quoted on an exchange. Professional traders use econometric models, seasonal patterns, days-of-inventory data, and spot-to-futures spreads to infer it. Once they have a conviction about convenience yield, they can extract implied storage and compare it to actual tank rental rates from logistics firms.

## Reading the curve: storage across maturities

The implied storage rate is not constant across the forward curve. Early months (spot to +3 months) may face seasonal storage constraints—harvest season fills grain elevators to capacity, winter heating demand strains oil storage. Later months see lower marginal storage costs because the acute squeeze has passed.

This is why forward curves often [kink](/commodity-curve-kink/)—the slope steepens in nearby months where storage is constraining, then flattens at far months where storage becomes cheaper. By computing the implied storage rate at each maturity, traders can pinpoint where marginal costs shift.

## Practical application: storage arbitrage

Suppose crude forward prices imply a storage rate of $2 per barrel per month, but you can physically store crude at your facility for only $1 per barrel per month. You can:

1. Buy spot crude.
2. Pay $1/barrel to store it.
3. Sell it forward at the implied price (embedded with $2 storage cost assumption).
4. Pocket the $1/barrel spread at expiration.

This is a [cash-and-carry arbitrage](/spot-exchange-rate/)—a textbook commodity trade. It is profitable when implied storage is *above* actual storage. Conversely, if implied storage drops below your actual cost, you unwind the position.

The market self-corrects: if many traders execute this arbitrage, they push spot prices up and forward prices down, compressing the spread until implied storage aligns with actual cost. Efficient markets should have implied and actual storage in rough equilibrium, except at [commodity curve kinks](/commodity-curve-kink/) where structural changes (seasonal peaks, production restarts) create temporary dislocations.

## Impact of interest rates and financing

A rising [interest rate](/interest-rate/) increases financing costs for anyone holding physical inventory. This should push the forward curve steeper—you pay more to carry the commodity forward because borrowing costs more. Conversely, when rates fall, financing gets cheaper, and contango should compress.

In practice, this relationship is not mechanical. Central banks and [monetary policy](/monetary-policy/) decisions can affect commodity curves for several reasons: rate changes alter convenience yields and demand expectations; low rates incentivize storage accumulation; high rates encourage inventory drawdown. The implied storage rate can shift *because* financing changed, or *despite* it, if convenience yield or actual storage constraints change simultaneously.

## Why it is not a directly observed cost

The implied storage rate is never quoted as such—no warehouse publishes a "market storage rate" in real time. It is always a *backed-out* number, derived from prices of instruments that traders understand. This makes it a useful diagnostic: if implied storage diverges sharply from known physical costs (tank rental, insurance, labour), it signals that either (1) the market is irrational, (2) your convenience yield estimate is wrong, or (3) the curve contains priced-in expectations about future supply disruptions or seasonal patterns.

Professional storage operators carefully track implied rates. If the market is paying $2 per barrel for storage (embedded in the forward premium) but they operate at $1.50, they capture the spread. Scale this across millions of barrels, and the economics of storage operations hinge on getting the implied storage rate right.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — the forward curve state where near prices are below far prices, typically enriched by storage costs
- [Backwardation](/backwardation/) — inverted curve where convenience yield dominates storage cost
- [Commodity Curve Kink](/commodity-curve-kink/) — sharp breaks in the curve slope where storage costs transition seasonally
- [Forward Curve Bootstrapping (Commodities)](/commodity-forward-curve-bootstrapping/) — building a continuous curve from discrete futures to observe storage-cost structure
- [Time Spread Option (Commodities)](/time-spread-option-commodity/) — options sensitive to storage-cost changes embedded in the curve
- [Forward Contract](/forward-contract/) — the underlying economic relationship between spot and forward prices

### Wider context

- [Interest Rate](/interest-rate/) — financing cost incorporated into the cost-of-carry formula
- [Futures Contract](/futures-contract/) — exchange-traded version of forward contracts at discrete maturities
- [Arbitrage](/spot-exchange-rate/) — exploiting mispricings between spot and forward markets
- [Spot Exchange Rate](/spot-exchange-rate/) — the immediate price, baseline for all forward premiums

</div>

---
title: "Storage Costs and Their Effect on Commodity Futures Pricing"
description: "Storage, insurance, and financing costs are embedded in commodity futures prices via the cost-of-carry model, explaining contango and backwardation."
keywords:
  - storage costs commodity futures pricing
  - cost of carry
  - commodity futures pricing
  - storage costs
  - carrying costs
  - contango backwardation
---

*The futures price of a commodity is not determined solely by supply and demand expectations. **Storage costs and their effect on commodity futures pricing** reveals how warehousing fees, insurance, and financing costs are mathematically built into the futures contract. The difference between today's price and a future contract's price reflects what it costs to store, insure, and finance the commodity from now until delivery. This cost-of-carry model explains [contango](/contango/) and [backwardation](/backwardation/), and is essential to understanding why commodity ETFs and hedgers face persistent costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Carry — Key Facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Storage, insurance, and financing costs built into futures prices through arbitrage.</div>

|   |   |
|---|---|
| **Cost of carry formula** | Forward price ≈ Spot price × (1 + interest rate + storage cost − convenience yield) |
| **Key components** | Storage fee ($/unit/month); insurance (% of value); financing (interest on borrowed capital) |
| **Typical storage cost** | Oil: $0.20–$0.60/bbl/month; Wheat: 1–3¢/bu/month; Gold: 0.1–0.3%/year |
| **Interest cost** | Borrowing rate (LIBOR, SOFR, or bank rate) on the value of the commodity held |
| **Convenience yield** | Implicit benefit of holding physical (scarcity premium, production flexibility); reduces forward price |
| **Result** | Contango (high storage costs) or backwardation (high convenience yield) |

</aside>

## The Cost-of-Carry Model

The futures price is not a forecast. Instead, it is anchored to an arbitrage relationship: the cost to buy physical commodity today and deliver it on the contract date must approximately equal the futures price, or arbitrageurs will buy low and sell high (or short high and buy low) until prices align.

A trader who buys oil at $60 today and wants to deliver it three months out must pay:

1. **Spot price:** $60 per barrel
2. **Storage:** Approximately $0.30 to $0.60 per barrel for three months in a tank
3. **Insurance:** A fraction of the commodity's value, typically 0.1–0.3% annually
4. **Financing:** The interest cost on $60 per barrel for three months (if borrowing at, say, 5% annually, that is about $0.75 per barrel for three months)

The sum—roughly $61.60—is approximately what the three-month futures should price at. If the three-month contract traded at $59, an arbitrageur would buy spot oil at $60, store it, insure it, finance it, and sell the futures at $59—locking in a loss and immediately exiting at a profit through the futures sale. Prices would adjust until the gap closed.

This arbitrage relationship is not perfect (there are transaction costs, credit constraints, and operational frictions), but it is tight enough that cost of carry dominates short-term futures pricing.

## Why Storage Varies by Commodity

Storage cost is not uniform. It depends on the commodity's properties and the infrastructure available.

**Metals (gold, silver, copper, platinum):** Can be stored indefinitely with minimal degradation. Gold storage is typically 0.1–0.3% of value per year. This is remarkably cheap because gold does not rust or decay; it sits in a vault or London Bullion Market Association (LBMA) facility. A 6-month gold futures contract is typically only 0.05–0.15% above spot.

**Oil and natural gas:** Require specialized infrastructure. Crude oil is stored in tanks; natural gas in caverns or LNG tanks. Costs vary by location and capacity utilization. A full storage facility charges high rates; an underutilized one might offer discounts. Cost of carry for crude is often 0.3–0.5% per month, much higher than metals.

**Agricultural commodities (wheat, corn, soybeans):** Require temperature, humidity, and pest control. A grain elevator in the Midwest might charge 1–3 cents per bushel per month, or 2–5% per year on the commodity's value. Soft commodities also face spoilage risk, which is priced into storage charges.

**Live cattle and hogs:** Cannot really be stored (they must be fed and cared for). The cost of carry includes feed, healthcare, and facilities. This cost is high and unpredictable, so futures contracts are short-dated and volatile.

## Contango: The Normal Market

When storage costs are high and convenience yield is low, futures prices are higher than spot prices. This is **contango**. A three-month futures contract might trade at 105, while spot is 100. The 5-point gap reflects carrying costs.

Contango is "normal" in many commodities because storage has a real cost. Wheat in storage costs money; crude in a tank costs money. A hedger or long-term holder must pay these costs. This is why long-dated commodity ETFs and hedgers consistently lose money in contango markets—they pay the full carrying cost through rolling futures or buying storage.

Contango is also normal in times of ample supply. When warehouses are full and inventory is high, storage charges might be low or even negative (the commodity owner pays the warehouse for the ability to store, implying oversupply), but the contango still reflects the financing and insurance costs.

## Backwardation: The Stressed Market

When convenience yield is very high, futures can trade *below* spot price. This is **backwardation**. A three-month crude futures might trade at 95, while spot is 100. The commodity is worth a premium *right now* because it is scarce or in high demand for immediate use.

Backwardation arises when:

- **Supply is tight.** Refineries need crude immediately; a futures contract six months out is less valuable because they need it today.
- **Storage is full or unavailable.** When facilities are congested, producers would rather sell now than wait.
- **Production flexibility is valuable.** A refinery running lean on inventory can boost profit by buying physical crude and processing it immediately. The option to produce now is worth more than the option to receive later.
- **Geopolitical disruption.** If a major producer is offline (war, sanction, natural disaster), immediate supplies are scarce, and backwardation widens.

In backwardation, hedgers and storage operators earn a "roll yield." If you buy spot and sell futures, and the futures is lower, you lock in a gain when you roll or deliver. Commodity ETFs in backwardated markets can profit from rolling; producers can lock in better-than-spot prices by selling futures.

## Interest Rates and Cost of Carry

The financing cost is often the largest component of cost of carry, especially for high-value commodities and volatile rates.

A trader financing $1 million of gold for six months at a 5% annual rate pays roughly $25,000 in interest. If gold is trading at $1,800 per ounce, and the trader holds 556 ounces, the interest cost is about $45 per ounce, or 2.5% of the gold's value—far larger than storage or insurance.

This is why **lower interest rates tend to lower commodity futures prices** relative to spot. In a low-rate environment, carrying cost is cheap; futures trade lower relative to spot; contango is mild. Conversely, rising rates increase carrying costs and steepen contango.

## The Convenience Yield: The Hidden Benefit

Real-world futures prices often trade *lower* than the cost-of-carry formula alone predicts. This is because holding physical commodity confers a benefit—the **convenience yield**.

A refinery that owns crude in inventory can boost production if prices spike or demand surges. A farmer with stored wheat can time sales to peaks in local demand. A gold dealer holding inventory can supply regular customers immediately. These operational flexibilities are worth something, reducing the net cost of carry.

Convenience yield is not directly observable; it is inferred from the difference between futures and spot prices after subtracting known storage and financing costs. It rises when supply is tight (the benefit of holding inventory is high) and falls when supply is abundant.

In times of extreme scarcity (a major supply disruption), convenience yield can become so large that it more than offsets storage and financing costs, pushing futures into deep backwardation.

## Practical Implications for Hedgers and Traders

A commodity producer who hedges must understand cost of carry. If a farmer sells wheat futures three months out at a price 5% above spot, they might expect that premium reflects the three-month storage and financing costs. If contango is tighter than expected—say, 2%—the farmer is locking in a premium that exceeds the real carry. Conversely, if contango widens to 8%, the farmer is locking in a smaller premium.

Traders who arbitrage spot and futures (cash-and-carry or reverse cash-and-carry) compete away most of the unexplained gap. But in illiquid markets or for commodities with high storage constraints, the gap can persist.

Long-term holders of commodity ETFs or passive indexes face persistent costs in contango markets. Rolling from near-month to far-month futures locks in carry costs monthly or quarterly. Over years, these accumulate. This is why gold ETFs (low storage cost) have tracked spot price closely, while crude ETFs (higher storage cost and volatile contango) have lagged in prolonged contango.

## How Storage Capacity Affects Prices

When a commodity's storage capacity fills up (as happened with crude oil in 2020 during a demand collapse), carry costs can spike or even turn negative. Storage operators raise rates sharply; contango steepens dramatically. In extreme cases, prices go negative—the commodity owner will *pay* someone to take it off their hands rather than pay further storage and financing costs.

Conversely, new storage capacity coming online (more tanks, expanded caverns) softens carry costs and steepens contango by making carry cheaper.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — Far-month futures trading above near-month; driven by carry costs
- [Backwardation](/backwardation/) — Near-month futures trading above far-month; driven by tight supply
- [Commodity basis risk](/commodity-basis-risk/) — How local spot prices diverge from exchange futures
- [How commodity ETFs track prices](/how-commodity-etfs-track-prices/) — Why futures-based ETFs underperform in contango
- [Soft commodities vs hard commodities](/soft-commodities-vs-hard-commodities/) — Why storage costs differ between commodity types
- [Futures contract](/futures-contract/) — How standardized commodity contracts are priced and settled

### Wider context

- [Forward contract](/forward-contract/) — Over-the-counter analogs to futures; also priced via cost of carry
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — The general framework for present-value pricing via carry costs
- [Interest rate](/interest-rate/) — The cost of financing; a key component of carry
- [Yield curve](/yield-curve/) — The term structure of interest rates; affects carry for different maturities
- [Volatility smile](/volatility-smile/) — How option markets price tail risks in commodity markets

</div>

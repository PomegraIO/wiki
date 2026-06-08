---
title: "Cost of Carry in a Futures Position"
description: "Cost of carry in futures determines fair value and profit/loss. It combines financing, storage, and convenience yield to explain why futures trade above or below spot."
keywords:
  - cost of carry futures
  - futures cost of carry
  - cost of carry formula
  - basis and cost of carry
  - futures fair value
  - financing cost futures
  - convenience yield futures
image: "/svg/trading.svg"
---

*The **cost of carry** is the combined cost of financing, storing, and holding a physical asset until a futures contract expires. It determines whether a futures contract should trade above or below the spot price, explains spreads between contracts of different maturities, and reveals whether a trade is likely to be profitable.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Carry — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Fair futures value = spot price + cost of carry; deviations create arbitrage opportunities.</div>

|   |   |
|---|---|
| **Components** | Financing cost + storage cost − convenience yield |
| **Formula** | F = S × e^((r + u − y)T) (continuous approximation) |
| **Financing** | Interest rate paid to borrow money or capital tied up |
| **Storage** | Physical warehousing, insurance, spoilage (grain, oil, metals) |
| **Convenience yield** | Benefit of holding the physical good (liquidity, production input) |
| **Implications** | High carry → futures trade above spot (contango) |
| **Implications** | Low carry → futures trade near or below spot (backwardation) |

</aside>

## The principle: locking in the cost of carry

If you want to buy gold today and sell it in one year, you have two options:

1. **Buy spot, hold it**: Pay the current spot price, finance it for a year, pay insurance and storage, and sell in one year.
2. **Buy a one-year futures contract**: Lock in a forward price now, pay nothing until settlement, then take delivery and settle.

These two paths should result in the same final profit or loss. If they do not, an arbitrageur will exploit the gap. This is the principle of [cost of carry](/cost-of-carry/): the futures price must equal the spot price plus the cost of financing, storing, and carrying the asset to the [expiration date](/expiration-date/).

Formally:

**Fair futures price = Spot price × e^((r + u − y) × T)**

Where:
- **r** = risk-free interest rate (borrowing cost)
- **u** = storage cost (as a percentage of the asset value)
- **y** = convenience yield (benefit of holding physical; negative, reduces carry)
- **T** = time to expiration (in years)

## Financing cost: the interest rate

If you buy an asset today and hold it for one year, you must finance that purchase. The financing cost is typically the risk-free rate (government bond yield) plus a borrowing spread. A trader might fund a gold position by borrowing at the one-year Treasury rate plus a bank spread.

For highly leveraged traders or institutions with poor credit, the borrowing cost is higher. For [central banks](/central-bank/) and government treasuries, it is lower. This creates a cost-of-carry hierarchy: different market participants face different financing costs, so they value the same futures contract differently. A cheap borrower is more willing to buy the spot and hold it; an expensive borrower prefers to buy futures.

## Storage costs: real and variable

Commodities must be stored. Physical gold requires secure vaults; [crude oil](/crude-oil/) requires tanks; [corn](/corn/) and grain require elevators and climate control; [natural gas](/natural-gas/) requires pipeline injection or LNG terminals.

Storage is not free. Warehousing fees, insurance against loss or damage, and spoilage all add to the carry cost. For agricultural commodities, storage is steep (a significant percentage of the commodity's value per month). For financial assets like [Treasury bonds](/treasury-bond/), storage is negligible (data costs only).

A trader who buys spot and holds it must absorb these storage costs, passed through to the futures price. If futures rise above spot by more than the carry cost, the arbitrage becomes profitable: buy spot, sell futures, pocket the difference.

## Convenience yield: the hidden benefit

A **convenience yield** is the benefit of holding the physical good rather than a paper contract. A manufacturing company that uses copper in production benefits from having copper on hand: it can respond to orders immediately, avoid supply disruptions, and maintain continuous production. A trader holding copper futures does not have these benefits; the contract is just a stand-in.

The convenience yield is hardest to measure but often the largest component of cost of carry. It depends on the tightness of the market. In a well-supplied market (ample copper, low prices), convenience yield is near zero; the benefit of having physical copper right now is low. In a tight market (shortages, high prices, long lead times), convenience yield is large; being able to produce immediately is worth a lot.

Convenience yield is subtracted from the cost of carry because it reduces the incentive to hold futures instead of spot. If I value physical gold at a high convenience yield (perhaps I am a jeweler and need it for immediate production), I am less willing to sell spot gold and buy futures; I will demand a discount on the futures to compensate. This compression of futures relative to spot is called **backwardation**.

## Contango and backwardation: reading the market

**Contango** is when futures trade above spot: F > S. This happens when the cost of carry (r + u − y) is high and positive. It is the "normal" state for most financial futures (Treasuries, equity indices, currencies) and well-supplied commodity futures. The futures price simply reflects the cost of financing and storing the underlying until expiration.

**Backwardation** is when futures trade below spot: F < S. This happens when convenience yield is large or negative carry dominates. Backwardated markets are common in tight commodity markets (near-term contracts especially) or during disruptions. A trader who owns spot and sells futures at a discounted price is being compensated for the convenience yield of owning the physical.

During the 2020 [crude oil](/crude-oil/) crisis, [WTI crude](/crude-oil/) May futures fell to negative prices (buyers paid to take delivery) while June futures were positive, a sharp backwardation. The convenience yield of having oil right then—or the desperation to avoid taking delivery at all—overwhelmed normal financing costs.

## Basis and roll yield

**Basis** is the difference between futures and spot: Basis = Futures − Spot.

In a normal contango market, basis is positive. As expiration approaches, the basis shrinks: the futures converges to spot at delivery. A trader holding a long futures position through this convergence experiences "roll yield"—a profit as the futures price falls (toward spot) as expiration nears, if you close the position before settlement. This is the carry yield you capture by holding a futures contract as it matures.

For a trader holding a contango spread (long nearby, short deferred futures), the basis between contracts decays as both converge. If the nearby contract is $2 above spot and the deferred contract is $4 above spot, holding the spread earns the $2 difference plus the difference in carry costs as both contracts approach expiration.

## The carry trade: arbitrage and risk

A **carry trade** in futures exploits the cost of carry by buying spot, selling futures, and pocketing the difference at expiration. If the futures price exceeds the theoretical fair value (spot + carry), the carry trade is profitable.

Example: Gold spot is $2000, one-year futures is $2100. Carry cost (financing + storage − convenience yield) is $80. Fair futures value is $2080. The futures are overpriced by $20. A trader can:

1. Borrow $2000, buy physical gold, pay $80 in carry costs
2. Sell one-year gold futures at $2100
3. At expiration, deliver the gold and net $2100 − $2000 − $80 = $20 profit

This arbitrage is risk-free if you can lock in all prices today and there are no transaction costs or financing surprises. In reality, financing rates may change, storage fees may be higher than expected, and delivery logistics may fail. But the principle holds: basis trades (buying spot, selling futures) harvest the carry.

## Negative carry and why people hold it

Occasionally, carry is negative—the benefit of holding spot exceeds the cost. This is rare for stocks or bonds (why pay financing and storage for a negative return?) but common for commodities with high convenience yield during supply disruptions.

If convenience yield is very high (tight markets, urgent production needs), even holders of negative financial carry will hold the physical. A manufacturer short of a critical input will pay financing costs to hold it on hand.

In financial markets, negative carry is deliberately chosen by [central banks](/central-bank/) and governments (holding reserves) or by traders during liquidity panics (holding cash or safe assets at a loss because the safety is worth it).

## Practical implications for futures traders

Understanding cost of carry helps you:

- **Predict basis moves**: In contango, basis shrinks as you approach expiration; rolling forward locks in the decay.
- **Spot mispricings**: If futures deviate materially from spot plus carry, an arbitrage opportunity appears.
- **Choose contracts**: Holding a contango spread (long nearby, short deferred) is a carry-harvesting trade; it profits if basis tightens as expected, regardless of the direction of the asset.
- **Manage storage and financing**: For physical traders, the cost of carry tells you the maximum you should pay for spot if you plan to hold to futures expiration.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — standardized contracts and mechanics
- [Basis](/basis/) — difference between futures and spot
- [Contango](/contango/) — futures above spot, normal for well-supplied markets
- [Backwardation](/backwardation/) — futures below spot, typical in tight markets
- [Expiration Date](/expiration-date/) — when a futures contract settles
- [Forward Contract](/forward-contract/) — customized carry agreements
- Convenience Yield — the value of holding physical goods

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — using futures to manage risk
- [Spot Rate](/spot-rate/) — immediate delivery price
- [Interest Rate Risk](/interest-rate-risk/) — how rate moves affect carry
- [Execution Risk](/execution-risk/) — costs and timing of buying or selling
- [Carry Trade](/carry-trade/) — exploiting interest-rate or carry differences
- Arbitrage — risk-free profit from mispricing

</div>

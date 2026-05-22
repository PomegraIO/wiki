---
title: "Commodity Carry Trade"
description: "Financing long commodity positions with storage and convenience yield; holding physical or futures while capturing the cost-of-carry premium."
keywords:
  - commodity carry trade
  - cost of carry
  - convenience yield
  - futures rolling
  - commodity financing
---

*A **commodity carry trade** finances a long position in a commodity by borrowing to fund storage and carrying costs, then collecting the [convenience yield](/wiki/convenience-yield-commodity/) and [contango](/wiki/contango/) premium. The strategy profits when the future price is sufficiently higher than the spot price to cover funding costs, storage, insurance, and financing. It is the commodity equivalent of a [cash-and-carry arbitrage](/wiki/arbitrage-pricing-theory/).*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Structure** | Buy spot commodity; finance with debt; store; sell futures forward |
| **Profit driver** | Contango: futures price > spot + carry costs |
| **Carry costs** | Storage, insurance, financing, convenience yield loss |
| **Risk** | Spot price collapse; storage facility failure; funding stress |
| **Time horizon** | Days to months; typically liquidated before expiration |
| **Returns** | 2–8% annualized if contango persists; can exceed borrowing cost |
| **Liquidity** | Requires deep futures markets; illiquid commodities reduce viability |
| **Counterparty** | Commodity trader, hedge fund, or bullion bank |

</aside>

## The mechanics of commodity carry

A trader observes the following prices for oil:

- **Spot (WTI Crude)**: $75/barrel
- **December futures**: $76.50/barrel
- **Storage cost**: $0.05/barrel/month
- **Financing cost**: 5% annualized (~$0.31/barrel for 6 months)
- **Insurance**: $0.02/barrel/month

**The carry calculation**:
- Futures price minus spot: $76.50 − $75 = $1.50
- Total carry cost for 6 months: (6 × $0.05) + $0.31 + (6 × $0.02) = $0.61/barrel
- **Net profit (if no price change)**: $1.50 − $0.61 = $0.89/barrel per spread

The trader can:
1. Buy 100,000 barrels of crude oil at spot ($75/barrel) = $7.5M
2. Finance the $7.5M at the repo rate (5% annualized)
3. Store and insure the oil
4. Sell December futures at $76.50/barrel
5. **Profit**: $0.89 × 100,000 = $89,000 for the 6-month carry

This is a quasi-arbitrage: the profit is nearly locked in if the position is hedged with futures.

## Contango and backwardation in carry trades

The profit of a carry trade depends on the shape of the [futures curve](/wiki/futures-contract/).

**Contango** (normal backwardation in commodity jargon): Futures prices rise with maturity. The Dec contract is higher than Nov, Nov higher than Oct. This is the carry-friendly environment.

**Backwardation**: Futures prices fall with maturity (or invert at very near dates). This is carry-unfriendly because storing the commodity to deliver into a cheaper future contract loses money.

In a strongly backwardated market (e.g., oil in 2024 with supply fears), the spot premium is so high that storing oil is uneconomical. Carry traders avoid, and spot oil becomes scarce, bidding up the physical price further.

In contango (normal post-crisis, low-risk markets), carry traders actively arbitrage, borrowing to finance long positions and funding storage.

## Convenience yield as the hidden benefit

Beyond the futures spread, commodities offer a **convenience yield**: the benefit of holding the physical commodity.

A refiner short on crude oil might pay a premium (reflected in backwardation or a physical spot bid) to have immediate access to fuel. A precious metals dealer might value holding physical gold because customers can buy it instantly. This convenience yield is not observable in futures prices but is captured by those holding physical.

The carry trade implicitly collects this convenience yield: the refiner or dealer pays the carry trader's storage costs plus financing costs, because the convenience of having spot material available is valuable.

In gold, the convenience yield is typically small (1–2% annually) because gold is fungible and liquid. In crude oil, it swings from 0% (abundant storage) to 5%+ (supply concerns, storage full). Understanding the convenience yield helps predict when carry trades are most profitable.

## Financing and repo markets

The cost of carry depends on the **repo rate**: the interest rate at which a trader can finance collateral in the securities lending market.

In normal times:
- Repo rate: 4–5%
- Oil carry cost: 2–3% (storage + insurance)
- **Total cost**: ~6–8%

If the contango yield is 8%, carry is profitable. If contango yields 6%, carry is break-even or negative after all costs.

During financial stress (2008, 2020, 2023), repo rates spike, sometimes reaching 10%+. Carry trades become uneconomical overnight, and traders unwind, pressing spot prices lower and sometimes inverting the curve.

This is why carry traders are vulnerable to funding shocks. A sudden repo spike or loss of financing access can force liquidation, spreading losses beyond the trader to the broader commodity market.

## The cost-of-carry model

The **cost-of-carry formula** describes the theoretical relationship between spot and futures prices:

**Futures Price = Spot Price × e^(r+s+i-c)×T**

Where:
- **r** = risk-free rate (financing)
- **s** = storage cost (per unit)
- **i** = insurance
- **c** = convenience yield
- **T** = time to expiration

If the futures price exceeds this calculated "fair value," the contract is overpriced, and a carry trader profits by being long physical and short futures (cash-and-carry). If the futures price is below fair value, a reverse carry is profitable (short physical, long futures).

## Practical examples: Gold and Oil

**Gold carry** (typical contango):
- Spot: $2,000/oz
- 1-year futures: $2,080/oz (4% contango)
- Financing cost: 5% (repo)
- Storage/insurance: 0.12% annually (~$2.40/oz)
- **Net carry**: 4% − 5% − 0.12% = −1.12%

Gold carry is unprofitable here because financing exceeds the contango premium. Gold is typically backwardated or minimal contango.

**Oil carry** (example from 2021):
- Spot WTI: $60/barrel
- 6-month futures: $62/barrel
- Financing cost: 3% annualized (~$0.90 for 6 months)
- Storage + insurance: $0.30/barrel for 6 months
- **Net carry**: $2 − $0.90 − $0.30 = $0.80/barrel, or 1.3% for 6 months (10.4% annualized)

Oil carry is profitable, and traders actively finance long positions.

## Rolling futures and managing expiration

A commodity trader holding a long physical position cannot simply hold the spot forever—they must eventually sell. The futures market allows rolling positions.

A trader long December crude:
- December contract approaches expiration → pressure to settle
- Trader sells December contract at, say, $76.50
- Simultaneously buys January contract at $75.80 (backwardation rolling forward)
- **Roll cost**: Sold at $76.50, bought at $75.80 = $0.70/barrel loss

Over many rolls, the trader captures the curve shape each time. In contango, rolling is cheap (futures decline toward the roll date); in backwardation, rolling is expensive.

A successful carry trader manages roll costs tightly, rolling multiple times per year if markets permit.

## Risks: Storage, price, and funding

**Storage risk**: Physical commodity can deteriorate, leak, or be destroyed. Crude in a tank can emulsify; metals can be lost in theft or facility failure. Traders buy insurance, but it has limits and costs.

**Price risk**: If spot price crashes (OPEC production cuts reversed, recession demand collapse), the trader is long at a loss. Even if the carry trade was "arbitrage," a large adverse move can exceed the carry profit.

Example: Trader finances crude at $75 for a $76.50 futures sale. Oil crashes to $70. The trader is underwater $5/barrel, a 6.7% loss, far exceeding the $0.89 carry profit.

**Funding risk**: If the repo market dries up (2008, 2020) or credit concerns spike, financing rates leap, and the trade becomes unprofitable instantly. Forced liquidation can force the trader to sell at the worst time.

## Strategic use in portfolio context

Commodity carry trades are used by:

- **Commodity traders**: Professional arbitrageurs capturing carry premiums
- **Banks/bullion dealers**: Financing customer positions; extracting carry
- **Hedge funds**: Tactical plays on contango/backwardation mean reversion
- **Commodity ETFs/funds**: Rolling positions to track spot prices; incurring carry costs

For ETF holders, carry is a drag. An ETF tracking crude by rolling futures in contango loses 0.5–2% annually to rolling costs. This is why contango environments lead to ETF underperformance versus spot prices.

## Counterintuitive outcomes

**COVID-era example (April 2020)**: Oil spot fell to −$40 (negative!) as storage filled and demand vanished. Futures remained slightly positive. A carry trader long physical (worthless or costing to store) shorted futures (positive price) suffered catastrophic losses. Contango inverted; backwardation spiked; carry collapsed.

This shows the carry trade's dark side: when fundamentals shift sharply, carry trades can blow up faster than expected.

<div class="wiki-seealso">

### Closely related
- [Convenience yield](/wiki/convenience-yield-commodity/) — benefit of holding physical commodity; reduces carry cost
- [Contango and backwardation](/wiki/contango-backwardation-impact/) — future prices relative to spot; shapes carry profitability
- [Cost of carry](/wiki/cost-of-carry/) — financing, storage, and insurance costs
- [Commodity futures](/wiki/commodity-futures-rolling/) — derivative contracts for buying/selling commodities

### Wider context
- [Arbitrage](/wiki/arbitrage-pricing-theory/) — exploiting price differences between markets
- [Repo market](/wiki/repurchase-agreement/) — short-term secured lending using collateral
- [Commodity storage costs](/wiki/commodity-storage-costs/) — physical holding expenses
- [Commodity investing](/wiki/commodity-etf/) — strategies for gaining commodity exposure

</div>

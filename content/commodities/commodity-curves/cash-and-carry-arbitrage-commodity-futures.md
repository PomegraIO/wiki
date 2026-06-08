---
title: "Cash-and-Carry Arbitrage in Commodity Futures"
description: "Cash-and-carry arbitrage in commodity futures locks in a riskless profit by buying the spot commodity, storing it, and selling a deferred futures contract when the futures price exceeds the spot plus carrying costs."
keywords:
  - cash and carry arbitrage commodity futures
  - commodity arbitrage spot futures
  - futures curve arbitrage
  - contango arbitrage
  - storage arbitrage commodities
image: /svg/commodities.svg
---

*A **cash-and-carry arbitrage in commodity futures** is a riskless trade where an investor buys a physical commodity at the spot price, pays for storage and financing, and simultaneously sells a deferred futures contract at a premium, locking in a profit spread. It exploits structural mispricings in the [futures curve](/futures-contract/) when far-out contracts trade at too steep a premium.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cash-and-Carry Arbitrage — Key Facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Three simultaneous moves: buy spot, finance and store, sell futures—to harvest the curve premium.</div>

|   |   |
|---|---|
| **Basic structure** | Long spot commodity + short deferred futures contract |
| **Profit source** | Futures premium minus financing, storage, and insurance costs |
| **Market condition** | [Contango](/contango/) (futures > spot + carry costs) |
| **Risk profile** | Theoretically riskless if held to maturity and counterparties perform |
| **Participants** | Commodity merchants, refiners, banks, specialized arbitrage funds |
| **Exit timing** | At futures expiration; carry is harvested or rolled forward |
| **Capital requirement** | Full spot purchase price + margin for futures short position |

</aside>

## The Mechanics of the Trade

Cash-and-carry arbitrage works through a simultaneous three-leg transaction. First, the arbitrageur buys the physical commodity at the current spot market price. Second, the arbitrageur arranges financing (a repo or loan) to pay for the spot purchase and obtains storage (a warehouse or tank facility). Third, the arbitrageur sells a forward or futures contract at a price locked in today, with delivery at a specified future date.

If the futures price exceeds the total cost of spot purchase plus financing, storage, insurance, and other carrying costs, the arbitrageur has locked in a profit at origination. Because all three legs are entered simultaneously and at known prices, the trade carries no directional risk—the arbitrageur does not care whether the spot price rises or falls during the holding period, only that the curve structure remains wide enough to cover costs.

For example, suppose crude oil trades at $70 per barrel spot. A 12-month futures contract trades at $75 per barrel. The arbitrageur buys 1,000 barrels at $70 (cost: $70,000), finances the purchase at 5% annually (cost: $3,500), and pays $0.50 per barrel for storage and insurance over the year (cost: $500). Total cost: $74,000. The arbitrageur sells 1,000 barrels of the 12-month futures at $75 (revenue: $75,000). Locked-in profit: $1,000 before taxes and transaction costs.

## Why the Futures Premium Must Exist

The **[basis](/basis/)** is the difference between the futures price and the spot price. A positive basis (futures > spot) creates [contango](/contango/), the condition under which cash-and-carry works. Why does contango exist? Because holding the physical commodity costs money: financing, storage, spoilage risk, and opportunity cost. A rational seller of futures should demand compensation for these costs. If the futures price did not exceed spot by at least the carrying cost, it would be cheaper to simply own the commodity than to short it, and the market would rebalance.

The futures premium, properly measured, is the cost of carry. When the premium exceeds carry cost—when the market is "overpriced" relative to the cost of holding spot—an arbitrage exists. Conversely, when the premium is tight or the market is in backwardation (futures < spot), cash-and-carry is unprofitable or impossible, and the arbitrage market disappears.

## Financing and Storage: The Carry Costs

Financing is often the largest cost component. An arbitrageur who borrows $70,000 to buy 1,000 barrels pays interest at the prevailing lending rate. Large banks and commodity merchants typically borrow via repurchase agreements (repos), where they post the physical commodity as collateral and borrow short-term funds at a spread to benchmark rates. Over longer holding periods, the cost compounds.

Storage and handling vary by commodity. Oil tanks, grain elevators, warehouse receipt programs, and vaults each charge fees—sometimes a flat rate, sometimes a percentage of value, sometimes both. Some commodities degrade or shrink in storage (grain loses moisture, oil may evaporate slightly), eroding the profit margin further. Insurance against loss or damage is another line item. In liquid, high-volume contracts (crude oil, natural gas, gold), these costs may be tight enough that only the thinnest margins survive; in niche commodities or during thinly traded periods, carry costs can be substantial.

## The Role of Authorized Participants

In commodity **[ETFs](/etf/)**, especially [commodity-linked funds](/commodity-etf/), **[authorized participants](/authorized-participant/)** (APs) perform cash-and-carry arbitrage to keep the ETF price aligned with the underlying futures curve. When the ETF trades at a premium to its net asset value, APs buy futures (or spot commodity) and redeem them for ETF shares, then sell the shares at the premium, capturing the spread. This mechanism keeps ETF pricing tight and is essential to how commodity funds operate efficiently.

## Exit and Roll-Forward Mechanics

A cash-and-carry arbitrage is naturally closed at the expiration of the futures contract. The arbitrageur delivers the physical commodity into the futures contract, completing the sale at the locked-in price. The futures contract then expires, and the profit is realized.

However, if an arbitrageur wishes to hold the commodity beyond the original futures expiration, they may **roll** the position: sell the near-term futures and buy a longer-dated contract, establishing a new cash-and-carry spread. If the curve remains steep enough to cover carry, the arbitrage can persist through multiple rolls. If the curve flattens or inverts, rolling becomes unprofitable, and the arbitrageur should exit.

## Risk and Basis Risk

Although cash-and-carry is theoretically riskless, real-world frictions introduce risk. **Basis risk** can arise if the spot and futures prices do not converge exactly at maturity—for instance, if the futures contract specifies a delivery location that is distant from the arbitrageur's warehouse, and transportation costs differ from expectations. **Counterparty risk** exists if the storage facility or financing provider defaults. **Regulatory or liquidity risk** can emerge if a futures exchange closes trading, changes contract terms, or imposes position limits that prevent the arbitrageur from maintaining the short futures hedge.

Also, if the cost of carry is misjudged—if storage runs higher than estimated, or if financing rates spike—the profit may shrink or vanish. For this reason, institutional arbitrageurs model carry costs conservatively and continuously monitor them throughout the holding period.

## Market Efficiency and Arbitrage Elimination

Cash-and-carry arbitrage is a classic example of **market efficiency** in action. When the futures premium exceeds carry, sophisticated participants exploit the mispricing by buying spot and selling futures, driving down the futures price (or driving up the spot price) until the premium narrows back to fair value. The arbitrage opportunity gradually disappears as more capital floods in. In mature, liquid commodity markets with tight contango, cash-and-carry spreads are often only a few basis points (hundredths of a percentage point)—enough to reward high-volume traders with tight financing but too thin for casual or small-scale operators.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — the curve structure that enables cash-and-carry
- [Futures Contract](/futures-contract/) — the instrument and mechanics underlying the arbitrage
- [Basis](/basis/) — the spread between spot and futures that drives the arbitrage
- [Authorized Participant](/authorized-participant/) — institutional players who execute cash-and-carry in ETFs
- Commodity Curves — the structure of spot, forward, and futures prices
- [Carry Trade](/carry-trade/) — a related arbitrage concept across asset classes

### Wider context

- [Crude Oil](/crude-oil/) — a primary commodity for cash-and-carry strategies
- Commodities — the broader asset class and market structure
- [Securitization](/securitization/) — how cash flows are financed in commodity trade

</div>
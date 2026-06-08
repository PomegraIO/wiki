---
title: "Key Terms in a Futures Contract Specification"
description: "Futures contract specs define contract size, grade, tick size, delivery terms, and trading rules. Learn what each field means and how they affect trading."
keywords:
  - futures contract specification
  - futures contract specifications key terms
  - contract size
  - tick size
  - delivery location
  - futures grade standards
  - last trading day
image: "/svg/derivatives.svg"
---

*Every **futures contract specification** is a legal document that locks in the exact terms under which two parties agree to transact. A crude oil future and a wheat future differ not just in the commodity; they differ in contract size, delivery grade, settlement location, and dozens of other rules that appear in the exchange spec. Understanding these key terms is essential to trading futures.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Contract Specifications — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Standardized terms that define exactly what you are buying or selling.</div>

|   |   |
|---|---|
| **Contract size** | How many units (bushels, barrels, ounces) you control per contract |
| **Grade/quality** | Which quality standard the deliverable must meet |
| **Delivery location** | Warehouse, port, or exchange where physical settlement occurs (if exercised) |
| **Tick size** | Smallest price move allowed; determines minimum profit/loss per contract |
| **Last trading day** | Final day when the contract can be traded; after this, it settles |
| **Expiration cycle** | Which months contracts are available (quarterly, monthly, etc.) |
| **Daily price limits** | How much the price can move up or down in one trading session |
| **Settlement type** | Physical delivery, cash settlement, or choice thereof |

</aside>

## Contract size: controlling scale

Contract size is the foundation of any futures spec. A COMEX gold futures contract represents 100 troy ounces; a CBOT wheat contract represents 5,000 bushels; a WTI crude oil contract represents 1,000 barrels. These numbers are not arbitrary—they reflect historical trading conventions and aim to make contracts useful for both hedgers and speculators.

For a trader, contract size determines [leverage](/leverage-ratio-forex/). Buying one gold contract gives you exposure to 100 ounces. At a gold price of $2,000 per ounce, you control $200,000 of value, but you post only a margin requirement (often 10–15% of contract value) to do so. Smaller contract sizes exist for retail traders (E-mini contracts are one-fifth the size of standard contracts), allowing participation with less capital and lower absolute risk.

Contract size also affects liquidity. The most-traded contracts are the standard ones; mini contracts sometimes trade more thinly. A trader comparing two exchanges or contract variants must verify the contract size, as price moves translate to different dollar amounts.

## Grade and quality standards

Deliverable-grade specifications define what physical commodity you actually receive if a contract settles into delivery. For gold, the spec states minimum purity (typically 99.5%). For crude oil, grade might be "West Texas Intermediate" or "Brent Crude," with specified API gravity and sulfur content ranges.

Agricultural contracts often allow multiple grades at par or with price adjustments. A wheat contract might accept No. 2 Hard Red Winter wheat but allow delivery of higher-grade No. 1 at a premium or lower-grade No. 3 at a discount. This flexibility keeps the contract liquid—it allows many producers to participate—but introduces basis risk. A farmer with premium wheat will deliver it at a slight premium; one with lower-grade wheat may accept a small haircut.

These specifications exist because quality varies. They prevent a gold producer from delivering 90%-pure gold and declaring it equivalent to pure gold. They anchor the contract to a real commodity, not an abstraction.

## Delivery location

Futures contracts specify one or more approved delivery locations (or warehouses), typically chosen to be liquid and accessible to both buyers and sellers. COMEX gold contracts allow delivery at designated vaults in New York or London. Corn contracts allow delivery at several grain elevators in Illinois, Iowa, and other major production zones.

Delivery location matters because transportation costs real money. If a contract specifies delivery only in a remote location, the buyer bears the cost of shipping the commodity to a useful place. Specifications that allow delivery in multiple locations reduce this friction. However, some locations are preferable—a buyer or seller closer to one location gains a small advantage, creating a basis spread.

For cash-settled contracts (like index futures), there is no physical location; the contract value is simply paid in cash at expiration.

## Tick size and price increments

Tick size (or "minimum price movement") is the smallest price change allowed. For gold futures, the tick might be $0.10 per troy ounce. For crude oil, it might be $0.01 per barrel. This is not merely a convention—it has real economic impact.

If oil trades at $80 per barrel with a $0.01 tick and a contract size of 1,000 barrels, one tick equals $10 of profit or loss. A trader holding the contract experiences $10 swings with every tick. Coarser tick sizes (say, $0.05) mean larger minimum moves; finer ticks (say, $0.001) mean smaller moves. Exchanges choose tick sizes to balance fairness (sufficient resolution to avoid price clustering) against liquidity (finer ticks can fragment trading across too many price levels).

Tick size also affects bid-ask spreads. Broader ticks naturally create wider [bid-ask-spread](/bid-ask-spread/) because there is no price level between one tick and the next.

## Last trading day and expiration cycle

Every futures contract has a last trading day—the final moment you can trade the contract in the exchange. After that date, the contract settles (either by delivery or cash payment), and it is gone. A crude oil contract might expire on the 20th business day before the next delivery month; a stock index future might expire on the third Friday of the expiration month.

Exchanges publish expiration cycles. Some commodities trade contracts for every month; others only quarterly. A grain producer hedging next year's harvest must know that December wheat contracts expire in December, March contracts in March, and so on. If you are holding a position and the last trading day approaches, you must either close the position or accept delivery (if physical) or cash settlement (if cash-settled).

Expiration cycles also create a term structure of prices. Nearby contracts (those expiring soon) often trade differently than distant contracts, reflecting supply expectations and [carry](/carry-trade/) costs. The difference in price between two expirations is called [contango](/contango/) (if distant contracts are pricier) or [backwardation](/backwardation/) (if nearby are pricier).

## Daily price limits and circuit breakers

Many futures exchanges impose daily price limits—the maximum amount a contract can move in a single trading session. A limit of 2% might mean that if wheat opens at $7.00 per bushel, it cannot trade above $7.14 or below $6.86 that day. These limits are meant to prevent panic selling or buying from causing wild swings.

When a contract hits its limit—either up or down—trading often halts or moves to a "lock limit" state where only liquidating trades are allowed. This prevents cascading losses but can also trap traders. If news breaks overnight (a bad harvest, a geopolitical event), the market may want to reprice, but the limit prevents it. At the next open, a gap often occurs.

Some contracts have no limits, particularly financial futures and index contracts, which move based on real-time news rather than supply shocks.

## Settlement type: physical or cash

The spec states how the contract settles. Physical-delivery contracts (most agricultural and commodity futures) require actual transfer of the commodity. Cash-settled contracts (most equity indexes, currency, and interest-rate futures) pay out the difference in cash.

Physical settlement creates a logistics chain: sellers must deliver to approved warehouses, buyers arrange pickup and transport. Cash settlement is simpler: the exchange calculates the final payoff and deposits it directly to accounts.

Knowing the settlement type is critical. A trader planning to hedge a physical commodity needs a physical-delivery contract; a portfolio manager tracking the S&P 500 needs a cash-settled index contract.

## Putting it together: a wheat example

Consider a CBOT wheat futures contract in December. The spec states:

- **Contract size:** 5,000 bushels
- **Grade:** No. 2 Hard Red Winter wheat, or higher-grade at premium, lower-grade at discount
- **Delivery locations:** Several approved elevators in Illinois, Iowa, Kansas, Missouri, Nebraska
- **Tick size:** $0.0025 per bushel ($12.50 per contract)
- **Last trading day:** Second-to-last business day of the delivery month (December)
- **Daily limit:** 50 cents per bushel ($2,500 per contract)
- **Settlement:** Physical delivery or cash equivalent

A farmer with 10,000 bushels of wheat to sell in December can short two December wheat contracts, locking in a price. A food processor needing wheat can buy contracts, secure in the knowledge that the commodity will meet grade standards. If wheat prices spike 3% in one day, the price-limit rule kicks in, preventing the full move that day. When December arrives, the farmer delivers wheat (or a buyer takes delivery), or both sides settle in cash for the difference.

Without these standardized terms, every wheat trade would require custom negotiation about quality, location, and settlement. The spec enables a [liquid, efficient market](/market-capitalization/).

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the basic definition and how futures work
- [Contango](/contango/) — when distant expiration months trade higher
- [Backwardation](/backwardation/) — when nearby months trade higher
- [Last trading day](/expiration-date/) — the deadline for trading
- [Tick size](/bid-ask-spread/) — minimum price movement and spread width

### Wider context

- [Forward contract](/forward-contract/) — customized alternative to standardized futures
- [Derivative markets](/derivatives-hedging/) — how futures fit into the broader derivatives ecosystem
- [Price discovery](/price-discovery/) — how futures markets reveal true market prices

</div>

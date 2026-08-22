---
title: "Copper Futures Contract Specifications"
seo_title: "Copper Futures Contract Specs: Size, Tick, Delivery"
description: "COMEX copper futures cover 25,000 lbs per contract with a $12.50 tick and 99.99% cathode grade. Full specs: lot size, months, delivery, and hedging math."
keywords:
  - copper futures contract size and specifications
  - comex copper futures specs
  - copper futures contract details
  - copper futures lot size
  - industrial copper hedging
image: "/svg/commodities.svg"
---

*[Copper futures contract specifications](/copper-futures-contract-specs/) define the standardized contract terms on the COMEX exchange: lot size (25,000 pounds), tick size (0.0005 cents/pound), minimum grade (99.99% purity), delivery locations, and settlement mechanics. Understanding these specs is essential for industrial copper users and hedgers to calculate position sizes, margin requirements, and [basis risk](/basis-risk-explained-with-example/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">COMEX Copper Futures — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The world's most actively traded copper contract; standardized around industrial end-user needs.</div>

|   |   |
|---|---|
| **Exchange** | COMEX (CME Group) |
| **Ticker** | HG (e.g., HGZ26 for December 2026) |
| **Lot size** | 25,000 pounds (11,339 kilograms) per contract |
| **Minimum grade** | Cathode copper, 99.99% pure (electrolytic grade) |
| **Tick size** | 0.0005 cents/pound (0.1 mil); minimum price move = $12.50 per contract |
| **Contract months** | Quarterly cycle: Jan, Mar, May, Jul, Sep, Dec (23 months forward) |
| **Delivery** | Settlement in New York, COMEX-approved warehouses; physical or cash |
| **Clearing** | CME Clearinghouse; marked to market daily |

</aside>

## The standard COMEX copper contract

COMEX copper futures are the world benchmark for copper commodity trading. The contract is standardized to make it liquid and suitable for both hedgers (industrial producers and buyers) and speculators.

### Lot size and notional exposure

Each COMEX copper contract represents 25,000 pounds. At a copper price of $4.00/pound, one contract has a notional value of $100,000. An industrial buyer needing to hedge 500,000 pounds of copper would buy 20 contracts (500,000 ÷ 25,000 = 20).

This lot size is large enough to be efficient—low transaction costs per pound—but also means that smaller buyers or hedgers must round up or employ strategies like [basis trading](/basis-risk-explained-with-example/) or cash-settled swaps.

### Tick size and price increments

The minimum price move is 0.0005 cents/pound, called one "tick." On a 25,000-pound contract, one tick equals $12.50 (0.0005 × 25,000). Prices must be quoted in half-tick increments (0.00025) in electronic trading.

A trader might see a price quote of $4.5025/pound (read as "four-fifty and a quarter"). Price movements of less than one half-tick are not allowed. This standardization ensures consistent liquidity and pricing.

### Grade and purity

COMEX copper futures require delivery of electrolytic copper cathode at minimum purity of 99.99%. This is the grade used in electrical wiring, motors, transformers, and most industrial applications. Impurities beyond 0.01% must be within allowable limits for common elements (iron, tin, cadmium, etc.).

Higher-purity grades (99.99% and above) trade at modest premiums; lower-purity scrap copper is dealt with separately (not eligible for COMEX futures). This ensures delivery is fungible—any approved cathode from an approved producer meets the spec.

### Delivery locations and warrants

Physical copper is stored in COMEX-approved warehouses, primarily in the New York area but also in select US locations. When a futures contract is held to expiration, the holder receives a "warrant"—a certificate of ownership for the copper held in the warehouse.

Transportation between warehouses carries cost; moving copper from a US interior location to New York adds basis. Industrial hedgers often account for this in their [cross-hedge calculations](/basis-risk-explained-with-example/).

## Contract months and rolling

COMEX copper futures trade 23 contract months forward: the current month and the following 22 months. However, most volume is concentrated in the nearest three months. The "front-month" contract (the next to expire) is the most liquid.

Standard expirations are:

- **January, March, May, July, September, December** (quarterly cycle, plus Nov and Feb micro-contracts in some periods)

An industrial buyer that needs three months of copper might:

1. Buy three consecutive monthly contracts (e.g., Jan, Mar, May).
2. Roll down: hold the Jan contract, and as it nears expiration, sell Jan and buy Apr to extend the hedge forward.

Each roll entails transaction costs and [basis risk](/basis-risk-explained-with-example/) as nearby and deferred contracts may have different prices.

## Position limits and trading halts

COMEX imposes position limits—the maximum number of contracts any single trader can hold—to prevent manipulation and ensure market integrity. Non-commercial traders (speculators) have lower limits than bona fide hedgers (producers and end-users). A large industrial producer might be granted a hedge exemption to hold 10,000+ contracts if it can prove physical copper exposure.

Daily price limits trigger trading halts if copper moves too far in one day. These are designed to prevent panic; the halt pauses trading, then resumes with expanded limits if volatility persists.

## Margin and leverage

Futures trading requires margin—a cash deposit—to enter a position. Initial margin for COMEX copper might be $3,000–$5,000 per contract (roughly 3–5% of notional value), depending on volatility. Maintenance margin is slightly lower; if the account dips below maintenance, the trader must post additional margin or liquidate positions.

Leverage is inherent: controlling $100,000 of copper exposure with $4,000 in margin is 25:1 leverage. A 4% adverse move in copper ($0.16/pound) wipes out the margin and forces liquidation. This is why most commercial hedgers (who have real copper exposures) use futures differently from speculators: they are offsetting real risk, not amplifying returns.

## Delivery mechanics and settlement

Two weeks before contract expiration, open-interest holders must decide: take delivery or liquidate. The contract is cash-settled or physically delivered (buyer receives warrant, pays final settlement price).

**Physical delivery:**
- Seller delivers a warehouse warrant to the buyer.
- Buyer pays the settlement price × 25,000 pounds.
- Buyer can then take possession of the physical copper or sell the warrant.

**Cash settlement (rare for copper):** The contract is settled in cash based on final exchange price.

Most financial traders liquidate before delivery; industrial buyers occasionally take delivery and use the warrant to claim copper. The process is standardized and settled by the CME Clearinghouse.

## Calculating hedge position size

An electrical equipment manufacturer uses 50,000 pounds of copper per month. It wants to hedge the price of copper purchases for the next three months.

**Naive calculation:**
- Total copper needed: 150,000 pounds
- Contracts required: 150,000 ÷ 25,000 = 6 contracts

**Adjusted for basis risk:**
Suppose historical data shows that the manufacturer's actual **local copper costs (delivered to its factory) move only 0.92 against COMEX price movements** due to transport, grade premiums, and local supply factors. Then:

- Effective contracts: 6 × 0.92 = ~5.5 contracts (round to 5 or 6 depending on risk preference)

A regression of historical local copper prices against COMEX futures prices yields the hedge ratio, reducing [basis risk](/basis-risk-explained-with-example/).

## Contract variations and alternatives

COMEX copper is the primary global standard. However, the London Metal Exchange (LME) also trades copper futures (in metric tonnes, not pounds), and regional exchanges in China and India have contracts denominated locally. A global copper producer might hedge with COMEX (US dollars, accessible globally) while a local Chinese processor might use the Shanghai Futures Exchange (CNY-denominated, with delivery in China).

For smaller positions or risk-averse buyers, copper swaps (OTC derivatives) are an alternative, customized to the buyer's specific grade and delivery location and thus often with lower [basis risk](/basis-risk-explained-with-example/) than futures.

## Specifications in practice

Industrial buyers often compare futures specs to their actual needs:

| Aspect | COMEX Spec | Actual Need | Implication |
|--------|-----------|----------|-----------|
| Lot size | 25,000 lbs | 8,000 lbs/month | Must over-hedge or use swaps |
| Grade | 99.99% cathode | 99.5% acceptable | Grade mismatch; mild basis risk |
| Delivery location | NY warehouse | Factory in Chicago | Transport cost is basis |
| Tenor | Quarterly months | Weekly buys | Must roll frequently or use swaps |

Each mismatch introduces basis risk; the buyer's job is to measure it and decide whether futures, swaps, or a combination is cost-effective.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the broad mechanics of commodity futures contracts
- [Basis Risk Explained with Example](/basis-risk-explained-with-example/) — how futures specs create mismatch risk in hedging
- Commodities — the asset class that copper futures represent
- [Hedging](/derivatives-hedging/) — how industrial buyers use copper futures to manage price risk
- [Swap](/swap/) — an alternative to futures for customized copper exposure

### Wider context

- [Crude Oil](/crude-oil/) — another heavily-traded commodity future with similar mechanics
- [Forward Contract](/forward-contract/) — the OTC alternative to exchange-traded futures
- [Counterparty Risk](/counterparty-risk/) — a difference between exchange-cleared futures and OTC swaps
- [Clearinghouse](/derivatives-hedging/) — CME Clearinghouse's role in managing futures settlement
- [Volatility Smile](/volatility-smile/) — how option skews affect industrial copper options strategies

</div>

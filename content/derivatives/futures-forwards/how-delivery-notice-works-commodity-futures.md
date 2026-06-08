---
title: "How the Delivery Notice Process Works in Commodity Futures"
description: "Step-by-step mechanics of delivery notice issuance by shorts, exchange matching, and physical or cash settlement in commodity futures contracts."
keywords:
  - delivery notice commodity futures
  - how delivery notice works
  - commodity futures delivery
  - physical settlement
  - futures contract mechanics
  - short squeeze
image: /svg/derivatives.svg
---

*In commodity futures, a **delivery notice** is the formal announcement by a short (seller) that they intend to fulfill their contract by delivering the physical commodity. The mechanics—from notice to matching to settlement—are tightly choreographed by the exchange and set strict timelines and grade specifications to prevent disputes and ensure finality.*

<div class="wiki-hatnote">

For an overview of commodity futures themselves, see [Futures Contract](/futures-contract/). This article covers the delivery notice mechanics specifically.

</div>

## The Core Delivery Notice Process

When a commodity futures contract nears or enters its delivery period (the last two weeks to month of the contract month, depending on the commodity), short holders can issue a **delivery notice** to declare their intent to satisfy the contract by delivering the actual commodity rather than buying back their position in the market.

The process follows these steps:

1. **Short notifies the clearinghouse** (typically via broker) that they intend to deliver.
2. **Clearinghouse randomizes or assigns a long** (buyer) to take delivery.
3. **Short provides warehouse receipt or physical proof** of approved commodity quality and location.
4. **Long inspects and accepts** (or disputes) the delivery.
5. **Funds settle** (long pays, short receives).
6. **Commodity transfers** to the long's nominated warehouse or account.

The entire sequence is designed to be orderly, transparent, and final—preventing disputes and squeezes. Exchanges publish exact rules governing grade, quantity, location, inspection windows, and penalties.

## The Short's Notice to the Clearinghouse

### Timing and Notification

Shorts must issue a delivery notice within strict deadlines set by the exchange. For many commodities:

- Notice must be filed **before the market opens on a specific "first notice day"**—often two or more weeks before contract expiration.
- Some exchanges allow notice only on certain days (e.g., Tuesday or Wednesday for crude oil).
- Once filed, the notice is irrevocable; the short must follow through.

Missing the deadline means the short must instead close the position (buy back the contract) or roll to the next month.

### Grade and Specification Compliance

The short must certify that the commodity meets the contract's specifications:

| Aspect | Example (crude oil futures) |
|--------|---------------------------|
| **Grade/Quality** | WTI Crude: API gravity 38–42, sulfur < 0.42% |
| **Quantity** | Contracts typically 1,000 barrels; delivery within ±0.5% |
| **Location** | Cushing, Oklahoma (the physical delivery hub for WTI futures) |
| **Proof of deposit** | Warehouse receipt from an exchange-approved facility |
| **Testing certificate** | Recent lab assay confirming grade |

If the commodity doesn't meet specs, the exchange rejects the notice, and the short must source different material or close the contract.

### Warehouse Receipt and Logistics

The short deposits the physical commodity in an **approved warehouse** operated by a facility the exchange has licensed. The warehouse issues a **receipt** (a negotiable title document) that the short presents to the clearinghouse.

For agricultural contracts (corn, soybeans, wheat), the receipt certifies warehouse location, quantity, grade, and the date stored. For metals (gold, copper), it certifies assay and bar serial numbers. For energy (crude, natural gas), it might reference a pipeline injection or tank location.

The short does *not* hand the commodity directly to the clearinghouse; the short merely demonstrates legal title to approved inventory.

## The Clearinghouse Matches the Long

Once the short's notice is accepted, the clearinghouse **assigns the delivery obligation to a long**—typically the oldest open long contract (FIFO, first-in-first-out, to ensure fairness).

### Random or Deterministic Assignment

Exchanges use different assignment methods:

- **FIFO queue**: The longest-held long contract gets assigned.
- **Random assignment**: Weighted by position size so larger longs absorb more deliveries.
- **Voluntary acceptance**: Some exchanges allow longs to volunteer to take delivery, especially if they need the commodity.

The long receives a **notice of delivery**—a formal document stating:
- Contract specifications.
- Grade and quantity.
- Warehouse location.
- Warehouse contact and procedures.
- Payment due date.

## The Long's Inspection and Acceptance Window

Upon receiving the delivery notice, the long has a limited window (often 2–5 business days, depending on the commodity) to:

1. **Inspect the commodity** (physically visit the warehouse or accept third-party inspection results).
2. **Verify grade and quantity** match the contract and receipt.
3. **Accept or reject** the delivery.

### Accepted Delivery

If the long inspects and accepts, they:
- Pay the futures settlement price (not the market price on the delivery day) multiplied by the quantity.
- Receive the warehouse receipt or take possession (depending on the commodity).
- The position is closed; the contract is settled.

### Contested or Rejected Delivery

If the long disputes the grade, discovers damage, or finds the quantity is short, they can **reject** the delivery:

- The warehouse (or short) must cure the issue or the exchange arbitrates.
- If arbitration finds the commodity non-conforming, the short must source replacement material *or* buy back the contract at a penalty.
- This rarely happens because exchange grade specifications are strict and sellers have strong incentive to comply.

## Settlement and Payment

### Price Settlement

The critical fact: the long **pays the official settlement price** of the futures contract on the day the short issued the notice, *not* the spot price of the commodity on delivery day. This is why delivery provides price certainty.

Example:
- Long held contract at $60/barrel (bought at that price weeks earlier).
- Short issues delivery notice when crude is trading at $62/barrel.
- Long still pays $60/barrel × 1,000 barrels = $60,000 (not $62,000).

This pricing mechanism is what makes futures contracts powerful: longs and shorts lock in prices regardless of spot-market moves between contract entry and delivery.

### Cash Payments

- The long sends payment to their broker; the broker remits to the clearinghouse.
- The clearinghouse releases payment to the short's broker.
- The short receives the proceeds, minus commissions and warehouse costs.
- Warehouse fees (storage, inspection, handling) are typically borne by the short (the party exiting the position via delivery).

### Warehouse Transfer

The warehouse updates its records to reflect the long as the new owner of the commodity. The long can:
- Take physical possession (paying demurrage and transport costs).
- Keep the commodity in the warehouse under their account.
- Re-deliver it in a later month's futures contract (if they hold a contract forward).

## Scenarios and Edge Cases

### Short Squeeze and Delivery Notice Timing

If a long accumulates a large position and wants to **force physical delivery** (either to control supply or to pressure shorts), they may take a long position and hold it into the delivery period. Shorts with insufficient supply can face:

- Rising cost to source replacement commodity.
- Forced buyback at inflated prices.
- Technical delivery defaults.

This is a **short squeeze**. Exchanges regulate against it by setting position limits and monitoring for manipulative intent.

### Cash Settlement Commodities

Some futures contracts (e.g., stock index futures, some financial contracts) **do not allow physical delivery**; they settle to cash based on an official reference price. The short is obliged to pay or receive cash on the delivery date, but no commodity changes hands.

### Fungible vs. Specific Commodity

Most agricultural and metals futures specify the commodity by grade *only*, not by specific lot or producer. A long receiving corn delivery has no claim on *which farm's* corn arrives—only that it meets grade specs. This fungibility simplifies matching and settlement but removes quality nuance.

## Timeline Summary

| Phase | Parties | Timing |
|-------|---------|--------|
| **Notice filing** | Short to clearinghouse | First notice day (often 2+ weeks pre-expiry) |
| **Notice acceptance** | Clearinghouse validates specs | 1 business day |
| **Long assignment** | Clearinghouse to long | Concurrent with notice acceptance |
| **Inspection window** | Long inspects commodity | 2–5 business days post-notice |
| **Acceptance/rejection** | Long confirms or disputes | End of inspection window |
| **Settlement** | Long pays; short receives | Same day or next business day |
| **Commodity transfer** | Warehouse updates ownership | Within 1 business day of payment |

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the underlying instrument; explains contract specifications and settlement mechanisms
- [Contango](/contango/) — when far-month futures trade above near-month; storage and delivery costs create this curve shape
- [Backwardation](/backwardation/) — when near-month futures trade above far-month; often signals physical shortage or urgent demand
- Commodity Exchange — the marketplace where futures trade and delivery rules are enforced
- [Spot Rate](/spot-rate/) — the current physical-market price; often differs from futures price due to carry costs and convenience yield
- [Expiration Date](/expiration-date/) — the final day a futures contract can be held or delivered
- Clearinghouse — the entity that guarantees and enforces delivery and settlement

### Wider context

- [Forwards Contract](/forward-contract/) — customized, non-exchange-traded agreements; do not have standardized delivery mechanics
- [Market Maker Trading](/market-maker-trading/) — dealers who provide liquidity in futures markets; some take and hedge deliveries
- Arbitrage — traders may buy spot and sell futures (or vice versa) to lock in delivery-related profit
- Commodity Hedging — companies use futures delivery windows to manage physical supply-chain timing
- [Warehouse](/warehouse-receipt/) — facilities that store commodities and issue receipts for futures settlement
- [Roll](/expiration-contracts/) — how traders shift positions from expiring to forward contracts without taking delivery

</div>

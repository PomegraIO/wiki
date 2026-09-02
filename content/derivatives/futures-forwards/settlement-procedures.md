---
title: "Settlement Procedures"
description: "The detailed mechanics of finalizing futures and forward contracts—from notification through delivery or cash payment—the operational framework that makes derivatives markets work."
---

*When a [futures contract](/wiki/futures-contract/) expires, two things must happen: positions are closed, and money or goods change hands. The settlement procedure is the choreography ensuring this happens reliably, fairly, and without disputes.*

## The settlement lifecycle

A [futures contract](/wiki/futures-contract/) lifecycle has three phases:

**1. Trading phase:** Contracts are bought and sold in the market. Positions are opened, closed, adjusted. [Mark-to-market](/wiki/mark-to-market/) occurs daily. [Variation margin](/wiki/variation-margin/) flows.

**2. Notice period:** As expiration approaches, the short side (in [physically deliverable contracts](/wiki/delivery-mechanisms/)) can announce intent to deliver. This typically opens 1-4 weeks before expiration, depending on the contract.

**3. Settlement phase:** The contract expires. Remaining positions are either delivered or [cash-settled](/wiki/cash-settlement/). Money and goods are transferred.

## Notice procedures

In [physically deliverable contracts](/wiki/delivery-mechanisms/), the short side initiates settlement by serving **notice of intent to deliver** to the clearing house and their broker.

The notice specifies:
- **Which contracts:** Exactly how many contracts the short intends to deliver against.
- **What grade and quality:** The specification of the commodity being delivered.
- **Where delivery will occur:** The approved warehouse, elevator, or terminal.
- **When delivery will occur:** The day within the delivery window.

Once notice is served, the short is **obligated** to deliver. The long is obligated to accept. The clearing house matches them, notifies both parties, and sets a delivery date.

The long then has **delivery acceptance period:** typically 24-48 hours to inspect and accept the delivery. If the commodity meets contract specifications, it must be accepted. If it is off-spec, the long can reject it, and the short must redeliver elsewhere (or the exchange may arbitrate).

## Physical delivery execution

For commodities, delivery often occurs through **warehouse receipts** or **electronic transfers** rather than physical movement:

**Warehouse receipts:** The commodity is already stored in an exchange-approved warehouse. The warehouse issues a receipt to the short, who tenders it to the clearing house. The clearing house transfers the receipt to the long. The long now owns the warehouse receipt (and thus the commodity). The commodity never physically moves from the warehouse.

**Electronic book transfer:** For some commodities (especially crude oil at Cushing), the underlying is stored at a central location. Settlement occurs as an electronic transfer of ownership records. The long's name is added to the inventory at the facility; the short's is removed. Title passes; no barrels are trucked.

**Bill of lading:** For commodities in transit, a bill of lading (a document evidencing shipment) changes hands. The short delivers goods; the short (or a shipping agent) issues a bill of lading to the long proving delivery has occurred.

This system is elegant: it avoids the cost and chaos of moving actual commodities. A 100-contract crude oil delivery (100,000 barrels) does not result in 100,000 barrels being trucked; the warehouse records simply transfer.

## [Cash settlement](/wiki/cash-settlement/) procedures

For [cash-settled contracts](/wiki/cash-settlement/), settlement is simpler:

1. **Settlement price is published.** The exchange announces the official settlement price (typically the opening, closing, or a special auction during the settlement window).

2. **Final P&L is calculated.** Each position's gain or loss is computed against the settlement price.

3. **Cash is transferred.** The clearing house debits losing traders' accounts and credits winning traders'. Settlement occurs T+1 (one business day after settlement price is announced).

Example: An S&P 500 E-mini [futures](/wiki/futures-contract/) trader went long at 4,500. At [expiration](/wiki/expiration-contracts/), the settlement price is 4,600. The gain is (4,600 - 4,500) × $50 multiplier = $5,000. The clearing house credits the account $5,000 and debits the counterparty (or pool of counterparties) $5,000.

## The clearing house role

The clearing house (often the **Options Clearing Corporation (OCC)** for equities and equity derivatives, or **DTCC** subsidiaries for other asset classes) is the central counterparty:

- **Every trader's counterparty:** When you buy a contract, you buy from the clearing house (not the seller). When you sell, you sell to the clearing house.
- **Default guarantor:** If a trader defaults, the clearing house absorbs the loss (funded by member fees and capital reserves).
- **Settlement operator:** The clearing house executes all settlement procedures—matching delivers, confirming [cash settlements](/wiki/cash-settlement/), transferring warehouse receipts.

Because the clearing house is the counterparty to every trade, it is essential that it remain solvent. Exchanges impose strict margin, [initial margin](/wiki/initial-margin/), and [maintenance margin](/wiki/maintenance-margin/) requirements to ensure members can meet their obligations.

## Settlement cycles and fails

Most settlements occur as planned. But occasionally, failures occur:

**Delivery fail:** A short promised delivery but failed to assemble the commodity or arrange transportation. The short must either redeliver (if time permits) or pay a penalty.

**Payment fail:** A trader settled in cash but funds did not arrive on time. The clearing house may charge interest and penalties.

**Inspection fail:** A long rejected delivered goods as off-spec. The short must redeliver and may face financial penalties for the delay.

Modern settlement systems are designed to prevent fails through:
- **Real-time gross settlement (RTGS):** Cash and securities transfer in real-time, not batched. If you cannot transfer funds, the transaction fails immediately (not after a day of clearing).
- **Central depositories:** Physical certificates are eliminated; securities are recorded in central ledgers. Electronic transfers are instantaneous.
- **Margin monitoring:** The clearing house monitors margin continuously; if a member falls below maintenance, the member is forced to liquidate before default occurs.

The 2008 financial crisis exposed vulnerabilities in settlement infrastructure, leading to regulatory reforms emphasizing real-time settlement and higher capital buffers.

## Special settlement scenarios

**Early settlement:** A trader who no longer wants their position can settle before [expiration](/wiki/expiration-contracts/). They simply close the position in the market (sell to offset a buy, buy to offset a sell). No formal settlement procedure; the position is liquidated at market prices.

**Novation:** When a position changes hands (one trader's long becomes another trader's long through brokerage systems), the clearing house steps in. The old trader's long is closed against the clearing house; a new long is opened from the clearing house. The original counterparties are severed; both now face the clearing house.

**Corporate actions:** If the underlying asset undergoes a dividend, stock split, or spin-off, [futures contracts](/wiki/futures-contract/) on that asset may be adjusted. A stock split (2 for 1) might cause an [index futures](/wiki/sp-500-index/) multiplier to double to preserve position equivalence.

**Force liquidation:** If a member faces a bankruptcy or regulatory suspension, the clearing house can force liquidation of all positions. Contracts are transferred to other members, ensuring the clearing house's liability is covered.

## Settlement failures and systemic risk

When settlement fails systematically (multiple fails, cascading defaults), systemic risk emerges:

**Long-Term Capital Management (LTCM), 1998:** A massive hedge fund faced margin calls during the Russian financial crisis and had to liquidate enormous positions. Settlement was chaotic; counterparties feared default. The Federal Reserve orchestrated a rescue to prevent cascading settlement failures.

**Lehman Brothers, 2008:** Lehman's bankruptcy created uncertainty about trillions in derivatives and [futures](/wiki/futures-contract/) positions. The clearing house and regulators had to carefully separate Lehman's positions, assign them to other members, and ensure settlement did not break down.

**2020 VIX futures volatility:** During the March 2020 crisis, [VIX futures](/wiki/volatility-index-futures/) and related products experienced extreme moves. Retail traders using leveraged VIX ETPs faced margin calls they could not meet, leading to forced liquidations. Settlement was orderly but created significant losses.

These episodes remind regulators and clearing houses that settlement infrastructure is fragile under extreme stress. Continuous improvements in real-time monitoring, margin models, and emergency protocols are ongoing.

## Settlement and the end user

For most traders and hedgers, settlement is invisible. You close a position; funds appear or disappear in your account. The clearing house orchestrates the details.

But for those holding positions through [expiration](/wiki/expiration-contracts/)—farmers taking delivery, refineries accepting crude, speculators forced to settle—the details matter immensely. The difference between efficient settlement (delivering goods promptly, paying in accordance with contract terms) and inefficient settlement (delays, disputes, force liquidations) is the difference between profitable hedging and disaster.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the instruments whose settlement is the subject of this entry.</li>
<li><a href="/wiki/delivery-mechanisms/">Delivery mechanisms</a> — how [physically deliverable contracts](/wiki/delivery-mechanisms/) settle through warehouses and logistics.</li>
<li><a href="/wiki/cash-settlement/">Cash settlement</a> — resolution via cash transfer rather than physical delivery.</li>
<li><a href="/wiki/expiration-contracts/">Expiration dates</a> — when settlement procedures are triggered.</li>
<li><a href="/wiki/mark-to-market/">Mark-to-market</a> — daily revaluation preceding final settlement.</li>
<li><a href="/wiki/variation-margin/">Variation margin</a> — daily cash settlement of P&L during the holding period.</li>
<li><a href="/wiki/dtcc/">DTCC</a> — the central clearing organization for many financial contracts.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li>Derivatives — the broader category of financial instruments requiring settlement procedures.</li>
</ul>
</div>

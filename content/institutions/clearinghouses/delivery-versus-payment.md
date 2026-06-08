---
title: "Delivery Versus Payment"
description: "Settlement principle that links security and cash transfers so both complete or both fail, eliminating settlement risk."
keywords:
  - delivery versus payment
  - dvp
  - atomic settlement
  - settlement risk
  - finality
  - securities settlement
image: /svg/institutions.svg
---

*In **delivery versus payment** (DVP) settlement, the transfer of a security is linked to the transfer of cash such that neither completes without the other. If the seller delivers the security but the buyer does not pay, the transfer is reversed; if the buyer pays but the seller does not deliver, the payment is reversed. This atomic principle eliminates settlement risk—the risk that one party receives its side of the trade but the other does not.*

Before DVP, settlement of securities was messy. A buyer would send cash; days later, the seller would deliver the security. The buyer would be unsecured for the cash during those days; the seller would be unsecured for the security. If either party failed in that gap, the other was left as an unsecured creditor. By introducing simultaneity—"you get your security if and only if I get my cash"—DVP eliminates this exposure entirely.

## The settlement risk problem

Imagine a sale of 1,000 shares at $100 per share. The buyer sends $100,000 to the seller's bank. Two days later (T+2 in most markets), the seller sends the shares to the buyer via a [central securities depository](/central-securities-depository/) (CSD) or clearing system. But what if the seller's bank fails on T+1, before the shares are delivered? The buyer is stuck: the bank has the cash and is insolvent, and the buyer doesn't have the shares.

Or the mirror scenario: the seller delivers the shares to the buyer's account at a CSD on T+2, and the buyer's bank fails before paying cash. The seller now holds an unsecured claim on a bankrupt buyer.

These scenarios are not hypothetical. Before DVP was widely adopted, settlement failures were common and costly. In the 1987 stock market crash, settlement gridlock nearly broke the financial system because too many transactions were pending and counterparty credit was strained.

## How DVP works in practice

A DVP settlement typically involves three parties: the seller, the buyer, and one or more infrastructures.

1. The seller's cash account is credited and the buyer's is debited (at a [central bank](/central-bank/) or the CCP's cash account).
2. Simultaneously, the seller's securities account is debited and the buyer's is credited (at a [CSD](/central-securities-depository/)).
3. Both transfers are final and irrevocable.

The synchronisation is critical. Most modern DVP systems achieve this through **simultaneous gross settlement**: the [central bank's](/central-bank/) real-time gross settlement (RTGS) system and the CSD communicate in real time and settle both legs together. If one leg fails (e.g., the buyer has insufficient funds), both are reversed.

Some older or simpler markets use **delivery first / payment second**: the seller delivers securities first; the buyer's bank then pays cash. This reduces buyer credit risk slightly (the buyer now holds the shares as collateral) but still leaves the seller at risk if the buyer's bank fails after receiving the securities. It is less protective than true simultaneous DVP.

## DVP and the role of the CCP and CSD

For exchange-traded securities and derivatives, a clearinghouse (CCP) and a [central securities depository](/central-securities-depository/) work together to implement DVP. The CCP calculates settlement obligations via [multilateral netting](/multilateral-netting/): who owes whom cash and who owes whom securities. The CSD then executes the settlement, crediting and debiting accounts in sync with the central bank's RTGS system.

The CCP itself bears the credit risk during this process—it promises each party that if the other party fails, the CCP will step in and complete the transaction. This is why [capital adequacy](/capital-adequacy/) and [default funds](/default-fund/) are so important for CCPs; they must have resources to absorb a member failure without disrupting settlement.

## Models of DVP: the three flavours

Regulators and academics distinguish three DVP models:

**Model 1** is same-bank DVP. The seller and buyer both bank at the same institution. That institution debits one account and credits the other, in a single entry. There is no settlement risk because both legs are internal to the bank. But this model is rare; most large trades involve different banks.

**Model 2** is delivery-first DVP. The CSD delivers securities to the buyer; the RTGS system simultaneously stands ready to pay cash to the seller. If the buyer's bank fails to pay, the CSD has authority to reverse the securities delivery. This protects the seller but leaves the buyer holding the securities if the seller's bank fails to honour any refund obligation.

**Model 3** is simultaneous DVP. The CSD and the RTGS system settle both legs at exactly the same moment—a true atomic transaction. Both legs complete or both fail. This is the gold standard and is mandatory in most major markets today.

## Legal and technical requirements

To implement true simultaneous DVP, legal and technical infrastructure must align. Legally, the seller must have a claim that the securities transfer is final only if and when the cash transfer is final. Technically, the CSD and the RTGS system must be linked with sufficient granularity and speed that a failure of one leg triggers an immediate reversal of the other.

This requires real-time communication between systems that operate at high speed and must never fail. Modern implementations use cryptographic commitments and atomic transaction protocols borrowed from distributed systems. The Bank for International Settlements and the [International Organization of Securities Commissions](/iosco/) jointly set technical standards (the **Principles for Financial Market Infrastructures**, or PFMI) that most CSDs and RTGS operators must meet.

## Cross-border DVP and complexity

DVP becomes harder across borders. If a US buyer purchases German shares, the shares are held in a German [CSD](/central-securities-depository/) and cash is settled in euros via a European [real-time gross settlement](/real-time-gross-settlement/) (RTGS) system. Synchronising settlement across two CSDs, two RTGS systems, and two currencies adds latency and operational risk.

Many cross-border trades are settled through **custody chains**: an international custodian or settlement agent holds accounts at both CSDs and RTGS systems, managing the synchronisation on behalf of the buyer and seller. This adds a layer of intermediation but enables DVP at the operational level even if full technical integration is missing.

Some CSDs have established **links** with foreign counterparts, enabling direct DVP settlement of cross-border trades. But most international settlement still relies on custodians and delivery versus receipt (a less strict variant of DVP used in OTC markets).

## Impact on market efficiency and risk

DVP is an economic force. By eliminating settlement risk, it dramatically reduces the amount of credit reserves banks must hold. Before DVP, a large securities trader might hold tens of millions in cash as a buffer against settlement failures. With DVP, that buffer can be much smaller. This freed-up capital fuels market growth and efficiency.

But DVP also creates operational dependencies. If the CSD or RTGS system fails, all settlement halts. A CSD outage is a systemic event. This is why modern CSDs and RTGS systems are systemically important institutions subject to intensive regulatory oversight, stress testing, and investment in redundancy.

## See also

<div class="wiki-seealso">

### Closely related

- [Central Securities Depository](/central-securities-depository/) — executes the securities leg of DVP
- [Real-Time Gross Settlement](/real-time-gross-settlement/) — payment system that executes the cash leg of DVP
- Clearinghouse — calculates settlement obligations that DVP then executes
- [Multilateral Netting](/multilateral-netting/) — reduces the number of settlements that must be coordinated via DVP
- Settlement Infrastructure — broader system of which DVP is a core principle
- [Central Bank](/central-bank/) — operates the RTGS system that DVP relies on
- [Counterparty Risk](/counterparty-risk/) — settlement risk that DVP eliminates

### Wider context

- Systemically Important Institution — CSDs and RTGS systems are designated as such
- [Capital Adequacy](/capital-adequacy/) — regulatory framework that ensures CCPs can honour DVP commitments
- Securities Settlement — process of which DVP is the foundational principle
- [Liquidity Risk](/liquidity-risk/) — intraday liquidity management interacts with DVP requirements

</div>

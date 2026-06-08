---
title: "Proof of Solvency vs Proof of Reserves in Crypto"
description: "Proof of reserves shows assets exist; proof of solvency proves assets exceed liabilities. Why the distinction matters for exchange security audits."
keywords:
  - proof of solvency vs proof of reserves
  - crypto exchange solvency audit
  - reserves verification blockchain
  - exchange balance sheet proof
---

*A cryptocurrency exchange's **proof of reserves** demonstrates that it holds the assets it claims to hold. **Proof of solvency**, by contrast, goes further—proving that total assets exceed total liabilities, meaning the exchange is solvent. The distinction is fundamental: reserves alone tell only half the story.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proof of Solvency vs Proof of Reserves — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Reserves verify assets; solvency verifies net equity.</div>

|   |   |
|---|---|
| **Proof of reserves** | Demonstrates the exchange holds claimed assets on-chain |
| **Proof of solvency** | Proves assets exceed liabilities (net worth is positive) |
| **Key limitation of reserves alone** | Silent on whether exchange owes more than it holds |
| **Solvency calculation** | Total assets − Total liabilities = Net equity (must be > 0) |
| **Audit mechanism** | Merkle tree + on-chain snapshot, or third-party ledger review |

</aside>

## Why "proof of reserves" is incomplete

An exchange can hold substantial cryptocurrency and still be insolvent if it has borrowed more money, owes more to users, or carries liabilities exceeding those assets. A **proof of reserves** audit confirms only the asset side of the balance sheet.

Consider a simplified example:

| Item | Value |
|------|-------|
| Bitcoin held | $1,000,000 |
| USD deposits from users | $900,000 |
| Loans from other firms | $200,000 |
| **Total liabilities** | **$1,100,000** |
| **Net equity** | **−$100,000** |

The exchange holds $1 million in bitcoin—proof of reserves satisfied. But the exchange is technically insolvent: it owes $1.1 million against $1 million in assets. When FTX collapsed in late 2022, it demonstrated this exact problem. The exchange had substantial assets on its balance sheet, yet liabilities (to users and counterparties) exceeded those assets by several billion dollars.

## What proof of solvency requires

**Proof of solvency** demands transparency on both sides: the full balance sheet. An auditor or third party must verify:

1. **Assets:** All cryptocurrency, fiat deposits, loans receivable, and other holdings are real and controlled by the exchange
2. **Liabilities:** All customer deposits, loans, settlement obligations, and accrued expenses are accurately recorded
3. **Net equity:** Assets − Liabilities > 0

This is far harder than proof of reserves. While cryptocurrency holdings can be cryptographically verified on-chain (an address signs a message proving control), liabilities require auditing internal ledgers and verifying claims against third parties—a task more similar to traditional bank audits.

## The technical challenge of proving both

Proof of reserves uses [blockchain](/blockchain-fundamentals/) and Merkle tree technology to prove, without revealing individual customer balances:

- The exchange controls specific addresses
- Those addresses hold assets matching published figures
- This snapshot occurred at a specific time

Proof of solvency requires the same for assets *plus* auditing of liabilities. Many schemes proposed post-FTX collapse try to combine both by:

- Publishing a cryptographic commitment to user liabilities (total balances owed to all customers)
- Verifying that published assets exceed that total
- Using privacy-preserving proofs (zero-knowledge proofs) so individual balances remain confidential

But this remains controversial. A full liability audit exposes proprietary information (total customer net worth, lending exposure, fee structure) that exchanges resist disclosing.

## Why solvency proofs matter more than reserves alone

A proof of reserves audit can pass while an exchange is quietly borrowing against its holdings, lending to undercapitalized affiliates, or carrying hidden obligations. The reputational assurance is shallow.

Proof of solvency—even approximate or periodic—offers genuine reassurance: the entity cannot be simultaneously solvent *and* fraudulent in a way that reserves-only audits miss. It answers the question: "If the exchange shut down today and liquidated all positions, would customer deposits be fully repaid?"

This is why regulators and auditors increasingly push for liabilities-inclusive verification, and why many post-2022 crypto firms have committed to annual "full" audits rather than reserves-only snapshots.

## Practical limitations of current approaches

Even true solvency proofs face obstacles:

- **Liabilities are harder to cryptographically verify** than assets, requiring trust in the exchange's ledger systems
- **Frequent repricing:** Asset values change constantly; a proof valid at Tuesday's snapshot may be outdated by Thursday
- **Third-party dependencies:** Deep liability audits require a skilled auditor, adding cost and creating dependency on an external firm's competence
- **Regulatory uncertainty:** No global standard for what "proof of solvency" must include, allowing firms to define minimal compliance

Some proposals combine periodic human audits (for liabilities) with continuous on-chain proof of assets (for reserves), a hybrid approach balancing transparency and practicality.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain fundamentals](/blockchain-fundamentals/) — underlying technology for on-chain asset verification
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — platforms where proofs of solvency are most relevant
- [Custodian](/custodian/) — role of third-party holders of assets and verification
- [Smart contract](/smart-contract/) — mechanism for automated, transparent liability tracking
- [Counterparty risk](/counterparty-risk/) — danger posed by exchange insolvency

### Wider context

- [Balance sheet](/balance-sheet/) — traditional financial statement showing assets and liabilities
- [Liquidation](/liquidation/) — process testing whether assets exceed liabilities
- [Credit rating](/credit-rating/) — external assessment of solvency and default risk
- [Distributed ledger](/distributed-ledger/) — technology enabling transparent record-keeping

</div>

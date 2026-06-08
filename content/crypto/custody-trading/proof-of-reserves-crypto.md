---
title: "Proof of Reserves"
description: "How cryptocurrency exchanges cryptographically verify they hold sufficient customer assets without exposing sensitive account data."
keywords:
  - proof of reserves
  - exchange solvency
  - cryptographic proof
  - merkle tree
  - customer assets
  - exchange custody
image: "/svg/crypto.svg"
---

*A **proof of reserves** is a cryptographic method that allows a cryptocurrency [exchange](/stock-exchange/) to publicly demonstrate that it controls sufficient customer assets without revealing individual account balances or wallet addresses. Rather than asking customers to trust management claims, exchanges publish mathematical proofs that can be independently verified.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proof of Reserves — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency concepts." />

<div class="wiki-infobox-caption">A cryptographic method for demonstrating exchange solvency without exposing customer account details.</div>

|   |   |
|---|---|
| **What it is** | A mathematical proof that an exchange holds assets corresponding to the sum of all customer balances |
| **Core mechanism** | Merkle trees or similar cryptographic structures combined with on-chain verification |
| **Purpose** | Build confidence in exchange solvency without disclosing sensitive data |
| **Frequency** | Usually performed at irregular intervals or under regulatory pressure |
| **Limitations** | Proves asset holdings, not liabilities; one-point-in-time snapshot |
| **Key assumption** | Customer cannot verify their own balance is included in the published root hash |

</aside>

## Why exchanges don't just open their books

Traditional financial institutions are subject to regulatory audits: an independent third party inspects ledgers and certifies that assets match liabilities. Cryptocurrency exchanges operate in a different environment. Many jurisdictions lack clear custody rules; regulators have no authority to audit blockchains. Customers funding exchange accounts must accept operational and counterparty [risk](/counterparty-risk/) as a condition of trading.

When a large exchange fails—as happened with FTX in late 2022—the gap between claimed assets and actual holdings becomes clear only after collapse. A proof-of-reserves scheme attempts to make that gap visible earlier, by cryptographically anchoring the exchange's claim to immutable on-chain data. The idea is sound: if an exchange proves it holds 100,000 bitcoin, and its customer liabilities total 99,000 bitcoin (which only the exchange knows), it has a safety buffer.

## How merkle-tree proofs work

The standard approach uses a Merkle tree, a data structure that compresses information into a single hash. Here's the sequence:

1. The exchange lists all customer accounts with their balances: Account A holds 1.5 BTC, Account B holds 0.8 BTC, and so on.
2. Each account is hashed (using SHA-256 or similar). Pairs of hashes are then hashed together. This process continues recursively until a single hash—the **root hash**—remains.
3. The exchange publishes this root hash. Any customer can independently verify that their account was included: they request a "Merkle proof" (the minimal set of hashes needed to reconstruct the root) and check that their balance + everyone else's produces the same root.
4. The exchange then proves it controls the assets by signing a message with a private key corresponding to a public address known to hold those assets on-chain.

This approach reveals the total liabilities (the sum of all customer balances embedded in the tree) and the on-chain holdings, without exposing individual account balances or the exchange's wallet keys.

## The verification problem that remains

A major gap persists: **the scheme proves assets, not liabilities.** If an exchange claims 100,000 bitcoin in reserves but the true customer liabilities total 150,000 bitcoin, the proof reveals nothing. The exchange can fraudulently suppress accounts or miscount balances in the Merkle tree. Customers cannot verify that their own balance is accurately included—only that *some* balance for some account exists in the tree.

Furthermore, a proof of reserves is a snapshot. An exchange might publish reserves equal to 105% of customer liabilities on a Tuesday, liquidate assets on Wednesday, and fail on Thursday. The proof becomes stale almost immediately.

Some exchanges have tried to add a "proof of liabilities" phase, asking third-party auditors to verify the Merkle tree and cross-check it against their internal ledger. This reintroduces trust in the auditor, defeating the original premise of cryptographic verification.

## On-chain vs. off-chain asset breakdown

Exchanges hold assets in multiple forms. Bitcoin and Ethereum sit on public blockchains and are auditable on-chain. But many exchanges also hold:

- **Fiat currency** in bank accounts (entirely opaque to the blockchain)
- **Stablecoins** like USDC or USDT (on-chain, but the issuer's reserve claims are separate assertions)
- **Illiquid tokens** (easily overstated in value)

A proof-of-reserves scheme is most credible when it focuses on major on-chain assets. Including fiat or illiquid holdings requires assumptions about valuation and bank account verification—exactly the trust relationships the scheme tried to circumvent.

## Regulatory and voluntary implementations

As of the mid-2020s, proof of reserves remains largely voluntary. A handful of large exchanges (Kraken, Coinbase, and others) have published periodic proofs, usually under pressure from regulators or after internal compliance reviews. Some jurisdictions with crypto licensing regimes—Singapore, Hong Kong—have begun requiring custodians to disclose reserve proofs as part of licensure.

The practice gained urgency after the 2022 collapse of FTX, which operated without transparent reserves. Regulators now view reserves proofs as a basic hygiene measure, though regulatory standards are still forming.

## Comparison to traditional bank audits

A traditional bank publishes quarterly financial statements audited by a major accounting firm. An auditor physically inspects vaults (for gold) or verifies bank balances with counterparties, then attests to solvency. This process is resource-intensive, slow, and centralizes trust in the audit firm.

A proof of reserves is faster and cheaper: the exchange publishes a hash, customers verify it in seconds using free tools. But it sacrifices the auditor's legal liability and professional judgment. Customers must weigh the convenience of instant verification against the absence of human assurance.

## See also

<div class="wiki-seealso">

### Closely related

- [Self-Custody in Crypto](/self-custody-crypto/) — Avoiding exchange risk by controlling private keys directly
- [Crypto Prime Brokerage](/crypto-prime-brokerage/) — Institutional services that include custody and collateral management
- [Custodian](/custodian/) — Financial institutions holding assets on behalf of clients
- [Distributed Ledger](/distributed-ledger/) — The immutable record that makes on-chain verification possible
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Trading platforms and their custody obligations

### Wider context

- [Bitcoin](/bitcoin/) — The largest on-chain asset, most frequently included in reserves proofs
- [Ethereum](/ethereum/) — Second-largest on-chain asset and primary venue for DeFi collateral
- [Blockchain Fundamentals](/blockchain-fundamentals/) — Public ledger mechanics underlying cryptographic proof schemes
- [Credit Rating](/credit-rating/) — Traditional solvency assessment; proof of reserves as a crypto alternative
- Risk Management — How to assess counterparty risk when custodians use partial reserves

</div>

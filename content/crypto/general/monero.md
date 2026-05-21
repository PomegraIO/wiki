---
title: "Monero"
description: "Monero is a privacy-focused cryptocurrency that obscures sender, recipient, and transaction amounts using ring signatures, stealth addresses, and confidential transactions. It prioritises anonymity over transparency."
keywords:
  - monero
  - xmr
  - privacy
  - cryptocurrency
  - ring signature
  - stealth address
image: "/svg/crypto.svg"
---

*A **Monero** (**XMR**) is a [cryptocurrency](/cryptocurrency-exchange/) explicitly designed to prioritise privacy. Unlike [Bitcoin](/bitcoin/), where transactions are transparent and pseudonymous, Monero obscures the sender, recipient, and transaction amount using cryptographic techniques, making it the primary coin used for truly anonymous transfers.*

<div class="wiki-hatnote">

This entry covers Monero's privacy features and design. For transparent blockchains, see [Bitcoin](/bitcoin/) or [Ethereum](/ethereum/); for general cryptocurrency concepts, see [blockchain fundamentals](/blockchain-fundamentals/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Monero — key facts</div>

<img src="/svg/crypto.svg" alt="Monero logo and privacy visualization" />

<div class="wiki-infobox-caption">Monero: a cryptocurrency engineered for maximum privacy.</div>

|   |   |
|---|---|
| **What it is** | A privacy-focused cryptocurrency |
| **Ticker symbol** | XMR |
| **Created** | April 2014 |
| **Consensus mechanism** | [Proof-of-work](/proof-of-work/) |
| **Hashing algorithm** | RandomX |
| **Block time** | ~2 minutes |
| **Privacy model** | Mandatory (not optional) |
| **Emission schedule** | Tail emission (ongoing block rewards) |

</aside>

## Design philosophy

Monero emerged from a predecessor coin called Bytecoin in 2014, when developers forked the project and implemented improvements. The core philosophy: privacy should be mandatory and transparent to users, not optional or technical. Every Monero transaction is private by default.

This contrasts with Bitcoin, where transparency is the default. Bitcoin proponents argue that pseudonymity is sufficient and that transparency enables auditability; Monero developers argue that pseudonymity fails under scrutiny and that true financial privacy is a fundamental right.

## Ring signatures

Monero's first privacy tool is the **ring signature**. When you send Monero, the transaction includes your actual input mixed with decoys pulled from the blockchain's recent history. Observers see a transaction from one of those addresses but cannot determine which one is genuine. This obscures the sender.

The larger the "ring size" (number of decoys), the harder it is to guess which address is real. Monero defaults to a ring size of around 15, meaning each transaction appears to come from one of 16 possible addresses.

## Stealth addresses

The second tool is the **stealth address**. When someone sends you Monero, they derive a one-time address for that specific transaction using your public key. Outside observers cannot link multiple transactions to you because each received payment uses a different address. This obscures the recipient.

## Confidential transactions

The third tool is **confidential transactions**, which hide the amount. Bitcoin shows both the input and output amounts (though not necessarily who controls them). Monero hides the amounts using a zero-knowledge proof — a cryptographic proof that the transaction is valid without revealing the amounts involved. This obscures the value transferred.

## The mining algorithm

Monero uses the RandomX hashing algorithm, designed to be memory-hard and resistant to ASIC optimisation. The goal was to keep mining accessible to ordinary CPUs and prevent the dominance of specialised hardware seen in [Bitcoin](/bitcoin/) and [Litecoin](/litecoin/). While ASICs for RandomX have since been developed, the algorithm remains more CPU-friendly than SHA-256.

## Regulatory challenges

Monero's privacy features have made it controversial with governments and regulators. Several exchanges have delisted XMR trading pairs to avoid regulatory risk, and some jurisdictions have restricted its use. Law enforcement views Monero as a tool for money laundering and ransomware payments — the latter being a major real-world problem.

Monero's privacy is so robust that even if law enforcement seizes your hardware, they cannot determine how much Monero you own or where it came from. This makes taxes and sanctions enforcement nearly impossible, a feature some celebrate and others find dangerous to the rule of law.

## Technical limitations

Monero transactions are significantly larger than Bitcoin transactions due to the cryptographic overhead of ring signatures and confidential transactions. This increases storage and bandwidth requirements, making Monero slightly slower and more resource-intensive to run.

Additionally, Monero has a "tail emission" — block rewards that do not halve but instead continue indefinitely at a small fixed amount. This prevents Monero's supply from reaching a hard cap, though the tail emission is tiny enough that Monero's effective scarcity approaches Bitcoin's over very long timescales.

## Current use cases

Monero is primarily used by privacy advocates, those circumventing capital controls, and participants in darknet markets. Its adoption for legitimate commerce is limited; most merchants cannot easily accept a payment they cannot link to their customer.

Some jurisdictions view Monero as contraband; the Indian government temporarily banned it, and South Korea's exchanges delisted it. This regulatory hostility, while good marketing to privacy advocates, limits mainstream adoption.

## See also

<div class="wiki-seealso">

### Closely related

- [Bitcoin](/bitcoin/) — transparent blockchain, contrast to Monero
- [Proof-of-work](/proof-of-work/) — Monero's consensus mechanism
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where Monero trades (with limitations)
- [Private blockchain](/private-blockchain/) — alternative privacy approach

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Distributed ledger](/distributed-ledger/) — Monero's network architecture
- [Public blockchain](/public-blockchain/) — Monero is still public; privacy applies to transactions
- [Mining Bitcoin](/mining-bitcoin/) — similar principles apply to Monero
- [Difficulty adjustment](/difficulty-adjustment/) — Monero uses this mechanism too

</div>

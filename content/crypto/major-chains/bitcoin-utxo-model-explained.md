---
title: "Bitcoin UTXO Model Explained"
description: "The Bitcoin UTXO model tracks balances as unspent transaction outputs, not account balances, affecting transaction construction, privacy, and fee calculation."
keywords:
  - bitcoin utxo model explained
  - unspent transaction outputs
  - bitcoin transaction inputs outputs
  - utxo privacy blockchain
image: "/svg/crypto.svg"
---

*Bitcoin does not track balances in accounts the way your bank does. Instead, it tracks **unspent transaction outputs** — cryptographic pieces of value that you own but that previous transactions created. This fundamental design choice affects how you spend, what fees you pay, and how traceable your activity is on the [blockchain](/blockchain-fundamentals/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">UTXO Model — Core Mechanics</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Bitcoin's balance is the sum of all unspent outputs you control; spending creates new outputs.</div>

|   |   |
|---|---|
| **What is a UTXO** | Unspent transaction output; a cryptographic claim to value created by a prior transaction |
| **Your balance** | Sum of all UTXOs your private key can unlock |
| **Spending** | Selecting one or more UTXOs (inputs) and creating new ones (outputs) for recipients |
| **Fee calculation** | Based on transaction size in bytes, not amount transferred; more inputs = higher fee |
| **Privacy implication** | Inputs reveal all addresses whose UTXOs you are spending together |
| **Contrast: account model** | Ethereum, Ripple track a running balance per address; no need to list all prior outputs |

</aside>

## How the UTXO Model Differs from Account Balances

Most financial systems you know track balances: your bank account shows a single number, your cash app balance is a running tally, Ethereum addresses show a balance. If you send $10 to Alice and $15 to Bob, your balance decreases by $25, and both recipients see their balance increase.

Bitcoin works differently. Your wallet does not hold a balance; it holds a list of **unspent outputs** — specific amounts from prior transactions that were sent to you and that you have never spent. When you "send" Bitcoin, you are not deducting from a balance; you are selecting one or more of these outputs (called inputs in the new transaction), combining their value, and creating new outputs assigned to the recipient's address.

Example: Suppose a prior transaction sent you 2 bitcoins to your address. That output sits on the blockchain, unspent, until you decide to use it. When you want to send 0.5 bitcoins to someone, you take that 2-bitcoin output as an *input* to your new transaction, create a new output of 0.5 bitcoins to the recipient, and create a second output of 1.49 bitcoins back to yourself (the 0.01 bitcoin difference is the fee). Now your original 2-bitcoin output is "spent" and no longer available; the two new outputs are unspent and belong to whoever controls the corresponding private keys.

## Why Bitcoin Uses UTXOs Instead of Accounts

The UTXO model has deep roots in Bitcoin's design philosophy: simplicity, immutability, and parallelizability.

**Immutability**: Once a transaction is confirmed, it can never be changed or reversed (short of a 51% attack). A UTXO either exists on the blockchain or it does not. There is no updating a "balance field" — no state that can be corrupted or overwritten. Every UTXO is created once and either spent or unspent.

**Parallelization**: Because UTXOs are independent objects, multiple transactions can process UTXOs in parallel without conflicts. If I spend Output A and you spend Output B, neither transaction conflicts with the other. In an account model, two transactions spending from the same account can race, and the system must order them. Bitcoin's UTXO design sidesteps this bottleneck.

**Scriptability**: Each UTXO can carry a small program (a "script") that defines the conditions under which it can be spent. A simple output requires a valid signature; a more complex one might require multiple signatures, or might be spendable only after a certain block height. The UTXO model makes it natural to attach conditions to individual units of value.

The [proof-of-work](/proof-of-work/) consensus mechanism also pairs well with UTXOs: verifying a transaction is quick (check that inputs exist, are unspent, and satisfy their scripts) and does not require knowing the account balance history.

## Building a Transaction: Inputs and Outputs

When you spend Bitcoin, your wallet software performs several steps:

1. **Gather UTXOs**: It scans the [blockchain](/blockchain-fundamentals/) for all outputs locked to your address that you have not yet spent. This is your spendable balance.

2. **Select inputs**: Your wallet chooses one or more of these UTXOs to use as inputs. A simple transaction might use one input; a wallet that receives many small payments might need to use dozens.

3. **Create outputs**: For each recipient, you create an output specifying the amount and the address (or script) that locks it. You also create an output back to yourself if you have change (the difference between total input and total output).

4. **Sign and broadcast**: You sign each input with your private key (proving you authorized the spend) and broadcast the transaction to the network.

Example transaction:
- **Input 1**: 2.0 bitcoin (from a prior transaction to your address)
- **Output 1**: 0.5 bitcoin to Alice
- **Output 2**: 1.49 bitcoin back to your address (change)
- **Fee**: 0.01 bitcoin (implicit: input minus outputs)

Once the transaction is confirmed, the 2-bitcoin input is marked spent, and the two outputs are now unspent UTXOs that others can reference in future transactions.

## How UTXO Selection Affects Transaction Fees

The fee you pay is determined by transaction size (measured in bytes or virtual bytes), not the amount transferred. A transaction that sends 0.1 bitcoins and a transaction that sends 100 bitcoins cost the same *if they have the same size in bytes*.

Transaction size is driven primarily by the number of **inputs**. Each input requires a signature and other data, adding roughly 140–180 bytes. Outputs are smaller, around 30 bytes each.

This creates a practical consequence: if your wallet holds many small UTXOs (because you have received many small payments), spending them is expensive. A transaction using 10 inputs might be 1,800 bytes, while a transaction using 1 input is 250 bytes. If the fee rate is 50 satoshis per byte, the first transaction costs about 90,000 satoshis, the second 12,500 satoshis — a 7x difference for the same amount sent.

Wallet software tries to minimize this by intelligently selecting inputs — combining small ones when necessary, but preferring fewer large ones. Some users also practice "coin consolidation," voluntarily combining many small UTXOs into fewer larger ones during low-fee periods, to reduce future spending costs.

## Privacy and the UTXO Model

The UTXO model has a subtle privacy cost: every transaction input reveals all the addresses whose outputs you are spending together *in the same transaction*. If you combine outputs from two different addresses you control in a single transaction, an observer can infer that both addresses belong to the same person.

Example: If your wallet sends you payments to address A and address B, and later you spend both A and B as inputs in the same transaction, a blockchain analyst can reasonably conclude that A and B are controlled by the same entity.

This is why many wallets and privacy-conscious users avoid mixing UTXOs from different addresses in a single transaction. Some wallets maintain separate "coins" (groups of UTXOs) and ensure that each transaction uses inputs from only one coin. Others employ coin-mixing protocols (like [CoinJoin](/smart-contract/)) to obscure which inputs belong together.

[Ethereum](/ethereum/) and other account-based blockchains do not have this particular privacy leakage, since you are simply decreasing one address's balance and increasing another's — no explicit linking of prior sources.

## UTXOs and Scalability

Bitcoin's UTXO design has implications for scalability. To fully validate a transaction, a node must check that every input refers to an existing, unspent UTXO. This requires maintaining a large "UTXO set" in memory — a database of all unspent outputs on the network.

As the number of UTXOs grows (more transactions, more fragmentation), the UTXO set grows, increasing storage and RAM requirements for nodes. This is one reason Bitcoin's block size and transaction throughput are limited: to keep UTXO set growth manageable.

Layer-2 solutions like the Lightning Network address this by moving many transactions off-chain and settling only periodically, reducing the number of on-chain UTXOs. Other approaches, like Taproot upgrades, improve script efficiency to reduce UTXO size.

## Spending Change and UTXO "Dust"

When you spend a UTXO, you must use its full value. If a UTXO contains 2 bitcoins and you want to send 0.5, you create two outputs: 0.5 to the recipient and 1.49 to yourself (change). That 1.49 is a new UTXO you now own.

Over time, wallets accumulate many small UTXOs (change from prior transactions, small payments received, etc.). These are called "dust" if they are so small that the fee to spend them exceeds their value. A 50-satoshi UTXO is economical only if future fees remain very low; if fees spike, it is uneconomical to spend.

This is another behavioral difference from account models: in Bitcoin, you must consciously manage your UTXO composition. Some wallets automate this; others leave it to the user.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledger concepts underlying UTXOs
- [Bitcoin](/bitcoin/) — the original cryptocurrency using the UTXO model
- [Proof of work](/proof-of-work/) — consensus mechanism that validates UTXO transactions
- [Smart contract](/smart-contract/) — how scripts attached to UTXOs enable programmability
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where UTXOs are bought and sold
- [Distributed ledger](/distributed-ledger/) — the data structure that records UTXOs

### Wider context

- [Ethereum](/ethereum/) — account-based alternative to the UTXO model
- [Proof of stake](/proof-of-stake/) — alternative consensus used by some UTXO-based chains
- [Volatility smile](/volatility-smile/) — applied to options pricing, not blockchain (listed for contrast)

</div>

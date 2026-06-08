---
title: "Validium Architecture"
description: "A blockchain scaling technique that uses zero-knowledge proofs to verify off-chain transactions while keeping data off-chain, trading security for throughput."
keywords:
  - validium
  - scaling
  - zero-knowledge proof
  - off-chain
  - rollup
  - throughput
image: "/svg/crypto.svg"
---

*A **validium** is a scaling layer that verifies transaction batches using zero-knowledge proofs but keeps the underlying transaction data off-chain—achieving high throughput at the cost of lower security than a full rollup.*

<div class="wiki-hatnote">

For the broader rollup ecosystem, see [Layer 2 scaling](/layer-2-scaling/). For ZK proofs, see zero-knowledge proof. For the security trade-off, see data availability.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Validium Architecture — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain and cryptocurrencies." />

<div class="wiki-infobox-caption">Speed over settlement certainty: off-chain data with on-chain proof.</div>

|   |   |
|---|---|
| **What it is** | A scaling solution in which transaction data is stored and executed off-chain, but correctness is proved on-chain using zero-knowledge proofs. |
| **Also called** | Off-chain data availability rollup; sometimes grouped with StarkNets or dYdX implementations. |
| **Key difference from rollups** | Data is not published on-chain; instead, a trusted or decentralised committee keeps it off-chain. |
| **Main advantage** | Much higher transaction throughput (thousands per second vs hundreds). |
| **Main risk** | If the off-chain data provider goes offline or censors, users cannot withdraw funds without that data. |
| **Data availability assumption** | Relies on a centralised or federated operator to keep and serve data; not guaranteed by the consensus layer. |
| **Proof mechanism** | Uses zero-knowledge proofs (often STARKs) to prove state transitions without revealing transaction details. |

</aside>

## The speed-versus-security trade-off

A traditional rollup—whether [optimistic](/optimistic-rollup/) or zero-knowledge—publishes all transaction data to the main blockchain. This is expensive: storing thousands of transactions per block consumes gas, raising per-transaction costs. But it has a decisive advantage: anyone can independently verify the history and recover user funds even if the rollup operator vanishes.

A validium ditches this guarantee. Instead of publishing data on-chain, the operator keeps transaction details in an off-chain database—say, on a private server or a federated cluster. Users interact with this off-chain system, and periodically, the operator submits a zero-knowledge proof to the main chain proving that all those off-chain transactions were valid.

The proof is cryptographically sound: if the proof is accepted on-chain, the transactions *definitely* happened correctly. The problem is data availability: if the operator disappears, no one outside the operator can prove what the current state is or recover their funds.

## How the proof works

The operator collects thousands of transactions (transfers, swaps, any action) into a batch. It then runs a prover algorithm that generates a zero-knowledge proof showing:

1. Every transaction in the batch is valid (signatures correct, balances sufficient).
2. The state transition from the old root hash to the new one is accurate.
3. No double-spends or other violations occurred.

This proof is small—usually a few kilobytes—and can be verified quickly and cheaply on the main chain. The main chain's smart contract checks the proof, updates the accepted state root, and that's it. The actual transaction data never appeared on-chain.

This is why validiums scale so well. Thousand-transaction batches are proved for roughly the cost of a single on-chain transaction. Per-transaction cost drops dramatically.

## Data availability committees and operators

To mitigate the risk that a single operator hoards data, some validium designs use a **data availability committee** (DAC)—a set of validators who collectively hold the off-chain transaction data. If the operator goes offline, the committee can reconstruct the data and allow users to exit.

This is a trade-off. A DAC reduces the single-point-of-failure risk but introduces new trust assumptions: you must trust that a quorum of the committee members are honest. If the committee colludes, users can still lose access to their funds.

dYdX v3 and Immutable X have used DAC designs. Others, like StarkNet, have moved toward keeping data availability decentralised (blurring the line between validium and zk-rollup).

## When validium makes sense

Validiums excel in high-frequency, low-stakes scenarios. A decentralised exchange running order books, a gaming platform processing thousands of moves per second, or a payment system optimised for throughput can accept the data-availability risk in exchange for near-instant settlement and minimal fees.

They make less sense for applications requiring maximum settlement certainty. If you're moving a large amount of value and need the absolute guarantee that the on-chain consensus will back your recovery, a full ZK rollup or even an [optimistic rollup](/optimistic-rollup/) with on-chain data is more prudent.

## The bridge back to the main chain

A user's funds in a validium are represented by tokens (or claims on collateral) held in a smart contract on the main chain. To exit, the user submits a withdrawal request to the validium's off-chain system. The operator includes it in the next batch, generates a proof, and submits the proof on-chain. Once the proof is verified, the smart contract releases the user's funds on the main chain.

If the operator is responsive and honest, this process is fast and cheap. If the operator is offline or censors the user, the user cannot exit unless the DAC or another mechanism can help recover the transaction data.

## Validium versus optimistic rollup

An [optimistic rollup](/optimistic-rollup/) publishes data on-chain and assumes transactions are valid unless proven otherwise within a challenge window (typically 7 days). A validium publishes no data but uses a cryptographic proof of validity immediately. Optimistic rollups are more transparent and have longer challenge periods, giving users more time to react to fraud; validiums are faster but require more immediate trust in the operator.

Neither is "better"—it depends on the application's throughput, finality, and security requirements.

## Emerging hybrid designs

The line between validium and rollup is blurring. Polygon Plasma uses a hybrid: most data is off-chain (validium-like), but the main chain periodically commits a Merkle root of the state, and users can prove their account balance against that root if they need to exit during an operator failure.

Other teams are experimenting with "data availability on demand": normally, data stays off-chain for speed, but if an operator becomes unavailable, users can submit a recovery transaction on-chain with the data included, forcing the system to re-execute the batch and update the state fairly.

These designs aim to capture validium's speed while reducing the trust assumptions and recovery risks.

## The IOU problem

A subtle but real issue with validiums: funds in a validium are not truly final until the proof is on-chain and verified. During that interval, the operator could theoretically accept a withdrawal from one user while still processing it off-chain—creating an IOU that might not be backed if the operator is insolvent. This is less common in well-run systems but remains a structural risk compared to on-chain settlement.

## See also

<div class="wiki-seealso">

### Closely related

- Zero-knowledge proof — the cryptographic tool that proves state transitions
- [Layer 2 scaling](/layer-2-scaling/) — the broader category of off-chain solutions
- Rollup — the general scaling technique of batching transactions off-chain
- ZK rollup — a validium's cousin, which publishes data on-chain
- [Optimistic rollup](/optimistic-rollup/) — the competing scaling design that uses fraud proofs
- Data availability — the fundamental trade-off in validium design

### Wider context

- Throughput — transaction capacity per unit time
- Consensus mechanism — the main-chain protocol that backs the validium
- Gas — the cost that validiums reduce by moving computation off-chain
- STARK proof — one family of zero-knowledge proof often used in validiums
- Settlement — finality and the guarantees of a validium exit
- Immutable X — a real-world NFT validium
- dYdX — a decentralised exchange validium

</div>

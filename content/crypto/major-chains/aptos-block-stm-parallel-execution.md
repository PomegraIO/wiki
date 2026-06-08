---
title: "Aptos Block-STM Parallel Execution"
description: "How Aptos's software transactional memory scheduler executes transactions in parallel and rolls back only conflicting transactions."
keywords:
  - aptos block-stm
  - parallel execution
  - software transactional memory
  - blockchain scalability
  - transaction throughput
  - optimistic execution
image: /svg/crypto.svg
---

*Most [blockchains](/blockchain-fundamentals/) execute transactions sequentially—one after another—because a smart contract running on one account might interfere with another's state, and the network must be certain no conflicts occur. **Aptos Block-STM** breaks this pattern by using **software transactional memory** to optimistically execute many transactions in parallel, rolling back only those that genuinely conflict. The result is higher throughput and lower latency than sequential execution, without sacrificing safety or decentralization.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Aptos Block-STM — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptography and blockchain." />

<div class="wiki-infobox-caption">Parallel transaction execution via optimistic rollback, not consensus-layer change.</div>

|   |   |
|---|---|
| **Execution model** | Optimistic parallel + conflict detection + selective rollback |
| **Conflict detection** | Read-write and write-write to [smart contracts](/smart-contract/) and state keys |
| **Throughput gain** | 10–100x vs. sequential, depending on conflict rate |
| **Finality** | Same as sequential; no additional consensus rounds needed |
| **Implementation** | Aptos Move language and runtime; per-block, not global ordering |
| **Trade-off** | Non-deterministic execution order; rollback overhead on conflicts |

</aside>

## The sequential execution bottleneck

Traditional blockchains like Ethereum execute transactions in the order miners or validators include them in a block. If transaction A modifies account X and transaction B reads account X, B must wait for A to finish—even if they do not conflict. This is the fundamental throughput limit: a single-threaded execution model.

Consider a high-volume payment network processing thousands of transfers per block. Most transfers touch disjoint accounts and could run in parallel without any race condition. But sequential execution forces them to queue, creating a bottleneck. Throughput is capped by the time to run a single transaction times the number of transactions per block—typically 15–20 TPS on Ethereum, despite hardware capable of much more.

[Solana](/solana/) and other "high-throughput" chains have tried to tackle this by increasing block size or lowering latency, but they do not fundamentally change the bottleneck: execution is still a serialized bottleneck on modern hardware.

## How software transactional memory (STM) works

**Software transactional memory** is a concurrency technique from academic computer science. Instead of locking resources, a thread speculatively executes code. The system tracks all reads and writes. At the end, if no conflict occurred—no other thread wrote a value this thread read, and vice versa—the transaction commits. If a conflict is detected, the transaction rolls back and retries.

In Aptos's Block-STM:

1. **Optimistic execution**: The validator reads all transactions in a block and spawns worker threads (or async tasks), each executing a transaction independently and speculatively.
2. **Read-write tracking**: Each transaction logs which state keys it reads and which it writes. A read conflict occurs if another transaction writes a key that this transaction read. A write conflict occurs if another transaction writes a key that this transaction also writes.
3. **Conflict detection**: After execution, the system compares all read-write pairs to identify conflicts.
4. **Rollback or commit**: Non-conflicting transactions commit. Conflicting transactions are rolled back, their writes discarded, and they are re-executed in a later round (or a fallback sequential order).

The algorithm repeats in waves until all transactions are conflict-free and committed. In blocks with low conflict rates (most realistic workloads), a single wave succeeds, and throughput scales with the number of CPU cores available.

## Why this works for blockchain

Blockchain applications naturally exhibit low conflict rates. Most transfers, swaps, and smart contract calls involve disjoint state—different accounts, different NFTs, different protocol parameters. A payment from Alice to Bob conflicts with a payment from Charlie to Diana only if they touch the same account, which is rare in a diverse economy.

Additionally, the blockchain imposes a total order anyway: all nodes must agree on the final state after executing a block. Block-STM does not change the consensus mechanism or final settlement. It merely uses the flexibility of the Move language and runtime to defer the full sequencing until after execution. As long as the executor outputs the same final state, the order in which it temporarily runs transactions is invisible to downstream validators.

This is different from Solana's approach, which requires application developers to declare conflicting accounts upfront in each transaction. Aptos's Block-STM requires no explicit hints; the system infers conflicts from actual read-write footprints.

## Execution and finality

A critical point: Block-STM does not change finality. A transaction is final when it is included in a block and that block is finalized by the [consensus protocol](/proof-of-stake/). The parallel execution is a local optimization within a validator's execution layer; it does not create additional consensus rounds or delay settlement. From the perspective of the network, a block is a black box: the validator outputs a final state, and that state is either accepted or rejected by consensus.

This contrasts with proposals like optimistic rollups, which require separate settlement and dispute phases. Block-STM is a pure execution optimization—faster, but not weaker in security.

## Latency and throughput gains

Measured improvements in testnet and production:

- **Low-conflict workloads** (e.g., bulk transfers between distinct accounts): 10–100x throughput increase, depending on parallelism and conflict rate.
- **Medium-conflict workloads** (e.g., a concentrated DeFi protocol with popular liquidity pools): 2–10x increase; many transactions conflict and must retry.
- **High-conflict workloads** (e.g., a single smart contract receiving all calls): near-sequential performance; the benefit is minimal.

Latency (time from transaction submission to inclusion in a block) is also reduced, because blocks are executed faster and the validator can afford more transactions per block without exceeding compute budgets.

## The rollback cost and non-determinism

Block-STM introduces two design challenges:

**Rollback overhead**: Each conflict triggers a re-execution. If a transaction is rolled back multiple times, it consumes CPU cycles. In high-conflict scenarios, rollback cost can offset parallelism gains. The system must balance aggressive parallelism (more rollbacks) against conservative execution (fewer conflicts).

**Non-deterministic execution order**: Transactions are executed in parallel, so their temporary execution order is non-deterministic. This is fine as long as the final committed state is deterministic—which it is, because the blockchain consensus layer enforces it. However, some smart contracts may rely on implicit execution order (e.g., assuming a transaction's side effects are visible to the next transaction's read). Block-STM can expose such bugs. Aptos Move, being resource-oriented and designed for parallel execution, avoids many such pitfalls, but careful contract design is still required.

## Why not everywhere?

Block-STM is not a universal solution. It works best for:

- Low-conflict state (uncorrelated accounts, disjoint data).
- Deterministic smart contract logic (no randomness or external data that depends on execution order).
- Hardware with available CPU cores (parallelism requires threads or async tasks).

It is less effective for:

- Highly contended state (a single hot account, e.g., a popular DeFi pool receiving many calls).
- Legacy contracts assuming sequential execution order.
- Single-threaded executors or validator setups without parallelism resources.

As blockchains scale and applications diversify, most will achieve high throughput through a combination of approaches: Block-STM, batching, Layer 2 solutions, and protocol-level optimizations.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart contract](/smart-contract/) — programs executed on blockchains and their execution models
- [Proof of stake](/proof-of-stake/) — Aptos's consensus mechanism, independent of execution
- [Distributed ledger](/distributed-ledger/) — consensus and finality in decentralized systems

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — how blockchains work and scale
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — real-world throughput demands from trading
- [Ethereum](/ethereum/) — reference implementation using sequential execution
- [Solana](/solana/) — alternative parallel approach via declared conflicts

</div>

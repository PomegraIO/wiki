---
title: "Sui Object-Centric Model Explained"
description: "How Sui stores blockchain state as owned objects rather than a global account tree, enabling parallel transaction execution."
keywords:
  - sui object-centric model
  - sui blockchain
  - owned objects
  - parallel transactions
  - sui consensus
  - blockchain state management
  - sui architecture
---

*The **Sui object-centric model** replaces the traditional global state tree with independently owned objects. Rather than a central ledger of accounts, each object belongs to an address and can be modified only by transactions that hold ownership rights. This architecture allows non-conflicting transactions to execute in parallel, dramatically increasing throughput.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sui Object Model — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A state architecture that prioritizes object ownership over global consensus, enabling parallel execution.</div>

|   |   |
|---|---|
| **Core principle** | State is owned objects, not accounts in a global tree. |
| **State unit** | Object, identified by a unique ID and owned by an address. |
| **Transaction type** | Either modifies owned objects (single-writer, parallelizable) or shares state (requires consensus). |
| **Parallel execution** | Non-conflicting transactions on different objects run simultaneously. |
| **Consensus layer** | Narwhal—a faster commit mechanism for transactions that touch shared state. |
| **Key benefit** | 10x–100x higher throughput than account-based chains. |
| **Design trade-off** | Programmers must think in objects and ownership; requires explicit object-passing semantics. |

</aside>

## The Account Model vs. the Object Model

Most blockchains—Ethereum, Solana, Bitcoin—use an **account model**. Every user has an account with a balance and nonce. When a transaction executes, it reads and writes to the global state tree. The blockchain must serialize transactions and apply them one at a time to ensure consistency. Even if Alice sends funds to Bob and Charlie sends funds to David simultaneously—two operations that touch entirely different accounts—the network must process them sequentially. This sequential bottleneck is why Ethereum can only process ~15 transactions per second.

Sui inverts this. Instead of accounts and a global ledger, Sui stores **owned objects**. An object is a unit of state—a token balance, an NFT, a game item, a smart contract's data—that belongs to a specific address. When you own an object, only transactions you authorize can modify it. This creates a crucial property: **if two transactions operate on different objects with different owners, they conflict with nothing and can run in parallel**.

Alice owns object A. Bob owns object B. A transaction from Alice that modifies A and a transaction from Bob that modifies B can execute simultaneously without synchronization. There is no race condition, no double-spending, no ledger inconsistency—because the objects are independently owned.

## Objects and Ownership

In Sui, an **object** is the fundamental state unit. It has:

- A unique **object ID** (a globally unique identifier)
- An **owner** (typically an address, but can also be shared or immutable)
- **Versioning** (each state change increments a version number)
- **Content** (the actual data: a coin balance, an NFT, contract state, etc.)

Objects come in three ownership flavors:

**Owned objects** belong to a single address. Only the owner can authorize a transaction that modifies the object. These are the parallelizable sweet spot—two transactions from different owners on different objects run without contention.

**Shared objects** are mutable state accessible to multiple addresses—think of a decentralized exchange's liquidity pool that many traders can swap against. Shared objects require consensus sequencing; Sui's Narwhal consensus layer must order transactions that touch them. This is slower but still much faster than Ethereum's sequential baseline.

**Immutable objects** are write-once and can be read freely by anyone without consensus overhead. This is useful for historical data, completed transactions, and other write-once records.

## Why This Enables Parallelism

The key insight: **conflicts are rare in real applications.**

In a typical DeFi session, thousands of users interact with the protocol simultaneously. Alice swaps tokens on a decentralized exchange. Bob mints an NFT. Charlie sends stablecoins to a friend. Dave plays an on-chain game. Of these four operations, how many actually conflict?

- Alice's swap touches a shared liquidity pool (requires consensus, but shares the pool with many other swaps).
- Bob's mint creates a new owned object in Bob's account (no conflict with Alice, Charlie, or Dave's operations).
- Charlie's stablecoin transfer moves coins from Charlie's owned account to a friend's owned account (only these two accounts are touched; no conflict with Alice's swap or Bob's mint).
- Dave's game action modifies Dave's owned game state (no conflict with anyone else's owned objects).

On an account-based chain, each operation must wait for the previous one to complete, even though three of the four touch completely separate state. On Sui, Bob's mint and Charlie's transfer execute simultaneously with Alice's swap, as long as the swap and its liquidity pool are consensused among the swap transactions themselves.

## Transaction Types and Execution

Sui recognizes two broad transaction classes:

**Single-writer transactions** touch only owned objects with a single owner (the transaction sender). These require no consensus—Sui's validators simply execute them in parallel, checking that the sender owns the objects being modified and has sufficient balance or rights. Confirmation is instant.

**Multi-writer (consensus) transactions** touch shared objects or involve multiple owners. These are ordered through Narwhal, Sui's high-throughput consensus layer. Narwhal batches transactions, orders them, and broadcasts the result to validators for execution. Because shared-object transactions are a smaller fraction of total traffic, the consensus bottleneck is modest compared to a fully sequential chain.

## Practical Implications for Developers

Building on Sui requires thinking in objects and ownership.

A developer writing a decentralized exchange must model:

- User **coin objects** (owned by each trader; can be moved in parallel)
- A **liquidity pool object** (shared; requires consensus ordering for swaps)
- An **order book** or **price curve** (shared state, also consensus-ordered)

When a trader swaps, the transaction:
1. Reads the liquidity pool (shared object)
2. Consumes the trader's input coin (owned object)
3. Creates a new output coin (owned object)

Steps 1 and 3 are clear. But step 2 is critical: ownership allows the validator to confirm that only this specific trader can spend this specific coin. No double-spending, no signature forgery.

By contrast, on Ethereum, the contract must maintain a mapping of balances inside a single contract storage tree. Every swap must read and write to that tree. The tree becomes the bottleneck.

## Narwhal: Consensus for Shared State

When a transaction touches shared state, Sui routes it to **Narwhal**—a two-stage consensus protocol optimized for throughput. Narwhal separates **mempool and ordering** from **finality**.

In the first stage, validators collect transactions into batches and gossip them around the network. This is fast; no voting required.

In the second stage, validators run a standard Byzantine Fault Tolerant (BFT) consensus to order the batches. BFT is slower but still much faster than proof-of-work or even Ethereum's current consensus, because Sui already committed to holding the set of validators constant.

Shared-object transactions are ordered by Narwhal and executed afterward. The ordering is deterministic, preventing double-spending and race conditions on shared state.

## Performance Implications

The architecture delivers substantial throughput gains. In practice:

- **Owned-object transactions** (the majority): 10,000+ TPS feasible, latency ~500ms.
- **Shared-object transactions** (minority): limited by Narwhal ordering, typically 1,000–5,000 TPS per validator set, latency ~1–2 seconds.

A typical blockchain application—a game with owned player assets, an exchange with a shared liquidity pool, a social network with owned user profiles—will see 70–90% of transactions be single-writer, parallelizable operations. Only swaps, mints from a shared pool, or cross-user interactions hit the consensus layer.

## Design Trade-Offs

The object model's parallelism comes at a cost. **Programming is more complex.** Smart contract developers must reason about ownership, object passing, and which operations require consensus. Ethereum's mental model—"my contract state is a big map, I read and write to it"—is simpler, even if it is slower.

**Tooling is less mature.** Sui's [smart contract language, Move, is newer than Solidity. Fewer libraries, fewer examples, fewer battles fought and lessons learned.

**Liquidity fragmentation.** If an asset is owned by multiple users, it cannot be locked in a single vault the way Ethereum's ERC-20 standard assumes. Sui applications must design for distributed ownership, which can fragment liquidity.

But for applications that prioritize throughput—games, social networks, payments, high-frequency trading—the trade-off is worth it.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum/) — the account-based architecture that Sui contrasts with
- [Proof-of-stake](/proof-of-stake/) — Sui's consensus foundation
- [Smart contract](/smart-contract/) — the programs that manage objects on Sui
- [Blockchain fundamentals](/blockchain-fundamentals/) — state, transactions, and consensus
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — a shared-object use case on Sui

### Wider context

- [Distributed ledger](/distributed-ledger/) — the broader category of which Sui is an instance
- Consensus — Narwhal and BFT mechanisms underpinning Sui
- Parallel processing — the computer science principle enabling Sui's throughput
- Transaction finality — how Sui confirms transactions in different object categories

</div>

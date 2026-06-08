---
title: "Preconfirmations in Rollup Transactions"
description: "How preconfirmation mechanisms on rollup transactions provide near-instant soft finality before formal batch inclusion, and how they differ from true settlement."
keywords:
  - preconfirmations rollup transactions
  - soft finality blockchain
  - rollup transaction confirmation
  - preconfirmation protocol
  - liveness and safety rollups
image: /svg/crypto.svg
---

*When a user submits a transaction to an Ethereum rollup, they typically wait 5–30 seconds for that transaction to be batched and posted to the main chain. **Preconfirmations in rollup transactions** create an intermediate step: a sequencer or operator cryptographically commits to including the transaction, offering "soft finality"—near-certainty that the transaction will be executed, but not legally final until it appears on-chain. This paper-over bridges the gap between user desire for instant settlement and the rollup's need for cost efficiency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Preconfirmations — Key Mechanics</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A sequencer promise, not a guarantee; reverts are possible if the batch fails.</div>

|   |   |
|---|---|
| **Soft finality window** | 100 ms – 5 seconds after submission |
| **Hard finality** | 1–30 minutes, when batch is posted and confirmed |
| **Operator role** | Sequencer signs a preconfirmation receipt; takes on reversion risk |
| **Failure mode** | If sequencer crashes or is censored, preconfirmed txs may not appear in next batch |
| **Economic incentive** | Operator profits from MEV; preconfirmations enable MEV extraction |
| **Slashing risk** | If operator violates preconfirmation, capital is at risk (depends on design) |

</aside>

## The timing problem and why it matters

Rollups achieve cost reduction by bundling thousands of user transactions into a single batch, then posting that batch to Ethereum mainnet. Posting a batch costs ~$10–50 in gas fees; spreading that across 1,000 transactions is ~$0.01–0.05 per transaction.

But the user has to wait. After submitting a transaction to the rollup:

1. **The transaction enters the mempool** (milliseconds). The sequencer (a privileged operator) receives it and orders it.
2. **The sequencer orders and executes it locally** (seconds). The user's wallet sees a "pending" status, but nothing is final.
3. **The sequencer batches it and posts to mainnet** (5–30 seconds). Only now does Ethereum consensus secure the transaction.
4. **Ethereum confirms the batch** (minutes). After 12+ Ethereum blocks, the batch is cryptographically irreversible.

From the user's perspective, steps 1–2 feel slow. A trader on a centralized exchange gets fills in milliseconds; a rollup user waits 5+ seconds just to see a transaction appear on-chain. For DeFi, this latency matters: MEV, slippage, order races.

## How preconfirmations close the gap

A preconfirmation is a signed commitment by the sequencer: *"I promise to include your transaction in my next batch and execute it at the state I'm about to commit."* In exchange, the user gets immediate psychological feedback—"your swap is as good as done"—without waiting for on-chain finality.

Mechanically:

1. User submits transaction to sequencer.
2. Sequencer signs a preconfirmation receipt: `"Hash X will execute at block 1234, with this exact output."` This is a cryptographic signature, not just a message.
3. User sees preconfirmation and can act: accept the swap, move funds, etc.
4. Sequencer then includes the transaction in a batch posted to mainnet.
5. Mainnet confirms the batch, achieving hard finality.

From the user's view, preconfirmation + mainnet posting = two security checkpoints. Preconfirmation is risk-on (assumes operator honesty); mainnet is risk-off (assumes mainnet consensus).

## Soft finality vs hard finality

**Soft finality** is the preconfirmation. The operator has committed, but that commitment can be broken if:

- The sequencer crashes before batching
- The sequencer is censored or offline
- The operator violates the preconfirmation (rare, but economically rational if the operator has an incentive to reorder transactions for MEV)
- The batch is invalid (state transition bug), causing reversion

In practice, these failures are rare. A well-capitalized operator losing a preconfirmation is bad PR and economically wasteful. But they can happen.

**Hard finality** is when the batch is on mainnet and Ethereum has confirmed it (12+ blocks, ~3 minutes). At this point, reversing the transaction requires a mainnet reorg—essentially impossible without a 51% attack.

## The MEV and ordering problem

Preconfirmations solve a deeper problem: MEV extraction.

On Ethereum mainnet, a searcher can see a pending transaction in the mempool, insert their own profitable transaction in front of it (sandwich), and profit. The user's transaction is included, but they lose value to the searcher.

On rollups, the sequencer is the MEV extractor. If a user submits a large swap, the sequencer can reorder transactions, extract MEV, and keep the profit. This is a form of centralization and unfairness.

Preconfirmations *mitigate* this by committing the sequencer to an order and state *in advance*. Once a preconfirmation is signed, the sequencer cannot reorder that transaction without violating the commitment. This removes the sequencer's ability to sandwitch or front-run after the fact.

However, the sequencer can still extract MEV from *other* transactions—those not preconfirmed. And a preconfirmation doesn't prevent the sequencer from learning about a transaction and adjusting *other* market activity accordingly.

## Slashing and economic security

Some rollup designs add a slashing mechanism: if the sequencer violates a preconfirmation (includes a reordered or invalid transaction), the operator's capital is penalized. This creates an economic cost to breaking the commitment.

The design varies:

- **Optimistic rollups** (Arbitrum, Optimism): Preconfirmations are soft and not slashed on-chain. Operators rely on reputation and self-interest.
- **ZK rollups with sequencer stakes**: Operators post collateral; preconfirmation violations trigger slashing via on-chain proof.
- **Builder/proposer-separation models** (similar to Ethereum PBS): Sequencers bid to order transactions; violations are caught by provers and slashed.

Without slashing, preconfirmations are weaker. With slashing, they approach certainty—but require the operator to post real capital, raising operational costs.

## Failure modes and recovery

**Single sequencer censorship:** If the operator is offline or malicious and refuses to batch preconfirmed transactions, users lose. The mainnet has no way to know which transactions were preconfirmed; it just sees a valid batch with missing transactions. Some rollups add a sequencer lease: if the operator is offline for N blocks, control passes to a second sequencer. This adds latency but ensures recovery.

**State divergence:** If the operator preconfirms a transaction at state S1, but then executes it at state S2 (after new blocks), the transaction may fail or produce different output. Preconfirmations mitigate this by timestamping the exact block height at which the transaction will execute. But if the sequencer doesn't hit that block (e.g., due to reorg), the preconfirmation is void.

**Batch invalidity:** If the batch posted to mainnet is invalid (e.g., a zk-proof is wrong, or an optimistic-rollup fraud proof is filed), the entire batch reverts. Preconfirmed transactions revert with it. The operator is responsible for refunding users or eating the loss.

## Preconfirmations vs proposer-builder separation

Ethereum itself is moving toward proposer-builder separation (PBS) on mainnet, which creates similar layering: builders (who order transactions) are separate from proposers (who commit blocks). Rollups are essentially mimicking this structure by letting sequencers preconfirm, then relying on mainnet for final settlement.

The key difference: on rollups, the sequencer is centralized and trusted (at least for soft finality). On Ethereum with PBS, builders are decentralized, and proposers are chosen by [proof-of-stake](/proof-of-stake/). This gives mainnet stronger decentralization and harder finality.

## Practical implications for users

From a user's perspective:

- **Preconfirmations enable near-instant feedback** for swaps, trades, and transfers without trusting the sequencer with custody (your funds are still locked in a smart contract).
- **Reversion risk is low but nonzero.** If you're trading stablecoins, the risk is minimal. If you're trading illiquid tokens or relying on a specific slippage boundary, the risk is higher (price could move between preconfirmation and mainnet confirmation).
- **MEV is reduced but not eliminated.** Sequencers extract less MEV from preconfirmed transactions, but more from others. Users who want MEV-resistance should use preconfirmations and accept slightly slower settlement, or use encrypted-mempools and threshold encryption schemes (more complex, higher latency).

## See also

<div class="wiki-seealso">

### Closely related

- Rollup — Layer 2 scaling technology using batching
- Sequencer — Operator ordering transactions on rollups
- Soft finality — Near-certain, revocable settlement
- [Maximal extractable value](/maximal-extractable-value/) — Profit from transaction ordering
- [Optimistic rollup](/optimistic-rollup/) — Settlement type where preconfirmations are most common
- ZK rollup — Alternative rollup design with different finality guarantees

### Wider context

- [Blockchain finality](/blockchain-finality/) — Hard vs soft settlement
- Layer 2 — Scaling solutions and latency tradeoffs
- Ethereum scalability — Context for rollup adoption
- Cryptographic commitments — How preconfirmations are signed and verified

</div>

---
title: "Calldata Compression"
description: "Encoding techniques that reduce the size of rollup transaction batches posted to layer-1 chains, lowering per-transaction data-availability costs."
keywords:
  - calldata compression
  - rollup scalability
  - data encoding
  - layer-2 costs
  - transaction batching
image: "/svg/crypto.svg"
---

*[**Calldata compression**](#) is the process of encoding a rollup's transaction batch into the smallest possible byte representation before posting it to layer-1 chain storage. By removing redundancy, reusing state roots, and exploiting patterns in transaction data, rollups can reduce per-transaction costs by 50–90% — transforming data fees from the dominant cost into a rounding error.*

In [optimistic-rollup](/optimistic-rollup/) and zk-rollup systems, the sequencer bundles thousands of transactions and periodically publishes them to Ethereum (or another settlement layer) as calldata. Each byte of calldata costs gas — historically 16 gas per byte, now 4 gas per byte after EIP-4844 blobs. Even at 4 gas per byte, a typical transaction generates 100–200 bytes of data. For a user paying $5 to send a stablecoin, calldata fees can be $2–3 of that cost.

Compression attacks that ratio. If you shrink calldata by 75%, you shrink costs proportionally. Most modern rollups compress aggressively — some users pay under a cent in data fees.

## Redundancy elimination

Transactions share common fields: sender address, recipient address, nonce, token type. If you are posting a batch of 1,000 transfers, the recipient is often the same contract; the token is always the same stablecoin. Raw encoding would repeat these 1,000 times. Compressed encoding stores them once and references the index.

Signatures are even bigger targets. A transaction signature is 65 bytes. A batch signature — one signature over all transactions — is also 65 bytes. By aggregating signatures cryptographically, a rollup can drop per-transaction signature overhead from 65 bytes to negligible.

Some rollups use threshold cryptography or BLS signatures that batch even more efficiently, letting 1,000 transactions share a single 48-byte proof.

## Delta encoding

Instead of storing absolute values, store only the differences. If transaction 1 sends 1 million tokens and transaction 2 sends 1,000,100 tokens, store the first value in full and the second as "+100". This works especially well for nonces and balances, which increment linearly.

For addresses, you can store the first sender in full (20 bytes), then store only the low byte of subsequent senders if they are clustered, or use variable-length integers. A batch dominated by a few senders can save 95% on address bytes.

## Bit packing and type selection

Transactions have flags: is it a deploy? A call? A transfer? Most transactions are ordinary transfers. You can use 1 bit per transaction to indicate type, then use type-specific compact encoding. A transfer of a standard token might be just 21 bytes: 1 byte type, 4 bytes token, 8 bytes amount, 8 bytes recipient.

Rollups can also use variable-length integers. If an amount is under 256, store 1 byte instead of 32. If a nonce is under 16 million, store 3 bytes. For batches of small-value transactions, this slashes overhead significantly.

## State root and tree compression

Some rollups only publish the root hash of the new state tree, not the full tree. Validators can request sparse Merkle proofs of specific accounts if they need to verify. This trades off availability (you need the full tree off-chain) for on-chain size.

Others use merkle-tree subtree hashing to compress. If a subtree did not change, store its hash once. If it changed, store only the changed leaves and their paths. For a batch where most accounts are untouched, you save enormous amounts of space.

## Account abstraction and abstract transactions

New transaction formats like ERC-4337 abstract transactions move signature and nonce data off-chain entirely. The rollup posts only the execution intent: "set balance X to Y". Validation happens off-chain through a mempool service. This can shrink per-transaction overhead to a few bytes if you batch many intents together.

Some rollups also let users propose transactions in custom format — not raw EVM calldata but a higher-level language that encodes intent more compactly.

## Modern trade-offs: calldata vs. blobs

Before EIP-4844, all rollup data went into Ethereum calldata at 16 gas per byte. That made compression critical; a 10% compression gain was worth weeks of engineering. EIP-4844 introduced blob space at 4 gas per byte, with larger capacity and auto-expiring data.

Blobs reduced the urgency slightly — you can now post less-compressed data for the same cost. But compression remains valuable. A rollup that compresses from 100 bytes to 30 bytes per transaction saves 70%, whether the data costs 16 gas or 4 gas per byte.

Some rollups now use blobs for compressed calldata and reserve Ethereum calldata for the minimal state root and fraud-proof challenge data. This hybrid approach minimises settlement costs.

## Limits and diminishing returns

Compression has limits. You cannot remove data that validators need to reconstruct the state. If a transaction modifies an account's storage, the new value must be present somewhere in the batch or provably derivable. Heavy compression obscures this information, making [fraud-proof-mechanism](/fraud-proof-mechanism/) proofs slower to generate.

ZK-rollups face a different trade-off: the proof circuit must handle compressed data, which is more complex than handling plain transactions. If the circuit grows too large, proof generation becomes prohibitively expensive. Most ZK-rollups compress moderately to balance data cost with proof time.

## See also

<div class="wiki-seealso">

### Closely related

- [Optimistic Rollup](/optimistic-rollup/) — Rollup architecture relying on calldata for [fraud-proof-mechanism](/fraud-proof-mechanism/) verification
- [Modular Blockchain Design](/modular-blockchain-design/) — Data-availability layers handling compressed rollup batches
- [Validity Proof](/validity-proof/) — ZK-rollup proofs over compressed transaction sets
- Merkle Tree — Structure enabling sparse proof compression

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — Transaction models underlying rollup encoding
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Markets where low-fee rollups gain adoption
- [Distributed Ledger](/distributed-ledger/) — Settlement layers receiving compressed batches

</div>

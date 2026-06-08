---
title: "Modular Blockchain Design"
description: "Architecture separating execution, settlement, data availability, and consensus into specialised layers rather than monolithic chains."
keywords:
  - modular blockchain
  - execution layer
  - settlement layer
  - data availability
  - consensus
  - rollup
image: "/svg/crypto.svg"
---

*A **modular blockchain** decomposes the four functions of a traditional blockchain — execution, settlement, data availability, and consensus — into independent layers. Instead of one chain handling everything, each function runs on a specialised network, allowing blockchains to optimise for throughput, cost, or finality instead of forcing a one-size-fits-all design.*

Monolithic blockchains like Bitcoin and Ethereum do all four jobs simultaneously. They execute transactions, order them, store their data, and commit to the result through consensus. This guarantees security but creates a bottleneck: you can only process as many transactions as your consensus layer can secure, data-availability layer can store, and execution layer can compute. You cannot improve one without degrading the others.

Modular design breaks that constraint. An execution layer can focus purely on running smart contracts as fast as possible, knowing that settlement (finality commitment) and data availability happen elsewhere. This lets different networks optimise independently and compose together.

## The four layers

**Execution** is the state machine: running smart contracts, updating balances, processing transactions. It is pure computation, no consensus or publishing required. A modular execution layer can be faster and more expressive than a monolithic chain because it does not need to broadcast every operation to thousands of validators.

**Settlement** is the finality layer — usually Ethereum mainnet or another trusted blockchain. An execution layer submits batches or proofs of its state to settlement, and once settled, the state is considered final and secure. Settlement gives the execution layer economic security borrowed from the mainnet's consensus.

**Data availability** (DA) is the promise that transaction data can be retrieved and verified. In a monolithic chain, this is guaranteed by the blockchain itself — every node stores every block. In modular design, a separate DA layer (like [Ethereum dencun](/) or a dedicated DA chain) provides this guarantee. Rollups post commitments to execution, then post calldata or blobs to DA, so anyone can reconstruct the state.

**Consensus** is agreement on the canonical ordering and state of transactions. In monolithic chains, consensus is deep — every validator runs the full state machine. In modular design, consensus can be outsourced. A rollup might use a permissioned sequencer (centralised consensus) and rely on settlement and DA layers to prevent censorship.

## Execution layer examples

A modular execution layer is typically an Ethereum rollup: [Optimism](/optimism/), Arbitrum, or Starknet. These run their own virtual machine and state tree, optimised for speed or cost. Optimism runs the EVM at high throughput. Starknet uses Cairo bytecode, enabling more aggressive proof compression.

Execution layers do not need to be rollups. Sovereign rollups (no mainnet settlement) and app-chains (custom consensus for a single application) are also modular — they handle execution and lean on external DA and consensus infrastructure.

## Data availability layers

Historically, rollups posted all transaction data to Ethereum as calldata, paying by the byte. Modern DA layers like Ethereum's blob space (EIP-4844) and dedicated DA chains like Celestia offer cheaper, higher-throughput alternatives.

A DA layer's job is simple: store data and prove it was stored. Celestia does this with [blockchain-fundamentals](/blockchain-fundamentals/) — it runs a simple blockchain that stores data and uses [fraud-proof-mechanism](/fraud-proof-mechanism/) logic to punish nodes that claim data is available when it is not. Ethereum blob space is just sequestered space with lower-cost calldata. Both work; the choice depends on cost, throughput, and trust assumptions.

## Settlement and finality

A modular execution layer settles to a mainnet to inherit its security. If Ethereum has $100 billion of validators staked and a 32 ETH minimum stake, an Optimism transaction settled on Ethereum is as hard to revert as an Ethereum transaction itself. The execution layer's own sequencer or validators do not need to be well-funded — the mainnet's economic security shields them.

Alternatives exist. A rollup could settle to a custom consensus layer run by a set of trusted validators, accepting weaker security for higher performance. Or it could be sovereign and rely purely on [distributed-ledger](/distributed-ledger/) honest-majority assumptions to prevent double-spends.

## Composability and fragmentation

Modular design enables new combinations. A team can launch an execution layer on top of Ethereum + Celestia in weeks, borrowing security from both without running their own consensus. This is powerful for rapid iteration and risk reduction.

The drawback is composability friction. Applications on different execution layers cannot atomically interact without bridges. Cross-layer transactions are slow and expensive. If Ethereum's ecosystem is tightly integrated, a fragmented modular stack can feel clunky — you must choose one execution layer and accept isolation from others.

## Trade-offs in practice

Monolithic chains prioritise cohesion and simplicity. Modular chains optimise for one metric — throughput, cost, or programmability — and outsource the rest. Monolithic blockchains like Bitcoin are hard to scale but easy to reason about. Modular stacks like Arbitrum or Optimism are faster and cheaper but require coordinating multiple layers and trusting their operators.

Most modern blockchain designs are hybrid. Ethereum is nominally monolithic but increasingly modular as rollups take transaction volume and blobs replace calldata for DA. New L1s like Solana try to remain monolithic but are creeping toward modularity.

## See also

<div class="wiki-seealso">

### Closely related

- [Fraud Proof Mechanism](/fraud-proof-mechanism/) — Challenge-based security used in optimistic rollups
- [Validity Proof](/validity-proof/) — Cryptographic alternative enabling instant finality
- [Calldata Compression](/calldata-compression/) — Technique for reducing data-availability posting costs
- [Distributed Ledger](/distributed-ledger/) — Base layer technology for modular stacks
- [Blockchain Fundamentals](/blockchain-fundamentals/) — Consensus and cryptography underpinning all layers

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where modular-chain assets trade
- [Bitcoin](/bitcoin/) — Canonical monolithic blockchain design
- [Ethereum](/ethereum/) — Increasingly modular through rollups and EIP-4844

</div>

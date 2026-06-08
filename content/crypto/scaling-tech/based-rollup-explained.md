---
title: "Based Rollup: How Ethereum L1 Sequencing Works"
description: "How based rollups delegate transaction sequencing to Ethereum L1 validators, and the trade-offs between liveness, MEV exposure, and decentralization."
keywords:
  - based rollup ethereum sequencing
  - layer 2 scaling
  - ethereum rollups
  - mev sequencer
  - liveness guarantees
image: /svg/crypto.svg
---

*A **based rollup** is a Layer 2 chain that outsources transaction sequencing directly to Ethereum's own validators rather than running a dedicated sequencer, trading speed and MEV isolation for cryptographic liveness guarantees.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Based Rollup — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Sequencing by L1 validators rather than a central operator.</div>

|   |   |
|---|---|
| **Sequencing** | Ethereum validators order L2 transactions; no separate sequencer |
| **Liveness guarantee** | Transaction inclusion is certain if the chain stays alive |
| **MEV exposure** | L2 MEV flows to L1 validators; harder to hide |
| **Latency** | Slower than centralized rollups (Ethereum block time) |
| **Decentralization** | Native to Ethereum's validator set; no new consensus layer |
| **Key trade-off** | Liveness + transparency vs. speed and MEV efficiency |

</aside>

## How based rollup sequencing differs from centralized alternatives

Standard [Layer 2](/layer-2-scaling/) rollups designate a single sequencer—a trusted operator who collects transactions from users, orders them, executes them, and batches the results into bundles posted to Ethereum. This centralization is pragmatic: one operator can sequence blocks in milliseconds, absorb MEV privately, and reduce posting overhead. But it introduces a single point of failure. If the sequencer goes offline, falls victim to regulatory action, or is targeted by censorship, the chain stalls.

A based rollup inverts this. The L2 chain logic runs *on* Ethereum itself—typically as a smart contract or through derived state—and uses Ethereum's own block proposers to sequence L2 transactions. When an Ethereum validator builds the next block, that block includes both Ethereum transactions *and* an ordered set of L2 transactions. The L2 chain's canonical ordering becomes: "whatever order the L1 validators imposed." This is borrowed security: you cannot separate L2 liveness from L1 liveness. As long as Ethereum runs, your L2 transaction will eventually be included.

## Why liveness matters more than you'd think

A centralized sequencer failing looks catastrophic but recovers quickly—operators can be replaced, forced to exit, or replaced by governance. The real risk is *censorship*: an operator who silently refuses to sequence your transaction. You may not even know it happened; the operator can selectively order transactions, creating a private dark pool.

In a based rollup, censorship becomes impossible at the protocol level. An Ethereum validator who refuses to include your L2 transaction is refusing to propose a valid Ethereum block, which costs them their block reward and staking balance. The incentive structure is aligned: validators earn rewards for including all valid transactions, not for prioritizing some users over others.

This comes at a cost: Ethereum's 12-second block time sets a hard lower bound on L2 confirmation time. A centralized sequencer might finalize a transaction in under one second. With based sequencing, you wait for the next Ethereum block and the finality that follows.

## MEV: who captures it, and how

Maximum Extractable Value—the profit available from reordering or front-running transactions—flows to whoever controls sequencing. In a centralized rollup, the sequencer captures this value. In a based rollup, it flows to Ethereum's block proposers (the validators building the L1 block). This has two effects:

**First, MEV becomes visible.** L2 transactions are now in the L1 mempool, visible to all node operators and bots. MEV techniques like sandwich attacks apply directly. There's no privacy gained by moving to L2.

**Second, MEV incentives align with Ethereum security.** Instead of creating a separate MEV economy on L2, based rollups inherit Ethereum's MEV supply chain. Validators and block builders already have infrastructure, watchtowers, and business relationships optimized around L1 MEV capture. Adding L2 MEV to the same system doesn't materially change the game.

For users, this is a wash. You're exposed to the same MEV as on L1, just slightly more. For the protocol, it's a feature: you're not creating a new form of privilege or a separate rent-extraction layer.

## Practical throughput and cost trade-offs

Because based sequencing piggybacks on Ethereum's block time, throughput is bounded by how much data you can fit in an Ethereum block for L2 transactions. A modern Ethereum block is ~128 KB of blob space (post-EIP-4844). If each L2 transaction is ~200 bytes, that's roughly 600 transactions per Ethereum block, or ~50 per second. A centralized sequencer can achieve 1,000+ per second.

Transaction cost is similarly tied to L1 gas. Each L2 transaction must be included in an Ethereum block and pay the data fee. For a simple transfer (~100 bytes), that's ~$0.01–$0.05 depending on L1 congestion. A centralized rollup posting infrequent large batches can amortize this cost, bringing per-transaction fees to a fraction of a cent. The trade-off is real: liveness and decentralization cost throughput and efficiency.

## Implementation details and safety properties

Based rollups are typically implemented as contracts on Ethereum that execute L2 state transitions and verify fraud proofs or zero-knowledge proofs of correctness. The "sequencing" step is implicit: the L2 reads the ordering of its transactions from the Ethereum chain itself. When a validator includes L2 transactions in an Ethereum block, those transactions are canonically in that order, period.

The safety property is critical: a based rollup cannot fork unless Ethereum forks. The moment you have a canonical L1 chain, you have a canonical L2 ordering. There's no ambiguity, no competing rollup chains, no censorship windows.

Liveness is equally strong: any user can force their transaction onto L2 by submitting it to the Ethereum mempool. No sequencer opt-out, no pre-confirmation mechanism, no special ordering key. Ethereum's consensus will eventually include it.

## When based rollups make sense

Based rollups are ideal for applications where liveness and decentralization are paramount and throughput is secondary. Examples include governance tokens, staking bridges, and custody systems where transaction inclusion is non-negotiable. They're less suitable for high-frequency trading or mobile payments where sub-second latency is essential.

As Ethereum's base layer matures and danksharding raises data availability capacity, based rollups become more attractive economically. The throughput ceiling rises, and the cost per transaction falls. Over time, the gap between based and centralized sequencing may narrow enough that the liveness guarantee outweighs the speed loss.

## See also

<div class="wiki-seealso">

### Closely related

- [Layer 2 Scaling](/layer-2-scaling/) — overview of scaling solutions and their design trade-offs
- MEV and Sequencer Markets — deeper dive into MEV capture and who benefits
- Ethereum Consensus Finality — how L1 finality cascades to L2 chains
- Rollup Architecture — distinction between optimistic and zero-knowledge rollups
- Blockchain Liveness — liveness guarantees and censorship resistance

### Wider context

- Ethereum Validators — how L1 proposers are selected and incentivized
- [Distributed Ledger](/distributed-ledger/) — consensus and data availability foundations
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where L2 assets trade and liquidity migrates

</div>

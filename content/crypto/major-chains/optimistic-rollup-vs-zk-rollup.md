---
title: "Optimistic Rollup vs ZK-Rollup"
description: "Optimistic rollups use fraud proofs and a challenge period; ZK-rollups use validity proofs and settle faster. Each trades cost, speed, and verification complexity differently."
keywords:
  - optimistic rollup vs zk rollup
  - fraud proof
  - validity proof
  - rollup comparison
  - zero-knowledge rollup
  - ethereum scaling
---

*An **optimistic rollup** assumes transactions are valid unless proven false; it relies on a challenge period during which anyone can submit a fraud proof to dispute a batch. A **ZK-rollup** generates a cryptographic validity proof that mathematically certifies the batch is correct without needing re-verification. The choice between them involves fundamental trade-offs in computation cost, withdrawal speed, and complexity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Optimistic vs ZK-Rollup — Key Differences</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Two proof models lead to different security timelines and computational burdens.</div>

|   |   |   |
|---|---|---|
| **Aspect** | **Optimistic Rollup** | **ZK-Rollup** |
| **Proof method** | Fraud proof (reactive) | Validity proof (proactive) |
| **Computation cost** | Low; no complex math | High; extensive cryptography |
| **Withdrawal time** | 7+ days (challenge period) | Minutes to hours |
| **Finality assurance** | After challenge window passes | Upon proof verification |
| **Complexity** | Moderate (fraud proof logic) | High (proof circuits) |
| **Current examples** | Arbitrum, Optimism | zkSync, Polygon Hermez |

</aside>

## The Optimistic Model

Optimistic rollups operate on a simple assumption: assume every sequencer batch is correct. Users and applications see their transactions finalized almost immediately on the rollup. However, the rollup's final settlement to the base layer—and the user's ability to withdraw funds—is delayed by a **challenge period**, typically 7 days on Ethereum. During this window, anyone (a "verifier" or "challenger") can download the batch data, re-execute the transactions, and check the claimed state root. If the sequencer claimed an incorrect result, the challenger submits a cryptographic proof showing exactly where the computation went wrong.

When a valid fraud proof is detected, the batch is rolled back, the sequencer loses a bond (a stake held in the contract), and a new state is restored. This mechanism is elegant: computation is cheap and fast (just standard transaction execution), and the sequencer is incentivized to be honest because the cost of being caught far exceeds the cost of behaving correctly.

The challenge period is necessary because the base layer needs time for someone to potentially submit a fraud proof before permanently accepting the rollup's new state. Without that delay, the sequencer could lie and vanish before anyone caught it.

## The Zero-Knowledge Model

ZK-rollups take the opposite approach: generate a mathematical proof upfront that the batch is correct. The sequencer performs the computation off-chain, then produces a cryptographic certificate (a "validity proof" or "succinct proof") that can be verified by anyone in milliseconds. The base-layer contract checks the proof and immediately accepts the new state. No challenge period, no waiting—the rollup is final as soon as the proof is accepted.

The cost lies in proof generation. Creating a ZK proof requires solving complex cryptographic equations for every transaction in the batch. Powerful hardware and sophisticated algorithms are needed. However, because the proof is verifiable in seconds and requires no re-execution, the result is faster withdrawal times and a simpler finality model (the proof is either valid or it is not; there is no subjective challenge phase).

## Computational and Economic Implications

The computation-cost difference is profound. An optimistic rollup's sequencer runs a standard EVM or VM, executing each transaction exactly as it would on the base layer. This is well-understood and fast. The verifier also just re-runs the same computation. The base-layer smart contract needs only to verify a fraud proof showing a single step where computation diverged—typically a few kilobytes of data.

A ZK-rollup sequencer must convert transaction execution into a **constraint system** or **circuit**, a mathematical representation of the computation. It then executes those constraints and generates a proof (using zk-SNARKs, zk-STARKs, or other schemes) that is compact and instantly verifiable. This adds significant CPU and specialized-hardware demand, making ZK-rollup operators more capital-intensive.

However, the proof size is tiny—often 100 bytes to a few kilobytes—so data-posting costs to the base layer remain low. And because the proof is verified in seconds on the base layer, final settlement is near-instant, unlocking faster withdrawal and cross-chain communication.

## Security and Trust Assumptions

Both models are cryptographically secure, but they distribute trust differently. An optimistic rollup trusts that at least one honest verifier exists and is watching the chain. If no one challenges a fraud, or if all potential challengers are colluding with the sequencer, false batches slip through. This is a **liveness assumption**: someone must be awake and willing to pay gas fees to dispute bad batches.

A ZK-rollup trusts the underlying cryptographic assumptions (that the proof scheme is sound) and the implementation correctness of the circuit compiler. If the circuit logic is flawed or the proof scheme is broken, an invalid state could be accepted. ZK-rollups also require that sequencers and provers do not collude to generate false proofs, though this is cryptographically hard (unlike the optimistic model, where a silent sequencer can simply go unpunished if no one challenges it).

## Withdrawal Mechanics

Because optimistic rollups have a challenge window, a user wanting to exit the rollup and withdraw to the base layer must wait 7 days (on Ethereum) for the challenge period to expire. During that time, their funds are in an intermediate state—not on the rollup, but not finalized on the base layer either. Some protocols offer liquidity providers who buy these "pending withdrawals" at a discount, offering users instant exit; the LP waits the 7 days and reaps the full withdrawal themselves.

ZK-rollups settle withdrawal proofs in minutes. Once the proof is verified on-chain, the base-layer contract releases the funds. This is a significant user-experience advantage for applications that need frequent cross-layer transfers or for users who value access to their assets.

## When to Use Each

Optimistic rollups suit applications that do not require sub-minute settlement and where the user base is large enough to support verifier incentives. Arbitrum and Optimism have achieved this: the large transaction volume and many economic participants mean fraud proofs are submitted quickly when needed. The simplicity of the model also means fewer novel cryptographic risks.

ZK-rollups are attractive for high-frequency trading, cross-chain bridges, and applications where instant finality is critical. They shift computational burden to the sequencer and prover, not the verifier, making them work well in environments with a limited number of trusted operators. They also scale further because no challenge period consumes block space.

## Current Landscape

Arbitrum and Optimism, the two largest rollups by total value locked, use optimistic proofs. zkSync and Polygon Hermez use ZK-rollups. Some projects are exploring **validiums** (ZK-rollups with off-chain data availability) and **volitions** (hybrid systems allowing per-transaction choice), aiming to combine the strengths of both. The debate remains open: no single model is universally superior, and the choice depends on the application's priorities.

## See also

<div class="wiki-seealso">

### Closely related

- [What Is a Layer 2 Rollup](/what-is-a-layer-2-rollup/) — The shared architecture that optimistic and ZK rollups build upon
- [Bitcoin Block Size Limit Explained](/bitcoin-block-size-limit-explained/) — Related throughput constraints affecting all scaling decisions
- [Blockchain Fundamentals](/blockchain-fundamentals/) — Cryptographic and consensus foundations

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where rollup assets trade
- [Distributed Ledger](/distributed-ledger/) — Broader context for scalable ledger design
- [Proof of Work](/proof-of-work/) — Alternative consensus security model

</div>

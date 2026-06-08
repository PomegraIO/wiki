---
title: "Data Availability Committee Explained"
description: "A data availability committee is a small group of signers that attests off-chain transaction data is retrievable, reducing the security guarantees of on-chain verification."
keywords:
  - data availability committee
  - blockchain scaling
  - off-chain data
  - trust assumptions
  - layer 2 solutions
image: /svg/crypto.svg
---

*A **data availability committee** is a set of independent signers who cryptographically attest that transaction data posted off-chain is retrievable and available. Rather than verifying every transaction on-chain, a scaling solution can rely on the committee's signature to confirm data is safe — trading reduced computational cost for a new trust assumption that the committee members are honest and won't collude to hide data.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Data Availability Committee — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Signers vouch that off-chain data exists and remains accessible to users.</div>

|   |   |
|---|---|
| **Core function** | Attest that transaction data is stored and retrievable |
| **Typical size** | 10–100+ independent signers |
| **Signature requirement** | Threshold (e.g., 2-of-3, 7-of-10) to confirm availability |
| **Data location** | Off-chain; signers sample or verify locally |
| **Trust model** | Assumes committee members won't coordinate to hide data |
| **Scaling benefit** | Reduces on-chain verification burden significantly |
| **Failure mode** | If committee colludes, data can be censored or withheld |

</aside>

## The data availability problem in scaling

Most [blockchain](/blockchain-fundamentals/) solutions — particularly scaling systems — face a core tension: verifying every transaction on-chain costs computational resources, but posting all transaction data on-chain is expensive and doesn't compress well. For a system to scale, it must either skip verification or find a way to prove data exists without re-posting it in full.

Enter **data availability**. The challenge is convincing users and the wider network that transaction data is genuinely available for retrieval, even though it's stored off-chain. Without proof of data availability, a sequencer or operator could publish a state root (a cryptographic summary of a new block) without actually revealing what transactions it contains. Months later, if the operator goes offline or becomes adversarial, users would have no way to reconstruct the block or prove the state root was fraudulent.

## How a data availability committee works in practice

A data availability committee solves this by introducing a group of independent signers — sometimes 10, sometimes 100+, depending on the system's design. The typical workflow is:

1. A sequencer or operator bundles transactions and creates a block.
2. The operator sends the block data to committee members (off-chain, via a peer-to-peer network or cloud storage).
3. Each committee member verifies that the data is complete, computes a commitment (often a hash or polynomial commitment), and signs an attestation.
4. A threshold of signatures (e.g., 7-of-10 or 2-of-3) is required to confirm data is available.
5. Once the threshold is met, the state root is posted on-chain, and users can trust the data will be retrievable.

Committee members typically **sample** or spot-check portions of the data rather than downloading the entire block. In more sophisticated designs, the operator uses a technique like erasure coding — splitting data into redundant pieces so that any subset of pieces can reconstruct the whole — allowing committee members to verify availability with only a fraction of the data.

## Trust assumptions: on-chain vs. off-chain data availability

A key difference between a data availability committee and on-chain posting:

**On-chain posting**: Every full node verifies the data. If the data is fraudulent or missing, the network consensus mechanism detects it. Trust is distributed across all nodes.

**Data availability committee**: Only a small, fixed set of signers attests to availability. Users rely on the assumption that enough committee members are honest and won't collude to suppress data. If even one committee member secretly withholds data, users *may* still be fine — as long as at least one committee member has it. But if a threshold of members coordinate to hide data, the system has no on-chain defense.

This represents a trade-off. Scaling improves dramatically because you avoid re-posting terabytes of data on-chain. But you introduce a new party (the committee) and assume they remain honest and uncensorable.

## Where data availability committees are used

Several production and proposed systems rely on committees:

**Celestia** (as an external DA layer) can work with data availability committees, though it also supports full on-chain posting. Some rollups building on Celestia use committees as a stepping stone to full decentralization.

**Arbitrum** (specifically Arbitrum Nitro) uses a set of signers to attest to the availability of calldata submitted off-chain, with a fallback to on-chain posting if signers fail.

**StarkNet** and other [validity proofs](/proof-of-stake/) systems sometimes use committees to manage off-chain data, deferring to on-chain posting for higher security if needed.

**Polygon** and other side-chains have used committee-like structures, though the terminology and guarantees vary.

## Committee size and decentralization

A larger committee is harder to corrupt but slower to reach consensus. A smaller committee is faster but more centralized. Most designs aim for a sweet spot: large enough that no single party controls the majority, yet small enough to operate efficiently. Ten to thirty signers is common, though some experiments go much larger.

The committee's identity also matters. If all signers are run by the same organization, centralization risk is high. If they are spread across independent entities with different incentives, the threat of collusion is lower. Some systems rotate committee membership over time to prevent entrenchment.

## Comparison to other scaling approaches

**Rollups with on-chain data posting** (like Ethereum rollups) post compressed transaction data on-chain, so there is no trust assumption about a separate committee. The trade-off is higher on-chain cost.

**Sidechains and validators** may use a different consensus mechanism and trust model entirely, relying on a fixed validator set rather than a data availability committee.

**Sharding** (proposed for Ethereum) aims to distribute data verification across the network so no single committee is needed — at the cost of greater complexity.

A data availability committee is a pragmatic middle ground: better than trusting a single operator, but cheaper than posting all data on-chain.

## Failure modes and risks

If a data availability committee member goes offline, the system may tolerate it as long as the offline member was not critical to reaching the signature threshold. If enough members are unreachable, blocks cannot be finalized.

If a threshold of committee members are dishonest or coerced, they could refuse to sign a valid block (censorship) or could sign a block without actually storing the data (data unavailability). Either case is a serious failure, though the second is worse — it can lead to permanent loss of state.

Some systems mitigate this by allowing users to challenge the committee's attestation by posting the full data on-chain and proving the committee lied. This incentivizes honesty but requires users to be vigilant.

## Evolution toward greater decentralization

Many projects that start with a data availability committee view it as a temporary step. The long-term goal is often to move toward systems where data availability is verified by many independent nodes (as with Celestia) or where the data is intrinsically available on-chain.

This reflects a broader principle in blockchain design: decentralize trust and assumptions over time as the system matures and the ecosystem grows.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain fundamentals](/blockchain-fundamentals/) — the foundational technology
- [Smart contract](/smart-contract/) — off-chain scaling solutions execute smart contracts
- [Proof of stake](/proof-of-stake/) — consensus mechanism used alongside data availability
- Ethereum scaling — a primary use case for data availability committees
- [Distributed ledger](/distributed-ledger/) — the broader category of decentralized systems

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — infrastructure that may rely on scaling solutions
- Rollup scaling — technical approach combining data availability with transaction batching
- Consensus mechanism — how networks verify data and state

</div>

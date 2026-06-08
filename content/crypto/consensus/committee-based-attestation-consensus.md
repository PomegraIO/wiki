---
title: "Committee-Based Attestation in Blockchain Consensus"
description: "How protocols like Ethereum randomly assign validators to sub-committees to attest blocks without requiring every validator to vote on every block."
keywords:
  - committee-based attestation blockchain
  - how committee attestation works
  - ethereum attestation committees
  - validator sub-sampling consensus
image: /svg/crypto.svg
---

*Modern proof-of-stake blockchains cannot require every validator to vote on every block—the network would be flooded with messages. Instead, protocols like Ethereum use **committee-based attestation**: randomly selecting small sub-committees of validators to attest blocks, aggregating their votes, and using statistical sampling to ensure security. Understanding this mechanism explains how blockchains scale consensus from thousands of validators without sacrificing safety.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Committee Attestation — How It Works</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain consensus committees." />

<div class="wiki-infobox-caption">Random sub-sampling lets large validator sets reach consensus efficiently.</div>

|   |   |
|---|---|
| **Core idea** | Divide validators into committees; each attests a subset of blocks |
| **Committee size** | Typically 128–512 validators per committee (Ethereum: ~128) |
| **Rotation** | Committees change every slot (12–15 seconds) to prevent targeting |
| **Vote aggregation** | Signatures compressed using BLS cryptography |
| **Security threshold** | Need 2/3+ committee to attest; aggregate confirms safety |
| **Scalability gain** | Network traffic scales logarithmically, not linearly, with validator count |

</aside>

## The problem: scaling consensus to thousands of validators

Early proof-of-work and proof-of-stake designs required every validator to see every block and vote on it. Bitcoin miners implicitly "vote" for the longest chain; early proof-of-stake proposals (like Tendermint) required explicit supermajority consensus from every validator on every block.

This approach is secure but does not scale. With 1,000 validators, each block requires 1,000 signatures and votes. With 100,000 validators, network bandwidth explodes. Message propagation delays increase, confirming new blocks takes longer, and the network becomes vulnerable to network attacks (an attacker can trigger thousands of vote messages and flood nodes).

Ethereum faced this at launch: it needed to support tens of thousands of validators (later, hundreds of thousands) but could not require each to broadcast a vote per block. Committee-based attestation solved it.

## How committees are formed and rotated

In Ethereum's model, validators are divided into committees based on a pseudorandom selection using the current block hash as entropy:

1. **Slot and committee**: The network is divided into "slots" (12-second blocks). Each slot is further divided into "committees"—subsets of validators.

2. **Random assignment**: A validator's committee assignment for each slot is computed deterministically from the validator index, current epoch (collection of slots), and the block hash. No validator can predict their assignment far in advance, but every node can independently compute which validator belongs to which committee.

3. **Rotation every slot**: Committees change every slot. A validator assigned to Committee 3 in Slot 100 might be in Committee 17 in Slot 101. This frequent rotation prevents an attacker from targeting a single committee repeatedly and ensures no committee is chosen twice in the same epoch.

4. **Overlap across epochs**: Over an entire epoch (32 slots ≈ 6 minutes), a validator will be assigned to multiple committees, ensuring they contribute to consensus regularly.

## The attestation process

When a block is proposed, the assigned committee for that slot attests it:

1. **Block proposal**: A single validator (chosen randomly for that slot) proposes a new block.

2. **Committee attestation**: The validators in that slot's committee receive the block, validate it (checking that it extends a prior finalized block, contains valid transactions, etc.), and create an attestation—a cryptographic signature over the block's hash and some metadata.

3. **Signature aggregation**: Rather than broadcast 128 separate signatures, the protocol uses [BLS (Boneh-Lynn-Shacham) cryptography](/proof-of-work/) to combine all committee member signatures into a single aggregate signature. The aggregate proves that multiple validators signed without revealing which ones individually.

4. **Network relay**: The aggregated attestation (one compact signature) is broadcast to the network, confirming that the committee attested the block. A node receiving it can verify that a supermajority (≥2/3) of the committee signed.

5. **Finality accumulation**: As more epochs pass and new committees attest new blocks, earlier blocks accumulate enough attestations to achieve finality—irreversibility. Ethereum finalizes blocks after two epochs of uninterrupted honest consensus (≈12.8 minutes).

## Why random committee assignment matters

Randomness is critical for security:

**Prevents targeting**: An attacker controlling 1/3 of validators cannot ensure all their validators land in a single committee. The attacker is spread across many committees, limiting their influence on any one block.

**Prevents collusion ahead of time**: A validator does not know their assignment far in advance, so a coalition of validators cannot pre-arrange to corrupt a specific block or epoch.

**Homogenizes stake**: By rotating frequently, the protocol ensures no single committee is disproportionately influenced by one entity's large stake.

If committees were static, a powerful entity could wait for the committee to rotate to a constellation of small validators and coordinate an attack on a target block.

## Scaling benefits

Committee-based attestation delivers two major scaling gains:

**Bandwidth**: With 100,000 validators, requiring every validator to vote per block would generate 100,000 signatures. With committee size ~128, the network processes ~128 attestations per slot (after aggregation, one combined signature). Traffic is reduced by ~780×.

**Latency**: Message propagation time scales with the number of senders. Fewer attestations mean faster block confirmation and lower network latency.

**Validator decentralization**: Smaller machines can run validators because the message volume is manageable. Solo stakers with modest hardware can participate in securing the network.

The trade-off: the protocol now relies on statistical security. If a block has 100+ attestations from a committee of 128, there is a negligible probability the attacker controls enough of the committee to finalize a conflicting block. The math is solid, but it is not the "every validator confirms everything" certainty of earlier designs.

## Comparison with other sampling approaches

Not all protocols use Ethereum's approach:

**Polkadot**: Uses a smaller, rotating validator set (≈297 validators at any time) rather than sub-sampling from a large set. This simplifies finality but limits decentralization (validators must be nominated by holders with significant stake).

**Cosmos**: Earlier versions used all validators; newer designs (like Interchain Security) sub-sample using a similar committee approach.

**Avalanche**: Uses repeated random sub-sampling (asking random validator sets multiple times to reach agreement) rather than a single-round committee vote.

Ethereum's design emphasizes maximal participation (all validators can potentially attest) while avoiding per-slot global consensus, balancing decentralization and scalability.

## Committee attestation and network partitions

During a network partition, committee attestation is still subject to the [liveness-versus-safety trade-off](/consensus-liveness-vs-safety-tradeoff/). If one partition has < 2/3 of the validator set, committees in that partition cannot accumulate enough attestations to finalize new blocks. The network halts on the minority side. This is intentional: Ethereum prefers safety (no conflicting finalized blocks) over liveness.

A partition with 2/3+ validators continues finalizing normally. When the network heals, validators in the minority partition recognize the majority chain as canonical (or are slashed if they have already attested conflicting blocks).

## Validator requirements for committee participation

To participate in committee attestation, a validator must:

- Propose or attest blocks in their assigned committee (required).
- Not double-vote on conflicting blocks (slashing penalty if violated).
- Stay online and connected to the network (otherwise, inactivity leaks slowly erode their rewards).
- Run software that correctly computes their committee assignment.

Most validators use shared infrastructure (staking pools, cloud providers) to meet these requirements at scale. The protocol's reliance on random assignment and frequent rotation limits the risk that a single operator can control enough committees to attack the network.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — the consensus mechanism underpinning committee attestation
- [Liveness vs Safety in Consensus Protocols: The Core Trade-Off](/consensus-liveness-vs-safety-tradeoff/) — how committee sampling affects finality guarantees
- [Sybil Resistance in Consensus Mechanisms](/sybil-resistance-in-consensus-mechanisms/) — why random assignment prevents validator impersonation
- [Ethereum](/ethereum/) — the primary protocol using committee-based attestation
- [Byzantine Fault Tolerance](/proof-of-stake/) — the theory ensuring 2/3+ committee attestation is sufficient for finality

### Wider context

- [Distributed Ledger](/distributed-ledger/) — general architecture of consensus systems
- Smart Contracts — applications depending on committee-attested finality
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — settlement security depends on blockchain finality

</div>

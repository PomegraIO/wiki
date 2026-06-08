---
title: "Sync Committee Role in Light Clients"
description: "Sync committees enable light clients on Ethereum to verify the chain head without downloading full blocks. Learn how committee members rotate and why this matters for scalability."
keywords:
  - sync committee
  - light client
  - ethereum consensus
  - chain head verification
  - consensus layer
  - client scalability
image: /svg/crypto.svg
---

*The **sync committee role in light clients** is a critical piece of Ethereum's consensus design: a small set of validators rotates every ~27 hours to cryptographically attest to the chain head, allowing resource-constrained devices to stay in sync without processing full block history.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sync Committee — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">Sync committees allow light clients to verify blockchain state with minimal bandwidth and computation.</div>

|   |   |
|---|---|
| **Committee size** | 512 validators (randomly selected from active set) |
| **Rotation period** | ~27 hours (256 slots of ~12 seconds each) |
| **Light client requirement** | Must track only the current and next sync committee |
| **Signature burden** | Aggregate signature ~96 bytes, enabling ultra-light verification |
| **Full block download** | Light client does NOT download full blocks—only headers and merkle proofs |
| **Trust assumption** | 2/3 of committee members are honest (standard threshold) |

</aside>

## Why Light Clients Need Sync Committees

A full [Ethereum](/ethereum/) node downloads and verifies every block, every transaction, and every state change—a process that requires gigabytes of disk, substantial CPU, and continuous network bandwidth. For smartphones, IoT devices, and browsers, that's infeasible.

A light client aims to stay synchronized with the canonical chain without that burden. But here's the problem: if a light client only downloads block headers—not full blocks—how can it be sure the header is legitimate and hasn't been spoofed by a malicious node? The answer is consensus attestations.

In Ethereum's proof-of-stake consensus layer, validators attest to blocks they believe are correct. A full node can check these attestations against the active validator set. But a light client doesn't have the full validator set stored locally—downloading 500,000+ validator public keys defeats the purpose of being light.

The sync committee solves this: instead of tracking all validators, a light client needs only a small, rotating set of 512 validators whose aggregated signature proves that the chain head is valid. This cuts the verification burden from megabytes to kilobytes.

## Committee Selection and Rotation

Every 256 [Ethereum](/ethereum/) slots (approximately 51 minutes), the sync committee changes membership—a full rotation every two epochs, or roughly 27 hours.

The selection process is deterministic and transparent:

1. **Random seed:** The beacon chain consensus layer generates a random seed based on past block hashes and randomness.
2. **Sampling:** From all active validators, 512 are randomly selected using that seed. Each validator has a probability of selection proportional to their stake (stake-weighted sampling).
3. **Announcement:** The selected 512 validators are known for the entire ~27-hour period. They begin attesting to proposed blocks.
4. **Rotation:** When the period ends, a new seed is drawn, a new 512 are selected, and the cycle repeats.

The randomness is crucial: a potential attacker cannot easily predict or influence which validators will be in the next committee, so they cannot consolidate enough stake to gain control.

## How Sync Committees Attest to Block Headers

During each slot, the sync committee's validators are asked to produce an aggregate signature over the block header they believe is correct. The signature is typically the hash of the "finalized" or most recent "justified" block, depending on client configuration.

A **light client verifies the signature** by:

1. **Fetching the sync committee public keys** (only once per 27-hour rotation, then caching).
2. **Retrieving the aggregate signature** from a full node or the peer-to-peer network.
3. **Checking that 2/3 of the committee signed.** The signature is valid only if at least 341 of the 512 validators participated.
4. **Confirming the signature matches the proposed block header.** Elliptic curve cryptography confirms the 512 public keys produced this aggregate.

If all checks pass, the light client accepts that block header as part of the canonical chain. If the signature is missing, invalid, or fewer than 2/3 signed, the header is rejected.

## Bandwidth and Computational Savings

The efficiency gains are substantial:

- **Validator set tracking:** A full node tracks ~500,000 active validators and their balances. A light client stores only 512 sync committee member public keys and rotates that list every ~27 hours. Storage: kilobytes vs. megabytes.
- **Aggregate signatures:** Instead of verifying 512 individual signatures, a light client verifies one aggregate signature using BLS (Boneh-Lynn-Shacham) cryptography, reducing verification time from ~100 ms to ~1 ms per block.
- **Block body:** A light client does NOT download the full block body (transactions, calldata, etc.). It fetches only the header (~500 bytes) and optional merkle proofs to confirm specific data fields if needed.
- **Network bandwidth:** A light client can synchronize with the latest block in kilobytes per slot, allowing operation on mobile networks or intermittent connectivity.

## The Trade-Off: Trust and Finality

Light clients gain efficiency at the cost of a weaker security model compared to full nodes. A light client assumes that:

- **The sync committee majority is honest.** If 2/3+ of a 512-member committee colludes, they can sign a false block header, and the light client will accept it. A full node would reject it by re-executing transactions.
- **The block data exists.** A light client verifies the header is correct but does not check whether the block body is available. A full node would reject unavailable data. In practice, [Ethereum](/ethereum/) includes a "data availability" layer (originally Proto-Danksharding) to address this.
- **Committee rotation is unpredictable.** If the selection mechanism were flawed, an attacker could dominate future committees. The randomness seed prevents this, but the guarantee is cryptographic, not physical.

For many applications—a wallet confirming a user's balance, a bridge relayer verifying finality, a light dapp client—this trade-off is acceptable. For an exchange or a node validating the entire history, a full node is necessary.

## Practical Example: A Mobile Wallet

Imagine a smartphone wallet using a light client to track an Ethereum account balance:

1. The wallet software stores the latest sync committee public keys (512 keys, downloaded once).
2. When the user opens the app, it asks a peer (a full node on the network) for the current block header and the sync committee's aggregate signature over it.
3. The app verifies the signature locally. If valid, the header is canonical.
4. The app then queries a full node for the user's balance at that block. The full node provides a merkle proof, which the light client verifies against the header's state root.
5. Every ~27 hours, the wallet fetches the new sync committee keys and updates.

Total data downloaded: a few kilobytes per use. A full Ethereum node would download gigabytes.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — Consensus mechanism underlying sync committees
- [Distributed Ledger](/distributed-ledger/) — Foundational concept for blockchain verification
- [Blockchain Fundamentals](/blockchain-fundamentals/) — Overview of chain structure and validation
- [Ethereum](/ethereum/) — Network implementing sync committee consensus
- [Hash Rate](/hash-rate/) — Proof-of-work equivalent to validator participation in proof-of-stake

### Wider context

- Consensus Layer — Where sync committees operate
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Application requiring light client or full node security
- Distributed System — Architectural context for light clients
- Cryptography — Mathematical foundation for aggregate signatures

</div>

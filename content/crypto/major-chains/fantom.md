---
title: "Fantom"
description: "An EVM-compatible blockchain using Lachesis DAG-based aBFT consensus to achieve sub-second finality and low fees without compromising decentralization."
keywords:
  - fantom
  - dag consensus
  - abft
  - evm compatible
  - finality
image: "/svg/crypto.svg"
---

*[**Fantom**](/fantom/) is a layer-1 blockchain designed for speed and finality. Using Lachesis, a DAG-based asynchronous Byzantine Fault Tolerant (aBFT) consensus mechanism, Fantom achieves sub-second transaction finality without requiring proof-of-work hashing or long staking lockup periods. Its [EVM](/ethereum/) compatibility allows developers to deploy [Ethereum](/ethereum/) smart contracts with minimal changes, while its consensus model prioritizes practical transaction throughput over centralization concerns.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fantom — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptographic ledgers." />

<div class="wiki-infobox-caption">Ethereum-compatible chain with DAG-based consensus and sub-second finality.</div>

|   |   |
|---|---|
| **What it is** | A layer-1 blockchain using DAG structure and aBFT consensus for instant finality |
| **Consensus mechanism** | Lachesis (asynchronous Byzantine Fault Tolerant; requires 2/3 honest validators) |
| **Finality** | ~1 second (transactions final after ~2 voting rounds) |
| **EVM compatibility** | Full; Solidity contracts work unchanged |
| **Staking model** | Delegated Proof of Stake; validators lock FTM; no slashing (changed in recent versions) |
| **Block time** | Sub-second; no fixed block boundary |
| **Native token** | FTM (Fantom Token); used for gas, staking, governance |
| **Launched** | Mainnet December 2019 |

</aside>

## The consensus trilemma: Fantom's answer

Blockchain researchers often describe a trilemma: decentralization, security, and scalability are hard to achieve simultaneously. Proof of Work chains (like [Bitcoin](/bitcoin/)) are secure and decentralized but slow. Proof of Stake chains (like [Ethereum](/ethereum/)) improve throughput but face centralization pressure: fewer people can afford to run validators. Sharded blockchains fragment security.

Fantom's thesis is that the trilemma is not immutable. By using a DAG (directed acyclic graph) instead of a linear chain, and aBFT (asynchronous Byzantine Fault Tolerance) instead of round-robin voting, Fantom claims to break free: high throughput, fast finality, and a validator set large enough to resist centralization.

Whether this claim holds depends on assumptions about network conditions and validator behavior, which remain contested.

## Lachesis consensus: how DAGs order transactions

Most blockchains (including [Ethereum](/ethereum/), [Bitcoin](/bitcoin/)) are chains: block 100 points to block 99, which points to block 98, and so on. A total order is imposed: block 1, then 2, then 3.

Fantom uses a DAG: validators produce events (batches of transactions) that reference previous events by multiple validators, creating a graph structure. The consensus algorithm then orders these events into a sequence without requiring a single authoritative block producer.

Lachesis operates in three phases:

1. **Gossip**: Validators broadcast events to peers. Each event contains a timestamp, a list of previous events it references, and transactions.
2. **Heaviest Observed Subtree (HOS)**: Validators compute which transactions are "strongly seen" (referenced directly or indirectly by enough validators to be considered final).
3. **Voting**: Validators vote on the order of transactions using a Byzantine Fault Tolerant mechanism. After 2–3 voting rounds, consensus is reached.

The result: transactions are final within seconds, even if network conditions are poor or the network is asynchronous (no assumption of bounded message delay).

## EVM compatibility: from Ethereum to Fantom

Fantom runs the Ethereum Virtual Machine (EVM), the same bytecode interpreter [Ethereum](/ethereum/) uses. This means Solidity contracts compiled for Ethereum can often run on Fantom unchanged. Developers use the same tools (Hardhat, Truffle, MetaMask) with minor configuration changes.

This portability has made Fantom a refuge during Ethereum congestion: a developer facing high Ethereum fees can deploy to Fantom in minutes, reusing code and testing infrastructure.

## Fast finality: the killer feature

Fantom's primary competitive advantage is finality speed. On [Ethereum](/ethereum/), a transaction is typically considered final after 12–15 blocks (~3 minutes). Fintech applications and bridge operators require more confirmations (a custom bridge might require 100 blocks, ~25 minutes).

On Fantom, a transaction is cryptographically final after ~1 second. There is no fork risk; no reorganization is possible. This is valuable for:

- **DeFi protocols**: No risk of sandwich attacks or MEV-driven reversions after the fact.
- **Bridges**: Fast finality enables cross-chain transactions to clear without extended wait periods.
- **Applications requiring near-instant settlement**: Derivatives, betting, or gaming.

This differs from [Ethereum](/ethereum/), where finality is probabilistic (more confirmations = lower risk, but never zero). It differs from [Stacks](/stacks/), where finality is tied to Bitcoin's 10-minute blocktimes. And it differs from [Lightning Network](/lightning-network/), which offers instant settlement between channel peers but requires managing channel liquidity.

## Delegated Proof of Stake and validator set

Fantom uses a delegated Proof of Stake model: token holders stake FTM or delegate to validators. Validators lock a minimum amount of FTM and earn rewards for proposing events and voting. In early versions, validators could be slashed (penalized and ejected) for Byzantine behavior; recent network upgrades removed slashing, shifting the security model toward reputation and incentive alignment.

This is a trade-off. Slashing provides strong penalties for misbehavior; its absence reduces validator risk but weakens security guarantees. Fantom's developers argue that aBFT is secure enough that slashing is redundant, provided 2/3 of validators are honest.

The validator set is relatively small compared to [Ethereum](/ethereum/) (which has ~900,000 solo stakers) but large enough for practical decentralization (~50–100 active validators in recent counts).

## Ecosystem and adoption

Fantom has attracted DeFi protocols, especially during 2021–2022 when Ethereum fees were extreme. Major protocols (Aave, Curve, Balancer) deployed to Fantom. The network has spawned homegrown DeFi (Spooky Swap, Scream, Beets) and cross-chain bridges.

Adoption has waned relative to other layers as Ethereum's Layer-2 ecosystem (Arbitrum, Optimism, [zkSync Era](/zksync-era/)) matured and fees on those networks dropped. Fantom's current strength lies in niche use cases where sub-second finality is a hard requirement and EVM compatibility is desirable.

## Trade-offs vs. alternatives

**vs. [Ethereum L1](/ethereum/)**: Fantom is faster and cheaper; Ethereum is more decentralized and secure (larger validator set, more scrutiny).

**vs. Arbitrum/Optimism**: Those are [Ethereum](/ethereum/) layers, inheriting Ethereum's security directly; they offer longer finality times (~7 days optimistic, ~15 min rollup) but have lower censorship risk.

**vs. [zkSync Era](/zksync-era/)**: zkSync uses validity proofs (stronger security guarantee); Fantom uses aBFT (faster, simpler, less crypto).

**vs. [Stacks](/stacks/)**: Stacks settles to [Bitcoin](/bitcoin/); Fantom is its own chain. Stacks' finality is tied to Bitcoin (~10 min); Fantom is sub-second.

## Current development and future directions

Fantom's development has been volatile. The team (Fantom Foundation) has cycled through governance and vision changes. Recent upgrades have introduced new staking mechanisms, reduced validator slashing, and emphasized Fantom's role in bridge interoperability.

The roadmap includes Sonic (a client upgrade aiming for even higher throughput), cross-VM compatibility (allowing contracts written in non-EVM languages), and tighter integration with other chains.

## Security and the 2/3 assumption

Fantom's security assumes that at least 2/3 of the validator set (by stake) is honest. If 1/3 or more are Byzantine (malicious or offline), the consensus can stall or diverge. This is a standard assumption in Byzantine Fault Tolerant systems, but it is stricter than [Ethereum](/ethereum/)'s 51% assumption and stricter than [Bitcoin](/bitcoin/)'s Proof of Work (which requires attacking 50% of hash power, a moving target).

In practice, Fantom has experienced downtime and brief consensus failures during early years, though none have been attributed to explicit Byzantine attacks. The maturity of the network and the vigilance of its validator set remain factors.

## See also

<div class="wiki-seealso">

### Closely related

- [zkSync Era](/zksync-era/) — Ethereum layer-2 using zero-knowledge proofs for faster settlement
- [Stacks](/stacks/) — Bitcoin layer with smart contracts and 10-minute finality
- [Lightning Network](/lightning-network/) — Bitcoin's payment-channel network for instant off-chain payments
- [Ethereum](/ethereum/) — The reference EVM and primary smart-contract platform
- [Byzantine Fault Tolerance](/ethereum/) — Consensus mechanism concept underlying Fantom's Lachesis
- [Proof of Stake](/ethereum/) — Staking and validator concepts applied in Fantom's consensus

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — Consensus and finality concepts
- [Distributed ledger](/distributed-ledger/) — The broader family of decentralized systems
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where FTM trades and liquidity pools operate
- [Decentralized finance](/ethereum/) — The primary use case for Fantom smart contracts
- [Capital flows](/capital-flows/) — Movement of assets between Fantom and other chains via bridges

</div>

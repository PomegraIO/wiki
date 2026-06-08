---
title: "Proposer-Builder Separation Explained"
description: "Proposer-builder separation decouples block building and validation in proof-of-stake networks to reduce MEV extraction and improve fairness."
keywords:
  - proposer builder separation explained
  - pbs blockchain
  - mev mitigation
  - proof of stake fairness
  - block building separation
  - ethereum consensus
image: "/svg/crypto.svg"
---

*In a **proof-of-stake** network, a **proposer** is a validator chosen to submit a block, and a **builder** is a specialized node that bundles transactions into candidate blocks and bids for the right to have that block proposed. **Proposer-builder separation** (PBS) decouples these two roles so that the proposer does not see or assemble the transactions inside the block—the builder does. This separation reduces **maximal extractable value** (MEV) — the ability of a participant to profit by reordering, inserting, or censoring transactions—and makes consensus fairer and more decentralized.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proposer-Builder Separation — Core Concept</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Builders assemble blocks; proposers submit them. Neither sees inside the other's domain.</div>

|   |   |
|---|---|
| **Proposer role** | Submit block to chain, earn MEV tips |
| **Builder role** | Assemble transactions, order them, bid for inclusion |
| **Main benefit** | Reduced MEV leakage to large searchers |
| **Primary risk** | Builder centralization (a few builders dominate) |
| **Live status** | Ethereum (since 2023) |
| **Mechanism** | Builders submit block headers, proposer selects highest bid |
| **Degree of decentralization** | Improved over MEV-aware proposing alone |

</aside>

## The MEV Problem Before PBS

Before proposer-builder separation, a single validator acting as block proposer had visibility into the mempool—the queue of pending transactions waiting to be included in the next block. The proposer could:

- **Front-run** transactions: see a pending swap and insert his own swap before it to capture the price movement.
- **Sandwich** transactions: insert two of his own transactions around a user's transaction to extract value from price slippage.
- **Reorder** to extract profits from liquidations, arbitrage, or lending protocol interactions.

This ability to extract value is MEV—the difference between the naive block reward and the actual profit a validator can capture by ordering and selecting transactions. On networks like Ethereum before PBS, MEV was highly concentrated: large-scale searchers and mining pools with sophisticated infrastructure could capture much of it. Individual users bore the cost.

MEV was not fully preventable, even if all validators were well-intentioned. The proposer, by virtue of assembling the block, had first-mover advantage. Thousands of pending transactions offer opportunities for extraction. A single proposer could easily earn 5–20% of the block reward (or more, in turbulent market conditions) by clever transaction ordering.

This concentration of MEV was seen as a centralization risk: validators with sophisticated MEV capture could afford to run large operations, attracting more stake and more block proposals, widening the gap between large and small operators.

## How PBS Separates the Roles

Under proposer-builder separation, the proposer's job is narrowed: propose a block to the chain. The builder's job is expanded: assemble candidate blocks and bid for the right to have that block proposed.

The flow is:

1. **Builders** monitor the mempool. Each builder independently assembles a candidate block by selecting and ordering transactions.
2. Each builder also computes the MEV available in that candidate block—the profit from reordering or inserting transactions.
3. The builder submits a **sealed bid** (a cryptographic commitment) for the right to have its block proposed, along with a small **header** of that block (root, hash) but not the full transaction list.
4. The **proposer** receives all bids from all builders and selects the builder with the highest bid.
5. The builder then reveals its full block, which the proposer broadcasts to the chain.
6. The proposer earns the bid amount as a **MEV tip** but does not see the transactions inside the block and cannot capture MEV directly from reordering.

The critical insight is that the proposer is blind to the block's contents until after committing to it. The proposer cannot insert his own transaction to front-run, because the transaction list is already sealed. The builder captures the MEV from reordering, but the builder competes with other builders, so no single builder can exploit transactions at will—the builder must share gains with the proposer (via the bid) or risk being undercut by a competing builder.

## Reducing MEV Concentration

PBS reduces MEV concentration in two ways:

**First, it democratizes MEV capture.** Before PBS, a proposer with sophisticated MEV-search tools could extract high value. After PBS, MEV is extracted by builders—specialized operators—and the MEV is distributed to proposers in the form of tips. A small validator who never becomes a builder still earns MEV tips when proposing blocks (because builders bid for the honor). A large validator who becomes a builder earns MEV from assembling blocks, but also competes with other builders, eroding excess profits.

**Second, it mitigates the "MEV-burn" problem.** In a naive system, high MEV extraction incentivizes large players to concentrate stake and validator infrastructure. With PBS, smaller validators can still earn a fair share of MEV (via tips) without needing to run advanced extraction tools or maintain large pools. This reduces the economic incentive for stake centralization.

It is important to note that PBS does not eliminate MEV—builders still extract MEV, and they may still have first-mover advantage in the mempool. What PBS does is redistribute MEV to proposers and force builders to compete, rather than allowing a single proposer to monopolize extraction.

## Builder Centralization Risk

The flip side of PBS is that builders may themselves centralize. If only a few builders can afford the infrastructure and expertise to assemble blocks profitably, then PBS merely shifts the concentration problem from proposers to builders.

In practice, Ethereum's implementation has seen some centralization: a handful of sophisticated builders (like MEV-geth, MEV-Relay, and others) process a disproportionate share of blocks. This is because MEV extraction is technically complex and requires:

- **Real-time mempool monitoring** across many nodes.
- **Fast transaction simulation** to compute MEV from different orderings.
- **Low-latency block propagation** to win the bid competition.
- **Capital** to sometimes take directional bets (e.g., holding assets to profit from sandwich trades).

A single hobbyist validator cannot easily run a competitive builder. This means some degree of centralization remains, even with PBS.

However, there are mitigants:

- **Multiple builders** can and do exist. Ethereum has a dozen or more active builders, not just one or two.
- **Decentralized MEV-sharing** protocols like MEV-Share are being built to allow small searchers to participate without running their own builder.
- **In-protocol PBS** proposals (like EIP-1559 for MEV) could further reduce builder centralization by baking MEV distribution into the consensus layer itself, rather than relying on external builders.

## Technical Implementation: Ethereum's MEV-Boost

Ethereum's current PBS implementation uses **MEV-Boost**, a software relay that sits between validators and builders. The flow is:

1. Validators use MEV-Boost (or a similar relay) to receive bids from builders.
2. Builders submit sealed bids to the relay.
3. The relay forwards only the highest bid (and header) to the validator.
4. The validator signs the header and returns it to the relay.
5. The relay reveals the full block, which the validator broadcasts.

MEV-Boost is not part of the core Ethereum protocol; it is an optional layer. Validators can disable it and build blocks themselves (returning to the pre-PBS model), or use it. Most large validators use MEV-Boost because the MEV tips typically exceed what the validator could capture alone.

The design keeps the proposer (validator) blind to the block contents during bid selection, the core principle of PBS.

## Wider Implications for Consensus Fairness

PBS is part of a broader effort to improve consensus fairness in proof-of-stake systems. Related mechanisms include:

- **Encrypted mempools** and **encrypted transactions**: Nodes encrypt transactions so that MEV-searchers cannot see them before inclusion.
- **Commit-reveal schemes**: Validators commit to a block, then reveal it in a later step, reducing MEV opportunities.
- **Threshold encryption**: Transactions are encrypted and decrypted only after block inclusion, preventing front-running entirely.

PBS alone does not provide perfect censorship-resistance or perfect privacy, but combined with other mechanisms, it improves the fairness of the consensus process.

## Adoption Beyond Ethereum

PBS concepts are being explored or implemented in other proof-of-stake networks:

- **Solana** has an implied builder ecosystem but no formal separation; validators bundle transactions themselves.
- **Cosmos** chains have delegated consensus and MEV dynamics that differ from Ethereum.
- **Polkadot** uses a different consensus model (nominated proof-of-stake) with different MEV characteristics.

Each network's MEV dynamics are unique, so PBS may be more or less valuable depending on the protocol design, the transaction throughput, and the kinds of applications running on it.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — consensus mechanism underlying PBS
- [Hash Rate](/hash-rate/) — computational work in proof-of-work (MEV is less relevant there)
- [Blockchain Fundamentals](/blockchain-fundamentals/) — distributed ledger concepts
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where transactions originate
- [Distributed Ledger](/distributed-ledger/) — underlying technology for blockchain

### Wider context

- [Ethereum](/ethereum/) — primary network where PBS is live
- [Central Bank](/central-bank/) — centralized vs. decentralized financial infrastructure
- [Systemic Risk](/systemic-risk/) — concentration of power in consensus
- [Capital Flows](/capital-flows/) — how MEV affects liquidity and pricing

</div>

---
title: "Cross-Rollup Message Passing"
description: "Cross rollup message passing how it works: bridging contracts between layer-2 rollups, latency trade-offs, and atomic execution."
keywords:
  - cross rollup message passing
  - cross layer 2 communication
  - rollup interoperability
  - atomic swaps between rollups
image: /svg/crypto.svg
---

*A user holding tokens on Arbitrum (an optimistic rollup) might want to interact with a decentralized exchange on Optimism (another optimistic rollup) without unwinding back to Ethereum mainnet. **Cross-rollup message passing** is the infrastructure that allows a smart contract on one rollup to send a message to, or trigger a transaction on, another rollup. The latency and cost of such messages depend on which rollups are communicating and whether the bridging protocol requires Ethereum confirmation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Rollup Message Passing — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency technology." />

<div class="wiki-infobox-caption">Infrastructure for contracts on different rollups to communicate and settle assets.</div>

|   |   |
|---|---|
| **Goal** | Enable contracts on rollup A to trigger actions on rollup B |
| **Latency** | Immediate (relayed) or finality-dependent (via Ethereum) |
| **Atomicity** | Difficult across rollups; usually settled separately |
| **Risk** | Liquidity pools, relayer reputation, Ethereum finality delay |
| **Common patterns** | Liquidity networks, escrow relayers, optimistic light clients |
| **Examples** | Across Arbitrum/Optimism, zkSync Era, Polygon |

</aside>

## The problem: why rollups are isolated

Each rollup maintains its own state and settlement on Ethereum. A smart contract deployed on Arbitrum cannot directly call a function on Optimism, because Arbitrum's virtual machine and Optimism's do not share a state root.

Users who want to move tokens or liquidity from one rollup to another must do one of the following:

1. Withdraw to Ethereum mainnet, then deposit into the target rollup—slow and expensive.
2. Use a centralized exchange—requires trusting the exchange operator.
3. Use a decentralized cross-rollup bridge—relies on third-party relayers or liquidity pools.

Cross-rollup message passing aims to enable option 3 in a way that is trustless and reasonably fast.

## Relayed messaging: the speed vs. trust trade-off

The simplest approach uses a **relayer**. Contract A on Arbitrum emits an event saying "send 10 USDC to user X on Optimism." An off-chain relayer watching both chains sees this event, and submits a transaction to Contract B on Optimism, instructing it to release 10 USDC to user X.

This is fast—the relayed transaction can confirm on Optimism in seconds or minutes, without waiting for Arbitrum to finalize or Ethereum to settle. But it trades safety for speed. The relayer must have liquidity (or a guarantee of repayment) on both chains. If the relayer is dishonest or insolvent, the user loses funds.

Protocols like Connext and Across mitigate this by requiring relayers to post bonds and by routing messages through a liquidity network where many relayers compete. The network uses a voting or optimistic dispute mechanism to resolve discrepancies. Still, there is operational risk: a relayer crash or network partition could delay messages.

## Ethereum-finality-based bridges

A safer but slower approach requires Ethereum finality. Contract A on Arbitrum sends a message into Arbitrum's outbox, which is eventually finalized on Ethereum mainnet (after Arbitrum's 7-day fraud-proof window closes). Only then is Contract B on Optimism allowed to execute the message, because Ethereum serves as the source of truth.

This is trustless: no relayer is needed. The guarantee comes from Ethereum's security. But the latency is poor—a message might take 7 days to clear, because one of the rollups involved must finalize on Ethereum before the other can act.

For low-volume settlement, this is acceptable. For high-frequency trading or automated systems, it is prohibitive.

## Light client bridges

A more sophisticated approach uses **optimistic light clients**. Rollup A runs a light client of Rollup B inside a smart contract. Periodically, off-chain agents submit Rollup B's state roots to Rollup A's light client contract. If the light client accepts the root (after a challenge window if it uses optimistic assumptions), Rollup A now "knows" the state of Rollup B, and contracts on A can verify claims about Rollup B's state.

Similarly, Rollup B has a light client of Rollup A. Now both can send messages and settle them atomically: Contract A locks funds, posts a message to the light client, and if the light client confirms the message was processed on B, the settlement is final.

The latency is intermediate: waiting for light-client state roots (minutes to hours) plus any challenge window (seconds to hours). The security is strong if the light clients are implemented correctly, though there is residual risk if the light clients themselves are buggy.

## The atomicity problem

True atomic execution across rollups is hard. If Contract A on Arbitrum sends a message to Contract B on Optimism, and Contract B executes partially or fails, there is no automatic rollback of Contract A's actions. Instead, the typical pattern is optimistic settlement:

Contract A locks funds and emits a message. Contract B receives the message and executes conditionally. If something goes wrong, a dispute or slashing mechanism penalizes the relayer or causes a reversion on the source chain. This is not instant atomicity but a form of eventual consistency backed by incentives.

Some protocols propose pessimistic approaches where Contract A does not release funds until it receives a cryptographic proof that Contract B has executed. This is safer but slower and requires more complex infrastructure.

## Liquidity pools and swap patterns

In practice, many cross-rollup applications use liquidity pools rather than trying to move assets directly. A user wants to swap 100 USDC on Arbitrum for ETH on Optimism. Instead of a message passing to execute an atomic swap, the user interacts with a protocol that has liquidity pools on both chains:

1. User deposits 100 USDC into the Arbitrum pool.
2. An off-chain relayer or automated market maker sees the deposit and provides 1 ETH (or the market rate) from the Optimism pool to the user.
3. The relayer is credited the 100 USDC and settles it later on Arbitrum or via a back-channel agreement.

This pattern is fast (minutes) and reliable (if the liquidity pool is well-capitalized) but requires trust in the pool operator or a network of incentivized relayers.

## Real-world examples and maturity

As of mid-2026, protocols like Across, Connext, and Hyperlane enable cross-rollup messaging with varying architectures:

- **Across** uses a shared liquidity pool and optimistic dispute mechanism; fast but requires capital lock-up.
- **Connext** uses local liquidity and chain-agnostic messaging; works across EVM and non-EVM chains.
- **Hyperlane** uses interchain security modules (ISMs); flexible but requires custom integration per chain pair.

Arbitrum and Optimism have also implemented native bridges that allow programmable message passing to Ethereum, but bridging directly between Arbitrum and Optimism requires third-party protocols.

ZK rollups like zkSync Era and Polygon zkEVM are exploring similar patterns, though the ZK proof verification overhead can make light-client approaches more expensive.

## Latency, cost, and trade-offs

The choice of cross-rollup bridge depends on the application:

- **DeFi swaps**: liquidity pools or relayed messaging (seconds to minutes).
- **Token transfers**: relayed bridges or Ethereum-finality bridges (minutes to 7 days).
- **Smart contract calls**: light-client bridges or custom protocols (seconds to hours).
- **High-security settlement**: Ethereum finality (7 days typically).

No single solution optimizes all three of latency, cost, and decentralization. Developers must pick the trade-off that suits their use case.

## See also

<div class="wiki-seealso">

### Closely related

- [ZK Rollup vs Optimistic Rollup: Key Differences](/zk-rollup-vs-optimistic-rollup-comparison/) — the two rollup paradigms being bridged
- [Data Availability Sampling Explained](/data-availability-sampling-explained/) — supporting infrastructure for rollup scalability
- [Ethereum Gas Limit and Its Role in Scaling](/ethereum-gas-limit-scaling/) — fundamental scaling constraints
- [Smart contracts](/smart-contract/) — the applications using cross-rollup messaging

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — consensus and state in distributed systems
- [Proof of Stake](/proof-of-stake/) — Ethereum's security model
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — how trades are settled on-chain

</div>

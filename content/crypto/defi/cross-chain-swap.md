---
title: "Cross-Chain Swap"
description: "Trustless exchange of tokens across separate blockchains using hash time-locked contracts, liquidity networks, or bridge protocols."
keywords:
  - cross-chain swap
  - atomic swap
  - hash time-locked contract
  - bridge
  - interoperability
image: "/svg/crypto.svg"
---

*A **cross-chain swap** is a trustless exchange of tokens native to different blockchains—for example, Bitcoin on the Bitcoin chain for Ethereum on the Ethereum chain. Most modern swaps use liquidity-provider networks or wrapped-asset bridges rather than on-chain atomic contracts, trading absolute trustlessness for speed and liquidity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Chain Swap — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and decentralized finance." />

<div class="wiki-infobox-caption">Enabling two blockchains to exchange value without a trusted middleman.</div>

|   |   |
|---|---|
| **What it is** | Direct token exchange between different blockchains |
| **Classic method** | Hash time-locked contracts (HTLCs) |
| **Modern method** | Liquidity networks (Connext, THORChain) or bridge protocols |
| **Key challenge** | Coordinating settlement across two independent consensus systems |
| **Trade-offs** | Security, speed, liquidity, and cost |
| **Leading use case** | Hedging across multiple chains in high-frequency trading |

</aside>

## Why blockchains cannot speak directly

Every blockchain is an independent system with its own consensus, finality rules, and settlement mechanism. Bitcoin uses Proof of Work; Ethereum uses Proof of Stake; Solana uses a different consensus entirely. When a user owns Bitcoin, it is secured by Bitcoin's miners; the Ethereum network cannot directly verify or freeze a Bitcoin transaction. For one chain to "know" something happened on another, either a trusted intermediary relays the message, or both chains implement a trustless protocol to exchange information.

Early cross-chain swaps tried to solve this with atomic swaps: Hash Time-Locked Contracts (HTLCs). The idea is elegant: Alice and Bob wish to swap BTC for ETH without trusting each other. Alice locks her BTC in an HTLC: if Bob reveals a secret within a time window, he gets the BTC; if he doesn't, Alice reclaims it. Bob creates a matching ETH contract: if Alice reveals that same secret on the Ethereum chain, she gets the ETH. Both parties are forced to either reveal the secret or forfeit, ensuring atomicity—both trades execute or neither does. The blockchain itself enforces the contract; no middleman needed.

## Why HTLCs rarely work in practice

HTLCs are theoretically elegant but practically cumbersome. They require both parties to be online to participate, to agree on the secret and contract parameters beforehand, and to monitor two blockchains for settlement. Block times differ (Bitcoin: ~10 minutes, Ethereum: ~12 seconds); an HTLC designed for one may timeout before the other settles, leaving funds stuck. Mining congestion on one chain can delay settlement and trigger timeouts on the other. Most critically, HTLCs offer zero liquidity provision: swaps only occur if two parties happen to want opposite pairs at the same time.

In practice, HTLCs are used mainly by dedicated traders in high-frequency cross-chain arbitrage, where coordination and latency tolerance are built into the workflow.

## Liquidity networks: the modern solution

Modern cross-chain swaps use liquidity networks: protocols like Connext and older versions of THORChain operate by having liquidity providers (LPs) post capital on multiple chains. When Alice wants to swap Bitcoin for Ethereum, she sends her BTC to the protocol's Bitcoin pool. The protocol's Ethereum pool instantly credits her ETH—not from atomic contract magic, but from LP capital. The protocol's security model relies on the assumption that LPs have incentive to settle the BTC fairly, or lose their collateral. In practice, Connext uses optimistic settlement: the protocol assumes LPs acted correctly unless someone proves otherwise within a challenge window.

This approach is fast (no waiting for block confirmations on two chains) and liquid (deep pools on both sides). The cost is reliance on the network's validators to correctly sign messages and route tokens. If validators collude or fail to settle correctly, user funds can be lost.

## Bridges and wrapped assets

Another approach sidesteps the swap entirely: a bridge protocol allows users to lock assets on one chain and mint an equivalent IOU (wrapped token) on another. For example, locking 1 Bitcoin through the Wormhole bridge mints 1 wrapped Bitcoin (wBTC) on Ethereum. This isn't a true swap—no token leaves the original chain—but economically equivalent: the user can now use wrapped Bitcoin on Ethereum markets, and later redeem it for the original Bitcoin by burning the wrapped version.

Bridges introduce counterparty risk: the bridge operator(s) or validator set must honestly hold the locked assets. If the bridge is compromised, locked capital is at risk. Several major bridges (Ronin, Poly Network) have suffered exploits totalling hundreds of millions in losses. The security of a cross-chain system is only as strong as the weakest bridge participant.

## Competing technologies and trade-offs

Different protocols optimize for different properties. THORChain uses its own consensus layer and validator set, claiming independence from Ethereum or Bitcoin's security assumptions—at the cost of introducing a new trusted party. Connext delegates to Ethereum's security but only for settlement, reducing the trust model. Stargate relies on a liquidity-pool model. Across emphasizes UX simplicity.

All face a trilemma: trustlessness (no reliance on any party), speed (settlement within minutes or seconds), and liquidity (deep pools, low slippage). No current design optimizes all three; protocols sacrifice one for the other two.

## Cross-chain swaps and ecosystem fragmentation

As multiple blockchains emerge (Solana, Arbitrum, Polygon, Avalanche, etc.), cross-chain swaps have shifted from niche technical curiosity to everyday DeFi necessity. A user farming yield on Arbitrum but wishing to buy assets on Solana faces the cross-chain problem repeatedly. This has driven competition among bridge and liquidity-network protocols, each claiming security and efficiency. The proliferation itself introduces new risk: many bridges, many potential exploits, many points of failure.

Professional traders now monitor cross-chain arbitrage opportunities systematically, exploiting price differences across chains using HTLCs or liquidity networks. This activity improves cross-chain price efficiency but also concentrates capital in the hands of those most able to navigate the complex infrastructure.

## See also

<div class="wiki-seealso">

### Closely related

- Hash Time-Locked Contract — foundational atomic-swap primitive
- Bridge Protocol — trustless or semi-trustless asset relocation across chains
- [Atomic Swap](/atomic-swap/) — same-chain trustless exchange of tokens
- Liquidity Network — validator-backed cross-chain settlement
- [Slippage](/slippage/) — price impact of large cross-chain swaps

### Wider context

- Blockchain — independent consensus systems requiring bridges
- Decentralized Finance — ecosystem of cross-chain protocols
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — centralized alternative for token swaps
- Arbitrage — cross-chain price-differential capture

</div>

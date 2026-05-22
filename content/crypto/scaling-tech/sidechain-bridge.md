---
title: "Sidechain Bridge"
description: "A protocol or mechanism that connects a parallel blockchain (sidechain) to a main blockchain, enabling assets to transfer between the two chains."
keywords:
  - sidechain
  - blockchain bridge
  - layer-two scaling
  - cross-chain
---

*A **sidechain bridge** is a protocol or set of smart contracts that facilitate the movement of assets between a main blockchain (such as [Ethereum](/wiki/ethereum/)) and a parallel sidechain (such as Polygon or Arbitrum). Bridges enable users to lock tokens on one chain and mint or unlock equivalent tokens on the other.*

<aside class="wiki-infobox">

| Attribute | Details |
|-----------|---------|
| **Primary purpose** | Enable asset transfers across chains; reduce main-chain congestion |
| **Mechanism** | Lock-and-mint or burn-and-unlock cryptography |
| **Security model** | Depends on bridge design; can be validator-backed, algorithmic, or liquidity-based |
| **Speed** | Minutes to seconds (faster than main-chain transactions) |
| **Cost** | Lower gas fees than main chain (the whole point of sidechains) |
| **Risk** | Smart contract bugs, validator fraud, liquidity mismatches |
| **Examples** | Polygon PoS bridge, Arbitrum bridge, Optimism bridge |
| **Token representation** | Wrapped tokens (e.g., wrapped Ethereum = WETH on sidechain) |

</aside>

## Basic mechanics

A sidechain is a separate blockchain that runs in parallel to a main chain (e.g., Ethereum). It has its own consensus mechanism, validators, and block production. A bridge allows tokens to move between them.

**Flow from Ethereum to Polygon:**

1. User deposits 1 ETH into a bridge contract on Ethereum.
2. Contract locks the ETH and emits a receipt (an event or transaction).
3. Polygon validators observe the Ethereum transaction and confirm it.
4. Validators on Polygon mint 1 WETH (wrapped ETH) in the user's account.
5. User now holds WETH on Polygon, can trade it, lend it, or use it in smart contracts.

**Return flow (Polygon to Ethereum):**

1. User burns 1 WETH on Polygon.
2. Polygon validators confirm the burn.
3. Ethereum validators unlock the original 1 ETH from the bridge contract.
4. User withdraws ETH back to Ethereum mainnet.

The bridge acts as a custodian, holding collateral on one chain while releasing or minting tokens on the other.

## Why sidechains and bridges exist

Ethereum can process roughly 15 transactions per second. During periods of high demand (NFT mints, DeFi interactions), fees spike to $50–$100 per transaction. Users need alternatives.

**Sidechains** are separate blockchains with faster block times, cheaper fees, and higher throughput. [Polygon](/wiki/polygon/) can handle 7,000 TPS. [Arbitrum](/wiki/arbitrum/) can handle thousands per second.

**Bridges** let users move assets to sidechains to access these benefits. They trade off decentralization and security (sidechains have fewer validators, less hashpower) for speed and cost.

## Bridge security models

**Validator-backed bridges** (e.g., Polygon PoS bridge):
- A set of trusted validators observe and verify cross-chain transactions.
- Requires trust in validators not to steal locked funds.
- Faster (no proof verification), cheaper, but centralized risk.

**Light-client bridges** (e.g., IBC, interoperability protocols):
- Each chain runs a light client of the other chain, verifying headers and proofs.
- More secure and decentralized (no validator cartel needed).
- More expensive and slower (heavy cryptography).

**Liquidity pools** (e.g., Curve's stable-swap bridges):
- Bridge uses AMM (automated market maker) logic to swap tokens across chains.
- No token locking; instead, liquidity providers furnish capital.
- Fast and cheap; incentivizes third-party liquidity.

**Optimistic bridges** (e.g., Optimism's canonical bridge):
- Assume transactions are valid by default; only dispute if challenged.
- Faster final settlement; disputes are resolved in a fraud-proof game.
- Latency: 7-day challenge period on Optimism for security.

## Risks and failure modes

**Smart contract bugs:** Many bridges have suffered exploits due to flawed code. [Ronin bridge](/wiki/bridge-protocols/) was hacked for $625M in 2022 because validators were compromised. [Poly Network](/wiki/defi-composability/) lost $600M to a code vulnerability.

**Validator compromise:** If a validator is hacked or incentivized to steal funds, locked collateral can be withdrawn maliciously. This is the centralization risk of validator-backed bridges.

**Liquidity mismatches:** In liquidity-based bridges, if one side accumulates too much of a token and too little of another, the bridge runs dry. An imbalance can force users to pay slippage.

**Slashing and game theory:** [Optimistic bridges](/wiki/optimistic-rollup/) rely on validators posting a bond and being slashed if they attest to fraud. If slashing is insufficient or hard to trigger, validators may misbehave.

**Regulatory uncertainty:** Some bridges may be deemed money transmitters and face licensing requirements. Others face legal ambiguity about liability.

## Bridge tokens and wrapped assets

When you bridge an asset, you typically receive a wrapped version. 1 ETH on Ethereum becomes 1 WETH on Polygon. The bridge contract holds the original ETH in escrow; the WETH is a token representing that claim.

If the bridge is hacked, WETH holders lose their claim. This is why bridge tokens sometimes trade at a small discount to the underlying—the bridge risk is priced in.

[Stablecoins](/wiki/stablecoin/) bridge-traded versions (e.g., USDC on Polygon vs. Ethereum) create an additional risk: multiple versions of the same stablecoin can exist, and they can degrade if the bridge or issuer fails.

## Sidechain vs. layer 2 rollups

Sidechains are distinct from [layer-2 rollups](/wiki/optimistic-rollup/) (Optimism, Arbitrum), though the term is sometimes conflated.

**Sidechains:** Independent blockchains with their own consensus; security is lower (fewer validators). Example: Polygon PoS.

**Rollups:** Chains that post transaction data to Ethereum but inherit Ethereum's security. More secure but lower throughput than sidechains. Example: Optimism.

Bridges connect to both, but layer-2 bridges are generally safer because settlement is cryptographically tied to mainchain.

## Bridge economics and incentives

Bridges must be incentivized to maintain balanced liquidity. Some use:

- **Transaction fees:** Bridge takes a % of each cross-chain transfer.
- **Liquidity provider fees:** [AMM-based bridges](/wiki/defi-composability/) reward LPs with a portion of swap fees.
- **Governance rewards:** Validators or LP participants earn governance tokens.

If fee revenue is too low relative to costs, bridges become underfunded and risky.

## User perspective: when to bridge

**Bridge if:**
- You want to use DeFi protocols or NFT marketplaces on a cheaper chain.
- You have high-value transactions where even a 0.5% bridge fee is better than a $50 Ethereum transaction fee.
- You are comfortable with bridge risk (not negligible).

**Don't bridge if:**
- You plan to hold assets short-term and immediately unbridged (high slippage risk).
- You distrust the bridge security model.
- You need atomic, trustless settlement (use rollups instead, or stick to mainchain).

## The bridge ecosystem

Major bridges include:

- **Polygon PoS Bridge:** Validator-backed; connects Ethereum ↔ Polygon.
- **Optimism/Arbitrum Canonical Bridges:** Light-client or optimistic; connects Ethereum ↔ rollup.
- **Curve Stable-Swap Bridges:** Liquidity-based; for stablecoins across chains.
- **Wormhole, IBC, Across:** Interoperability protocols supporting multiple chains.

As the multi-chain ecosystem matures, standard bridge interfaces and shared liquidity pools are emerging to reduce fragmentation.

<div class="wiki-seealso">

### Closely related
- [Ethereum](/wiki/ethereum/) — Main chain sidechains connect to
- [Polygon](/wiki/polygon/) — Popular sidechain ecosystem
- [Arbitrum](/wiki/arbitrum/) — Layer-2 rollup with bridge
- [Layer-Three Protocol](/wiki/layer-three-protocol/) — Bridges at higher layers

### Wider context
- [Blockchain Fundamentals](/wiki/blockchain-fundamentals/) — Foundation of sidechains and bridges
- [Smart Contracts](/wiki/ethereum/) — Bridge contracts contain bugs
- [Stablecoin](/wiki/stablecoin/) — Common tokens being bridged
- [DeFi Composability](/wiki/defi-composability/) — Enables cross-chain yield farming
- [Validator Economics](/wiki/validator-economics/) — Incentives for bridge validators

</div>

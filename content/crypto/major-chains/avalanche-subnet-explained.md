---
title: "Avalanche Subnet Explained"
description: "Avalanche subnets are sovereign validator sets that run custom blockchains with their own rules while inheriting security from the main Avalanche network infrastructure."
keywords:
  - avalanche subnet
  - subnet blockchain
  - avalanche network
  - custom blockchain validator
image: "/svg/crypto.svg"
---

*An **Avalanche subnet** is a dynamic set of independent validators that run a custom blockchain with its own rules, token economics, and governance, while leveraging Avalanche's underlying security and consensus protocol. Unlike a sidechain or separate chain, a subnet does not need to bootstrap its own security; it inherits cryptographic finality from the Avalanche platform and can enforce its own virtual machine logic and state.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Avalanche Subnet — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">A privatized chain with public security.</div>

|   |   |
|---|---|
| **Operators** | Permissioned or permissionless validator set |
| **Consensus** | Inherits Avalanche's Snowball/Snowstorm protocol |
| **Finality** | Determined by subnet validators and Avalanche C-Chain anchor |
| **Token** | Custom token native to the subnet (not required to use AVAX) |
| **Use cases** | Gaming, enterprise blockchains, region-specific chains, DeFi protocols |
| **Cost** | Validators must stake AVAX; subnets may charge gas in custom token |

</aside>

## How Avalanche subnets differ from other layer-2 and sidechain models

The Avalanche ecosystem has three main chains: the X-Chain (asset exchange), the C-Chain (contracts, EVM-compatible), and the P-Chain (platform, managing validators and subnets). A subnet is **not** a layer 2 rollup sitting on top of the C-Chain, nor is it a fully independent blockchain like Ethereum or Bitcoin. Instead, it is a logical partition of validators within the Avalanche network.

A subnet validator must be registered on the P-Chain, prove it is online, and stake AVAX (the Avalanche token). In return, it earns the right to validate transactions in its subnet. The P-Chain does not store the subnet's state; it only tracks validator membership and subnet rules. The subnet itself—a custom blockchain—is validated by its own set of nodes. This is where the key difference emerges: **subnets inherit Avalanche's consensus safety without running the full Avalanche mainnet**.

A sidechain like Polygon or Harmony, by contrast, runs its own separate consensus and must convince the market to trust its security independently. A subnet's security is anchored to Avalanche because the P-Chain acts as a ledger of truth—it proves which validators are authorized to participate, and it records the subnet's network parameters. If a subnet validator misbehaves, the P-Chain can detect it and impose slashing. If an attacker wants to forge transactions in a subnet, it must somehow convince Avalanche's validator set that the forgery is legitimate, which it won't because the attacker does not control 2/3 of the subnet's validators.

## The validator set and permissioning model

A subnet requires a minimum validator set—typically 5 validators to start, though the subnet can decide its own rules. These validators do not have to be the same as Avalanche C-Chain validators. A company can run 10 nodes, invite 10 partners to run nodes, and designate those 20 as the authoritative set for its subnet. Only those 20 nodes validate blocks and produce the canonical chain history.

Subnets can be permissionless (like Avalanche's C-Chain, where anyone can become a validator by staking) or permissioned (where membership is controlled by the subnet's governance token holder or founder). A permissioned subnet is useful for consortiums, enterprises, or region-specific systems where participants are known and vetted. A permissionless subnet opens validation to anyone and tends toward greater decentralization but requires robust stake-based security (high AVAX requirements).

## Custom virtual machines and rules

A subnet does not have to use the Ethereum Virtual Machine ([EVM](/ethereum/)). The Avalanche platform supports arbitrary virtual machines (VMs). A subnet can:

- Run the C-Chain VM and be EVM-compatible (easiest migration path for Ethereum developers).
- Run a custom VM written in Go, Rust, or another language.
- Define its own gas mechanics, opcode set, account model, or state structure.

This is powerful for domain-specific blockchains. A gaming subnet might have a VM optimized for gaming state and transactions (low latency, no unnecessary generality). An enterprise subnet running supply-chain tracking might have a VM that enforces specific data formats and audit logs. A subnet does not inherit the EVM's bloat or memory costs if it does not need them.

## Finality and cross-chain communication

A transaction confirmed by a subnet's validators is final with respect to the subnet. It cannot be unconfirmed or double-spent within that subnet. However, finality is not instantaneous across the Avalanche ecosystem.

Avalanche subnets can anchor their state to the C-Chain via special transactions. If a subnet wants to prove to the mainchain that an event happened (e.g., a user locked tokens in the subnet), it can submit a **cross-subnet transaction** that is witnessed and recorded on the C-Chain. This creates a cryptographic record that other subnets and the mainchain can trust. It is not atomic—the subnet commit and the C-Chain commit are separate steps—but it enables bridges and multi-chain primitives.

A subnet and the mainchain can agree to **shared security**, where mainchain validators also validate the subnet. This increases the cost and complexity but ensures that attacking the subnet requires attacking the mainchain too. Most subnets do not use shared security; instead, they rely on their own validator set and Avalanche's consensus protocol for safety.

## Use cases and real-world examples

**Gaming and NFTs.** Subnets can offer low-latency, low-cost transactions for in-game asset trades and minting. A gaming company can launch its own subnet, control gas prices, and customize the VM for game logic.

**Enterprise and institutional chains.** Banks or consortiums can run permissioned subnets, issuing digital assets and settling transactions with privacy and control. Each organization runs a validator node; the subnet's smart contracts define settlement rules.

**Regional and soverign chains.** A country or region might launch a subnet to offer blockchain infrastructure under local regulatory rules and validator control, while still anchoring to Avalanche's security.

**DeFi protocols.** A protocol like Aave or Curve could launch a subnet as a dedicated environment for its contracts, optimizing gas costs and latency without competing with other applications on the main C-Chain.

Several projects have announced subnets: Avalanche Rush (a subnet for DeFi), Crabada (gaming), and others. None has yet achieved mainstream adoption comparable to Ethereum's layer-2s, but the infrastructure is live.

## Economics: staking, gas, and token models

Validators in a subnet must stake AVAX on the P-Chain to prove their commitment. The amount varies, but many subnets require 2,000–10,000 AVAX per validator. If a validator misbehaves (double-signs or goes offline), part of its stake is slashed.

Gas and transaction fees in the subnet are denominated in the subnet's own token. A subnet can charge gas in any token (AVAX, a custom ERC-20 equivalent, or even a stablecoin). This decouples the subnet's fee structure from AVAX's price and volatility. It also means that subnet tokens can have intrinsic value—if a subnet is popular, its token becomes valuable because users must hold it to pay gas.

The subnet can decide how much to charge per unit of gas, allowing it to price-compete with other subnets and layers. A gaming subnet might offer very low gas to attract volume; an enterprise subnet might charge higher fees to fund a strong validator set.

## Drawbacks and trade-offs

Subnets are not a panacea. They fragment liquidity. A token on one subnet cannot be spent directly on another without a bridge, and bridges introduce counterparty risk and latency. This limits network effects.

Starting a subnet requires a validator set and ongoing operational costs—hardware, bandwidth, governance. Smaller projects may not justify the overhead.

A subnet does not inherit Avalanche mainchain's decentralization and security out of the box. If its validator set is small or concentrated, the subnet is vulnerable to collusion or attack. Growing and securing a healthy validator set is a separate task.

Finally, there is limited tooling maturity for cross-subnet dApps. Developers are still learning how to architect applications that span subnets efficiently.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain fundamentals](/blockchain-fundamentals/) — Distributed ledger, consensus, and cryptographic proof
- [Proof of stake](/proof-of-stake/) — Validator-based consensus mechanism
- [Smart contract](/smart-contract/) — Programmable transaction logic on a blockchain
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Trading platform for digital assets
- [Distributed ledger](/distributed-ledger/) — Decentralized database technology

### Wider context

- [Ethereum](/ethereum/) — Leading smart contract platform with EVM
- [Bitcoin](/bitcoin/) — Original decentralized currency and ledger
- [Initial public offering](/initial-public-offering/) — Parallel to token launches in new subnets
- Network effects — How value concentrates in large, connected systems

</div>

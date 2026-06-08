---
title: "Wrapped Token Mechanics"
description: "How wrapped tokens like WBTC work in DeFi—locking native assets on another chain, custodial assumptions, and liquidity."
keywords:
  - how wrapped tokens work defi
  - wrapped bitcoin wbtc
  - wrapped ethereum weth
  - cross-chain token representation
  - defi asset bridge
---

*A **wrapped token** is a smart-contract representation of an asset locked on its native chain, allowing it to trade and participate in protocols on a different blockchain. Wrapped Bitcoin (WBTC) on Ethereum and wrapped Ethereum (wETH) on other blockchains are the most common examples, but the mechanic is identical: lock the real asset, mint a claim token on the destination chain, and burn it when the holder wants the original back. Understanding the custodial and technical assumptions behind wrapping is essential for anyone moving assets across chains or providing liquidity in DeFi.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Wrapped Tokens — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">A bridge from one asset class to another, built on trust assumptions.</div>

|   |   |
|---|---|
| **Definition** | A blockchain token representing a 1:1 claim on an asset locked elsewhere |
| **Common examples** | WBTC (Bitcoin on Ethereum), wETH (Ethereum on other chains), stETH (Ethereum staking token) |
| **Creation method** | Deposit native asset → smart contract or custodian mints wrapped token on destination chain |
| **Redemption** | Burn wrapped token → claim original asset (assuming custodian/contract cooperates) |
| **Primary use** | Access liquidity pools, lending protocols, and DeFi composability on non-native chains |
| **Custody model** | Centralized custodian (WBTC via Ren) or smart contract (wETH via simple Solidity) |
| **Key risk** | Wrapped token may not equal native token if custodian defaults or bridge is exploited |

</aside>

## The Basic Wrapping Flow

Wrapping an asset requires three steps. First, the user deposits the native asset (Bitcoin, Ethereum, or any other token) into a contract or custodian-managed address on the original chain. Second, an equal number of wrapped tokens are **minted** on the destination chain and sent to the user's address there. Third, the original asset is locked in escrow—it cannot be moved or spent until the wrapped token is burned.

When the user wants to unwrap, they send the wrapped token back to the contract or custodian, which **burns** it (removing the claim) and releases the original asset from escrow. The process is atomic in principle but custodian-dependent in practice. If the custodian goes bankrupt or is hacked, the locked collateral may be inaccessible even after burning the wrapped token.

The simplest wrapped token is **wETH**, Ethereum itself wrapped on Ethereum—which sounds circular but serves a technical purpose. Ether (ETH) is the native currency of Ethereum, but smart contracts interact best with ERC-20 tokens (a standard interface). Converting ETH to wETH makes it composable in [smart contracts](/smart-contract/), lending pools, and swaps. There is no custodian, just a Solidity contract that holds ETH 1:1 against outstanding wETH. This is the lowest-risk wrapping because the code is transparent and the contract cannot move the locked ETH.

## Custodial vs. Smart-Contract Wrapping

Wrapped tokens fall into two categories by trust model.

**Centralized custodian wrapping** (WBTC, aUSDC on some chains) relies on a company or consortium to hold the native asset in a vault. Users deposit Bitcoin at a custodian (Ren, RenVM, or an exchange), and the custodian mints WBTC on Ethereum. The custodian controls the keys to the Bitcoin address. If the custodian is compromised, becomes insolvent, or collapses, the WBTC holders have a claim on a bankrupt entity—not a guarantee of redemption. This model is necessary for Bitcoin wrapping because Bitcoin itself is not programmable; there is no way to lock Bitcoin natively on Ethereum without a third party holding it.

**Smart-contract wrapping** (wETH, stETH, and Curve LP tokens) is enforced by code. The contract holds the native asset and mints wrapped tokens in exact proportion. Anyone can redeem by sending the wrapped token to the contract; the contract automatically releases the asset. There is no custodian signing off. This is trustless in the sense that the only assumption is that the contract code is correct and not exploited. However, the code itself is still a source of risk—a [smart contract bug](/smart-contract/) can lock assets irretrievably, and the contract is only as transparent as its source code and audit history.

## Why Wrapped Tokens Matter in DeFi

Wrapped tokens enable **cross-chain liquidity**. Bitcoin is the most valuable cryptocurrency, but the Bitcoin blockchain is not Turing-complete; it cannot run lending markets, automated market makers, or complex derivatives. By wrapping Bitcoin as WBTC on Ethereum, Bitcoin holders can deposit WBTC into Aave or Uniswap without leaving the Ethereum ecosystem. The same logic applies to moving Ethereum to other chains (Polygon, Optimism, Arbitrum) as wETH, widening the addressable liquidity pool for each protocol.

Wrapped tokens also enable **yield and leveraged exposure**. A Bitcoin holder could swap BTC for WBTC, deposit it in a Curve pool to earn fees, or borrow stablecoins against WBTC in a lending protocol—all without trusting a centralized exchange. Staking-derived wrapped tokens like **stETH** (staked Ethereum from Lido) represent Ethereum locked in the Beacon Chain validators, earning staking rewards while remaining tradeable and composable in DeFi. The user gets yield without liquidity loss.

## Trust Assumptions and Counterparty Risk

The key question is: how confident can a user be that the wrapped token equals the native asset? This depends entirely on the wrapping mechanism.

For **centralized custodian tokens** like WBTC, the user must trust Ren (or whoever holds the Bitcoin) to not lose the keys, not be hacked, not be politically pressured to freeze assets, and not go bankrupt. Historical exchange hacks and custodian failures show this is a real risk. WBTC's transparency reports and active audits reduce the risk but do not eliminate it.

For **smart-contract wrapping**, the user assumes the contract code is correct and that the blockchain itself is secure. A bug in the contract could allow an attacker to mint wrapped tokens without locking collateral (causing the wrapped token to trade at a discount to native) or to drain the collateral (leaving wrapped token holders with claims on nothing). The 2023 hack of the Poly Network bridge and the 2022 Ronin bridge hack illustrated the scale of the risk.

Even **wETH**, the simplest and most trusted wrapped token, carries the assumption that Ethereum itself will not fork or suffer a permanent consensus failure. Unlikely, but not zero.

## Wrapped Token Premiums and Discounts

A wrapped token should trade at or very near parity to the native asset (plus a small fee for wrapping/unwrapping). In efficient markets, if WBTC trades significantly below the price of Bitcoin, an arbitrageur can buy WBTC cheaply, unwrap it, and sell the Bitcoin for a risk-free profit. This buying pressure closes the discount.

However, if market confidence in the custodian or smart contract deteriorates—due to news of a hack, regulatory threat, or fund freeze—wrapped tokens can trade at a **discount**. For example, during the 2023 banking stress, USDC.e (wrapped USDC on some chains) fell below parity on fears of Ethereum-based bridge insolvency. The discount reflects what the market believes the wrapped token is actually worth given the real risk of non-redemption.

Conversely, high demand for the wrapped token on its destination chain can cause it to trade at a small **premium** if wrapping is slow or supply is constrained. This incentivizes new minting, which closes the gap.

## The Role of Bridges and Dual Standards

Modern blockchain projects have spawned multiple wrapped versions of the same asset. Ethereum exists on Polygon, Optimism, Arbitrum, and other chains as wETH, and Ethereum on Solana exists as wETH as well. The liquidity is fragmented across these wrappers. A user on Optimism cannot automatically use Polygon's wETH; the two are separate tokens, even if both represent Ethereum.

Bridges (and bridge protocols like Stargate Finance, Across, or Synapse) attempt to move wrapped tokens between chains, but each bridge adds another layer of custodial or smart-contract risk. The bridge operator or smart contract must hold wrapped tokens on one chain and release them on another. If the bridge is hacked or the custodian fails, assets are lost across chains.

## Practical Implications for DeFi Users

Wrapping is rarely free. Most custodians and bridges charge a small percentage (0.1–0.5%) for wrapping and unwrapping. Over time, these fees matter. For example, a yield farmer earning 5% annually on wrapped Bitcoin is net-positive only after deducting wrapping and gas costs.

Wrapped tokens also introduce **smart contract risk** in addition to price risk. A user providing liquidity in a pool like Curve's WBTC–tBTC pair is exposed to both the price fluctuation of Bitcoin and the risk that one of the two wrapped versions becomes insolvent or unhackable. Diversifying across multiple wrapped versions of the same asset can hedge this risk but further fragments liquidity.

Finally, wrapped tokens are **not** a substitute for the native asset. WBTC is not Bitcoin; it is a claim on Bitcoin held by a custodian. In a severe market breakdown or loss of internet access, WBTC would be worthless while physical Bitcoin and access to the Bitcoin blockchain would preserve value. For any use case requiring true non-custody, wrapping is not appropriate.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart Contract](/smart-contract/) — the code that enforces wrapped token mechanics
- ERC-20 Standard — the token interface that makes wrapped tokens composable
- DeFi Liquidity Pools — the primary destination for wrapped tokens in lending and swapping
- [Proof of Stake](/proof-of-stake/) — the mechanism behind staking-based wrapped tokens like stETH
- [Distributed Ledger](/distributed-ledger/) — the underlying blockchain technology enabling wrapping

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — traditional off-chain custodians competing with wrapped token models
- [Initial Public Offering](/initial-public-offering/) — how DeFi protocols raise capital and governance tokens that may themselves be wrapped
- [Credit Risk](/credit-risk/) — the custodian risk inherent in wrapped token design

</div>

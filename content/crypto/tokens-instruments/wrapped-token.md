---
title: "Wrapped Token"
description: "A representation of an asset from one blockchain deployed on a different blockchain, enabling cross-chain asset transfers."
---

*A wrapped token is an IOU on one blockchain for an asset on another. If you hold Bitcoin but want to use it on the Ethereum network, you would deposit your Bitcoin with a custodian, who would lock it and issue you "Wrapped Bitcoin" (WBTC) on Ethereum. The wrapped token trades 1:1 with the underlying asset (or should, if the market is efficient), but it exists in a different ecosystem and can be used in Ethereum applications.*

## The cross-chain problem

Bitcoin cannot natively interact with Ethereum's smart contracts. Bitcoin lives on the Bitcoin network and is controlled by Bitcoin's consensus mechanism; Ethereum lives on the Ethereum network and has its own smart contracts, tokens, and applications. If a Bitcoin holder wants to earn interest in a decentralized-lending protocol on Ethereum, they have two problems: first, moving Bitcoin to Ethereum, and second, converting it back.

Wrapped tokens solve this by creating a parallel asset. The wrapped version is custodied—a trusted entity holds the original asset in locked storage—while the wrapped token is freely tradable on the new chain. When you want to unwrap, you burn the token and retrieve the original. The mechanism is economically efficient (assuming the custodian is trusted and solvent) but introduces custodial and bridge risk: if the custodian is hacked or the bridge fails, wrapped tokens become unbacked IOUs.

## Common wrapped tokens

WBTC (Wrapped Bitcoin) is the most widely used wrapped token. As of 2024, tens of billions of dollars worth of Bitcoin have been wrapped and deployed across Ethereum, Polygon, Arbitrum, and other networks. WBTC is controlled by a DAO governance structure, which theoretically reduces custodian risk by distributing custody among multiple signers.

Wrapped Ethereum (wETH) exists not for cross-chain purposes but for tokenization. Ether cannot be transferred as an [token](/wiki/ethereum/) in many smart contracts without additional logic; wrapping it as wETH makes it compatible with standard token interfaces. Every Ethereum user has likely interacted with wETH without realizing it.

Other notable wrapped tokens include wSTETH (a wrapped version of Lido-staked Ethereum), wUSDC (wrapped on other chains), and various derivatives created for [liquidity-pool](/wiki/liquidity-pool/) purposes.

## Custodian risk and bridge alternatives

The fundamental risk of wrapped tokens is the custodian. If you hold WBTC, you are trusting Circle (the issuer) and Bitgo (the custodian) to hold your Bitcoin securely. If Bitgo is hacked, your WBTC might be worth zero. This is counterintuitive to many crypto users, who chose crypto precisely to avoid trusting intermediaries. Yet wrapped tokens require trust by definition.

Some protocols attempt to minimize this risk through distributed custody: instead of one company holding all locked assets, a rotating set of validators hold smaller portions. Threshold Network's tBTC uses threshold cryptography to ensure that no single party can steal funds. Others use decentralized bridges—smart contracts on both chains that release assets based on consensus between validators rather than a single custodian's signature.

The emergence of multiple bridge designs—Wormhole, LayerZero, Stargate—reflects dissatisfaction with single-custodian models. However, decentralized bridges bring different risks: if the validators governing the bridge are corrupted or collude, they can issue infinite wrapped tokens without holding collateral. Major decentralized-bridge exploits have resulted in hundreds of millions in losses.

## Trade-offs in adoption

Wrapped tokens enable liquidity to flow across blockchains and are essential infrastructure for multi-chain applications. The alternative—maintaining separate order books and liquidity pools on each chain—fragments markets and wastes capital. Yet each wrapped-token intermediary adds latency and creates a new point of failure.

As [layer-2-scaling](/wiki/ethereum-dencun/) solutions like Arbitrum and Optimism gain adoption, the need for wrapped tokens may diminish. Native assets on multiple chains would eliminate custodial middlemen. However, cross-chain interoperability will remain necessary as long as multiple blockchains coexist, and wrapped tokens are the current best-practice solution—imperfect but functional.

## Regulatory and accounting implications

The tax treatment of wrapped tokens is unsettled in most jurisdictions. Wrapping and unwrapping a token likely triggers a taxable event (exchanging one asset for another), but guidance from tax authorities is sparse. Similarly, auditors and regulators debate whether WBTC should be listed as an asset on a company's balance sheet at the fair value of Bitcoin or at a discount reflecting custodial risk. These questions remain largely unanswered.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bridge/">Distributed Ledger</a> — the underlying blockchain systems that wrapped tokens must span.</li>
<li><a href="/wiki/liquidity-pool/">Liquidity Pool</a> — a common use case for wrapped tokens in decentralized finance.</li>
<li><a href="/wiki/automated-market-maker/">Automated Market Maker</a> — protocols that trade wrapped tokens between chains.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/bitcoin/">Bitcoin</a> — the most commonly wrapped asset.</li>
<li><a href="/wiki/ethereum/">Ethereum</a> — the blockchain hosting most wrapped tokens.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty Risk</a> — the main risk factor in wrapped-token systems.</li>
</ul>
</div>

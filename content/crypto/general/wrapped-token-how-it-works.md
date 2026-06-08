---
title: "Wrapped Token: How It Works"
description: "A wrapped token represents an asset from one blockchain recorded on another, allowing cross-chain trading and liquidity."
keywords:
  - wrapped token how it works
  - wBTC wrapped bitcoin
  - cross-chain asset bridge
  - wrapped ethereum
  - synthetic asset blockchain
---

*A **wrapped token** is a representation of an asset from one blockchain on a different blockchain. The original asset is locked in a custodian contract on its native chain, and an equivalent amount of the wrapped version is issued on the destination chain. Wrapped tokens enable assets to move between blockchains, powering cross-chain liquidity and trading without requiring the asset itself to physically leave its original chain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Wrapped Token — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">A tradable claim on an asset locked on another chain, not the asset itself.</div>

|   |   |
|---|---|
| **Original asset** | Locked in a custodian contract on its native blockchain |
| **Wrapped version** | Issued as an ERC-20 (or equivalent) token on the destination chain |
| **1:1 backing** | Each wrapped token is backed by exactly one unit of the original asset |
| **Redemption** | Wrapped tokens can be burned to retrieve the original asset |
| **Custody model** | Centralized custodian or smart contract automated (algorithmic) |
| **Price correlation** | Wrapped token trades near parity with the original, minus fees and trust discount |

</aside>

## Why wrapped tokens exist

Most blockchains are isolated: Bitcoin cannot natively run on Ethereum, and Ethereum tokens cannot exist on Bitcoin. Wrapped tokens bridge this gap.

Why would you want to use a wrapped version instead of the original? The answer is liquidity and capability:

- **DEX trading**: Bitcoin has limited DeFi depth. Wrapped Bitcoin (wBTC) can be traded on Ethereum DEXs (decentralized exchanges), accessed by Ethereum wallets, and used as collateral in lending protocols—none of which Bitcoin natively supports.
- **Smart contracts**: Bitcoin's blockchain does not run Turing-complete smart contracts at scale. A Bitcoin holder wanting to participate in an Ethereum lending pool must wrap their Bitcoin first.
- **Speed and cost**: Ethereum layer 2 networks process transactions faster and cheaper than Bitcoin or Ethereum mainnet. Wrapped assets enable participation in these ecosystems.
- **Arbitrage and trading**: Wrapped tokens allow traders to capture price differences between chains and markets without actually moving the underlying asset.

## Two models: custodial and algorithmic

**Custodial wrapping** (the dominant model) works like this:

1. You send 1 Bitcoin to a custodian (e.g., a regulated entity like Coinbase or a DAO-governed contract like the Wrapped Bitcoin DAO).
2. The custodian locks your Bitcoin in a cold storage vault or smart contract.
3. The custodian mints 1 wBTC (an ERC-20 token) on Ethereum and sends it to your Ethereum address.
4. You can now trade, lend, or use wBTC on Ethereum.
5. To unwrap and recover your Bitcoin, you burn the wBTC, and the custodian transfers Bitcoin back to your original Bitcoin address.

The custodian holds the private keys to the Bitcoin vault (or is controlled by a multi-sig arrangement). This centralization is a weak point: if the custodian is hacked, the Bitcoin backing wBTC could be stolen, and wBTC holders would face losses.

**Algorithmic wrapping** attempts to remove custodian risk. Instead of a single entity locking assets, the wrapped token is collateralized by crypto deposited in smart contracts. For example:

- You deposit $150 worth of Ethereum as collateral.
- You mint $100 worth of a wrapped Bitcoin substitute.
- Your ETH collateral sits in a smart contract, backing the wrapped token's value through over-collateralization.

If the wrapped token's price drops below the collateral backing it, the collateral is liquidated to maintain the peg. This model removes custodian risk but introduces liquidation risk: if the collateral value drops sharply, your deposit could be forcibly sold.

Most wrapped tokens in practice are custodial, because algorithmic models are complex and require careful design to avoid collapse. The most liquid wBTC uses the custodian model.

## How price stays pegged

Ideally, wBTC should trade at exactly the same price as Bitcoin. If wBTC trades cheaper, arbitrageurs can:

1. Buy wBTC on the open market.
2. Unwrap it (burn it and retrieve the underlying Bitcoin).
3. Sell the Bitcoin on a Bitcoin exchange.
4. Pocket the difference.

This buying pressure on wBTC pushes its price back up. Conversely, if wBTC trades *above* Bitcoin's price, arbitrageurs can:

1. Buy Bitcoin.
2. Wrap it (lock it and mint wBTC).
3. Sell wBTC on the open market.
4. Profit from the difference.

These arbitrage flows keep wrapped and original tokens trading near parity. However, the peg can slip during extreme market stress, network outages, or if redemption (unwrapping) is slow or blocked.

## Common examples

**Wrapped Bitcoin (wBTC)**: The most widely held wrapped asset, representing Bitcoin on Ethereum. Custodial, with backing managed by a DAO (the Wrapped Bitcoin DAO) and multiple custodians. wBTC has several billion dollars in circulation and is one of the largest ERC-20 tokens by market capitalization.

**Wrapped Ethereum (wETH)**: Ethereum wrapped on Ethereum itself. This sounds redundant, but it serves a technical purpose: Ethereum's native currency (ETH) doesn't follow the ERC-20 standard, so many DEXs and protocols require ERC-20 compliant tokens. wETH solves this by locking ETH and issuing an ERC-20 wrapper.

**Cross-chain bridges**: Newer bridges like Stargate and Across allow tokens to move across layer 2 networks and alternate layer 1 blockchains. A token might be "wrapped" on Arbitrum, Polygon, or Optimism—each with its own liquidity pool and custodian or algorithmic design.

## Risks specific to wrapped tokens

**Custodian risk**: The custodian could be hacked, regulated out of existence, or experience financial failure. Wrapped Bitcoin's security depends entirely on the custodian(s) protecting the Bitcoin vault.

**Redemption risk**: If redemption is paused (e.g., due to technical issues or regulatory action), wBTC holders cannot unwrap their tokens, potentially causing the peg to break.

**Liquidity risk**: Wrapped tokens are only useful if someone wants to trade them. In a downmarket, liquidity can evaporate, making it hard to unwrap or sell.

**Peg break**: If the wrapped token's price decouples from the underlying asset and stays low, wrapped token holders may face losses that arbitrage cannot heal (e.g., if unwrapping is blocked).

**Smart contract risk** (algorithmic wrapping): Over-collateralized wrapped tokens can face liquidation cascades, where falling collateral prices trigger automatic sales, further depressing the collateral and potentially destabilizing the system.

Most wrapped token risk is *custodian* or *protocol* risk—the direct responsibility of the operator, not the blockchain itself.

## The future: cross-chain standards

As multichain and layer 2 adoption spreads, the number of wrapped versions of the same asset can proliferate. Bitcoin might exist as wBTC on Ethereum, as Stargate's "bridge Bitcoin" on Arbitrum, and as Polygon's wrapped Bitcoin, each with different custodians and risks.

Future standards and protocols aim to standardize wrapping, reduce fragmentation, and possibly eliminate the need for wrapping altogether through native cross-chain communication. For now, wrapped tokens remain one of the main ways assets move between otherwise isolated blockchains.

## See also

<div class="wiki-seealso">

### Closely related

- [Distributed ledger](/distributed-ledger/) — The underlying technology enabling multiple independent blockchains that wrapped tokens bridge
- [Blockchain fundamentals](/blockchain-fundamentals/) — How assets are recorded and verified on chain
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where wrapped tokens are traded
- Smart contract risk — Security considerations for wrapping protocols

### Wider context

- [Bitcoin](/bitcoin/) — The most commonly wrapped asset
- [Ethereum](/ethereum/) — The most common destination chain for wrapped tokens
- [DeFi yield farming risks](/defi-yield-farming-risks/) — Where wrapped assets are deployed for yield
- [How a blockchain hard fork works](/how-a-blockchain-hard-fork-works/) — Related to cross-chain fragmentation

</div>

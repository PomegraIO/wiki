---
title: "Receipt Token"
description: "Protocol-issued tokens representing a claim on deposited collateral, redeemable for the underlying asset plus accrued yield, commonly used in lending and yield protocols."
keywords:
  - receipt token
  - yield farming
  - collateral claim
  - yield-bearing token
  - staking certificate
  - defi receipt
---

*A **receipt token** is a proof of deposit issued by a decentralized finance protocol when a user locks collateral—cryptocurrency, stablecoins, or other assets. The receipt token represents ownership of the deposit plus any accrued rewards or yield; it is redeemable for the original deposit plus earnings, effectively turning idle collateral into an interest-bearing instrument.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Receipt Token — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptographic assets and blockchain instruments." />

<div class="wiki-infobox-caption">A token representing collateral deposited in a yield-generating protocol, claimable for principal plus accrued yield.</div>

|   |   |
|---|---|
| **What it is** | A token issued 1:1 (or ratio-adjusted) for deposited collateral in a DeFi protocol |
| **Also called** | Yield token, staking certificate, deposit receipt, yield-bearing token |
| **Issued by** | Lending protocols, yield farms, or custody contracts |
| **Redeemable for** | Original collateral plus earned interest, fees, or staking rewards |
| **Blockchain standard** | ERC-20 on Ethereum; analogous standards on other blockchains |
| **Primary use** | Capturing yield on idle assets whilst maintaining composability in DeFi |

</aside>

## The yield-capture mechanism

When a user deposits 100 USDC (a stablecoin) into a lending protocol, the protocol mints a receipt token—call it rUSDC—and transfers it to the user's wallet. The USDC is locked in the protocol's vault, where it is lent out to borrowers at an interest rate. Borrowers pay interest, which accumulates in the vault. The user's rUSDC token is a claim on a proportional slice of that growing pool.

A week later, the vault holds $110 worth of USDC (the original $100 plus $10 earned in interest). The user's rUSDC is still technically 100 tokens, but each token now represents a claim on $1.10 of USDC, not $1.00. When the user redeems rUSDC, they receive the interest automatically.

This is elegant for both user and protocol. The user earns yield without moving assets; the receipt token itself is proof of claim, tradable and composable with other [smart contracts](/smart-contract/). The protocol captures a fee (typically 10–20% of interest earned) and uses the user's capital to lend out and earn spread. Everyone benefits.

## Composability and DeFi stacking

A major advantage of receipt tokens is their interoperability. Because they are ERC-20 standard, they can be used as collateral in other protocols, staked for governance, or swapped on [decentralized exchanges](/decentralized-exchange/).

Imagine a user deposits ETH into a liquid staking protocol and receives stETH (a receipt token for ETH in a staking pool). That stETH can then be deposited into a lending protocol to borrow USDC, which is swapped for other assets. The user is earning staking rewards on ETH whilst simultaneously borrowing against it. This layering—sometimes called "yield stacking"—creates complex, high-yield strategies that were impossible in traditional finance, where deposited collateral is locked.

This composability, however, introduces risk. Each layer adds a [smart contract](/smart-contract/) risk vector. A bug in the staking protocol, the lending protocol, or a price oracle could cascade and wipe out the user's position. Experienced DeFi users manage this through stress-testing and risk management, but casual users often underestimate the danger.

## Price dynamics and discounts

Ideally, a receipt token trades at its redemption value: rUSDC worth exactly $1.10 if the underlying vault holds $1.10 per token. In practice, receipt tokens trade at discounts or premiums based on market perception of protocol solvency and yield sustainability.

If a protocol is rumoured to be insolvent (unable to return deposited funds), its receipt token trades at a steep discount. A user might be able to buy rUSDC for $0.80 and redeem it for $1.00 in underlying collateral, capturing a profit. But they also bear the risk that the protocol fully collapses before they can withdraw.

Conversely, if a receipt token offers exceptionally high yield and the protocol is trusted, the token may trade at a premium. Speculators buy to capture yield, bidding up price beyond redemption value. This premium typically erodes as yield-seekers pile in and returns normalise.

## Variations: staking certificates and liquid staking

Receipt tokens go by different names depending on context. In proof-of-stake blockchains, a user who stakes cryptocurrency to secure the network receives a staking certificate—a receipt for staked assets. Traditionally, staking locks the asset: you cannot move, sell, or use it as collateral. Liquid staking protocols issue receipt tokens that unlock this; you stake ETH and receive stETH, which you can trade or use in DeFi immediately.

Other protocols use receipt tokens for yield farming, collateral vaults, or insurance pools. The underlying mechanism is the same: deposit assets, receive a token representing your claim, and redeem when you wish. What varies is the source of yield: lending interest, farming incentives, insurance premiums, or protocol fees.

## Redemption mechanics and the inflation trap

Most protocols allow redemption at any time, though they may impose withdrawal delays or small fees to prevent bank runs. Some implement a redemption curve: if you withdraw a large portion of the pool quickly, you pay a higher fee, incentivising stability and preventing sudden drains.

A critical risk is **redemption failure**. If more users try to withdraw simultaneously than the protocol has liquid reserves, some will be unable to exit. Early withdrawal is prioritised; late arrivals wait in a queue. In extreme cases, a "bank run" can force the protocol into insolvency, and users lose a portion of their deposits.

Additionally, if a protocol's yield is unsustainably high (funded by hyperinflation of protocol-native tokens rather than real economic activity), the receipt token is a diminishing asset. The yield dries up, token price crashes, and users lose their principal. This has happened repeatedly in DeFi: unsustainable yields of 100%+ per annum were mania, not fundamentals.

## Custody and counterparty risk

Receipt tokens shift custody risk. Instead of holding USDC in a personal wallet, you hold a receipt token in a smart contract. The asset is theoretically safer (the protocol's code can be audited) but introduces protocol risk (the code could be exploited). Traditional finance eliminates this by using regulated custodians and insurance; crypto receipt tokens rely on code audits, over-collateralisation, and sometimes insurance funds.

Major protocols mitigate this through transparent reserve verification: on-chain audits prove the vault holds enough collateral to back all receipt tokens. But the risk never vanishes entirely, and users must assess the protocol's track record, team, and code quality before depositing.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart Contract](/smart-contract/) — code managing receipt token issuance and redemption
- ERC-20 — token standard for receipt tokens
- Decentralized Finance — broader ecosystem where receipt tokens are used
- [Staking](/staking/) — process underlying staking certificates and liquid staking
- [Yield Farming](/yield-farming/) — strategy leveraging receipt tokens for high returns
- Collateral — assets backing DeFi lending

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — venues where receipt tokens trade
- [Blockchain Fundamentals](/blockchain-fundamentals/) — underlying ledger technology
- [Interest Rate](/interest-rate/) — yield source for receipt token returns
- Risk Management — strategies for managing DeFi exposure

</div>

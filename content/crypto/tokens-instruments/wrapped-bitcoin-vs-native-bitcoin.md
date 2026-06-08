---
title: "Wrapped Bitcoin vs Native Bitcoin"
description: "Wrapped bitcoin (WBTC) represents native Bitcoin on other blockchains, trading custody and settlement speed for portability and DeFi access."
keywords:
  - wrapped bitcoin vs native bitcoin
  - wbtc wrapped bitcoin
  - bitcoin bridge tokens
  - cross-chain bitcoin
  - bitcoin on ethereum
image: /svg/crypto.svg
---

*A **wrapped bitcoin** (most commonly WBTC) is a token issued on another blockchain—such as Ethereum—that represents a claim on Bitcoin held in custody by a bridge operator. Native Bitcoin exists only on the Bitcoin network itself. The trade-off is immediate: wrapped versions unlock liquidity and composability in decentralized finance ecosystems, but they introduce custodial risk and require trust in the bridge operator.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Wrapped vs native Bitcoin — Key distinctions</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Wrapped tokens move Bitcoin off its native chain to unlock DeFi utility, but custody concentration remains a real risk.</div>

|   |   |
|---|---|
| **Wrapped Bitcoin (WBTC)** | ERC-20 token on Ethereum; 1 WBTC = 1 BTC in custody |
| **Native Bitcoin** | Asset on Bitcoin network; no issuer; cryptographically secured |
| **Custody model** | Wrapped: third-party custodian; Native: self-custody possible |
| **Settlement time** | Wrapped: seconds (Ethereum); Native: Bitcoin block time (~10 min) |
| **Composability** | Wrapped: full DeFi access; Native: limited smart-contract capability |
| **Slashing risk** | Wrapped: custodial default; Native: nil (consensus-secured) |

</aside>

## What wrapped Bitcoin actually is

**Wrapped Bitcoin (WBTC)** launched in 2019 as a bridge asset. The mechanism is straightforward: a user sends native Bitcoin to a custodian (initially BitGo, now operated by a DAO with multiple signers), which locks it in a multi-signature wallet and issues an equivalent amount of WBTC on Ethereum. The user now holds an ERC-20 token that trades on Ethereum dexes, integrates with lending protocols, and participates in liquidity pools—all activities impossible with native Bitcoin.

To redeem, the process reverses: a user burns WBTC on Ethereum, and the custodian releases native Bitcoin from its wallet. In principle, the 1:1 backing is maintained through cryptographic proof and ongoing attestations.

Other chains have followed this pattern. Wrapped Bitcoin on Solana, Polygon, Arbitrum, and other Layer-2 networks operate on the same principle: a token representing locked Bitcoin, issued and redeemable by a custodian or set of custodians.

## The custodial risk trade-off

This is the critical distinction: **native Bitcoin has no custodian**. Its security derives from the Bitcoin network's [proof-of-work](/proof-of-work/) consensus and cryptographic verification. If you control your private keys, no third party can freeze, dilute, or misappropriate your Bitcoin.

Wrapped Bitcoin introduces a **custodian**—a party holding the native Bitcoin in reserve. WBTC is only valuable if the custodian actually holds the Bitcoin and does not:
- Misappropriate it
- Succumb to regulatory seizure (rare, but possible)
- Suffer a security breach (less likely with multi-sig, but not impossible)
- Become insolvent or cease operations

This is not merely theoretical. In recent crypto cycles, custodial breaches have resulted in significant losses. While WBTC's custodian model is more resilient than a single-signature wallet, it remains centralized in the sense that you are trusting a human institution.

Many WBTC users mitigate this by using decentralized custody solutions or by running their own nodes to verify custodian attestations. However, the default user typically accepts the custodian risk in exchange for DeFi access.

## Why wrapped Bitcoin exists: DeFi composability

Native Bitcoin's smart-contract capability is minimal. Bitcoin's scripting language is intentionally limited for security reasons, and on-chain conditional logic is clunky. A Bitcoin holder wanting to lend Bitcoin on a decentralized lending protocol, provide liquidity to an automated market maker (AMM), or participate in a complex options contract faces fundamental constraints.

Wrapped Bitcoin **solves this through portability**. On Ethereum, WBTC is a standard ERC-20 token. It integrates seamlessly with Uniswap, Aave, Curve, and thousands of DeFi applications. A holder can deposit WBTC into a lending protocol and earn yield, trade it in a dex, or use it as collateral in a derivatives contract—all within seconds.

This composability is valuable. A Bitcoin holder in a sustained bear market who wants to earn yield on their Bitcoin without selling it can bridge to Ethereum, deposit into a lending protocol, and earn interest. The alternative—holding native Bitcoin earning nothing—becomes less attractive.

## Settlement speed and cost differences

Native Bitcoin settles slowly by DeFi standards. A transaction on the Bitcoin network takes approximately 10 minutes per block, and confirmation typically requires 3–6 blocks (30–60 minutes). Final settlement is secure and immutable, but it is deliberate.

Wrapped Bitcoin on Ethereum, by contrast, settles in seconds. A Uniswap trade of WBTC for USDC executes and confirms in one Ethereum block (~12 seconds). This speed advantage is material for traders exploiting short-term opportunities or rebalancing positions.

Transaction costs tell a similar story. Bitcoin network fees (denominated in satoshis per byte) vary with congestion but are typically lower in absolute terms than Ethereum's gas costs in dollars. However, Ethereum's recent scaling improvements and Layer-2 solutions (Arbitrum, Optimism) have compressed the cost differential. A wrapped Bitcoin transaction on Arbitrum may cost pennies; native Bitcoin settlement costs multiples of that.

## When to use each

**Native Bitcoin** is the choice when:
- You want maximum security and no custodial risk
- You intend to hold long-term without trading or lending
- You can self-custody and manage key security
- You value Bitcoin's immutable, permissionless settlement

**Wrapped Bitcoin** is rational when:
- You want to earn yield through lending or liquidity provision
- You are actively trading and need fast settlement
- The custodial risk is acceptable given the utility gain
- You plan to redeem back to native Bitcoin within a known timeframe

The choice is not mutually exclusive. Sophisticated users often hold both: native Bitcoin as a core store of value, and wrapped Bitcoin as a smaller trading and yield-generation component.

## Proliferation and standardization risks

Multiple wrapped Bitcoin versions now exist—WBTC on Ethereum, renBTC (via Ren protocol), tBTC (decentralized), and others. Each has a different custody or bridge architecture and faces different risk profiles.

This proliferation creates **fragmentation risk**. A liquidity provider might accumulate a mix of wrapped versions without realizing the different risk profiles. If one bridge operator fails, that portion becomes illiquid or worthless. Standards like the Interoperability Group have attempted to establish best practices, but divergence persists.

The ideal long-term solution, from Bitcoin's perspective, is native Bitcoin smart-contract capability—either through covenant activation or through a sidechain tightly coupled to the main chain. Until then, wrapped Bitcoin remains a pragmatic if imperfect workaround.

## See also

<div class="wiki-seealso">

### Closely related

- [Bitcoin](/bitcoin/) — Native Bitcoin network and properties
- [Ethereum](/ethereum/) — Primary chain hosting wrapped Bitcoin
- [Proof-of-work](/proof-of-work/) — Bitcoin's consensus security model
- Custody — Centralized and decentralized custody structures
- [Liquidity pool](/liquidity-pool/) — DeFi mechanism enabling wrapped Bitcoin trading

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Trading venues for wrapped tokens
- [Smart contract](/smart-contract/) — Ethereum contracts that hold and validate wrapped assets
- Cross-chain bridge — Broader technology enabling asset portability
- [Distributed ledger](/distributed-ledger/) — Blockchain technology underlying both native and wrapped tokens

</div>

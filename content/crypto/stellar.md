---
title: "Stellar"
description: "Stellar is an open-source payment network designed to connect financial institutions and enable efficient cross-border payments. Its native asset is Lumens (XLM), and it uses a federated consensus mechanism."
keywords:
  - stellar
  - xlm
  - lumens
  - payment
  - settlement
  - consensus
image: "/svg/crypto.svg"
---

*A **Stellar** network, with its native **Lumens** (**XLM**) cryptocurrency, is an open-source payment settlement network designed to connect financial institutions and enable rapid, low-cost cross-border transactions. It uses a **federated consensus** mechanism where validators (called nodes) are operated by institutions worldwide.*

<div class="wiki-hatnote">

This entry covers Stellar's network and design. For a competing payment network, see [Ripple XRP](/ripple-xrp) or [Bitcoin](/bitcoin); for consensus mechanisms, see [proof-of-stake](/proof-of-stake).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stellar — key facts</div>

<img src="/svg/crypto.svg" alt="Stellar network and payment flows" />

<div class="wiki-infobox-caption">Stellar: a federated network for global payments.</div>

|   |   |
|---|---|
| **What it is** | An open-source payment network |
| **Native currency** | Lumens (XLM) |
| **Created** | 2014 |
| **Founder** | Jed McCaleb and Joyce Kim |
| **Consensus mechanism** | Stellar Consensus Protocol (federated) |
| **Block time** | ~5 seconds |
| **Transaction finality** | ~5 seconds |
| **Total supply** | ~50 billion XLM |
| **Foundation** | Stellar Development Foundation (non-profit) |

</aside>

## Origins and philosophy

Stellar was founded by Jed McCaleb (co-creator of [Ripple](/ripple-xrp)) and Joyce Kim in 2014. McCaleb, dissatisfied with Ripple's direction, created Stellar to embody similar ideals — fast, low-cost payments — but as a non-profit open-source project rather than a venture-backed company.

Stellar's explicit goal is to serve underbanked populations and individuals, not just financial institutions. It targets developing economies where traditional banking infrastructure is absent or unaffordable.

## The Stellar Consensus Protocol

Stellar uses the **Stellar Consensus Protocol** (SCP), a federated consensus mechanism. Unlike [proof-of-work](/proof-of-work), which requires solving puzzles, or [proof-of-stake](/proof-of-stake), which requires locking collateral, SCP relies on a web of trust.

Each node declares which other nodes it trusts to validate transactions. Consensus emerges from overlapping quorums of trusted nodes. This is more efficient than traditional [proof-of-work](/proof-of-work) but requires careful configuration of the quorum slices.

The advantage is speed and low energy consumption. The disadvantage is that the security model depends on humans' choices about whom to trust, rather than mathematical guarantees.

## Lumens and network operations

Lumens (XLM) serve several purposes:

1. **Transaction fees.** Transactions cost a tiny amount of XLM (less than one cent), preventing spam.
2. **Minimum balance.** Accounts must hold a small minimum of XLM, discouraging frivolous account creation.
3. **Native asset.** XLM can be directly transacted on the Stellar network.

Unlike [Ripple's XRP](/ripple-xrp), Stellar was designed to support multiple assets — any account can issue and trade any asset on the network, with XLM acting as the base currency.

## Multi-asset settlement

One of Stellar's innovations is its built-in multi-asset settlement. The network natively supports tokens representing any currency (USD, EUR, etc.) issued by anchors (institutions that guarantee redemption). Pathfinding algorithms automatically identify the best trading path to exchange assets.

This contrasts with [Bitcoin](/bitcoin), which is a single-asset network, or [Ethereum](/ethereum), where multi-asset swaps require smart contracts and intermediaries.

## Use cases and adoption

Stellar's adoption has been primarily in developing economies. Remittance corridors (transfers of money from workers abroad to home countries) use Stellar heavily. Countries like Nigeria, the Philippines, and parts of Latin America have seen significant Stellar adoption.

IBM, a major backer, has built payment solutions on Stellar. The Stellar Development Foundation has funded projects to expand adoption in underbanked regions.

However, adoption remains below that of [Bitcoin](/bitcoin) or [Ethereum](/ethereum), and speculative trading of XLM is likely far larger than actual payment volume.

## Comparison with Ripple

Stellar and [Ripple](/ripple-xrp) are extremely similar — both are payment networks designed for cross-border settlements. Key differences:

- **Governance.** Stellar is non-profit and open-source; Ripple is for-profit.
- **Target market.** Stellar targets individuals and developing-economy institutions; Ripple targets large banks.
- **Assets.** Stellar natively supports multiple assets; Ripple focuses primarily on XRP.
- **Consensus.** Both use federated models but with different technical implementations.

## Regulatory environment

Stellar has faced fewer regulatory challenges than [Ripple](/ripple-xrp), partly because XLM is not positioned as strongly as a security or investment asset, and partly because Stellar's non-profit status may afford it some regulatory deference.

However, if Stellar adoption increases substantially, regulatory scrutiny may intensify.

## Market position

Stellar has consistently ranked in the top 10–20 cryptocurrencies by [market capitalisation](/market-capitalization). Its price has been more stable than many cryptocurrencies, reflecting its positioning as a payment utility rather than a speculative asset.

Total value locked and actual payment volume on Stellar are difficult to measure but are likely small relative to market cap, suggesting that speculative trading dominates usage.

## See also

<div class="wiki-seealso">

### Closely related

- [Ripple XRP](/ripple-xrp) — a competing payment network with similar goals
- [Bitcoin](/bitcoin) — a single-asset payment cryptocurrency
- [Proof-of-stake](/proof-of-stake) — alternative consensus mechanisms
- [Cryptocurrency exchange](/cryptocurrency-exchange) — where XLM trades

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Distributed ledger](/distributed-ledger) — Stellar's network architecture
- [Public blockchain](/public-blockchain) — Stellar is permissionless
- Smart contract — Stellar supports limited scripting
- Layer-2 — alternative scaling approaches

</div>

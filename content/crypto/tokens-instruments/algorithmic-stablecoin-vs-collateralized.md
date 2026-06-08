---
title: "Algorithmic Stablecoin vs Collateralized Stablecoin"
description: "Two designs compete to hold a stablecoin's peg: algorithmic stablecoins use supply mechanics; collateralized ones hold reserve assets. Each carries distinct risks."
keywords:
  - algorithmic stablecoin
  - collateralized stablecoin
  - stablecoin design
  - cryptocurrency peg
  - token mechanisms
  - stablecoin reserves
image: "/svg/crypto.svg"
---

*A **stablecoin** aims to stay pegged to a reference value (usually the US dollar), but **two fundamentally different designs** compete to achieve this: algorithmic stablecoins adjust supply based on demand signals, while collateralized stablecoins hold reserve assets backing each token issued. The choice determines robustness, capital efficiency, and which scenarios trigger a peg failure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stablecoin Design — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two competing mechanisms to maintain a price peg in decentralized systems.</div>

|   |   |
|---|---|
| **Collateralized** | Holds reserve assets (dollars, bonds, crypto) to back issued tokens; peg backed by hard value |
| **Algorithmic** | Adjusts supply dynamically via price signals; peg backed by incentive mechanics |
| **Collateralization ratio** | Overcollateralized typically 150%–200%; algorithmic requires only incentive alignment |
| **Reserve transparency** | Collateralized: regular audits required; algorithmic: on-chain visible (but contracts may fail) |
| **Failure mode** | Collateralized: runs on reserves if confidence breaks; algorithmic: death spiral if incentives misalign |
| **Capital efficiency** | Algorithmic: better (no locked collateral); collateralized: worse (capital tied up) |
| **Real-world examples** | USDC (collateralized, fiat-backed); UST (algorithmic, failed 2022); DAI (collateralized, crypto-backed) |

</aside>

## Collateralized stablecoins: reserves as the peg anchor

A **collateralized stablecoin** is straightforward in principle: you hold reserve assets and issue tokens only up to the value of those reserves. If a stablecoin issuer holds $1 billion in cash, Treasury bonds, and short-term securities, it issues $1 billion in tokens. Each token is backed by a dollar-denominated reserve.

### Fiat-backed collateral

The strongest collateralized stablecoins (USDC, USDT) hold cash and short-term Treasury securities at banks and custodians. Reserves are regularly audited by third parties, proving 1:1 or near-1:1 backing. If the peg slips below $0.99, arbitrageurs buy tokens and redeem them for dollars at par, enforcing the peg. If it trades above $1.01, issuers mint new tokens to capture the premium, again anchoring the price.

This mechanism is robust: as long as the issuer retains a liquid reserve and honors redemptions, the peg is nearly unbreakable.

### Crypto-backed collateral

Other collateralized stablecoins (DAI, Aave's stablecoins) use crypto tokens (Ethereum, or other blockchain assets) as collateral. A user deposits, say, $2,000 worth of [Ethereum](/ethereum/) and borrows $1,000 of DAI stablecoin. The protocol maintains a 2:1 collateral ratio; if Ethereum falls, the position is liquidated to preserve the peg.

Crypto collateral works in principle, but is riskier: if collateral assets lose value rapidly, liquidations may cascade, forcing fire sales and peg breaks. DAI suffered peg slippage during the March 2020 market crash and the May 2022 Luna-UST collapse because liquidations queued up.

### Overcollaterlization

Collateralized stablecoins are almost always **overcollateralized**—a token's backing exceeds 100%. Fiat-backed coins like USDC are at or near 100% because fiat deposits are stable. Crypto-backed systems require 150%–200% to cushion volatility. This means capital is locked up: a trader who wants to borrow $100 of DAI must post $200 of Ethereum, tying up capital that could be invested elsewhere.

## Algorithmic stablecoins: supply mechanics as the peg anchor

An **algorithmic stablecoin** trusts market incentives, not reserves, to maintain the peg. The protocol adjusts the supply of stablecoins based on the market price. If the stablecoin trades below $1, the system introduces scarcity (burning tokens or offering rewards to remove supply) to push the price back up. If it trades above $1, the system mints new tokens, flooding the market and pushing price down.

### The incentive mechanism

The most common design uses a **secondary token** (often called the governance or seigniorage token) to manage the peg. If the stablecoin falls to $0.95, the protocol offers users an arbitrage: burn $0.95 of governance token and receive $1 of stablecoin. This incentivizes token buyers to participate, reducing stablecoin supply and raising its price. If the stablecoin trades above $1, users can burn $1 of stablecoin and receive governance tokens, minting governance supply and pushing price down.

The mechanism is elegant on paper: it requires no locked collateral, so capital is not wasted. A fully algorithmic system is 100% capital efficient.

### Terra and UST: the algorithmic failure

Terra's UST stablecoin was the most famous algorithmic design. UST was backed by incentives only; users could always exchange $1 worth of the LUNA governance token for 1 UST, and vice versa. For years, the peg held. But in May 2022, a series of withdrawals from Anchor (a high-yield lending protocol) broke confidence. Users rushed to redeem UST for LUNA. As LUNA supply exploded, LUNA's price crashed from $80 to near-zero, and UST fell to $0.10. No collateral protected it; the mechanism relied on faith that LUNA would hold value, and faith evaporated.

This outcome revealed the core fragility of pure algorithmic designs: they are only as strong as confidence in the secondary token's value. Once that breaks, the peg collapses irreversibly.

## Comparative risk table

| Risk | Collateralized | Algorithmic |
|------|---|---|
| **Reserve loss** | Mitigated by audits; risk if reserves move to lower-quality assets | N/A (no reserves) |
| **Confidence shock** | Manageable: liquidity and transparency restore trust | Catastrophic: death spiral likely irreversible |
| **Volatility in collateral** | Handled by overcollateralization; liquidation cascades possible | Passed to secondary token; amplifies pressure |
| **Scalability** | Limited by capital available for reserves | Theoretically unlimited (no collateral constraint) |
| **Regulatory clarity** | Higher: backed by tangible assets (favoured by regulators) | Lower: relies on incentive mechanism (regulatory uncertainty) |

## When each design works best

**Collateralized stablecoins** are suited for:
- Use cases requiring regulatory approval (banks, payment companies).
- Scenarios where collateral is abundant and stable (USDC with Treasury backing).
- Situations where the peg must hold in stress (crypto collateral with high ratio).

**Algorithmic stablecoins** theoretically work best for:
- Use cases where collateral is unavailable or uneconomical.
- Communities with strong, sustained belief in the governance token.
- Protocols that do not face sudden loss of confidence.

In practice, after the UST collapse, pure algorithmic designs have largely been abandoned. A handful of hybrid stablecoins (part collateral, part algorithmic incentive) exist, but the pendulum has swung hard toward collateralized coins.

## Hybrid and fractional designs

Some newer stablecoins blend both approaches: they hold partial collateral (e.g., 50%) backed by reserve assets, and offset the remainder via algorithmic supply management or governance mechanisms. Frax is an example. This trades off capital efficiency against resilience: less collateral than full backing, but more safety than pure algorithms.

These hybrids are less elegant but pragmatic; they implicitly acknowledge that collateral is the stronger peg anchor and that algorithms alone are insufficient.

## Regulatory trajectory

Regulators increasingly favor collateralized stablecoins, especially those backed by fiat and short-term Treasury securities. The EU's MiCA framework and proposed US stablecoin legislation both assume reserves backing. Algorithmic stablecoins are often viewed as speculative and are either banned or heavily restricted in proposed rules.

This regulatory bias will likely make collateralized designs the standard for any stablecoin that aspires to broad, legitimate adoption.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where stablecoins trade and are redeemed.
- [Distributed Ledger](/distributed-ledger/) — Technical substrate enabling stablecoin protocols.
- [Ethereum](/ethereum/) — The primary blockchain for crypto-collateralized stablecoins.
- [Smart Contract](/smart-contract/) — Implements peg-maintenance logic.
- [Proof of Stake](/proof-of-stake/) — Governance token mechanics.

### Wider context

- [Bitcoin](/bitcoin/) — Largest cryptocurrency; subject to stablecoin comparisons.
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Primary venue for stablecoin liquidity.
- [Blockchain Fundamentals](/blockchain-fundamentals/) — Technical foundation for all stablecoins.

</div>

---
title: "Money Market Protocol"
description: "Decentralized lending platforms where borrowers and lenders interact through pooled smart contracts and algorithmically adjusted interest rates."
keywords:
  - money market protocol
  - algorithmic interest rates
  - aave
  - compound
  - liquidity pool
  - defi lending
image: "/svg/crypto.svg"
---

*A **money market protocol** is a decentralized smart-contract system that matches borrowers and lenders by letting them deposit and withdraw assets into shared pools, with interest rates determined automatically by supply and demand. Aave and Compound pioneered this model; they are now the dominant architecture for on-chain lending.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Money Market Protocol — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and decentralized finance." />

<div class="wiki-infobox-caption">The engine of DeFi: pooled lending at algorithmic rates.</div>

|   |   |
|---|---|
| **What it is** | Smart-contract system allowing crypto asset lending and borrowing with supply–demand interest rates |
| **Key components** | Liquidity pools, interest rate curves, collateral requirements, liquidation mechanisms |
| **Primary use** | On-chain lending and borrowing without intermediaries |
| **Pioneered by** | Compound (2018), Aave (2018) |
| **Advantages** | Non-custodial, composable, transparent on-chain rates |
| **Risks** | Smart contract bugs, [liquidation](/liquidation/) cascades, oracle failure, impermanent loss |

</aside>

## How the pool economy replaces the bank

In a traditional bank, depositors surrender custody to the institution; the bank pays them interest from borrowers' loan payments. Money market protocols invert this: liquidity pools are transparent smart contracts on a public blockchain where anyone can deposit collateral or borrow against posted collateral. The protocol itself holds no assets—only the code that governs who owns what. Lenders deposit assets directly into a pool, earning interest; borrowers post collateral (often different from what they borrow) and pay interest proportional to their outstanding debt. Both rates fluctuate continuously as the pool balance changes.

The key innovation is that interest rates are not set by committee. Instead, a curve—usually a simple formula—maps the pool's *utilization ratio* (borrowed amount ÷ total deposits) to an interest rate. When utilization is low, rates are cheap (few borrowers compete for capital); when utilization spikes, rates climb. This automatic feedback loop encourages lending during shortages and discourages borrowing when capital is scarce. No bank officer need intervene.

## The utilization curve as monetary policy

Each protocol implements its own interest rate curve, but the principle is universal: the curve is an upward-sloping line or piecewise function tying utilization to borrowing rates. Deposit rates are derived as a fraction of borrowing rates (the spread funds the protocol). Consider Aave: when utilization climbs past 80%, rates accelerate sharply; when it exceeds 100%—meaning there are more borrowed units outstanding than deposits—the curve becomes nearly vertical, effectively closing the tap on new borrowing.

This mechanism serves a vital function: it prevents a liquidity death spiral. If a run begins and deposits drain faster than borrowers repay, rising utilization rates make borrowing suddenly expensive, discouraging fresh debt and encouraging existing borrowers to repay. The protocol thus auto-stabilizes through price (interest rate), not by fiat.

Different protocols tune their curves differently. Stable assets (e.g., USDC) often have gentler slopes and higher maximum rates; volatile assets (e.g., ETH) may have steeper curves. This granularity is a source of competitive differentiation and allows risk managers to match rate structures to asset risk.

## Collateral, leverage, and liquidation

Borrowing in a money market protocol always requires posting collateral—often more value than one intends to borrow. A borrower might deposit 1 ETH (worth $2,000) to borrow 1,000 USDC, accepting a collateral ratio of 50%. If the borrower's collateral falls below the required threshold (say, due to an ETH price drop), a liquidator—any third party—may execute a liquidation: the liquidator repays the outstanding debt and claims the collateral, typically at a discount (liquidation bonus, e.g., 5–10%). This mechanism ensures the protocol maintains solvency; collateral backing shrinks, but insolvency is prevented by forced closure of undercollateralized positions.

This design creates leverage opportunities. A user might deposit 1 ETH, borrow stablecoins against it, swap those stablecoins for more ETH, deposit that ETH to borrow again, and so forth—amplifying ETH exposure. Equally, it creates tail risk: if ETH drops suddenly and liquidations cascade before transactions can execute, the protocol may become insolvent. Most modern protocols mitigate this via risk parameters (e.g., loan-to-value ratios per asset) and circuit breakers, but tail events remain possible.

## Composability and recursive exposure

Money market protocols are composable—a user's position in one protocol can be collateral in another, or proceeds can be routed to yield-farming strategies. This composability is a strength (capital efficiency, complex strategies) and a source of fragility. A protocol exposing itself to another protocol's smart-contract risk, oracle risk, or collateral quality risk accumulates unseen leverage. Cascading liquidations in one protocol can trigger failures in dependent protocols, a risk heightened during market stress.

## Governance and protocol evolution

Early protocols like Compound introduced tokenized governance: the protocol issued a governance token (COMP) that allows holders to vote on parameter changes—interest rate curves, asset listings, risk settings, and protocol fees. This model democratizes control but introduces new attack surfaces: flash loan attacks can briefly acquire enough tokens to pass votes; voters may have misaligned incentives with depositors. Most established protocols have matured their governance structures through multisig-controlled time locks and academic review of risky changes.

## Scale and maturity

The largest protocols (Aave, Compound) manage tens of billions in deposits. Their codebases are battle-tested and audited repeatedly. Smaller protocols and new experimental curves carry higher risk. The entire ecosystem depends on robust oracle infrastructure to price collateral; oracle failure or price manipulation is a recurring attack vector. The market has evolved to demand multiple oracle sources and price staleness protections.

## See also

<div class="wiki-seealso">

### Closely related

- Compound — pioneering on-chain lending protocol and governance model
- Aave — largest money market protocol by assets under management
- Collateral — assets pledged to secure borrowing
- [Liquidation](/liquidation/) — forced closure of undercollateralized positions
- Oracle — trusted price feed mechanism
- [Yield farming](/yield-farming/) — strategies exploiting protocol incentives

### Wider context

- Decentralized Finance — ecosystem of non-custodial protocols
- [Smart contract](/smart-contract/) — self-executing code on blockchains
- Cryptocurrency — digital assets native to blockchains
- Leverage — borrowing to amplify exposure

</div>

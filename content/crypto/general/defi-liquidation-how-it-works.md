---
title: "DeFi Liquidation: How It Works"
description: "DeFi liquidation occurs when a borrower's collateral value falls below the protocol's required threshold, triggering automatic sale of collateral to repay the loan."
keywords:
  - defi liquidation how it works
  - collateral liquidation protocols
  - health factor threshold
  - liquidation mechanics
image: /svg/crypto.svg
---

*A **DeFi liquidation** occurs when a borrower's collateral drops in value and falls below the minimum required by the protocol, triggering an automated sale of that collateral to repay the loan. The process is mechanical, incentive-driven, and systemic to all on-chain lending.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DeFi Liquidation — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Liquidation is the enforcement mechanism that keeps lending protocols solvent when collateral values swing.</div>

|   |   |
|---|---|
| **Trigger** | Collateral value ÷ borrowed value falls below protocol's health factor threshold |
| **Health factor** | Typical threshold: 1.2–1.5 (varies by protocol and asset) |
| **Who executes** | Liquidators: third parties running bots that profit from the liquidation |
| **Liquidation bonus** | Liquidators receive 5–10% discount on collateral (compensation for execution and risk) |
| **Speed** | Happens on-chain in seconds if profitably triggered; often at block production time |
| **Borrower outcome** | Loses collateral; debt is partially or fully repaid by liquidator |

</aside>

## The health factor: how protocols measure solvency

Every borrower in a DeFi lending protocol holds a **health factor**, a real-time ratio that measures whether they are solvent:

**Health Factor = (Collateral Value × Liquidation Threshold) ÷ Borrowed Amount**

If a borrower deposits $10,000 in ETH as collateral and borrows $6,000 in USDC:

- Collateral value: $10,000.
- Borrowed value: $6,000.
- Liquidation threshold (set by the protocol, often 75–80%): 0.75.
- **Health factor = ($10,000 × 0.75) ÷ $6,000 = 1.25**.

A health factor above 1.0 means the collateral is worth more than the borrowed amount. The borrower is safe.

If ETH's price falls and the collateral value drops to $7,500:

- **Health factor = ($7,500 × 0.75) ÷ $6,000 = 0.9375** (below 1.0).

The borrower is now insolvent by the protocol's metric. Liquidation is triggered.

## Why the threshold exists

The liquidation threshold protects the protocol, not the borrower. Markets are volatile. [Cryptocurrency](/cryptocurrency-exchange/) prices move 5%, 10%, or 20% in a day. The threshold is a buffer: if collateral loses 20% of its value, the borrower should still have positive equity.

Different assets have different thresholds. Stablecoins (which should not move much) might have a 95% threshold. Volatile altcoins might have 50%. This reflects the protocol's assessment of each asset's price stability and liquidity.

If the protocol used a 1.0 threshold (no buffer), any small price move would trigger liquidation, and the protocol would be constantly liquidating borrowers with no margin for volatility. Liquidation itself has costs and delays; a buffer allows borrowers to continue as long as they maintain reasonable leverage.

## How liquidation executes

When a health factor drops below 1.0, the loan enters a liquidatable state. Liquidators—third-party actors running automated bots—detect this and submit a liquidation transaction to the blockchain.

The liquidator calls the protocol's liquidation function, specifying:

- The borrower's address.
- The amount of debt to repay (partial or full).
- The collateral asset to receive.

The protocol:

1. Accepts the liquidator's payment (USDC, or whatever the debt is denominated in) into the protocol contract.
2. Seizes the borrower's collateral (ETH, or whatever was pledged).
3. Gives the liquidator the collateral, minus the debt, minus a liquidation fee.

The entire sequence happens in a single transaction, atomically. Either it all succeeds or it all reverts; there is no in-between.

## The liquidation bonus: incentive for execution

Liquidators take on execution risk and deploy capital. To compensate, the protocol gives them a discount on the collateral they claim. This is the **liquidation bonus** or liquidation incentive, typically 5–10%.

If a liquidator repays $6,000 of the borrower's debt and the collateral is worth $7,500, the liquidator receives:

**Collateral given = $6,000 ÷ (1 − liquidation bonus) = $6,000 ÷ 0.95 = $6,315.79** (at 5% bonus).

The liquidator profits $315.79 on the transaction, minus gas/transaction fees. This profit is the incentive for liquidators to run bots and monitor the protocol.

If the profit is too small, liquidators ignore the transaction and the borrower's loan remains unpaid. If the profit is too large, liquidation is too punitive to the borrower.

## Cascading liquidations and systemic risk

When one asset's price crashes, multiple borrowers can become insolvent simultaneously. All their positions enter liquidation. If liquidators cannot execute fast enough, or if the collateral asset itself is illiquid (cannot be sold for the full value), liquidations can cascade.

The most severe scenario: a borrower has borrowed a stablecoin using a volatile token as collateral. The volatile token crashes 80%. The protocol tries to liquidate, but in doing so, it sells so much of that token that its price crashes further, triggering more liquidations. This is a **liquidation spiral**.

Protocols defend against this with:

- **Loan-to-value (LTV) limits**: borrowers cannot borrow more than a fraction of collateral value, leaving room for price swings.
- **Tiered collateral**: not all assets can be used as collateral; only those with sufficient liquidity.
- **Isolation**: some volatile or low-liquidity assets cannot be used alongside borrowed stablecoins; they create a separate, limited-size market.

## Partial vs. full liquidation

Most protocols allow **partial liquidation**: a liquidator can repay only a portion of the debt, not all of it. This lets multiple liquidators share the opportunity, prevents any single liquidator from being over-exposed, and lets the borrower retain some collateral.

For example, if a borrower owes $6,000, one liquidator might repay $3,000 and claim collateral, and a second liquidator might repay the remaining $3,000. The borrower's position is closed, but neither liquidator had to deploy $6,000 at risk.

Some protocols cap the maximum portion liquidable per transaction (say, 50%), forcing distributed liquidations and preventing single-liquidator dominance.

## Bad debt and protocol insolvency

If liquidation fails—the collateral is worth less than the debt, or is completely illiquid—the protocol absorbs the loss. This is **bad debt**. The lending protocol is now insolvent; it has promised to pay lenders more than its collateral is worth.

Most protocols have a reserve fund (built up from liquidation bonuses and fees) to absorb bad debt. Some use a tiered bailout: first the reserve is exhausted, then lenders proportionally lose funds, or the protocol governance votes on how to distribute losses.

In extreme cases (like the 2023 FTX crisis, where FTX's collateral was fraudulent), entire protocols fail and users lose their funds entirely.

## Flash loans and liquidation arbitrage

[Distributed ledgers](/distributed-ledger/) and [smart contracts](/smart-contract/) allow an unusual form of liquidation arbitrage: a liquidator can borrow a large sum in a flash loan (a loan that must be repaid within the same transaction), use it to liquidate a borrower, sell the collateral for more, repay the flash loan, and pocket the difference. This is possible because everything happens in a single atomic transaction.

Flash loan liquidation arbitrage has made liquidation more efficient (more liquidators, faster execution) and more profitable for bots. It has also introduced new risks: attackers can use flash loans to manipulate prices and trigger unwarranted liquidations.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart Contract](/smart-contract/) — the code that executes liquidation atomically
- [Distributed Ledger](/distributed-ledger/) — the record of collateral and debt
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where collateral values are set

### Wider context

- [Proof of Stake](/proof-of-stake/) — the consensus mechanism on which most DeFi protocols run
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the infrastructure underlying lending
- [Market Risk](/market-risk/) — the price volatility that triggers liquidation

</div>

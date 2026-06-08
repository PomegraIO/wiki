---
title: "Liquidation Mechanism"
description: "Automated process by which DeFi protocols seize and sell borrower collateral when it falls below required thresholds."
keywords:
  - liquidation
  - defi auction
  - liquidator bot
  - collateral sale
  - health factor
  - liquidation penalty
  - flashloan attack
image: "/svg/crypto.svg"
---

*A **liquidation mechanism** is the automated process by which a DeFi lending protocol seizes collateral from a borrower whose health factor has fallen below a safe threshold, auctions that collateral, and repays itself from the proceeds—protecting the protocol (and other depositors) from losses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidation Mechanism — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the cryptocurrency and decentralized finance topic." />

<div class="wiki-infobox-caption">The enforcement mechanism that turns overcollateralization from a rule into economic reality.</div>

|   |   |
|---|---|
| **What it is** | Automated seizure and sale of collateral when loans become undercollateralized |
| **Triggered by** | Health factor falling below liquidation threshold |
| **Executor** | Liquidator bots (any third party with incentive) or protocol-run auctions |
| **Liquidator incentive** | Bonus discount on auction proceeds (typically 5–15%) |
| **Penalty on borrower** | Lost upside, additional liquidation fee (often 5–10%) |
| **Price execution** | On-chain auction or third-party sale on secondary markets |

</aside>

## Why liquidation is necessary

In [overcollateralized lending](/overcollateralized-lending/), the collateral is the lender's ultimate security. But collateral prices move continuously. If a borrower deposits ETH collateral worth $30,000 and borrows $20,000 stablecoins, the protocol is protected—until ETH price crashes 50% overnight. Now the collateral is worth $15,000, less than the $20,000 loan. The protocol is technically insolvent: its assets (the collateral) are worth less than its liabilities (the owed loan). If liquidation does not occur, depositors who have lent stablecoins to the protocol will not be fully repaid.

Liquidation prevents this cascade by forcing the sale of collateral before it deteriorates further, ensuring the loan is repaid while sufficient collateral remains. Without liquidation, overcollateralized lending collapses into a bank run.

## The liquidation process

When a borrower's health factor falls below the protocol's liquidation threshold—typically 1.2 to 1.5—anyone can call a "liquidate" function on the smart contract. The liquidator supplies enough stablecoins (or other acceptable repayment asset) to cover part or all of the loan. In exchange, the liquidator receives a portion of the collateral, plus a bonus.

The bonus is the liquidator's compensation. If normal liquidation would return $20,000 worth of ETH (to match the $20,000 loan), the liquidator instead receives $21,000–$23,000 worth of ETH for their $20,000 payment. The protocol absorbs the extra $1,000–$3,000 cost (the liquidation bonus) from the seized collateral.

This design accomplishes several things:
- It incentivizes rapid liquidation (the sooner a liquidator acts, the larger the bonus relative to the borrow amount).
- It allows any third party to participate; liquidators do not need permission or a license.
- It ensures collateral is liquidated continuously, preventing the protocol from holding underwater positions.

## Liquidator bots and the liquidation arms race

In practice, liquidation is dominated by automated bots watching every loan on every protocol, ready to liquidate the instant health factor drops. These bots must be fast: other liquidators are watching the same opportunity. The first to call the liquidation function wins the bonus. Liquidators therefore:

- Monitor on-chain events (price feeds, collateral balance changes) in real-time.
- Pre-sign transactions or use flashbots to gain ordering advantage.
- Maintain stablecoins in reserve, ready to deploy instantly.

The competition is brutal and largely invisible. A borrower might be underwater for only milliseconds before a liquidator seizes the collateral. This speed benefits the protocol and other depositors (who are protected from insolvency) and harms the borrower (who has no opportunity to repay or adjust their position).

Some protocols have introduced "liquidation grace periods" (e.g., 1–2 minutes after health factor breach) during which only the protocol itself, not third-party liquidators, can liquidate. This gives borrowers a small window to deposit more collateral or repay, reducing the unfairness. But grace periods also reduce efficiency and increase protocol risk, so they are uncommon.

## Auction mechanisms and price execution

How is the collateral actually sold? There are several approaches:

**Direct liquidation**: The liquidator receives collateral directly, at a preset discount. Most common, fastest, but the liquidator now holds a volatile asset and must sell separately, risking slippage.

**On-chain auction**: The protocol itself auctions the seized collateral, with multiple potential buyers bidding in real-time. This can achieve better prices than direct liquidation but adds latency and complexity.

**Batch liquidation**: The protocol collects seized collateral and sells it in bulk on a secondary exchange (Uniswap, Curve, etc.), amortizing slippage across many positions.

Most modern protocols use direct liquidation for speed and certainty, accepting that the liquidator may pocket extra value from the subsequent resale.

## Liquidation penalties and borrower costs

Beyond the liquidation bonus paid to the liquidator, borrowers often pay an additional penalty (typically 5–10% of the loan value) to the protocol itself. This penalty serves as a deterrent—no rational borrower wants to be liquidated. But more importantly, it compensates the protocol for the cost and risk of maintaining the liquidation machinery.

In the worst case, a borrower who was collateralized at 160% LTV (safe) can suddenly be underwater if collateral drops 40% in minutes. That borrower loses not only the price move but also the liquidation bonus (5–15% of collateral) and the penalty fee (5–10% of borrowed amount). The total cost can exceed 25–30% of the original collateral in volatile conditions.

This creates a powerful incentive to maintain a conservative health factor if collateral is volatile. Borrowers who maximize leverage are taking a bet not only on collateral price but on volatility and the probability of sudden moves.

## Flash loans and liquidation attacks

A **flashloan** is a loan that must be repaid within a single transaction. A malicious actor can take a flashloan, manipulate prices on a small AMM pool, trigger liquidations at those manipulated prices, pocket the liquidation bonuses, repay the flashloan, and profit—all within one block. This attack exploits the assumption that liquidators execute at accurate prices.

Protocols defend against this by:
- Using time-weighted or oracle-derived prices, not spot prices from volatile pools.
- Requiring liquidations to be executed through trusted price sources (Chainlink, Band Protocol) rather than direct AMM quotes.
- Capping the liquidation bonus to prevent extremely high profits from price manipulation.
- Requiring waiting periods or challenge mechanisms before liquidation.

The arms race between attackers and protocols is ongoing, with new vulnerabilities occasionally discovered.

## Liquidation cascades and system risk

In volatile markets, cascading liquidations can occur. When collateral price drops sharply, many borrowers breach their liquidation thresholds simultaneously. If the collateral asset itself is common across borrowers (e.g., many borrowed against ETH), the resulting fire sale of collateral further depresses its price, triggering additional liquidations in a feedback loop.

Protocols with high leverage concentrations in single collateral types are most vulnerable. Some protocols have introduced circuit breakers (pausing liquidations during extreme moves) or dynamic parameter adjustments (temporarily raising collateral ratios to reduce liquidation frequency). These mechanisms buy time for market recovery but can create other problems (frozen positions, protocol insolvency if prices don't recover).

## See also

<div class="wiki-seealso">

### Closely related

- [Overcollateralized Lending](/overcollateralized-lending/) — the lending mechanism that liquidation protects
- [CDP Stablecoin](/cdp-stablecoin/) — another DeFi product with its own liquidation dynamics
- [Yield Aggregator](/yield-aggregator/) — protocols that must account for liquidation risk when deploying capital
- [Distributed Ledger](/distributed-ledger/) — the blockchain infrastructure enabling real-time liquidation
- Flash Loan — temporary loans used in attacks and arbitrage

### Wider context

- [Systemic Risk](/systemic-risk/) — how localized failures cascade across financial systems
- [Counterparty Risk](/counterparty-risk/) — the risk that a protocol itself fails
- [Market Maker Trading](/market-maker-trading/) — how liquidators operate as market participants

</div>

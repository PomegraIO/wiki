---
title: "Collateral Ratio"
description: "The ratio of collateral value to debt in an overcollateralized DeFi lending protocol, determining whether a borrower is in good standing or facing liquidation."
keywords:
  - collateral ratio
  - defi
  - overcollateralization
  - liquidation
---

*A **Collateral Ratio** (or "collateralization ratio") in [decentralized finance](/wiki/defi-composability/) (DeFi) is the proportion of collateral value to borrowed amount. If a borrower deposits $200 of [Ethereum](/wiki/ethereum/) to borrow $100 of [stablecoins](/wiki/stablecoin/), the collateral ratio is 200% (2:1 debt-to-collateral). Most DeFi lending requires ratios above 100% to ensure the borrower cannot disappear with the borrowed funds without loss.*

<aside class="wiki-infobox">

| Key Fact | Detail |
|---|---|
| **Formula** | Collateral value / Debt value (typically expressed as %) |
| **Minimum ratio** | Usually 110–150% depending on asset volatility |
| **Liquidation trigger** | Occurs if ratio falls below the minimum (e.g., if collateral price drops) |
| **Risk transfer** | Higher ratio = safer for lender, more capital-inefficient for borrower |
| **Liquidator function** | Automated bots or keepers execute liquidations when ratio breaches |
| **Governance** | Protocol sets minimum ratios; governed by DAO in decentralized protocols |

</aside>

## Overcollateralization in DeFi

Traditional banking relies on credit assessment—lenders evaluate a borrower's income, credit history, and ability to repay. DeFi protocols cannot assess creditworthiness (users are pseudonymous), so they enforce a different model: **overcollateralization**. You must put up more collateral than the value of the debt you incur, guaranteeing that if you default, the collateral can be seized and sold to repay the lender.

A borrower on Aave, a major lending protocol, might deposit 3 [Ethereum](/wiki/ethereum/) worth $9,000 and borrow 5,000 [USD Coin](/wiki/stablecoin/) (USDC). The collateral ratio is 180% (9000 / 5000). If the borrower defaults (simply never repays), Aave keeps the 3 ETH, sells it, and covers the loss. The overcollateralization ensures that even if ETH price falls 20%, Aave still breaks even.

## Why collateral ratios vary by asset

Not all collateral carries the same risk. [Bitcoin](/wiki/bitcoin/), with its long history and large market cap, is less volatile than an obscure altcoin. A protocol might accept a 110% collateral ratio for BTC but require 200% for a newer token. This is similar to traditional lending: a bank will lend 80% of the value of a home (a relatively stable asset) but only 50% of the value of a used car (more volatile).

The DeFi protocol's price oracle is crucial. If the oracle incorrectly reports the collateral's price—say, marking ETH as $100 when it is really $3,000—the protocol will incorrectly calculate the collateral ratio and allow unsafe borrowing. Several DeFi hacks have exploited oracle price errors.

## Liquidation mechanics

When collateral price falls, the collateral ratio declines. If a borrower has a 150% ratio (15,000 in collateral, 10,000 in debt), and collateral price falls 20%, the ratio drops to 120% (12,000 in collateral, 10,000 in debt). If the protocol's minimum is 125%, the position is underwater and eligible for liquidation.

A liquidator—typically a bot watching the blockchain—notices the breached ratio and executes a liquidation. The liquidator repays the debt on the borrower's behalf (using their own capital), seizes the collateral, and receives a penalty—usually 5–10% of the seized amount—as compensation for the effort and capital. The borrower loses the collateral and is left with no outstanding debt.

This mechanism creates a profit opportunity: liquidators compete to identify positions that are about to breach the minimum ratio, execute liquidations, and pocket the penalty. In volatile markets, liquidation is a major event; a sudden price drop can cascade into hundreds of millions of dollars of liquidations as borrowers lose collateral in rapid succession.

## Historical liquidations

When [Ethereum](/wiki/ethereum/) price crashed from $3,000 to $1,300 in May 2021, DeFi protocols experienced a cascade of liquidations. Borrowers who had a 150% ratio at $3,000 suddenly found their ratio at ~65% as the collateral price halved. Within hours, billions of dollars of collateral was seized and liquidated, further depressing prices.

Another famous event was the collapse of FTX and Alameda in 2022. Alameda had borrowed heavily using illiquid FTX exchange tokens as collateral, miscalculating the collateral ratio (the oracle was probably out of date or manipulated). When FTX imploded, the collateral value went to zero, and Alameda's DeFi positions were liquidated.

## The borrower's trade-off: capital efficiency vs. safety

A DeFi borrower faces a choice. Borrow at a 110% collateral ratio (capital-efficient: nearly as much borrowed as collateral, maximizing leverage) but risk rapid liquidation if price moves 10%. Or borrow at 200% (capital-inefficient: half as much borrowed, but very safe—would require a 50% price drop to liquidate).

The borrower must balance yield on the borrowed asset against liquidation risk. A farmer might borrow stablecoins at 110% and deploy them into a yield-farming strategy expecting 20% annual return. If the strategy pays off, they profit handsomely; if collateral price falls 10%, they're liquidated. This is the essence of DeFi leverage.

## Dynamic ratios and insurance

Some advanced DeFi protocols use **dynamic minimum ratios**: the required ratio adjusts based on volatility. High volatility (high liquidation risk) → higher minimum ratio. Low volatility → lower minimum ratio. This makes borrowing cheaper during stable periods and more expensive (safer) during turbulent periods.

Some protocols offer **liquidation insurance**: a user can pay a premium (similar to an insurance policy) to protect against the slippage cost if they are liquidated. Instead of the liquidator executing an immediate sale (which might involve slippage), the insurance pool covers the cost, improving the liquidated borrower's outcome.

## Smart contract implementation

At the smart contract level, the collateral ratio is enforced by the protocol code. Before a user can borrow, the code checks: "Is (collateral_value / debt_value) >= minimum_ratio?" If not, the transaction reverts and the borrow is denied. Similarly, when anyone calls the liquidation function, the code verifies the ratio is indeed below the minimum before executing the liquidation.

<div class="wiki-seealso">

### Closely related
- [Overcollateralization](/wiki/overcollateralization/) — The principle underlying DeFi collateral requirements
- [Liquidation](/wiki/liquidation/) — The forced sale of collateral
- [Stablecoin](/wiki/stablecoin/) — The typical borrowed asset in DeFi
- [Flash Loan](/wiki/flash-loan/) — A DeFi primitive that exploits collateral ratios for arbitrage

### Wider context
- [DeFi Composability](/wiki/defi-composability/) — How lending protocols interconnect
- [Ethereum](/wiki/ethereum/) — The blockchain where most DeFi collateral lives
- [Decentralized Exchange](/wiki/decentralized-exchange/) — Where collateral can be liquidated into stablecoins
- [Smart Contracts](/wiki/blockchain-fundamentals/) — The code implementing collateral and liquidation mechanics

</div>

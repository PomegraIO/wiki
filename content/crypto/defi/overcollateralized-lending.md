---
title: "Overcollateralized Lending"
description: "DeFi lending mechanism where borrowers must deposit collateral worth more than the loan, protecting the protocol against price volatility."
keywords:
  - overcollateralization
  - collateral ratio
  - defi lending
  - liquidation threshold
  - health factor
  - loan-to-value
image: "/svg/crypto.svg"
---

*In **overcollateralized lending**, a borrower deposits cryptocurrency collateral worth significantly more than the amount they wish to borrow—typically 150–200% of the loan value—ensuring the protocol remains solvent even if collateral prices fall sharply.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Overcollateralized Lending — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the cryptocurrency and decentralized finance topic." />

<div class="wiki-infobox-caption">The foundational safety mechanism that allows peer-to-smart-contract lending without underwriting.</div>

|   |   |
|---|---|
| **What it is** | Loan secured by collateral worth more than the principal borrowed |
| **Also called** | Collateralized lending, crypto lending |
| **Minimum ratio** | Typically 150–200% (depends on collateral type) |
| **Key metric** | Loan-to-value (LTV) or equivalently health factor |
| **Triggers liquidation** | When collateral value drops below required ratio |
| **Why required** | Blockchains cannot assess creditworthiness; collateral is the only guarantee |

</aside>

## The fundamental problem

Traditional lending relies on trust and underwriting. A bank evaluates a borrower's income, credit history, and employment to estimate repayment capacity, then extends credit at rates reflecting the assessed risk. On a blockchain, borrowers are pseudonymous, immutable, and legally unreachable. There is no credit bureau, no court system to enforce repayment, no job to garnish. If a smart contract lends ETH to an address and the borrower walks away, the lender has no recourse.

Overcollateralization solves this by removing the need for trust: the collateral is sufficient compensation regardless of the borrower's intent or ability. If a borrower deposits $2,000 worth of ETH as collateral and borrows $1,000 worth of stablecoins, the protocol is protected. Even if the ETH price drops 40%, the collateral ($1,200) still exceeds the loan ($1,000), and the borrower has an incentive to repay and recover their collateral. If they don't, the protocol seizes the collateral, sells it, and repays itself.

## Why borrowers accept the cost

Borrowing against collateral seems irrational on the surface—why not just sell the asset? The answer is that borrowers often seek leverage or liquidity without triggering a taxable event. A holder who believes Ethereum will appreciate 50% over the next two years can borrow stablecoins against their ETH, deploy those stablecoins in yield strategies, and pocket the spread. If yields exceed the borrow rate, the borrower profits even if Ethereum price is flat. Alternatively, a borrower may need short-term liquidity (for business operations or a down payment) but want to maintain long-term exposure to their assets—a loan avoids forced liquidation.

The overcollateralization requirement is the price of this flexibility. Most borrowers accept 150–200% ratios because the alternative—selling their assets outright—forfeits all upside.

## Collateral tiers and risk weights

Not all cryptocurrencies are equally safe to hold as collateral. A lending protocol faces two risks: price volatility (rapid collapse in value) and [counterparty risk](/counterparty-risk/) (the collateral token itself becomes worthless due to protocol failure or fraud). Protocols therefore assign risk weights or loan-to-value caps to different collateral types.

Major, liquid tokens (ETH, Bitcoin) might allow up to 75–80% LTV; mid-cap tokens might be capped at 40–50%; smaller or newer tokens might be allowed only 10–20% LTV or excluded entirely. Stablecoins backed by on-chain reserves (like USDC) often receive 80–90% LTV because price volatility is minimal. The protocol thus takes on more price risk (by allowing higher leverage) for stable, proven assets and less for speculative ones.

This tiering creates an implicit incentive structure: borrowers who collateralize with larger, established tokens face lower borrowing costs (because the protocol is willing to lend more per dollar of collateral) and can borrow more cheaply.

## Health factor and liquidation threshold

As collateral prices move, a borrower's safety margin erodes or improves. Protocols track this via a **health factor**: the ratio of collateral value to borrowed amount, adjusted for risk weights. A health factor of 2.0 means collateral is worth twice the loan; a health factor of 1.2 means it's only 20% above the loan value.

Each collateral type has a **liquidation threshold**—the health factor below which the protocol will seize the collateral. Typical thresholds are 1.3 to 1.5, meaning liquidation triggers when collateral drops to 30–50% above the loan. Once liquidation is triggered, the collateral is seized and auctioned, with the proceeds used to repay the loan. Any surplus goes back to the borrower.

The gap between maximum LTV and liquidation threshold is the **safety buffer**. If maximum LTV is 75% and liquidation threshold is 80%, the buffer is only 5%, meaning a small price movement can trigger liquidation. If maximum LTV is 50% and liquidation threshold is 75%, the buffer is 25%, making liquidation less likely but also restricting how much a borrower can lend.

## Real-world example

Suppose a borrower deposits 10 ETH (worth $30,000 at $3,000 per coin) and borrows $20,000 USDC. Health factor is ($30,000) / ($20,000) = 1.5. If the liquidation threshold is 1.2, the borrower is safe for now. But if ETH falls to $2,400 per coin, the collateral is worth $24,000, and health factor drops to 1.2—the liquidation threshold. At that point, the protocol seizes the 10 ETH, sells it for approximately $24,000, repays the $20,000 loan, and returns the $4,000 surplus to the borrower.

The borrower lost the price move (from $3,000 to $2,400) plus any costs incurred during liquidation. This creates a powerful incentive to repay before liquidation, and to maintain a comfortable buffer if the collateral is volatile.

## Interest rates and borrowing costs

DeFi lending protocols charge interest (called "borrow rates") on outstanding loans, typically ranging from 2–10% annually for stablecoins backed by liquid collateral, up to 20–50% for smaller or riskier tokens. These rates are set dynamically based on supply and demand: if deposits are scarce relative to borrowing demand, rates rise; if deposits are plentiful, rates fall. This market-driven approach contrasts with traditional banking, where rates are set by the lender and are sticky.

Interest accrues constantly and is paid by either the borrower executing a transaction to repay interest, or by the protocol auto-compounding interest into the debt (making the loan larger over time, which increases liquidation risk).

## Governance and risk management

Protocols governed by a decentralized token holder community ("governance tokens") can vote to adjust risk parameters: LTV caps, liquidation thresholds, and interest rate slopes. This is both a strength and a weakness. On one hand, governance is flexible and responsive to market conditions. On the other, governance attacks (where a large token holder influences decisions in their favor) or simple bad judgment can cause cascading risk. Some protocols have introduced "risk committees"—a smaller group of experts with decision-making power—to avoid populist votes that could destabilize the system.

The safest protocols maintain conservative parameters that erode slowly, even as the community lobbies for higher leverage.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidation Mechanism](/liquidation-mechanism/) — how collateral is seized and auctioned
- [CDP Stablecoin](/cdp-stablecoin/) — a stablecoin minted against over-collateral with built-in stability fees
- [Yield Aggregator](/yield-aggregator/) — protocols that optimize returns from lending pools
- [Distributed Ledger](/distributed-ledger/) — the blockchain infrastructure enabling these protocols
- [Counterparty Risk](/counterparty-risk/) — the risk that collateral or a borrowing protocol fails

### Wider context

- [Leverage Ratio Forex](/leverage-ratio-forex/) — analogous concept in foreign-exchange trading
- [Credit Risk](/credit-risk/) — traditional equivalent in conventional lending
- [Interest Rate](/interest-rate/) — the cost of borrowing across all financial systems

</div>

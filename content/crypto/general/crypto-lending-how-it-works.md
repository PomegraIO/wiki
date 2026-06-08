---
title: "Crypto Lending: How It Works"
description: "How cryptocurrency borrowers post collateral and lenders earn yield through centralized platforms and decentralized protocols."
keywords:
  - how does crypto lending work
  - cryptocurrency lending platforms
  - defi lending protocols
  - collateralized loans crypto
  - yield farming lending
---

*Crypto lending mirrors traditional lending: a borrower posts collateral, a lender provides funds, and the borrower pays interest. **Crypto lending** happens on centralized platforms (Celsius, BlockFi) and decentralized protocols (Aave, Compound), where lenders earn yield on idle cryptocurrencies and borrowers take loans against their holdings without selling them—but without the regulatory safety net of banking.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Lending — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Collateral overcoverage and liquidation risk define the market.</div>

|   |   |
|---|---|
| **Collateral requirement** | Typically 150%–250% of loan amount (varies by asset) |
| **Interest for borrowers** | 5%–15% annualized (varies by collateral and demand) |
| **Yield for lenders** | 3%–12% annualized (varies by platform and market conditions) |
| **Liquidation threshold** | Triggered when collateral value falls below loan + interest + penalties |
| **Platform types** | Centralized custodians or decentralized smart contracts |
| **Counterparty risk** | High on centralized platforms; [smart contract risk](/blockchain-fundamentals/) on decentralized ones |

</aside>

## The Basic Mechanics

A **crypto loan** works like this: you have 10 Bitcoin but want access to cash without selling. You deposit the Bitcoin as collateral into a lending protocol or centralized platform. The platform locks it, and lends you stablecoins or fiat (usually on centralized platforms) or other cryptoassets (on decentralized platforms) worth 40 to 70% of your collateral's value.

You pay interest on the borrowed amount, typically monthly or continuously compounded. When you repay the loan plus accrued interest, your Bitcoin is unlocked and returned. If you default or the loan becomes undercollateralized, the platform liquidates your Bitcoin to recover what you owe.

The rate you pay depends on market demand. If many borrowers want loans and few lenders want to provide capital, rates climb. If the opposite is true, rates fall. Supply and demand determine all prices in crypto lending.

## Centralized Lending Platforms

Centralized platforms (formerly Celsius, BlockFi, Genesis Global Capital) operate more like traditional brokers. You transfer cryptocurrency to them as collateral. They take custody and manage the collateral. You receive a loan in stablecoins or dollars (sometimes via wire transfer).

**How they make money**: The platform lends your Bitcoin to other borrowers (or trades it, or lends it to institutions) at a higher interest rate than they pay you. The spread is their profit. They also charge origination fees on loans and may charge account fees.

**Risks**: The platform holds your collateral and your borrowed funds. If the platform goes bankrupt, becomes insolvent, or is hacked, your assets are at risk. Centralized platforms offer convenience (easy fiat on/off ramps, simpler interfaces) but concentrate risk in one entity. None of these platforms are [FDIC](/federal-deposit-insurance-corporation/)-insured, so deposits are unsecured. In 2022 and 2023, Celsius, Voyager Digital, and BlockFi all filed for bankruptcy, leaving lenders with losses or lengthy recovery processes.

**Interest rates**: Centralized platforms typically pay lenders 5–12% annualized on deposits, and charge borrowers 8–15% annualized. This gap funds the operation and risk premium.

## Decentralized Lending Protocols

Decentralized finance (DeFi) protocols like Aave, Compound, and Curve do not hold custody. Instead, smart contracts hold collateral and manage lending algorithmically. Users deposit cryptocurrency directly into smart contracts and receive tokens (cTokens, aTokens) representing their share of a lending pool. When borrowers borrow against collateral, the interest accrued flows to lenders proportionally.

**How the mechanism works**: Suppose you deposit 1 Ethereum into Aave's lending pool. Aave issues you 1 aETH (a receipt token). As borrowers take loans and pay interest, the exchange rate between aETH and ETH increases. Your aETH represents a growing claim on the underlying pool. You can redeem aETH for more ETH than you put in (the difference is your accrued yield).

**Interest rate models**: DeFi protocols use algorithmic interest rates that respond to utilization. If 80% of the Ethereum in the pool is borrowed, rates climb to incentivize deposits. If only 20% is borrowed, rates fall. This keeps supply and demand balanced without human intervention.

**Risks**: Smart contract bugs, exploits, or unforeseen economic attacks can drain the protocol. Aave and Compound have experienced flash loan attacks; Curve has suffered impermanent loss. Yet DeFi protocols are transparent—anyone can audit the code, and transactions are visible on chain. There is no counterparty who can misappropriate your funds; the rules are enforced by code.

**Yields**: Aave and Compound lenders earn 2–10% annualized, depending on asset and market conditions. Borrowers pay 5–20% annualized, with a wider spread to cover [operational risk](/operational-risk/) and compensate lenders for smart contract risk.

## Collateral and Liquidation

All crypto lending requires overcollateralization. If you borrow $50,000, you must post $75,000 to $150,000 in collateral, depending on the platform and the asset. This buffer protects the lender against price drops.

If your collateral value falls, you edge toward **liquidation**. A liquidation threshold is a ratio—say, "loan cannot exceed 75% of collateral value." If your collateral is worth $100,000 and you have borrowed $75,000, you are at the threshold. If the collateral price drops to $98,000, your collateral is now only 75.6% of the loan, and the protocol liquidates some of your collateral to bring the ratio back into compliance.

Liquidation is a forced sale of your collateral, often at a discount (a liquidation penalty). Lenders or protocol arbitrageurs buy the collateral at a discount as compensation for handling the liquidation. You lose both the collateral sold and the profit opportunity if the price later rises.

On Aave, liquidation penalties are typically 5–10%. On Compound, they are similar. The penalty exists because the liquidator incurs gas costs and takes on temporary exposure; the discount compensates them.

## Interest Bearing Deposits vs. Lending Pools

A subtle distinction: you can deposit cryptocurrency into a centralized platform and earn interest without borrowing (a pure savings account). These deposits fund loans made to borrowers and are treated as unsecured debt to the platform. You are a creditor, not a collateral provider.

On decentralized protocols, you deposit into a lending pool and receive a token that represents your share. You are not lending to anyone in particular; you are providing liquidity to a pool. The pool operates like a market, matching supply and demand algorithmically.

Both expose you to risk: centralized deposits carry counterparty risk (the platform's solvency); decentralized deposits carry smart contract risk and market risk (if interest rates swing, your yield may fall).

## Staking and Yield Farming

Crypto lending is often bundled with [yield farming](/yield-farming/) or staking. On decentralized protocols, you may earn additional governance tokens (COMP, AAVE) alongside interest, boosting total yields. On centralized platforms, you might earn a higher rate on illiquid lockups (e.g., 10% annualized if you promise not to withdraw for one year).

These extra incentives are marketing and market-share grabs. The underlying economics—collateral, liquidation, and interest—remain unchanged.

## Regulatory Status

Crypto lending sits in a grey zone. The SEC has not classified lending platforms as broker-dealers or investment advisors, but regulators have warned that they may do so. Some countries (Singapore, El Salvador) have granted licenses to centralized platforms. Others (the US, EU) have indicated future oversight. DeFi protocols, being code without corporate entity, are harder to regulate—but regulators have begun enforcement against the humans running them.

As of 2025, centralized platforms have largely exited the US retail market, while DeFi protocols continue to operate globally with regulatory uncertainty. Bankruptcy law and deposit insurance remain unsettled.

## See also

<div class="wiki-seealso">

### Closely related

- [Mempool Explained](/mempool-explained/) — understanding transaction fees and pool economics
- [Smart Contracts](/blockchain-fundamentals/) — how decentralized protocols execute lending rules
- [Proof-of-Stake](/proof-of-stake/) — staking as an alternative to collateralized lending
- [Yield Farming](/yield-farming/) — earning rewards by providing liquidity to protocols
- [Interest Rate](/interest-rate/) — the economics of lending rates across traditional and crypto markets

### Wider context

- [Cost of Debt](/cost-of-debt/) — comparing borrowing costs across asset classes
- [Operational Risk](/operational-risk/) — how platform failures affect borrowers and lenders
- [Federal Deposit Insurance Corporation](/federal-deposit-insurance-corporation/) — regulatory contrast with crypto lending

</div>
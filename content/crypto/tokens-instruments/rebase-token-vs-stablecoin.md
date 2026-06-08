---
title: "Rebase Token vs Stablecoin"
description: "Compare elastic-supply rebase tokens that adjust wallet balances algorithmically with stablecoins that peg via reserve or collateral backing."
keywords:
  - rebase token vs stablecoin
  - elastic supply token rebase
  - stablecoin peg mechanism
  - rebase coin explained
image: /svg/crypto.svg
---

*A **rebase token** adjusts the quantity of coins in every wallet proportionally to move price toward a target (usually $1), while a **stablecoin** holds price steady through reserve backing or collateral. Rebase tokens use supply expansion or contraction as the mechanism; stablecoins rely on external assets or arbitrage. Both claim to solve price stability, but via entirely different economic models.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rebase Token vs Stablecoin — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and tokens." />

<div class="wiki-infobox-caption">Two competing approaches to achieving a stable price target.</div>

|   |   |
|---|---|
| **Rebase mechanism** | Proportional adjustment to all wallet balances; your token count changes, price target approached via supply change |
| **Stablecoin mechanism** | Collateral reserve (USD-backed) or algorithm (algorithmic stable) that maintains peg through arbitrage |
| **Which adjusts?** | Rebase: quantity in wallet. Stablecoin: price via external backing or market forces |
| **Failure mode (rebase)** | Supply spirals; arbitrage disappears; peg collapses and rebasing can't recover it |
| **Failure mode (stablecoin)** | Reserve depleted or discovered fraudulent; redemption halts; peg breaks |
| **Tax or "haircut" risk** | Rebase: every adjustment dilutes; stablecoin: holder dilution only if reserve fails |
| **Ideal use case** | Rebase: none proven; stablecoin: USD-on-chain, DeFi pricing, trading pairs |

</aside>

## How a Rebase Token Works

A rebase token uses a smart contract to adjust all balances across the network every N blocks or when a certain condition triggers (e.g., daily). The protocol observes the token's market price. If it trades above $1, the contract increases all wallet balances proportionally, expanding supply. If it trades below $1, the contract decreases all balances, shrinking supply.

**Example:** A rebase token called REBASE trades at $1.10. The protocol resets at midnight UTC. Every holder's balance is multiplied by 1.10, so if you owned 1,000 REBASE, you now own 1,100 REBASE. Simultaneously, the market price is expected to fall toward $1 because there are now many more tokens in circulation competing for the same total value.

The theory is elegant: supply adjusts automatically to meet demand without external intervention. In practice, rebasing only works if the market believes the peg will hold. The moment confidence breaks—if price drops and stays low—rebasing becomes a negative spiral. Holders see their balance shrink (negative rebase) and panic-sell, driving price lower. Rebasing can't reverse this; it only accelerates the collapse.

## How a Stablecoin Holds Its Peg

Stablecoins use external backing to defend $1. There are two main designs:

**Collateralized stablecoins** (USDC, USDT, BUSD): A reserve of USD, short-term Treasury bonds, or bank deposits sits in a custodian account. The issuer mints new stablecoins only when USD is deposited; they burn stablecoins only when USD is withdrawn. Price stays at $1 because redemption at par (1 USDC = $1 USD cash) is always available.

**Algorithmic or hybrid stablecoins** (less common; USDA, alUSD): A protocol issues stablecoins backed by collateral (e.g., ETH or other crypto) held in smart contracts. If the collateral's value falls below a threshold, the protocol triggers liquidation to recapitalize. Stablecoins trade at $1 because redemption is algorithmic; if price drifts, arbitrage brings it back.

Crucially, stablecoins work because someone—either a trusted entity (USDC issuer) or a smart contract (algorithmic)—guarantees the redemption. This anchors price.

## Why Rebase Tokens Fail in Practice

Rebase tokens have failed consistently. Examples include Ampleforth (AMPL), which launched in 2019 with the promise of a fully decentralized stable asset via rebasing. It never held its peg. Price swung wildly; holders watched their balances dilute or concentrate unpredictably. AMPL became a volatility play, not a stablecoin.

The core flaw: rebasing assumes that if you increase supply, price will fall. But price is set by market sentiment and liquidity, not by token count alone. If traders believe the peg is broken and no redemption is coming, they'll sell regardless of a positive rebase. The mechanism is retroactive—it tries to fix price after the fact, not prevent the divergence.

Another issue: rebasing penalizes patient holders. Even if the peg holds, every positive rebase is seen as dilution by the market (more tokens means lower price per token, even if your balance grew). Long-term holders often exit rather than endure constant balance churn.

## Risk Profiles

**Rebase token risk:** Unpredictable balance changes, no floor price, prone to collapse once peg breaks. Ideal for speculation, not holding.

**Collateralized stablecoin risk:** Issuer fraud, reserve misuse, or regulatory action could cause redemption to fail. Happens rarely because these are tightly regulated (USDC, USDT). Risk is low for major stablecoins; higher for smaller ones.

**Algorithmic stablecoin risk:** Liquidation cascades if collateral crashes (e.g., a crypto market crash collateralizing billions of stablecoins). Happened to Terra/Luna in 2022, when collateral reserves proved insufficient.

## When to Use Each

**Stablecoin:** Any time you want price stability and on-chain USD access. Trading pairs, loans, savings, purchasing power preservation. Dominant use case in DeFi and crypto payments.

**Rebase token:** No compelling use case proven. Some projects use rebasing as a gimmick to attract traders seeking volatility or novelty. Not suitable for actual store of value or payment.

A stablecoin succeeds because it solves a real problem (crypto-to-fiat bridge). A rebase token doesn't solve anything that a plain stablecoin or [bond](/bond/) doesn't already solve better.

## The Economics of Confidence

Both mechanisms depend on market confidence, but differently:

- **Rebase:** Confidence means traders believe the peg will hold even if supply changes. Breaks when traders lose faith that the algorithm can defend $1. Failure is often sudden.

- **Stablecoin:** Confidence means users believe the issuer or protocol is solvent and redemption will work. Breaks when reserve is exposed as fraudulent or depleted. Failure is often preceded by visible warning signs (reserve audits, issuer distress).

Stablecoins have a trust anchor (issuer reputation, regulatory oversight, verifiable reserve). Rebase tokens have only the math, which isn't enough.

## See also

<div class="wiki-seealso">

### Closely related

- [Stablecoin](/stablecoin/) — detailed mechanics of collateralized and algorithmic stablecoins
- USD Coin — leading example of a reserve-backed stablecoin
- Tether — most-used stablecoin; illustrates reserve backing debates
- [LP Token Impermanent Loss](/lp-token-impermanent-loss/) — rebase tokens often appear in AMM liquidity pools, exposing LPs to volatility
- [Token Emission Schedule](/token-emission-schedule/) — some protocols use emission to manage price, similar motivation to rebasing

### Wider context

- Cryptocurrency — broader assets and their use cases
- Volatility — why price stability is valuable in crypto
- Monetary Policy — how decentralized systems try to manage money supply
- Terra and Luna Collapse — case study of algorithmic stablecoin failure

</div>

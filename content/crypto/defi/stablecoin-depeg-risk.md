---
title: "Stablecoin Depeg Risk"
description: "The mechanisms and market conditions under which collateralized or algorithmic stablecoins lose their fixed dollar peg, and the cascade effects across DeFi."
keywords:
  - stablecoin depeg
  - peg risk
  - collateralized stablecoin
  - algorithmic stablecoin
  - defi contagion
image: "/svg/crypto.svg"
---

*A **stablecoin depeg** occurs when a stablecoin's market price deviates materially from its intended peg—typically $1.00. Both collateralized stablecoins (backed by USD or other assets) and algorithmic stablecoins (stabilized by mechanism alone) can depeg under stress, unleashing contagion across DeFi and harming users who treated the asset as riskless.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stablecoin Depeg Risk — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and decentralized finance." />

<div class="wiki-infobox-caption">When the safe asset becomes unsafe overnight.</div>

|   |   |
|---|---|
| **What it is** | Loss of peg by a stablecoin designed to trade at $1.00 |
| **Collateralized risk** | Bank failure, asset fire sales, redemption runs |
| **Algorithmic risk** | Feedback loops, death spirals, incentive failure |
| **Cascade risk** | Contagion across [money market protocols](/money-market-protocol/) and [yield farming](/yield-farming/) strategies |
| **Historical examples** | USDC (2023, brief), Terra Luna (2022, extreme), UST (algorithmic) |
| **Mitigation** | Over-collateralization, diversified backing assets, governance safeguards |

</aside>

## Collateralized stablecoins and bank runs

The simplest stablecoins—USDC, USDT, and others—promise to hold $1 of backing (cash, bank deposits, short-term Treasury securities) for each stablecoin issued. If the promise is credible, the stablecoin trades at par. Its depeg risk mirrors that of the issuer's backing: if the issuer's bank is compromised, or if backing assets decline in value, redemptions accelerate and the stablecoin's value falls.

USDC's March 2023 brief peg instability illustrates this: Silicon Valley Bank, a major holder of USDC backing assets, failed, and market participants feared USDC's collateral was trapped or unrecoverable. The price fell briefly to $0.87 before Silvergate and Circle (the USDC issuer) announced a guarantee against losses. Trust returned, and the peg recovered. But the episode revealed a hard truth: a collateralized stablecoin's peg depends entirely on the solvency and liquidity of its backer.

For stablecoins backed by diverse Treasury securities or stable bank deposits spread across multiple jurisdictions, depeg risk is low but nonzero. For stablecoins backed by a single bank or risky assets, depeg is a material tail risk. USDT, issued by Tether and backed opaquely by a mix of cash and commercial paper, has depegged multiple times when market participants doubted the backing.

## Over-collateralization and recursive depegs

Crypto-collateralized stablecoins like DAI (backed by Ethereum and other crypto) use *over-collateralization*: a user deposits $2 of ETH to mint $1 of DAI. If ETH falls 30%, the collateral is still ample. If it falls 50%, the position becomes underwater, and liquidators seize collateral to cover the debt.

During sustained downturns, over-collateralized stablecoins face a perverse dynamic: users rush to withdraw, collateral is liquidated, and asset sales push prices down further. If collateral assets are themselves stablecoins (nested over-collateralization), a failure in one cascades to others. During the 2022 collapse of Terra's Luna and UST ecosystem, DAI fell to $0.91 as liquidations accelerated and confidence in the collateral pool deteriorated.

Over-collateralization mitigates but does not eliminate depeg risk; under extreme volatility, liquidations may not keep pace with price declines.

## Algorithmic stablecoins and death spirals

Algorithmic stablecoins like Terra's UST attempted to maintain a dollar peg using only incentives and feedback loops, with no collateral backing. The mechanism varied, but the core idea: if UST trades below $1, arbitrageurs can burn 1 UST for $1 of Luna (the protocol's native token), profiting from the spread—thus pushing UST price up. If UST trades above $1, arbitrageurs can mint 1 UST by depositing $1 of Luna, profiting on the upside—pushing UST down.

In principle, these mechanisms keep UST at par. In practice, they depend on Luna's price stability and on perpetual market confidence that the arbitrage will work. When confidence breaks—say, a large Luna holder sells, causing Luna's price to collapse—the arbitrage model fails. UST collapses, Luna collapses in tandem, and the stablecoin unwinds catastrophically. This is the death spiral: as UST loses value, Luna must appreciate to maintain the arbitrage, but Luna's value is intrinsically tied to UST's success. Both assets converge toward zero.

Most major protocols have abandoned purely algorithmic models in favor of hybrid designs (some collateral, some algorithmic mechanisms). But death-spiral risk remains a concern for any stablecoin lacking sufficient hard-asset backing.

## Cascade effects across DeFi

Stablecoin depegs create contagion because stablecoins underpin DeFi's credit system. A [money market protocol](/money-market-protocol/) accepting USDC as collateral for borrowing must reprice risk if USDC deppegs. If USDC is worth $0.90, a $1 million deposit is now worth only $900,000, and previously-safe loan-to-value ratios become unsafe. Borrowers face unexpected liquidations; [money market protocols](/money-market-protocol/) suffer collateral shortfalls and insolvency.

Yield farmers using depegged stablecoins in leverage strategies suffer amplified losses. A farmer borrowing USDC at 5% APY to earn 8% yield on a USDC-ETH pool expects 3% net return; if USDC deppegs 10%, the farmer loses 10% plus financing costs, regardless of yield.

Stablecoin depeg risk thus propagates: a single stablecoin's failure to maintain peg can trigger liquidation cascades, liquidity drains, and systemic losses across multiple protocols and strategies. The interconnection of DeFi means there is no true isolation; risk in one corner eventually leaks into others.

## Structural mitigation and governance

Sophisticated protocols now impose limits on stablecoin exposures and enforce minimum capital ratios. Some protocols (e.g., Maker for DAI) have governance safeguards: if collateral ratios fall below thresholds, emergency parameters can be activated to prevent further minting and force liquidations. Others diversify collateral aggressively, reducing reliance on any single stablecoin.

Professional stablecoin issuers publish attestations of backing assets, submit to audits, and build redundancy into their backing infrastructure. Yet audits and attestations lag reality; market participants must weigh public claims against incentives to deceive and the historical track record of the issuer.

## The future: stability without risk?

The stablecoin landscape has matured toward two poles: heavily collateralized, transparently audited stablecoins (USDC, USDT alternatives) backed by fiat and Treasury securities, and emerging central-bank digital currencies (CBDCs), which would eliminate depeg risk by definition (they are central-bank liabilities). Algorithmic designs persist in niche applications but have lost mainstream credibility after UST and others.

Depeg risk will remain a staple of DeFi as long as stablecoins depend on collateral quality or market confidence in mechanisms. It is a tail risk for most users of mature stablecoins, but a material risk for those exposed to newer, less-capitalized, or purely algorithmic designs.

## See also

<div class="wiki-seealso">

### Closely related

- [Stablecoin](/stablecoin/) — definition and types
- Collateral — assets backing crypto-collateralized stablecoins
- [Money Market Protocol](/money-market-protocol/) — DeFi systems most exposed to depeg cascades
- [Liquidation](/liquidation/) — forced position closures triggered by depegs
- Terra Luna Collapse — historical case study of algorithmic depeg
- Bank Run — mechanism analogous to stablecoin redemption cascades

### Wider context

- Decentralized Finance — ecosystem contagion paths
- Solvency — financial stability of stablecoin issuers
- Peg — fixed-price promise
- [Monetary Policy](/monetary-policy/) — comparison to fiat currency stability mechanisms

</div>

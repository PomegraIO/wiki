---
title: "Algorithmic Stablecoins"
description: "Non-collateralized stablecoins that maintain peg through algorithm-based supply adjustments rather than collateral reserves."
keywords:
  - algorithmic stablecoins
  - non-collateralized stablecoins
  - dynamic supply adjustment
  - peg stability
---

*Algorithmic stablecoins are cryptocurrencies designed to maintain a target price (typically $1 USD) through algorithm-driven supply adjustments rather than collateral backing. They expand and contract the money supply in response to price deviations, using mechanisms that aim to push the asset back toward its peg.*

An algorithmic stablecoin operates without the vault of collateral that [collateralized-debt-obligation](/wiki/collateralized-debt-obligation/) systems or [asset-backed-security](/wiki/asset-backed-security/) frameworks require. Instead, the protocol itself acts as a stabilizer. When the token trades above $1, the algorithm mints new tokens to increase supply and push price down. When it falls below $1, the algorithm reduces supply (or creates incentives to burn tokens) to create scarcity and push price up. This mirrors central bank [monetary-policy](/wiki/monetary-policy/) mechanics but compressed into code.

<div class="wiki-hatnote">For other stablecoin designs, see [stablecoin](/wiki/stablecoin/). For collateral-based alternatives, see [collateralized-debt-obligation](/wiki/collateralized-debt-obligation/).</div>

<aside class="wiki-infobox">

| Attribute | Detail |
|-----------|--------|
| **Collateral** | Zero or minimal |
| **Stability mechanism** | Supply elasticity + incentives |
| **Price discovery** | Open market trading + arbitrage |
| **Risk profile** | High; depends entirely on design quality |
| **Historical examples** | LUNA/TerraUSD, Ampleforth |
| **Regulatory status** | Evolving; mostly unregulated |

</aside>

## Why zero-collateral design appeals to builders

Traditional [collateralized-loan-obligation](/wiki/collateralized-loan-obligation/) and over-collateralized systems lock up large amounts of capital as reserves. A maker who wants to issue $100 million stablecoins must hold $150 million+ in collateral, taking losses on [opportunity-cost](/wiki/cost-of-carry/). Algorithmic designs promise capital efficiency: issue a stablecoin without tying up vaults, using only code.

This efficiency appeal drove rapid adoption of projects like TerraUSD (UST), which paired an algorithmic stablecoin with a yield-farming governance token (LUNA) to incentivize holders. The model exploded in value, reaching $40 billion in UST market cap by early 2022—then collapsed catastrophically when the peg broke and incentive structures unraveled.

## The supply adjustment mechanism

The most straightforward algorithmic approach uses [automated-market-maker](/wiki/automated-market-maker/) mechanics or oracle-price feedback. When the stablecoin price rises above peg:

1. The protocol mints new tokens.
2. Minters receive a slight premium (e.g., $1.01 worth of new tokens for $1 in collateral if any, or a governance token reward).
3. Fresh supply floods the market, pulling price down.

When price falls below peg:

1. The protocol offers incentives to remove tokens from circulation (burning or locking).
2. Holders who burn tokens receive a discount purchase (e.g., buy governance tokens at a 5% discount) or direct reward.
3. Reduced supply creates scarcity, pushing price back up.

This is devilishly simple in theory. In practice, it requires constant arbitrage and an audience willing to participate in the incentive loop. If price drops and holders don't believe recovery is imminent, the incentive to burn evaporates, the peg breaks further, and confidence collapses—triggering a death spiral.

## The collateral reserve spectrum

"Non-collateralized" is a spectrum. Some protocols hold *some* collateral (often governance token reserves or cryptocurrency holdings) but far less than 100%. This is a [fractional-reserve-banking](/wiki/fractional-reserve-banking/) model applied to crypto. It reduces pure algorithmic risk but still relies on the supply adjustment mechanism if collateral reserves are insufficient during a prolonged peg break.

Other designs use a hybrid: partial collateral (e.g., 20% cash/crypto reserves) plus algorithmic supply adjustment. This blends safety and capital efficiency.

## Historical precedent in fiat

Algorithmic stablecoins invoke the gold standard and [bretton-woods](/wiki/bretton-woods/) thinking. Under the gold standard, central banks didn't manually adjust the money supply; the price of gold itself (and trade deficits) adjusted supply mechanically. The analogy breaks down because gold's [supply-demand](/wiki/asset-backed-security/) is driven by mining and industrial demand, not algorithmic code, but the conceptual appeal is the same: a rule-based, non-discretionary process that resists political interference.

## Failure modes

The fundamental challenge is that an algorithmic stablecoin's stability depends on participant psychology, not physics. The LUNA/UST collapse in May 2022 is the canonical case study:

- UST lost its peg because [luna](/wiki/ethereum/) (the governance token) collapsed, removing the financial incentive to arbitrage.
- As the peg broke, panic selling accelerated the collapse.
- The mechanism that was supposed to stabilize price—minting more tokens—only worsened the death spiral because trust in the system had evaporated.

The core issue: **an algorithm cannot force people to participate.** If belief in the system vanishes, no amount of new tokens or incentives can restore it. This is why algorithmic stablecoins are considered extremely risky and why regulators in many jurisdictions now restrict or ban their issuance.

## The game theory problem

Algorithmic stables require a coordination game where everyone believes everyone else will help defend the peg. Game theory shows this equilibrium is fragile. If even a significant minority of holders suspect the peg will break, they have incentive to exit immediately—which triggers the death spiral. The system is stable only as long as confidence is unanimous.

Collateralized stablecoins, by contrast, have a fallback: you can redeem your stablecoin for the underlying collateral. This creates a floor price and a reason to hold even if confidence momentarily wavers.

## Practical use cases

Despite the risks, algorithmic stablecoins persist:

- **High [inflation-targeting](/wiki/inflation-targeting/) cryptocurrencies** in countries with unstable national [currency-peg](/wiki/currency-peg/) policies may issue algorithmic stables to allow citizens to hold USD-pegged assets without full collateralization.
- **Protocol incentives.** Some chains use algorithmic adjustments to token supply for [monetary-policy-transmission](/wiki/monetary-policy-transmission/) (e.g., dynamically adjusting [staking](/wiki/staking/) rewards to keep token price stable).
- **Yield farming.** The incentive layer built into many algorithmic designs creates attractive [carry-trade](/wiki/carry-trade/) opportunities, drawing sophisticated participants willing to arbitrage the system.

## Regulatory and practical outlook

Most major crypto jurisdictions now treat algorithmic stablecoins with extreme skepticism. The [dodd-frank-act](/wiki/dodd-frank-act/) and its successors are still defining how stablecoins fit into traditional banking regulation, but the pattern is clear: systems without collateral or credible backing face heavy restrictions.

For a stablecoin to gain regulatory acceptance, it typically needs:
- Meaningful collateral reserves (≥100% for critical systems).
- Explicit redemption rights.
- Clear governance over the algorithm.
- Regular audits and transparency reports.

Algorithmic designs can survive only in niches where regulatory oversight is light and participants accept extreme risk.

---

<div class="wiki-seealso">

### Closely related
- [stablecoin](/wiki/stablecoin/) — Overview of all stablecoin types
- [collateralized-debt-obligation](/wiki/collateralized-debt-obligation/) — Collateral-backed approach
- [automated-market-maker](/wiki/automated-market-maker/) — Underlying mechanics for many algos
- [monetary-policy](/wiki/monetary-policy/) — Supply adjustment precedent in fiat

### Wider context
- [cryptocurrency-bubble-2017](/wiki/cryptocurrency-bubble-2017/) — Regulatory environment and speculation
- [defi-composability](/wiki/defi-composability/) — Ecosystem integration risk
- [euler-like-airdrop](/wiki/token-airdrop/) — Incentive mechanics in crypto

</div>

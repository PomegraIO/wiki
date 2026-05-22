---
title: "Flash Attacks"
description: "Exploiting flash loans to manipulate protocols within a single blockchain transaction."
keywords:
  - flash loan attack
  - defi protocol vulnerability
  - flash loan abuse
  - atomic transaction manipulation
---

*A **flash attack** exploits a [flash loan](/wiki/flash-loan/) to manipulate a [decentralized exchange](/wiki/decentralized-exchange/) or lending protocol within a single atomic transaction, borrowing enormous sums without collateral and repaying in the same block. The attacker profits by moving prices, draining reserves, or exposing arbitrage gaps that exist only during the manipulation.*

<aside class="wiki-infobox">

| Concept | Definition |
|---|---|
| **Attack Surface** | Protocols with price feeds dependent on [liquidity pools](/wiki/liquidity-pools/) |
| **Typical Loan Size** | Millions in stablecoins or tokens borrowed and repaid in seconds |
| **Profit Window** | Single transaction block (~12 seconds on Ethereum) |
| **Vulnerability** | Using [liquidity pool](/wiki/liquidity-pool/) spot prices as [oracle](/wiki/price-discovery/) |
| **Defense** | Time-weighted average prices (TWAP), external oracles, multi-block checks |
| **First Major Attack** | bZx (February 2020, ~$355k profit) |

</aside>

## How flash attacks work: the mechanics

A flash attack unfolds in stages within a single transaction:

1. The attacker calls a flash loan contract, borrowing millions in [stablecoins](/wiki/stablecoin/) or major tokens.
2. Using this capital, they dump the borrowed asset into a [liquidity pool](/wiki/liquidity-pool/), crushing its price temporarily.
3. A victim protocol that relies on that pool's spot price as a price feed now reports a distorted [valuation](/wiki/multiples-valuation/). The attacker exploits this mispricing—perhaps minting synthetic assets at inflated collateral ratios, swapping at favorable rates, or liquidating positions at artificially low prices.
4. The attacker unwinds the dump (or executes a counterrade elsewhere to profit).
5. The loan plus a small [fee](/wiki/transaction-fee-forex/) (0.05–0.09%) is repaid.
6. The transaction either succeeds atomically (all steps happen or none do) or fails and reverts.

The genius of this attack is that it requires **no initial capital**. Traditional market manipulation requires you to hold a position through settlement risk; flash attacks eliminate that by completing in a single block.

## The bZx case: February 2020

The first widely-publicized flash attack targeted bZx, a [margin trading](/wiki/forex-margin/) protocol. The attacker borrowed 7,500 ETH (~$1.5 million), dumped it on [Uniswap](/wiki/decentralized-exchange-mechanics/) to crash prices, and then executed a short position on bZx at the artificially low price. When prices recovered, the short was liquidated in the attacker's favor. The total profit was modest (~$355k), but it exposed a fundamental flaw in any on-chain [oracle](/wiki/price-discovery/) design that didn't account for same-block manipulation.

Following this attack, [DeFi](/wiki/defi-composability/) protocols scrambled to implement time-weighted average prices (TWAP oracles) and other safeguards. Yet vulnerabilities persisted.

## Why protocols remain exposed

Even with TWAP oracles in place, flash attacks succeed against protocols that:

- **Rely on external [liquidity pools](/wiki/liquidity-pools/)** without sanity checks on price movement within a single block
- **Don't isolate collateral from [liquidation](/wiki/liquidation/) calculations** across the same transaction
- **Lack secondary price validation** (e.g., no fallback oracle if the primary one moves >10% in one block)

A sophisticated attacker can exploit [composability](/wiki/defi-composability/)—chaining multiple [swaps](/wiki/decentralized-exchange-mechanics/), loans, and [derivative](/wiki/credit-derivative/) positions to create cascading effects. One 2021 attack on Pancakeswap used flash loans plus a price manipulation to drain over $45 million from liquidity pools.

## Defense layers in modern DeFi

Mature protocols now layer defenses:

1. **TWAP (time-weighted average price):** Average the price over the last N blocks rather than using the spot price. This forces attackers to sustain a dump for multiple blocks, raising costs.
2. **Chainlink / Band Protocol oracle fallbacks:** Use independent, decentralized [price feeds](/wiki/price-discovery/) not dependent on any single [liquidity pool](/wiki/liquidity-pool/).
3. **Sanity checks on single-transaction price moves:** If price moves >5%, delay [liquidation](/wiki/liquidation/) or require manual verification.
4. **Isolated [collateral](/wiki/collateral-ratio/) per-block:** Liquidations triggered in block *N* only affect collateral deposited before block *N−1*.
5. **Flash loan fees:** Many lending protocols (Aave, dYdX) charge 0.05–0.09% on flash loans, raising the cost of large attacks.

## Broader DeFi risk implications

Flash attacks highlight the tension at the heart of [DeFi](/wiki/defi-composability/): instant [settlement finality](/wiki/crypto-settlement-finality/) and permissionless composability create opportunities for sophisticated griefing. Unlike traditional [clearinghouses](/wiki/central-counterparty-clearing/), which settle trades across multiple days and can unwind risky positions, DeFi protocols must assume every actor is potentially adversarial and every [oracle](/wiki/price-discovery/) can be attacked.

This forces developers toward over-collateralization (requiring 150%+ backing) and conservative liquidation thresholds, raising capital costs for legitimate users. Some protocols accept this overhead as the price of decentralization; others argue for [layer-2 protocols](/wiki/state-channel/) or [bridges](/wiki/sidechain-bridge/) that batch transactions and delay finality, reintroducing some settlement lag to reduce atomic-transaction attack surface.

<div class="wiki-seealso">

### Closely related
- [Flash Loan](/wiki/flash-loan/) — Uncollateralized loan that must be repaid in the same transaction
- [Liquidity Pool](/wiki/liquidity-pool/) — Reserve of tokens in a [DEX](/wiki/decentralized-exchange/)
- [DeFi Composability](/wiki/defi-composability/) — Ability to chain DeFi primitives together
- [Decentralized Exchange](/wiki/decentralized-exchange/) — Non-custodial token trading
- [Liquidation](/wiki/liquidation/) — Forced sale of collateral at distressed prices

### Wider context
- [Cryptocurrency Exchange](/wiki/cryptocurrency-exchange/) — Centralized vs. decentralized trading venues
- [Arbitrage DeFi](/wiki/arbitrage-defi/) — Legitimate cross-venue price discrepancy trading
- [DeFi Tax Implications](/wiki/defi-tax-implications/) — Reporting attack gains
- [Smart Contract](/wiki/smart-contract/) — Code that executes flash loan logic
- [Flash Crash 2010](/wiki/flash-crash-2010/) — Traditional markets analog to DeFi manipulation

</div>

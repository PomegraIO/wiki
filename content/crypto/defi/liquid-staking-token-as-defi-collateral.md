---
title: "Liquid Staking Tokens as DeFi Collateral"
description: "How DeFi protocols accept liquid staking tokens like stETH as collateral, the oracle mechanics involved, and de-peg risk for this collateral class."
keywords:
  - liquid staking token as defi collateral
  - steth collateral lending
  - lst de-peg risk
  - liquid staking oracle
  - staking yield collateral
image: "/svg/crypto.svg"
---

*Liquid staking tokens (LSTs) like stETH and rETH are accepted as collateral in DeFi lending protocols because they combine a stable underlying asset with accrued staking yield—allowing borrowers to earn passive returns while maintaining borrowing capacity. However, LSTs carry de-peg risk and oracle dependencies absent from raw volatile assets or stablecoins, creating unique collateral dynamics.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquid Staking as Collateral — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">LSTs offer yield stacking but require collateral-quality oracles and de-peg safeguards.</div>

|   |   |
|---|---|
| **Common LSTs** | stETH (Lido), rETH (Rocket Pool), cbETH (Coinbase), swETH (Swell) |
| **Typical LTV** | 75–85% (higher than ETH ~60%, lower than USDC ~90%) |
| **Borrow rate on LST collateral** | 2–4% APY (vs. 6%+ for volatile assets) |
| **Primary risk** | De-peg from ETH price + accrued rewards |
| **Collateral quality mechanism** | Oracles report LST/ETH ratio; protocols cap LTV below 100% to absorb de-pegs |
| **Liquidation trigger** | LTV falls below protocol threshold (e.g., 85% LTV → liquidate if price drops 20%) |

</aside>

## Why Protocols Accept LSTs as Collateral

Liquid staking tokens represent claims on staked ETH that is actively earning rewards. When you stake ETH directly with Lido, you receive stETH; that stETH accrues rewards at ~3.5% annually, equal to Ethereum's staking APY. Unlike raw ETH collateral, which earns nothing while locked, stETH collateral earns passive yield.

For borrowers, this creates a powerful incentive structure. You can:
1. Post $100k stETH as collateral.
2. Borrow $75k USDC (or another stablecoin) at a lower rate than volatile-asset borrowing (2.5% vs. 6%).
3. Lend that $75k to a yield protocol earning 4%.
4. Pocket the spread (4% − 2.5% = 1.5%) while holding $100k of appreciating, yield-generating collateral.

This "yield stacking" has become a primary driver of LST demand in DeFi. Protocols accept LSTs because they attract capital (borrowers want yield), deepening liquidity and total value locked (TVL).

## LST Oracles and the Reported Exchange Rate

Protocols need oracles to determine collateral value and trigger liquidations. For stETH, the oracle reports the stETH/ETH exchange rate, which encodes two pieces of information: the underlying ETH value plus accumulated staking rewards.

Lido's stETH exchange rate works like this:
- Day 1: You deposit 1 ETH, receive 1 stETH (ratio = 1.0).
- Day 365: Staking earned 3.5% rewards. Your 1 stETH is now worth 1.035 ETH (ratio = 1.035).

The oracle publishes this 1.035 ratio. When a lending protocol values your stETH collateral, it multiplies the balance by the oracle rate: $100k stETH × 1.035 = $103.5k collateral value.

This design is elegant but creates oracle dependencies. If the stETH/ETH oracle fails or reports a stale rate, the collateral valuation becomes inaccurate. Most protocols use multiple oracle sources (Chainlink, direct Lido queries, fallbacks) to mitigate this.

## De-Peg Risk and Haircuts

De-pegging occurs when stETH trades at a discount to its reported exchange rate with ETH. This can happen for several reasons:

1. **Withdrawal queue delays**: Ethereum's staking withdrawal queue processes validators gradually. During periods of high exit demand, users holding stETH might withdraw at a discount to access immediate liquidity.

2. **Staking service distress**: If Lido's node operators fail, the protocol pauses, or reserves deplete, confidence in stETH's backing erodes. In 2022, during the Ethereum Shanghai upgrade, stETH temporarily de-pegged to $0.96 per ETH.

3. **LST ecosystem stress**: If a major LST-dependent protocol (e.g., Curve, Aave) suffers a hack or liquidity crisis, broader LST demand can collapse, pushing all LSTs into de-pegs.

4. **Underlying asset weakness**: A sharp ETH crash can trigger margin calls and forced stETH liquidations, overwhelming buy-side demand and pushing stETH below its fair value.

To absorb de-peg risk, lending protocols set LST LTVs below their theoretical maximum. A stETH worth 1.035 ETH might have a 75% LTV, meaning you can borrow $0.75 per $1.035 of stETH collateral. This 25% buffer is the "haircut," designed to protect lenders if stETH de-pegs by up to 25% without triggering liquidations.

However, large de-pegs (>30%) can overwhelm haircuts. During the March 2023 banking crisis, stETH fell to $0.99 per ETH; borrowers with 75% LTV and tight liquidation thresholds saw forced sales.

## Collateral Tiers and Protocol Risk Management

Most lending protocols use a tiered system for LST collateral:

**Isolated tier**: Some protocols treat individual LSTs in isolation, limiting borrowing and cross-collateral mixing. A borrower must post stETH separately from ETH and cannot pool the two for a combined LTV.

**Standard tier**: stETH and other major LSTs (rETH, cbETH) are accepted at standard LTV (75–85%). They can be mixed with other collateral to some extent.

**Discounted tier**: Niche or newer LSTs get lower LTVs (50–65%) until they prove stable and achieve sufficient liquidity.

This tiering prevents LST concentration from destabilizing the protocol. If all collateral were stETH and stETH crashed, the protocol would face cascading liquidations and insolvency.

## Real-World Example: Yield Stacking Liquidation Scenario

Suppose you:
- Deposit $100,000 stETH at 1.035 ETH/stETH ratio.
- Collateral value = $103,500.
- Borrow $75,000 USDC at 75% LTV.
- Liquidation threshold = 80% (protocol closes positions if LTV exceeds 80%).

**Current position**: $75k borrowed / $103.5k collateral = 72% LTV. Safe.

**Scenario 1 — stETH de-pegs 10%**: Exchange rate falls to 0.935 ETH per stETH.
- New collateral value = $100k × 0.935 = $93,500.
- LTV = $75k / $93.5k = 80.2%.
- **Liquidation triggered.** Lenders sell your collateral to cover the shortfall, locking in the loss.

**Scenario 2 — ETH price falls 15%**: stETH stays pegged; ETH falls in USD terms.
- stETH ratio unchanged (still 1.035).
- Collateral value = $100k × 1.035 = $103.5k in stETH units, but ETH is worth less USD.
- LTV unchanged (72%) in stETH terms, but your collateral is worth less USD.
- **No immediate liquidation**, but your position is underwater in USD terms.

The distinction matters: de-peg risk is specific to LST mechanics, while price risk affects all crypto collateral.

## Oracle Fallback Mechanisms

Protocols protect against oracle failure with fallbacks:

1. **Primary oracle**: Chainlink's stETH/USD or stETH/ETH price feed (most protocols use Chainlink).
2. **Secondary oracle**: Direct Lido contract query or on-chain proxy.
3. **Fallback**: Use the last reported price or temporarily disable collateral if oracles diverge beyond a threshold.

Some protocols use price-band guards: if the oracle reports a price outside a reasonable range (e.g., stETH falls below $0.90 per ETH), the protocol pauses collateral acceptance until the price stabilizes. This prevents flash-crash liquidations.

## Comparing LST Collateral Across Services

Different LSTs have different oracle and de-peg characteristics:

| LST | Backing | De-peg History | Current LTV | Oracle Type |
|---|---|---|---|---|
| stETH (Lido) | ~31% of staked ETH | 3–5% de-pegs (2022, 2023) | 75–85% | Chainlink primary |
| rETH (Rocket Pool) | Decentralized pool | Rare, minor (<2%) | 70–80% | Less liquid, slightly lower LTV |
| cbETH (Coinbase) | Centralized (Coinbase) | None | 75–80% | Counterparty risk on Coinbase |
| swETH (Swell) | Newer, smaller | Minimal history | 50–65% | Still proving reliability |

Lido's dominance (>30% of staked ETH) makes stETH the deepest LST market and easiest to liquidate. rETH is smaller but more distributed. cbETH carries implicit Coinbase counterparty risk. Newer LSTs get lower LTVs due to unproven history.

## Yield Stacking Sustainability

Yield stacking—borrowing against LST collateral to re-lend—is profitable when borrow rates are low and lending rates are high. But this spread can vanish:

- **Lender competition**: As more capital floods into lending pools, yields fall. A 4% yield can drop to 2%, squeezing the 1.5% spread.
- **Risk re-pricing**: After a de-peg event, borrow rates on LST collateral might jump from 2.5% to 4%, eliminating arbitrage.
- **Liquidation losses**: If you're liquidated during a de-peg, you lose not just the spread but principal, erasing months of gains instantly.

Sophisticated yield stackers hedge by:
- Using low LTV (e.g., 60% instead of 80%) to survive larger de-pegs.
- Monitoring oracle prices and adjusting positions before liquidation thresholds are hit.
- Diversifying across multiple LSTs to avoid single-service risk.

## Integration with DeFi Lending Protocols

Major lending protocols (Aave, Compound, Maker) have deployed LST-specific risk frameworks:

**Aave**: Accepts stETH, rETH, cbETH in separate "risk modes." stETH has the highest LTV (82.5%), rETH slightly lower (70%), reflecting de-peg history and collateral quality.

**Compound**: More conservative; stETH LTV capped at 70% initially, increased to 75% after stability proven.

**Maker**: Mints DAI against LST collateral; uses 50% LTV for most LSTs, emphasizing stability of DAI peg over capital efficiency.

These choices reflect protocol governance preferences and risk appetite. Protocols with lower risk tolerance use lower LTVs; those seeking TVL growth use higher LTVs.

## The Future: Multi-LST Collateral Pools

As LSTs mature, protocols are exploring collateral pools combining multiple LSTs (stETH + rETH + cbETH). This diversification reduces single-service risk: if stETH de-pegs, the pool's average de-peg is smaller because rETH and cbETH might stay stable. These pools use blended oracles and allow borrowers to post LST combinations for improved capital efficiency without concentrating on one service.

## See also

<div class="wiki-seealso">

### Closely related

- [DeFi Collateral Types Compared](/defi-collateral-types-compared/) — Full comparison of volatile assets, LSTs, and stablecoins
- [DeFi Fee Tier Selection for Liquidity Providers](/defi-fee-tier-selection/) — How LST holders provide liquidity and earn fees
- [Vote-Escrow Bribe Markets in DeFi](/ve-token-bribe-market/) — Governance incentives for LST-supporting liquidity
- [Counterparty Risk](/counterparty-risk/) — Staking service solvency and LST defaults
- [Price Discovery](/price-discovery/) — Oracle mechanics and price-feed reliability
- [Liquidation and Margin Calls](/debt-to-equity-ratio/) — Liquidation mechanics and haircut calculations

### Wider context

- [Ethereum Staking](/proof-of-stake/) — Underlying ETH staking mechanics
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — LST/ETH trading pairs and de-peg mechanics
- [Yield](/dividend-yield/) — Staking yield and reinvestment strategies

</div>

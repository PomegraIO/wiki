---
title: "Stablecoin Collateralization Ratio Explained"
description: "What over-collateralization means for crypto-backed stablecoins, why ratios above 100% are required, and what happens when collateral falls below the threshold."
keywords:
  - stablecoin collateralization ratio explained
  - over-collateralization crypto
  - crypto-backed stablecoin
  - liquidation trigger stablecoin
  - collateral requirements stablecoin
image: "/svg/crypto.svg"
---

*A **stablecoin collateralization ratio** is the percentage of collateral (usually crypto) held in reserve relative to the value of stablecoins issued. Crypto-backed stablecoins require ratios above 100%—often 150% or higher—because the collateral itself is volatile. When the ratio falls below the minimum, the protocol automatically liquidates collateral to restore the peg.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stablecoin Collateralization — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Over-collateralization is the price of maintaining stability when collateral is volatile.</div>

|   |   |
|---|---|
| **Collateralization ratio** | Collateral value ÷ Stablecoins issued; expressed as a percentage |
| **Typical range** | 120% to 200%+ for crypto-backed stablecoins |
| **Why over 100%** | Collateral is volatile; buffer prevents insolvency if collateral price drops |
| **Liquidation trigger** | Automatic if ratio falls below minimum threshold (often 110–120%) |
| **Capital efficiency** | Lower ratio = more stablecoins issued per unit collateral, but higher liquidation risk |
| **Example** | $1,500 in ETH collateral backing 1,000 STABLEUSD = 150% collateralization |

</aside>

## The Core Idea: Collateral as a Safety Buffer

A **crypto-backed stablecoin** is issued against cryptocurrency held in reserve. The simplest model: a protocol holds $1 in Bitcoin and issues $1 in stablecoins. In theory, the stablecoin is fully backed and can always be redeemed.

In practice, the collateral is volatile. If Bitcoin's price drops 20% overnight, $1 of Bitcoin is now worth $0.80, but $1 of stablecoins is still outstanding. The protocol is insolvent: there isn't enough collateral to cover all issued stablecoins.

To prevent this, crypto protocols require **over-collateralization**: holders must lock up more collateral than the value of stablecoins they mint. A 150% collateralization ratio means locking $150 of collateral to mint $100 of stablecoins. Now if collateral drops 20%, there's still $120 of value backing $100 of stablecoins. The protocol remains solvent.

## How the Ratio Is Calculated

The formula is straightforward:

**Collateralization Ratio = (Total Collateral Value) / (Total Stablecoins Issued) × 100%**

Example:
- A user deposits 1 Bitcoin (worth $43,000) into the Dai stablecoin protocol.
- The protocol allows them to mint 20,000 Dai (worth $1 each = $20,000 issued).
- Collateralization ratio = $43,000 / $20,000 = 215%

The user is over-collateralized by a factor of 2.15. They've locked up 2.15x the value they've borrowed. This 215% ratio is typical for Dai; other protocols set different requirements.

A user could mint more Dai (say, 25,000 Dai worth $25,000) if they were willing to live with a lower ratio of 172%. But lower ratios increase liquidation risk, so there's usually a minimum threshold—e.g., Dai may allow collateralization ratios down to 150%, and liquidate positions that fall below 150%.

## Why Not Just Require 100%?

With 100% collateralization, each stablecoin is backed 1:1 by collateral. Why not just do that?

The answer: **volatility**. Crypto prices move fast and continuously. On any given day, Bitcoin or Ethereum can swing 5–10% or more. A 100% collateralized pool would be liquidating constantly, and small price moves would trigger insolvency.

Over-collateralization creates a buffer. If the collateral has a 10% haircut intraday, a 150% ratio still has a 40% safety margin before hitting the liquidation threshold.

The ratio needed depends on the **volatility** and **liquidity** of the collateral:
- **Low-volatility collateral** (e.g., wrapped fiat, bonds): could use lower ratios, maybe 105–110%.
- **High-volatility collateral** (e.g., altcoins, small-cap tokens): requires higher ratios, often 180%+ or even unlimited (not allowed).

Most protocols accept only blue-chip cryptocurrencies (Bitcoin, Ethereum) as collateral because they're deep-liquidity, well-studied assets. Accepting smaller tokens would require much higher ratios or introduce unhedgeable risk.

## Liquidation: What Happens When the Ratio Falls

Every crypto stablecoin protocol sets a **minimum collateralization ratio**. For Dai, it's 150%. For other protocols, it might be 120% or 200%.

If a user's collateral value drops or they mint more stablecoins and their ratio falls below the minimum, the position becomes eligible for **liquidation**.

In liquidation:
1. The protocol (or an incentivized third party, called a "liquidator") sells some of the collateral.
2. The proceeds are used to burn (retire) some of the stablecoins, restoring the ratio above the minimum.
3. The user keeps any leftover collateral after repaying stablecoins + liquidation penalty.

Example:
- Alice has 1 BTC ($43,000) as collateral and 20,000 Dai ($20,000) minted against it (215% ratio).
- Bitcoin crashes 30%, now worth $30,100.
- Alice's new ratio is $30,100 / $20,000 = 150.5%. She's at the threshold.
- Bitcoin falls another 2%, Alice's collateral is now $29,498.
- Her ratio is now 147.5%, **below** the 150% minimum. She's liquidated.
- A liquidator sells 0.3 BTC (~$12,900) and uses the proceeds to pay off $12,900 of her Dai.
- Alice now has 0.7 BTC (~$30,100 - $12,900 = remaining collateral) and owes $7,100 Dai.
- Her new ratio is ($30,100 - $12,900) / $7,100 ≈ 240%, safe again.
- Alice also paid a liquidation fee (often 5–10%), which goes to the liquidator as incentive.

This process is **automatic** and happens on-chain. There's no human judgment or delay. As soon as the ratio dips below the threshold, liquidations trigger.

## Capital Efficiency vs. Safety

Lower collateralization ratios are more **capital efficient**: a user can issue more stablecoins for a given amount of locked collateral. A 120% ratio lets you mint 83 cents of stablecoins per dollar of collateral; a 150% ratio lets you mint only 67 cents per dollar. The 120% ratio is "more efficient" in that sense.

But lower ratios are also riskier. With 120%, a 20% drop in collateral value causes liquidation. With 150%, you'd need a 33% drop. Over-collateralization is a cost of stability.

Protocols balance this by:
- Setting collateralization ratios based on the asset's volatility (Bitcoin: 150%, riskier alts: 200%+).
- Charging stability fees or borrow rates that compensate lenders for the risk.
- Offering incentives (governance tokens, rewards) to users who over-collateralize heavily.

Traders and speculators often prefer lower ratios to maximize leverage. Conservative lenders prefer higher ratios to reduce liquidation risk. Protocols try to serve both by allowing a range and adjusting parameters via governance.

## Cascading Liquidations and Systemic Risk

One risk in stablecoin systems: **cascade liquidations**. If many users are at or near the liquidation threshold and collateral drops sharply, a wave of simultaneous liquidations floods the market with sell orders.

In a market downturn, this can push collateral prices down further, triggering more liquidations, creating a death spiral. If liquidations overwhelm the market's ability to absorb them, collateral may sell at a steep discount, and stablecoins may lose their peg.

Dai is often cited as a resilient system because:
1. It requires high collateralization (150%+), so there's a large buffer.
2. It accepts multiple collateral types, reducing concentration risk.
3. It has governance mechanisms to adjust rates and thresholds in a crisis.

Less-robust designs (e.g., single-collateral systems with tight thresholds) have historically spiraled into insolvency when liquidations hit.

## Fiat-Backed and Algorithmic Stablecoins: Different Models

Not all stablecoins use crypto collateral. Different backing models have different risk profiles:

**Fiat-backed** (e.g., USDC, Tether): Backed by dollar reserves in a bank, not crypto. No liquidation mechanic because the backing is external and stable. The risk is whether the issuer actually holds the claimed reserves.

**Crypto-backed** (e.g., Dai): Backed by volatile crypto collateral. Requires over-collateralization and liquidation mechanisms to stay stable.

**Algorithmic** (e.g., Terra Luna's UST): Backed by a mechanism (incentives to arbitrage the peg), not by explicit collateral. No collateralization ratio. These have historically been the most fragile.

Regulators increasingly favor fiat-backed stablecoins because they're simpler and more transparent. Crypto-backed systems are more decentralized but harder for non-technical users to understand and more prone to liquidation cascades.

## See also

<div class="wiki-seealso">

### Closely related

- [Stablecoin](/stablecoin/) — overview of stablecoin types and mechanisms
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where stablecoins are traded and collateralized
- [Smart Contract](/smart-contract/) — the code executing liquidations automatically
- [Liquidation](/liquidation/) — the automatic sale of collateral when a threshold is breached
- Decentralized Finance — the blockchain environment where crypto-backed stablecoins operate

### Wider context

- Leverage and Leverage Ratio — related to over-collateralization in traditional finance
- Margin Call — the traditional finance analog to liquidation
- [Blockchain Fundamentals](/blockchain-fundamentals/) — how stablecoins are issued and tracked on-chain

</div>
---
title: "Health Factor in DeFi Borrowing"
description: "Health factor measures how close a DeFi loan is to liquidation. See how it's calculated and why it matters to avoid forced collateral sales."
keywords:
  - health factor defi borrowing
  - health factor defi
  - defi health factor calculation
  - liquidation threshold
  - collateral ratio
image: /svg/crypto.svg
---

*A **health factor** is the speedometer of a DeFi loan. It tells you how much collateral cushion you have before the protocol automatically liquidates your position. Understanding how it's calculated and watching it in real time is the difference between a controlled borrowing strategy and a sudden margin call.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Health Factor — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Health factor above 1.0 is safe; below 1.0 triggers liquidation. The higher, the more cushion you have.</div>

|   |   |
|---|---|
| **Definition** | Ratio of (collateral value × liquidation threshold) to outstanding debt |
| **Safe threshold** | Above 1.5 (conservative) to 1.0 (at risk) |
| **Liquidation trigger** | Drops to 1.0 or below |
| **Calculation** | HF = (Collateral Value × LT) / Outstanding Debt |
| **What moves it** | Collateral price changes, borrowed amount changes, new deposits/withdrawals |
| **Real-time monitoring** | Critical; HF can swing 20%+ in minutes during market volatility |

</aside>

## The Health Factor Formula

The **health factor** is calculated as:

**Health Factor = (Collateral Value × Liquidation Threshold) / Outstanding Debt**

Breaking this down:

- **Collateral Value**: The current market value of all assets you've posted as collateral.
- **Liquidation Threshold (LT)**: A percentage set by the protocol for each asset, representing how much of the collateral can be borrowed against. Not all assets have the same LT; volatile assets have lower ones.
- **Outstanding Debt**: The total amount of borrowed assets you owe, valued at their current prices.

**Example:**

You deposit $15,000 of ETH (liquidation threshold 80%) and borrow $10,000 of USDC.

Health Factor = ($15,000 × 0.80) / $10,000 = $12,000 / $10,000 = **1.2**

Your health factor is 1.2. You have a 20% cushion before liquidation. If ETH falls 16.7%, collateral drops to $12,500, and:

Health Factor = ($12,500 × 0.80) / $10,000 = $10,000 / $10,000 = **1.0**

At 1.0, liquidation is triggered.

## Why Different Assets Have Different Liquidation Thresholds

A protocol doesn't treat all collateral equally. **Liquidation Threshold (LT)** varies by asset based on risk:

| Asset | Typical LT | Reason |
|-------|-----------|--------|
| ETH | 80–82% | High liquidity, moderate volatility |
| BTC | 75–80% | Lower supply, similar volatility to ETH |
| Stablecoins (USDC, USDT) | 90–95% | Low volatility, predictable price |
| Altcoins | 40–60% | High volatility, lower liquidity |
| Exotic tokens | 10–30% | Very high risk, low liquidity |

A stablecoin has a 95% LT because it's unlikely to lose 5% of its value suddenly. ETH has 80% because a 20% swing is plausible. A volatile altcoin might have 50% because liquidation is more likely.

This design incentivizes borrowers to post stable, liquid collateral and discourages relying on risky assets as a cushion.

## Health Factor in Motion: A Real Scenario

Imagine you have a typical DeFi borrowing position:

**Initial setup:**
- Collateral: $20,000 of ETH at $2,000/ETH (10 ETH), LT = 80%
- Borrowed: $12,000 of USDC
- Health Factor = ($20,000 × 0.80) / $12,000 = 1.33 (safe)

**Scenario 1: Mild market dip**

ETH drops to $1,900/ETH. Collateral is now worth $19,000.

Health Factor = ($19,000 × 0.80) / $12,000 = $15,200 / $12,000 = **1.27** (still safe)

You lost $1,000 in collateral value, but your health factor only dropped 0.06 points. No liquidation risk yet.

**Scenario 2: Sharp sell-off**

ETH crashes to $1,500/ETH. Collateral is now worth $15,000.

Health Factor = ($15,000 × 0.80) / $12,000 = $12,000 / $12,000 = **1.0** (liquidation zone)

You're at the liquidation threshold. A liquidator can now repay your debt and take your collateral (plus a [liquidation penalty](/defi-liquidation-penalty-explained/)).

**Scenario 3: Deeper crash**

ETH falls to $1,250/ETH. Collateral is worth $12,500. You're being liquidated.

Health Factor = ($12,500 × 0.80) / $12,000 = $10,000 / $12,000 = **0.83** (below 1.0)

Your position is underwater; liquidation has already been triggered. A liquidator steps in, pays off your $12,000 USDC, and takes your $12,500 ETH (plus the [liquidation penalty](/defi-liquidation-penalty-explained/)).

## Multi-Asset Collateral and Weighted Health Factors

Most DeFi protocols allow you to deposit multiple assets as collateral. The health factor calculation extends to all of them:

**Health Factor = (Sum of All Collateral Values × Their Respective LTs) / Total Outstanding Debt**

**Example with mixed collateral:**

- $10,000 of ETH (LT 80%)
- $5,000 of USDC (LT 95%)
- $8,000 of DAI (LT 90%)
- Total collateral value: $23,000
- Total LT-weighted value: ($10,000 × 0.80) + ($5,000 × 0.95) + ($8,000 × 0.90) = $8,000 + $4,750 + $7,200 = $19,950
- Outstanding debt: $15,000

Health Factor = $19,950 / $15,000 = **1.33**

This framework allows you to optimize collateral composition. Swapping volatile altcoins for ETH and stablecoins improves your health factor without changing your total collateral value.

## Factors That Move the Health Factor

**1. Collateral price changes (most common).** If your collateral loses value, your health factor falls. Volatile collateral is riskier because big swings are frequent.

**2. Borrowed asset price changes.** If you borrowed ETH and the price of ETH rises, your debt (measured in USD or other reference) increases, and health factor falls. If ETH falls, your debt (in USD terms) shrinks, and health factor rises. This is why borrowing volatile assets is riskier—the debt you owe can suddenly balloon.

**3. Deposits or withdrawals.** Adding more collateral raises your health factor; removing collateral lowers it. The protocol may prevent withdrawals if they would push your health factor below a safe level.

**4. New borrows.** Every time you borrow more, your debt increases and health factor falls.

**5. Repayments.** Paying off debt raises health factor immediately.

**6. Protocol changes to liquidation thresholds.** If the protocol adjusts an asset's LT downward (recognizing increased risk), health factors fall across all positions using that collateral. This is rare but can happen during market stress.

## The Danger of Watching HF Only

A common mistake: treating health factor as a static number. It's not. During a market crash, it can deteriorate much faster than borrowers expect.

Here's why:

- **Collateral and debt prices move independently.** If you borrowed BTC when BTC was $60k and posted ETH at $2,000, a sudden BTC pump to $70k increases your debt while ETH might stay flat. Your HF falls instantly.
- **Liquidation cascades.** If a major position gets liquidated (collateral dumped on exchanges), it can push other collateral prices down, triggering more liquidations and sinking other HFs.
- **Liquidation delays.** During extreme volatility (network congestion, exchanges offline), liquidators may not be able to act instantly. Your HF can drop well below 1.0 before anyone can liquidate. You might lose 20%+ of collateral to slippage and penalties.

## Practical Rules for Health Factor Management

**Conservative:** Keep HF above 2.0. You can tolerate a 50% collateral crash without liquidation.

**Moderate:** Keep HF above 1.5. A 33% collateral decline won't trigger liquidation, but volatility is noticeable.

**Aggressive (not recommended):** Keep HF between 1.1 and 1.2. Any 8–10% collateral move is dangerous. You're one flash crash away from liquidation.

**Never borrow in such a way that your health factor is below 1.5** unless you're an expert trader actively managing the position and you understand the liquidation penalty you'll pay if things go wrong.

## Monitoring Tools

Most DeFi platforms display health factor prominently in the UI. But for serious borrowers:

- **Set alerts** (on platforms that offer them) when HF drops below 1.5.
- **Monitor collateral prices** in real time, especially if you're borrowing volatile assets.
- **Run scenarios**: "If ETH drops 15%, what's my HF?" This helps you size positions wisely.
- **Automate** small repayments or collateral additions to keep HF stable when prices move.

The protocol's liquidation threshold and your health factor are the guardrails of safe borrowing. Ignore them at your peril.

## See also

<div class="wiki-seealso">

### Closely related

- [DeFi liquidation penalty explained](/defi-liquidation-penalty-explained/) — the cost you pay when HF drops to 1.0
- [Real yield DeFi vs inflationary yield](/real-yield-defi-vs-inflationary-yield/) — understanding protocol incentives and borrowing sustainability
- Collateral — the assets securing your debt
- [Leverage](/leverage-ratio-forex/) — general concept of borrowing for amplified returns

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — how DeFi protocols execute liquidations on-chain
- Risk management — broader borrowing and margin discipline
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where liquidators dump collateral
- [Volatility](/currency-volatility/) — the force that moves health factors

</div>

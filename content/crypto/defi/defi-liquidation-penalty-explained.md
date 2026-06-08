---
title: "DeFi Liquidation Penalty Explained"
description: "When a DeFi loan gets liquidated, borrowers lose collateral. See what percentage gets seized and why protocols choose different penalties."
keywords:
  - defi liquidation penalty explained
  - liquidation penalty defi
  - liquidation fee
  - collateral loss defi
  - protocol penalties
image: /svg/crypto.svg
---

*When a **DeFi liquidation penalty** is triggered, a borrower doesn't just lose the collateral needed to cover the debt—they lose additional collateral as a fee. The size of that penalty, typically 5–15%, varies by protocol and asset, and understanding it is crucial to calculating true borrowing risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DeFi Liquidation Penalty — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Penalties reward liquidators for acting quickly and compensate protocols for bad debt; they're built into borrowing costs.</div>

|   |   |
|---|---|
| **Typical penalty range** | 5–15% of collateral value |
| **Who pays it** | The borrower (collateral owner) |
| **Who receives it** | Protocol treasury, liquidator, or both |
| **When it applies** | At the moment a position hits the liquidation threshold |
| **Why it exists** | Incentivizes rapid liquidation and covers protocol losses |
| **Example** | Borrow $10k, collateral worth $15k; liquidation penalty 10%; lose $11.5k worth of collateral to cover $10k debt |

</aside>

## How a Liquidation Penalty Works in Practice

A **DeFi liquidation penalty** is a haircut applied on top of the debt repayment when a position is forcibly closed. Here's a concrete example:

You deposit $15,000 of ETH as collateral and borrow $10,000 of USDC. The protocol sets the [health factor](/health-factor-defi-borrowing/) liquidation threshold at 1.0 and a liquidation penalty at 10%.

If ETH falls and your health factor hits 1.0, a liquidator can repay your $10,000 USDC debt. In exchange, they receive the collateral—but the borrower (you) pays a 10% penalty on the repaid amount. So the liquidator gets $11,000 worth of your ETH collateral for paying off $10,000 of debt. You've lost an additional $1,000 beyond the collateral erosion itself.

The mechanics vary slightly:

- **Penalty paid to the liquidator** (most common): The liquidator receives collateral worth debt + penalty.
- **Penalty split** (some protocols): Liquidator gets a portion, protocol treasury gets the rest.
- **Protocol-only penalty** (rarer): The protocol treasury captures the fee, and the liquidator is compensated only by arbitrage opportunity.

## Why Penalties Exist

Liquidation penalties serve three functions:

**1. Incentivizing rapid liquidation.** A [health factor](/health-factor-defi-borrowing/) can deteriorate quickly during market shocks. A liquidator will only move capital and pay gas fees if the profit is certain and large enough. The penalty creates that profit opportunity. Without it, positions might linger at the brink of insolvency, increasing risk to the protocol and other depositors.

**2. Covering protocol losses.** If a liquidation is slow or collateral value drops further during the liquidation process, the protocol eats the loss. The penalty is a buffer. It also compensates the protocol for bad debts that occasionally slip through (liquidators fail to act, slippage is worse than expected, or collateral was misvalued).

**3. Penalizing leverage abuse.** The fee discourages borrowers from taking on excessive leverage. If you know you'll lose an extra 10% on top of collateral erosion if something goes wrong, you're more cautious about margin ratios. This is a form of behavioral control—the protocol uses the penalty to price risk.

## Penalty Levels Across Protocols

Liquidation penalties vary widely. Here's why:

**Aave** (one of the largest lending protocols) sets penalties at 5–10% depending on the asset and reserve configuration. High-risk collateral (volatile altcoins) may have 10–15% penalties; stable assets like stablecoins have lower ones.

**Compound** uses fixed 8% penalties across most assets, with no variation.

**Curve** (focused on stablecoin trading and lending) often runs lower penalties (2–5%) because the collateral is less volatile and liquidations happen less frequently.

**MakerDAO** (overcollateralized [cryptocurrency](/cryptocurrency-exchange/) lending to issue stablecoins) sets penalties based on stability fees and risk; they're often 10–13%.

The variation reflects protocol design philosophy and risk tolerance:

- **Higher penalties** (12–15%) suit volatile assets or newer protocols that need strong liquidation incentives.
- **Lower penalties** (3–7%) work for stablecoin pairs or platforms with deep liquidity where liquidators can easily exit collateral.
- **Dynamic penalties** (some newer protocols) adjust based on market volatility; they rise during crashes to ensure liquidators have skin in the game.

## The True Cost of Borrowing

A borrower should think of the liquidation penalty as part of the borrowing cost, not a one-time event. If you're borrowing with a 150% [collateral ratio](/—/) and a 10% liquidation penalty, a 33% drop in collateral price will trigger liquidation and cost you 10% of your outstanding debt. That's expensive insurance against a bad outcome.

Calculating true borrowing cost requires:

**1. Interest rate** paid to depositors (e.g., 5% per annum).

**2. Probability of liquidation** over your holding period (depends on [collateral volatility](/currency-volatility/) and your margin).

**3. Expected penalty loss** = Liquidation probability × Penalty size.

If your collateral is volatile, that expected penalty loss can exceed the interest you're earning on borrowed assets, making the trade uneconomical.

## When Penalties Spike and Edge Cases

Penalties become painful during market crashes. When the [health factor](/health-factor-defi-borrowing/) threshold is breached, a liquidator may face:

- **Slippage.** Selling $11,000 of seized collateral in a thin market may net only $10,500, so the liquidator's profit evaporates or turns negative. Rational liquidators stop participating, positions fester, and the protocol must absorb losses.
- **Cascading liquidations.** If ETH drops 40% in one hour, thousands of positions hit liquidation at once. Liquidators are overwhelmed; some slippage is inevitable, making liquidation less profitable. The penalty alone may not be enough to compensate liquidators for slippage risk.

Some protocols address this with **escalating penalties**: if a position isn't liquidated quickly, the penalty increases to 15–20% after a time delay, forcing liquidators to act or lose more.

## Comparing Penalties to Total Borrowing Risk

A typical DeFi borrowing scenario:

| | Risk component |
|---|---|
| Interest rate | 5% annually |
| Liquidation penalty (if triggered) | 10% one-time |
| Probability of liquidation in 1 year | ~5% (for conservative 150% ratio) |
| Expected liquidation cost | 0.5% annually |
| **Total annual cost** | **5.5%** |

This is higher than the interest rate alone, which is why borrowers demand collateral returns (via staking, token emissions, or trading fees) to offset the risk. Protocols that offer high token rewards but have tight liquidation thresholds are essentially hiding the true cost of borrowing.

## Liquidity, Liquidators, and Penalty Sufficiency

The liquidation penalty only works if liquidators exist and are willing to act. In illiquid or exotic-asset markets, even a 20% penalty may not attract liquidators because they can't exit the collateral profitably. This is a real fragility: the protocol's entire liquidation mechanism depends on a functioning arbitrage market.

Major protocols address this by:

- Whitelisting liquid collateral only (ETH, major stablecoins, major altcoins).
- Running liquidation auctions where liquidators bid competitively.
- Offering protocol-owned liquidity pools to absorb collateral sales.
- Raising penalties dynamically when liquidity dries up.

## See also

<div class="wiki-seealso">

### Closely related

- [Health factor in DeFi borrowing](/health-factor-defi-borrowing/) — the metric that triggers liquidation
- [Real yield DeFi vs inflationary yield](/real-yield-defi-vs-inflationary-yield/) — understanding true protocol sustainability and collateral returns
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where collateral is traded during liquidation
- [Liquidation](/liquidation/) — broader concept of asset sales under distress

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — how DeFi executes smart contracts
- [Smart contract risk](/—/) — operational risks in protocol mechanics
- [Collateral](/—/) — the asset securing the loan
- [Leverage](/leverage-ratio-forex/) — how collateral ratios create liquidation risk

</div>

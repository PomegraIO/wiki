---
title: "How Futures Margin Is Calculated"
description: "Learn how futures exchanges calculate initial and maintenance margin using SPAN and VAR models to cover counterparty risk."
keywords:
  - how futures margin is calculated
  - initial margin futures
  - maintenance margin futures
  - span model
  - var margin
  - futures clearing risk
---

*Futures exchanges don't set margin based on whim—they use mathematical models like SPAN (Standardized Portfolio Analysis of Risk) or Value-at-Risk to calculate how much collateral a trader must post. These models estimate the maximum loss a position could suffer in adverse market moves and set margin requirements high enough to cover that risk while keeping trading viable.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Margin — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Exchanges quantify trader loss exposure; margin covers that daily.</div>

|   |   |
|---|---|
| **Initial margin** | Collateral posted when opening a position; typically 5–15% of contract value. |
| **Maintenance margin** | Lower threshold; shortfall triggers forced liquidation. Often 70–75% of initial. |
| **SPAN model** | Scans 16 price scenarios (up/down moves, volatility shifts) to find worst loss. |
| **Mark-to-market** | Futures settle daily; gains/losses cash in or out each close. |
| **Variation margin** | Cash posted/withdrawn to restore balance after each day's settlement. |
| **Counterparty risk driver** | Clearinghouse must cover if a defaulting trader's losses exceed margin held. |

</aside>

## The Goal: Cover Tail Risk Without Strangling Trading

Margin is fundamentally a risk-containment tool for the clearinghouse—the central counterparty that guarantees every futures trade. When you buy a contract, you don't own it outright; the clearinghouse sits between you and the seller. If prices move sharply against you and you can't cover losses, the clearinghouse faces a hole. Initial and maintenance margin are designed to cushion that risk.

The key tension is this: set margin too low and the clearinghouse bleeds in a crash; set it too high and traders can't afford to trade. Exchanges calibrate using scenario analysis—modeling what the worst realistic loss could be—rather than simple percentage rules.

## SPAN: The Industry Standard

SPAN (Standardized Portfolio Analysis of Risk), developed by the Chicago Mercantile Exchange, is the dominant methodology. It works by scanning your entire portfolio through 16 standardized price scenarios:

- **Underlying price moves**: typically ±1, ±2, and ±3 standard deviations of recent volatility
- **Volatility shifts**: implied volatility rises or falls by a fixed amount
- **Time decay**: value erodes as expiration nears

For each scenario, SPAN recalculates the mark-to-market P&L on every position. It then identifies the worst loss across all scenarios—the "scanning risk"—and sets initial margin equal to (roughly) that worst-case loss plus a small buffer.

**Concrete example**: Suppose you're long one S&P 500 futures contract (worth ~$500,000 notional at an index level of 5,000 per point value of $250). The contract is very liquid, so volatility is stable. SPAN scans 16 scenarios including "index drops 3%." That would cost you $3,750 (0.03 × 500,000 × factor). If the worst loss across all scenarios is $4,200, initial margin might be set at $5,000 to add a cushion.

## Value-at-Risk (VaR) as an Alternative

Some exchanges, particularly for less-liquid contracts, use a VaR-based approach. VaR estimates the loss level that would be exceeded only, say, 1% of the time under normal market conditions (the "confidence level"). A 1-day, 99% VaR on a position might estimate a $4,000 loss; margin is set to cover that, often with an extra multiplier (e.g., 1.5×) for prudence.

VaR is more statistically grounded but can underestimate tail risk during market stress—a known weakness that regulators have acknowledged since the 2008 crisis. SPAN's scenario-based approach sidesteps this by not relying on historical volatility and can be adjusted manually if stress conditions warrant.

## Initial vs. Maintenance Margin

**Initial margin** is what you must post to open or add to a position. It's the full calculated cushion.

**Maintenance margin** is lower—often 70% or 75% of initial—and triggers a margin call if your account balance falls below it. The gap between initial and maintenance gives you a buffer zone; you don't face liquidation the instant a small loss occurs.

**Example**: Initial margin $5,000, maintenance $3,750. You open a long position and post $5,000. If the contract falls and your position loses $1,500, your account balance drops to $3,500—below the $3,750 maintenance level. Your broker demands a margin call; you must deposit at least $1,500 to restore it to the initial level. If you don't, the broker liquidates your position.

## Mark-to-Market and Variation Margin

Futures settle daily. At the close of each trading day, your position is revalued at the settlement price, and gains or losses are realized in cash—either added to or subtracted from your margin account.

This is **variation margin**: the daily settlement cash flow. It's distinct from initial and maintenance margin, which are account balance thresholds. Variation margin is the mechanism that forces losses to be paid immediately, before they can compound.

Because of daily settlement, the theoretical counterparty risk over a single day is smaller than with forwards or swaps. The clearinghouse collects losses daily and doesn't let positions rot; a trader can't bury a $100,000 loss by walking away.

## Why Margin Levels Vary Across Contracts

Margin isn't uniform. A highly liquid, tightly tracked contract like ES (E-mini S&P 500) has lower initial margin—perhaps $10,000–$12,000—because the risk is well-understood and the contract can be liquidated instantly without slippage. A thinly traded agriculture futures contract might have 15%–20% initial margin because it's harder to exit in a squeeze.

Volatility also matters. During tranquil markets, SPAN scans show modest worst-case losses, so margins stay low. When volatility spikes—such as March 2020 or May 2010—SPAN recomputes and margin jumps sharply. This is a feature, not a bug: it forces traders to delever when the system is stressed.

## Leverage and Margin Efficiency

A trader with $10,000 margin posting $5,000 initial margin can control two contracts worth ~$1 million notional—roughly 100:1 leverage. This is legal and standard in futures. But it's also why margin calls bite: a 1% move costs $10,000 and wipes out the account.

Some sophisticated funds optimize margin efficiency by submitting a "portfolio-level" margin calculation to their clearinghouse or broker. Instead of calculating margin on each contract separately, they show the clearinghouse their entire portfolio and argue that diversification lowers the collective worst-case loss. The clearinghouse agrees and negotiates a lower combined margin requirement. This is rare for retail traders but standard for hedge funds and dealers.

## The 2020 Volatility Spike: Margin in Stress

In March 2020, as equity volatility exploded, major exchanges doubled or tripled margin requirements within days. Traders who relied on tight margin calculations suddenly faced simultaneous margin calls on multiple contracts. Some large funds couldn't raise cash fast enough and were liquidated—a small contributor to the broader fire-sale dynamic that week. The lesson: margin models work fine in normal times; in tail events, both the model and the trader's liquidity can fail together.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — mechanics of standardized exchange-traded derivatives
- [Counterparty Risk](/counterparty-risk/) — why clearinghouses demand collateral
- [Value-at-Risk](/value-at-risk/) — statistical measure of loss distribution used in margin models
- [Mark-to-Market](/mark-to-market/) — daily settlement mechanism in futures
- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — margin and leverage in currency trading

### Wider context

- [Derivatives: Hedging](/derivatives-hedging/) — using futures to manage portfolio risk
- [Forward Contract](/forward-contract/) — over-the-counter alternative with no daily settlement
- [Basis Risk](/basis-risk/) — slippage when hedging with an imperfect contract
- [Execution Risk](/execution-risk/) — risk of liquidation orders failing to fill

</div>

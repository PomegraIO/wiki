---
title: "How to Calculate a Hedge Ratio"
description: "A hedge ratio is the size of a derivative position needed to offset the risk of an underlying exposure. The minimum-variance hedge ratio uses correlation and volatility to minimize residual risk."
keywords:
  - hedge ratio calculation
  - minimum-variance hedge ratio
  - hedging formula
  - futures hedge ratio
  - correlation-based hedging
  - effective hedge
---

*A **hedge ratio** tells you how many futures or derivative contracts to buy or sell to neutralize the price risk of an underlying position. The most common approach, the minimum-variance hedge ratio, uses historical [correlation](/basis/) and [volatility](/historical-volatility/) to find the position size that leaves you least exposed to residual risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hedge Ratio — Key Formula and Intuition</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A 0.8 hedge ratio means buying or selling 80 contracts to hedge 100 units of underlying exposure.</div>

|   |   |
|---|---|
| **Minimum-variance formula** | h = ρ × (σ_S / σ_F), where ρ = correlation, σ_S = volatility of spot, σ_F = volatility of futures |
| **Typical h range** | 0 (no hedge) to 1.0 (perfect one-to-one); >1 is possible but rare |
| **Application** | Futures contracts, forward contracts, swap hedges, protective puts |
| **Data required** | Historical price series (typically 1–3 years) or current market parameters |
| **Residual risk** | Even perfect h does not eliminate all risk if correlation is <1 or other factors move independently |
| **Rebalancing** | Hedge ratio drifts over time; periodic recomputation advised |

</aside>

## The Hedge Ratio Problem

Suppose you own 100,000 barrels of crude oil as inventory. The price is volatile, and you want to lock in a selling price today for delivery three months from now. You decide to hedge using crude oil [futures contracts](/futures-contract/).

One futures contract controls 1,000 barrels. A naive approach: short exactly 100 contracts (100 × 1,000 = 100,000 barrels), a one-to-one hedge.

But there is a catch: the futures contract and the physical crude oil don't move in lockstep. The futures trade on a centralized exchange with daily mark-to-market settlement; physical oil is delivered at the end of three months. If the futures basis (the difference between futures price and spot price) changes unexpectedly, your hedge is imperfect.

The **hedge ratio** solves this by asking: "What number of futures contracts minimizes my overall risk?" The answer is rarely exactly 100.

## The Minimum-Variance Hedge Ratio Formula

The most widely used approach in risk management is the **minimum-variance hedge ratio**:

**h = ρ × (σ_S / σ_F)**

Where:
- **h** = hedge ratio (number of futures contracts per unit of underlying)
- **ρ** (rho) = historical [correlation](/basis/) between the spot price and the futures price (ranges from −1 to +1)
- **σ_S** (sigma S) = historical [volatility](/historical-volatility/) of the spot price (standard deviation of price returns)
- **σ_F** (sigma F) = historical volatility of the futures price

The numerator ρ × σ_S captures how much the underlying moves relative to the average. The denominator σ_F captures how much the futures move. Dividing them tells you how many futures contracts to use to track the underlying's moves.

If correlation is perfect (ρ = 1) and volatilities are equal (σ_S = σ_F), then h = 1: a one-to-one hedge is optimal. If volatility of the underlying is twice that of the futures, or if correlation is only 0.5, then h will be less than 1, and you would use fewer futures to hedge.

## A Worked Example: Hedging a Copper Inventory

You own 50 metric tons of copper (approximately $200,000 at current prices). You are concerned about price drops over the next six months. To hedge, you plan to sell copper futures contracts.

**Step 1: Gather historical data**

Using the past two years of daily prices, you compute:
- **Correlation between spot copper and copper futures**: ρ = 0.92 (high correlation; they move together most of the time)
- **Volatility of spot copper (σ_S)**: 18% annualized
- **Volatility of copper futures (σ_F)**: 20% annualized

**Step 2: Calculate the hedge ratio**

h = 0.92 × (0.18 / 0.20) = 0.92 × 0.9 = 0.828

**Step 3: Determine the position size**

A standard copper futures contract controls 25 metric tons. You own 50 tons.

Using a hedge ratio of 1.0 (one-to-one), you would short 2 contracts (2 × 25 = 50 tons).

Using the minimum-variance ratio of 0.828, you would short 0.828 × 2 = 1.656 contracts. Since you can't short a fractional contract, you round to **1.66 contracts** (or 1–2 contracts, depending on your broker's rounding convention).

**Step 4: Observe the outcome**

Over the next three months, suppose copper spot price falls 10% (your inventory loses $20,000). The copper futures contract falls 9.5% (driven by slightly lower volatility). Your short 1.66 futures contracts gain approximately 0.095 × 1.66 × 25 tons × (copper price per ton) ≈ $19,000.

Your net loss is only $1,000 instead of the full $20,000. The hedge worked—not perfectly, because of basis risk and rounding, but well enough to substantially reduce your loss.

## Why Not a Perfect One-to-One Hedge?

You might ask: why not just short 2 contracts (a one-to-one physical-to-futures match) and call it done?

The answer is that the futures and spot prices don't move identically. Futures volatility is 20%, while spot is 18%, and their correlation is 0.92, not 1.0. If you over-hedge by using too many futures, you end up with a net short position if prices rise: you would miss upside gains because the futures gains don't fully offset the underlying asset's movement.

Using the minimum-variance ratio de-emphasizes the futures leg to match the true risk of the underlying. It is optimal in the sense that it minimizes the variance of the hedged portfolio's returns. It doesn't eliminate all risk (that would require h = 1 and perfect correlation), but it comes as close as the historical relationship allows.

## Basis Risk and Imperfect Hedges

Even with an optimal hedge ratio, residual risk remains. This is **basis risk**: the risk that the basis (futures price minus spot price) changes unexpectedly.

In the copper example, if the futures-spot spread widens unexpectedly—say, because of transport delays or sudden demand for physical copper—your hedge may leave you exposed despite the correct h.

Three reasons basis risk persists:

1. **Correlation < 1**: The futures and spot don't move in perfect lockstep. Idiosyncratic factors (supply shocks, regulatory changes) can move one but not the other.
2. **Volatility mismatch**: Even with the same correlation, if one asset is more volatile, the hedge ratio will under- or over-weight it, leaving residual exposure.
3. **Time-varying parameters**: Historical correlation and volatility are not constant. If the market regime changes, the hedge ratio estimated from past data becomes suboptimal.

A hedge ratio of 0.83 (as in the copper example) typically reduces risk by 60–80%, but not to zero. This is why hedging is called risk *reduction*, not risk *elimination*.

## Computing Hedge Ratios in Practice

Professional risk managers use several approaches:

**Regression method (most common)**: Regress historical spot returns on futures returns. The slope of the regression line is the hedge ratio. This directly estimates how much a 1% move in futures translates to a move in spot, adjusted for correlation.

Regression equation: **ΔS = α + h × ΔF + ε**

Where ΔS is the spot return, ΔF is the futures return, and ε is the residual. The estimated h is the optimal hedge ratio.

**Beta method**: In some markets, hedge ratio is estimated as the beta of the spot with respect to the futures. For commodity markets, this is often computed using 1–3 years of historical daily returns.

**Model-based method**: For derivatives like options, the hedge ratio is the [delta](/delta/), computed using the Black-Scholes model or other [derivatives pricing](/derivatives-hedging/) frameworks.

## Dynamic Hedging and Rebalancing

A hedge ratio is not static. As market prices change, correlations and volatilities shift, and the optimal h drifts. Professional hedgers recompute the ratio monthly or quarterly and rebalance.

If your copper hedge ratio was 0.828 six months ago and is now 0.75 (perhaps because spot and futures volatilities have shifted), you should adjust: reduce your short futures position from 1.66 to 1.50 contracts to restore optimality.

Frequent rebalancing incurs transaction costs, so there is a trade-off. Hedging too aggressively (using too large an h) leaves you exposed to upside moves. Hedging too timidly (too small an h) leaves you exposed to downside. The minimum-variance framework balances this using statistical evidence.

## Limitations and Extensions

The minimum-variance approach assumes:
- Normal distributions of returns (real markets have fat tails)
- Constant correlation and volatility (markets are regime-dependent)
- No transaction costs (real hedging is expensive)
- Sufficient historical data (in novel markets, data is sparse)

For larger hedges or more complex exposures, traders may use **value-at-risk (VaR)** models or stress-testing frameworks to supplement the hedge ratio with scenario analysis.

## See also

<div class="wiki-seealso">

### Closely related

- [Basis](/basis/) — the futures-spot spread; basis risk is the key residual after hedging
- [Historical volatility](/historical-volatility/) — critical input into the hedge ratio formula
- [Correlation](/basis/) — another critical input; imperfect correlation limits hedge effectiveness
- [Futures contract](/futures-contract/) — the instrument used in most operational hedges
- [Delta](/delta/) — the hedge ratio for options positions
- [Delta hedging explained with example](/delta-hedging-explained-with-example/) — application of hedging to derivatives

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — broader framework for managing derivatives risk
- [Risk management](/concentration-risk/) — the goal of all hedging activity
- [Value-at-risk](/value-at-risk/) — an alternative framework for measuring residual risk post-hedge
- [Spot rate](/spot-rate/) — the underlying price being hedged

</div>

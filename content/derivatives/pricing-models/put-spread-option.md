---
title: "Put Spread"
description: "Strategy combining a long put with a short put at a lower strike to define and limit downside risk."
keywords:
  - put spread
  - defined risk
  - bearish options strategy
  - debit spread
---

*A **put spread** pairs a long put with a short put at a lower strike, capping both the loss and the profit in a downside bet. The spread costs less than a naked long put but cuts maximum payoff; it's the disciplined way to hedge when you're certain about direction but budgeted on cost.*

<aside class="wiki-infobox">

| Factor | Detail |
|--------|--------|
| **Type** | Defined-risk options strategy |
| **Posture** | Bearish (directional down) |
| **Max Profit** | Strike difference minus premium paid |
| **Max Loss** | Premium paid |
| **Breakeven** | Long strike minus net debit |
| **Implied Cost** | Debit (net outflow upfront) |
| **Liquidity Need** | Moderate to high |

</aside>

## How a put spread reduces risk

A naked [long put](/wiki/put-option/) exposes you to unlimited theoretical loss if the stock rallies past the strike — you stay short the downside forever. A put spread closes that risk window by selling a put further down the chain. The proceeds from the short put shrink your net outlay; you trade away unlimited upside leverage for a defined, quantifiable cost. This is [capital discipline](/wiki/capital-allocation/) in action: you decide in advance exactly how much downside you're willing to fund.

## Construction and payoff

You buy a put at strike *S₁* and sell a put at strike *S₂*, where *S₂ < S₁*. The net debit is (*S₁ premium minus S₂ premium*). Both contracts share the same expiration.

**Below *S₂* (maximum loss):** Both puts are in-the-money. The long put gains point-for-point; the short put loses point-for-point. They cancel below *S₂*, locking your loss at the initial debit. 

**Between *S₂* and *S₁* (profit zone):** The long put is profitable, the short put is worthless. Your gain grows linearly up to the strike difference.

**Above *S₁* (maximum profit):** Both puts expire worthless. You keep the net credit as pure profit.

## Mechanics at expiration

At settlement, the exchange nets the two obligations. If the stock closes at *S₂ − 5*, you exercise the long put and are assigned on the short put simultaneously. Cash settles the difference: you receive the full width of the spread minus your upfront premium. Assignment risk is [eliminated](/wiki/central-counterparty-clearing/) by the clearing corporation.

## When put spreads beat naked puts

You use a put spread when:

- **Budget constraints:** You want downside exposure but can only afford a fraction of a naked put's cost.
- **Defined risk horizons:** You're hedging a known, time-bound liability (a dividend payment due next month, for instance), not betting indefinitely on the market turning.
- **Probability weighting:** You're confident the stock will fall *to a certain floor* but have no conviction below that floor. The short put caps your exposure right at your conviction boundary.
- **Income focus:** You sell a higher-conviction short strike to finance a more aggressive long strike, converting leverage cost into income.

Compare a single long put on XYZ at 100 strike costing 3 points (300 per contract) to a 100–95 put spread costing 1 point (100 per contract). The spread costs a third as much; you lose that edge if the stock falls below 95. That trade-off is explicit and predetermined.

## Rolling and adjustment

Put spreads invite [calendar management](/wiki/rolling-options/). If the stock stabilizes above *S₁*, you can roll the short put down and out to lock in premium or reduce decay drag on the long put. If the stock crashes, you can roll the long put up to widen your range and collect more premium from the short put. These trades require active monitoring and broker coordination; [passive holders](/wiki/buy-and-hold-strategy/) who can't execute roll orders should avoid spreads entirely.

## Spread width and Greeks

A tighter spread (e.g., 100–98, two points) costs less but leaves little room between breakeven and max profit. A wider spread (e.g., 100–90, ten points) costs more but offers more cushion and profit per premium unit. Neither is universal; width depends on your conviction range and volatility regime.

The [delta](/wiki/delta-option-greeks/) of the spread equals the long delta minus the short delta. A 100–90 spread on a stock near 100 might have a blended delta of 0.45 − 0.15 = 0.30, moving 30 cents per dollar move. The [gamma](/wiki/gamma-option-greeks/) concentrates near the short strike, where the spread's payoff flattens.

## Taxation and wash sales

Each leg of the spread is a separate contract. A closing trade or assignment on one leg does not affect the other. This can create [wash-sale](/wiki/wash-sale/) complexity if you're harvesting losses while holding the other leg. Document each fill separately and consult your tax accountant if you're scaling in and out of positions.

## Comparison to other bearish spreads

A [bear call spread](/wiki/bear-call-spread/) (long call, short call, upside cap) is its mirror: you sell call premium to fund a long call. A put spread is more aggressive in the downside direction. The [bear put spread](/wiki/bear-put-spread/) (short put, long put, defined loss) collects premium upfront — the opposite cash flow — and profits if the stock stays above *S₂*. All three are defined-risk; the direction and premium flow are what differ.

<div class="wiki-seealso">

### Closely related
- [Put Option](/wiki/put-option/) — foundational single-leg downside bet
- [Debit Spread](/wiki/debit-spread/) — cost-structure category for all spreads paid upfront
- [Bear Put Spread](/wiki/bear-put-spread/) — opposite cash flow, same strikes
- [Call Spread](/wiki/call-spread/) — long call equivalent
- [Defined Risk](/wiki/defined-risk-options/) — core principle

### Wider context
- [Options Greeks](/wiki/options-greeks/) — delta, gamma, theta, vega behavior
- [Option Expiration](/wiki/option-expiration/) — settlement mechanics
- [Capital Allocation](/wiki/capital-allocation/) — budgeting downside bets
- [Interest Rate Risk](/wiki/interest-rate-risk/) — spreads on fixed income
- [Risk Management](/wiki/risk-management/) — broader portfolio discipline

</div>

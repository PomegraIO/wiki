---
title: "Duration Hedging"
description: "Matching the duration of assets and liabilities to immunise a portfolio against parallel shifts in the yield curve."
keywords:
  - duration hedging
  - interest-rate immunisation
  - duration matching
  - yield-curve risk
  - asset-liability management
image: "/svg/risk.svg"
---

*A **duration hedge** offsets interest-rate risk by matching the time-weighted sensitivity of assets against the time-weighted sensitivity of liabilities. When durations are aligned, a parallel shift in yields leaves the net portfolio value (assets minus liabilities) roughly unchanged.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk and hedging." />

<div class="wiki-infobox-caption">The insurance that works when yields move uniformly; the reminder that yields rarely do.</div>

|   |   |
|---|---|
| **What it is** | Equalising the [duration](/duration/) of assets and liabilities to neutralise interest-rate risk |
| **Also called** | Duration immunisation, duration matching, gap management |
| **Why it matters** | Protects net worth from unexpected yield curve shifts without requiring frequent rebalancing |
| **Key measure** | [Duration](/duration/) — weighted average time to cash flow, expressed in years |
| **Common users** | Banks, insurers, pension funds, bond portfolio managers |
| **Limitation** | Works only for small, parallel yield shifts; fails when curve is non-parallel or convex |

</aside>

## The asymmetry of time

A bond is a sequence of future cash flows. The farther in the future those flows lie, the more they are affected by a change in yield. [Duration](/duration/) captures this: it is the weighted-average time to receipt of a bond's cash flows, with weights proportional to the present value of each flow.

A bond with a duration of 5 years loses approximately 5% of its value if all yields rise by 1 percentage point. A bond with a duration of 2 years loses approximately 2%. This linear approximation is precise for small yield moves and is the foundation of duration hedging.

A bank's liabilities—primarily customer deposits—have an implicit duration. Deposits in a checking account have a duration close to zero, because they can be withdrawn on demand. Deposits in a Certificate of Deposit maturing in 3 years have a duration of roughly 3 years (less, because of early withdrawal risk). The bank's overall liability duration is a weighted average of all customer balances.

If the bank invests 80% of deposits in 10-year mortgages and 20% in 2-year securities, its asset duration is roughly 8.4 years. If the deposit base has an average duration of 1 year (short-term money that can be withdrawn quickly), the bank is *long duration*: its assets will fall much more than its liabilities if all yields rise. A duration hedge would shorten the asset side—by selling some mortgages and buying more short-term securities, or by using interest-rate derivatives to synthetically shorten duration—until assets and liabilities are matched.

## Why matching matters

When asset duration equals liability duration, parallel yield shifts do not change the economic net worth of the institution. If yields rise by 1% across all maturities, assets and liabilities both fall by roughly the same percentage, and net assets (equity) are unchanged. Conversely, if yields fall by 1%, both assets and liabilities rise, and equity is unaffected.

This is the promise of duration hedging: immunisation against interest-rate risk, without speculating on the direction of rate moves. The bank does not need to predict whether rates will rise or fall. It simply keeps its assets and liabilities duration-matched and is protected either way.

Pension funds and insurers apply the same logic. A pension fund has a liability stream: promised payments to retirees stretching decades into the future. It can estimate the duration of this liability stream (the weighted-average time to payouts). By investing in a bond portfolio with matching duration, the fund insulates itself from rate risk. A rise in rates increases the present value of its future contributions (lower discount rate for funding) while decreasing the value of its current asset holdings, but these effects approximately offset.

## The practise: rebalancing and drift

In theory, a duration-hedged position is static: once matched, it stays matched. In practise, duration is not truly constant. As time passes, bonds age. A 5-year bond today is a 4-year bond tomorrow. If nothing else changes, duration of the held bond declines. Similarly, as yields shift, durations of both assets and liabilities change (usually in the same direction but not by identical amounts). The hedge drifts, and periodic rebalancing is needed.

A conservative approach is to rebalance whenever the hedge drifts by more than 0.5 years of duration (or 1 year, depending on risk tolerance). This rebalancing incurs transaction costs—bid-ask spreads, commissions, market impact—but it keeps the duration match tight enough that yield moves do not create large unintended gains or losses.

An alternative is to use interest-rate derivatives instead of actually buying and selling bonds. A bank could hold a bond portfolio with 8 years of duration, then sell interest-rate swaps (paying fixed, receiving floating) with a notional amount calibrated to synthetically shorten the duration to match a 1-year liability duration. The swap costs less to enter and exit than selling and buying bonds, and rebalancing is faster. The trade-off is counterparty risk: the bank is exposed to the credit of the swap counterparty.

## The assumption: parallel shifts

The bedrock of duration hedging is the assumption that yield curves shift in parallel: all yields rise or fall by the same amount. In reality, yield curves twist, flatten, and steepen. Short yields sometimes move differently from long yields. Spreads between different maturities widen and narrow. A duration hedge that is perfectly neutralised to a parallel shift can be devastatingly exposed to a non-parallel move.

Consider a bank that matches its overall duration but has liabilities concentrated in short maturities (deposits maturing in 1–2 years) and assets concentrated in long maturities (10-year mortgages). If short yields rise by 2% while long yields fall by 1% (a steepening), the bank's liabilities reprice upward immediately, but the assets stay underwater. The duration hedge is useless.

This is where [convexity hedging](/convexity-hedging/) and more sophisticated techniques come in. A bank managing serious interest-rate risk does not stop at duration; it also monitors key-rate durations (the sensitivity of the portfolio to shifts at specific points on the curve) and hedges against non-parallel moves.

## Duration in other contexts

Duration hedging extends beyond balance-sheet management. A pension fund managing its liability stream uses duration matching. A real-estate investor with a mortgage can hedge using bond futures or swaps to offset interest-rate risk. A corporate treasurer managing bond debt can buy [call options](/call-option/) or swaptions to hedge refinancing risk—the risk that rates rise and future borrowing becomes expensive.

In all cases, the principle is the same: estimate the duration of your exposure, then use a hedging instrument with matching duration to neutralise first-order interest-rate risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the weighted-average time to a bond's cash flows; a measure of interest-rate sensitivity
- [Convexity hedging](/convexity-hedging/) — managing second-order interest-rate sensitivity beyond duration
- [Interest-rate swap](/interest-rate/) — exchanging fixed and floating payments to synthetically adjust duration
- [Proxy hedging](/proxy-hedging/) — using correlated instruments when direct hedges are unavailable
- [Gamma hedging](/gamma-hedging/) — rebalancing to maintain a delta-neutral position as prices move
- [Yield curve](/yield-curve/) — the relationship between bond maturity and yield

### Wider context

- [Bond](/bond/) — a fixed-income security with periodic coupons and principal repayment
- Immunisation — strategy to insulate a portfolio from interest-rate moves
- [Interest-rate risk](/interest-rate-risk/) — the sensitivity of asset values to changes in market yields
- [Mortgage](/fixed-rate-mortgage-personal/) — a loan secured by real estate; often duration-hedged
- Liability-driven investment — aligning investment strategy with future obligations

</div>

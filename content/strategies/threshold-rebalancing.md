---
title: "Threshold rebalancing"
description: "Threshold rebalancing is a strategy of returning portfolio allocations to target levels only when allocations drift beyond predetermined thresholds, keeping transaction costs low while maintaining desired allocation."
keywords:
  - threshold rebalancing
  - drift-based rebalancing
  - trigger-based rebalancing
  - tolerance bands
  - bands rebalancing
  - dynamic rebalancing
image: "/svg/strategies.svg"
---

*Threshold rebalancing is an approach of rebalancing a [portfolio](/asset-allocation/) only when [asset-class](/asset-allocation/) weights drift beyond predetermined tolerance bands or thresholds. Unlike [calendar rebalancing](/calendar-rebalancing/), which rebalances on a fixed schedule, threshold rebalancing rebalances opportunistically, only when needed.*

<div class="wiki-hatnote">

For time-based rebalancing, see [calendar-rebalancing](/calendar-rebalancing/). For broader rebalancing context, see [asset-rebalancing](/asset-rebalancing/). For allocation strategy, see [asset allocation](/asset-allocation/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Threshold rebalancing — key facts</div>

<img src="/svg/strategies.svg" alt="Tolerance bands showing when rebalancing is triggered" />

<div class="wiki-infobox-caption">Threshold rebalancers act only when allocations cross predetermined bands, minimizing costs and trading frequency.</div>

|   |   |
|---|---|
| **Core idea** | Rebalance when allocations drift beyond tolerance bands |
| **Typical band** | ±5% from target (e.g., 60% ± 5% = 55–65% stocks) |
| **Frequency** | Variable; depends on volatility and drift |
| **Advantage** | Lower transaction costs and tax drag |
| **Disadvantage** | Requires monitoring; judgment on band widths |
| **Flexibility** | High; rebalances when markets demand it |
| **Implementation** | Manual monitoring or automated alerts |

</aside>

## How threshold rebalancing works

An investor sets predetermined tolerance bands around each target allocation:

**Target:** 60% stocks, 40% bonds

**Tolerance bands:** ±5%

**Allowable range:** 55–65% stocks, 35–45% bonds

The investor monitors the portfolio periodically (monthly, quarterly). When allocations drift outside the band, rebalancing is triggered. When they remain within the band, no rebalancing occurs.

**Example:** After a stock rally, the portfolio drifts to 68% stocks, 32% bonds — outside the 55–65% band. Rebalancing is triggered to return to 60/40. If the portfolio is 62% stocks, 38% bonds — still within the 55–65% band — no rebalancing occurs.

## Advantages

1. **Efficiency.** By rebalancing only when necessary, threshold rebalancing minimizes transaction costs relative to calendar rebalancing.
2. **Tax efficiency.** Fewer trades mean fewer capital gains triggers in taxable accounts.
3. **Market-aware.** Rebalancing is triggered by drift, not by calendar, so it naturally responds to volatile markets with more rebalancing when allocations change rapidly.
4. **Reduced herding.** The threshold approach is less synchronized with others' rebalancing schedules, potentially avoiding crowded rebalancing moments.

## Disadvantages

1. **Monitoring required.** Unlike calendar rebalancing (which happens on autopilot), threshold rebalancing requires periodic monitoring.
2. **Drift tolerance.** Wide tolerance bands (±10%) mean the portfolio can drift significantly from targets, increasing risk. Narrow bands (±2%) trigger frequent rebalancing, increasing costs.
3. **Behavioral temptation.** The flexibility of threshold rebalancing can allow discretionary overrides ("Wait, the market looks good; I'll rebalance next quarter instead").
4. **No forced buy in crashes.** If a crash occurs and stocks fall to 45% (within 55–65%), no forced buying occurs. A more conservative investor might prefer calendar rebalancing to force buying in crashes.

## Typical band widths

- **5% bands.** Most common for equity-bond portfolios. Balances cost efficiency with allocation maintenance.
- **3% bands.** More conservative; more frequent rebalancing to stay closer to targets.
- **10% bands.** For cost-conscious investors or those with high transaction costs.

Bands are typically symmetric around the target (±5%) but can be asymmetric (e.g., ±3% lower, ±7% upper) if the investor has strong views about acceptable drift directions.

## See also

<div class="wiki-seealso">

### Closely related

- [Asset-rebalancing](/asset-rebalancing/) — the broader rebalancing discipline
- [Calendar-rebalancing](/calendar-rebalancing/) — the alternative time-based approach
- [Asset allocation](/asset-allocation/) — the target allocation
- [Capital-rotation](/capital-rotation/) — active reallocation
- [Tax-loss harvesting](/tax-loss-harvesting/) — tax-aware rebalancing

### Wider context

- [Stock](/stock/) — equity component
- [Bond](/bond/) — fixed-income component
- [Diversification](/diversification/) — rebalancing maintains it
- [Risk management](/asset-allocation/) — allocation discipline

</div>

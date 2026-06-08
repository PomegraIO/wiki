---
title: "Constant Proportion Portfolio Insurance"
description: "A dynamic rebalancing rule that increases exposure to risky assets as the portfolio value rises above a specified floor."
keywords:
  - constant proportion portfolio insurance
  - CPPI
  - dynamic asset allocation
  - portfolio insurance
  - floor value
image: "/svg/strategies.svg"
---

*A **Constant Proportion Portfolio Insurance** (CPPI) strategy is a dynamic rebalancing formula that scales a portfolio's exposure to risky assets in proportion to how far the current value sits above a minimum acceptable level (the "floor"). As the portfolio grows, risky exposure increases; if the portfolio declines toward the floor, risky exposure shrinks. The formula mechanically enforces a cushion between the current portfolio value and the floor, ensuring the floor is never breached under normal market conditions while allowing upside participation when the portfolio is healthy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Constant Proportion Portfolio Insurance — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for portfolio strategy." />

<div class="wiki-infobox-caption">A formula that grows bolder as you grow richer.</div>

|   |   |
|---|---|
| **What it is** | A dynamic rebalancing rule that links risky-asset exposure to portfolio value relative to a floor |
| **Also called** | CPPI, proportional portfolio insurance |
| **Core formula** | Risky Exposure = Multiplier × (Portfolio Value − Floor) |
| **Typical multiplier** | 2–4; higher multiplier = more aggressive scaling |
| **Floor** | Minimum acceptable portfolio value; typically a percentage of initial value or a specific dollar amount |
| **Suited for** | Long-term investors with explicit return floors; liability-driven portfolios; endowments |
| **Risk** | Gap risk: in extreme market jumps, the floor may be breached; leverage risk if multiplier is too high |

</aside>

## The floor and the multiplier

CPPI operates through two parameters:

1. **The floor**: A minimum portfolio value, expressed either as a dollar amount (e.g., "never fall below $500,000") or as a percentage of initial value (e.g., "maintain 80% of starting capital"). The floor represents the investor's true loss-aversion limit—the point at or below which the strategy must reduce risk to zero.

2. **The multiplier**: A constant that determines how aggressively to scale up risky exposure as the portfolio grows above the floor. Common multipliers range from 2 to 4.

The rebalancing formula is:

**Risky Exposure = Multiplier × (Current Portfolio Value − Floor)**

**Safe Exposure = Current Portfolio Value − Risky Exposure**

For example, suppose a portfolio starts at $1,000,000 with a floor of $800,000 and a multiplier of 2:

- **Current value**: $1,000,000; Cushion: $200,000; Risky exposure: 2 × $200,000 = $400,000; Safe exposure: $600,000.
- **If value rises to $1,200,000**: Cushion: $400,000; Risky exposure: 2 × $400,000 = $800,000; Safe exposure: $400,000. The portfolio becomes more aggressive as wealth accumulates.
- **If value falls to $900,000**: Cushion: $100,000; Risky exposure: 2 × $100,000 = $200,000; Safe exposure: $700,000. The portfolio becomes more conservative to guard the floor.

## Why it works: insuring upside while protecting downside

CPPI is psychologically and financially appealing because it offers what investors often want: a guaranteed minimum outcome with unencumbered participation in good markets.

Consider two alternatives:

- **Buy-and-hold**: If the portfolio is 60% equities and markets crash, you fall well below your acceptable minimum.
- **Static stop-loss**: If the portfolio falls below 90% of value, you sell everything to cash. This locks in losses and misses the recovery.

CPPI threads the needle. It reduces equity exposure as the portfolio approaches the floor, but increases it as the portfolio rises above the floor. If markets recover after a shock, the portfolio is partially invested in equities and participates in the bounce. If markets fall further, the strategy has already de-risked and is not exposed.

## Relationship to other rebalancing rules

CPPI is more aggressive than [volatility-band rebalancing](/volatility-band-rebalancing/) because it compounds exposure gains: each dollar of profit is re-invested into riskier assets. A 60/40 portfolio stays 60/40 regardless of performance. A CPPI portfolio shifts toward 80/20 equity-heavy as wealth grows. This amplifies both gains and losses.

CPPI is more structured than [opportunistic rebalancing](/opportunistic-rebalancing/), which uses fixed allocation targets and adjusts only when both calendar and drift triggers align. CPPI rebalances continuously (or frequently) based on a mathematical formula, not on whether drift thresholds are breached.

The [rebalancing bonus](/rebalancing-bonus/) captured by mean-reversion strategies works within CPPI as well. CPPI's constant rebalancing creates natural buy-low, sell-high trades as allocations drift and are restored by the formula.

## Multiplier choice: risk and return trade-offs

The multiplier determines how much upside you capture relative to how much downside you shield:

- **Low multiplier (1.5–2)**: Conservative. The portfolio grows slowly but rarely approaches the floor. Safe for investors with strong floors (large cushions between portfolio value and minimum acceptable level).

- **High multiplier (3–4)**: Aggressive. The portfolio captures more upside from risky assets, but the cushion erodes faster, and you hit rebalancing bands more frequently. Appropriate for investors with large cushions and high risk tolerance.

- **Very high multiplier (5+)**: Carries substantial leverage risk, especially during market jumps. If equity markets gap down 20% overnight (as happened in 1987 or during the COVID crash), the formula cannot rebalance fast enough and the floor is breached. Most practitioners avoid this.

## Gap risk: the fatal flaw

CPPI assumes continuous or near-continuous rebalancing. In reality, markets often gap—prices jump without intervening trades. If a stock market crashes 30% between the close of one day and the open of the next, CPPI cannot sell equities fast enough. The portfolio value may plunge below the floor, violating the insurance contract.

This "gap risk" is CPPI's Achilles heel. During the 1987 crash, CPPI portfolios that gapped through their floors suffered losses that weren't supposed to be possible. Similarly, during the 2008 financial crisis, the 9/11 attacks, and the COVID-19 market crash, gap risk materialized.

Practitioners mitigate gap risk by:

- Using a lower multiplier to maintain a larger cushion.
- Setting the floor conservatively (e.g., 70% of initial value instead of 90%).
- Using options or [protective puts](/protective-put/) alongside the formula to enforce an absolute floor.
- Rebalancing more frequently (daily or intraday if possible).

## When CPPI makes sense

CPPI works best for:

- **Endowments and foundations**: Long time horizons; explicit return floors tied to spending requirements.
- **Pension funds**: Liability-driven investing; need to ensure minimum funding ratios.
- **Wealthy investors late in the accumulation phase**: Have large cushions; can afford aggressive multipliers; benefit from rising exposure as wealth compounds.
- **Hedged portfolios**: If you combine CPPI with long-volatility strategies or put protection, you address gap risk and enforce the floor mathematically.

CPPI is poorly suited for:

- **Investors with small cushions**: If your floor is 95% of current portfolio value, even small market moves trigger constant rebalancing.
- **Illiquid portfolios**: Daily rebalancing is not feasible if your holdings are difficult to trade.
- **Taxable accounts without good execution**: Every rebalancing creates taxable events; without careful [tax-loss harvesting](/tax-loss-harvesting/), the tax drag may exceed the insurance benefit.
- **Investors who will panic-sell**: CPPI requires discipline to stick to the formula during crises. If you ignore it and sell near the floor, you lock in losses.

## Variants and extensions

**Time-varying CPPI**: Adjust the floor and multiplier as you approach your investment horizon. Early in the accumulation phase, use an aggressive multiplier; as you approach spending, become more conservative.

**Stochastic CPPI**: Use [value-at-risk](/value-at-risk/) or other probabilistic models to set the floor and multiplier based on expected market movements, not just current value.

**Multi-asset CPPI**: Apply the formula to multiple risky assets (equities, commodities, alternatives) against a safe anchor (bonds, cash), not just equities vs. bonds.

## See also

<div class="wiki-seealso">

### Closely related

- [Volatility-Band Rebalancing](/volatility-band-rebalancing/) — adjusting triggers based on market conditions
- [Opportunistic Rebalancing](/opportunistic-rebalancing/) — combining calendar and drift-based triggers
- [Rebalancing Bonus](/rebalancing-bonus/) — the mean-reversion return embedded in frequent rebalancing
- [Protective Put](/protective-put/) — option strategy that enforces a floor, often paired with CPPI
- [Asset Allocation](/asset-allocation/) — the target weights adjusted dynamically by CPPI
- [Leverage Ratio](/leverage-ratio-forex/) — CPPI amplifies returns via dynamic leverage scaling

### Wider context

- Portfolio Insurance — broader strategy class for protecting downside
- [Value at Risk](/value-at-risk/) — risk measure used to set CPPI parameters
- Risk Management — framework for setting floors and acceptable loss levels
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — coordinated strategy to reduce tax drag from frequent rebalancing
- [Options](/option/) — alternatives and complements to CPPI formula
- [Tail Risk](/tail-risk/) — gap risk and extreme market moves that can breach CPPI floors

</div>

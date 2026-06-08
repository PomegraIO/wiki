---
title: "Rolling Beta vs Static Beta"
description: "Understand why a single beta number can mislead: rolling beta tracks how market sensitivity changes over time, revealing regime shifts invisible in static beta."
keywords:
  - rolling beta vs static beta
  - time-varying beta
  - beta stability
  - regime change detection
  - moving-window beta
  - beta drift
---

*A **static beta** is a single number calculated from historical returns over a fixed period (e.g., three years). A **rolling beta** recalculates beta over a moving window (e.g., monthly or quarterly), exposing how a stock's market sensitivity shifts across market regimes. Static beta masks these shifts; rolling beta reveals whether a company's business model and leverage have fundamentally changed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Two Ways to Measure Market Sensitivity — Key Facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">Static is simple; rolling is honest about change.</div>

|   |   |
|---|---|
| **Static beta window** | e.g., 36-month lookback; one number |
| **Rolling beta window** | e.g., 12-month window; recalculated monthly |
| **Use case (static)** | Quick screening, regulatory filings |
| **Use case (rolling)** | Active management, regime detection |
| **Stability assumption** | Static: β is constant; Rolling: β changes |
| **Recalculation frequency** | Static: rarely; Rolling: every update interval |
| **Data points per number** | Static: 1 series; Rolling: dozens or hundreds |
| **Beta drift example** | Stock rising from 1.2 to 1.8 over 2 years |

</aside>

## The Static Beta Assumption

Most investors and research reports cite a single beta number: "Apple has a beta of 1.2" or "This small-cap has a beta of 2.1." These are static betas, usually calculated from three to five years of monthly returns regressed against the S&P 500. The calculation is straightforward and stable—useful for quick valuation or regulatory disclosures.

But static beta rests on a hidden assumption: that the relationship between the stock and the market is constant over time. This assumption often breaks down. A company that shifts its strategy, takes on debt, enters a new market, or faces structural change can see its beta shift significantly. A static beta averaged over the entire period misses these pivots.

## Rolling Beta Captures Regime Change

**Rolling beta** recalculates the regression constantly—say, every month using the prior 12 months of data. As you move forward in time, you drop the oldest month and add the newest, creating a moving window. The result is a time series of beta values rather than a single point estimate.

Rolling beta excels at exposing when a company's market sensitivity has genuinely changed. A stock that rises from 1.2 beta to 1.8 beta over two years will show static beta of, perhaps, 1.5. The rolling window will show the drift month by month, signaling that something in the company or market has shifted.

## A Worked Example: Fintech Disruption

Consider a regional bank with a 36-month static beta of 1.3. But zoom into rolling 12-month windows:

- **Jan 2020–Dec 2020**: beta = 0.9 (steady earnings, low volatility)  
- **Jan 2021–Dec 2021**: beta = 1.1 (interest rates rising, lending accelerates)  
- **Jan 2022–Dec 2022**: beta = 1.6 (deposit flight, rate shock hits margins)  
- **Jan 2023–Dec 2023**: beta = 1.8 (digital disruption, client defection fears)  
- **Jan 2024–Dec 2024**: beta = 2.1 (restructuring announcement, high uncertainty)

The 36-month static beta averaging these periods might be 1.5, hiding the reality: the bank's risk profile has deteriorated sharply. A portfolio manager using only the static 1.5 would have mispricced the stock's recent volatility. Rolling beta tells the true story.

## Why Beta Drifts

Several forces cause beta to change over time:

**Leverage changes**: A company that borrows heavily to fund acquisitions sees higher beta because financial leverage amplifies equity volatility. Conversely, debt paydown lowers beta.

**Business model shift**: A mature industrial company entering cyclical new markets (e.g., transitioning to renewable energy capex) can see beta rise as earnings become more volatile.

**Market structure change**: During liquidity crises, correlations spike and volatility clustering occurs, causing even stable stocks to exhibit higher beta than in normal times. Conversely, in calm periods, betas can compress.

**Size and liquidity evolution**: A company growing rapidly might shift from micro-cap (high beta, low liquidity) to mid-cap (lower beta, better liquidity). Its beta naturally normalizes downward.

**Competitive landscape**: A stock facing new disruptive competitors (e.g., a bank competing with fintech, a retail chain facing Amazon) often exhibits rising beta as profit uncertainty increases.

## Calculation Mechanics

Static beta (36-month, monthly returns):

```
Beta = Covariance(Stock Returns, Index Returns) / Variance(Index Returns)
```

Rolling beta at time *t* (12-month window):

```
Beta_t = Covariance(Stock Returns [t-11 to t], Index Returns [t-11 to t]) / Variance(Index Returns [t-11 to t])
```

The denominator variance can shift significantly across windows. In periods of high market volatility, the denominator swells, often pushing betas lower (stocks become less extreme relative to the noisier market). In calm periods, low denominator variance can inflate betas. This is not a flaw in rolling beta; it's a feature revealing true sensitivity during each regime.

## Shorter Windows and Noise

A shorter rolling window (e.g., 3 months) is more responsive to recent shifts but also noisier—random price swings can produce spurious beta spikes. A longer window (e.g., 24 months) is smoother but slower to signal genuine regime change. Most practitioners use 12-month rolling windows as a compromise.

## Static Beta in Practice: When It's Enough

Static beta is not wrong; it's just incomplete. It works well for:

- Screening for asset allocation (e.g., "I want low-beta bonds and high-beta equities")  
- Regulatory filings and prospectuses (which require a standardized, stable number)  
- Initial sizing of positions (conservative approach: use the higher of recent rolling beta or static beta)

But for active management, risk control, and understanding whether a business has fundamentally changed, rolling beta is essential.

## Beta Stability Across Market Cycles

Rolling beta is especially revealing in market stress. During normal times, two stocks might have similar static betas. But in a sharp drawdown, their rolling betas often diverge sharply. A stock with strong balance sheet and counter-cyclical earnings (e.g., a discount retailer) might see rolling beta drop to 0.8 during a crash. A leveraged cyclical stock might spike to 2.5. Static beta averages these events; rolling beta captures them.

## Cross-Asset Rolling Beta

Rolling beta also applies to asset classes and sectors. A cryptocurrency's beta to equities might be zero in a bull market (no correlation) but 0.8 in a risk-off crash (flight to safety dynamics). A rolling calculation reveals this shift. Similarly, international stocks show time-varying beta to the U.S. market, driven by currency movements, policy divergence, and contagion.

## Practical Integration

Many portfolio management systems now calculate both static and rolling beta. Active managers use rolling numbers for tactical decisions (whether to increase or trim exposure) and static for strategic positioning and transparency to clients. The two together paint a full picture: static beta anchors expectations, rolling beta alerts you when the anchor has drifted.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — the systematic risk measure itself
- [Volatility](/historical-volatility/) — price swings that beta captures
- [Regime Shift](/business-cycle/) — structural changes in markets or businesses
- [Leverage](/leverage-ratio-forex/) — financial or operating changes that drive beta drift
- [Time-Varying Risk](/volatility-smile/) — how sensitivity changes across conditions
- [Covariance](/capital-asset-pricing-model/) — the statistical foundation of beta

### Wider context

- [Risk Management](/value-at-risk/) — using beta in portfolio frameworks
- [Performance Attribution](/sharpe-ratio/) — separating alpha from beta contributions
- [Sector Rotation](/sector-rotation/) — recognizing changing betas in tactical moves
- [Market Cycles](/business-cycle/) — economic regimes that drive beta changes

</div>

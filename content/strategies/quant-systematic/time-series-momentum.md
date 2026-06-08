---
title: "Time-Series Momentum"
description: "A systematic strategy that trades each asset long or short based on the sign of its recent return alone, without comparing it to peers."
keywords:
  - time-series momentum
  - trend following
  - systematic trading
  - price momentum
  - cross-asset strategies
image: "/svg/strategies.svg"
---

*A **time-series momentum** strategy trades each asset long or short based solely on whether its own price has risen or fallen over a fixed lookback window, regardless of how other assets have performed. The trader exploits the observable tendency for many assets to continue in the direction they have been moving, filtering out absolute returns in favour of directional signals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Time-Series Momentum — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for quantitative trading strategies." />

<div class="wiki-infobox-caption">Trade the direction of each asset's own recent price movement.</div>

|   |   |
|---|---|
| **What it is** | A [systematic trading](/stock-market/) rule that long each asset if its return over 1–12 months is positive, short if negative |
| **Also called** | Absolute momentum, price momentum, univariate momentum |
| **Key lookback window** | Typically 1, 3, 6, or 12 months of historical returns |
| **Signal** | Positive return → long; negative return → short |
| **Applies to** | Individual stocks, bonds, commodities, currencies, [ETFs](/etf/) |
| **Rivals** | Cross-sectional [momentum](/momentum-investing/), mean reversion, [volatility](/historical-volatility/) strategies |

</aside>

## The core mechanism: riding your own wave

Time-series momentum rests on a deceptively simple observation: assets that have been rising tend to keep rising, and those falling tend to keep falling. This is *not* a claim that markets are perfectly efficient; nor is it random walk behaviour. Instead, it captures **price drift** — the stubborn persistence of asset returns over medium timeframes (weeks to a year), which behavioural factors, [momentum](/momentum-investing/)-seeking traders, and order-flow imbalances can sustain.

The strategy works in isolation. You don't care whether stock A has outperformed stock B; you only ask: has stock A gone up in the past six months? If yes, go long. If no, go short. You apply the same rule to every asset in your universe in parallel. For equity indices, commodity futures, and [bond](/bond/) prices, decades of research confirm that such rules capture meaningful [alpha](/alpha/).

Contrast this with cross-sectional momentum, which ranks assets against each other and bets on the winners. Time-series momentum is *univariate*—it answers only the question: which way is this asset pointing? The simplicity is its power; it requires no relative pricing, no rankings, no peers.

## Why it works: inertia, not randomness

Financial economists have documented time-series momentum across hundreds of asset classes and decades of history. The pattern is robust:

- **Medium-term drift:** Over 1- to 12-month periods, prior returns predict future returns (weakly positive autocorrelation).
- **Risk premia:** Momentum may partly reflect a systematic [risk](/market-risk/) that investors require compensation to bear—holding a momentum portfolio exposes you to drawdowns when trends reverse.
- **Behavioural anchoring:** Traders and portfolio managers often update their models sluggishly, lending inertia to price movements.
- **Order imbalance:** [Algorithmic trading](/algorithmic-trading/) and passive flows can amplify trending moves.

The effect is not universal. Equities exhibit stronger momentum than [fixed income](/bond/); some [currencies](/indian-rupee/) show trend-following patterns; [commodities](/crude-oil/) often do as well. But across a diversified mix, the signal survives. Academic tests using real transaction costs, slippage, and commissions still show positive returns after fees—though margins have tightened as capital has poured into quant strategies.

## Building the strategy: implementation choices

A working time-series momentum strategy requires three decisions:

**Lookback window.** A 6-month or 12-month lookback is typical. Some traders use rolling 3-month or 1-month windows for higher turnover. Shorter windows (days to weeks) capture microstructure noise and may trade against you. Longer windows (2–5 years) can hold you in a dying trend too long. The optimal window varies by asset and market regime; many live strategies backtest across multiple windows and blend the signals.

**Holding period.** Do you rebalance weekly, monthly, quarterly, or annually? Higher turnover increases transaction costs but allows the strategy to adapt to regime changes faster. Most systematic implementations rebalance monthly or quarterly.

**Position size and scaling.** A simple approach: equal weight each asset, then scale the portfolio by [inverse volatility](/historical-volatility/) to stabilize risk. More sophisticated variants use a [Kelly criterion](/kelly-criterion/) or risk-parity weighting. Without careful [position sizing](/position-sizing/), a few volatile assets can dominate the portfolio.

## When momentum falters: crash and reversion

Time-series momentum is not a free lunch. The strategy can suffer severe drawdowns in two regimes:

- **Trend reversals.** When an asset that has been rising suddenly turns, a momentum strategy is caught on the wrong side. A stock market crash after a bull run is the classic example; the strategy exits only after prices have already fallen.
- **Mean reversion.** In tightly mean-reverting markets (some [currency](/currency-risk/) pairs during normal times), momentum can lose money systematically.
- **Structural breaks.** A regime shift (e.g., a [central bank](/central-bank/) pivot from stimulus to tightening) can end years of profitable patterns overnight.

The drawdowns tend to cluster at market inflection points—exactly when you need diversification most. Many practitioners pair time-series momentum with other [factors](/factor-investing/) (like [value](/value-investing/) or low [volatility](/historical-volatility/)) or tactical [hedges](/hedge-fund/) to reduce left-tail risk.

## Cross-asset and regime-aware variants

Time-series momentum is just the foundation. Practitioners build on it:

- **Cross-asset blending:** Combine momentum signals across equities, bonds, commodities, and currencies. Each asset class operates on different frequencies, and blending captures diversification.
- **Volatility normalization:** [Volatility](/historical-volatility/) spikes in a crash. Some strategies dampen the long signal or increase short exposure when volatility is extreme.
- **[Regime-aware](/regime-switching-strategy/) overlays:** Add a hidden Markov filter to detect bear markets and reduce long exposure or shift to defensive signals when recession risk rises.
- **Machine learning refinements:** Instead of a fixed lookback, some quant teams train neural networks to weight the past 12 months of returns adaptively, learning which sub-windows predict the next period best.

## Institutional adoption and crowding

Since the 1990s, time-series momentum has gone from academic curiosity to mainstream quant strategy. Managed futures funds, CTA (commodity trading advisor) funds, and risk-parity portfolios all rely on it. This means:

- **Reduced edge.** With trillions invested in trend-following strategies, the alpha premium has compressed. The signals are slower to exploit, and reversals happen faster.
- **Crowding risk.** If many managers use the same lookback window and rebalance on the same days, coordinated selling can amplify drawdowns.
- **Regulatory scrutiny.** Exchanges and regulators monitor for "flash crashes" and correlated liquidations, sometimes limiting how aggressively momentum traders can act.

For individual investors, the implications are clear: time-series momentum remains a useful diversifier within a [multi-factor portfolio](/factor-investing/), but it is no longer a licence to print money.

## See also

<div class="wiki-seealso">

### Closely related

- [Momentum investing](/momentum-investing/) — broad framework for trend-following across equities and sectors
- [Alternative data strategies](/alternative-data-strategies/) — systematic approaches using unconventional data sources
- [Regime-switching strategy](/regime-switching-strategy/) — conditioning allocation rules on detected market states
- [Factor investing](/factor-investing/) — building portfolios around systematic risk premia
- [Algorithmic trading](/algorithmic-trading/) — automated execution at scale

### Wider context

- [Volatility smile](/volatility-smile/) — how [implied volatility](/implied-volatility/) varies by strike, relevant to risk management
- [Value-at-risk](/value-at-risk/) — measuring portfolio tail risk
- [Leverage ratio](/leverage-ratio-forex/) — controlling notional exposure in systematic strategies
- [Market timing](/market-timing/) — the perennial alternative to trend-following rules
- Backtesting — validating strategy returns on historical data

</div>

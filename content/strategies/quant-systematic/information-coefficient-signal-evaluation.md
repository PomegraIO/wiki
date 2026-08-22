---
title: "Information Coefficient for Evaluating Quant Signals"
seo_title: "Information Coefficient (IC): How to Evaluate Signals"
description: "Information coefficient (IC) is the correlation between a signal's forecasts and realized returns. Typical values, ICIR, and pitfalls in signal testing."
keywords:
  - information coefficient ic quant
  - signal evaluation metrics
  - quant signal predictive power
  - information coefficient ranking signal
  - icir information ratio
  - systematic trading validation
  - signal strength measurement
---

*The **information coefficient** is the correlation between a quantitative signal's predictions and actual subsequent returns—a standard metric in quantitative investing to measure whether a trading signal genuinely forecasts price movement or merely looks good in hindsight. By comparing IC across signals and across time periods, systematic traders decide which factors deserve a place in a live strategy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Information Coefficient — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for quantitative strategies." />

<div class="wiki-infobox-caption">IC quantifies signal skill before deploying capital.</div>

|   |   |
|---|---|
| **Definition** | Correlation between signal prediction and realized returns |
| **Range** | −1 to +1; typically 0.01–0.10 for tradeable signals |
| **Time window** | Usually 1 to 20 trading days forward-looking |
| **ICIR** | IC divided by standard deviation of IC; risk-adjusted signal quality |
| **Interpretation** | Higher (further from zero) = stronger forecasting power |
| **Pitfall** | High IC in backtest may not persist in live trading (overfitting) |

</aside>

## Why Information Coefficient Matters

In quantitative investing, a signal is only as good as its ability to predict future price movement. Information coefficient answers the question directly: does this signal contain skill, or just noise?

Without IC, a systematic trader might build a portfolio around a factor that appears profitable in historical data but happens to align with one lucky market regime. IC reveals whether the alignment is genuine—a stable, repeatable correlation—or mere coincidence. It's the foundation of [due diligence](/due-diligence/) in factor research and the primary hurdle a signal must clear before being allocated real capital.

The metric is named after the broader concept of "information ratio," which measures risk-adjusted returns; IC is the raw correlation that feeds into that calculation.

## How Information Coefficient Is Calculated

**IC is simply the Pearson correlation coefficient** between your signal (on a given date) and the subsequent returns of the same assets (over a forward-looking window, often 1 to 20 days). 

The formula is:

```
IC = Corr(Signal_t, Return_t+1)
```

Where:
- **Signal_t** = The signal value (a rank, z-score, or raw prediction) for each asset on day t
- **Return_t+1** = The realized return for each asset between day t and day t+k (the forward window)
- **Corr** = Pearson correlation, calculated across all assets in the universe on that date

**Example**: On Monday, you compute a momentum signal for 500 stocks (values ranging from −2 to +2). The next Friday, you measure each stock's 5-day return. You then calculate the correlation between Monday's signal and Friday's returns. If the correlation is 0.08, your IC for that week is 0.08.

Practitioners typically compute IC for every date in the backtest (rolling window), producing a time series of IC values—e.g., 250 daily ICs across one year—and then report the mean IC and the standard deviation of IC.

## What Makes a "Good" Information Coefficient

**The interpretation depends on context, but for liquid, well-studied markets, the bar is high:**

- **IC = 0.00** = Signal has zero predictive power; it's pure noise.
- **IC = 0.01 to 0.05** = Weak but potentially tradeable. If you combine dozens of such signals (diversification benefit) or use very low-cost execution, you might generate alpha.
- **IC = 0.05 to 0.10** = Solid signal. Many successful quant funds operate on signals in this range.
- **IC = 0.10+** = Exceptional. Rare in public markets; if you find it, guard it. Most published academic factors show ICs of 0.02–0.07.
- **IC < 0.00** = Signal has negative predictive power (inverse signal). Flip it and re-test.

The key insight: even a 0.02 IC can be profitable if you manage costs and scale the signal across thousands of positions. Conversely, a 0.05 IC can be worthless if trading costs eat the edge.

## Rank IC vs. Raw IC

When comparing assets, **you must decide whether to rank the signal or use its raw value.** This choice matters for IC.

**Raw IC (Pearson on raw values):** Most common. Measures whether the signal's absolute magnitude correlates with returns. Works well if your signal is already zero-mean or naturally scaled (e.g., a z-score).

**Rank IC (Spearman on ranks):** Uses the rank of each signal value rather than the value itself. More robust to outliers. Preferred when your signal has extreme values that might distort a correlation.

In practice, both are often computed. If they diverge significantly, it suggests your signal has outliers that dominate the relationship—a red flag.

## Information Coefficient Ratio (ICIR)

**ICIR = Mean IC / Std Dev of IC**

This ratio normalizes IC for its consistency. A signal with IC = 0.05 every month is stronger than one with IC = 0.08 one month and −0.02 the next, even if the average is higher.

ICIR of 0.5 or above is considered good; 1.0+ is excellent. It's analogous to a [Sharpe ratio](/sharpe-ratio/) but applied to signal quality rather than portfolio returns.

## The Backtest-Reality Gap: Overfitting and Decay

The biggest pitfall: a signal with stellar IC in backtested data often disappoints in live trading. This happens for several reasons:

**Overfitting**: The signal was tuned to historical noise that won't repeat. A signal that passes multiple threshold-tweaks and parameter optimizations will naturally fit idiosyncrasies of the backtest period.

**Regime change**: The IC was high during a particular market environment (e.g., a bull market favoring momentum). When the regime shifts, the signal's predictive power vanishes.

**Data snooping**: Across thousands of candidate signals, some will show high IC by pure chance. Without a stringent false-discovery test, you'll deploy them and watch them fail.

**Decay**: Even genuine signals tend to weaken after publication. Once many traders exploit a factor, the edge dissipates.

To mitigate, professional quant shops use:
- **Out-of-sample testing**: Holdout test periods not used in optimization.
- **Walk-forward analysis**: Rolling train-test windows to check if IC remains stable.
- **Cross-asset or cross-period validation**: Verify the signal works on different assets or countries, not just the original backtest set.
- **Stress testing**: Measure IC during market stress (volatility spikes, crashes) to see if the signal holds.

## Integrating IC Into a Multi-Signal Strategy

Systematic strategies rarely deploy a single signal. Instead, they combine dozens or hundreds, each contributing small positive IC. The portfolio's overall edge comes from [diversification](/diversification/) across uncorrelated signals.

A typical workflow:
1. **Test each candidate signal's IC** in isolation. Discard any with IC < 0.01 or high overfitting risk.
2. **Compute pairwise correlations** between signals. Prefer uncorrelated signals to compound the edge.
3. **Construct a [portfolio](/capital-asset-pricing-model/)** weighting each signal by its ICIR or other risk-adjusted metric.
4. **Monitor live IC** weekly or monthly. If a signal's IC collapses, remove or recalibrate it.

This modular approach distributes risk: if one signal fails, others carry the strategy.

## See also

<div class="wiki-seealso">

### Closely related

- [Alpha](/alpha/) — The excess returns a signal or strategy generates above market benchmarks
- [Factor investing](/factor-investing/) — Systematic approach to harvesting returns from risk factors
- [Quantitative easing](/quantitative-easing/) — Central bank policy; unrelated but often confused with quant trading
- Backtesting — Historical validation of trading strategies; IC is a core metric
- Overfitting — The risk that IC in-sample does not predict out-of-sample returns

### Wider context

- [Sharpe ratio](/sharpe-ratio/) — Risk-adjusted return metric for portfolios; ICIR is the signal equivalent
- Market efficiency — If markets are efficient, IC should be zero; high IC suggests market gaps
- [Algorithmic trading](/algorithmic-trading/) — Automated execution of quant signals

</div>
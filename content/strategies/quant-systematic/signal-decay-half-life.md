---
title: "Signal Decay and Half-Life in Quantitative Finance"
description: "How quickly a predictive factor loses its edge over time and why measuring a signal's half-life determines appropriate holding periods and rebalancing cadence."
keywords:
  - signal decay half life quantitative finance
  - factor decay holding period
  - alpha decay over time
  - signal half-life measurement
image: /svg/strategies.svg
---

*In quantitative finance, every predictive signal has a lifespan. **Signal decay and half-life** measure how fast an edge erodes once identified. A momentum factor might be at full strength on day 1, half as powerful on day 30, and nearly useless by day 60. Understanding a signal's decay curve tells you the optimal holding period, rebalancing frequency, and whether the strategy is still viable after a few months of live trading.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Signal Decay and Half-Life — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for systematic strategies." />

<div class="wiki-infobox-caption">Half-life is the time at which a signal's predictive power decays to 50% of its initial strength.</div>

|   |   |
|---|---|
| **Half-life definition** | The holding period at which a signal retains 50% of its initial predictive edge |
| **Common ranges** | Mean reversion: 5–20 days; momentum: 20–90 days; value/quality: 90–365+ days |
| **How to measure** | Plot information coefficient or Sharpe ratio of a signal against holding days; fit exponential decay |
| **Implication** | Trade near half-life for optimal risk-reward; hold past half-life only if other signals justify it |
| **Why it matters** | Holding too long after decay destroys risk-adjusted returns; rebalancing too fast incurs unnecessary costs |

</aside>

## What Signal Decay Means

Suppose you identify a mean-reversion pattern: stocks that fall 5% in a day tend to bounce 1% the next day. On day 1 after the fall, this signal is fresh and strong—the predictive edge is real. But on day 5, some of that bounce has already happened, and the signal is weaker. On day 20, the stock has either recovered or continued falling, and the original signal is nearly dead.

This is signal decay: the statistical power of the factor to predict future returns diminishes as time passes. The causes vary. Mean reversion decays because prices revert quickly and the edge is exhausted. Momentum decays because eventually the driver of momentum (sentiment, earnings surprise, fund flows) loses impact. Value factors decay slowly because fundamental cheap-ness is a longer-horizon signal.

The **half-life** is the specific moment when the signal retains 50% of its initial predictive power. If a mean-reversion signal starts with a 2% expected alpha and has a 10-day half-life, it drops to 1% alpha at day 10, 0.5% at day 20, and so on, decaying exponentially.

## Measuring Half-Life

The standard method is to compute the **information coefficient** (IC, the correlation between the signal and forward returns) at different holding periods.

For a signal tested on 252 trading days:

1. On day 1: IC = 0.15 (strong signal; 15% correlation with next-day returns)
2. On day 5: IC = 0.10 (signal fades)
3. On day 10: IC = 0.075 (half of the original 0.15)
4. On day 20: IC = 0.04 (decay continues)
5. On day 60: IC = near 0 (signal is dead)

The half-life is day 10, because that is when IC dropped to 0.075 (50% of 0.15).

Alternatively, use [Sharpe ratio](/sharpe-ratio/) per holding period. A signal might have Sharpe 2.0 at a 5-day hold, Sharpe 1.0 at a 10-day hold, and Sharpe 0.3 at a 20-day hold. Again, the holding period where Sharpe drops to 50% of its peak is the half-life.

The decay often follows an exponential curve:

$$\text{Signal Strength}(t) = S_0 \times e^{-\lambda t}$$

Where $\lambda$ is the decay rate. Half-life is the time $t$ where $\text{Signal Strength}(t) = 0.5 \times S_0$, solving to $t = \frac{\ln(2)}{\lambda} \approx \frac{0.693}{\lambda}$.

Fitting this curve to empirical IC or Sharpe across multiple holding periods gives a clean decay model and a precise half-life.

## Half-Life and Optimal Holding Period

Intuitively, you want to hold a signal near its half-life, not much longer. Here is why:

**At half-life:** the signal is still substantial (50% of original power), and holding longer brings diminishing returns.

**Past half-life:** costs (commissions, slippage, market impact from rebalancing) mount, but signal power is fading. By holding past 2–3 half-lives, most of the edge is gone but all the [transaction costs](/transaction-cost-impact-on-quant-strategy/) are paid.

**Before half-life:** you exit early, leaving alpha on the table. But you also redeploy capital sooner, which can be an advantage if other signals emerge.

The precise optimum depends on [transaction cost impact](/transaction-cost-impact-on-quant-strategy/). A strategy with low costs (e.g., index rebalancing) can afford to hold near half-life. A high-turnover strategy with 20 basis points per round trip should exit even sooner.

**Example:** A mean-reversion signal has a 5-day half-life and round-trip cost of 10 basis points. The signal's edge on day 1 is 50 basis points. After costs, net alpha is 40 basis points. At day 5 (half-life), the signal edge is 25 basis points, net alpha is 15 basis points—still positive but declining. At day 10 (one decay cycle past half-life), the edge is 12.5 basis points, and costs have compounded (if you rebalance multiple times). The strategy is barely profitable. Smart rebalancing happens between day 2 and day 4, not day 5 or later.

## Signal Decay Across Asset Classes and Factors

**Mean reversion:** typically 3–15 days. Mean reversion is a short-horizon effect; prices overshoot and snap back fast.

**Momentum:** 20–90 days. Momentum persists longer because it reflects sustained sentiment or fund flows, but it eventually exhausts.

**Value and quality:** 90–365+ days. Cheap stocks stay cheap, and good businesses stay good, for many months. These signals decay slowly and can support longer holding periods.

**Earnings surprises:** 10–30 days. A stock rallies on a beat, but the initial pop fades and the stock drifts to its fair value over weeks.

**Volatility-based signals:** 5–20 days. High volatility regimes shift quickly; strategies based on vol mean reversion have short half-lives.

No universally "best" decay rate exists. The half-life tells you what you have, and you size the holding period to match.

## Portfolio Implications: Rebalancing Cadence

If your portfolio holds 50 distinct signals, each with a different half-life, you face a rebalancing puzzle. Some signals say "hold, still strong" while others say "decay is kicking in, reduce."

One approach: **rebalance to half-life levels.** Compute the half-life for each signal-asset pair empirically; rebalance on the schedule that matches the portfolio's median or weighted-average half-life.

Another: **stagger rebalancing.** Instead of rebalancing the entire portfolio on a fixed cadence (e.g., monthly), rebalance different sub-portfolios on different schedules matched to their decay profile. Momentum-heavy sub-portfolio rebalances monthly; value-heavy rebalances quarterly.

## Signal Decay and Market Regime

Signal decay is not constant across time. In calm markets with stable correlations, decay is predictable and measured. In crisis or high-volatility regimes, decay accelerates. A signal that has a 30-day half-life in normal times might have a 10-day half-life during a drawdown, because correlations break and relationships that held are suddenly scrambled.

A robust strategy either measures decay in multiple market regimes separately (and uses regime-dependent holding periods) or uses a conservative half-life estimate (based on crisis data) to be safe.

## Signal Decay vs. Lookback Period

These are related but distinct. [Lookback period](/lookback-period-selection-quant/) is the window of historical data used to *compute* the signal. Signal decay is how fast the signal *loses power* after it is generated.

A long lookback period (120 days) produces a smoother, slower-moving signal. That signal may have a 60-day half-life: it decays slowly but also responds slowly to changes. A short lookback (20 days) produces a responsive signal with maybe a 10-day half-life: it turns on and off quickly, but its edge vanishes fast.

The interplay is important. A 120-day lookback signal with a 10-day half-life is a mismatch: you are using three months of data to forecast something that has a 10-day edge. A 20-day lookback with a 60-day half-life is also odd: you are trusting a signal computed on old data (relative to its half-life). Align them roughly for coherence.

## See also

<div class="wiki-seealso">

### Closely related

- [Lookback Period Selection in Quantitative Strategies](/lookback-period-selection-quant/) — the historical window used to compute the signal
- [Transaction Cost Impact on Quant Strategy](/transaction-cost-impact-on-quant-strategy/) — how costs interact with holding period and rebalancing frequency
- [Momentum Investing](/momentum-investing/) — a factor with predictable decay
- Mean Reversion — short-lived signals that decay rapidly
- Information Coefficient — the metric used to measure signal strength and decay
- [Volatility Scaling for Position Sizing](/volatility-scaling-position-sizing/) — adapting size as regime changes affect signal validity

### Wider context

- Backtesting — testing signal decay over multiple periods and regimes
- [Alpha](/alpha/) — the edge that decays; half-life drives the economics
- Overfitting — ignoring decay in backtest leads to overestimating strategy returns
- [Risk-Adjusted Returns](/sharpe-ratio/) — Sharpe ratio falls as signals decay

</div>
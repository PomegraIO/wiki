---
title: "Parametric VaR vs Historical Simulation VaR"
description: "Compare parametric VaR and historical simulation VaR methods: normal distribution assumptions versus scenario replay, and when each method understates tail risk."
keywords:
  - parametric var vs historical simulation
  - var parametric method
  - historical simulation var
  - value at risk calculation methods
image: "/svg/ratios.svg"
---

*The **parametric VaR vs historical simulation** debate hinges on how you model market risk. Parametric VaR assumes returns follow a normal (bell-curve) distribution and calculates risk analytically; historical simulation replays past market outcomes to estimate future loss thresholds. Each method has blindspots: parametric VaR routinely underestimates tail risk if markets exhibit fat tails and skew, while historical simulation misses risks that did not occur in the historical period.*

<div class="wiki-hatnote">

This article compares two mainstream [Value-at-Risk](/value-at-risk/) methods. A third approach, Monte Carlo simulation, blends aspects of both.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Parametric vs Historical VaR — at a glance</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Each method trades simplicity for realism in different ways.</div>

|   |   |
|---|---|
| **Parametric VaR** | Assumes normal distribution; calculated via formula using volatility and correlation |
| **Historical Simulation** | Replays past returns; no distributional assumption |
| **Speed** | Parametric is fast; historical is slower for large datasets |
| **Memory requirement** | Parametric: low; historical: needs full historical return series |
| **Tail risk accuracy** | Parametric often understates if tails are fat; historical only captures past extremes |
| **Best for** | Parametric: liquid, normally-behaving assets; historical: stressed or non-normal markets |
| **Main blind spot** | Parametric: ignores skew and tail events; historical: missing risks not yet observed |

</aside>

## The parametric approach: the normal distribution shortcut

Parametric VaR assumes that asset returns follow a normal (Gaussian) distribution. Under this assumption, you can calculate a confidence-level loss threshold using just two inputs: volatility and correlation between assets.

For a single asset, the formula is:

```
VaR = Portfolio Value × (Expected Return - (Volatility × Z-score))
```

The Z-score corresponds to the confidence level. For a 95% confidence level (meaning a 5% chance of exceeding the loss), the Z-score is 1.645. For 99%, it's 2.326.

**Example**: A $10 million equity portfolio with 15% annual volatility. The 95%-confidence, one-day VaR is:

```
VaR = $10M × (0 - (0.15 × 1.645 / √252))
    = $10M × (- 0.00155)
    = -$15,500
```

This means there is a 5% chance that the portfolio will lose more than $15,500 in a single day.

Parametric VaR extends to multi-asset portfolios using a covariance matrix, which captures correlations between asset pairs. The portfolio volatility aggregates these correlations, and the rest follows.

**Why it's used**: Parametric VaR is computationally fast, requires little data, and is easy to explain to non-technical stakeholders. Regulators and risk committees often prefer it because the calculation is deterministic and auditable.

## The historical simulation approach: no assumptions, just replay

Historical simulation abandons distributional assumptions entirely. Instead, it replays historical returns and observes where losses would have landed.

**Procedure**:
1. Gather daily (or weekly) returns for the portfolio going back, say, 252 days (1 trading year) or 1,000 days (4 years).
2. Reweight historical returns using today's portfolio weights (or assume weights have not changed).
3. Sort the returns from best to worst.
4. For a 95% confidence level, the 5th percentile of returns is your VaR. For 99%, the 1st percentile.

**Example**: A $10 million portfolio with 252 days of historical returns. Sorting these returns from worst to best, the 5th worst day (5% of 252) showed a loss of $180,000. That is the 95% one-day VaR.

**Why it's used**: Historical simulation requires no assumptions about the shape of the return distribution. If markets regularly exhibit crashes, large reversals, or other non-normal behavior, historical simulation will capture those patterns directly. It is also intuitive: VaR is literally "the loss we have seen before at this level of frequency."

## The normal assumption problem: fat tails and skew

Real financial returns do not follow a perfect normal distribution. Markets exhibit **fat tails**—extreme losses and gains occur far more often than a bell curve predicts. They also exhibit **negative skew**: large downside moves are more frequent than large upside moves of the same magnitude.

For a normal distribution, a loss of -5 standard deviations occurs roughly once every 1.7 million days (not in anyone's career). Yet stock market history is peppered with days of -3 to -5 standard-deviation moves: the 1987 crash, the 2008 crisis, the 2020 March selloff, the 2024 flash crashes. These happen every 10–20 years, not every million days.

Parametric VaR, trusting the normal assumption, systematically underestimates these tail events. A risk manager using parametric VaR might believe a 99% confidence loss is $50 million when the true historical loss at that level was $80 million. This blind spot is dangerous during the crises that matter most.

## Historical simulation's constraint: data availability and structural change

Historical simulation has its own failure mode. If a loss *did not happen* in your historical window, the method will not see it.

A portfolio heavy in emerging market bonds might have 5 years of tranquil data with correlations near zero. Then a geopolitical shock hits, correlations spike to 0.9, and losses cascade. Historical simulation, having no memory of this regime, misses it entirely. Parametric VaR, using a forward-looking [volatility estimate](/historical-volatility/) (often updated daily), might catch it sooner, though only if volatility spiked beforehand.

Similarly, if your historical data spans only 2005–2007 (a period of low [volatility](/volatility-smile/) and strong credit conditions), your VaR estimate will be dangerously low because you missed the 2008 crash. Extending the history to include 2008–2009 fixes this, but then you might overstate risk for a post-2010 environment where leverage and structural hazards changed.

**Minimum data recommendation**: Most practitioners use at least 1 year (252 trading days) for daily VaR, though 3–5 years is preferable for stability. Even then, structural breaks (a regulatory change, a major mergers, a geopolitical event) can render old history less relevant.

## When parametric VaR underestimates (and historical does not)

Parametric VaR will systematically understate risk:

- **During periods of low measured volatility preceded by a crash.** Markets often exhibit low volatility for months before a sudden spike, and parametric VaR lags because it uses historical volatility. Historical simulation, conversely, includes the crashes from prior periods.
- **For option-heavy portfolios.** Options exhibit [convexity](/convexity/) and gamma risk. A portfolio long puts or short calls does not lose linearly; losses accelerate in extreme moves. Parametric VaR assumes linearity and misses this acceleration. Historical simulation can capture it if the extreme move happened before.
- **For portfolios with fat-tailed assets** (emerging market equities, high-yield bonds, leveraged positions). The normal distribution overstates the probability of moderate moves and understates the probability of extreme moves.

## When historical simulation lags

Historical simulation will underestimate risk:

- **If you use too short a history.** A portfolio of U.S. large-cap stocks with only 6 months of data might miss the tail risk that emerges over a 20-year horizon.
- **During unprecedented crises.** The 2020 pandemic was, by definition, unprecedented in modern portfolio history. Historical simulation could not anticipate it because it had never occurred.
- **For new assets or markets.** A cryptocurrency fund in 2015 had very little historical data. Historical simulation would miss tail risk from market maturation, regulatory shifts, or technical failures.
- **When volatility regimes shift.** If a portfolio's holdings change significantly, or if a market structure changes (e.g., a bond market becoming illiquid), old history is less relevant.

## Hybrid and refined approaches

Many risk teams use both methods and compare results. If parametric and historical VaR diverge widely (e.g., parametric says 99% VaR is $50M, historical says $70M), that gap is itself informative. It signals that the normal assumption is breaking down and tail risk is likely higher.

Some shops employ **stressed historical simulation**, which weights recent market crises more heavily or uses data from past volatile periods to estimate tail risk without assuming normality. Others use **EVT (extreme value theory)** to model tail behavior separately from the body of the distribution, blending the speed of parametric methods with the realism of historical observation.

Monte Carlo simulation is a third approach that generates thousands of synthetic return paths using specified distributions (which can include non-normal tails), then observes the loss outcomes. It combines flexibility with computational demand and is popular in large institutions.

## See also

<div class="wiki-seealso">

### Closely related

- [Value-at-Risk](/value-at-risk/) — the broader risk metric both methods estimate
- [Historical Volatility](/historical-volatility/) — a key input to parametric VaR
- [Implied Volatility](/implied-volatility/) — forward-looking volatility used in some parametric models
- [Tail Risk](/tail-risk/) — the extreme outcomes that both methods struggle to capture
- Monte Carlo Simulation — a simulation-based alternative to both methods

### Wider context

- [Market Risk](/market-risk/) — the category of risk VaR measures
- [Risk-Weighted Assets](/risk-weighted-assets/) — regulatory capital that uses VaR
- [Stress Testing](/stress-testing/) — another way to estimate tail risk
- [Volatility Smile](/volatility-smile/) — non-normal features of market returns
- [Operational Risk](/operational-risk/) — complementary to market risk in a risk framework

</div>

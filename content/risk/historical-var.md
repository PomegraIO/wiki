---
title: "Historical VaR"
description: "Historical value-at-risk is a method of calculating the loss threshold by sorting actual historical returns and selecting the percentile corresponding to the confidence level, without assuming any particular distribution."
keywords:
  - historical VaR
  - non-parametric VaR
  - empirical VaR
  - historical simulation
  - past returns
image: "https://picsum.photos/seed/historical-var/900/600"
---

*Historical value-at-risk (also called empirical or non-parametric VaR) is a method of estimating portfolio loss by examining actual historical returns, sorting them from worst to best, and selecting the percentile loss corresponding to the desired confidence level. It makes no assumptions about the distribution of returns.*

<div class="wiki-hatnote">

This entry covers historical VaR calculation. For alternative VaR methods, see [parametric-var](/parametric-var) and [monte-carlo-var](/monte-carlo-var); for the general [value-at-risk](/value-at-risk) concept.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Historical VaR — key facts</div>

<img src="https://picsum.photos/seed/historical-var/900/600" alt="A histogram of actual returns with a marked tail threshold" />

<div class="wiki-infobox-caption">Historical VaR is grounded in real market outcomes, not assumptions.</div>

|   |   |
|---|---|
| **Method** | Sort actual returns; select the percentile at confidence level |
| **Assumption** | None; uses empirical distribution of returns |
| **Calculation** | For 99% VaR on 1,000 days, use the worst 10th day |
| **Speed** | Fast; only requires sorting historical data |
| **Accuracy** | Reflects actual market behavior; no distributional assumptions |
| **Data requirement** | Requires sufficient historical data; extreme tails are sparse |
| **Key limitation** | Past may not represent future; misses new types of events |

</aside>

## How historical VaR works

**Step 1: Gather historical data.**
Collect daily portfolio returns for a sufficient period, e.g., the past 5 years (roughly 1,250 trading days).

**Step 2: Sort from worst to best.**
Order the returns from most negative (worst) to most positive (best).

**Step 3: Select the percentile.**
For 99% confidence, select the worst 1%. On 1,250 days, that is the worst 12-13 days.

**Step 4: Use that return as VaR.**
The loss on the 12th or 13th worst day becomes the 99% VaR estimate. If the 12th worst day was -3.5%, then the 1-day 99% VaR is -3.5%.

**Example:**
Worst 10 days from 1,250 days of data: -5%, -4.8%, -4.5%, -3.8%, -3.5%, -3.2%, -3.0%, -2.8%, -2.5%, -2.2%.

99% VaR (worst 1%, or day 12-13): approximately -3.2%.

## Advantages of historical VaR

**No distributional assumptions.** Unlike [parametric-var](/parametric-var), historical VaR does not assume returns follow a normal distribution. It uses actual market data.

**Reflects reality.** If the actual worst 1% of days averaged -4%, historical VaR captures that. Parametric VaR might say -2.28%, missing the true tail severity.

**Captures fat tails.** Because it is based on actual data, historical VaR naturally includes fat tails if they exist in the historical record.

**Simple to explain.** "The worst 1% of days in the past 5 years lost X%." This is intuitive and hard to argue with.

## Disadvantages of historical VaR

**Data sparsity in the tail.** For 99% VaR on 1,000 days, only 10 observations fall in the tail. Those 10 days determine the VaR. If one day was particularly bad (a crash), it dominates the estimate.

**Past may not represent future.** Stock market returns were different in the 1990s (lower volatility) than in 2008 (high volatility) or 2020 (pandemic spike). A historical VaR estimated from calm years underestimates risk when markets turn choppy.

**Misses new types of events.** If the past 5 years included no crises, historical VaR is too low for a period when crises occur. The 2008 financial crisis was partly a surprise because the historical VaR from the previous 10 years was too optimistic.

**Sensitive to data window.** Using 5 years of data gives one estimate; using 10 years gives another. The choice of window is somewhat arbitrary.

## When historical VaR works well

Historical VaR is reasonable for:
- **Backtesting.** You can test whether actual returns exceeded historical VaR estimates. If they did, the VaR model failed.
- **Cross-checking.** Compare historical VaR to [parametric-var](/parametric-var). If they differ significantly, investigate why. If historical is much worse, it suggests fat tails.
- **Regime-aware estimation.** If you estimate historical VaR separately for bull and bear markets, you capture regime differences.
- **Longer-term horizons.** Over longer periods (weeks or months), statistical stability improves and historical VaR is more reliable.

Historical VaR fails when:
- **Structures change.** If you use pre-2008 data to estimate VaR in 2009, the estimate is too low because the 2008 crisis changed volatility and correlations.
- **New instruments.** If you add a new asset class or derivative to a portfolio, historical data for the portfolio as a whole does not exist. You need [monte-carlo-var](/monte-carlo-var) or [parametric-var](/parametric-var).
- **Tail events are rare.** If the worst day in 1,000 days is -3%, but you want 99.9% VaR (worst 1 day in 1,000), you only have 1 data point to estimate from.

## Comparison: Parametric vs. Historical VaR

**Scenario:** A portfolio of US large-cap stocks over 1,000 trading days.

**Parametric VaR:**
- Mean daily return: 0.05%, Std dev: 1%.
- 99% VaR = 0.05% - 2.33 × 1% = -2.28%.

**Historical VaR:**
- Actual worst day: -5% (2008 crash).
- Actual 10th worst day: -3.2%.
- 99% VaR = -3.2%.

The historical VaR is worse (-3.2% vs. -2.28%), reflecting the fat tail captured by actual crash data.

## Practical use

Most risk managers use historical VaR as a cross-check:
1. Calculate [parametric-var](/parametric-var) for speed and consistency.
2. Calculate historical VaR to see if actual tail risks are worse than the normal distribution assumes.
3. If they diverge significantly, investigate. Use [stress-testing](/stress-testing) and [scenario-analysis](/scenario-analysis) to understand tail risks.

Modern frameworks like [Basel III](/capital-adequacy) emphasize multiple VaR methods, not just one.

## See also

<div class="wiki-seealso">

### Closely related

- [Value-at-risk](/value-at-risk) — the VaR concept itself
- [Parametric-var](/parametric-var) — alternative method using distributional assumptions
- [Monte-carlo-var](/monte-carlo-var) — simulation-based VaR
- [Expected-shortfall](/expected-shortfall) — measures tail severity
- [Backtesting](/value-at-risk) — checks whether VaR estimates are accurate

### Strengths and weaknesses

- [Fat-tail-risk](/fat-tail-risk) — historical VaR captures this; parametric does not
- [Model-risk](/model-risk) — all VaR models depend on assumptions
- [Parameter-risk](/parameter-risk) — estimates are uncertain
- [Tail-risk](/tail-risk) — historical VaR better at capturing
- [Stress-testing](/stress-testing) — complements VaR methods

</div>

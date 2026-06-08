---
title: "GDP Seasonal Adjustment Explained"
description: "How is GDP seasonally adjusted? Statisticians remove predictable seasonal patterns from quarterly figures to reveal underlying economic trends."
keywords:
  - how is gdp seasonally adjusted
  - seasonal adjustment gdp
  - removing seasonal patterns
  - quarterly gdp data
image: /svg/macro.svg
---

*Gross domestic product data arrives in two forms: raw (or "not seasonally adjusted") and **seasonally adjusted**. The difference is crucial. Raw quarterly GDP includes predictable swings — retail sales spike in November and December, agriculture peaks after harvest, construction slows in winter — that repeat every year. Statisticians remove these recurring patterns to expose what economists actually care about: whether the economy is truly accelerating or contracting, or whether the change is just the calendar talking. The adjustment is a mechanical technique, not a forecast, and the adjustments themselves are published so readers can see what was removed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Seasonal Adjustment — key facts</div>

<img src="/svg/macro.svg" alt="An abstract editorial mark for macroeconomics." />

<div class="wiki-infobox-caption">A statistical filter that isolates trend from predictable calendar patterns in quarterly data.</div>

|   |   |
|---|---|
| **Purpose** | Extract underlying economic momentum from recurring seasonal swings |
| **Data used** | Typically 10+ years of historical data to estimate seasonal patterns |
| **Method** | X-13ARIMA-SEATS (U.S. Bureau of Economic Analysis) |
| **Adjustment factors** | Published separately; readers can reverse them |
| **Timing** | Applied to retail, employment, production, and GDP data |
| **Error risk** | Estimates break down during unusual years or structural shifts |

</aside>

## Why raw data needs adjustment

Consider a simple example: an economy with no underlying growth, where output stays flat year after year at $1 trillion. Yet raw quarterly figures would show Q4 always higher than Q3 (holiday spending, year-end inventory builds), and Q1 always lower than Q4 (post-holiday contraction, bad weather). The variation is purely seasonal — the calendar, not economic health.

If a policymaker or investor saw Q4 data jump from $1.0 trillion to $1.05 trillion, they might mistake it for real growth. Seasonal adjustment erases that optical illusion by dividing out the predictable seasonal factor. Q4's upward bump is expected, so it gets removed. What remains is the trend: flat, as it truly is.

Conversely, if actual growth occurs *during* a normally strong season — say retail sales surge even more than usual in November — the seasonal adjustment will leave some of that extra strength visible, because it exceeds the historical seasonal norm.

The benefit is clarity. With seasonal adjustment, a quarter-on-quarter change in GDP almost always signals a real shift in economic momentum, not a calendar artifact. Without it, forecasters and investors must do the filtering themselves, which breeds noise and disagreement.

## How the adjustment is estimated

Statisticians use at least a decade of historical quarterly data to estimate the seasonal pattern. For each quarter (Q1, Q2, Q3, Q4) and each component of GDP — personal consumption, business investment, government spending, net exports — they calculate an average seasonal factor.

A worked example: suppose the Bureau of Economic Analysis has 40 years of real consumption data. It groups all Q4 figures (Christmas and holiday spending boost), all Q3 figures (back-to-school, summer travel), and so on. After removing long-term trend and cyclical movements, it calculates what fraction of typical annual consumption occurs in each quarter.

If the pattern shows that Q4 normally accounts for 28% of annual consumption (2 percentage points above the "fair share" of 25%), the seasonal factor for Q4 is 1.02. When a new Q4 figure is released at, say, $3.0 trillion, the seasonal adjustment divides it by 1.02 to get a seasonally adjusted figure of roughly $2.94 trillion — the Q4 number stripped of its predictable seasonal boost.

This is applied separately to each subcomponent, then aggregated upward. The adjustment is transparent: the Bureau publishes both the raw and adjusted figures, plus the factors themselves, so economists can reconstruct the calculation.

## The method: X-13ARIMA-SEATS

The U.S. Bureau of Economic Analysis uses a statistical algorithm called **X-13ARIMA-SEATS**, descended from earlier Census Bureau methods. The algorithm works in layers:

First, it estimates the "trend-cycle" component — the long-term direction and business-cycle swings that repeat over years, not seasons. Second, it estimates the seasonal component — patterns that repeat quarterly, month to month, or within a quarter. Third, it estimates irregular fluctuations — one-off shocks or measurement noise.

The algorithm is iterative: as the trend estimate improves, the seasonal estimate becomes more precise. Outliers (unusual years) are flagged and can be down-weighted, so a severe winter or a strike that temporarily halted production does not distort the baseline seasonal pattern.

The output is a seasonally adjusted series that, in principle, removes recurring patterns while preserving real economic information.

## Challenges and limitations

Seasonal adjustment works well during normal years, when the seasonal pattern is stable. It breaks down when the economy undergoes a structural shift. For example, the rise of e-commerce reduced the seasonal amplitude of retail sales — the November-December spike is now smaller relative to the rest of the year — so seasonal factors estimated from 1990s data become stale. The Bureau periodically re-estimates factors, but there is always a lag.

The 2020 COVID-19 pandemic exposed a deeper problem. Lockdowns obliterated normal seasonal patterns: retail collapsed in Q2 2020 in an unprecedented way, and the seasonal adjustment algorithm, confronted with a year outside its training data, struggled. Many economists switched to looking at longer rolling averages or raw changes to avoid being misled by stale adjustment factors.

A second risk is **revision**. When a year completes, statisticians can look back and see whether their seasonal estimate was accurate. Earlier quarters are often revised, sometimes substantially. A growth rate that seemed robust in the preliminary report can weaken after revisions as seasonal factors are fine-tuned.

## Interpreting adjusted vs. raw figures

News releases always report seasonally adjusted figures prominently — that is the headline number for GDP growth, employment changes, and industrial production. Raw figures are listed below or in appendices. When comparing one quarter to the last, always use seasonally adjusted data; raw comparisons are misleading.

When comparing one quarter to the same quarter a year ago (year-over-year), seasonal adjustment matters less, because both quarters carry the same seasonal pattern. Year-over-year growth can be calculated from raw data with reasonable accuracy. But quarter-on-quarter growth — the standard measure of acceleration or deceleration — requires seasonal adjustment to be meaningful.

## What seasonal adjustment reveals

Once seasonal factors are removed, the pattern that emerges shows how the economy is actually behaving. A strong Q3 that beats the previous Q2 by more than the seasonal factor would typically expect means real momentum; a Q3 that rises within its normal seasonal range suggests stability or modest growth; a Q3 that underperforms its seasonal norm signals weakness.

The same logic applies to labor markets, retail sales, and production. Seasonal adjustment is not a forecast or an opinion — it is a filter that isolates trend from calendar noise, letting the data speak more clearly about what is genuinely happening.

## See also

<div class="wiki-seealso">

### Closely related

- [Gross domestic product](/gross-domestic-product/) — the primary economic measure that uses seasonal adjustment in its quarterly releases
- Quarterly GDP release — how the Bureau of Economic Analysis publishes adjusted and unadjusted figures
- [Business cycle](/business-cycle/) — recurring expansions and contractions that seasonal adjustment distinguishes from seasonal swings
- [Leading indicator](/leading-indicator/) — economic signals, many seasonally adjusted, that forecast near-term growth

### Wider context

- Economic data revision — why published figures change as more information arrives
- [Federal Reserve](/federal-reserve/) — the central bank that relies on seasonally adjusted data for monetary policy decisions
- [Fiscal multiplier](/fiscal-multiplier/) — how government spending impacts GDP, a calculation that depends on clean, adjusted data
- [Recession](/recession/) — typically defined by consecutive quarters of negative adjusted GDP growth

</div>

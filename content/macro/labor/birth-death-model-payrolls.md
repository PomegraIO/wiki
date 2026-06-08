---
title: "Birth-Death Model in Nonfarm Payrolls"
description: "Birth-death model nonfarm payrolls explains the BLS statistical adjustment for unobserved business creation and closure that can distort near-term employment readings."
keywords:
  - birth death model
  - nonfarm payrolls
  - business births
  - business deaths
  - bls adjustment
  - employment data
  - statistical smoothing
---

*The **birth-death model** is a statistical technique used by the U.S. Bureau of Labor Statistics (BLS) to estimate job creation from new businesses and job loss from business closures that have not yet been observed in the monthly payrolls survey. Because actual data arrives slowly, the BLS predicts what the unobserved sectors should contribute, which can materially misestimate short-term employment trends.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Birth-Death Model in Nonfarm Payrolls — Key Facts</div>

<img src="/svg/macro.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">An essential but imperfect mathematical fill-in for rapid business entry and exit.</div>

|   |   |
|---|---|
| **Purpose** | Estimate jobs from new businesses (births) and closures (deaths) before actual data arrives |
| **Data lag** | Actual business formation data arrives 6–12 months late; model must forecast near-term |
| **Annual adjustment** | Benchmark revision each August corrects the model's year-long accumulated error |
| **Typical annual error** | USD 50K–200K net jobs overestimated or underestimated before revision |
| **Seasonal adjustment** | Birth-death estimates are seasonally adjusted, compounding forecast uncertainty |
| **Scope** | Primarily affects small business sector; less impact on large corporate payrolls |

</aside>

## Why the Model Is Needed

The BLS conducts the Current Employment Statistics (CES) survey, which is based on a large sample of business establishments—roughly 140,000 worksites across all sectors. These establishments report their total employment monthly. However, new businesses open and old businesses close every month, and not all of these transitions are captured in the survey immediately.

When a new restaurant or construction firm opens, it may take weeks or months to be identified, contacted, and added to the survey sample. Similarly, when a small business closes, it may take time for the BLS to recognize that the establishment has ceased operations. This lag creates a gap: the survey captures employment changes at existing businesses, but misses the net employment effect of business formation and failure.

For policy and market decisions, a one- or two-month lag in capturing business dynamism is unacceptable. The Federal Reserve needs current payrolls data to set monetary policy; investors use employment trends to forecast economic growth. The BLS therefore uses the birth-death model to estimate the "missing" jobs from births and deaths, producing an estimate of total nonfarm payroll employment each month.

## How the Model Works

The birth-death model is built on historical data: over many decades, the BLS has observed correlations between:

1. **Economic conditions** (GDP growth, unemployment rate, industry trends)
2. **Business births** (new establishments and their initial employment)
3. **Business deaths** (closures and job loss)

The model fits a regression or time-series model to historical business formation and failure rates, stratified by industry and size. It then projects forward based on recent economic conditions.

For example, during periods of strong growth, the model predicts higher business formation and lower failure rates. During recessions, the model predicts fewer births and higher death rates. The model then estimates the net job contribution from these births and deaths, which is added to the month-to-month change in employment at surveyed establishments to produce the headline nonfarm payroll figure.

The adjustment is often sizable. In a typical month, the birth-death adjustment might add or subtract 50,000–100,000 jobs from the survey's direct count, representing 10–25% of the monthly employment change.

## When the Model Goes Wrong

The model works well on average over a full year, but can be seriously wrong month-to-month or even over several consecutive months.

**Recession entry:** When an economy is sliding into recession, business failure typically accelerates. However, the failure happens gradually: businesses close over weeks or months as demand dries up. The birth-death model, trained on historical patterns, may underestimate the speed of business death, implying that payrolls remain stronger than they actually are. Conversely, if recession arrives suddenly (as in March 2020 during the COVID-19 pandemic), the model has no historical precedent, and its forecast is nearly useless.

**Boom periods:** Similarly, during strong expansions, new business formation can surge faster than the model predicts. This leads to undercounting of job growth in near-term payroll reports, with a revision upward months later.

**Sector-specific shocks:** The model is stratified by industry, but shocks to specific sectors (energy price collapses, tech layoffs, retail restructuring) can outpace the historical patterns embedded in the model. The model may miss rapid job loss in a sector that is experiencing structural decline.

## The Benchmark Revision

Every August, the BLS releases a **benchmark revision**, which compares the model's estimates over the prior 12 months to actual employment data from a more comprehensive, tax-record-based Census count. This revision reveals how far the birth-death model drifted from reality over the year.

In strong economic environments, the benchmark revision typically shows that the model *undercounted* business births and job creation, requiring an upward revision to prior months' payrolls. In weak environments or during recessions, the model often *overcounted* births or undercounted deaths, requiring downward revisions.

For example, in August 2022, the BLS revised down the prior 12 months of payroll employment by 818,000 jobs—a massive adjustment revealing that the birth-death model had significantly overestimated job creation during a period of economic weakness and incipient labor market cooling.

## Controversy and Opacity

The birth-death adjustment has drawn criticism for three reasons:

1. **Opaqueness:** The BLS publishes the total adjustment each month, but the detailed methodology and assumptions underlying the model are less transparent than many economists would prefer. The model is complex, and its inner workings are not fully audited or debated by the research community in real time.

2. **Policy relevance:** Monetary policy decisions (interest rate moves by the Federal Reserve) are partly based on payroll reports. If the headline figure is materially distorted by a misspecified birth-death model, the Fed may make policy errors. For instance, if the model is consistently overestimating job growth during a slowdown, the Fed might hold rates steady when it should be cutting, or vice versa.

3. **Ex-post revision:** The fact that payroll figures are later revised by tens of thousands or hundreds of thousands of jobs undermines their credibility as a "hard" economic statistic. Market participants who trade or invest based on the initial report only to see it revised months later face a form of information asymmetry.

Defenders of the model note that:

- No perfect real-time alternative exists. The Census employment data used for benchmarking also arrives late and is subject to revision.
- The model, despite its flaws, is better than publishing only surveyed establishments and ignoring births and deaths entirely.
- The annual benchmark revision eventually captures reality; the distortion is temporary.
- Investors and policymakers can and do discount the headline payroll number by accounting for typical revision magnitudes.

## See also

<div class="wiki-seealso">

### Closely related

- [Unemployment Rate](/unemployment-rate/) — complementary labor market statistic, derived independently
- [Business Cycle](/business-cycle/) — broader context for business formation and failure patterns
- [Leading Indicator](/leading-indicator/) — category of forward-looking economic signals including employment trends
- [Recession](/recession/) — period when business deaths accelerate and the model often fails

### Wider context

- [Gross Domestic Product](/gross-domestic-product/) — the ultimate outcome variable that economic statistics attempt to track
- [Federal Reserve](/federal-reserve/) — the central bank that uses payroll data for policy decisions
- [Labor Productivity](/labor-productivity/) — related labor market metric tracking output per worker
- [Natural Rate of Unemployment](/natural-rate-of-unemployment/) — long-run equilibrium employment concept
- Macroeconomic Policy — decision-making context relying on payroll data

</div>

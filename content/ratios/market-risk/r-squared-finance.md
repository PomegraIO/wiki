---
title: "R-Squared"
description: "The percentage of a portfolio's volatility explained by its benchmark, revealing how much of its performance comes from systematic versus idiosyncratic risk."
keywords:
  - r-squared
  - beta
  - alpha
  - benchmark comparison
  - portfolio analysis
  - systematic risk
image: "/svg/ratios.svg"
---

*[R-squared](/r-squared-finance/) measures the proportion of a portfolio's variance that moves in tandem with its benchmark. A high R-squared (above 0.8) signals that most of the fund's swings track the market; a low R-squared (below 0.6) means its returns dance to its own drum, making [beta](/beta/) and [alpha](/alpha/) harder to interpret.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">R-Squared — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Expressed as a decimal (0–1) or percentage (0–100%); higher readings mean benchmark-hugging.</div>

|   |   |
|---|---|
| **What it is** | The coefficient of determination; the square of the correlation coefficient |
| **Formula** | Typically: 1 − (sum of squared residuals / total sum of squares) |
| **Range** | 0 to 1 (or 0% to 100%) |
| **Interpretation** | 0.90 = 90% of portfolio moves explained by benchmark |
| **Use in practice** | Validates [beta](/beta/) reliability; context for [alpha](/alpha/) significance |
| **Limit** | Does not measure absolute return quality or risk-adjusted performance |

</aside>

## The core idea: what portion of the fund actually follows the index?

Picture a fund manager steering a portfolio through a market cycle. Some of that manager's decisions—or the fund's construction—force the portfolio to move closely with the [S&P 500](/sp-500-index/) or whatever [benchmark](/beta/) applies. But other decisions carve out independent moves: a bet on a particular sector, a timing call, or simply a smaller asset base that skips certain holdings.

R-squared quantifies that split. If the [S&P 500](/sp-500-index/) rises 20% and the fund rises 18%, and if movements with the index explain 92% of the fund's volatility over the period, its R-squared is 0.92. The remaining 8% of variance—the fund's own idiosyncratic wobbles—comes from choices unique to the portfolio.

This matters because [beta](/beta/) and [alpha](/alpha/) only make sense if R-squared is high enough. If you're comparing a fund to a benchmark using beta as the lever, but the fund barely moves with that benchmark, the beta number becomes almost fictional.

## Why R-squared is a credibility meter for beta and alpha

Imagine two funds, each posting a [beta](/beta/) of 1.1 relative to the [S&P 500](/sp-500-index/). One has an R-squared of 0.95; the other, 0.45.

The first fund—tightly bound to the index—probably earned that 1.1 beta through deliberate leverage or overweight positioning in high-beta stocks. You can trust the number.

The second fund's 1.1 reading is almost meaningless. That fund swings all over the place, guided more by its own bets than by index movements. Its correlation to the benchmark is too weak for beta to describe the relationship. The number could easily flip depending on the time period or market regime you measure.

Practitioners often use 0.75 as a rough threshold: above it, the fund is benchmark-like enough that beta and [alpha](/alpha/) deserve attention. Below it, you're dealing with something closer to a satellite portfolio or a specialist strategy, where comparisons to a broad index become less relevant.

## The mechanics: how R-squared gets calculated

R-squared is the square of the correlation coefficient between portfolio returns and benchmark returns. When you plot the fund's monthly returns against the index's monthly returns, R-squared tells you how tightly those dots cluster around the fitted line. A perfect line (R² = 1.0) would mean every return pair lands exactly on the prediction; a cloud scattered across the chart (R² = 0.3) means the benchmark explains almost nothing.

The formula boils down to comparing the sum of squared deviations from the predicted return (based on the benchmark relationship) to the total variance in the fund's actual returns. The closer those predicted and actual returns track, the higher R-squared climbs.

The calculation requires a full period of returns—typically three to five years of monthly data, sometimes daily. Shorter windows produce noisier R-squared readings; longer windows smooth out temporary divergences and reveal true structural alignment.

## When a low R-squared is a feature, not a flaw

A low R-squared can signal poor fund management, but it can also mean the portfolio is doing exactly what it was built to do.

A [hedge fund](/hedge-fund/) that uses [short-selling](/short-selling/) alongside longs, or one that shifts dynamically between sectors and geographies, will have low R-squared relative to the [S&P 500](/sp-500-index/). So will a [bond fund](/bond/) benchmarked to an equity index (a category error, but it happens in institutional reporting). So will a concentrated emerging-markets strategy or a narrowly focused [thematic ETF](/thematic-etf/).

The trap lies in misinterpreting what low R-squared means. Some investors see it and assume the manager is adding alpha; others assume the manager is just taking uncompensated risk. The truth depends on whether the fund's strategy—and its documented [beta](/beta/) and [alpha](/alpha/)—actually explain the independent movements. A high-conviction value investor with low R-squared to the [S&P 500](/sp-500-index/) might be delivering strong risk-adjusted returns precisely because she's making different bets.

## The limits of R-squared as a quality measure

R-squared reveals nothing about whether a fund has beaten its benchmark or preserved capital in a downturn. A fund could have an R-squared of 0.95 and still deliver negative [alpha](/alpha/) year after year—it just does so predictably.

Similarly, R-squared doesn't reflect [concentration risk](/concentration-risk/), [volatility](/market-risk/), or [downside protection](/down-capture-ratio/). A fund might track the index closely (high R²) yet take on idiosyncratic volatility through large positions that happen to move with the market on average.

For a full picture, pair R-squared with [beta](/beta/) to understand sensitivity, [alpha](/alpha/) to assess outperformance, and metrics like [down-capture ratio](/down-capture-ratio/) or [Modigliani risk-adjusted performance](/modigliani-risk-adjusted-performance/) to weigh returns against actual risk borne. R-squared is the first question—"Is this fund even trying to track the benchmark?"—not the last.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — the fund's sensitivity to benchmark moves, only meaningful if R-squared is high
- [Alpha](/alpha/) — the risk-adjusted outperformance; harder to validate when R-squared is low
- [Down-Capture Ratio](/down-capture-ratio/) — how much the fund participates in benchmark downturns
- [Up-Capture Ratio](/up-capture-ratio/) — how much the fund captures benchmark rallies
- [Modigliani Risk-Adjusted Performance](/modigliani-risk-adjusted-performance/) — rescales any portfolio to benchmark volatility for direct comparison
- [Volatility smile](/volatility-smile/) — pattern in option implied volatility; unrelated to R-squared but often analyzed alongside beta

### Wider context

- [Market risk](/market-risk/) — systematic risk that affects all securities; the core of benchmark-relative analysis
- [Idiosyncratic risk](/idiosyncratic-risk/) — portfolio-specific volatility not explained by the benchmark
- [Actively managed fund](/actively-managed-fund/) — typically has lower R-squared than index funds
- [Index fund](/index-fund/) — engineered for near-perfect R-squared to its benchmark
- [Factor investing](/factor-investing/) — uses R-squared to isolate factor contributions to returns
- [Concentration risk](/concentration-risk/) — idiosyncratic risk that high R-squared does not capture

</div>

---
title: "Ulcer Index"
description: "A risk metric that measures the depth and duration of drawdowns, penalizing prolonged periods below previous highs rather than just the magnitude of the largest loss."
keywords:
  - ulcer index
  - downside risk
  - drawdown duration
  - volatility alternative
  - risk-adjusted return
image: "/svg/ratios.svg"
---

*The **Ulcer Index** blends the severity and length of underwater periods into a single score, capturing a dimension of pain that traditional [volatility](/volatility-smile/) overlooks. Where standard deviation treats all fluctuations equally, the Ulcer Index hammers funds that stay depressed—rewarding managers who recover quickly and punishing those who linger below previous highs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ulcer Index — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for risk metrics." />

<div class="wiki-infobox-caption">Duration and depth of losses combined into a single metric.</div>

|   |   |
|---|---|
| **What it is** | A [volatility](/volatility-smile/) alternative that squares the percentage shortfall below a rolling peak, then takes the square root of the average. |
| **Formula** | UI = √(Σ(max drawdown %)² / n) |
| **Range** | 0 to unbounded; lower is better. |
| **Also called** | Martin Ulcer Index, after inventor Peter Martin. |
| **Key insight** | Penalizes underwater duration more than single-day crashes. |
| **Counterpart ratio** | [Calmar Ratio](/calmar-ratio/) or Sharpe Ratio for return normalisation. |

</aside>

## How it captures pain that volatility misses

A fund that drops 50% in one session then recovers instantly has the same standard deviation (in hindsight) as one that drifts sideways, losing 50% over two years without regaining lost ground. The Ulcer Index hates the second scenario. It measures the *percentage below the previous peak* at each point—draw a curve of cumulative returns, then for every dip below the running high-water mark, square that percentage gap and accumulate it. The larger the gap and the longer it persists, the bigger the penalty.

This means a recovery, even a slow one, immediately improves the score. A fund underwater for 18 months, then surging back in week 19, looks dramatically better on Ulcer Index than on raw volatility. For investors who feel genuine financial stress during drawdowns—not just abstract concern about standard deviation—this metric aligns better with lived experience.

## Calculating the index step-by-step

Let's say a fund's monthly returns are +3%, –2%, +1%, –5%, –3%, +2%. You calculate the rolling high (peak return at each month), then measure how far below peak each new low falls.

Month 1: Peak = 3%, current = 3%, drawdown = 0%.
Month 2: Peak = 3%, current = 1%, drawdown = (1 – 3) / 3 = –66.7%.
Month 3: Peak = 3%, current = 2%, drawdown = (2 – 3) / 3 = –33.3%.
Month 4: Peak = 3%, current = –3%, drawdown = (–3 – 3) / 3 = –200%.
Month 5: Peak = 3%, current = –6%, drawdown = (–6 – 3) / 3 = –300%.
Month 6: Peak = 3%, current = –4%, drawdown = (–4 – 3) / 3 = –233.3%.

Square each: 0, 4,445, 1,111, 40,000, 90,000, 54,444.

Take the mean and square root: √(189,999 / 6) ≈ √31,667 ≈ 178.

This fund's Ulcer Index is roughly 178. Concrete, actionable, and sensitive to both the depth of losses and how long they lasted.

## Why duration matters more than you'd think

Professional investors often gloss over the difference between a "flash crash" and a structural bear market. A 40% plunge that recovers within months stings but doesn't cripple. A 30% decline that takes three years to repair corrodes confidence, increases forced selling, and demoralizes clients. The Ulcer Index reorders that intuition into mathematics: staying underwater is more costly, per unit of loss, than getting there quickly.

This becomes especially relevant for long-term [investment funds](/growth-fund/), pension portfolios, and individuals in drawdown (spending from retirement accounts). A fund that bounces back cuts future forced selling; one that stays flat keeps you in a bind.

## Interpreting scores: what 50 means

An Ulcer Index of 50 typically signals a moderately painful fund—long stretches 5–10% off peak, or several 15–20% drawdowns with slow recovery. An index below 15 suggests a mostly smooth ride, rare trips underwater, and quick bounces. Above 100, you're looking at either persistent bear market conditions or a fund that haemorrhages capital and takes forever to recover.

Direct comparison: a Sharpe Ratio of 0.8 is decent (1 is very good); an Ulcer Index of 30 is respectable, 10 is excellent. They measure different things—one normalises return by all volatility, the other punishes duration—so use both.

## Strengths and blind spots

The Ulcer Index elegantly captures tail-risk persistence and recovery lag. It favours active managers who limit drawdown depth *and* bounce back fast—two real skills. Passive [index funds](/index-fund/), especially broad stock indices, can have paradoxically low Ulcer scores during bull markets because they don't drop deeply relative to their benchmark (there is no separate "peak" to measure against).

The main weakness: a fund that crashes 80% in month one, then drifts higher for years scores far better on Ulcer Index than on [volatility](/volatility-smile/) or [value-at-risk](/value-at-risk/) metrics. Some investors care most about *how likely* a catastrophic loss is (tail risk), not how long recovery takes. Ulcer Index answers a different question: given that you're underwater, how much does it hurt to stay there?

## See also

<div class="wiki-seealso">

### Closely related

- [Calmar Ratio](/calmar-ratio/) — return normalised by maximum drawdown; Ulcer Index's conceptual cousin for measuring pain.
- Sharpe Ratio — return per unit of volatility; broader but treats upside swings the same as downside.
- [Sortino Ratio](/sortino-ratio/) — penalises only downside [volatility](/volatility-smile/), not upside.
- [Maximum Drawdown](/maximum-drawdown/) — the single biggest peak-to-trough loss; Ulcer aggregates all underwater periods.
- [Volatility Smile](/volatility-smile/) — how option prices embed tail risk; related to the limits of simple standard deviation.
- [Beta](/beta/) — systematic market sensitivity; independent of drawdown duration.
- [Value at Risk](/value-at-risk/) — probability of loss at a given confidence level; different focus than recovery time.

### Wider context

- Risk-Adjusted Return — the family of metrics normalising performance by risk taken.
- [Fund Prospectus](/fund-prospectus/) — where risk metrics are disclosed to investors.
- [Hedge Fund](/hedge-fund/) — where Ulcer Index is commonly used to compare risk-adjusted skill.

</div>

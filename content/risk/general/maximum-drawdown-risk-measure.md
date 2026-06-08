---
title: "Maximum Drawdown as a Risk Measure"
description: "Understand maximum drawdown as a risk metric: how it measures peak-to-trough losses, what it reveals about downside risk that volatility misses, and how investors use it for position sizing."
keywords:
  - maximum drawdown risk measure
  - drawdown calculation
  - peak to trough loss
  - volatility vs drawdown
  - portfolio risk assessment
---

*A **maximum drawdown** is the largest peak-to-trough loss a portfolio or investment has suffered within a given period—the percentage decline from the highest value ever reached down to the lowest point afterward. Unlike volatility, which measures how much returns jitter around an average, maximum drawdown captures the actual magnitude of the worst pain a real investor experienced. It tells you: if you had bought at the worst possible moment and held through the worst subsequent decline, how much of your money would have been gone. This is the number that determines whether you have the stomach to own something.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maximum Drawdown — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">Drawdown is the hardship of loss; volatility is the frequency of jitter.</div>

|   |   |
|---|---|
| **Definition** | Peak value minus trough value, expressed as a percentage of peak |
| **Formula** | (Trough − Peak) ÷ Peak × 100% |
| **Timeframe** | Calculated over any historical period; can be rolling or annual |
| **How often measured** | During recoveries; multi-year drawdowns are rare for diversified portfolios |
| **Typical stock market drawdown** | 20–35% in a bear market; 40–60% in severe recessions |
| **Typical bond portfolio drawdown** | 5–20%, depending on duration and credit quality |
| **Typical balanced portfolio drawdown** | 15–30%, depending on allocation |
| **Why it matters** | Reveals behavioral risk: can investors actually stay invested? |
| **Distinction from volatility** | Low-volatility assets can have large drawdowns; high-volatility assets may recover quickly |

</aside>

## How Maximum Drawdown Is Calculated

Start with a portfolio value over time. Find the peak—the highest point the portfolio reached. Then identify every subsequent valley. The largest percentage decline from a peak to any trough below it is the maximum drawdown.

A concrete example: a portfolio reaches $100,000 on January 1. It climbs to $120,000 in March (new peak). Then the market crashes, and it falls to $80,000 in April. The drawdown from the $120,000 peak to the $80,000 trough is ($80,000 − $120,000) / $120,000 = −33.3%.

Later the portfolio recovers to $110,000 in June, then declines to $90,000 by August. This drawdown is only −18.2%. The maximum drawdown for the period is the larger of the two: −33.3%.

Crucially, a drawdown is not reversed by a recovery. The portfolio can return to $150,000, fully surpassing the old peak. The historical maximum drawdown remains −33.3%, locked in as a fact of what occurred.

## Why Drawdown Matters More Than It Seems

Volatility, the standard risk metric taught in textbooks, measures dispersion of returns around an average. A portfolio with 10% annual volatility bounces up and down by roughly 10% on an annualized basis—a normal, manageable fluctuation.

But volatility says nothing about the *magnitude of a drawdown*. A series of small, frequent losses can produce high volatility yet low drawdown. A long, grinding, one-directional decline produces low volatility but massive drawdown (because returns are consistently negative, not dispersed).

More importantly, drawdown is what investors actually *feel*. Losing 40% of your net worth is a fundamentally different experience from a 40% volatility. The latter is abstract; the former is real pain, and it tests commitment. How many investors can hold a bond fund that drops 20%? How many can hold a stock fund that drops 50%?

[Volatility](/historical-volatility/) also ignores *time in recovery*. A portfolio that drops 50% and recovers in three months has the same maximum drawdown as one that takes ten years to recover, even though the emotional and opportunity costs are vastly different.

## Drawdown vs Volatility: A Worked Example

Consider two portfolios over 10 years:

**Portfolio A** (High volatility, moderate drawdown):
- Annual returns: +15%, −8%, +22%, −5%, +18%, −10%, +12%, +19%, −7%, +14%
- Annualized volatility: 12.5%
- Maximum drawdown: −10% (from the peak to the next trough)

**Portfolio B** (Low volatility, large drawdown):
- Annual returns: +3%, +2%, +4%, −18%, −22%, −15%, +5%, +4%, +3%, +4%
- Annualized volatility: 10.2%
- Maximum drawdown: −50% (cumulative over the three-year downturn from peak to trough)

Portfolio B looks less risky by volatility alone (10.2% vs 12.5%), yet an investor holding it through years 3–5 lost half their money. The maximum drawdown is the better predictor of whether that investor can live with the investment.

## Drawdown Duration and Psychological Break-Even

Maximum drawdown answers: "How bad does it get?" A secondary question, often more important to behavioral investors, is: "How long does recovery take?"

Stocks have historically entered drawdowns and recovered to new highs within 3–5 years on average. Bonds recover faster (6–18 months). Illiquid assets or those requiring structural recovery (office buildings during an exodus to remote work) can take a decade.

An investor facing a 30% drawdown in stocks might hold if she expects recovery in two years. The same 30% drawdown in real estate, if recovery looks like five years, might break her commitment and force a liquidation at the worst moment.

This is why [portfolio diversification](/diversification/) and [asset allocation](/asset-allocation/) matter. A 60/40 stocks-bonds portfolio might experience drawdowns of 15–25%, with recoveries in 2–3 years. An all-stock portfolio might see 35–50% drawdowns with 3–5 year recoveries. A 40/60 allocation might see only 10–15% drawdowns, but with higher drag on long-term returns.

## Using Drawdown for Position Sizing

Sophisticated traders and institutions use maximum drawdown to size positions. If a given strategy has a 25% historical maximum drawdown, and you have $1 million in capital you're willing to risk entirely, you can allocate $4 million to the strategy (because at worst you lose 25% × $4M = $1M). If you can only afford to lose $500,000, you size down to $2 million.

Similarly, if a fund manager tells you: "Our fund has a 40% maximum historical drawdown," you should ask: "Could I have psychologically stayed in for that loss? Did other investors?" If the answer is no, the fund is riskier to *you* than the statistics suggest, even if the long-term returns were attractive.

## Limitations of Historical Drawdowns

Past maximum drawdowns are not guarantees of future ones. A portfolio that never experienced a 40% loss before 2008 suffered one then. Conversely, a strategy that had a 35% drawdown in its first decade might go decades without repeating it.

Maximum drawdown is also "lookback" data—it requires a full cycle of peak and trough. In real time, as a drawdown develops, investors don't know whether they're in a 5% pullback or the start of a 50% crash. This uncertainty is why [stress testing](/stress-testing/) and scenario analysis matter; they help investors grapple with drawdowns that never happened but could.

Additionally, maximum drawdown is sensitive to the starting date. Beginning analysis one month before a crash inflates the figure; beginning one month after understates it. Professional analysts use multiple time windows and rolling drawdowns to smooth this artifact.

## Drawdown and Asset Class Comparison

Different asset classes experience different maximum drawdowns:

- **Large-cap stocks**: 40–60% in severe bear markets
- **Small-cap stocks**: 60–80% (higher volatility, deeper drawdowns)
- **Investment-grade bonds**: 5–15% (rare, mostly in rising-rate environments)
- **High-yield bonds**: 25–45% (rare; usually correlated with equity crashes)
- **Real estate**: 30–50% (often gradual; recovery slow)
- **Commodities**: 50–70% (extreme volatility and cyclicality)

A diversified portfolio mixing stocks, bonds, and alternatives dampens maximum drawdown relative to its components—the central benefit of [diversification](/diversification/).

## See also

<div class="wiki-seealso">

### Closely related

- Volatility — dispersion of returns, distinct from drawdown magnitude
- [Beta](/beta/) — systematic risk relative to a market benchmark
- [Sharpe Ratio](/sharpe-ratio/) — return-to-volatility efficiency, which drawdown analysis complements
- [Value at Risk](/value-at-risk/) — statistical confidence interval for loss, another drawdown alternative
- [Stress Testing](/stress-testing/) — scenario analysis to model possible future drawdowns

### Wider context

- [Portfolio Diversification](/diversification/) — primary tool for reducing maximum drawdown
- [Asset Allocation](/asset-allocation/) — the strategic balance determining expected drawdown
- [Market Cycle](/market-cycle/) — economic context within which drawdowns occur
- [Risk-Weighted Assets](/risk-weighted-assets/) — capital framework accounting for downside risk

</div>

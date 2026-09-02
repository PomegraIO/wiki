---
title: "Drawdown Analysis"
description: "Measuring the peak-to-trough decline in a portfolio's value over time, a key risk metric for assessing downside volatility."
keywords:
  - drawdown
  - peak-to-trough
  - portfolio risk
  - maximum drawdown
  - portfolio recovery
---

*Drawdown analysis measures the peak-to-trough decline in a portfolio's value from its highest point to its lowest subsequent point before recovering, providing a direct measure of the largest loss an investor would have experienced if they bought at the worst possible time.*

<aside class="wiki-infobox">

| Metric | Definition |
|---|---|
| **Drawdown (DD)** | Loss from peak to trough, typically as %-age |
| **Maximum drawdown (MDD)** | Largest drawdown over the period analyzed |
| **Recovery period** | Time to return to prior peak |
| **Underwater time** | Duration portfolio is below peak |
| **Intra-period drawdown** | Multiple drawdowns within a holding period |
| **Comparison** | More intuitive than volatility for many investors |

</aside>

## Why drawdown matters more than volatility

Standard deviation (volatility) measures how much returns fluctuate around the average. A portfolio up 30% one year and down 30% the next has the same volatility as one up 15% and down 15%, but the emotional and financial impact is very different. The first portfolio experienced a 30% loss; the second, a 15% loss. **Drawdown** captures this directly: it is the peak-to-trough decline, the actual loss from worst timing. A retiree who bought at the peak of the dot-com bubble in 2000 and held through 2003 experienced a 50%+ drawdown in the Nasdaq 100; standard deviation alone does not capture the pain of that scenario.

## Calculating maximum drawdown

The **maximum drawdown (MDD)** is the largest decline from any peak to any subsequent trough in the return series. To calculate it:

1. Compute the cumulative value of the portfolio over time (or its return index).
2. For each date, identify the prior maximum value (the running peak).
3. Calculate the decline from that peak to the current value.
4. Record the largest such decline.

If a portfolio grows from $100 to $150 to $120 to $160 to $90, the running peaks are $100, $150, $150, $160, and $160. The declines are 0%, 20%, 20%, 44%, and 44%. The maximum drawdown is 44% (from $160 to $90). MDD is always a negative number, expressed as a percentage or dollar amount.

## Multiple drawdowns and the underwater timeline

Most portfolios experience multiple drawdowns over a holding period. A portfolio might drop 20% over three months, recover to a new high, then drop 15%, then recover again. Drawdown analysis tracks each decline. The total time a portfolio spends "underwater" (below a prior peak) is another useful metric. A portfolio that drops 30% but recovers in two months has the same MDD as one that drops 30% and takes two years to recover, but the investor experience is vastly different. Underwater time is thus a complement to maximum drawdown.

## Drawdown and recovery time

Recovery time is how long it takes for a portfolio to return to its prior peak after hitting the trough. This depends on both the magnitude of the drawdown and the subsequent returns. A 50% drawdown requires 100% gains to recover to breakeven (a tough bar). A 20% drawdown requires 25% gains. If a portfolio declines 50% and then earns 10% per year, the recovery can take many years. This interaction between drawdown severity and recovery rate is why both matter: a large drawdown with slow recovery inflicts extended investor pain.

## Comparing drawdown across portfolios and strategies

Drawdown is a popular metric for comparing investment strategies. A hedge fund that claims 12% annualized return with a 15% maximum drawdown is more appealing than one with 12% return but a 40% maximum drawdown. Similarly, a passive index investor might tolerate a 40% drawdown in a bear market because the index always recovers; an active manager with a 40% drawdown might be forced to close the fund due to redemptions or reputational damage. Drawdown is one of the few risk metrics that directly aligns with investor experience.

## Limitations of drawdown analysis

Drawdown tells you the worst (or peak-trough) loss, but it does not capture the frequency of losses or the distribution of returns. A strategy with many small 5% drawdowns and occasional 50% crashes has a high maximum drawdown but a different risk character than a strategy with steady 15% drawdowns every three years. Also, maximum drawdown is a **backward-looking** statistic; it measures the worst historical loss, not the probability of future losses. A portfolio that has never drawdown more than 20% could still suffer a 50% loss in the next crash.

## Underwater portfolio and psychological impact

Investors who experience large drawdowns often exhibit regrettable behavior: panic selling at the bottom, abandoning strategies, or becoming overly conservative. Drawdown analysis helps illustrate why: a 50% drawdown is emotionally devastating. Some target-date funds or risk-managed portfolios explicitly limit maximum drawdown to 30% or less, betting that this level of loss is what retirees or risk-averse investors can psychologically tolerate. By avoiding the 50% drawdown, the strategy preserves investor discipline.

## Drawdown-based performance metrics

Several metrics combine drawdown with returns to assess risk-adjusted performance:

- **Calmar ratio**: Annualized return divided by maximum drawdown.
- **Recovery factor**: Total profit divided by maximum drawdown (higher is better).
- **Sortino ratio**: Return in excess of a minimum acceptable return, divided by downside deviation (related to drawdown).

These metrics favor strategies that generate return with controlled drawdowns, not those that occasionally spike in value but experience large crashes.

<div class="wiki-seealso">

### Closely related
- [Maximum drawdown](/wiki/drawdown-forex/) — Largest peak-to-trough loss
- [Volatility](/wiki/historical-volatility/) — Standard deviation of returns
- [Tail risk](/wiki/tail-risk/) — Risk of extreme losses
- [Value at risk](/wiki/value-at-risk/) — Quantile-based loss measure

### Wider context
- Risk management — Systematic approach to downside control
- [Performance metrics](/wiki/sharpe-ratio/) — Evaluating return and risk
- [Portfolio construction](/wiki/asset-allocation/) — Building risk-controlled portfolios

</div>

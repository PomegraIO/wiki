---
title: "Conditional Drawdown at Risk (CDaR)"
description: "Conditional Drawdown at Risk (CDaR) is a coherent risk measure that averages the worst drawdown episodes beyond a chosen confidence threshold, replacing the drawdown cliff of maximum drawdown."
keywords:
  - conditional drawdown at risk
  - cdar risk measure
  - drawdown risk
  - coherent risk measure
  - maximum drawdown alternative
---

*The **Conditional Drawdown at Risk** (CDaR) is a risk measure that quantifies the average loss in the worst drawdown episodes above a chosen confidence level. Unlike [maximum drawdown](/), which captures only the single deepest decline from peak to trough, CDaR spreads the risk across multiple bad scenarios, averaging the worst episodes. It is a "coherent" risk measure, meaning it respects diversification and scales appropriately with portfolio size—making it a sounder tool than maximum drawdown for portfolio construction and risk management.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Conditional Drawdown at Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A coherent drawdown-based risk metric that averages the worst drawdowns beyond a threshold, fixing the cliff-like discontinuity of maximum drawdown.</div>

|   |   |
|---|---|
| **Definition** | Average loss magnitude in the worst drawdown episodes above a confidence level (e.g., 95th percentile) |
| **Formula foundation** | Average of drawdown episodes exceeding the chosen quantile |
| **Confidence level** | Typically 90% to 99%; CDaR-95 = average of the worst 5% of drawdowns |
| **Advantage over max drawdown** | Spreads risk across multiple scenarios; avoids single-outlier distortion |
| **Comparison to Value at Risk** | Both are coherent; [VaR](/value-at-risk/) applies to returns; CDaR applies to drawdowns |
| **Use case** | Portfolio optimization, hedge fund performance assessment, tail-risk management |

</aside>

## What Is Drawdown and Why Measure It?

A **drawdown** is the decline in value from a previous peak. If a portfolio reaches $1 million on day 100, then falls to $900,000 by day 200, the drawdown is $100,000 or 10%. Investors care deeply about drawdown because it represents real losses from the high-water mark—the worst moment in a holding period to have bought the portfolio.

Traditional risk measures like [volatility](/volatility-smile/) (standard deviation of returns) treat gains and losses symmetrically. A volatility-based model does not care whether a 20% swing is a gain or a loss. But investors hate losses far more than they enjoy equivalent gains—a behavioral bias called [loss aversion](/loss-aversion/). Drawdown metrics respect this asymmetry by measuring downside directly.

The oldest drawdown measure is **maximum drawdown**—the largest peak-to-trough decline over the period. A portfolio with a 50% maximum drawdown experienced at least one moment when it was 50% underwater. This metric is intuitive but has a critical flaw: it responds to a single outlier event. A portfolio might have dozens of small 5% drawdowns and one catastrophic 50% drop; the maximum drawdown ignores the pattern of pain and fixates on the worst day.

## From Maximum Drawdown to CDaR

**Conditional Drawdown at Risk** fixes this by averaging over the worst drawdowns, not just the single worst. This move mirrors the evolution from a single risk measure to a more sophisticated one.

The **maximum drawdown** is equivalent to asking: "What is the deepest loss my portfolio ever hit?" The answer is a number, and it is often driven by one volatile day. In a leveraged or [hedge fund](/hedge-fund/) context, that one day might be an outlier caused by a [tail risk](/tail-risk/) event, which investors correctly fear but which may be statistically rare.

**CDaR** answers: "On average, how deep are the worst drawdowns?" By averaging over multiple bad episodes, it captures the severity of repeated stress, not just the one unluckiest day.

Mathematically, CDaR at a confidence level (e.g., 95%) is the average drawdown among all historical drawdowns that exceed the 95th percentile. If historical data show 1,000 days of returns, CDaR-95 averages the drawdowns on the 50 worst days (top 5%).

## Coherent Risk Measures

CDaR is a **coherent risk measure**, a term with a precise definition in quantitative finance. A coherent measure must satisfy four properties:

1. **Monotonicity:** If portfolio A always returns more than portfolio B, the risk of A is less than or equal to the risk of B.
2. **Homogeneity:** Doubling the portfolio doubles the risk. This prevents distortions when scaling strategies.
3. **Translation invariance:** Adding cash reduces risk proportionally.
4. **Subadditivity:** The risk of combined portfolios is at most the sum of individual risks. This ensures diversification never increases risk.

Maximum drawdown fails subadditivity. Two portfolios with 20% maximum drawdowns can combine into a portfolio with a 40% maximum drawdown if their drawdowns align perfectly. A coherent measure like CDaR would cap the combined risk at 40%, reflecting genuine diversification benefits.

[Value at Risk](/value-at-risk/) (the maximum loss at a given confidence level over a set holding period) is also coherent. CDaR is sometimes called "conditional maximum drawdown" and is the drawdown analogue of VaR. Both are expected shortfall concepts—averages of the tail of a loss distribution.

## CDaR in Practice

**Portfolio optimization.** Investors can optimize portfolio weights to minimize CDaR instead of volatility or [Sharpe ratio](/sharpe-ratio/). A CDaR-minimizing portfolio will hold assets that together avoid the worst drawdown episodes. This often leads to higher [diversification](/diversification/) and a different asset mix than volatility-based optimization.

**Hedge fund and active strategy evaluation.** A hedge fund manager claims a "15% volatility" but suffered a 50% maximum drawdown in a single year. The average investor cares more about the drawdown. CDaR-95 might reveal that the fund's typical bad month (when it is in the worst 5% of months) sees an 8% drawdown. That is a more honest picture than the maximum.

**Tail risk and black swan hedging.** CDaR surfaces how expensive the worst episodes are, which guides decisions on [tail risk](/tail-risk/) hedges (e.g., [put options](/put-option/)). A portfolio with a CDaR-95 of 15% should expect serious drawdowns; this information can justify the cost of [protective puts](/protective-put/).

**Comparative strategy assessment.** Strategy A has a 30% maximum drawdown and a 12% CDaR-95. Strategy B has a 40% maximum drawdown and a 10% CDaR-95. The larger single drop in B is offset by its lower average of the worst episodes; CDaR reveals that B's bad episodes are less severe overall, even if one bad month was worse.

## Calculation and Interpretation

To compute CDaR-90 for a portfolio over 252 trading days:

1. Calculate the drawdown on each day (maximum loss from that day's starting peak).
2. Rank drawdowns from largest to smallest.
3. Identify the top 10% worst days (roughly 25 days).
4. Average the drawdown values on those 25 days.

The result is CDaR-90 in dollars or percentage terms. A CDaR-90 of 12% means that, on the average of the 10% worst-case drawdown days, the portfolio loses 12% from peak.

A critical interpretation: CDaR-90 is *not* a worst-case bound (unlike maximum drawdown). It is a conditional expectation. The portfolio could still experience worse drawdowns in new data; CDaR quantifies the average severity of the historically worst episodes, not an absolute floor.

## Strengths and Limitations

**Strengths:**
- Coherent, so it respects diversification and avoids scaling oddities.
- Sensitive to multiple bad events, not just one outlier.
- Aligns with investor loss aversion; focus is on downside, not upside.
- Yields meaningful comparisons across different time periods and strategies.

**Limitations:**
- Requires substantial historical data; CDaR-99 needs at least ~100 observations to be reliable.
- Backward-looking; past drawdowns may not predict future ones.
- Can be dominated by one or two extreme events in short data histories (same pitfall as maximum drawdown, though less acute).
- Less widely understood than [volatility](/volatility-smile/) or [Value at Risk](/value-at-risk/), so institutional adoption lags.

## Relationship to Other Risk Measures

**Maximum drawdown** is the simplest; it captures one worst day, making it easy to explain but prone to outlier distortion.

**CDaR** averages over multiple worst days, mitigating outlier effects and satisfying coherence axioms.

**[Value at Risk](/value-at-risk/)** measures the tail of return distribution (e.g., 99% confidence that losses won't exceed X). CDaR measures the tail of the drawdown distribution. Both are coherent and related; CVaR (Conditional VaR) is the return-space analogue of CDaR.

**[Volatility](/volatility-smile/)** treats gains and losses equally. Drawdown-based metrics (including CDaR) are one-sided, capturing downside only. For investors with loss-averse preferences, drawdown metrics are more behaviorally salient.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — coherent return-based tail risk measure; CDaR is its drawdown equivalent
- Maximum Drawdown — simpler drawdown metric; focuses on single worst episode
- [Loss Aversion](/loss-aversion/) — behavioral bias that motivates focus on downside risk
- [Tail Risk](/tail-risk/) — extreme loss episodes that CDaR captures in its average
- [Volatility](/volatility-smile/) — symmetric risk measure; contrasts with drawdown focus
- [Sharpe Ratio](/sharpe-ratio/) — return-adjusted risk metric using volatility; CDaR optimization offers an alternative

### Wider context

- Risk Measurement — broader framework of risk quantification
- Portfolio Optimization — process where CDaR can replace or complement volatility
- [Hedge Fund](/hedge-fund/) — strategies where drawdown risk is critical to evaluation
- [Diversification](/diversification/) — portfolio benefit that coherent measures like CDaR respect
- [Protective Put](/protective-put/) — hedging strategy motivated by CDaR or drawdown concerns

</div>

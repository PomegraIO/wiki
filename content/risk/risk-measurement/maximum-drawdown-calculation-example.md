---
title: "Maximum Drawdown Calculation With Example"
description: "Maximum drawdown measures the steepest decline from peak to trough in a portfolio or asset return series. A worked example shows how to calculate it step by step."
keywords:
  - maximum drawdown calculation
  - how to calculate maximum drawdown
  - drawdown definition
  - portfolio peak-to-trough loss
  - recovery time after losses
image: /svg/risk.svg
---

*A **maximum drawdown calculation** identifies the worst decline an investment has suffered from its highest point to its lowest point afterward, expressed as a percentage loss. If a portfolio peaks at $100,000, then falls to $75,000 before recovering, the maximum drawdown is 25%. Calculating it requires scanning the entire return history to find the biggest peak-to-trough drop, then comparing it to other risk metrics like [volatility](/market-risk/) or the [Sharpe ratio](/sharpe-ratio/) to assess whether returns justify the pain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maximum Drawdown — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Maximum drawdown captures the depth of loss from peak to trough.</div>

|   |   |
|---|---|
| **Definition** | Largest percentage decline from a previous peak to a subsequent trough |
| **Time period** | From peak date to the date of the trough; critical for assessing recovery speed |
| **Formula** | Drawdown = (Trough Value − Peak Value) / Peak Value |
| **Expressed as** | Percentage (negative); e.g., −35% |
| **Worst-case scenario** | Maximum drawdown is the hypothetical worst entry point: buy at the peak, sell at the trough |
| **Differs from** | Average drawdown (mean of all declines) and average drawdown duration |
| **Related metrics** | [Calmar ratio](/sharpe-ratio/) (return per unit of max drawdown); recovery time |

</aside>

## Defining Maximum Drawdown

Maximum drawdown is the largest percentage drop a portfolio experiences from a peak value to a trough value at any later date. It answers: "What is the worst loss an investor who bought at the absolute worst time would have suffered?"

Formally:

$$\text{Max Drawdown} = \frac{\text{Trough Value} - \text{Peak Value}}{\text{Peak Value}} \times 100\%$$

The result is negative. A maximum drawdown of −35% means that at some point, the portfolio fell 35% from its prior high.

This metric is psychologically important. While [volatility](/market-risk/) captures the typical swing (standard deviation of returns), maximum drawdown captures the *worst* realistic swing. Investors often care more about the deepest pain they might endure than about abstract statistical measures.

## Worked Example: Calculating Maximum Drawdown

Consider a portfolio with monthly ending values over 12 months:

| Month | Value | Peak to Date | Drawdown % |
|-------|-------|--------------|-----------|
| 1 | $100,000 | $100,000 | 0% |
| 2 | $105,000 | $105,000 | 0% |
| 3 | $108,000 | $108,000 | 0% |
| 4 | $103,000 | $108,000 | −4.6% |
| 5 | $98,000 | $108,000 | −9.3% |
| 6 | $95,000 | $108,000 | −12.0% |
| 7 | $102,000 | $108,000 | −5.6% |
| 8 | $107,000 | $108,000 | −0.9% |
| 9 | $110,000 | $110,000 | 0% |
| 10 | $106,000 | $110,000 | −3.6% |
| 11 | $104,000 | $110,000 | −5.5% |
| 12 | $112,000 | $112,000 | 0% |

**Step 1:** Track the running peak. As the portfolio rises, the peak updates. Once it falls, the peak stays put until a new high is set.

**Step 2:** At each date, calculate the drawdown from the peak: (Current Value − Peak) / Peak.

**Step 3:** Find the minimum (most negative) drawdown.

In this example:
- Month 3 is a new peak at $108,000.
- Months 4–6 fall, with Month 6 reaching the trough: $95,000.
- Drawdown at Month 6 = ($95,000 − $108,000) / $108,000 = −12.0%.
- Month 9 recovers above the prior peak to $110,000, establishing a new peak.
- Month 10–11 dip slightly (−3.6% and −5.5% from the $110,000 peak).
- Month 12 hits $112,000, a new all-time high.

**Maximum drawdown = −12.0%**, occurring at Month 6 (the trough from the Month 3 peak).

## Key Insights from This Example

**Recovery time:** The portfolio took 3 months to recover from the trough ($95,000 in Month 6) back above the prior peak ($108,000), not reaching a new peak until Month 9. Investors who bought at the Month 3 peak and held until Month 9 experienced a −12% peak-to-trough loss and a 6-month drawdown duration.

**Not the same as loss:** The portfolio did not lose −12% over the year; it ended up 12% higher ($100k → $112k). But the maximum drawdown reveals the path was bumpy, and a worst-case buyer would have suffered real losses.

**Subsequent peaks are irrelevant:** Month 12's peak at $112,000 does not change the maximum drawdown calculation; it is computed from past highs only.

## Maximum Drawdown vs. Average Drawdown

Average drawdown is the arithmetic mean of all the declines (in our example, the average of the 6 months of negative drawdown %). It is more forgiving than maximum drawdown but less commonly used in practice.

Maximum drawdown is stricter: it focuses on the single worst episode. This makes it useful for portfolio managers and investors wanting to understand the worst-case scenario they might face.

## Maximum Drawdown vs. Volatility

Volatility (standard deviation) describes typical swings around the mean return. A portfolio with 15% annual volatility might see 90% of monthly returns fall within ±1.3%. But volatility does not tell you about the absolute worst decline.

A portfolio could have low volatility (stable monthly returns) but still suffer a large maximum drawdown if the returns are consistently negative over a stretch. Conversely, a high-volatility portfolio with frequent large ups and downs might have a smaller maximum drawdown if the ups are large enough to erase the downs quickly.

**Example:** Two portfolios, both with 15% annual volatility:
- Portfolio A: steady gains of 1.2% per month → max drawdown near 0%.
- Portfolio B: alternating ±10% returns → max drawdown of ~10% (worst case: down 10% from a peak, then recovering).

Volatility alone does not differentiate them, but maximum drawdown does.

## The Calmar Ratio

One way to use maximum drawdown is the **Calmar ratio** (or drawdown ratio):

$$\text{Calmar Ratio} = \frac{\text{Average Annual Return}}{\text{Maximum Drawdown (absolute value)}}$$

A portfolio with 12% annual return and −20% maximum drawdown has a Calmar ratio of 12/20 = 0.60. Higher ratios indicate better risk-adjusted returns; the portfolio earned more per unit of drawdown endured.

The Calmar ratio complements the [Sharpe ratio](/sharpe-ratio/), which divides return by volatility. Some strategies (e.g., long volatility, trend-following) may have high Sharpe ratios but poor Calmar ratios because they suffer occasional deep drawdowns. Conversely, a slow, steady strategy might have a lower Sharpe ratio but an excellent Calmar ratio.

## Limitations and Practical Notes

**Historical bias:** Maximum drawdown is computed from past data. There is no guarantee a future drawdown will not exceed the historical maximum, especially for longer lookback windows.

**Path dependence:** Maximum drawdown only reports the size of the decline, not the speed. A 20% drawdown over 2 months is more psychologically taxing than a 20% drawdown spread over 12 months, but both show −20%.

**Not forward-looking:** Like all historical metrics, maximum drawdown describes what happened, not what will happen. A strategy that had a modest 10% maximum drawdown in a bull market may face a 40% drawdown in the next bear market.

**Length of data:** A 1-year maximum drawdown may not capture a once-in-a-decade crash. Longer histories reveal worse declines. Risk managers often examine drawdowns over 10–20 years or stress-test against historical extreme scenarios.

**Sequence risk:** Maximum drawdown captures one type of risk—the loss from peak to trough at any point. It does not address [sequence risk](/asset-allocation/) (the order of returns) or [tail risk](/tail-risk/) (rare catastrophic events) directly.

## See also

<div class="wiki-seealso">

### Closely related

- [Volatility](/market-risk/) — statistical dispersion vs. maximum drawdown's worst-case scenario
- [Sharpe ratio](/sharpe-ratio/) — another risk-adjusted metric combining return and volatility
- [Value at risk](/value-at-risk/) — probability of a loss beyond a threshold on a given day
- [Tail risk](/tail-risk/) — extreme losses in the far distribution tails
- [Calmar ratio](/sharpe-ratio/) — return divided by maximum drawdown, complementing Sharpe

### Wider context

- [Asset allocation](/asset-allocation/) — managing drawdowns through diversification
- Risk measurement — suite of tools for quantifying portfolio risk
- [Beta as systematic risk measure](/beta-as-systematic-risk-measure/) — market-driven volatility component

</div>

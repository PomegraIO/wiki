---
title: "Calmar Ratio"
description: "A risk-adjusted performance metric that measures annualized return relative to the maximum drawdown, highlighting recovery risk."
keywords:
  - calmar ratio
  - maximum drawdown
  - risk-adjusted return
  - trend following
  - recovery time
  - drawdown recovery
image: "/svg/ratios.svg"
---

*The **Calmar ratio** divides annualized return by [maximum drawdown](/maximum-drawdown/), rewarding strategies that earn steady gains without catastrophic losses. It is particularly valued in trend-following and systematic trading, where avoiding deep underwater periods matters as much as total return.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Calmar Ratio — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">Annualized return divided by peak-to-trough loss; emphasizes drawdown severity.</div>

|   |   |
|---|---|
| **What it is** | Annualized return divided by [maximum drawdown](/maximum-drawdown/), measuring return per unit of worst-case loss |
| **Also called** | Return over maximum drawdown (informal) |
| **Numerator** | Annualized total return over the measurement period |
| **Denominator** | Maximum drawdown as a percentage (expressed as a positive number for the ratio) |
| **Higher is better** | Yes—higher ratio indicates better return relative to worst drawdown suffered |
| **Typical benchmark** | Used primarily for [trend-following](/trend-following/) and [hedge funds](/hedge-fund/) |
| **Strengths** | Simple to understand; captures worst-case scenarios; sensitive to recovery time |
| **Weakness** | Heavily influenced by a single large drawdown; doesn't measure frequency of drawdowns |

</aside>

## Why drawdown depth matters more than volatility

Volatility—the standard deviation of returns—tells you how much a strategy jiggles month to month, but it says nothing about the deepest hole the fund falls into. A strategy could have steady 2% monthly gains punctuated by a devastating 40% collapse, and the volatility figure would understate the damage. The Calmar ratio zeroes in on that worst drawdown, making it crucial for strategies where capital recovery is slow or psychological tolerance for loss is finite.

Trend-following strategies—which exploit momentum in stocks, bonds, commodities, and currencies—are especially vulnerable to large drawdowns during regime-change shocks. When a bull market suddenly reverses, a system riding long positions gets hit hard before it can pivot. The Calmar ratio penalizes those deep trough periods, incentivizing strategies that either hedge tail risk or rotate defensively before crashes arrive.

## Calculation and example

The formula is simple:

**Calmar Ratio = Annualized Return / Maximum Drawdown**

Suppose a [managed futures](/managed-futures/) fund returned 12% annualized over three years. During that period, the worst peak-to-trough loss (maximum drawdown) was 18%. The Calmar ratio is 12 ÷ 18 = 0.67.

Compare this to a bond-biased fund returning 5% annualized with a maximum drawdown of only 4%. Its Calmar ratio is 5 ÷ 4 = 1.25. Despite the lower absolute return, the bond fund's superior Calmar ratio signals that it achieved returns more efficiently relative to downside risk—in this case, a smoother ride to profit.

A long-only equity fund returning 10% with a 25% drawdown has a Calmar of 0.4. If another fund returns 8% with only a 10% drawdown, its Calmar is 0.8. The lower-returning fund would attract investors who weight drawdown-free capital preservation heavily.

## Calmar ratio strength in different market conditions

The metric shines in sideways or choppy markets where buy-and-hold strategies languish and drawdowns are frequent. A Calmar ratio of 1.0 or higher is generally considered strong—it means the annualized return at least matches the severity of the worst loss, suggesting the strategy recovers quickly or avoids large drawdowns altogether.

Ratios above 1.5 are excellent and typically signal either a remarkably defensive or exceptionally well-timed strategy. Ratios below 0.3 suggest the strategy's drawdowns are too deep relative to the return it generates, raising the question of whether the risk is worth it.

During bull markets, when drawdowns are shallow and returns are generous, Calmar ratios can inflate artificially. A fund may look great in a five-year window that missed the 2008 financial crisis entirely. This is why historical depth (ten years or more) matters: it ensures the ratio has been stress-tested through at least one major bear market.

## Calmar ratio versus other drawdown metrics

The [Sharpe ratio](/sharpe-ratio/) uses volatility (the standard deviation of all returns) as the denominator; the Calmar uses maximum drawdown. Sharpe can obscure tail risk—a strategy with moderate volatility but occasional 30% drops could still score well on Sharpe. Calmar cannot hide those worst scenarios.

The [Omega ratio](/omega-ratio/) goes further by measuring the full distribution of gains versus losses at a threshold, not just the worst single trough. An investor might use Calmar for a quick, intuitive sense of drawdown risk and then dig into Omega for a deeper picture of downside probability.

[Information ratio](/information-ratio/) measures alpha relative to a benchmark; Calmar measures absolute return relative to the worst loss experienced. They answer different questions: information ratio asks, "Did the manager beat the index consistently?" Calmar asks, "Did the manager avoid catastrophe while generating returns?"

## Limitations of the ratio

The Calmar ratio is a snapshot: a single catastrophic loss—whether one-in-a-century or a warning sign of structural weakness—can make a three-year history look deceptively bad or, conversely, a four-year history that happened to exclude a crash can look deceptively good. The ratio is therefore most useful when compared across peer groups or when tracked over extended periods.

It also ignores frequency. A strategy that falls 20% once every ten years and recovers quickly will have a similar Calmar ratio to one that falls 20% every three years and recovers more slowly. An investor should pair Calmar with frequency analysis: how often does this drawdown occur, and how long does recovery take?

Finally, Calmar is most meaningful for strategies with consistent positive returns. A breakeven strategy with a 5% drawdown would show a Calmar of 0, and a strategy that loses money overall but happens to have a small drawdown could show a negative ratio—both cases where the metric loses interpretive power.

## Practical use in hedge fund and alternative selection

Institutional investors reviewing [hedge fund](/hedge-fund/) or [commodity trading advisor (CTA)](/commodity-trading-advisor/) track records almost always reference Calmar alongside Sharpe and maximum drawdown itself. A high Calmar suggests the manager has either superior market timing, better risk controls, or both. A low Calmar despite decent absolute returns suggests concentration of losses in a few bad periods—a pattern that might repeat.

The metric is also used internally by systematic traders to optimize strategy parameters. If two versions of a trend-following algorithm have similar Sharpe ratios but one has a Calmar of 0.8 and another has 1.2, the second likely controls position sizing or stop losses more effectively. Portfolio managers can then choose or weight the more robust version.

## See also

<div class="wiki-seealso">

### Closely related

- [Maximum Drawdown](/maximum-drawdown/) — the denominator; peak-to-trough percentage loss in the equity curve
- [Sharpe Ratio](/sharpe-ratio/) — risk-adjusted return using volatility; less sensitive to tail risk
- [Omega Ratio](/omega-ratio/) — probability-weighted gains versus losses; captures full distribution
- [Information Ratio](/information-ratio/) — excess return versus tracking error; benchmark-relative measure
- [Trend Following](/trend-following/) — strategy type where Calmar ratio is most commonly cited
- [Managed Futures](/managed-futures/) — systematic strategy relying on drawdown management

### Wider context

- [Hedge Fund](/hedge-fund/) — vehicles where Calmar is a primary evaluation metric
- Risk-Adjusted Return — family of metrics combining return and risk
- Portfolio Construction — how drawdown metrics influence allocation
- [Stress Testing](/stress-testing/) — complementary analysis of worst-case scenarios

</div>

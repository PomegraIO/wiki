---
title: "Maximum Drawdown"
description: "The largest percentage decline from a portfolio's peak value to its lowest subsequent value, capturing the worst case loss between highs."
keywords:
  - drawdown
  - peak-to-trough
  - maximum loss
  - portfolio risk
  - stress period
  - recovery time
image: /svg/risk.svg
---

*A **maximum drawdown** is the largest peak-to-trough loss a portfolio or investment has experienced over a historical period. If a portfolio rises to £1m, falls to £800k, then recovers, the maximum drawdown is 20%. Unlike volatility, which is bidirectional, drawdown captures only losses and is unambiguous: it's a pure loss from a prior high. For investors, it answers the feared question: "In the worst case I lived through, how much did I lose?"*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maximum Drawdown — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement concepts." />

<div class="wiki-infobox-caption">Worst historical loss from peak, a visceral measure of portfolio pain.</div>

|   |   |
|---|---|
| **What it is** | Largest percentage decline from a prior peak to a trough |
| **Formula** | (Trough Value − Peak Value) / Peak Value |
| **Time-aware** | Yes; includes both depth and duration of the drawdown |
| **Pros** | Intuitive; easy to calculate; historically realistic |
| **Cons** | Backward-looking; one large event dominates; doesn't predict future drawdowns |

</aside>

## Why volatility misses the story

Volatility measures how much a portfolio's returns bounce around their average—day-to-day noise, both up and down. A portfolio with 10% annualized volatility might have swings of ±2% in a week. But volatility doesn't tell you the worst case. It's symmetric: it penalizes you equally for +10% moves and −10% moves. For investors, a sharp loss and a sharp gain feel very different.

A hedge fund might have low volatility because returns are smooth. But if those returns are consistently negative (a slow bleed), volatility is low and the investor is incinerated. Conversely, a venture capital fund might be quiet for years, then jump 100% once or twice, then crash 50%. Volatility spikes on the crashes, but the story is that investors tolerate the volatility because they knew the downside risk.

Maximum drawdown strips away the noise and asks: "What's the worst peak-to-trough decline I've ever endured?" It's an extreme loss, not an average or standard deviation.

## Calculating and interpreting

The calculation is simple. Take the time series of portfolio values (or cumulative returns). For every point in time, find the highest value that came before it (the running maximum). The drawdown at that point is:

Drawdown_t = (Value_t − Max_s<t (Value_s)) / Max_s<t (Value_s)

The maximum drawdown is the lowest (most negative) drawdown in the entire series.

Example: A portfolio's weekly values are £1000, £1050, £1040, £900, £950, £980.

| Week | Value | Running Max | Drawdown |
|------|-------|-------------|----------|
| 1 | £1000 | £1000 | 0% |
| 2 | £1050 | £1050 | 0% |
| 3 | £1040 | £1050 | −0.95% |
| 4 | £900 | £1050 | −14.3% |
| 5 | £950 | £1050 | −9.5% |
| 6 | £980 | £1050 | −6.67% |

Maximum drawdown: **−14.3%**.

This happened in week 4 (from the peak of £1050 to £900) and persisted even as the portfolio recovered slightly. Most investors would use this 20-year-historical-maximum-drawdown figure as a key risk metric. If the maximum drawdown over the past five years is −32%, then potential investors know they should expect that level of pain as a realistic worst-case.

## Duration and recovery

Drawdown data often includes two companion metrics:

**Duration**: How long did the drawdown last? In the example above, the maximum drawdown lasted from week 2 (when the peak was set) until week 6 (when values finally exceeded £1050 again). That's 4 weeks of being underwater.

**Time to recovery**: How long from the trough (week 4) to break-even? Week 6 is the first point above the prior peak, so recovery took 2 weeks from the trough.

These matter. A −20% drawdown that lasts 2 months is painful but survivable. A −20% drawdown that lasts 3 years erodes investor confidence and often leads to panic selling at the worst time. Similarly, recovery time affects opportunity cost and psychological resilience.

## Historical examples and benchmarks

The [S&P 500](/sp-500-index/) experienced a maximum drawdown of −56% during the Great Depression (1929–1932). In the 2008 financial crisis, the drawdown was −57% from peak to trough. The COVID-19 pandemic caused a −34% drawdown, recovered in about 5 months. Most calendar-year equity investors experience drawdowns of −15% to −25% during a typical bear market.

A diversified 60/40 portfolio (60% equities, 40% bonds) historically has a maximum drawdown of around −30% to −35% over multi-decade periods. A 100% bond portfolio might see maximum drawdowns of −10% to −15% during rising-rate periods. A money-market fund sees almost no drawdown.

These are backward-looking. The question haunting every investor is whether the next drawdown will be worse. The S&P has drawdowns of −50%+ once every 80 years or so. Does that mean it won't happen in the next decade? No. Maximum drawdown is historical, not predictive.

## Advantages and blind spots

Maximum drawdown is intuitive and honest. It's what investors actually fear: the worst case they'll see, from a comforting high to a terrifying low. It doesn't smooth over the pain with volatility formulas.

But it has gaps. First, it's a single-point statistic—one bad month or quarter dominates. If a portfolio had a −30% drawdown in 2008 and has been fine for 15 years since, that −30% still counts as the maximum. A new investor in 2024 might see it and be spooked, not realizing it's ancient history under a different market regime.

Second, it's not forward-looking. Just because a portfolio experienced a −30% drawdown in the past doesn't mean it will experience −30% in the next crash. Market structure changes, diversification changes, correlations change. Copulas and scenario analysis try to predict forward drawdowns; historical maximum drawdown is silent.

Third, it doesn't account for probability. A maximum drawdown of −50% tells you the worst case happened; it doesn't tell you whether that worst case is a once-in-a-thousand-year event or a once-a-decade occurrence. [Value at Risk](/value-at-risk/) and [Expected Shortfall](/expected-shortfall/) try to add probability; maximum drawdown is pure history.

## Portfolio construction use

Many investors set a drawdown tolerance as part of their investment policy. A pension fund might say, "We'll accept a maximum drawdown of no more than −25%." A risk manager then constructs a portfolio that historically would not have exceeded that threshold. This often leads to increasing [bond](/bond/) and cash allocations or introducing [hedge funds](/hedge-fund/) for downside protection.

[Performance fees](/performance-fee/) in hedge funds are sometimes tied to maximum drawdown recovery. If a fund drops −20% in year one, it cannot charge incentive fees until it recovers above the prior peak (the "high-water mark"). This protects investors from paying performance on a rebound to −10%.

For [algorithmic trading](/algorithmic-trading/) strategies, drawdown limits are enforced in real time. If a strategy's maximum drawdown from its starting capital exceeds a threshold (say, −10%), it automatically stops trading. This prevents a temporary loss from cascading.

## Integration with other risk metrics

Maximum drawdown works best alongside other measures. Pair it with volatility and you get a richer picture: a low-volatility, high-drawdown fund is probably experiencing slow, sustained losses. Pair it with [Sharpe ratio](/sharpe-ratio/) and you're seeing return relative to risk. Pair it with [Value at Risk](/value-at-risk/) and you're seeing both historical worst case and statistical tail probability.

A prudent investor uses maximum drawdown as a gut check and a scenario anchor—"Here's what I actually experienced"—then combines it with forward-looking metrics like [stress tests](/stress-testing/) and [scenario analysis](/scenario-analysis/) to plan for the next crisis.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — statistical loss metric complementing historical drawdown
- Volatility — bidirectional risk measure; drawdown captures only losses
- [Expected Shortfall](/expected-shortfall/) — tail loss beyond a confidence level
- [Stress Testing](/stress-testing/) — forward-looking worst-case scenarios
- Portfolio Optimization — construction under drawdown constraints
- [High-Water Mark](/high-water-mark/) — threshold for fee calculation after drawdown recovery

### Wider context

- [Market Risk](/market-risk/) — broader framework for portfolio loss
- [Concentration Risk](/concentration-risk/) — magnifies drawdown depth
- [Bear Market](/bear-market/) — extended period of drawdown
- [Risk Contribution Decomposition](/risk-contribution-decomposition/) — attributing drawdown to holdings

</div>

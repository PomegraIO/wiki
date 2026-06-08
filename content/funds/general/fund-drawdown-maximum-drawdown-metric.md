---
title: "Maximum Drawdown as a Fund Risk Metric"
description: "Maximum drawdown is the largest peak-to-trough decline a fund experiences. Unlike volatility, it captures tail risk and the emotional cost of losses."
keywords:
  - maximum drawdown
  - fund risk metric
  - peak-to-trough decline
  - tail risk measurement
  - volatility vs drawdown
  - fund performance risk
  - portfolio downside risk
image: "/svg/funds.svg"
---

*A **maximum drawdown** is the steepest percentage decline from a fund's peak value to its lowest point before recovery. It measures the worst-case loss a shareholder could have suffered if they invested at the worst possible time, unlike volatility, which treats ups and downs symmetrically.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maximum Drawdown — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A measure of downside risk that volatility alone cannot capture.</div>

|   |   |
|---|---|
| **What it measures** | The largest peak-to-trough loss in fund value, expressed as a percentage |
| **Why it matters** | Captures emotional and real cost of bear markets that standard deviation misses |
| **How it's calculated** | (Lowest price − Peak price) ÷ Peak price, over rolling windows |
| **Typical range** | −10% to −50%+ for equity funds; smaller for bonds |
| **Usefulness** | Best paired with volatility, CAGR, and [Sharpe ratio](/sharpe-ratio/) for full risk picture |
| **Limitation** | Only one number; doesn't distinguish depth vs. duration of decline |

</aside>

## Why drawdown differs from volatility

Two funds can have identical annual volatility but drastically different drawdowns. **Volatility** measures how far returns scatter around the average—ups count the same as downs. **Drawdown** is directional and path-dependent: it captures the actual loss you experience when you buy at the peak and hold through the trough.

A fund posting steady 8% annual volatility with gyrating monthly returns might have a −40% drawdown if those gyrations happen to point downward. Another fund with identical 8% volatility but balanced turbulence might bottom at −15%. Standard deviation cannot tell them apart; maximum drawdown can.

This matters because emotional and financial pain is not symmetrical. A −40% loss requires a 67% gain to break even. A −15% loss requires only an 18% recovery. Drawdown directly measures the break-even hurdle you'd face in a realistic worst-case scenario.

## How maximum drawdown is calculated

The calculation is straightforward but requires daily (or periodic) price history:

1. Identify every peak (local maximum) in the fund's net asset value over the lookback period.
2. Measure the largest percentage drop from that peak to any subsequent trough before a new peak forms.
3. Repeat for all peaks and record the single largest decline.

**Formula:**
```
Drawdown = (Trough Price − Peak Price) / Peak Price × 100%
```

For example, if a fund valued at $1,000 per share peaks at $1,200, then drops to $800 before recovering to $1,300, the drawdown is:

```
($800 − $1,200) / $1,200 = −33.3%
```

Most funds report the maximum drawdown over standard periods: the past year, three years, five years, or since inception. Trailing drawdowns are most relevant to current investors.

## Maximum drawdown vs. standard deviation

These are complementary, not rival, measures. Here's how they diverge:

| Metric | Captures | Misses |
|--------|----------|--------|
| Standard deviation | Volatility in any direction | Direction and duration of losses |
| Maximum drawdown | Worst-case loss magnitude | Frequency or likelihood of severe declines |

A low-volatility fund with stable monthly returns of +0.5% or −0.5% has modest standard deviation but could still experience a −30% drawdown if markets plunge 60% in a quarter (since it holds equities). Meanwhile, a fund that bounces wildly but recovers fully each month might have high volatility but moderate drawdown.

The [Sharpe ratio](/sharpe-ratio/)—which divides excess return by volatility—also ignores downside severity. An alternative, the Sortino ratio, uses only downside volatility, making it more aligned with drawdown philosophy, though they still answer different questions.

## Interpreting drawdown in context

Drawdown alone is misleading without recovery speed and return. A fund down −50% is worse than a fund down −30%, but not if the −50% fund recovers in six months while the −30% fund takes two years.

Key pairs to examine:

- **Drawdown + time to recovery**: How long did the worst drawdown last? Days, months, or years?
- **Drawdown + CAGR**: A fund with −40% maximum drawdown but 12% annualized return may be acceptable for a long-term investor; the same drawdown paired with 3% return is a warning.
- **Drawdown + frequency**: Has the fund experienced multiple −20%+ declines, or was the maximum drawdown a one-time event?

Comparing funds, a manager with a −25% drawdown over five years is generally preferable to one with −45%, all else equal. But if the −45% drawdown was a single 2008-style shock and returns have been stellar since, context matters.

## Maximum drawdown limitations

This metric captures one dimension of risk and should never be used alone:

- It is a historical statistic. Past drawdowns do not guarantee future ones; markets may always decline further than they have before.
- It is indifferent to probability. A −50% drawdown that occurred once in fifty years is not the same risk as one that recurs every five years, yet both produce the same number.
- It offers no forward-looking signal. Volatility, [momentum](/momentum-investing-bear-market/), and market sentiment can hint at future drawdowns; historical drawdown does not.
- It is most useful for equity and [alternative strategies](/hedge-fund/); for [bond funds](/bond-etf/) and money-market funds, smaller absolute drawdowns can still be material in a low-return environment.

## When to prioritize drawdown analysis

Drawdown deserves weight in three scenarios:

1. **Capacity to hold through downturns**: If you cannot tolerate portfolio losses without panic-selling, lower maximum drawdowns matter more than absolute returns. A −20% fund you hold steadily beats a −50% fund you flee.
2. **Limited recovery time**: Investors near or in retirement have shorter horizons to recoup losses. A young accumulator can wait out a −40% drawdown; a retiree may not.
3. **Comparing strategies with similar returns**: When two funds have similar CAGR and volatility, the one with lower maximum drawdown is the safer choice.

For buy-and-hold, long-term investors, maximum drawdown is informative but not paramount. For tactical traders, loss-averse investors, or those with near-term liabilities, it becomes central.

## See also

<div class="wiki-seealso">

### Closely related

- [Volatility](/historical-volatility/) — How much a fund's returns scatter; distinct from drawdown
- [Sharpe ratio](/sharpe-ratio/) — Return per unit of volatility, but indifferent to drawdown shape
- [Value-at-risk](/value-at-risk/) — Statistical estimate of maximum loss at a given confidence level
- [Hedge fund](/hedge-fund/) — Strategies explicitly designed to limit drawdowns in down markets
- [Drawdown duration](/value-at-risk/) — How long recovery takes matters as much as depth

### Wider context

- [Fund prospectus](/fund-prospectus/) — Official disclosure of historical performance and risk metrics
- [Risk-weighted assets](/risk-weighted-assets/) — How institutions quantify portfolio risk
- [Tail risk](/tail-risk/) — Extreme market events that dwarf standard measures
- [Market cycle](/market-cycle/) — Historical context for when major drawdowns occur

</div>

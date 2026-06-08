---
title: "Downside Deviation vs Standard Deviation in Risk Measurement"
description: "Downside deviation measures only negative returns below a target, while standard deviation captures all volatility. Learn when each metric matters most."
keywords:
  - downside deviation vs standard deviation
  - downside risk
  - risk measurement asymmetry
  - volatility metrics
  - target return analysis
  - sortino ratio
image: "/svg/risk.svg"
---

*When measuring investment risk, **downside deviation vs standard deviation** raises a fundamental question: should risk measure all price swings equally, or only the ones that hurt? Standard deviation treats gains and losses symmetrically; downside deviation counts only returns below a target threshold. The choice between them shapes how portfolios are evaluated and compared.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Downside Deviation vs Standard Deviation — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Two measures of risk; one captures all movement, the other only unfavorable moves.</div>

|   |   |
|---|---|
| **Standard deviation** | Treats upside and downside price moves as equal risk |
| **Downside deviation** | Counts only returns below a chosen target (often zero or required return) |
| **When to use each** | Standard for broad comparisons; downside for loss-averse evaluation |
| **Related metric** | [Sortino ratio](/sortino-ratio/) uses downside deviation; [Sharpe ratio](/sharpe-ratio/) uses standard deviation |
| **Practical difference** | Smooth, steady performers look riskier under standard deviation; volatile but upside-heavy assets understate risk this way |
| **Target choice** | Downside deviation requires defining what counts as "bad" — zero, inflation, fund objective, or minimum required return |

</aside>

## What standard deviation measures

Standard deviation captures the typical distance of returns from the average. A fund posting returns of 8%, 10%, 12%, and 10% has a mean of 10% and relatively tight standard deviation — prices cluster around expectation. The same fund posting −5%, 15%, 20%, and 10% has an identical mean but much wider standard deviation, because outcomes are scattered further away.

The critical assumption built into standard deviation is *symmetry*: a 10% gain counts as equally risky as a 10% loss, because both are the same distance from the mean. For many investors, this assumption does not match reality. Winning big is welcome; losing big is the problem. Standard deviation penalizes the upside as much as the downside.

## The logic of downside deviation

Downside deviation measures only the volatility of returns that fall short of a chosen target. Common targets are zero (returns below 0%), a required return (such as your minimum annual goal), or a benchmark return (such as inflation or the S&P 500).

The calculation is similar to standard deviation, but instead of squaring all deviations from the mean, you square only the deviations below the target, set any above-target returns to zero, and then take the square root of the average. The result is a narrower number—often much narrower—because half the data (upside returns) contributes nothing to the risk measure.

If a bond fund returns 4%, 3.8%, 4.2%, 4.1%, and 3.9% (tight, predictable behavior), both standard deviation and downside deviation will be small. But if an equity fund returns −15%, 35%, 22%, −5%, 45%, standard deviation will be large. Downside deviation, however, counts only the −15% and −5%; the 35%, 22%, and 45% returns are treated as acceptable, not risk. The downside deviation is therefore much lower than standard deviation.

## When each metric tells a truer story

Standard deviation is best for comparing assets where losses and gains are roughly symmetrical—most bond indices, balanced funds, or highly diversified portfolios. It is also the familiar metric; most fund databases report it, and advisors and investors understand it intuitively.

Downside deviation shines when evaluating strategies designed to capture upside while limiting downside: option-based strategies, volatility-targeting funds, and hedge fund approaches. It also mirrors how people *feel* about risk: no investor lies awake worrying about returns that exceeded their goal.

In practice, downside deviation often reveals that certain assets—particularly equity-heavy or tail-hedged portfolios—are less risky than standard deviation suggests. A stock fund that returns +40%, −5%, +35%, −8%, +50% will show ugly standard deviation but tamer downside deviation if you define "bad" as anything below 0%. Conversely, a fund that is smooth and low-volatility but never delivers returns above a target (such as a money market fund) may show similar standard and downside deviation, revealing the true cost of safety.

## Choosing your target

Downside deviation requires an explicit definition of what counts as failure. Three common targets emerge:

**Zero.** Any negative return is below-target. This suits risk-averse investors and is easy to explain—losses hurt, gains don't. It works well for defensive portfolios.

**Required return or minimum goal.** If you need 5% annually, only returns below 5% count as risky. This frames risk relative to your objective, not to market conventions. It aligns risk measurement with your actual financial plan.

**Benchmark or inflation.** Some investors target matching an index or beating inflation. Downside deviation then measures how often (and by how much) the portfolio underperforms. This is common among professional managers.

The target you choose materially changes the result. A fund with returns of 8%, 12%, 6%, 10%, 15% has different downside deviations under a 0% target, a 10% target, and a 7% target. There is no universally "correct" target—it depends on your economic reality.

## Downside deviation in portfolios and ratios

The [Sortino ratio](/sortino-ratio/) divides excess return by downside deviation, offering a risk-adjusted return metric that focuses on losses. It often ranks portfolios differently than the Sharpe ratio (which uses standard deviation). A strategy that wins big most of the time but crashes occasionally will have a high Sharpe ratio (capturing the crash as high volatility) but may have a lower Sortino (since the crash is one downside event, and most returns are upside, which doesn't count as risk).

When constructing a portfolio, downside deviation can reveal hidden correlations: two assets with low standard deviations may have higher downside deviation if they both stumble during the same market stress events. Conversely, an asset that bounces around a lot but rarely posts truly bad returns will look safer under downside than standard deviation.

## Limitations and caveats

Downside deviation ignores sequence risk and tail events. A fund that loses 50% once in twenty years will show up with higher downside deviation than one that loses 2% every year—even though the steady loser may be psychologically harder to tolerate. Also, choosing a target is subjective; changing it changes conclusions, and there is a risk of selecting a target after seeing results (a form of data snooping).

Standard deviation, for all its symmetry bias, has the advantage of stability: it is harder to manipulate, easier to compare across databases, and reflects the actual volatility an investor experiences day to day. For most published fund comparisons and research, standard deviation remains the default.

Neither metric captures [tail risk](/tail-risk/) or black-swan events—both smooth returns and rare catastrophes can hide in a small standard or downside deviation. They are tools for understanding recent, typical behavior, not guarantees about the future.

## See also

<div class="wiki-seealso">

### Closely related

- [Sortino ratio](/sortino-ratio/) — risk-adjusted return using downside deviation instead of standard deviation
- [Sharpe ratio](/sharpe-ratio/) — risk-adjusted return using standard deviation
- Volatility — how price swings are measured and annualized
- [Value-at-risk](/value-at-risk/) — another loss-focused risk metric
- [Tail risk](/tail-risk/) — rare, extreme outcomes that symmetric measures may underestimate

### Wider context

- [Risk-weighted assets](/risk-weighted-assets/) — how banks measure their own risk exposure
- [Beta](/beta/) — systematic risk relative to a benchmark
- [Concentration risk](/concentration-risk/) — how large single positions amplify portfolio risk

</div>

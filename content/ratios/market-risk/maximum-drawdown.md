---
title: "Maximum Drawdown"
description: "The largest peak-to-trough percentage decline in the value of an investment or portfolio over a specific period."
keywords:
  - maximum drawdown
  - drawdown
  - peak to trough
  - portfolio loss
  - recovery time
  - capital preservation
image: "/svg/ratios.svg"
---

*The **maximum drawdown** is the steepest cumulative loss an investor would have suffered if they held an investment from its highest point to its lowest point before recovery. It captures the worst case an actual holder faced, making it essential for assessing whether a strategy's return is worth the worst-case pain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maximum Drawdown — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">The deepest underwater period; measures worst-case loss from peak to trough.</div>

|   |   |
|---|---|
| **What it is** | Largest cumulative percentage decline from a previous peak to a subsequent trough in portfolio or security value |
| **Calculation** | (Trough Value − Peak Value) / Peak Value, expressed as a negative percentage |
| **Time frame** | Can be measured over any period: one year, five years, inception to date |
| **Volatility vs. drawdown** | Volatility is the standard deviation of returns; drawdown is the worst actual loss experienced |
| **Recovery time** | The period from trough back to the previous peak; not part of the drawdown metric itself |
| **Psychological impact** | Often determines whether investors will stay the course or abandon a strategy |
| **Frequency** | Multiple drawdowns may occur in a given period; the metric reports only the maximum one |

</aside>

## Why peak to trough matters more than volatility alone

Volatility tells an investor how much a portfolio jiggles on average. A portfolio might have 15% annualized volatility—meaning monthly returns swing by 4% or so—yet never fall more than 8% from peak to trough. Conversely, another portfolio with identical volatility might have plummeted 35% at some point, even though its average monthly jiggle was the same.

The maximum drawdown captures what an actual investor experiences. If you bought a fund at $100 and watched it fall to $65 before climbing back, you lived through a 35% maximum drawdown. The volatility figure wouldn't have warned you of that severity. For this reason, drawdown is often more psychologically and financially relevant than volatility alone.

An investor who can tolerate volatility on paper may panic-sell during a 40% drawdown. A retiree drawing income from a portfolio needs to know whether a drawdown is 10% (annoying but manageable) or 50% (potentially catastrophic if it happens early in retirement). Volatility alone doesn't answer that.

## Calculation and concrete example

The formula is straightforward:

**Maximum Drawdown = (Trough Value − Peak Value) / Peak Value**

Suppose a [mutual fund](/mutual-fund/) had the following monthly ending values over two years:

- Month 0: $100 (starting)
- Climbs to a peak of $125 by month 6
- Falls to $92 by month 9 (drawdown from peak: (92 − 125) / 125 = −26.4%)
- Recovers to $130 by month 18
- Falls to $105 by month 20 (drawdown from peak: (105 − 130) / 130 = −19.2%)
- Ends at $128 by month 24

The maximum drawdown over the two years is −26.4%, the worst trough-from-peak loss regardless of when it occurred or how quickly recovery happened.

This is different from a one-period loss. If the fund had lost 26% in a single month, that's a different concept (a one-month return); maximum drawdown is the cumulative loss across multiple periods, from the highest point touched down to the lowest point before recovery begins.

## Drawdown severity and investor psychology

A −10% maximum drawdown is usually tolerable; many investors expect at least that in normal markets. A −20% maximum drawdown is significant and will trigger anxiety in conservative portfolios. A −40% maximum drawdown, like many equities suffered in 2008 or 2020, forces the genuine question of whether the strategy is right for the investor.

Research in behavioral finance shows that investors are far more sensitive to losses than to equivalent gains—a phenomenon called [loss aversion](/loss-aversion/). A portfolio that is down 30% requires a 43% gain just to break even. This mathematical asymmetry, combined with psychological pain, means a large drawdown often causes investors to abandon a strategy right before recovery, locking in losses.

For this reason, many [hedge funds](/hedge-fund/) and managed accounts explicitly manage to drawdown limits—not just because it reduces risk, but because it increases the probability that investors will stay invested long enough for compounding to work.

## Drawdown versus return: the trade-off

A strategy that returns 8% annually with a −15% maximum drawdown is generally preferable to one returning 9% with a −40% maximum drawdown, even though the second has higher absolute return. The [Calmar ratio](/calmar-ratio/) and [Sharpe ratio](/sharpe-ratio/) both formalize this trade-off by penalizing larger drawdowns.

However, the relationship is not linear. A strategy returning 20% with a −30% drawdown might still be worth holding for a long-term investor, despite the pain, because the excess return compounded over decades far outweighs the single bad year. A retiree withdrawing 5% annually might not tolerate that volatility at all. Context matters.

## Recovery time: the hidden cost of drawdown

Maximum drawdown itself doesn't measure how long recovery takes. A fund that falls 30% in month 1 and recovers by month 3 is very different from one that falls 30% and takes three years to climb back. The second investor experiences a far longer period of regret and opportunity cost.

If recovery takes years, opportunity cost compounds. Money trapped in a sinking portfolio could have been deployed elsewhere. For this reason, investors often pair maximum drawdown with "recovery time" or measure underwater duration—the total number of periods the portfolio spent below the previous peak.

[Calmar ratio](/calmar-ratio/) indirectly penalizes slow recovery because a fund that takes years to recover will have lower annualized returns over the measurement period, weakening the Calmar ratio even if the drawdown percentage itself is the same as a fast-recovering rival.

## Maximum drawdown across asset classes

Equities typically have high maximum drawdowns—−40% to −60% in severe bear markets—balanced by long-term upside. Bonds are usually in the −10% to −20% range. Alternatives like [hedge funds](/hedge-fund/) or [managed futures](/managed-futures/) often boast maximum drawdowns of −15% to −25%, part of their appeal to risk-conscious investors.

These ranges shift with market environment. During deflationary crises like 2008, bonds held up better than equities. In inflationary environments, bonds suffer alongside equities. A portfolio's maximum drawdown is thus a function of its [asset allocation](/asset-allocation/) and the particular market regime in its historical sample.

## Limitations and context

Maximum drawdown is backward-looking. A strategy with a −10% drawdown over the past five years might suffer a −50% drawdown in the next crisis if its risk management is brittle or if it's exposed to an unproven tail scenario. Investors should not extrapolate past maximum drawdown as a ceiling on future losses.

The metric also depends on the time frame. A fund that suffered a −35% drawdown between 2008 and 2009 looks worse if measured from 2006 inception to date, yet might look better if measured from 2010 onward. Long measurement windows that include bear markets are more credible than short windows that miss them.

Finally, maximum drawdown is a single data point—it tells you the worst loss but not the distribution of drawdown frequency or severity. A strategy might have one catastrophic −50% drawdown or ten −20% drawdowns; both could have the same maximum drawdown but very different risk profiles. Pairing the metric with frequency analysis is wise.

## See also

<div class="wiki-seealso">

### Closely related

- [Calmar Ratio](/calmar-ratio/) — annualized return divided by maximum drawdown
- [Sharpe Ratio](/sharpe-ratio/) — risk-adjusted return using volatility rather than drawdown
- [Omega Ratio](/omega-ratio/) — probability-weighted gains versus losses; alternative to drawdown focus
- [Information Ratio](/information-ratio/) — excess return versus tracking error; benchmark-relative
- [Value at Risk](/value-at-risk/) — worst-case loss at a given confidence level; complements drawdown analysis
- Underwater Duration — time spent below previous peak; complements drawdown severity

### Wider context

- Risk Management — broader framework in which drawdown control sits
- Behavioral Finance — loss aversion and investor psychology around drawdowns
- [Asset Allocation](/asset-allocation/) — strategic decisions that determine expected maximum drawdown
- [Hedge Fund](/hedge-fund/) — vehicles evaluated heavily on drawdown control
- [Managed Futures](/managed-futures/) — strategy type emphasizing drawdown mitigation

</div>

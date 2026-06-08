---
title: "Calmar Ratio"
description: "Risk-adjusted return metric dividing annualized return by maximum drawdown, favored by commodity trading advisor analysis."
keywords:
  - calmar ratio
  - risk-adjusted returns
  - commodity trading advisors
  - maximum drawdown
  - hedge fund performance
image: "/svg/funds.svg"
---

*The **Calmar ratio** measures how much annual return a fund generates for each unit of downside risk it endures. It divides annualized return by maximum drawdown—the steepest peak-to-trough decline—making it a favourite among hedge fund managers who trade commodities and futures, where volatility is brutal and drawdowns are the real test of strategy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Calmar Ratio — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for funds and indices." />

<div class="wiki-infobox-caption">A metric that weights profit against the worst loss a fund has suffered.</div>

|   |   |
|---|---|
| **Formula** | Annualized return ÷ absolute value of max drawdown |
| **Also called** | Drawdown ratio |
| **Best used for** | [Commodity trading advisors](/commodity-trading-advisor/), trend-following strategies |
| **Strength** | Focuses on actual pain, not volatility |
| **Weakness** | Penalizes recovery; one large loss can dominate years of good performance |
| **Typical range** | 0.5 to 3+ (higher is better) |

</aside>

## The logic behind a single bad month

Most risk-adjusted return metrics fret about volatility—squaring deviations from average return. But volatility can swing both ways, and investors don't care equally about upside noise and downside losses. The Calmar ratio sidesteps that abstraction. It asks: how much profit do I get for tolerating the worst loss this fund ever took?

A fund posting 20% annual return with a 10% maximum drawdown earns a Calmar of 2.0. Another posting 15% return with a 5% drawdown earns 3.0. The second has converted each unit of maximum pain into more profit—a cleaner signal if you're managing real capital and real anxiety.

For [commodity trading advisors](/commodity-trading-advisor/) and trend-following [hedge funds](/hedge-fund/), this framing makes intuitive sense. These strategies can suffer sharp, sudden losses when a commodity rally reverses or volatility spikes. Calmar doesn't smooth that away; it puts it front and centre.

## How it differs from Sharpe

The [Sharpe ratio](/sharpe-ratio/) divides excess return by standard deviation—a mathematical average of how much returns wander from the mean. A strategy with mostly small ups and occasional devastating crashes can have a decent Sharpe if the small ups balance the crashes enough on average. Calmar ignores the distribution entirely and fastens on the single worst moment.

This difference matters. A trend-following fund might post returns distributed oddly—years of steady small gains interrupted by a 30% drawdown during a flash crash. Its Sharpe looks mediocre because volatility is high; its Calmar might be poor for the same reason. An options seller grinding out steady 15% yearly returns with no big loss might excel on Sharpe but suffer on Calmar, since it has never been stress-tested by a true drawdown.

The [Sharpe ratio limitations in hedge funds](/hedge-fund-sharpe-ratio-critique/) often stem from this mismatch: Sharpe assumes normal, bell-shaped returns. Reality, especially in alternatives, is skewed and fat-tailed.

## Persistence and the recovery problem

One quirk of Calmar: it locks a fund's worst drawdown in place forever, unless and until the fund posts a new one. If a [hedge fund](/hedge-fund/) suffered a 25% loss in 2008 but has delivered steady 12% annual returns for the past decade, that 2008 drawdown still dominates its Calmar calculation. Recovery doesn't erase it; only a worse drawdown changes the metric.

This can penalise recovering funds unfairly. A manager who weathered a genuine crisis and learned from it may show worse Calmar five years later than five years earlier, even though returns have improved, because the absolute drawdown figure doesn't budge.

Conversely, a young fund with no large losses yet can sport an artificially high Calmar. It hasn't been tested. Once it encounters a real stress scenario—a [market correction](/bear-market/), [liquidity crisis](/liquidity-risk/), or sector crash—its drawdown rises and Calmar falls sharply. Investors comparing a pristine young manager to a weathered one using Calmar alone might misread the comparison entirely.

## Where Calmar shines

For funds where strategy success hinges on managing drawdowns—[commodity trading advisors](/commodity-trading-advisor/), [trend-following](/trend-following/) systems, and [funds of funds](/fund-of-funds/)—Calmar offers useful focus. It forces an honest conversation about worst-case loss versus profit. A 2.0 Calmar means the fund printed two dollars for every dollar of maximum drawdown it inflicted. That's informative.

Calmar also avoids the assumption of normal returns. It doesn't care whether losses come from a few black swans or many small ones; only magnitude matters. For [hedge funds](/hedge-fund/) with skewed or multimodal return distributions, this robustness is an asset.

Yet no single ratio tells the full story. Calmar should travel with [Sharpe](/sharpe-ratio/), maximum consecutive losing months, and recovery period—the time it took the fund to claw back a drawdown. A fund with a dazzling 3.0 Calmar but a three-year recovery period looks different than one that bounced back in three months. Calmar captures intensity of drawdown; it cannot capture duration.

## See also

<div class="wiki-seealso">

### Closely related

- [Maximum drawdown](/maximum-drawdown/) — the peak-to-trough loss metric Calmar uses in its denominator
- [Sharpe ratio](/sharpe-ratio/) — the most common risk-adjusted return measure; uses volatility instead
- Hedge fund performance metrics — a survey of how professionals evaluate manager skill
- [Commodity trading advisor](/commodity-trading-advisor/) — the strategy type where Calmar is most often cited
- [Hedge fund](/hedge-fund/) — the broader asset class this metric serves

### Wider context

- Risk-adjusted returns — the category of metrics that standardize return for risk taken
- Volatility — standard deviation of returns; often called historical volatility
- Drawdown — any peak-to-trough decline in an investment's value

</div>

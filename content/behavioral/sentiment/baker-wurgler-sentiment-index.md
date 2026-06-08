---
title: "Baker-Wurgler Sentiment Index"
description: "A composite measure of investor sentiment derived from IPO volume, equity turnover, dividend initiations, and closed-end fund discounts, used to predict market returns and volatility cycles."
keywords:
  - sentiment index
  - Baker Wurgler
  - IPO volume
  - equity turnover
  - market prediction
image: "/svg/behavioral.svg"
---

*Malcom Baker and Jeffrey Wurgler built a sentiment index to capture the collective mood of the market. Rather than relying on surveys of investor optimism—which are subjective and often shallow—they assembled objective trading data into a single number: IPO volume, turnover, closed-end fund premiums, dividend payments, and equity issuance. The index is powerful because it aggregates real behaviour, not opinions, and because it predicts subsequent returns.*

## Why traditional sentiment surveys fall short

The most straightforward way to measure sentiment is to ask investors how they feel. Surveys from the American Association of Individual Investors, Investor's Intelligence, and others have tracked confidence levels for decades. But surveys have flaws: respondents may not articulate true beliefs, responses depend on wording, and survey samples are small and unrepresentative.

Worse, surveys are reactive and backward-looking. Investors report confidence or fear based on recent experience, making surveys inherently procyclical—they tend to be highest near market tops and lowest near market bottoms, exactly when contrarian readings would be useful.

Baker and Wurgler recognised that if sentiment is real, it should leave fingerprints in actual trading behaviour. Irrational optimism would manifest as high IPO volumes, rapid equity turnover, low dividend yields, and premiums on closed-end funds. Irrational pessimism would manifest as the opposite. They set out to capture these signals in one composite index.

## The components of the index

The original Baker-Wurgler index combines six components, equalweighted and standardised:

**IPO volume and first-day returns.** When sentiment is high, investors are eager to buy newly public firms and bid up first-day returns. When sentiment is low, IPO markets freeze. Both the number of IPOs and their first-day performance signal underlying demand for new equity risk.

**Equity issuance relative to debt issuance.** High sentiment encourages firms to issue equity (cheap relative to intrinsic value, in the eyes of management). Low sentiment makes equity issuance difficult and expensive, pushing firms to debt. The ratio of seasoned equity offerings to total corporate issuance captures this toggle.

**Stock market turnover.** High sentiment correlates with rapid trading, as optimistic investors chase momentum and overconfident traders increase activity. Turnover rises, though this component is noisy because institutions' algorithmic trading can inflate volume.

**Volatility.** Sentiment swings are accompanied by spikes in implied and realised volatility. High sentiment often manifests as low realised volatility (complacency), while sentiment crashes see sharp spikes. The original index uses lagged realised volatility.

**Dividend premium.** Stocks initiating dividends typically underperform in the short run, and premium initiators outperform later. Baker and Wurgler define the premium as the difference in average returns between dividend initiators and non-initiators. High sentiment depresses this premium (markets care less about dividends); low sentiment elevates it.

**Closed-end fund discount.** As discussed in depth in the [closed-end fund discount](/closed-end-fund-discount/) entry, the average discount (price to net asset value) of closed-end equity funds reflects retail investor sentiment. Wide discounts signal pessimism; narrow discounts or premiums signal optimism.

These six components are normalised to have mean zero and unit variance over the sample period, then averaged to produce a single index ranging from roughly -2 to +2.

## Predictive power

The index's strength lies in its predictive ability. In historical testing from 1960 onward, high sentiment indices forecast lower returns in subsequent months and years. A sentiment index value of +1 standard deviation above mean predicts annual returns roughly 3 to 5 percentage points lower than average, a material effect.

Conversely, low sentiment (index near -1) predicts above-average returns. This predictive pattern holds in expansions and recessions, across market caps, and internationally (though the components vary by country).

The index also predicts volatility. High sentiment periods tend to be followed by increased volatility, consistent with the idea that overextended sentiment reversals are abrupt and violent.

Importantly, the index has predictive power beyond what standard valuation ratios provide. The [price-to-earnings ratio](/price-to-earnings-ratio/) and [market capitalization](/market-capitalization/) relative to GDP can be elevated when sentiment is high, but the sentiment index captures something additional: the willingness of retail investors and firms to take risk and issue equity.

## Interpretation and caveats

A high Baker-Wurgler index does not mean the market will crash tomorrow. Sentiment can remain elevated for months or years while prices continue to rise. The index predicts mean reversion eventually, not timing.

Moreover, the index is backward-looking. All six components are historical: past IPO volume, past turnover, past dividends. By the time the index reaches an extreme, some of the sentiment shift may already be priced in. The index is most useful when it reaches multi-decade extremes and contradicts the prevailing market narrative.

The index is also mechanical. It treats all six components equally, but in some periods one component may be more relevant than others. For example, low turnover can reflect structural shifts in market microstructure (the rise of passive investing, circuit breakers) rather than sentiment decline. During the 2010s, falling turnover was as much about declining volatility and passive adoption as about changed sentiment.

The dividend component is particularly sensitive to tax law changes. After the Jobs and Growth Tax Relief Reconciliation Act of 2003 lowered dividend tax rates, dividend initiations surged for reasons unrelated to sentiment, inflating the index artificially.

Despite these caveats, the index has proved robust. Academic research and practical trading have documented that extreme readings often precede reversals or volatility spikes.

## Real-world application

Practitioners use the Baker-Wurgler index in several ways. Some treat it as a market-timing tool, raising cash when it is extreme high and deploying when it is extreme low. Others use it to adjust portfolio risk—increasing long equity positions when sentiment is depressed, reducing when elevated.

Asset allocation frameworks sometimes embed the index as a signal of valuation dispersion. When sentiment is high, the performance spread between value and growth tends to widen, as growth stocks benefit more from optimism while value stocks lag. Conversely, sentiment crashes tend to hurt high-volatility growth most, creating sector rotation opportunities.

Hedge funds and quantitative traders often incorporate the index into factor models alongside other predictors like momentum, [value](/value-investing/), and carry. Its predictive power, though modest in any single month, compounds over long periods.

## See also

<div class="wiki-seealso">

### Closely related

- [Closed-End Fund Discount](/closed-end-fund-discount/) — One of the six components, reflecting retail investor sentiment
- [Retail Investor Sentiment](/retail-investor-sentiment/) — The behaviour underlying sentiment index movements
- [Noise Trader Risk](/noise-trader-risk/) — The theoretical framework explaining why sentiment matters for returns
- [Market Timing](/market-timing/) — The application of sentiment indices to allocation decisions
- [Implied Volatility](/implied-volatility/) — Another sentiment-driven indicator
- [Initial Public Offering](/initial-public-offering/) — Whose volume and first-day performance feed the index
- [Stock Market](/stock-market/) — The arena in which sentiment fluctuates

### Wider context

- Behavioral Finance — The field grounding sentiment measurement
- [Price to Earnings Ratio](/price-to-earnings-ratio/) — A fundamental valuation measure supplemented by sentiment
- [Business Cycle](/business-cycle/) — The macro backdrop against which sentiment swings occur
- Risk Premium — Sentiment drives time-variation in risk premia

</div>

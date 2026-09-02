---
title: "Quality Adjustment in CPI"
description: "Methodology for accounting for improved product quality in the Consumer Price Index to avoid overstating inflation."
keywords:
  - CPI
  - inflation measurement
  - quality adjustment
  - hedonic pricing
  - substitution bias
  - methodology
  - consumer price index
---

*When the [Consumer Price Index](/wiki/consumer-price-index/) (CPI) measures the cost of living, it must account for the fact that products improve over time. A smartphone today has far more power than one from 2005, and a car is far more reliable. **Quality adjustment in CPI** is the statistical method used to isolate the true price change—how much of the bill increase is due to inflation vs. how much is due to the product being better? Without it, CPI would systematically overstate [inflation](/wiki/inflation/) by conflating price rises with quality advances.*

## The core problem

Suppose a car cost $30,000 in 2010 and the same model costs $35,000 in 2024. A naive calculation would say price rose 16.7%. But if the 2024 model has better fuel efficiency, a larger screen, superior crash-test ratings, and longer-lasting components, is the car really 16.7% more expensive, or is it mostly worth more because it is substantially better?

This problem became acute with technology. The original iPhone cost $599 in 2007; flagship phones today cost $1,200. Without quality adjustment, this would suggest smartphone inflation of 100%. But 2024 iPhones have processors millions of times faster, radically better cameras, always-on connectivity, and vastly longer battery life. Most economists agree phones are not 100% more expensive in real terms—they're better, and the quality improvement offsets much of the nominal price rise.

## Hedonic pricing method

The standard adjustment technique is **hedonic pricing**. Statisticians run regressions that decompose a product's price into its characteristics: processor speed, RAM, screen size, battery life, etc. Each characteristic is assigned a marginal price. If RAM increased by 2 GB between two observations, the hedonic model estimates the price change attributable to that RAM boost, then strips it out to isolate the "pure" price change.

For a car, hedonic models regress price on engine displacement, weight, safety features, fuel economy, and warranty length. For a refrigerator, they use capacity, energy efficiency, and features like ice-makers. The Bureau of Labor Statistics (BLS) employs this method for technology, appliances, and vehicles, which account for a significant chunk of CPI weighting.

The advantage is precision: each feature gets a price. The disadvantage is that the regression coefficients are estimates—they vary with the sample and time period—and new features (smartphone cameras in 2007) or disappearing features (cassette decks in cars) are hard to value because there's no historical price data.

## Alternative: linking and direct comparison

When hedonic regressions are unreliable, the BLS uses **direct comparison** or **linking**. If a specific model of refrigerator is discontinuedand replaced by a new one, statisticians examine the two models' features side by side and judge whether the new one is "better," "the same," or "worse." If it's better, they assume the price increase is partly quality improvement and apply a quality adjustment. If it's the same, the full price change counts as inflation.

Linking has the virtue of simplicity but is subjective. Different appraisers might assess quality improvement differently, introducing bias.

## Substitution bias and quality adjustment

Quality adjustment is intimately tied to [substitution bias](/wiki/substitution-bias-inflation/) in CPI. The headline index uses a fixed basket of goods—the same model of car, loaf of bread, etc. If a product becomes expensive relative to substitutes, consumers switch, but CPI doesn't. Over time, the gap between the fixed-basket CPI and a [chained](/wiki/chained-cpi/) or geometric-mean index grows.

Quality adjustment attempts to reduce this gap by revaluing the old product to account for quality deficiency. If a 2010 car was worse than a 2024 car, and consumers have switched to the 2024 model, the 2010 version's price is implicitly lower after adjustment, reducing the measured inflation.

## Controversy and biases

Critics argue that quality adjustment is a form of measurement fudging. If the BLS is constantly stripping out quality improvements, isn't it inventing reasons why prices haven't "really" risen? In the 2000s and 2010s, when official CPI was 2–3% but many consumers felt prices (especially healthcare, education, housing, childcare) were rising far faster, some blame fell on excessive quality adjustment.

The converse risk exists too: the BLS might miss quality *deterioration*. A cheaper car with fewer safety features or less durable materials should see negative quality adjustment, but the methodology might miss this.

There's also a small bias in hedonic models toward high-income consumers. When the BLS values a feature (e.g., a larger screen), it often uses implicit prices derived from higher-income households' purchases. A low-income consumer who doesn't value that feature is ignored, leading to overstatement of quality improvement for that segment.

## Scale and impact

Quality adjustment matters most for goods with rapid innovation: technology, cars, appliances, medical equipment. For food, energy, and basic services, quality improvement is slower and harder to measure, so adjustments are smaller.

Historically, quality adjustment has reduced measured inflation by roughly 0.3–0.5 percentage points annually in the United States. For technology alone, the BLS estimates quality adjustments of 5–10% annually because feature improvements and performance gains are so rapid. This is not a rounding error—it materially affects [inflation-targeting](/wiki/inflation-targeting/) decisions at the [Federal Reserve](/wiki/federal-reserve/).

## Alternatives: hedging quality in indices

Some economists propose that instead of adjusting CPI prices, we should ask whether the [cost of living](/wiki/purchasing-power-parity/) has actually risen. The [Personal Consumption Expenditures (PCE) deflator](/wiki/personal-consumption-expenditures-price-index/) and chained-CPI (which allow substitution dynamically) address this differently: they reweight the basket as consumers switch goods, avoiding some of the quality adjustment problem.

Another approach is to publish multiple inflation measures: headline CPI (no adjustments), adjusted CPI (with quality adjustments), and chained CPI. Readers can choose based on their view of what "inflation" means to them.

<div class="wiki-seealso">

### Closely related
- [Consumer Price Index](/wiki/consumer-price-index/) — the headline inflation measure relying on quality adjustments
- [Substitution Bias](/wiki/substitution-bias-inflation/) — CPI error from fixed baskets; quality adjustment is one correction
- [Personal Consumption Expenditures Price Index](/wiki/personal-consumption-expenditures-price-index/) — alternative using chaining to reduce bias
- [Inflation](/wiki/inflation/) — the phenomenon CPI measures, complicated by quality change

### Wider context
- [GDP Deflator](/wiki/gdp-deflator/) — a different inflation measure from national accounts
- [Core Inflation](/wiki/core-inflation/) — inflation excluding volatile items; still subject to quality adjustment
- [Inflation Targeting](/wiki/inflation-targeting/) — central banks' reliance on inflation measures like CPI to set [interest rates](/wiki/federal-funds-rate/)
- [Purchasing Power Parity](/wiki/purchasing-power-parity/) — comparing living costs across countries, also complicated by quality differences

</div>

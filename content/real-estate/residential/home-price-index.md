---
title: "Home Price Index"
description: "A statistical measure that tracks residential price movements over time by comparing repeat sales of the same properties, isolating appreciation from compositional changes."
keywords:
  - home price index
  - case-shiller index
  - repeat sales methodology
  - residential prices
  - hedonic pricing
  - price growth
image: "/svg/real-estate.svg"
---

*A **home price index** is a time-series measure of [residential-real-estate](/residential-real-estate/) value that isolates genuine price appreciation from shifts in neighbourhood composition, property mix, or sales quality. The most authoritative version, the **Case-Shiller index**, compares identical homes sold multiple times over decades, stripping away the confounding effect of comparing a 2000-square-foot 1970s colonial to a 3000-square-foot new construction in the same year.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Home Price Index — key facts</div>

<img src="/svg/real-estate.svg" alt="An abstract mark representing real-estate valuation." />

<div class="wiki-infobox-caption">A statistical tool that measures residential appreciation by tracking the same properties over time, eliminating compositional bias.</div>

|   |   |
|---|---|
| **What it is** | A longitudinal price measure based on repeat sales of individual homes |
| **Core methodology** | Pair-wise comparison of matched properties sold at two different time points |
| **Primary advantage** | Holds property characteristics constant, isolating true price movement |
| **Most common variant** | S&P Case-Shiller Index (national and metropolitan-area versions) |
| **Alternative approach** | Hedonic regression, which weights property attributes and estimates prices from them |
| **Lag and granularity** | Typically 2–3 months behind current sales; monthly or quarterly releases |

</aside>

## The compositional problem

A naive price index simply averages all home sales in a period and compares it to the prior period. If the median price in Suburb A rises from $300,000 to $330,000 year-over-year, a naive interpreter declares 10 per cent appreciation. But that conclusion is fragile.

What if the 2024 sample skewed toward larger, newer properties while the 2023 sample was skewed toward older, smaller homes on the same streets? The 10 per cent gain might be entirely compositional—you're comparing apples to oranges—and actual [residential-real-estate](/residential-real-estate/) price growth on *identical* homes might be flat or negative. This was a chronic problem in housing data before the 1980s: reported indices would rise, but you couldn't trust whether it was real appreciation or just a shift in what was being sold.

## The repeat-sales approach

Karl Case and Robert Shiller (later joined by Ishan Sen) invented the repeat-sales framework to solve it. The method is conceptually simple: identify every home that sold at least twice over a defined period, compare the earlier sale price to the later one, and construct an index from those price changes.

If a home on Oak Street sold for $200,000 in 2000 and $250,000 in 2024, that property appreciated 25 per cent—regardless of what else sold in the neighbourhood, regardless of whether it was renovated (the data tries to flag major alterations), and regardless of broader market composition. By aggregating thousands of such pairs, you build a price series that reflects genuine appreciation of comparable properties.

The Case-Shiller index exists in three forms: a national index, 20 major metropolitan areas, and 10 metropolitan divisions. The national series stretches back to 1987 (with some retroactive construction to 1975) and updated monthly with a two-month lag. The methodology weights each property pair equally, meaning a modest-value home in Detroit and a high-value home in San Francisco both count as a single data point—an assumption that some critics contest.

## Hedonic alternatives

Not all indices use repeat sales. The **hedonic pricing** model takes a different angle: it observes the sale price of *all* homes in a period, then estimates how much value each attribute—square footage, lot size, year built, number of bedrooms—contributes to the price. From those coefficients, it constructs an implicit price for a "standard" home and tracks changes in that standard home's value.

The Federal Housing Finance Agency (FHFA) publishes a hedonic index covering homes financed by Fannie Mae and Freddie Mac mortgages, which is useful for the broad conforming-loan market but excludes cash sales and jumbo loans. Zillow's Zestimate and other proprietary indices blend repeat-sales and hedonic methods, weighting recent sales more heavily.

Hedonic indices have two advantages: they use more of the available data (every sale, not just repeats), and they can interpolate where data is sparse. But they're more model-dependent; if you misweight bedroom count or underestimate the impact of neighbourhood gentrification, the results drift. Case-Shiller's constraint—you can only use homes with multiple sales—is mathematically cleaner, even if it throws away some information.

## What the index measures and doesn't

A home price index measures *market price*, the amount a willing buyer and a willing seller exchange for a property. It does not measure true economic value (what a [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) or income-based valuation would suggest), nor does it adjust for the *quality* of the transaction. A distressed foreclosure sale, an all-cash deal, and a standard 20 per cent down-payment purchase all count equally.

The index also doesn't capture financing terms. If a property sold for $300,000 in 2010 with a fixed-rate 4.5 per cent mortgage and for $350,000 in 2024 with a fixed-rate 7 per cent mortgage, the nominal 16.7 per cent price gain is offset by the fact that the buyer's debt service is now much higher. A purchaser's true affordability might have deteriorated, even though the index rose.

Similarly, the index measures the *price* at sale, not the value at each moment in between. If homes in a region sold heavily in one month at high prices and barely at all the next month at lower implied values, the index may underweight the month of sparse sales. This is why indices use smoothing and time-weighted aggregation to avoid seasonality distortions.

## Metropolitan and national variation

Case-Shiller's 20 metropolitan indices reveal persistent regional divergence. Some metropolitan areas (Phoenix, Las Vegas, Miami) experienced wild boom-and-bust cycles, while others (New York, Los Angeles) moved more steadily. These differences reflect local [business-cycle](/business-cycle/) strength, [construction-spending](/construction-spending/) patterns, and in-migration.

The national index smooths these variations and is most useful for macroeconomic analysis: Federal Reserve policy-makers monitor whether broad housing appreciation is outpacing [inflation](/inflation/) (a sign of a potential bubble) or lagging it (a sign of weakness in real [residential-real-estate](/residential-real-estate/) demand). Investors, by contrast, often use metropolitan indices to identify local [market-timing](/market-timing/) opportunities, though the two-month lag makes real-time trading difficult.

## The index in practice

Central banks, economists, and [real-estate-investment-trust](/real-estate-investment-trust/) managers use home price indices as a barometer. A persistent flattening of the index signals that housing demand is weakening relative to supply, often preceding recessions. A sharp spike can trigger concern about [inflation-risk](/inflation-risk/) and asset bubbles, prompting monetary tightening.

Individual investors use indices to gauge whether a local [housing-affordability-index](/housing-affordability-index/) has improved or deteriorated, informing decisions about [residential-real-estate](/residential-real-estate/) acquisitions and [real-estate-wholesaling](/real-estate-wholesaling/) opportunities. Property appraisers use indices to anchor valuation—a home's estimated value grows roughly in line with the local index, adjusted for property-specific factors.

The index's limitations matter in practice. A home price index that rose 5 per cent annually for ten years masks years where price fell 8 per cent (a crash) and years where price rose 15 per cent (a boom). Using the index to forecast future prices is notoriously unreliable; past appreciation is not predictive of future returns. And using the index to time entry or exit requires acknowledging that by the time the index confirms a trend, the trade may already be crowded and late.

## See also

<div class="wiki-seealso">

### Closely related

- [BRRRR Method](/brrrr-method/) — a rental-acquisition strategy using rehab and refinance to recycle capital
- [Housing Affordability Index](/housing-affordability-index/) — whether median-income households can afford median-priced homes at current rates
- [Real Estate Investment Trust](/real-estate-investment-trust/) — publicly traded entities that own and operate real-estate portfolios
- [Market Timing](/market-timing/) — the practice of buying and selling based on price-cycle predictions
- [Residential Real Estate](/residential-real-estate/) — the market for owner-occupied and rental homes

### Wider context

- [Inflation](/inflation/) — sustained price growth across an economy; indices adjust for it when measuring real returns
- [Construction Spending](/construction-spending/) — aggregate investment in building, driving long-term housing supply
- [Business Cycle](/business-cycle/) — economic expansions and contractions that correlate with housing markets
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — an economic-value approach that differs from market price

</div>

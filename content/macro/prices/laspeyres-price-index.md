---
title: "Laspeyres Price Index"
description: "A fixed-base price index that holds quantities constant and systematically overstates inflation, especially when prices rise unevenly across categories."
keywords:
  - laspeyres-index
  - fixed-basket-inflation
  - price-index-bias
  - substitution-bias
  - cpi-methodology
image: /svg/macro.svg
---

*A **Laspeyres Price Index** is a price measure that compares the cost of a fixed basket of goods—determined in a base period—to the same basket today. By design, it does not account for the fact that consumers substitute away from goods that have become expensive, leading it to systematically overstate the true rise in living costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Laspeyres Price Index — key facts</div>

<img src="/svg/macro.svg" alt="An abstract editorial mark for macroeconomic data." />

<div class="wiki-infobox-caption">The canonical inflation index, biased upward by its refusal to let baskets move.</div>

|   |   |
|---|---|
| **What it is** | Index number = (cost of base-period basket at current prices) ÷ (cost at base prices) × 100 |
| **Who uses it** | Most major [Consumer Price Indices](/consumer-price-index/) worldwide |
| **Key bias** | Substitution bias (overstates inflation when consumers shift to cheaper alternatives) |
| **Alternative** | [Paasche Price Index](/paasche-price-index/), Fisher index, or [hedonic pricing](/hedonic-pricing/) adjustments |
| **Base period** | Often reset every 10–20 years; US CPI uses a rolling base |

</aside>

## The fixed-basket trap

The Laspeyres index is named after the 19th-century economist Ernst Louis Étienne Laspeyres. The method is elegantly simple: define a basket of goods as it existed in year zero (say, 2000), then track how much that identical basket costs each year. If bread was 10% of household spending in 2000, then bread remains 10% of the index weight in 2024, regardless of actual eating habits.

This is the mathematical foundation of most official [Consumer Price Index](/consumer-price-index/) measures, and it has a seductive clarity. You know exactly what you are measuring: the price change of a fixed list of items. But that clarity comes at a cost. The Laspeyres index answers a hypothetical question—"How much more money would a 2000 household need to buy the same 2000 basket today?"—not the practical question households actually face: "How much does it now cost to live as well as we did before?"

## Substitution bias in action

Here is the distortion in practice. Suppose beef prices triple while chicken prices stay flat. A Laspeyres index, holding the basket fixed at 2000 proportions, counts the full beef price increase. But households do not buy the same amount of beef when it triples; they buy less beef and more chicken. The true cost of living rises less than the Laspeyres index suggests, because people have avoided some of the price shock by substituting.

The bigger and more uneven the price moves, the larger the bias. The 1970s energy crisis created wild substitution: households switched to more efficient appliances, drove less, insulated homes. Yet Laspeyres indices, locked to 1960s consumption patterns, exaggerated the inflation shock because they forced the old basket to remain constant.

This upward bias is not a bug in the formula—it is the inevitable result of asking a fixed-quantity question. The Laspeyres index is not *wrong*, but it is systematically biased toward showing more inflation than households actually experience, assuming they have the flexibility to adjust.

## Why governments use it anyway

Despite this upward bias, most central banks and statistical agencies rely on Laspeyres methodology (or close variants, like the [chained Consumer Price Index](/consumer-price-index/), which recalibrates the basket more frequently). They do so for several reasons.

First, **institutional persistence**. The index was codified in law in many countries; changing it requires legislative or regulatory action. Second, **lagged data**. To measure a true [Paasche Price Index](/paasche-price-index/), which uses current-period quantities, you must wait until you know what people actually bought—survey data lags. Laspeyres requires only current prices, not current quantities, so it can be published faster. Third, **political convenience**. An index that slightly overstates inflation deflates public complaints about rising living costs ("It's not as bad as the index says"). Governments and central banks have little incentive to adopt a lower-bias measure.

## The lag problem compound the bias

When the basket is updated only every decade or two, Laspeyres bias compounds. The US [Consumer Price Index](/consumer-price-index/) now rebases its weights periodically and uses geometric means to capture some substitution effects, but the core concept remains: a fixed basket held constant over the inter-rebase period.

[Shelter inflation](/shelter-inflation/), the largest CPI component, exemplifies this trap. The basket assumes people will keep spending the same fraction on housing even as rents or mortgage rates surge. In reality, households constrained by budget cuts, delay home purchases, or downsize. But the index records the full price rise, exaggerating inflation.

## Measuring the bias

Economists estimate Laspeyres substitution bias at 0.2–0.5 percentage points per year in developed economies. That may sound small, but compound it over decades: a Laspeyres index that reads 5% inflation annually, versus a true cost-of-living measure at 4.5%, creates a cumulative distortion that affects wage negotiations, policy decisions, and expectations.

The Federal Reserve has published alternate inflation indices (like the "sticky price" CPI) to try to tease out how much of headline inflation is true price pressures versus measurement artifacts. The gap between measures is sometimes substantial.

## See also

<div class="wiki-seealso">

### Closely related

- [Consumer Price Index](/consumer-price-index/) — the official inflation measure built largely on Laspeyres logic
- [Paasche Price Index](/paasche-price-index/) — uses current quantities and has downward bias, balancing Laspeyres upward bias
- [Core Inflation](/core-inflation/) — inflation excluding volatile items, still measured via Laspeyres
- [Hedonic Pricing](/hedonic-pricing/) — a technique to adjust for quality changes within a fixed basket
- [Inflation](/inflation/) — the general rise in price levels, measured (imperfectly) by indices like this

### Wider context

- [Central Bank](/central-bank/) — institutions that monitor inflation via Laspeyres-based measures
- [Deflation](/deflation/) — the opposite of inflation, also measured with Laspeyres bias
- [Monetary Policy](/monetary-policy/) — policy decisions informed by (biased) inflation indices

</div>

---
title: "Gravity Model of Trade"
description: "The gravity model of trade explains why bilateral trade flows are proportional to economic size and inversely related to distance; applications in policy evaluation."
keywords:
  - gravity model of trade explained
  - bilateral trade flows economic size
  - trade distance friction
  - gravity equation trade
  - trade agreement impact evaluation
image: /svg/macro.svg
---

*The **gravity model of trade** predicts that the flow of goods and services between two countries is proportional to their economic size (GDP) and inversely proportional to the distance between them—much as gravity pulls harder between larger, closer objects. A simple equation, widely validated by data, it is used to forecast the impact of trade agreements, estimate the effect of tariffs, and isolate the role of geography and policy in shaping global commerce.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gravity Model of Trade — key facts</div>

<img src="/svg/macro.svg" alt="An abstract editorial mark for macroeconomics." />

<div class="wiki-infobox-caption">The gravity equation is one of the most robust empirical findings in economics; distance and size explain most trade variance.</div>

|   |   |
|---|---|
| **Basic form** | Trade flow ∝ (GDP₁ × GDP₂) / Distance^θ |
| **Core empirical finding** | Doubling the distance reduces trade by ~40–50% |
| **Key coefficients** | GDP elasticity ≈ 1; distance semi-elasticity ≈ −0.7 to −1.0 |
| **"Distance" includes** | Physical miles, time zones, language, shared borders, colonial ties, tariffs |
| **Use case** | Benchmark trade prediction; counterfactual analysis (tariff, trade deal impact) |
| **Explanatory power** | 60–70% of bilateral trade variance in typical datasets |

</aside>

## The intuition and the equation

The gravity model is deceptively simple. Consider the United States and Canada. Both have large GDPs; they share a border; they speak largely the same language; they have deep supply chains. Trade between them is enormous. Now consider the United States and a country half as large, on the other side of the world, with a different language and no formal trade agreement. Trade is much smaller. The gravity model codifies this pattern.

The basic equation is:

**Trade(i,j) = A × [GDP(i) × GDP(j)]^β / [Distance(i,j)]^δ**

Where:
- **Trade(i,j)** is the bilateral flow (exports + imports, or a one-direction measure)
- **GDP(i), GDP(j)** are the national incomes of countries i and j
- **Distance(i,j)** is the physical or economic distance between them
- **A, β, δ** are parameters estimated from data

Empirically, β ≈ 1 (trade scales linearly with the product of GDPs), and δ ≈ 0.7 to 1.0 (each doubling of distance cuts trade by roughly 40–50%). The constant A captures global trade intensity and other omitted factors.

The intuition is straightforward: larger economies produce and consume more, so they are bigger trading partners. Distant economies face higher transport costs, tariffs, communication barriers, and cultural friction. Trade is harder; less of it happens.

## Beyond physical distance: effective distance

In practice, "distance" in the gravity equation encompasses far more than miles. Researchers augment the model with additional factors that predict bilateral trade:

- **Adjacency**: Sharing a border dramatically increases trade (often a 50–100% boost).
- **Language**: Shared official language raises trade by 20–40%, reflecting lower transaction costs and cultural affinity.
- **Colonial ties**: Former colonial relationships predict persistent trade flows even after independence.
- **Trade agreements**: A preferential trade deal (like NAFTA or the EU) increases bilateral trade by 50–200%, depending on depth.
- **Cultural and institutional distance**: Differences in legal systems, corruption, and governance; larger gaps reduce trade.
- **Infrastructure and logistics**: Poor ports, roads, or weak institutions in one partner raise effective distance.
- **Time zone overlap**: Countries in similar time zones trade more (easier communication and business hours overlap).

These factors are often incorporated as dummy variables (1 if true, 0 if false) or continuous indices alongside the core GDP and distance terms.

## Explaining the gravity model: theory and evidence

Why does gravity hold so reliably? Economists have offered several theories:

**The Krugman explanation** (1980s): Trade occurs because of comparative advantage and economies of scale. Larger economies enjoy more specialization and bigger markets; distant economies face transport costs that erode trade gains. The gravity equation emerges naturally from a model where goods are differentiated by origin, transport costs matter, and firms serve multiple markets.

**The Anderson-van Wincoop explanation** (2003): Trade between i and j depends not just on their bilateral distance and size, but on their size and distance relative to other trading partners. A large, distant country might trade heavily with a small nearby country if alternatives are scarce. This "multilateral resistance" introduces fixed effects by country that reflect the broader trade context. When these effects are included, the gravity fit improves dramatically.

**Supply chain logic**: Modern trade is not only final goods; it is components, intermediates, and services flowing back and forth. Proximity reduces inventory, transport time, and risk. Companies locate operations where production costs are low and supply chains are short. This supply-chain sensitivity to distance is particularly strong in electronics, automobiles, and textiles.

**Empirical validation** is overwhelming. Gravity models explain 60–70% of the variation in bilateral trade flows across thousands of country pairs and decades of data. The coefficients are stable across time, regions, and samples. Doubling distance consistently reduces trade by a large factor.

## Using gravity to evaluate trade agreements

The gravity model's most powerful application is **counterfactual analysis**: estimating what trade would have been absent a trade agreement, tariff, or policy change.

### Example: NAFTA's impact

Before NAFTA (1994), economists used gravity models fitted to pre-1994 data to forecast how much US-Mexico and US-Canada trade would be under NAFTA's preference. The model predicted a 40–60% boost to bilateral flows beyond what GDP growth and normal trends would deliver. Actual post-NAFTA data show US-Mexico trade rose sharply; US-Canada trade also grew. Researchers compare the actual flow to the gravity-model counterfactual (what trade "should be" given GDP, distance, etc.), and attribute the excess to the trade agreement. Most estimates credit NAFTA with 15–25% of actual trade growth above the baseline.

### Example: Tariff effects

If a government imposes a 10% tariff on imported automobiles, the gravity model helps predict the magnitude of trade decline. The tariff effectively increases the "cost distance" between trade partners. Calibrated models suggest a 10% tariff reduces trade by 8–15%, depending on elasticities. This quantitative prediction helps policymakers understand the economic footprint of protection.

## Critiques and limitations

The gravity model's simplicity is both strength and weakness. 

**Omitted variables**: Trade is driven by supply-chain integration, multinational firm networks, and factor endowments (labor costs, capital, natural resources) that gravity alone does not capture. Adding variables on human capital, capital-labor ratios, and institutional quality improves fit but also complexity.

**Reverse causation**: Does distance reduce trade, or do low-trade-cost technologies (fast shipping, videoconference, digital platforms) reduce the friction of distance? The model is descriptive; causality is harder to pin down.

**Structural breaks**: Gravity coefficients can shift if trade technology, logistics, or tariff regimes change fundamentally. The rise of e-commerce and global supply chains may be rewriting the distance coefficient.

**Aggregation**: Gravity works for total bilateral trade, but not always for specific sectors. Gravity predicts agricultural trade poorly; capital-intensive manufacturing fits better.

**Dynamic effects**: Gravity captures steady-state trade flows, not the transition path after a shock. A trade agreement's initial impact differs from long-run equilibrium as firms adjust.

## Modern extensions and recent research

Recent work has integrated gravity with:

- **Firm-level heterogeneity**: Models where only high-productivity firms export, and distance raises the productivity threshold to profitability. These "new new trade" models explain why a few firms dominate exports.
- **Supply chains and value-added trade**: Tracking where value is created across borders, not just bilateral goods flows. Gravity still applies but must account for intermediate flows.
- **Structural estimation**: Deriving gravity from first principles (consumer preferences, production functions, competition) rather than treating it as an empirical pattern.
- **Gravity and development**: Using gravity to measure bilateral trade "deficits"—countries trading less than gravity predicts. These deficits reflect policy, institutions, and infrastructure gaps.

## See also

<div class="wiki-seealso">

### Closely related

- [Comparative advantage](/comparative-advantage/) — the economic principle underlying why trade occurs and gravity predicts its volume
- Trade agreement — preferential deals (NAFTA, EU, CPTPP) that shift gravity coefficients
- Tariff — trade barriers that increase effective distance and reduce bilateral flows
- Supply chain — modern trade networks that gravity helps explain via distance sensitivity
- Export — one direction of bilateral flows; gravity predicts country-pair totals

### Wider context

- International trade — the broad field; gravity is a workhorse tool
- [Gross domestic product](/gross-domestic-product/) — the size variable in gravity; larger economies trade more
- Infrastructure — ports, roads, and logistics affect effective distance
- [Trade balance](/trade-balance/) — differences between imports and exports; gravity helps identify anomalies
- [Bretton Woods](/bretton-woods/) — historical context for modern trade system and tariff negotiations that gravity models help evaluate

</div>

---
title: "Maintenance versus Growth Capex"
description: "Splitting capital expenditure into sustaining (maintaining current revenue) and growth (creating new revenue) to refine DCF models."
keywords:
  - maintenance capex
  - growth capex
  - capital expenditure split
  - discretionary spending
  - maintenance capex ratio
  - growth investment
image: "/svg/valuation.svg"
---

*A company's [capex](/capex-maintenance-vs-growth/) serves two purposes: **maintenance capex** preserves existing revenue and operating capability, while **growth capex** creates new capacity and incremental revenue. Conflating them in a [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) can inflate or deflate the business's cash-generation ability. Explicitly splitting maintenance from growth often reveals the true economics.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maintenance versus Growth Capex — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Replacing versus expanding: two very different investments.</div>

|   |   |
|---|---|
| **What it is** | Capex classified by purpose: sustaining or creating |
| **Maintenance capex** | Replacement and upkeep; required to maintain current state |
| **Growth capex** | Incremental investment; generates new revenue or markets |
| **Key ratio** | Maintenance capex as % of depreciation or revenue |
| **Impact on FCF** | Influences sustainable free cash flow and reinvestment rate |
| **Typical split** | Ranges from 40/60 to 80/20 depending on industry and phase |

</aside>

## Why the split matters for valuation

A utility reports $500 million of annual capex. A growth-stage retailer reports $500 million of capex. They are not comparable figures. The utility's capex is mostly replacement—new pipes, transmission lines, aging equipment—needed just to maintain current revenue and reliability. The retailer's capex is store buildouts and distribution centres—growth investments that add revenue.

In a DCF, [free-cash-flow](/free-cash-flow/) is calculated as operating cash flow minus capex. If you treat all capex the same, a maintenance-heavy business looks less profitable than a growth-heavy one, even if they generate equal operating cash. The utility's $500M capex erodes its FCF; the retailer's $500M arguably generates future cash. Understanding the split lets you forecast each path correctly.

## Maintenance capex: the sustaining level

**Maintenance capex** is the annual spend required to keep the business running at its current capacity and revenue. A manufacturing plant has machinery with a 10-year life; each year, 10% of the fleet must be replaced just to stay even. An airline must overhaul engines, replace landing gear, and update avionics to maintain safety and flight hours. A telecom must upgrade trunk lines and replace aging cell towers to hold market share.

A rule of thumb: maintenance capex roughly equals **depreciation & amortisation** (D&A) over the long run. Not precisely—some assets might last longer or shorter than their accounting life—but in a stable business, D&A is a good proxy for the annual "keep the lights on" spend. If a company consistently reports $100M in D&A and $80M in capex, the gap suggests either the business is shrinking (capex < replacement), or the company is buying assets at bargain prices (market value < book value). If capex is $150M, either the company is building new capacity or is replacing at a faster rate than D&A suggests.

To estimate maintenance capex:
1. Start with reported [depreciation & amortisation](/accumulated-depreciation/).
2. Adjust for inflation. A dollar of capex today is worth more than a dollar was ten years ago. If inflation has averaged 2%, maintenance capex should grow by ~2% annually.
3. Look at [capital intensity](/capex-maintenance-vs-growth/) trends. Is the company getting more or less capital efficient? Improving efficiency might mean maintenance capex grows slower than revenue.
4. Sanity-check against peers. A competitor spending 3% of revenue on maintenance capex versus your company's 5% suggests either better efficiency or underinvestment.

## Growth capex: the investment in new earnings

**Growth capex** is the marginal spend that expands capacity, enters new markets, or builds new products. A retailer opening 50 new stores. A software company building a new data centre. A pharma company building a manufacturing facility for a new drug. This capex does not maintain the current state; it creates incremental future earnings.

The tricky part: growth capex is not "nice-to-have." In many industries, it is essential. A telecom without network expansion gets left behind. An e-commerce company that doesn't scale warehouses loses market share. Confusing growth capex with excess shareholder returns (or vice versa) distorts valuation.

To estimate growth capex:
1. Identify the company's stated growth trajectory. If management targets 10% annual revenue growth, how much incremental capex per dollar of new revenue?
2. Benchmark against industry capex-to-growth. In retail, opening stores might require 2–3% of revenue in growth capex to achieve 5–7% revenue growth. In software, growth capex (infrastructure) might be 1–1.5% of revenue.
3. Examine management's capital allocation strategy. Are they reinvesting heavily (growth), returning cash (mature), or acquiring? Capital intensity tells you their business model.
4. Check past correlation. If revenue grew 20% last year and capex grew 30%, perhaps 10% of capex fuelled growth and 20% was maintenance. Graph the relationship; it reveals the true capex burden.

## Constructing the split in a DCF

In your [forecast](/discounted-cash-flow-valuation/), you might allocate capex as follows:

| Year | Revenue | Growth | Maintenance Capex (2% of revenue) | Growth Capex (8% of growth) | Total Capex |
|---|---|---|---|---|---|
| 1 | $1,000M | 10% | $20M | $80M | $100M |
| 2 | $1,100M | 10% | $22M | $80M | $102M |
| 3 | $1,210M | 10% | $24M | $80M | $104M |
| Terminal | $1,331M | 3% | $27M | $9M | $36M |

In the terminal year (perpetual growth), growth capex shrinks because growth itself slows. A company cannot grow 10% forever; it will eventually revert to GDP-ish growth, maybe 2–3%. At that point, capex drops dramatically because incremental investment is minimal.

This split reveals something crucial: the company's **true reinvestment rate**. If growth capex is $80M and incremental operating cash flow from new stores is $150M, the company is highly profitable on marginal dollars. If growth capex is $200M for $150M incremental OCF, you're buying growth at a premium; the expected returns are lower. This shapes both valuation and hurdle rates.

## Testing your split: historical capex intensity

Audit your assumptions against history. Suppose you've modelled:
- Maintenance capex at 2.5% of revenue
- Growth capex at 8% of incremental revenue

Check the past three years:
- Year −2: Revenue $900M, Capex $85M (9.4%)
- Year −1: Revenue $950M, Capex $95M (10.0%)
- Year 0: Revenue $1,000M, Capex $105M (10.5%)

The company is spending 10–10.5% on capex total. If your forecast says 10.5% in Year 1 (2.5% maintenance + 8% growth on 10% revenue growth), that's consistent. But if you forecast 7% (assuming lower growth), you're predicting capex will drop. That's possible if growth slows and the company matures, but justify it. Otherwise, use history as your guide.

## Industry variation: when the split breaks down

Some industries have blurry lines between maintenance and growth. A cloud provider buying servers is partly maintenance (replacing depreciated hardware) and partly growth (adding capacity for customers). A pharma company investing in R&D creates future growth, but R&D is expensed, not capitalized. An oil driller's exploration capex is growth, while platform maintenance is sustaining; the split is clear, but exploration risk means growth returns are volatile.

Best practice: be specific about your business. If you're valuing a hospital REIT, maintenance is predictable and easily benchmarked. If you're valuing a growth-stage e-commerce player, growth capex is the dominant lever and has high optionality. Sensitivity-test your capex assumptions; small shifts in growth capex intensity can swing the valuation substantially.

## See also

<div class="wiki-seealso">

### Closely related

- [Free Cash Flow](/free-cash-flow/) — capex is a core component
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — where the split is applied
- [Depreciation](/depreciation/) — used as a benchmark for maintenance capex
- [Normalised Free Cash Flow](/normalised-free-cash-flow/) — normalisation often involves capex adjustments
- [Return on Invested Capital](/return-on-invested-capital/) — influenced by growth capex efficiency

### Wider context

- Capital Allocation — strategic framework for how companies deploy capex
- Valuation — overarching framework
- [Business Cycle](/business-cycle/) — influences capex intensity (expansion vs. maturity)
- [Operating Lease](/operating-lease/) — alternative to capex for asset use

</div>

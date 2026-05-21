---
title: "Multiples Valuation"
description: "A market-based valuation method that values a company by applying market-observed price multiples (PE, EV/EBITDA, price-to-sales) to its financial metrics."
keywords:
  - multiples valuation
  - EV/EBITDA
  - price-to-earnings
  - valuation multiple
  - relative valuation
image: "/svg/valuation.svg"
---

*A **multiples valuation** answers a simple question: if similar companies trade at 10x earnings, and this company earns 50 million, it is worth 500 million. It is faster than [discounted cash flow](/discounted-cash-flow-valuation), requires fewer assumptions, and is often more credible in M&A because it is anchored to observable market prices. But it is also a shortcut that can hide poor thinking.*

## What a multiple is

A multiple expresses price as a ratio of some financial metric. The most common multiples are:

- **Price-to-earnings (PE).** Stock price divided by earnings per share. A 20x PE means investors pay 20 dollars for every dollar of annual earnings.

- **Enterprise value to EBITDA (EV/EBITDA).** Enterprise value (market cap plus net debt) divided by EBITDA (earnings before interest, taxes, depreciation, amortization). A 10x EBITDA multiple means the company is valued at 10 times its operating earnings.

- **Price-to-sales (P/S).** Market cap divided by revenue. A 3x sales multiple means the company is worth 3 times its annual revenue.

- **Price-to-book (P/B).** Market cap divided by book value of equity. A 2x book multiple means the market values equity at twice its accounting value.

**Other multiples:** EV/Sales, EV/FCF, P/FCF, PEG ratio (PE divided by growth rate), price-to-subscribers, and dozens of industry-specific multiples.

## How multiples valuation works

1. Pick a multiple.
2. Identify comparable companies and calculate the multiple for each.
3. Take the median or mean of comparables.
4. Apply that multiple to your target company's metric.
5. Result is implied valuation.

**Example.** Three comparable software companies have EV/EBITDA multiples of 12x, 11x, and 13x. Median is 12x. Your target company has EBITDA of 30 million. Implied enterprise value is 360 million.

## Why multiples work

**Market-based.** Multiples reflect what actual buyers and sellers think the market is worth, not what a theoretical model predicts. In M&A, multiples are how deals are priced.

**Simple.** No complex cash flow projections, no crystal-ball assumptions about perpetual growth. Just observable data.

**Quick.** A multiples analysis takes minutes. A DCF takes days or weeks.

**Defensible.** If 10 of your target's peers trade at 12x EBITDA, saying your target is worth 12x EBITDA is easy to defend.

## Which multiple to use

**P/E ratio.** Most familiar, widely available. But distorted by capital structure (highly levered companies have lower net income, higher P/E). Best for comparing similar companies with similar leverage.

**EV/EBITDA.** Unaffected by capital structure (EBITDA is before interest and taxes). Industry standard in M&A. Works well for mature companies with stable EBITDA.

**EV/Sales.** Works for unprofitable companies (no earnings to compare). Less distorted by accounting choices. But less precise—two companies with same sales might have very different profitability.

**P/B.** Standard for banks, insurance, real estate. Reflects accounting value. Less useful for asset-light or high-growth businesses where intangibles are most valuable.

**Industry-specific.** Telecom companies use EBITDA, subscribers, or free cash flow. Biotech uses EV/marketed-product sales or unmonized pipeline value. E-commerce uses EV/GMV (gross merchandise value).

## Comparable company analysis

The most rigorous application of multiples is [comparable company analysis](/comparable-company-analysis): identify truly similar firms, calculate their multiples, and apply the median to your target.

The challenge is defining "comparable." Same industry? Yes, but a large, diversified telecom is not truly comparable to a small, regional telecom. Same growth rate? Profitability? Same capital intensity? The more dimensions you require, the fewer comparables you find.

Most analyses start with industry peers, then adjust the multiple for growth, profitability, risk, and capital structure differences.

## Multiples across the business cycle

Multiples are not stable. In booms, when growth expectations are high, multiples expand (investors pay more per dollar of earnings). In recessions, multiples compress (investors are pessimistic). The same company trading at 18x PE in 2021 might trade at 12x in 2023.

This is why multiples analyses often show a range: the market multiple might be 10–14x, reflecting recent valuations. If your company is better than the median, use the high end. If worse, use the low end.

## When multiples analysis is best

**M&A transactions.** Buyers and sellers negotiate using multiples. Saying "your EBITDA multiple is 11x; the market trades at 10x" is concrete and defensible.

**Quick valuations.** You need a rough value in an hour, not a detailed DCF.

**Benchmarking DCF.** After building a DCF, calculate what multiple it implies. If the DCF implies 20x EBITDA and the peer set trades at 10x, reconsider your assumptions.

**Peer comparison.** Understanding whether your target is more expensive or cheaper than competitors.

## When multiples analysis is misleading

**Structurally different companies.** Comparing a capital-light, high-margin SaaS company at 40x sales to a capital-intensive retail company at 2x sales would be nonsensical.

**Different growth rates.** A 20% growth company might trade at 25x PE; a 5% growth company at 12x. Applying 25x to the slower company would overprice it. The PEG ratio (PE divided by growth rate) helps adjust for this, but it has its own issues.

**Cyclical timing.** If multiples are at cycle peaks, using them as anchors overstates value. A utility that normally trades at 12x EBITDA but currently at 14x due to low rates is probably overvalued at 14x for long-term purposes.

**One-time items.** If a comparable's earnings are depressed or inflated by one-time charges or gains, the multiple is distorted. Use normalized or adjusted metrics.

## Multiples as a complement to DCF

The best approach is to use both. Build a DCF model to understand intrinsic value and sensitivity. Then calculate multiples and compare to peers. If the DCF implies 15x EBITDA and peers trade at 10–12x, ask why: Is your growth assumption too high? Your discount rate too low? Or is the market mispricing the peer set?

This cross-check keeps you honest. A DCF that implies a 30x EBITDA multiple for a stable utility should trigger skepticism.

## See also

<div class="wiki-seealso">

### Closely related

- [Comparable company analysis](/comparable-company-analysis) — applying multiples systematically
- [Comparable transaction analysis](/comparable-transaction-analysis) — multiples from M&A deals
- [Relative valuation](/relative-valuation) — valuation relative to peers
- [Price-to-earnings ratio](/price-to-earnings-ratio) — the most common multiple

### Alternatives

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — fundamental approach
- [Sum-of-the-parts valuation](/sum-of-the-parts-valuation) — multiples applied to segments
- [Scenario valuation](/scenario-valuation) — discrete outcomes

### Analysis and refinement

- [Peer group selection](/peer-group-selection) — choosing right comparables
- [Sensitivity analysis](/sensitivity-analysis-valuation) — multiples sensitivity
- [Football field valuation](/football-field-valuation) — multiple approaches combined

</div>

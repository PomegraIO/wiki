---
title: "Comparable Company Analysis"
description: "A valuation method that values a target company by comparing it to similar publicly traded companies and applying their trading multiples."
keywords:
  - comparable company analysis
  - comps
  - peer group
  - trading multiples
  - relative valuation
image: "/svg/valuation.svg"
---

*A **comparable company analysis** (or "comps" analysis) is the most practical application of [multiples valuation](/multiples-valuation) in M&A and equity research. You identify publicly traded peers, calculate their trading multiples (EV/EBITDA, PE, EV/Sales), apply a median multiple to your target company's financial metrics, and arrive at an implied valuation range. The method is fast, market-based, and credible—if you can find truly comparable companies.*

## The process

**Step 1: Build the peer group.** Identify 5–15 companies in the same or similar industries as the target. Similar size helps but is not mandatory.

**Step 2: Gather financials.** Pull the latest revenue, EBITDA (or operating income), free cash flow, earnings, and balance sheet data for each peer from public filings or databases like CapitalIQ or Bloomberg.

**Step 3: Calculate multiples.** For each peer, calculate:
- EV/EBITDA (enterprise value divided by EBITDA)
- PE ratio (market cap divided by net income)
- EV/Sales (enterprise value divided by revenue)
- EV/FCF (enterprise value divided by free cash flow)
- Any industry-specific metrics

**Step 4: Calculate median and mean.** Find the central tendency. The median is often preferred because it excludes outliers.

**Step 5: Adjust for differences.** If the target is higher-growth than the median peer, apply a higher multiple. If lower-growth, apply a lower multiple.

**Step 6: Apply to target.** Take the target's EBITDA (or revenue or FCF) and multiply by the peer multiple. This gives implied enterprise value.

**Step 7: Derive equity value.** Subtract net debt (debt minus cash) from enterprise value to get equity value. Divide by shares outstanding to get implied per-share value.

## Why comps work

**Market reality.** The peer group's multiples reflect actual prices paid by actual investors in an actual market, not theoretical models.

**Fast and credible.** Boards, banks, and sophisticated investors understand multiples. Saying "the company trades at 12x EBITDA; your target is worth 12x EBITDA times 40 million EBITDA = 480 million" is intuitive.

**Defensible.** If challenged, you can point to 10 public trades supporting your multiple. That is harder to argue with than a DCF's perpetual growth assumption.

**M&A standard.** In negotiations, the first thing discussed is multiples. Lawyers and bankers speak in multiples, not intrinsic values.

## Peer selection: the hard part

The biggest challenge is finding truly comparable companies. A few heuristics:

**Industry.** Start with companies in the same 4-digit GICS or SIC code. But recognize sub-segments: two telecom companies might be vastly different (one is high-growth 5G, the other is declining wireline).

**Size.** Company size should be roughly similar, or you adjust for the size effect. Comparing a 50 billion-dollar company to a 500 million-dollar company in the same industry is problematic (different growth rates, profitability, risk).

**Growth rate.** A high-growth company will trade at higher multiples than a mature one. If possible, group peers by growth rate.

**Profitability.** A profitable, stable business trades differently than a growing, unprofitable one.

**Capital intensity.** Asset-light businesses (software, consulting) trade at higher multiples than capital-intensive businesses (manufacturing, utilities).

**Geography.** Geographic exposure might matter. A US-focused company might not be comparable to a company with major emerging-market exposure.

## Adjusting multiples

If your target is different from the median peer on any major dimension, adjust the multiple accordingly:

**Higher growth.** If your target grows 15% and the peer set grows 8%, add a growth premium. Industry wisdom (the PEG ratio) might suggest adding 1–2x per percentage point of growth difference.

**Better margins.** If your target has 40% EBITDA margins versus peer 30%, apply a higher multiple.

**Higher ROIC.** If your target earns 20% ROIC versus peer 12%, value is higher. You might apply 1.2x the median multiple.

**Earlier stage.** A pre-profitable company in a mature industry deserves a discount to the profitable-company multiple.

These adjustments are often 10–30% either direction, moving the multiple from the median by 1–2 percentage points.

## Median vs. mean

Use the median (middle value when sorted) rather than the mean (average), because medians are less distorted by outliers. If 10 peers trade at 10–12x EBITDA but one is at 20x due to a special situation, the mean is skewed; the median is robust.

Some analyses show both to indicate the range.

## Which multiples are most reliable

**EV/EBITDA.** Most reliable for mature, profitable companies. EBITDA is before interest and taxes, so it is independent of capital structure. Industry standard.

**PE ratio.** Widely available but distorted by leverage and capital structure. A highly levered company has lower net income (higher interest expense), higher PE. Use EV/EBITDA instead if comparing companies with different leverage.

**EV/Sales.** Works for unprofitable companies or those with inconsistent profitability. But less precise—two companies with same sales might have very different profitability.

**EV/FCF.** Good if free cash flow is stable and positive. Less reliable for capital-intensive businesses where capex varies.

## Common pitfalls

**Including non-comparables.** Adding a poorly comparable company to the peer set and averaging in its multiple can badly distort results.

**Not adjusting for differences.** Applying the peer median to a much-higher-growth target without adjustment is lazy.

**Circular reasoning.** If the entire peer set is overvalued, you inherit that overvaluation.

**Ignoring cycle timing.** If you are doing the analysis at peak valuations, the multiples are elevated. Anchoring to peak multiples for long-term valuation is wrong.

**One-time items.** If a peer has had a big one-time charge that depressed earnings or EBITDA, adjust the multiple or exclude the peer.

## Comps plus DCF

The best practice is to do both comps and DCF and compare. If comps imply 12x EBITDA and DCF implies 15x, reconcile: Why the difference? Is the DCF's growth assumption too high? Or are comps undervalued? This friction often reveals insights.

## See also

<div class="wiki-seealso">

### Closely related

- [Multiples valuation](/multiples-valuation) — parent method
- [Comparable transaction analysis](/comparable-transaction-analysis) — multiples from M&A deals
- [Peer group selection](/peer-group-selection) — choosing comparables carefully
- [Relative valuation](/relative-valuation) — valuation relative to market

### Integration with DCF

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — the intrinsic approach
- [Sensitivity analysis](/sensitivity-analysis-valuation) — multiples can be tested
- [Football field valuation](/football-field-valuation) — combining methods

### Practical application

- [Sum-of-the-parts valuation](/sum-of-the-parts-valuation) — comps applied to segments
- Precedent transaction — related multiples concept
- [Exit multiple terminal value](/exit-multiple-terminal-value) — using multiples for DCF terminal value

</div>

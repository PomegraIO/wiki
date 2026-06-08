---
title: "DCF Sensitivity to the Terminal Growth Rate"
description: "How DCF sensitivity to terminal growth rate drives enterprise value swings; why small assumptions cause disproportionate valuation changes."
keywords:
  - dcf sensitivity to terminal growth rate
  - terminal growth rate valuation
  - perpetuity growth rate dcf
  - terminal value sensitivity
  - dcf terminal value risk
  - long-run growth rate valuation
  - dcf value sensitivity analysis
image: /svg/valuation.svg
---

*The **terminal growth rate in a DCF model** is deceptively powerful: a seemingly modest shift from 2.0% to 2.5% perpetual growth can swing [enterprise value](/enterprise-value/) by 15–25%. Because the terminal value typically comprises 60–80% of total DCF value, sensitivity to this single assumption often dwarfs sensitivity to revenue growth, margins, or [discount rate](/discount-rate/) moves in the near term.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Terminal Growth Sensitivity — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Terminal value is usually 60–80% of total DCF; it is inherently fragile because it is discounted 10–30 years into the future and rests on a single growth number.</div>

|   |   |
|---|---|
| **Terminal value as % of EV** | Typically 60–80% |
| **Perpetuity formula sensitivity** | EV doubles if g rises 1% (when g ≈ WACC − 2%) |
| **Typical range for g** | 1.5% to 3.0% (rarely above long-run GDP growth) |
| **Peer variation** | Analysts disagree on g by 0.5–1.5 percentage points routinely |
| **Risk drivers** | Long-term margin stability, competitive moat, reinvestment needs |

</aside>

## The perpetuity formula and its cliff edge

The [terminal value](/terminal-value/) of a DCF is usually calculated as:

```
Terminal Value = NOPAT(final year) × (1 + g) / (WACC − g)
```

where g is the assumed perpetual growth rate. This is the **Gordon Growth Model**, and it is elegant—also dangerous.

Rearranged, enterprise value is proportional to:

```
EV ∝ (1 + g) / (WACC − g)
```

This formula has a cliff. When WACC = 10% and g = 2%, the denominator is 8%, and EV scales by 0.125 × (1.02). If g rises to 2.5%, the denominator shrinks to 7.5%, and EV scales by 0.167 × (1.025)—a 33% increase in the denominator sensitivity.

As g approaches WACC, the denominator approaches zero, and EV approaches infinity. This is why terminal growth rates are capped at or below long-run GDP growth: if you assume a company will grow faster than the economy forever, you are claiming it will eventually be larger than the economy, which is mathematically impossible (and implicitly contradicts the perpetuity assumption).

## Quantifying the sensitivity: worked example

Assume:
- Year 10 NOPAT: USD 100 million.
- WACC: 9%.
- Forecast period: 10 years.
- Discount factor to year 10: 0.42 (1.09^−10).

| Terminal Growth g | Terminal Value (year 10) | PV of Terminal Value | % of Total EV |
|---|---|---|---|
| **1.5%** | USD 1,700 million | USD 714 million | 68% |
| **2.0%** | USD 2,000 million | USD 840 million | 72% |
| **2.5%** | USD 2,429 million | USD 1,020 million | 75% |
| **3.0%** | USD 3,000 million | USD 1,260 million | 78% |

**Change from 2.0% to 2.5% terminal growth:** Terminal value rises 21%, and total EV rises approximately 12–15% (depending on the PV of explicit-period cash flows). A 0.5 percentage point shift in a single assumption drives USD 180 million (21% of USD 840M) of value change.

This is not a rounding error. In a USD 7 billion acquisition, a 1% variance in terminal growth (say, 2.0% versus 3.0%) can swing equity value by USD 500 million to USD 1 billion.

## Why analysts disagree on terminal growth

Terminal growth is supposed to reflect the **long-run sustainable growth rate** the company will achieve in perpetuity. In theory, it should not exceed GDP growth: if the company grows faster than the economy, it must be stealing share from competitors or entering new markets indefinitely—an assumption that only works for the largest, most durable franchises.

In practice, analysts use three anchors and often disagree:

1. **Long-run GDP growth.** Often 2.0–2.5% for developed markets, 3–4% for emerging markets. This is a floor: most companies cannot outpace GDP forever.

2. **Company's historical growth.** If a company has grown at 4% over the past 20 years, assuming 2% terminal growth is inconsistent. But historical growth is often inflated by industry tailwinds or market-share gains that may not persist.

3. **Analyst discretion.** A company with a durable moat (brand, network effects, scale) might deserve 2.5–3% growth (modest above GDP, reflecting competitive advantage). A cyclical or commoditized business might get 1.5–2% (at or below GDP).

**Common disagreement zones:**
- Tech / SaaS companies: analysts split between 2.5% (GDP-aligned, acknowledging market saturation) and 3.5–4.0% (assuming superior long-run growth from innovation).
- Utilities: narrow range, 2.0–2.5%, because they are price-regulated and slow-growing.
- Retail: 1.0–2.0%, with debate over whether online disruption reduces long-term growth.

A 1.5 percentage point spread in terminal growth (e.g., 2.0% vs. 3.5%) is not unusual across sell-side analysts covering the same company. This alone can account for 30–50% variance in target price.

## The sensitivity table: standard practice

Most professional valuations include a **sensitivity table** isolating terminal growth risk:

| WACC \ g | 1.5% | 2.0% | 2.5% | 3.0% |
|---|---|---|---|---|
| **8.0%** | 11.2x NOPAT | 13.3x | 17.0x | 25.0x |
| **9.0%** | 9.1x | 10.0x | 11.8x | 14.3x |
| **10.0%** | 7.7x | 8.3x | 9.1x | 10.0x |

Each cell shows enterprise value as a multiple of final-year NOPAT. A reader can instantly see that if WACC is 9% and terminal growth is 2.0%, the EV multiple is 10x NOPAT. If growth is 2.5%, it jumps to 11.8x—an 18% increase from a 0.5-point shift.

This table is a critical communication tool: it shows the buyer, the board, or the investor the range of defensible valuations and where the highest risk lies.

## Stress-testing and bounding the range

Sophisticated analysts bracket the terminal growth rate:

1. **Bear case:** Terminal growth = long-run GDP growth (or slightly below, if the company faces headwinds). For the US, this is often 1.5–2.0%.

2. **Base case:** Terminal growth = long-run GDP growth + a modest moat premium (typically 0.25–0.75 percentage points). For a quality company, this might be 2.2–2.5%.

3. **Bull case:** Terminal growth = long-run GDP growth + a larger moat premium (or specific evidence of sustained outgrowth). This rarely exceeds 3.0–3.5% for mature companies.

The base case is supposed to be the analyst's best estimate, not the midpoint. But showing the range makes clear that the valuation is a distribution, not a point.

## Common mistakes

### Mistake 1: Terminal growth above GDP growth without justification

A USD 100 billion company assuming 4% perpetual growth in a 2.2% GDP environment is claiming it will double in size every ~18 years and eventually exceed the size of the economy. Red flag: either the company faces headwinds not modeled in the forecast, or the terminal growth is overstated.

### Mistake 2: Mismatching terminal growth and WACC

If you assume a 2.5% terminal growth rate but use a WACC that was calculated assuming 2.0% long-run inflation (or vice versa), you are internally inconsistent. The WACC discount rate and the terminal growth rate should reflect the same long-run economic assumptions.

### Mistake 3: Failing to update terminal growth when assumptions change

When the Federal Reserve raises interest rates, WACC rises. When inflation expectations fall, both WACC and terminal growth should adjust downward. A model that holds terminal growth constant at 2.5% while WACC swings from 8% to 11% due to rate changes is stale.

### Mistake 4: Terminal growth sensitivity is larger than explicit-period sensitivity

A 1% change in year-5 revenue growth (e.g., from 3% to 4%) may affect enterprise value by 5–10%. The same 1% change in terminal growth (e.g., from 2% to 3%) affects value by 25–50%. Many analysts spend effort modeling near-term growth rates and spend no time stress-testing the terminal assumption—backwards priorities.

## Communicating terminal growth risk to stakeholders

When presenting a DCF to a board, investor, or lender, highlight:

1. **The terminal value proportion.** "Terminal value is 72% of total enterprise value; the valuation is highly sensitive to the perpetual growth assumption."

2. **The sensitivity table.** Show how enterprise value changes across a range of WACC and terminal growth combinations.

3. **The justification for the chosen g.** "We assume 2.3% terminal growth, reflecting long-run GDP growth of 2.1% plus a 0.2-point premium for the company's market leadership in a growing niche."

4. **Downside and upside scenarios.** "If terminal growth falls to 1.5% due to increased competition, enterprise value declines to USD X. If the company sustains 2.8% growth through durable innovation, enterprise value rises to USD Y."

5. **Peer and historical context.** "The market is currently pricing peer companies at multiples consistent with 2.4–2.6% terminal growth. Our base-case 2.3% is slightly below-market, reflecting near-term cyclical headwinds."

## Checking reasonableness

Before finalizing a terminal growth rate, run three checks:

1. **GDP comparison.** Terminal growth should be at or slightly below long-run GDP growth. If it exceeds 3.0%, be prepared to defend why the company is exceptional.

2. **Reinvestment needs.** A company growing at 2.5% perpetually must reinvest a portion of cash flow to fund that growth. Estimate the sustainable growth rate given the [return on invested capital](/return-on-invested-capital/) and retention ratio: g = ROIC × (1 − payout ratio). If your terminal growth assumption exceeds this, it is not sustainable.

3. **Market multiples.** Compare your implied terminal growth (backed out from your valuation multiple) to what the public market is pricing. If your 2.5% growth assumption yields a 12x NOPAT multiple but peers trading at the same multiple are priced for 2.0% growth, you have a mismatch to reconcile.

## See also

<div class="wiki-seealso">

### Closely related

- [Terminal Value](/terminal-value/) — the perpetuity calculation at the heart of the sensitivity
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the parent DCF framework
- WACC — the denominator in the perpetuity formula; must be consistent with g
- [Sensitivity Analysis Valuation](/sensitivity-analysis-valuation/) — the broader framework for isolating risks
- [Return on Invested Capital](/return-on-invested-capital/) — the driver of sustainable long-run growth
- [Gross Domestic Product](/gross-domestic-product/) — the anchor for terminal growth limits

### Wider context

- [Relative Valuation](/relative-valuation/) — market multiples provide a sanity check on implied growth
- [Market Capitalization](/market-capitalization/) — constrains terminal growth (company cannot exceed economy size)
- [Inflation](/inflation/) — affects both WACC and long-run nominal growth rates
- [Business Cycle](/business-cycle/) — terminal growth assumes a mature, normalized state, not cyclical peak or trough

</div>

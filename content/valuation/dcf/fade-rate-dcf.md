---
title: "Fade Rate in DCF Forecasting"
description: "A decay schedule that gradually reduces growth or return rates as a firm converges toward steady-state equilibrium."
keywords:
  - fade rate
  - dcf forecasting
  - growth assumption
  - long-term growth
  - convergence
image: /svg/valuation.svg
---

*The **fade rate** in discounted cash flow analysis is the speed at which a firm's excess growth or abnormal returns decline toward a long-run, economy-wide steady-state level, reflecting the competitive pressure and market saturation that erode supernormal performance over time.*

## Why growth cannot persist forever

A young company forecasted to grow [revenue](/revenue-recognition/) at 40% annually for decades would eventually be larger than the global economy—an impossible endpoint. Yet many first-pass DCF models, especially analyst write-ups of high-growth tech firms, implicitly project precisely this: rapid growth for five years, then a jump to a 3% perpetual growth rate, with no gradual transition.

This cliff-edge assumption is mechanically crude and economically implausible. Competitive advantage naturally decays. Market positions are challenged. Labour and capital become expensive. Regulatory scrutiny rises. A pharmaceutical company with a blockbuster drug does not enjoy 30% growth forever once the patent expires and generics flood the market.

The **fade rate** embeds this convergence into the forecast. Instead of holding growth constant for years and then dropping it abruptly, the model assumes growth fades—shrinks gradually—toward a sustainable long-term rate, often called the terminal or steady-state growth rate. The speed of that fade is the fade rate.

## Conceptual framework

Imagine a company with a current [return on invested capital](/return-on-invested-capital/) (ROIC) of 18% and a weighted average [cost of capital](/cost-of-equity/) (WACC) of 9%. The spread—a 9% "excess return"—is what drives valuation above a break-even NPV. Over time, competition erodes this spread.

A **linear fade** assumes the spread shrinks by a constant percentage point per year. If the spread is 9% and the fade is –0.5 percentage points per year, year 1 shows a 8.5% spread, year 2 shows 8.0%, and so forth until the spread hits zero (ROIC equals WACC) after 18 years. At that point, the firm earns its cost of capital and growth no longer creates value.

A **curved fade** assumes the decay is faster initially and slows down, or vice versa. This is mathematically smoother and can reflect the idea that early erosion of a moat is steep, then stabilizes. A company might see ROIC decline from 18% to 15% in year 1 (three percentage points), to 13% in year 2 (two points), to 11% in year 3 (two points), and then level off—a pattern of rapid initial decay.

## Practical parameterization

In spreadsheet models, fade rates are often defined as:

1. **Fade duration**: How many years until the spread reaches zero (or a target steady-state level)? Five years, ten years, or twenty years?
2. **Fade shape**: Linear, exponential (geometric decay), or custom curves?
3. **Target steady-state ROIC or growth rate**: What is the ultimate normal level? Often assumed equal to the long-run GDP growth rate (2–3%) plus inflation (1–2%), yielding a 3–5% terminal rate.

For a company with a 5-year explicit forecast, the fade rate determines years 6–15 or beyond. A short fade (3–5 years) implies that competitive advantage erodes quickly, suitable for commoditized or capital-intensive businesses. A long fade (10–20 years) is more appropriate for moated companies with defensible market positions: brand franchises, network effects, high switching costs.

## Link to the reinvestment rate

Fade rates and [reinvestment rates](/reinvestment-rate-dcf/) are closely linked. A company with a 15% ROIC and a 50% [reinvestment rate](/reinvestment-rate-dcf/) can grow its [free cash flow](/free-cash-flow/) at roughly 7.5% (15% × 50%) while maintaining that ROIC. As ROIC fades toward WACC, growth also naturally fades unless reinvestment is increased. 

The fade rate thus disciplines the reinvestment assumption: if ROIC converges to 9% over ten years, and reinvestment stays at 50%, growth converges to 4.5%. Most models that fade ROIC adjust reinvestment implicitly by assuming the fade is due to both declining returns and rising competitive pressure reducing the value of each dollar reinvested.

## Common mistakes in fade implementation

**Ignoring the fade entirely** is widespread in equity research. A 5-year explicit forecast at 20% growth, then 3% perpetual, is common shorthand. The value attributed to the gap between year 5 and perpetuity (via the [terminal value](/discounted-cash-flow-valuation/)) can be substantial and overstated.

**Fading too slowly** is equally common. A analyst building a 30-year fade (100 basis points per year off a 9% spread) is implicitly betting that the company will hold extraordinary returns for three decades—unusual outside of a few tech leaders or entrenched oligopolies.

**Fading the growth rate instead of returns on capital** is a shortcut some models take. If revenue grows at 15% but [ROIC](/return-on-invested-capital/) is stable at 10%, fading revenue growth does not reflect the true source of value erosion (competitive returns), and the model risks overstating or understating [terminal value](/discounted-cash-flow-valuation/).

**Forgetting to tie fade to reinvestment** disconnects the growth forecast from its capital requirement. A company fading ROIC from 15% to 9% over ten years but holding reinvestment constant will generate less cash per dollar of capital deployed—a distortion.

## Sector patterns

**Technology, software, biotech**: Typically short to moderate fades (5–10 years), reflecting the pace at which competitive moats erode. High-margin SaaS platforms might persist longer; commodity hardware products shorter.

**Consumer discretionary**: Often fade over 7–10 years as brands age, new competitors emerge, and consumer preferences shift. Luxury goods (heritage, narrow moat) fade more slowly; trendy consumer electronics fade rapidly.

**Financials**: Moderate fades (5–8 years), reflecting the difficulty of sustaining above-market risk-adjusted returns in competitive banking and insurance. Oligopolistic markets (credit cards) fade more slowly than retail banking.

**Utilities, energy**: Long or negligible fades, because competitive advantage (regulated returns, natural resources) is institutionally protected or exogenously determined. ROIC is often pinned near WACC from year one.

**Industrials, materials**: Moderate fades (7–12 years), reflecting cyclicality and capital intensity that eventually arbitrage away excess returns. Cyclical downturns often accelerate the fade in practice.

## Testing the fade

Sensitivity analysis on the fade rate is important and often revealing. A ten-year fade versus a twenty-year fade can move fair value by 15–25% for high-growth firms; for mature companies, it barely matters. Likewise, varying the terminal ROIC (is it 9%, 10%, or 11%?) within a small range can shift valuations meaningfully.

Many practitioners compare their fade assumptions to historical precedent: how long did past winners (Apple, Microsoft, Amazon) sustain excess returns before normalizing? Empirically, even the strongest moats typically compress toward WACC over 10–20 years, though the best operators manage to extend that window. Academic studies on competitive advantage decay are scarce; most fade calibration remains judgment-driven.

## See also

<div class="wiki-seealso">

### Closely related

- [Reinvestment Rate](/reinvestment-rate-dcf/) — the capital reinvestment assumption paired with fade
- [Return on Invested Capital](/return-on-invested-capital/) — the metric typically faded toward WACC
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the framework embedding the fade
- [Terminal Value](/discounted-cash-flow-valuation/) — the end-state assumption after fade completes
- [Cost of Capital](/cost-of-equity/) — WACC, the steady-state target
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — testing fade assumptions

### Wider context

- [Competitive Advantage](/price-to-earnings-ratio/) — the underlying economic concept
- [Market Maturity](/business-cycle/) — industry dynamics driving fade
- [Valuation](/discounted-cash-flow-valuation/) — the larger framework

</div>

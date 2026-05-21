---
title: "Perpetuity Growth Terminal Value"
description: "The most common terminal value approach, which assumes a company's cash flows grow at a constant rate forever and uses the Gordon growth formula to calculate value."
keywords:
  - perpetuity growth
  - terminal value
  - Gordon growth
  - perpetual growth rate
  - DCF
image: "https://picsum.photos/seed/perpetuity-growth-terminal-value/900/600"
---

*The **perpetuity growth terminal value** is the workhorse endpoint in every [discounted cash flow](/discounted-cash-flow-valuation) model. It assumes that in year N plus one and beyond, a company's free cash flow grows at a constant rate forever, and it uses the [Gordon growth model](/gordon-growth-model) formula to collapse that infinite stream into a present value. Despite its theoretical beauty, this approach rests on an assumption—perpetual growth rate—that is easier to state than to defend.*

## The formula and its logic

Terminal value equals next-period free cash flow divided by the discount rate minus the perpetual growth rate. If a company generates 100 million in free cash flow in year 11, you require an 8% return, and the company grows at 2% forever, terminal value is 100 million divided by 0.06, or 1.67 billion dollars.

The logic is that if something grows at a constant rate forever, its value is the next payment divided by the difference between your required return and its growth rate. This is mathematically sound, assuming the growth rate is perpetual, stable, and below the discount rate.

The trouble is that the last clause—perpetuity—is a constraint on reality that reality often violates.

## Choosing the perpetual growth rate

This is where the method's elegance collides with practice. What is the perpetual growth rate?

For a developed-economy company, it should be close to long-run nominal GDP growth: typically 2–3% in the US, 1–2% in Japan or Europe, 3–5% in an emerging market. This makes intuitive sense: no company can grow faster than the economy forever. Eventually, at some point, growth must converge to the economy's growth rate, or the company becomes larger than the entire economy, which is impossible.

**The most common mistake.** Analysts assume perpetual growth equal to recent growth. A software company growing at 25% today gets a 5–6% perpetual growth assumption. This is a category error. Recent growth is elevated because the company is young, expanding into new markets, or benefiting from a secular tailwind. Once markets saturate or competitors arrive, growth normalizes downward. Extrapolating recent growth to perpetuity is a recipe for massive overvaluation.

**A practical rule.** For a developed-economy company, assume perpetual growth between 2% and 3% unless you can articulate a very specific reason (regulatory protection, network effects, secular tailwind) for a higher rate. For an emerging-market company, 3–5% is reasonable. For a US company in a mature industry facing commoditization, 1–2% is appropriate.

## The sensitivity nightmare

This single number drives enormous valuation swings. If discount rate is 9% and you assume 2% perpetual growth, terminal value is next-year cash flow divided by 0.07. If you assume 3%, it is divided by 0.06, a 16% increase. If you assume 4%, it is divided by 0.05, nearly a 40% increase.

For most [two-stage DCF](/two-stage-dcf) models, terminal value is 70–75% of total enterprise value. A 16% change in terminal value moves total value by roughly 11%. A 40% change moves total value by 30%.

This is why running a [sensitivity analysis](/sensitivity-analysis-valuation) on perpetual growth is critical. Any DCF that does not show valuation at 2%, 3%, and 4% perpetual growth is hiding fragility.

## Why perpetuity works for some businesses

**True perpetuities.** Regulated utilities with statutory rights to operate for decades and known capex needs. Real estate generating stable rents. Infrastructure with long concessions. For these, perpetuity is less theology and more forecast of an actual stable state.

**Businesses with durable competitive advantages.** A company like Coca-Cola or Procter & Gamble, with brand moats and distribution networks that have persisted for decades, might credibly grow at 3–4% in perpetuity. Not 10%, but 3–4% is plausible.

**Mature, low-growth industries.** A bank or insurance company in a developed economy with stable margins and steady competitive dynamics. Perpetuity assumptions are here closer to observable reality.

## When perpetuity growth is indefensible

**High-growth startups.** A software company growing 40% annually cannot grow at 40% forever. It will eventually saturate. A perpetuity model that fails to anticipate that deceleration will catastrophically overvalue it.

**Disruptive businesses in inflection.** A company benefiting from a secular shift (remote work, automation, electrification) might enjoy a 15-year tailwind before growth normalizes. Assuming perpetual growth at today's rate is fantasy.

**Cyclical or commoditized businesses.** Airlines, shipping, commodity chemicals. These do not have perpetual competitive advantages. Assuming stable perpetual growth ignores the cycle.

**Emerging-market companies with political risk.** Perpetual growth assumes perpetual stability of government, regulation, and the business environment. This is often not true.

## Alternatives and complements

Many practitioners use [exit multiple terminal value](/exit-multiple-terminal-value) instead: forecast year-10 EBITDA, assume a realistic multiple, discount to present. This converts the perpetual growth assumption into an observable multiple, which feels more grounded.

Others use a [three-stage DCF](/three-stage-dcf) with an explicit transition period, letting growth decline gradually to the perpetual rate. This acknowledges that the perpetual rate is a destination, not a starting point.

Some run [scenario valuation](/scenario-valuation) with discrete bear, base, bull cases, each with its own perpetual growth assumption, rather than relying on a single central estimate.

## Making the assumption testable

The best practice is to make the perpetual growth assumption explicit and to justify it:

- State your assumed perpetual growth rate clearly.
- Compare it to long-term GDP growth in the company's primary market.
- If above GDP growth, articulate why the company gains share forever.
- Run sensitivity to show valuation at 2%, 3%, 4% to expose the fragility.
- Cross-check: what exit multiple does your perpetual assumption imply?

A perpetuity growth model that meets these criteria is transparent and defensible. One that hides the assumption or uses a round number like 5% or 6% without justification is guesswork.

## See also

<div class="wiki-seealso">

### Closely related

- [Terminal value](/terminal-value) — the endpoint concept
- [Gordon growth model](/gordon-growth-model) — the formula
- [Exit multiple terminal value](/exit-multiple-terminal-value) — the alternative
- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — parent model

### Time-structured models

- [Two-stage DCF](/two-stage-dcf) — explicit plus perpetual
- [Three-stage DCF](/three-stage-dcf) — with transition period
- [Dividend discount model](/dividend-discount-model) — same perpetuity logic applied to dividends

### Testing and sensitivity

- [Sensitivity analysis](/sensitivity-analysis-valuation) — perpetual growth sensitivity
- [Scenario valuation](/scenario-valuation) — discrete cases
- [Football field valuation](/football-field-valuation) — ranges and confidence intervals
- [Reverse DCF](/reverse-dcf) — backing out the implied perpetual growth from market price

### Inputs

- [Weighted average cost of capital](/weighted-average-cost-of-capital) — the discount rate
- [Cost of equity](/cost-of-equity) — for equity valuation
- [Market risk premium](/market-risk-premium) — used in cost of equity

</div>

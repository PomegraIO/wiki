---
title: "DCF Valuation for Mining and Natural Resource Companies"
description: "Commodity price deck assumptions, reserve depletion, closure costs, and risk adjustments for mining company discounted cash flow models."
keywords:
  - dcf valuation mining
  - mining valuation
  - natural resource companies
  - commodity price deck
  - reserve depletion
  - mining closure costs
---

*Valuing a mining company using **discounted cash flow (DCF)** is more complex than valuing a stable, mature business. A mine depletes its ore or mineral reserves and eventually closes. The company must forecast the commodity price over 20+ years, estimate how fast reserves will deplete, and account for the non-trivial cost of closing the mine safely. Getting these assumptions right can swing a valuation by 50% or more.*

## The Commodity Price Deck

The foundation of any mining DCF is the **commodity price deck**—a long-term forecast of the price of gold, copper, oil, lithium, or whatever the company extracts. Unlike a tech company, whose revenue grows with product adoption and market share, a miner's revenue is almost entirely commodity price × tonnes produced. A $50/barrel oil price yields radically different cash flows than $100/barrel, all else equal.

Most mining companies don't forecast commodity prices themselves; they use one of several industry benchmarks. The most common sources are bank research (from Goldman Sachs, JPMorgan, etc.), consensus expectations from commodities dealers, and historical price floors or regional studies. A prudent analyst might gather 5–10 price forecasts from different sources, average them, or use one as the "base case" with high and low scenarios.

The curve should reflect long-run marginal cost of production. If oil's long-run marginal cost (the cost to produce one more barrel globally) is around $60, prices rarely stay far above or below that for decades. Copper's long-run cost hovers around $3–4/lb; lithium, which is newer and more volatile, might assume $10–15/kg. The price deck typically shows prices declining slightly over the project life toward that long-run cost.

For example, a copper miner might assume:
- Years 1–5: $4.50/lb (above long-run cost; supply is tight)
- Years 6–15: $4.00/lb (gradual decline toward long-run)
- Years 16+: $3.70/lb (stable long-run price)

This is more cautious than assuming prices stay high indefinitely, which is a common error in optimistic mining valuations.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mining DCF Challenges — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation concepts." />

<div class="wiki-infobox-caption">Commodity prices, reserve life, and closure costs are the big three drivers of error.</div>

|   |   |
|---|---|
| **Forecast period** | 20–50 years (depends on reserve life) |
| **Key variables** | Commodity price, reserve depletion, capex, closure cost |
| **Price volatility** | ±40% annual; long-term assumption most critical |
| **Reserve risk** | Discovery, depletion, grade decline over mine life |
| **Terminal value** | Usually 0 (mine closes); sometimes salvage value |

</aside>

## Reserve Depletion and Mine Life

A copper mine has perhaps 500 million tonnes of proven and probable reserves. The company produces 50,000 tonnes per year. That's a **mine life** of 10,000 years—obviously unrealistic. In practice, as the mine digs deeper, extraction becomes more expensive, ore grade declines, and the mine becomes uneconomic to operate. The company eventually closes it. For valuation, the analyst must estimate the **economic life**—how many years the mine will operate profitably at current commodity prices and extraction costs.

Many mining DCFs assume a 20–30 year operating life, though this varies. An iron ore mine in Australia might operate for 40+ years; a small gold prospect might have 10 years. The key is that reserves deplete over the forecast period. If a mine produces 50,000 tonnes/year and starts with 500 million tonnes, it can't sustain that for 100 years. The analyst should model declining output in the tail years as ore grades fall, or assume closure once economic reserves are exhausted.

Reserve estimation is also fraught with uncertainty. Proven reserves are ore bodies that have been extensively drilled and studied; probable reserves are educated guesses based on geology. A new drilling program can double reserves overnight, or prove that previous estimates were wildly optimistic. Many mining companies have had to write down reserves sharply. A prudent DCF should do sensitivity analysis: What if reserves are 20% lower than the company reports? What if the mine life is 10 years instead of 25? Valuations that don't flex these assumptions are overconfident.

## Capital and Operating Expenditure

Mining requires large upfront and ongoing capital. An open-pit copper mine might require $2 billion to build (the mine, processing plant, tailings storage, roads, power, water). Over the life of the mine, there's additional **sustaining capex**—replacement of worn-out equipment, expansion of tailings storage, environmental upgrades. A 10% error in capex assumptions can easily swing a valuation by 15–20%.

Operating costs (extraction, milling, smelting, transport) depend on commodity type and geography. A low-cost producer (large scale, good ore grade, low energy cost) might produce copper at $2.50/lb. A high-cost producer might pay $3.50/lb. Operating costs also tend to rise over the mine life as the orebody is depleted and digging must go deeper. A realistic DCF should forecast rising unit costs as the mine matures. Many companies assume flat costs, a common pitfall.

## Environmental Remediation and Closure Costs

This is often underestimated. When a mine closes, the company must stabilize tailings, cap water infiltration, restore the landscape, and monitor groundwater quality for decades. For a large mine, this can cost $500 million to $2 billion. Some costs are known (the company is legally required to set aside a closure fund); others are uncertain because environmental standards may tighten.

In a DCF, closure costs are usually modeled as a single large outflow at the end of the mine life, discounted back to present value. For example, a $1 billion closure cost 25 years in the future, discounted at 8%, is worth roughly $145 million today. It's a meaningful chunk of the enterprise value, yet many amateur valuations ignore it or assume a salvage value (selling the site for $100 million) that doesn't materialize. 

The investor should ask: Does the company have the financial strength to fund closure? If not, the government or local community may have to pay, reducing shareholder value. Some jurisdictions now require mines to post closure bonds, pre-funding the expected cost. This is economically sound and reduces downside surprise.

## Discount Rate and Risk

Mining is higher-risk than a stable utility or manufacturing company. The discount rate ([cost of equity](/cost-of-equity/) or [WACC](/cost-of-equity/)) should reflect this. Typical mining discount rates range from 8% to 12%, depending on the company size, the commodity, reserve certainty, and country risk.

A large, diversified producer (Rio Tinto, Glencore) with established reserves in developed countries might use 8%; a junior explorer in an unstable region with speculative reserves might use 12% or higher. Commodity price volatility should be baked into the risk rate, not treated separately. Some analysts run scenario analysis instead: assume a 30% probability of high prices (12% discount rate) and 70% probability of low prices (9% rate), then blend the valuations. This is often more transparent than trying to embed price volatility into a single "correct" discount rate.

Leverage also matters. A miner financed entirely with equity has a different cost of capital than one with significant debt. The debt is risky because if commodity prices collapse, the miner may not generate enough cash to service it. The [debt-to-equity ratio](/debt-to-equity-ratio/) and the covenant structure (does the company have to pay down debt if cash flow falls below X?) should inform the WACC.

## Worked Example

Suppose you're valuing a small gold miner:
- Proven reserves: 2 million ounces
- Mine life: 10 years at 200,000 oz/year
- Operating cost: $1,200/oz
- Capex: $500 million upfront, $30 million/year sustaining
- Gold price: $2,000/oz (years 1–5), $1,900/oz (years 6–10)
- Closure cost: $200 million in year 10
- Discount rate: 10%

Year 1–5 annual cash flow: (200,000 oz × $2,000) − (200,000 oz × $1,200) − $30M = $160M − $30M = $130M
Year 6–10 annual cash flow: (200,000 oz × $1,900) − (200,000 oz × $1,200) − $30M = $140M − $30M = $110M

Discounting at 10%:
- PV of years 1–5 cash flow: ~$492M
- PV of years 6–10 cash flow: ~$280M
- PV of year 10 closure cost (−$200M): ~−$77M
- Less: upfront capex (−$500M)

Enterprise value = $492M + $280M − $77M − $500M = $195M

This is the economic value of the business. If the company has $50M in net debt, equity value is $145M. Divided by, say, 10M shares outstanding, that's $14.50 per share—a starting point for comparison to the market price.

## Sensitivity and Scenario Analysis

The real power of a DCF in mining is sensitivity analysis. How does value change if:
- Gold price is $1,800 instead of $2,000? (Perhaps −30% to equity value)
- Mine life is 8 years instead of 10? (−20% to value)
- Operating cost is $1,300/oz instead of $1,200? (−15% to value)

A good mining analyst builds a spreadsheet that flexes all three assumptions and shows a valuation matrix. This makes clear which assumptions matter most and where the downside risk lies. If the valuation is highly sensitive to small changes in gold price or reserve life, the equity is risky. If value is robust across a wide range of price scenarios, it's cheaper.

Scenario analysis—combining multiple assumptions into a "bull" case (higher prices, longer life, lower costs) and a "bear" case (the opposite)—gives a range of intrinsic values. The market price should land somewhere in that range. If not, the stock may be mispriced.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — foundation of DCF methodology
- [Cost of equity](/cost-of-equity/) — discount rate for mining valuations
- [Debt to equity ratio](/debt-to-equity-ratio/) — financial leverage in mining
- Commodity price volatility — price driver of mining cash flows

### Wider context

- [Enterprise value](/enterprise-value/) — total economic value of a business
- [Free cash flow](/free-cash-flow/) — unlevered cash available to investors
- [Sensitivity analysis valuation](/sensitivity-analysis-valuation/) — stress-testing valuations
- [Fair value](/fair-value/) — intrinsic worth independent of market price

</div>

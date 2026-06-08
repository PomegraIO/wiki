---
title: "Normalised Free Cash Flow"
description: "Adjusting reported cash flows to remove one-time gains, losses, and anomalies before inserting them into a DCF model."
keywords:
  - normalised cash flow
  - adjusted free cash flow
  - one-time items
  - recurring cash flow
  - run-rate cash flow
  - fcf normalization
image: "/svg/valuation.svg"
---

*A **normalised free cash flow** strips one-off and non-recurring items from reported [free-cash-flow](/free-cash-flow/) figures, leaving a cash-generation rate that the business can sustain. A company might report $100 million of FCF in a year, but if that includes a $30 million insurance settlement and a warehousing asset sale, normalised FCF is closer to $70 million. Using the inflated figure in a [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) would overstate the company's earning power.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Normalised Free Cash Flow — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Remove the noise; value the engine.</div>

|   |   |
|---|---|
| **What it is** | FCF adjusted for non-recurring, one-time, or unsustainable items |
| **Also called** | Adjusted FCF, run-rate FCF, recurring FCF, normalized cash flow |
| **Typical add-backs** | Litigation settlements, asset sales gains, restructuring costs |
| **Typical deductions** | Unusual tax benefits, one-time tax refunds, insurance windfalls |
| **Frequency** | Calculated once, or annually if one-offs are common |
| **Goal** | Forecast sustainable future cash flows accurately |

</aside>

## Why reported numbers lie (unintentionally)

A company's reported [free-cash-flow](/free-cash-flow/) is accurate—it's audited, it's real. But it reflects the past twelve months in full, including events that won't recur. In 2022, a chemical firm paid $50 million to settle a legacy environmental lawsuit. That cash outflow was real, but it won't happen again next year. If you use reported 2022 FCF to project 2023–2027 cash generation, you're predicting another lawsuit every year, which is false.

Conversely, a retailer might sell a closed warehouse for $15 million in 2022, boosting reported FCF. That's real cash, but it's not part of operating earnings power. If you use the inflated 2022 figure as your base for perpetuity growth, you're assuming the company keeps selling real estate forever.

Normalisation is the discipline of asking: "What would FCF have been if 2022 had been a normal year?" It is not fiddling the books; it is backing out the noise to reveal the signal.

## Common adjustments

**Gains or losses on asset sales.** When a company sells a building, a business unit, or a patent portfolio, the cash proceeds boost reported FCF, but the gain or loss goes through the [income-statement](/income-statement/). Include the cash (it's real), but adjust for the one-time gain. A $40 million sale with a $12 million gain means add back $12 million to operating cash, then deduct $40 million as a non-recurring item from FCF. Or more simply: exclude the $40 million sale entirely if you're building a stand-alone operating valuation.

**Litigation and legal settlements.** A company pays $20 million to settle a shareholder lawsuit. That's real cash out, and it belongs in the past year's reported FCF. But when projecting future years, it won't recur (at least not every year). Add it back to derive normalised FCF.

**Restructuring and severance.** A cost-cutting programme costs $30 million in severance and facility exit costs upfront, then saves $15 million in recurring annual expenses. Reported FCF that year is reduced by $30 million. Normalised FCF should back out the upfront charge but include the $15 million savings, because that is the new run-rate cost structure going forward.

**Insurance recoveries and tax refunds.** An insurance claim pays out $5 million unexpectedly. A tax audit results in a $10 million refund. These are real, one-time cash inflows. Add them back to get to underlying operating cash flow.

**Significant working-capital swings.** If a company's [inventory-turnover](/inventory-turnover/) improved dramatically in one year (releasing $50 million in cash), check whether this is sustainable or a one-off. If it's a permanent efficiency gain, that's real and should stay in normalised FCF. If a customer pre-paid for an enormous order, inflating [accounts-receivable](/accounts-receivable/) collections, that's non-recurring. Back it out.

**Changes in capex cycle.** A manufacturer usually spends 5% of revenue on [capex](/capex-maintenance-vs-growth/). One year it spends 2% because a major plant-upgrade cycle finished. The next year, a new facility project starts and capex jumps to 8%. Reported FCF will look lumpy. Normalised FCF should smooth these lumps to the long-term sustainable capex rate.

## Building normalised FCF: a worked example

A software company reports the following in Year 1:

| Item | Amount |
|---|---|
| Operating cash flow | $250M |
| Capex | −$40M |
| **Reported FCF** | **$210M** |

But Year 1 included:
- A $15M severance charge (unusual)
- A $20M sale of an old office (one-time gain; already in reported FCF as reduced capex)
- A tax refund of $8M from a prior-year audit (non-recurring)

Adjusted:

| Item | Amount |
|---|---|
| Reported FCF | $210M |
| Add back: severance (non-cash or normalise) | +$15M (or adjust in forecast) |
| Deduct: one-time tax refund | −$8M |
| Normalised capex (sustain 6% of revenue, not this year's 3.5%) | adjust to 6% baseline |
| **Normalised FCF** | **~$215M** |

This $215M is your base case for the DCF. You then forecast that it grows at a reasonable rate, not at a rate that assumes severance and tax refunds every year.

## Frequency and consistency

Normalisation can be done for a single year or across a multi-year average. If one-offs are rare, normalise just the latest year and start your forecast from there. If one-offs are chronic (a serial acquirer, or a company that frequently sells units), it may be cleaner to use a three-year average of FCF and normalise across that window.

The discipline is not to manipulate the number toward a desired valuation but to ensure your forecast is internally coherent. If you normalise out a $20 million restructuring cost and assume the savings persist, you must actually forecast reduced future costs. You can't add back restructuring and then fail to credit the benefit.

## Pitfalls: over-normalising and under-normalising

**Over-normalisation:** Some analysts strip out too much. "The company had an unusually strong year for working-capital collection, so I'll deduct 20% from FCF going forward." That's not normalisation; that's pessimism. If the company improved its [cash-conversion-cycle](/cash-conversion-cycle/) permanently, that's a real, sustainable gain. Keep it.

**Under-normalisation:** Other analysts assume everything is sustainable. A company took a one-time $100 million tax settlement; the analyst forecasts it will receive $100 million in tax settlements annually. Or a commodity company had a bumper year because prices spiked; the analyst projects commodity prices forever high. This is backwards. Normalise to the sustainable, predictable base.

Good normalisation requires judgment. You must know the business. Is the CEO restructuring chronic because the company is perpetually misaligned, or a one-time retooling after an acquisition? Are asset sales a funding strategy, or genuine disposals of non-core operations? The investor presentation, earnings call, and footnotes in the [10-K](/10-k/) often reveal whether management calls something "one-time" or recurring.

## See also

<div class="wiki-seealso">

### Closely related

- [Free Cash Flow](/free-cash-flow/) — the foundation metric being normalized
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — where normalized FCF feeds
- [Cash Flow Statement](/cash-flow-statement/) — source document for FCF and one-time items
- [Working Capital](/accounts-payable/) — often the source of normalisation adjustments
- [Capex Maintenance versus Growth](/capex-maintenance-vs-growth/) — capex normalization in detail

### Wider context

- [Earnings Quality](/earnings-quality/) — broader concept of separating recurring from one-off earnings
- [Revenue Recognition](/revenue-recognition/) — related accounting discipline
- Valuation — overarching framework
- [Financial Statement Analysis](/balance-sheet/) — detecting one-off items in reported financials

</div>

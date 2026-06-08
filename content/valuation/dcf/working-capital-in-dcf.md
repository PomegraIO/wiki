---
title: "Working Capital Changes in DCF"
description: "How incremental investment in operating assets and liabilities reduces free cash flow in DCF valuations of growing companies."
keywords:
  - working capital
  - dcf valuation
  - free cash flow
  - operating capital
  - cash flow adjustments
  - growth companies
image: /svg/valuation.svg
---

*The **working capital change** is the cash tied up when a growing company invests in receivables, inventory, and payables. It sits between operating profit and free cash flow, and ignoring it inflates DCF valuations by overlooking a real drag on distributable cash.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Working Capital Changes — cash tied up in operations</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation and finance mechanics." />

<div class="wiki-infobox-caption">The cash cost of growing without changing payment terms or inventory turns.</div>

|   |   |
|---|---|
| **What it is** | Net investment in operating assets (receivables, inventory) minus liabilities (payables, accruals) |
| **Also called** | Change in NWC, change in net working capital |
| **Why it matters in DCF** | Reduces free cash flow available to debt and equity holders |
| **Link to metrics** | [Cash flow statement](/cash-flow-statement/), [free cash flow](/free-cash-flow/) |
| **Scale** | Can swing 10–50% of [EBITDA](/ebitda/) for fast-growing retailers or manufacturers |
| **Direction** | Growing companies: negative (cash outflow); maturing companies: positive (cash recovery) |

</aside>

## Why growing companies must invest in working capital

When a company ships 20% more goods next year, its invoices will sit longer if payment terms stay the same. Customers who paid in 30 days still pay in 30 days—but there are more invoices outstanding. The company funds that gap until cash arrives. The same logic applies to inventory: a retailer holding 15% more stock has committed more capital to shelves, even though the goods will eventually sell.

Accounts payable work in the opposite direction. If a manufacturer buys more raw materials on 60-day terms, it benefits from the float—keeping its own cash longer. So working capital is the net position: receivables plus inventory, minus payables and accrued expenses.

In a DCF model, this net investment flows out as a cash drag. A company that generates $100 million in operating cash flow but must invest $8 million in receivables and inventory (and only recovers $2 million from slower payables) has only $94 million of truly free cash. That $6 million gap—the net working capital increase—is not available to shareholders or debt holders. It must be booked in the DCF.

## How to measure the working capital change

The cleanest route is the [cash flow statement](/cash-flow-statement/). The line item "changes in operating assets and liabilities" already nets everything. If it says –$8 million, working capital grew by $8 million (a cash outflow); if +$3 million, it shrunk (a cash inflow).

Alternatively, you can build it from the [balance sheet](/balance-sheet/):

1. Calculate **net working capital** at the end of each period: (Current Assets − Cash) − (Current Liabilities − Debt)
2. Take the *change* from one year to the next

This second method requires care. Exclude cash and debt—they belong in the financing section, not operations. Many analysts also exclude non-operating items like dividends or one-off litigation settlements.

For a company with seasonal spikes, use an average—take the mid-point of Q4 and Q1, for instance, to smooth the distortion.

## Forecasting working capital in a DCF

Static ratios are deceptive. A retailer might anchor on "days inventory outstanding" (DIO) or "days sales outstanding" (DSO), but those ratios shift with scale and efficiency. A maturing company's inventory might decline as a percentage of sales; a struggling one might build excess stock.

The safest approach: model working capital as a **percentage of incremental revenue**. If a company has historically spent $0.12 on working capital for every $1 of new revenue, assume that ratio continues. This assumes no major shifts in payment terms, supply-chain efficiency, or customer mix.

For more granular models, forecast each component separately:

- **Accounts Receivable** = (Forecasted Revenue × Historical DSO) / 365
- **Inventory** = (Forecasted Cost of Goods Sold × Historical DIO) / 365
- **Accounts Payable** = (Forecasted COGS × Historical DPO) / 365

Subtract prior-year balances from new balances to get the annual change.

## Terminal value and working capital recovery

At the end of the explicit forecast period, the company reaches a "steady state"—growth slows, capital efficiency stabilizes. In most DCF models, the [terminal value](/terminal-value/) assumes a perpetual growth rate of 2–3%.

Here's a key insight: if the company stops growing, it does not need to invest in incremental working capital anymore. It may *recover* cash from winding down excess receivables and inventory. Some analysts reverse the final year's working capital increase in the terminal-value calculation, effectively returning that cash to investors.

Others assume working capital stabilizes as a percentage of revenue and grows only at the perpetual growth rate. Both are defensible; the choice depends on your view of the company's long-term capital discipline.

## When working capital swamps the valuation

Fast-growing retailers, food distributors, and manufacturers often have working capital changes that rival operating profit in magnitude. A supermarket expanding by 8% a year might show $50 million in operating cash flow but only $20 million in free cash flow if working capital investment is $30 million.

This is not a sign of poor quality—it is structural. A high-growth retail chain *must* pre-fund inventory and receivables or it stops growing. But it does mean the DCF free cash flow is genuinely lower than a casual reading of EBITDA or operating profit would suggest.

Conversely, a mature, shrinking retailer can harvest working capital: it sells through inventory without replacing it, collects cash from old receivables, and free cash flow briefly spikes. Investors sometimes misread this as profitability improvement; it is often liquidation.

## Negative working capital and the cash trap

Some tech or software businesses operate with *negative* net working capital: customers pay upfront, but the company pays suppliers 30, 60, or 90 days later. This is a cash gift. SaaS companies with annual prepaid contracts are the extreme case.

In the DCF, negative working capital becomes a *positive* cash flow—a boost to free cash flow. But it is unsustainable. Once the company matures, customers are no longer prepaying at an accelerating rate, and the company must reflect that in the model. Assume the negative working capital unwinds partly or wholly in the terminal period.

## See also

<div class="wiki-seealso">

### Closely related

- [Free cash flow](/free-cash-flow/) — operating cash flow minus capital expenditure and working capital investment
- [Cash flow statement](/cash-flow-statement/) — where changes in working capital are reported
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the full framework into which working capital feeds
- [Operating lease](/operating-lease/) — another liability that can mask working capital changes
- [Cash conversion cycle](/cash-conversion-cycle/) — the time between paying suppliers and collecting customer cash
- [Accounts receivable](/accounts-receivable/) — customer invoices, a major working capital component
- [Inventory turnover](/inventory-turnover/) — how fast goods move, a driver of working capital need

### Wider context

- [Balance sheet](/balance-sheet/) — where current assets and liabilities live
- Valuation — the broader discipline of pricing companies
- Capital allocation — how management deploys cash across growth and returns
- [Business cycle](/business-cycle/) — macroeconomic expansion and contraction that affect working capital needs

</div>

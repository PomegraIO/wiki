---
title: "Cash Conversion Efficiency"
description: "Percentage of net income converted into operating cash flow, measuring the quality and sustainability of reported earnings."
keywords:
  - cash conversion
  - quality of earnings
  - operating cash flow
  - accrual accounting
  - financial analysis
---

*Cash Conversion Efficiency is the ratio of operating cash flow to net income, expressed as a percentage. It measures how much of a company's reported profit is backed by actual cash generation, rather than non-cash accruals. A high ratio signals earnings quality; a low ratio may indicate aggressive accounting or deteriorating operations.*

<div class="wiki-hatnote">For related cash-flow metrics, see [Cash Flow Ratio](/wiki/cash-flow-ratio/) and [Operating Cash Flow Ratio](/wiki/operating-cash-flow-ratio/).</div>

<aside class="wiki-infobox">

| Metric | Calculation | Interpretation |
|--------|-----------|-----------------|
| Cash Conversion | OCF / Net Income | % of earnings converted to cash |
| Strong range | 80–120% | Earnings are being realized in cash |
| Weak range | <60% | High accruals; quality concern |
| >100% | OCF > NI | Cash improving despite lower earnings |
| <50% | Heavy accrual load; possible manipulation |
| Typical industry | Varies (retailers ~80–100%, tech ~60–80%) |

</aside>

## The principle

Under accrual accounting, a company recognizes revenue when earned (often before cash is received) and expenses when incurred (often before cash is paid). This creates timing differences.

Example: ABC Corp sells $1M of products to customers on 90-day payment terms in Q4. Under accrual accounting, it recognizes $1M of revenue and reports $300k net income. But it receives no cash—the customer hasn't paid yet. At year-end:

- **Net income**: $300k (accrual basis)
- **Operating cash flow**: $0 or negative (cash basis)
- **Cash Conversion Efficiency**: 0% (or undefined; no cash generated)

If accounts receivable are collected in Q1, cash flow will catch up. But if collections stall or receivables grow indefinitely, earnings and cash diverge.

## Why high cash conversion is prized

Investors prefer earnings that are **backed by cash** because:

1. **Sustainability**: Cash earnings can be sustained; accrual earnings might reverse if receivables are eventually written off or inventory becomes obsolete.
2. **Dividend safety**: Paying dividends requires cash, not earnings. A company with 50% cash conversion must retain more capital than one with 100% conversion.
3. **Fraud detection**: Aggressive accounting (recognizing revenue prematurely, delaying expense recognition) inflates earnings relative to cash. Divergence is a red flag.
4. **Growth viability**: If a company's earnings are 50% cash and 50% receivables/inventory, growth requires financing growth in working capital. This consumes cash.

## Calculation and interpretation

$$\text{Cash Conversion Efficiency} = \frac{\text{Operating Cash Flow}}{\text{Net Income}} \times 100\%$$

**Interpretation bands**:

- **>100%**: OCF exceeds net income. This can happen when:
  - Depreciation/amortization (non-cash charges) are large relative to net income.
  - Receivables or inventory are decreasing, releasing cash.
  - Example: A company reports $100k net income but has $50k of depreciation and collects $60k of receivables. OCF = $100k + $50k + $60k = $210k. Ratio = 210%.
  - This is generally *favorable*—cash generation is outpacing earnings.

- **80–100%**: Typical for stable, profitable companies. Earnings and cash are in sync; working capital is stable.

- **60–80%**: Below-average; working capital is growing (receivables or inventory expanding relative to sales) or accruals are high. Not a crisis, but warrants investigation.

- **<50%**: Alarm. Either:
  - Revenue is recognized via long-term contracts or very liberal revenue recognition, but cash collection is delayed.
  - Inventory is accumulating (potential write-down risk).
  - Receivables are aging and potentially uncollectible.
  - Accruals (provision for doubtful accounts, warranty reserves) are very large relative to net income.

## Industry variations

Cash conversion efficiency varies by business model:

**Retailers** (e.g., Target, Walmart): 90–120%. They collect cash upfront at the register but pay suppliers on net-30 or net-60 terms. This creates a **cash gap**—positive operating cash flow even with modest earnings. This is a structural advantage of retail.

**Manufacturing**: 70–100%. Capital expenditure on property, plant, and equipment is a cash outflow but recorded as depreciation (non-cash) in earnings. The ratio normalizes when you account for capex separately.

**Software/SaaS**: 50–90%. Upfront subscription payments hit cash immediately, but revenue is recognized over the subscription period. This creates favorable cash timing early in a company's growth, then normalizes later.

**Insurance**: 100%+. Insurance companies collect premiums in cash upfront but recognize earnings as claims are incurred (sometimes years later). This creates a structural cash conversion advantage.

**Real estate/development**: <50%. Long project cycles and deferred revenue recognition create large timing gaps.

## Working capital and cash conversion

The key driver of cash conversion variance is **working capital movement**:

$$\text{OCF} = \text{Net Income} + \text{Depreciation/Amortization} \pm \text{Changes in Working Capital}$$

If receivables increase by $30k (customer hasn't paid yet), that's a $30k drain on OCF relative to earnings. If receivables decrease by $30k (collections exceed new sales), that's a $30k boost to OCF.

A company growing rapidly will often see its cash conversion efficiency *decline* because growth requires working capital investment (more inventory, more receivables). This is normal and not necessarily a concern if the growth is profitable.

## Detecting accounting quality issues

**Red flag: Declining cash conversion despite stable earnings**

If net income is flat, but operating cash flow is falling, investigate:
- Is accounts receivable (DSO: days sales outstanding) growing?
- Is inventory (inventory turnover) slowing?
- Is the company recording large one-time accruals?

Example: Enron reported rising earnings while operating cash flow was stagnant or negative. The difference was fictional revenues (roundtrip transactions, special-purpose entities) that were booked as earnings but never realized in cash.

**Red flag: Rising earnings, falling or negative operating cash flow**

A company that books $100M in earnings but generates −$20M in operating cash flow is either:
- Growing working capital aggressively (inventory, receivables exploding).
- Using aggressive revenue recognition (early revenue, extended payment terms).
- Experiencing operational distress (paying suppliers faster to avoid insolvency).

## Adjustments for capital intensity

Operating cash flow already deducts capital expenditure (capex is a cash outflow). But depreciation/amortization is added back (non-cash charge). For highly capital-intensive businesses (airlines, railroads, utilities), this creates noise.

Some analysts prefer **free cash flow**, which adjusts for capex:

$$\text{Free Cash Flow} = \text{OCF} - \text{Capital Expenditure}$$

A more refined cash conversion metric is:

$$\text{Cash Conversion to Equity} = \frac{\text{Free Cash Flow}}{\text{Net Income}}$$

This controls for capex and gives a clearer picture of cash available to shareholders.

## Cash conversion in valuations

In [discounted cash flow (DCF)](/wiki/discounted-cash-flow-valuation/) models, analysts use free cash flow, not earnings. A company with 50% cash conversion and $100M earnings generates $50M of FCF. If a competing company with 90% cash conversion also reports $100M earnings, it generates $90M of FCF—a 80% valuation premium (if multiples are equal).

This is why earnings surprises matter less than cash flow surprises. A company that beats earnings expectations but disappoints on cash flow is likely to underperform.

<div class="wiki-seealso">

### Closely related
- [Cash Flow Ratio](/wiki/cash-flow-ratio/) — related liquidity metric
- [Operating Cash Flow Ratio](/wiki/operating-cash-flow-ratio/) — cash-to-liabilities
- [Cash Conversion Cycle](/wiki/cash-conversion-cycle/) — working capital timing
- [Quality of Earnings](/wiki/earnings-quality/) — accrual quality
- [Free Cash Flow](/wiki/free-cash-flow/) — FCF calculation

### Wider context
- [Accrual Accounting](/wiki/accrual-accounting/) — earnings basis
- [Cash Flow Statement](/wiki/cash-flow-statement/) — source document
- [Working Capital Ratio](/wiki/net-working-capital-ratio/) — balance sheet view
- [Discounted Cash Flow](/wiki/discounted-cash-flow-valuation/) — DCF valuation

</div>

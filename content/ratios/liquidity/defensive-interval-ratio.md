---
title: "Defensive Interval Ratio"
description: "A liquidity metric that measures how many days of operating expenses a company can cover with its most liquid assets."
keywords:
  - defensive interval ratio
  - liquidity
  - operating expenses
  - cash ratio
---

*The **defensive interval ratio** is a liquidity measure that divides a company's most liquid assets (cash, [marketable securities](/wiki/money-market-fund/), [accounts receivable](/wiki/accounts-receivable/)) by its average daily operating expenses, answering: how many days can the company operate using only its most liquid assets, without relying on sales or external financing?*

The formula is:

**Defensive Interval Ratio = (Cash + Marketable Securities + Accounts Receivable) / Daily Operating Expenses**

If a company has $50M in cash and receivables, and spends $1M per day on operating expenses, the ratio is 50. This means the company can self-fund operations for 50 days without selling inventory, generating new sales, or borrowing. It is a "worst-case" liquidity lens: if all revenue dries up immediately, how long until the company runs out of liquid cash?

The defensive interval ratio is more conservative than the [current ratio](/wiki/current-ratio/) (which includes inventory) or the [quick ratio](/wiki/quick-ratio/) (which includes some semi-liquid items). It focuses on the hardest-to-monetize assets: actual cash, investments the company can sell in minutes, and receivables the company is confident will be collected.

<aside class="wiki-infobox">

| Feature | Detail |
|---|---|
| **Numerator** | Cash + Marketable securities + AR (most liquid) |
| **Denominator** | Daily operating expenses (COGS + SG&A + interest, ex-tax) |
| **Result** | Days of operating coverage |
| **Benchmark** | 30–60 days typical; >90 days very strong; <20 days concerning |
| **Comparison** | More conservative than current or quick ratio |
| **Limitation** | Ignores working capital timing (e.g., inventory turns) |
| **Use case** | Short-term solvency assessment; distressed companies |
| **Industry variation** | Retailers, manufacturers, tech; very different norms |

</aside>

## Calculation example

A retail company's annual financials:

- Cash: $15M
- Short-term marketable securities: $5M
- Accounts receivable: $10M
- Total liquid assets: $30M
- Annual operating expenses: $120M (COGS $70M, SG&A $40M, interest $10M)
- Daily operating expenses: $120M / 365 ≈ $328,767

**Defensive interval ratio = $30M / $328,767 ≈ 91 days**

The company can run for 91 days on liquid assets alone. This is healthy for most industries—most companies expect to generate cash from sales long before 91 days elapse. However, if a recession hits and sales plummet, this cushion is critical.

## Comparison to other liquidity ratios

| Ratio | Numerator | Denominator | Insight |
|---|---|---|---|
| **Current Ratio** | All current assets | Current liabilities | Can the company pay short-term debt? |
| **Quick Ratio** | (CA – Inventory) | CL | Excluding slow-moving inventory |
| **Cash Ratio** | Cash + marketable securities | CL | Most conservative; pure liquid cash |
| **Defensive Interval** | Cash + AR + securities | Daily operating expenses | How many days of normal ops? |

The defensive interval ratio is the only one that uses *operating expenses* as the denominator, making it unique. It asks about operational sustainability, not just debt repayment. A company might have a healthy [current ratio](/wiki/current-ratio/) (enough to pay creditors) but a weak defensive interval ratio (not enough liquid cash to survive a sales freeze).

## Industry and context variations

A **healthy defensive interval ratio** varies by industry:

- **Retailers and distributors**: 30–60 days typical. Retail turns inventory fast and converts cash quickly; 30 days of liquid assets is enough if suppliers and customers both continue flowing. Below 20 days is concerning.

- **Manufacturers**: 45–90 days. Manufacturing cycles are longer; raw materials, work-in-progress, and finished goods slow the cash conversion cycle. 60 days is a reasonable floor.

- **Software/SaaS**: 60–120 days. High upfront R&D costs and recurring revenue means SaaS companies maintain larger cash reserves. 200+ days is common for well-capitalized startups.

- **Financial institutions**: Different frameworks entirely (regulatory capital ratios replace this metric).

A company with 150 days of defensive interval coverage looks strong in a vacuum—but if the industry average is 200 days, it is below par. Conversely, 40 days in retail (where inventory is liquid) may be fine, but 40 days in manufacturing signals risk.

## Use in distress and covenant monitoring

Lenders and creditors monitor the defensive interval ratio of distressed borrowers. A company burning cash (expenses exceeding revenue) with a declining defensive interval ratio is a red flag: the company has months, not years, of runway before insolvency. Debt covenants sometimes include a floor: "Maintain a minimum defensive interval ratio of 30 days." Covenant violations can trigger acceleration and default.

Private equity firms use the defensive interval ratio when assessing LBO targets. A mature company with 200 days of liquid assets is a safer acquisition (lower financial risk) than one with 20 days. The target's working-capital optimization becomes a value-creation lever: shortening the defensive interval by improving [collection cycles](/wiki/accounts-receivable-turnover/) and turning inventory faster frees up cash for debt repayment.

## Limitations and complementary metrics

The defensive interval ratio assumes expenses remain constant if revenue drops—unrealistic for companies with variable costs. A retailer selling 0 units incurs zero cost of goods sold but still has rent and labor. A more realistic stress scenario adjusts the expense base down to fixed costs only.

The ratio also ignores **external financing optionality**: a healthy company can borrow in a pinch. A startup with 20 days of coverage but a $10M credit line is safer than it appears. Conversely, a company in distress (poor credit, covenant violations) cannot draw credit and faces the full defensive interval risk.

Complementary metrics include:

- **[Cash conversion cycle](/wiki/cash-conversion-cycle/)** — how long cash is tied up in operations.
- **[Operating cash flow ratio](/wiki/operating-cash-flow-ratio/)** — cash from operations divided by current liabilities; directly measure cash generation.
- **[Free cash flow](/wiki/free-cash-flow/)** — after capex; the cash truly available for debt service and dividends.

A company with a weak defensive interval ratio but strong operating cash flow and free cash flow is less risky than the ratio alone suggests—the company is generating cash, not just burning it.

<div class="wiki-seealso">

### Closely related
- [Quick Ratio](/wiki/quick-ratio/) — includes receivables, excludes inventory
- [Current Ratio](/wiki/current-ratio/) — broader liquidity measure
- [Cash Ratio](/wiki/cash-ratio/) — most conservative liquidity metric
- [Operating Expenses](/wiki/operating-income-to-price/) — denominator of the ratio

### Wider context
- [Cash Conversion Cycle](/wiki/cash-conversion-cycle/) — working-capital timing
- [Operating Cash Flow](/wiki/operating-cash-flow-ratio/) — cash actually generated
- [Free Cash Flow](/wiki/free-cash-flow/) — cash available after capex
- [Debt Covenants](/wiki/debt-covenant-type/) — financial-ratio requirements

</div>

---
title: "Accounts Receivable Aging Schedule"
description: "Accounts receivable aging schedule explained: breaks down customer balances by payment timeliness to estimate uncollectible amounts."
keywords:
  - accounts receivable aging schedule
  - allowance for doubtful accounts
  - uncollectible receivables
  - aging buckets days past due
image: "/svg/accounting.svg"
---

*An accounts receivable aging schedule is a table that categorizes outstanding customer invoices by how long they have been unpaid. Buckets—typically current, 30, 60, 90+ days past due—reveal which invoices are at risk of non-collection, allowing the company to estimate and reserve for bad debt.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Receivable Aging Schedule — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting." />

<div class="wiki-infobox-caption">Stale invoices signal credit risk; time-based buckets and historical loss rates drive bad-debt estimates.</div>

|   |   |
|---|---|
| **Typical buckets** | Current, 31–60 days, 61–90 days, 91+ days past due |
| **Purpose** | Estimate uncollectible balances; support internal credit decisions |
| **Output** | Allowance for [doubtful accounts](/accounts-receivable/) reserve on the balance sheet |
| **Accounting method** | Aging method (historical loss rates per bucket) or percentage of sales |
| **Standard** | [ASC 326](/asc-606/) (Credit Losses), [GAAP](/generally-accepted-accounting-principles/) guidance |
| **Reporting unit** | Usually prepared monthly or quarterly for management; summarized in year-end financials |

</aside>

## Why aging matters

A customer invoice due on January 15 but still unpaid in May is less likely to be collected than one due next week. The longer an invoice sits unpaid, the higher the credit risk. An aging schedule quantifies this intuition: by grouping invoices by age, a company can apply historical loss rates to each bucket, estimating how much of its [accounts receivable](/accounts-receivable/) will ultimately not be paid.

This estimate is recorded as an "allowance for doubtful accounts"—a contra-asset account that reduces the gross receivable balance to a net, realizable amount. Under [ASC 326](/asc-606/) (effective for large public companies in 2020), companies must use an "expected credit loss" model, incorporating probability of default, loss given default, and exposure at default—directly supported by aging data.

## Constructing an aging schedule

A simple aging schedule lists customer balances and age bands. Here is a stylized example:

| Customer | Current | 1–30 Days | 31–60 Days | 61–90 Days | 91+ Days | Total Balance |
|---|---|---|---|---|---|---|
| ABC Corp | $10,000 | $5,000 | — | — | — | $15,000 |
| XYZ Ltd | — | $8,000 | $3,000 | $2,000 | $1,000 | $14,000 |
| Global Inc | $20,000 | — | — | — | — | $20,000 |
| **Total** | **$30,000** | **$13,000** | **$3,000** | **$2,000** | **$1,000** | **$49,000** |

Next, the company applies historical loss rates (the percentage of invoices in each bucket that were ultimately not collected) to estimate the reserve. For example:

| Bucket | Total Balance | Historical Loss Rate | Reserve Amount |
|---|---|---|---|
| Current | $30,000 | 0.5% | $150 |
| 1–30 days | $13,000 | 2% | $260 |
| 31–60 days | $3,000 | 5% | $150 |
| 61–90 days | $2,000 | 15% | $300 |
| 91+ days | $1,000 | 30% | $300 |
| **Total** | **$49,000** | | **$1,160** |

The company then records or adjusts the allowance to $1,160:

- Debit: Uncollectible Account Expense (Income Statement) $1,160
- Credit: Allowance for Doubtful Accounts (Balance Sheet) $1,160

On the balance sheet, accounts receivable is shown as:

> Accounts Receivable (gross)     $49,000
> Less: Allowance for Doubtful Accounts     ($1,160)
> Accounts Receivable (net)     $47,840

## Historical loss rates: the foundation

Loss rates are derived from the company's own history. If, over the past three years, the company invoiced $1 million to customers and ultimately collected $970,000, the overall loss rate is 3%. But this varies by age: invoices more than 90 days old might have a 25% loss rate, while current invoices might have a 0.5% rate.

Companies track this by:

1. **Recording invoiced amounts by date.**
2. **Recording cash collections and write-offs** over time.
3. **Calculating the percentage of each age cohort** that was never collected.
4. **Updating the rates** annually based on rolling recent data.

A company with improving credit quality (faster payments, lower default) will see loss rates decline; conversely, economic downturns or industry disruption can cause rates to spike.

## Allowance vs. write-off: the cycle

When an invoice is deemed uncollectible, it is written off against the allowance. Suppose XYZ Ltd's $1,000 invoice from six months ago is deemed worthless. The company records:

- Debit: Allowance for Doubtful Accounts $1,000
- Credit: Accounts Receivable $1,000

The allowance declines, as does gross receivable; the net amount is unaffected, so net income is unaffected (the expense was already recorded when the allowance was established). Later, if XYZ pays part or all of the written-off balance, the company may reverse part or all of the write-off.

## Aging method vs. percentage-of-sales

Two broad approaches to estimating the allowance exist:

**Aging method.** Apply historical loss rates to each age bucket (as shown above). This is the more precise method, especially for companies with varied customer creditworthiness or payment patterns. It captures the reality that older invoices are riskier.

**Percentage-of-sales method.** Reserve a fixed percentage of credit sales in the period. For example, if a company historically loses 2% of its credit sales, it reserves 2% of this quarter's credit sales. This is simpler but less nuanced and can lag reality if payment patterns change.

Most mature, mid-to-large companies use aging; smaller entities or those with stable, homogeneous customer bases may use percentage-of-sales.

## ASC 326 and the expected credit loss model

Under the new expected credit loss (ECL) standard, companies no longer wait for a loss to be "probable" before reserving; instead, they reserve for all expected losses, even if remote. The reserve incorporates:

- **Probability of default (PD):** The likelihood the customer will not pay.
- **Loss given default (LGD):** The percentage of the balance that will not be recovered.
- **Exposure at default (EAD):** The outstanding balance at the time of default.

Allowance = PD × LGD × EAD, summed across all customers (or estimated using the aging method as a proxy).

Aging schedules directly support this calculation: older buckets have higher PDs; internal collection efforts and recovery rates inform LGD.

## Internal decision-making

Beyond financial reporting, aging schedules drive operational credit decisions:

- **Collections priority.** The 91+ day bucket gets the most urgent attention and follow-up.
- **Credit limit reviews.** Customers with persistent aging may have credit limits reduced or terms tightened.
- **Concentration risk.** If one customer dominates the 61–90 day bucket, management flags the concentration.
- **Seasonal patterns.** Predictable aging spikes (e.g., post-holiday seasons) are anticipated and reserved for.

## Challenges and limitations

**Estimation error.** Loss rates based on recent history may not reflect future conditions; a sudden economic downturn can render historical rates obsolete.

**Customer concentration.** A single large customer's payment failure skews the reserve; aging alone may underestimate risk if that customer is stressed.

**Segment differences.** A company with domestic and international customers, or retail and wholesale channels, may need separate aging schedules per segment to avoid blending distinct risk profiles.

**Subjective collectibility judgments.** Some invoices are disputed (wrong shipment, delivery issues); aging does not flag these unless tracked separately.

## Integration with the cash flow statement

Aging and write-offs affect the [cash flow statement](/cash-flow-statement/) indirectly. Changes in accounts receivable (a working capital item) reduce or increase operating cash flow. A company that aggressively writes off old receivables will show lower ending receivable balances, improving the working capital line; conversely, lenient collection or growth in sales to risky customers will increase receivables and reduce reported operating cash flow.

## See also

<div class="wiki-seealso">

### Closely related

- [Accounts Receivable](/accounts-receivable/) — the asset being analyzed
- [Allowance for Doubtful Accounts](/accounts-receivable/) — the reserve estimated via aging
- [Bad Debt Expense](/accounts-receivable/) — the income statement impact of write-offs and adjustments
- [Credit Risk](/credit-risk/) — the underlying risk being quantified
- [Income Statement](/income-statement/) — where bad-debt expense is reported

### Wider context

- [Balance Sheet](/balance-sheet/) — where gross and net receivables appear
- [Cash Flow Statement](/cash-flow-statement/) — changes in receivables affect operating cash
- [Generally Accepted Accounting Principles (GAAP)](/generally-accepted-accounting-principles/) — ASC 326 is the governing standard
- [Working Capital](/cash-conversion-cycle/) — receivables are a key component

</div>

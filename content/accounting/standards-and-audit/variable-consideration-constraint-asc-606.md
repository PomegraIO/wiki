---
title: "Variable Consideration Constraint Under ASC 606"
description: "Understand ASC 606's constraint on variable revenue: when to limit estimated bonuses, rebates, and penalties to avoid revenue reversals."
keywords:
  - variable consideration constraint ASC 606
  - ASC 606 constraint
  - revenue constraint
  - variable revenue recognition
  - significant reversal test
image: "/svg/accounting.svg"
---

*The **variable consideration constraint** is a critical rule in ASC 606 (the FASB's revenue recognition standard) that requires companies to exclude or cap estimated variable payments—such as rebates, performance bonuses, or penalties—unless they are highly probable that no significant reversal will occur. Without this constraint, companies could recognize overly optimistic revenue, only to write it down later when actual claims, refunds, or adjustments become known.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Variable Consideration Constraint — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The guardrail that prevents aggressive revenue forecasting under ASC 606.</div>

|   |   |
|---|---|
| **Core test** | Only include variable amounts that are "highly probable" of no significant reversal |
| **Types affected** | Rebates, volume discounts, performance bonuses, warranties, penalties, contingent fees |
| **When triggered** | Whenever outcome is uncertain or customer has a claim/refund right |
| **Related concept** | [Revenue recognition](/revenue-recognition/), [accrual accounting](/accrual-accounting/), [ASC 606](/asc-606/) |
| **Practical impact** | Often forces deferral of revenue until uncertainty is resolved or claim period expires |

</aside>

## The five-step model and where the constraint applies

ASC 606 lays out five steps to recognize revenue: (1) identify the contract, (2) identify performance obligations, (3) determine transaction price, (4) allocate the price to obligations, and (5) recognize revenue as obligations are satisfied. The variable consideration constraint sits inside **step three**—determining the transaction price.

The transaction price is the amount of consideration the company expects to receive in exchange for delivering goods or services. In many deals, that price is fixed (a customer buys 100 units at $10 each, for $1,000 total). But in many others, the price is contingent on future events:

- A software company offers a $50,000 license with a **$10,000 performance bonus** if the customer achieves certain adoption metrics.
- A distributor sells goods at a list price but offers a **rebate** if the customer hits a volume target.
- A contractor is paid $500,000 for a project but faces **penalties** if certain milestones are missed.
- A consulting firm bills a base fee but earns a **success fee** tied to client revenue improvements.

In the absence of a constraint, the company could include the full bonus, rebate, or contingent amount in the initial transaction price, recognizing all revenue upfront. The constraint prevents this overly optimistic practice.

## The "highly probable" test

ASC 606 requires that variable consideration be included in the transaction price **only if it is highly probable that a significant reversal will not occur**. "Highly probable" is interpreted as roughly 75%–90% confidence (not an exact threshold, but a high bar of certainty). A "significant reversal" means that the amount actually received or accepted later differs materially from what was originally estimated.

The test is forward-looking and scenario-based:

- **Can the customer claim a refund or credit?** If the customer has the right to return goods, claim a rebate, or receive a credit, the company must assess how likely it is that the right will be exercised.
- **Is the outcome genuinely uncertain?** If the performance bonus depends on the customer hitting adoption targets, and history shows variability, the company must reserve judgment rather than assume the best case.
- **What does historical data say?** If the company has years of claims data showing that X% of customers exercise a refund right, that empirical rate informs the estimate.
- **Are there stand-still periods or claim windows?** If a rebate claim expires 180 days after the sale, the company can include it in revenue once the claim window closes without a claim.

## Practical application: worked examples

**Example 1: Performance bonus on software sales**

A company sells a $100,000 three-year enterprise software license. The contract includes a $25,000 annual performance bonus if the customer's usage hits a specified threshold, assessed at year-end. The company estimates a 60% probability the customer will hit the target.

Under the constraint, the company **cannot** include the expected bonus ($25,000 × 60% = $15,000) in the transaction price. Why? Because hitting the usage threshold is contingent on customer behavior that the company cannot fully control and is not "highly probable" at inception. Instead:

- The company recognizes $100,000 in year one.
- As each year passes, the company updates its estimate. If, at the end of year one, the customer **does** hit the threshold, the company can now recognize that year's $25,000 bonus (it is no longer contingent; the performance obligation is satisfied).
- If the customer misses the threshold in year one, the company does not reverse revenue; it simply does not recognize the bonus.

**Example 2: Volume rebate**

A distributor sells $500,000 of products to a retailer, offering a $50,000 rebate if the retailer purchases more than $750,000 in the calendar year. Historical data shows that 85% of customers hit the volume target.

The 85% hit rate seems like "highly probable," but the constraint also requires that the company assess whether the individual customer is likely to hit the target—not just rely on aggregate averages. If this customer is new or has historically fallen short of volume commitments, the company may not treat 85% as reliable for this contract. If the customer is a large, reliable account with a strong history, the company might include the rebate.

Assuming the company includes the full $50,000 rebate, the transaction price is $550,000 and revenue is recognized upfront. At year-end, if the customer indeed exceeded $750,000, the rebate is owed and no adjustment is needed. If the customer fell short, the company reverses the $50,000 rebate provision and reduces revenue (or increases revenue if no amount was initially reserved).

**Example 3: Warranty and refund rights**

A retailer sells a $300 electronics item with a 30-day return right and a $30 warranty coverage option. Historical data shows 10% of customers exercise the return right (a $300 refund) and 20% of warranty purchasers claim benefits averaging $15.

The return right is clear and empirically supported: the company reduces the transaction price by $30 (10% of $300), recognizing $270 in revenue. At the end of the 30-day window, if the return rate matches history, no adjustment is needed. If it deviates materially, the company adjusts.

The warranty is trickier: the $15 expected payout occurs over the warranty period (e.g., two years), not upfront. The company may estimate a $3 warranty liability (20% × $15) but should reconsider whether to reduce revenue upfront or recognize the warranty obligation separately. ASC 606 distinguishes between warranty-as-performance-obligation (which reduces transaction price and revenue) and warranty-as-liability (which is a separate liability under ASC 450, Contingencies). The company's choice here turns on whether the warranty is a service the customer purchased or a promise to fix a defective product.

## When to conservatively estimate and defer

Best practice under the constraint is to ask: **Is the outcome genuinely certain or highly probable?**

Conservative positions:
- **Defer the bonus or rebate.** Recognize revenue only for the fixed portion; wait until the contingency is resolved.
- **Use the most likely amount.** If outcomes range from $0 to $50,000, estimate the most-likely single outcome (not the expected-value average) and assess whether it passes the "highly probable no reversal" bar.
- **Use empirical claim rates.** Historical data is the strongest support; aggregate averages are weak if applied to an atypical customer.
- **Document the assessment.** The constraint requires judgment, and the company should document why variable amounts are included or excluded.

Aggressive positions:
- **Include the full bonus if the trend is favorable.** If the last five years show increasing customer adoption, assume the trend continues.
- **Use aggregate hit rates.** If 90% of customers hit rebate thresholds, include the rebate for most customers.
- **Shorten claim windows.** Argue that if no claims are made within 90 days, the company can reverse the reserve and recognize the revenue.

The FASB's intent is to force discipline: companies cannot wishfully include revenue and reverse it later. The constraint is the mechanism.

## Common errors and misapplications

**Error 1: Confusing "highly probable" with "more likely than not."** In probability, "more likely than not" is >50%; "highly probable" is 75%+. The constraint sets a higher bar.

**Error 2: Using expected value instead of most likely outcome.** ASC 606 permits two methods: the "expected value" method (probability-weighted sum) or the "most likely amount" method (the single most probable outcome). The constraint applies to both, but the company's judgment of probability is different. If outcomes are bimodal (either $0 or $100), expected value might be $50, but the most likely amount is $0 or $100 (not $50).

**Error 3: Ignoring customer-specific factors.** A company uses a blanket rebate rate across all customers, even though a particular customer has a weak history or is in a distressed market. The constraint requires customer-level assessment, not blanket averages.

**Error 4: Failing to reassess.** As time passes and new information arrives, the company must update its estimate of variable consideration. If a customer signals strong usage at mid-year, the company should recognize the bonus. If a customer approaches a rebate threshold late in the year, the company may need to book a reserve.

## Integration with other accounting standards

The constraint interacts with ASC 450 (Contingencies), which governs uncertain liabilities and asset reversals. A reserve for a rebate or return is a contingent liability until the contingency is resolved. Under ASC 606, the transaction price is reduced; under ASC 450, a refund liability is recognized. The two are closely related and must be coordinated in the company's financial statements and internal controls.

The constraint also ties to [revenue-recognition](/revenue-recognition/) timing and [accrual accounting](/accrual-accounting/) principles: deferred variable revenue is recognized ratably, when the contingency is resolved, or when the claim window expires. This timing must align with the satisfaction of performance obligations.

## See also

<div class="wiki-seealso">

### Closely related

- [ASC 606](/asc-606/) — the foundational revenue standard that contains the constraint
- [Revenue recognition](/revenue-recognition/) — the overarching principle; the constraint is a sub-rule
- [Accrual accounting](/accrual-accounting/) — how companies book contingent liabilities and defer revenue
- [Fair value](/fair-value/) — the basis for estimating transaction price and variable amounts
- Contingencies — ASC 450 governs uncertain liabilities related to variable considerations

### Wider context

- [Earnings quality](/earnings-quality/) — aggressive variable-consideration practices are a red flag for earnings quality
- [Income statement](/income-statement/) — where the constraint's impact is most visible in revenue and refund-liability line items
- [Form 10-K](/10-k/) — companies must disclose significant judgments about variable consideration in MD&A and footnotes
- Cost of revenue — rebates and adjustments reduce net revenue and affect margin analysis
- [Segment reporting](/segment-reporting/) — variable-consideration adjustments are sometimes tracked by customer segment or geography

</div>

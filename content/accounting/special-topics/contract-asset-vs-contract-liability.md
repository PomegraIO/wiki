---
title: "Contract Asset vs Contract Liability"
description: "The difference between contract assets (earned but unbilled revenue) and contract liabilities (advance payments before performance)."
keywords:
  - contract asset
  - contract liability
  - asc 606
  - revenue recognition
  - deferred revenue
  - contract balances
image: "/svg/accounting.svg"
---

*Under modern revenue accounting rules, companies must distinguish between **contract assets** and **contract liabilities**—two sides of the same timing mismatch. A contract asset arises when you have earned the right to payment but have not yet billed the customer; a contract liability emerges when you have been paid in advance before delivering the good or service.*

<div class="wiki-hatnote">

For the broader framework governing these classifications, see [ASC 606](/asc-606/). For related balance sheet items, see [Accounts Receivable](/accounts-receivable/), [Deferred Revenue](/deferred-revenue/), and [Revenue Recognition](/revenue-recognition/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contract balances — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting." />

<div class="wiki-infobox-caption">Contract assets and liabilities arise from the timing gap between performance and payment.</div>

|   |   |
|---|---|
| **Contract asset** | Earned the right to payment, not yet billed (asset side) |
| **Contract liability** | Received cash or obligation to pay, not yet earned revenue (liability side) |
| **Recognition point** | Assessed when contract is signed and performance obligations identified |
| **Balance sheet location** | Current assets or liabilities (if performance < 1 year) or non-current |
| **Reclassification** | Asset converts to receivable on billing; liability converts to revenue when earned |
| **Overlap risk** | Impairment must be assessed for contract assets under expected credit loss models |

</aside>

## The core distinction: the performance vs. billing gap

**Contract Asset:** You have performed your obligations (delivered goods, rendered services, completed milestones) and have the unconditional right to payment—but you have not yet invoiced the customer.

**Contract Liability:** The customer has paid you (or you have an unconditional obligation to refund or provide a credit) before you have fulfilled your performance obligation.

The two represent opposite ends of the execution timeline. At any given moment, a company may have one, both, or neither, depending on how contracts are structured.

## When contract assets arise

A contract asset emerges in contracts where billing is tied to performance milestones, achievement of KPIs, or the customer's usage—not to a fixed invoice schedule.

**Example 1: Software development services.** A consultant signs a contract to build custom software for a client. The pricing is $500,000. The contract specifies that payment is due upon delivery of the final system, but the consultant is entitled to invoice for completed development work before final delivery. By the end of month 2, the consultant has completed design and development totaling $150,000 in value. She recognizes $150,000 in revenue under [ASC 606](/asc-606/), but she has not sent an invoice. The difference is a contract asset of $150,000.

Journal entry (month 2):
```
Debit:  Contract Asset          $150,000
Credit: Revenue (Performance)             $150,000
```

When the consultant invoices the customer:
```
Debit:  Accounts Receivable     $150,000
Credit: Contract Asset                    $150,000
```

The contract asset converts to a receivable—now the customer officially owes the invoice.

**Example 2: Gas utility providing service.** A gas utility delivers gas to customers monthly, and because the meter reading and billing lag by 2 weeks, the utility has earned the right to revenue for delivered gas it has not yet billed. The utility records a contract asset for the unbilled volumes.

## When contract liabilities arise

A contract liability (often called deferred revenue or advance payment) arises when a customer pays upfront before the company has delivered goods or rendered services.

**Example 1: Subscription or SaaS.** A company sells a 12-month software license for $120,000 upfront. On day 1, the customer pays the full amount. The company recognizes it has a performance obligation to provide 12 months of access. It cannot recognize all $120,000 as revenue yet (only $0 on day 1). Instead, it records:

```
Debit:  Cash                    $120,000
Credit: Contract Liability (Deferred Revenue)  $120,000
```

As each month passes, the company earns the right to $10,000 in revenue:

```
Debit:  Contract Liability      $10,000
Credit: Revenue                            $10,000
```

**Example 2: Home builder receiving a down payment.** A home builder signs a contract to build a house for $400,000. The customer puts down $100,000 on signing. The builder has the cash but has not earned it (no construction has occurred). The down payment is a contract liability until the builder performs.

```
Debit:  Cash                    $100,000
Credit: Contract Liability (Progress billing liability)  $100,000
```

As the builder completes 25% of the work:

```
Debit:  Contract Liability      $100,000
Credit: Revenue                            $100,000
```

And so on as milestones are met.

## The reclassification cycle

A contract asset and contract liability are in motion. They do not remain on the balance sheet indefinitely; they resolve as time passes and the business executes.

**Contract asset → Accounts Receivable → Cash**

A company earns revenue (contract asset), invoices the customer (converts to [Accounts Receivable](/accounts-receivable/)), and collects payment (converts to cash). The contract asset is temporary.

**Contract Liability → Revenue → (already received as cash)**

A customer pays in advance (contract liability), the company delivers (revenue is recognized, reducing the liability), and no further cash is exchanged. The liability shrinks to zero.

## Practical interplay: the general contractor

Consider a large construction contract with milestone billing. The contract is $1 million, with 5 equal milestones (20% each = $200,000 per milestone).

- **Month 1:** General contractor begins work. No billings yet, no cash in. No asset or liability.
- **Month 3:** Contractor completes milestone 1 (20% = $200,000 earned). Issues invoice. Records:
  - Debit: Contract Asset $200,000 / Credit: Revenue $200,000 (for performance earned)
  - Debit: Accounts Receivable $200,000 / Credit: Contract Asset $200,000 (for invoice issued)
  
  Net on balance sheet: AR $200,000.

- **Month 4:** Client pays invoice. Debit: Cash $200,000 / Credit: Accounts Receivable $200,000. AR is now zero.

- **Month 6:** Contractor completes milestone 2 but the contract specifies that the client gets a 30-day grace period before the invoice must be sent. Under ASC 606, if the contractor unconditionally has the right to the payment (only time and paperwork remain), a contract asset arises for $200,000.

- **Month 7:** Contractor invoices. Contract asset converts to AR, then to cash.

At any moment, the balance sheet shows the state of performance and cash collection. Comparing contract assets to contract liabilities reveals whether the business is ahead of cash (assets) or behind (liabilities).

## Impairment and expected credit losses

Contract assets are subject to expected credit loss analysis (like [Accounts Receivable](/accounts-receivable/)). If a contract asset reflects future cash from a customer with uncertain ability to pay, it may need to be impaired. Contract liabilities, by contrast, do not typically require allowance recognition (since the company has already received the cash and the obligation is to perform, not to refund).

## Disclosure requirements

Public companies must disclose contract assets and liabilities separately on the balance sheet (or in the notes) and must explain significant changes period over period. The notes will typically show:

- Opening and closing balances
- Amounts recognized in revenue from opening liabilities (revenue from performance in period)
- New contract liabilities from contracts signed in the period

This transparency helps investors and creditors understand the quality of earnings and the timing of future cash conversion.

## Common confusion points

**Contract asset ≠ Accounts Receivable.** A contract asset is the right to invoice (earned but unbilled). An AR is the right to cash (invoiced but unpaid). The contract asset is one step earlier.

**Contract liability ≠ Warranty obligation.** A contract liability is an unearned performance obligation (you owe the customer goods or services). A warranty obligation is a separate liability for potential remediation costs. They are independent.

**Contract asset can impair; liability cannot.** Because a contract asset depends on future cash collection, it must be assessed for expected loss. A contract liability is an obligation to perform; the company has cash in hand and the liability shrinks as it delivers.

## See also

<div class="wiki-seealso">

### Closely related

- [ASC 606](/asc-606/) — the revenue recognition standard governing both contract balances
- [Revenue Recognition](/revenue-recognition/) — when revenue is earned under ASC 606
- [Accounts Receivable](/accounts-receivable/) — the billing and collection side of the cycle
- [Deferred Revenue](/deferred-revenue/) — the common term for contract liabilities
- [Accrual Accounting](/accrual-accounting/) — the principle underlying contract-based timing
- [Income Statement](/income-statement/) — where contract-based revenue flows
- Impairment — expected loss testing for contract assets

### Wider context

- [Balance Sheet](/balance-sheet/) — where contract assets and liabilities appear
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — the conceptual framework including ASC 606
- [International Financial Reporting Standards](/international-financial-reporting-standards/) — the analogous standard under IFRS 15
- [Cash Flow Statement](/cash-flow-statement/) — how contract-based timing affects working capital

</div>
---
title: "Lease Modification Accounting Under ASC 842"
description: "Learn when lease modifications trigger new contract accounting or remeasurement under ASC 842, with practical examples and journal entries."
keywords:
  - lease modification asc 842
  - lease remeasurement
  - asc 842 changes
  - operating lease modification
  - finance lease modification
image: "/svg/accounting.svg"
---

*A **lease modification** under ASC 842 either creates a separate new contract or remeasures the existing lease liability—the distinction determines whether you recognize a gain or loss immediately. Identifying which applies requires careful analysis of the modification's scope, cash flows, and whether commercial terms have genuinely shifted.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lease Modification Accounting — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting standards." />

<div class="wiki-infobox-caption">ASC 842 splits modifications into two paths: separate contract treatment or remeasurement.</div>

|   |   |
|---|---|
| **When it applies** | Any change to lease terms that substantially alters economics |
| **Separate contract** | New scope, new options, incremental payments form distinct economic unit |
| **Remeasurement** | Existing lease terms revised; liability recalculated and repriced loss/gain recognized |
| **Key test** | Would a standalone price for the modification's incremental rights equal or exceed the incremental cash outflow? |
| **Lessee journal entry (separate)** | Debit ROU asset, credit lease liability + cash |
| **Lessee journal entry (remeasure)** | Adjust ROU asset, lease liability; recognize P&L impact immediately |

</aside>

## The two paths under ASC 842

ASC 842 is unambiguous in structure: when a lease is modified, you must first ask whether the modification is **substantial enough to be a separate lease**. If yes, you account for it as a brand-new contract, side-by-side with the original. If no, you treat it as a change to the existing lease—remeasure the liability and adjust your accounting accordingly.

The bright-line test lies in whether the modification grants the lessee **additional right-of-use assets** that weren't present before. In plain terms: if the company gains the right to use something new, or to use existing assets under materially different terms that economic analysts would price separately, it's a new lease. Otherwise, it's a remeasurement.

## When a modification is a separate lease

A modification creates a **separate new lease** when both conditions hold:

1. **The lease grants the lessee an additional right of use** of an identified asset (or a part of an asset).
2. **The incremental consideration** the lessee promises to pay equals or exceeds the **standalone price** for the additional right-of-use asset.

Consider a practical example: a manufacturer has a 5-year operating lease on a 10,000-square-foot warehouse. After two years, the lessee and lessor agree to add an adjacent 5,000-square-foot space, with a separate rent schedule reflecting current market rates. Since the lessee has gained a distinct right to use new space, and the rent promised for that space aligns with what the lessor would charge a new tenant, this is a **separate lease**. The original lease remains on the books; the new warehouse section is capitalized as a second lease asset with its own right-of-use and liability.

Conversely, a modification is **not** a separate lease if the change merely extends the term, adjusts the payment schedule on existing space, or modifies non-lease components (maintenance, taxes). A lessee and lessor might agree to extend an existing office lease by two years, keeping the same square footage and rate structure. That extension modifies the original lease; it does not create a new one.

## How remeasurement works

When a modification does not qualify as a separate lease, you remeasure the **lease liability and right-of-use asset** as of the modification date. The journal entry depends on whether the lessee must recognize a loss or gain on the change.

**Step 1: Recalculate the lease liability.** Use the modified cash flows (new payment schedule, revised term, new interest rate if applicable) and the lease's incremental borrowing rate (or the original rate, if no change to credit risk). Discount to present value as of the modification date.

**Step 2: Determine the new ROU asset balance.** The new ROU asset equals the remeasured liability, adjusted for any prepaid or accrued lease payments, and minus any lease incentives the lessor grants as part of the modification.

**Step 3: Recognize the gain or loss.** Compare the old ROU asset (net of accumulated depreciation) to the new ROU asset. If new ROU < old net ROU, recognize a gain. If new ROU > old net ROU, recognize a loss.

### Worked example: remeasurement with a loss

A hospital has a finance lease on diagnostic imaging equipment with:
- Original remaining liability: $800,000 (4 years remaining, $50,000 annual payments)
- Original ROU asset (gross): $900,000; accumulated depreciation: $225,000 (net: $675,000)
- Incremental borrowing rate: 5%

The lessor and lessee agree to extend the lease by two additional years, with annual payments rising to $60,000 (to reflect equipment wear and market escalation). No other terms change.

New lease liability:
- Years 1–4: $50,000 per year
- Years 5–6: $60,000 per year
- Discount at 5%: ($50,000 × 3.546) + ($60,000 × 1.859) = $177,300 + $111,540 = $288,840
- But we need to account for the old liability's present value. More directly: the remaining obligation ($200,000 over 4 years at $50,000/yr) discounts to $177,300. Adding the two new years at $60,000/yr discounted: PV = $177,300 + ($60,000 ÷ 1.05^4) × (1 ÷ 1.05) + ($60,000 ÷ 1.05^5) × (1 ÷ 1.05) ≈ $177,300 + $49,342 + $47,002 = $273,644

(In practice, you'd calculate the full remaining obligation stream as of the modification date.)

Assume the recalculation yields a new liability of $890,000.

- Old net ROU asset: $675,000
- New net ROU asset: $890,000
- Loss to recognize: $890,000 − $675,000 = $215,000 (operating loss on the remeasurement)

Journal entry (at modification date):
```
Debit: Equipment ROU asset  $215,000
  Credit: Equipment lease liability                 $215,000
  (To adjust for remeasurement of lease)

Debit: Lease expense (or operating loss)  $215,000
  Credit: Equipment ROU asset              $215,000
  (To recognize loss on lease modification)
```

In practice, many organizations combine these into a single entry:
```
Debit: Lease expense                       $215,000
Debit: Equipment lease liability           $890,000
  Credit: Equipment ROU asset (gross)                $1,105,000
  (To remeasure lease and recognize loss)
```

## Lessee vs. lessor perspectives

For the **lessor**, the accounting is typically simpler. A modification that does not result in a new lease is treated as a reassessment of the original lease classification. If the lease was operating, it generally stays operating. If it was finance (sales-type), the lessor may need to recalculate the selling profit or loss, but the asset remains on the balance sheet (or already has been derecognized if sales-type).

For the **lessee**, modifications are more frequent in decision trees because the lessee must segregate new assets and revalue existing ones under ASC 842's stricter bright-line rules.

## Common modifications that trigger remeasurement

- **Rate adjustments**: The lessor and lessee agree to increase or decrease the payment schedule due to inflation, credit-rating changes, or refinancing. The lease term and asset scope do not change.
- **Term extensions**: Both parties agree to prolong the lease without materially new rights. A 2-year extension of an office lease at existing rates is a remeasurement.
- **Partial early termination**: The lessee and lessor agree to reduce the leased space or shorten the remaining term. The liability must be remeasured and any gain recognized immediately.
- **Covenant or contingency modifications**: Changes to late-payment penalties, maintenance obligations, or other lease covenants may trigger remeasurement if they materially affect the cash flows.

## ASC 842 transition and reliance on judgment

ASC 842 became effective for most public companies in 2019 and for private companies in 2022. Since then, auditors and preparers have refined their interpretations of what constitutes a "separate lease." The dividing line between incremental payments and the standalone price for an incremental right-of-use asset requires careful analysis—especially for complex real-estate or equipment leases where comparable market data is limited.

Entities should document their conclusion (separate vs. remeasure) alongside the supporting computation. Changes in facts or interpretations may require retrospective adjustment if discovered later.

## See also

<div class="wiki-seealso">

### Closely related

- [Operating Lease](/operating-lease/) — foundational accounting model for non-ownership leases
- [Finance Lease](/finance-lease/) — balance-sheet treatment and lessee perspective
- [ASC 606](/asc-606/) — revenue recognition standard; often paired with lease modifications affecting consideration
- Lease Incentives — common cash outflow adjustment in lease remeasurement
- Incremental Borrowing Rate — discount rate critical to liability recalculation

### Wider context

- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — the regulatory home for ASC standards
- [Income Statement](/income-statement/) — where lease modification gains or losses appear
- [Balance Sheet](/balance-sheet/) — where ROU asset and lease liability are reported
- [Going Concern](/going-concern/) — long-term lease modifications may signal covenant stress

</div>

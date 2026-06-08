---
title: "Lease Modification Accounting Treatment"
description: "Understand lease modification accounting treatment under ASC 842 and IFRS 16: when a modification is a new lease, remeasurement of ROU assets, and change-in-substance tests."
keywords:
  - lease modification accounting treatment
  - ASC 842
  - IFRS 16
  - operating lease modification
  - right-of-use asset
  - lease remeasurement
---

*A **lease modification** is a change to the original contract terms—typically an extension, expansion of space, or change in payment schedule. Under ASC 842 and IFRS 16, a modification that substantially increases the scope or changes the economics is accounted for as a new lease; otherwise, the original lease is remeasured on the modification date, with an adjustment to the right-of-use (ROU) asset or a gain/loss recognized through the income statement.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lease Modification — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Distinguishing a new lease from a modification changes the ROU asset balance sheet treatment.</div>

|   |   |
|---|---|
| **New lease test** | Does modification substantially increase the scope or right of use? |
| **Accounting if new** | Record separate ROU asset and lease liability for additional rights |
| **Accounting if modification** | Remeasure existing lease liability; adjust ROU asset or record gain/loss |
| **Effective date** | Modification takes effect on the date of agreement (ASC 842) or date of change (IFRS 16) |
| **Key difference** | IFRS 16 is narrower on "additional right of use"; ASC 842 requires more judgment |

</aside>

## The Core Question: New Lease or Modification?

Under both ASC 842 (U.S. GAAP) and IFRS 16 (International), the accounting treatment of a lease change hinges on a single question: Does the modification substantially increase the scope of the lease?

If yes, it is accounted for as a separate, new lease. A second right-of-use asset and lease liability are recorded on the balance sheet.

If no, the original lease is remeasured. The existing lease liability is adjusted to reflect the new payments and terms; the ROU asset is either adjusted (if the change is favorable) or a gain/loss is recorded (if unfavorable).

This distinction matters for the balance sheet, the income statement, and lease footnote disclosures.

## What Constitutes "Substantially Increased Scope"?

### ASC 842 Approach

ASC 842 offers limited explicit guidance, requiring judgment. A modification substantially increases scope if:

- The lessee gains a right to use a materially larger area or additional underlying asset (e.g., the lessee leases an additional floor, an adjacent warehouse, or extra square footage). The increase must be more than incidental.
- The additional space or asset has standalone value and would normally be leased separately.

**Example 1 (New Lease):** A retailer leases 10,000 sq. ft. of store space. Two years in, the lease is modified to include an adjacent 3,000 sq. ft. section (30% expansion). This substantially increases scope. The additional 3,000 sq. ft. is accounted for as a separate lease.

**Example 2 (Modification):** A retailer leases 10,000 sq. ft. The lease is modified to extend the term by five years and reduce the rent. The scope of the underlying asset (the 10,000 sq. ft.) is unchanged. This is a modification, not a new lease.

### IFRS 16 Approach

IFRS 16 is more prescriptive. A modification grants an additional right of use (and is thus a new lease) if the lessee gains the right to use one or more underlying assets that the original lease did not grant. The increase must be distinguishable from the original right.

IFRS 16 also clarifies that a modification is *not* a new lease if:
- The modification only changes the lease terms (e.g., payment schedule, interest rate, or lease duration) without changing the underlying asset or the lessee's right to use.
- The modification changes lease payments to reflect changes in market conditions (e.g., rent resets based on an index or inflation).

Under IFRS 16, a rent increase tied to the [consumer-price-index](/consumer-price-index/) is a modification, not a new lease, because it does not expand the right of use—it just adjusts the price of the same right.

## Accounting for a New Lease

When a modification is judged to be a new lease, the lessee:

1. Recognizes a separate ROU asset for the additional rights.
2. Recognizes a separate lease liability for the future lease payments attributable to the new lease.
3. Applies the same [present-value](/discounted-cash-flow-valuation/) calculation used in initial lease recognition, using a new incremental borrowing rate at the modification date.

The original lease accounting is unchanged. Both the original and new lease ROU assets appear on the balance sheet; both lease liabilities appear in the balance sheet and interest-expense calculations.

**Example:** A truck lessor and lessee originally lease 20 trucks. On modification, the lessee adds 5 trucks under the same lease agreement. The 5 additional trucks are accounted for as a new lease under ASC 842, with a separate $150,000 ROU asset and $150,000 lease liability recognized at the modification date.

## Accounting for a Lease Modification (Not a New Lease)

When the modification is not a new lease, the lessee remeasures the lease as of the modification date:

1. **Remeasure the lease liability** at the modified lease payments, discounted at the original incremental borrowing rate (ASC 842) or the modified rate if the modification changes the discount rate (IFRS 16).

2. **Adjust the ROU asset** by the change in the lease liability:
   - If the lease liability decreases (e.g., rent is cut), reduce the ROU asset and record a gain in earnings (or reduce a loss carryforward).
   - If the lease liability increases (e.g., extension with the same rent), increase the ROU asset (debit), with a corresponding increase to the liability.

### Favorable Modification Example (Rent Decrease)

An operating lease requires $100,000 annual payments for a remaining 5-year term. The lessee's incremental borrowing rate is 5%; the present value of remaining liabilities is approximately $432,948.

The lease is modified to reduce annual payments to $95,000. The new present value of remaining 5-year liabilities is approximately $411,007.

- Old lease liability: $432,948
- New lease liability: $411,007
- Adjustment: $21,941 reduction

The lessee records:
- Debit: Lease Liability: $21,941
- Credit: Operating Lease ROU Asset: $21,941 (or Income if the ROU asset balance is below the adjustment amount)

No gain is immediately recognized; instead, the ROU asset is reduced, and lower rent expense over the remaining term reflects the favorable modification.

### Unfavorable Modification Example (Extension with Same Rent)

An operating lease has 2 years remaining, with $100,000 annual payments (remaining liability ≈ $190,909 at 5% discount rate). The modification extends the term by 3 additional years at the same $100,000 annual payment.

The new 5-year present value of $100,000 annual payments is approximately $432,948.

- Old lease liability: $190,909
- New lease liability: $432,948
- Adjustment: $242,039 increase

The lessee records:
- Debit: Operating Lease ROU Asset: $242,039
- Credit: Lease Liability: $242,039

The ROU asset is increased to match the expanded liability, reflecting the lessee's fresh obligation.

## Incremental Borrowing Rate at Modification

Both standards require discounting the modified lease payments. The discount rate to use varies:

**ASC 842:** Use the original incremental borrowing rate at which the lease liability was initially recognized. This keeps the accounting clean—the ROU asset is simply adjusted by the change in liability.

**IFRS 16:** If the modification changes the substance of the lease (e.g., a different lessor, currency, credit quality), use the modified incremental borrowing rate. Otherwise, use the original rate.

In practice, ASC 842's approach (always original rate) is simpler and more common in the U.S.

## Practical Judgment Calls

Two tricky scenarios:

**Scenario 1: Rent reset based on market conditions.** A lease includes a clause: "Rent resets to fair market value every 5 years." The reset occurs on schedule. Is this a modification? Under IFRS 16, no—it is an anticipated lease term change. Under ASC 842, the treatment depends on whether the change is "substantial"; many practitioners treat it as a modification with no change in scope (remeasure at new rate). The right answer depends on the lease's original terms and the company's accounting policy.

**Scenario 2: Early renewal or extension with revised terms.** A lease originally had a 10-year term with two 5-year renewal options. The lessee exercises the renewal option but negotiates a rent cut. Is this a new lease? If only the payment changed and the underlying asset and remaining term are the same, both standards treat this as a modification (remeasure, adjust ROU asset or record gain).

## Income Statement Impact

Under ASC 842, a favorable modification reduces the ROU asset, typically lowering future rent expense—the benefit is amortized over the remaining lease term as lower depreciation. Under IFRS 16, the treatment is similar, though the mechanics of gain recognition differ slightly if the modification is not part of the original lease terms.

For financial statement users, modifications create a one-time swing in the ROU asset balance but smooth out through the income statement over the remaining term, provided the lease is not subsequently remeasured for other reasons (e.g., a new lease component).

## See also

<div class="wiki-seealso">

### Closely related

- [ASC 606](/asc-606/) — Revenue recognition standard; related to lease accounting under Topic 842
- [Operating Lease](/operating-lease/) — The lease classification under which most modifications occur
- Right-of-Use Asset — The balance sheet account that changes on a modification
- [Lease Liability](/lease-liability/) — The matching obligation, remeasured at modification
- Incremental Borrowing Rate — The discount rate used to remeasure lease liabilities

### Wider context

- IFRS 16 — International lease accounting standard with slightly different modification guidance
- [Balance Sheet](/balance-sheet/) — Where the ROU asset and lease liability appear
- [Income Statement](/income-statement/) — Where modification gains or losses flow
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — Overarching U.S. GAAP framework under which ASC 842 sits

</div>

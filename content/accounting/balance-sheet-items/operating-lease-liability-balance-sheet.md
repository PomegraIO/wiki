---
title: "Operating Lease Liability on the Balance Sheet"
description: "How the present value of operating lease payments is recognized as a liability and split into current and long-term portions under ASC 842 and IFRS 16."
keywords:
  - operating lease liability balance sheet
  - lease liability measurement
  - asc 842 current vs noncurrent
  - present value lease payments
  - ifrs 16 operating lease
image: "/svg/accounting.svg"
---

*Under ASC 842 and IFRS 16, the **operating lease liability** is the lessee's discounted obligation to pay all remaining lease payments, appearing on the balance sheet split between current (due within one year) and non-current (due after one year) portions. It is measured at inception using the lessee's incremental borrowing rate and is reduced as cash payments are made and interest accrues.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Operating Lease Liability — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Lease obligations now sit squarely on the balance sheet, creating transparency about future payment commitments.</div>

|   |   |
|---|---|
| **Initial measurement** | Present value of all lease payments discounted at borrowing rate or implicit rate |
| **Interest component** | Increases in early years; declines as liability balance decreases |
| **Current vs. non-current split** | Determined by whether payment is due within 12 months |
| **Reduction mechanism** | Decreases as principal payments are made; increases with interest accrual |
| **Discount rate** | Lessee's incremental borrowing rate (if implicit rate unknown) |
| **Applicable standards** | ASC 842 (US GAAP); IFRS 16 (IFRS) |

</aside>

## What Changed: Pre- and Post-2019 Treatment

Before ASC 842 took effect in 2019, operating leases were largely off-balance-sheet. Lessees expensed rent monthly but did not record a lease liability. This meant a company could be obligated to pay millions in future rent but show no corresponding obligation on the balance sheet—making leverage ratios appear artificially favorable and hiding the true cost of the business.

Under ASC 842 and IFRS 16, virtually all leases (operating and finance) now require the lessee to recognize both a [right-of-use asset](/right-of-use-asset-operating-lease/) and an operating lease liability. This fundamental change increased balance sheet liabilities for most lessees and brought lease financing closer to visibility with traditional debt.

## Measurement: The Present Value Calculation

The operating lease liability is measured as the present value of:
1. Fixed lease payments
2. Variable lease payments that depend on an index or rate (e.g., rent escalations tied to inflation)
3. Any residual value guarantees or purchase options the lessee is reasonably certain to exercise

**Excluded** from the liability are variable lease payments that do not depend on an index (e.g., usage-based or contingent payments not tied to an identifiable rate).

The discount rate applied is the lessee's **incremental borrowing rate** (IBR)—the rate the lessee would pay for a separate borrowing of similar maturity and credit quality. If the lease specifies an implicit rate, the lessee should use that instead. Most lessees use their IBR, which is estimated based on:
- Their credit rating and borrowing history
- Current market rates for similar borrowing
- The lease term

**Example:** A three-year equipment lease with annual payments of $100,000 (due at the end of each year). The lessee's IBR is 5%.

Present value = $100,000 / 1.05 + $100,000 / 1.05² + $100,000 / 1.05³
             = $95,238 + $90,703 + $86,384
             = **$272,325**

This $272,325 is the operating lease liability at inception. Paired with any direct execution costs, it also anchors the [right-of-use asset](/right-of-use-asset-operating-lease/).

## Current vs. Non-Current Split

On the balance sheet, the lease liability is split:

- **Current portion**: the principal amount of the next lease payment(s) due within 12 months of the balance sheet date
- **Non-current portion**: the remaining undiscounted principal of all future payments beyond 12 months

This is straightforward but requires careful computation. Using the example above, assume the lease began January 1, Year 1. At December 31, Year 1:

| Item | Amount |
|------|--------|
| Year 2 payment (due Dec 31, Year 2) | $100,000 |
| Year 3 payment (due Dec 31, Year 3) | $100,000 |
| Total remaining undiscounted payments | $200,000 |

However, at the end of Year 1, the liability has been partially satisfied by the first payment. The carrying amount has declined. The accounting splits this:

- **Current lease liability** = principal portion of Year 2 payment ≈ $90,703 (the discounted amount at inception)
- **Non-current lease liability** = principal portion of Year 3 payment ≈ $86,384

The amounts are derived by reducing the initial $272,325 by the principal portion of the Year 1 payment made.

## Interest Accrual and Principal Reduction

Each period, the operating lease liability changes in two ways:

1. **Interest accrual** — a financing cost computed as the beginning-of-period liability balance × the discount rate
2. **Principal payment** — the cash lease payment, minus interest

**Year 1 activity:**
- Beginning balance: $272,325
- Interest expense (Year 1): $272,325 × 5% = $13,616
- Cash lease payment (end of Year 1): $100,000
- Principal reduction: $100,000 − $13,616 = $86,384
- **Ending balance: $272,325 − $86,384 = $185,941**

| Year | Beginning Balance | Interest Expense | Cash Payment | Principal Reduction | Ending Balance |
|------|-------------------|------------------|--------------|----------------------|-----------------|
| 1 | $272,325 | $13,616 | $100,000 | $86,384 | $185,941 |
| 2 | $185,941 | $9,297 | $100,000 | $90,703 | $95,238 |
| 3 | $95,238 | $4,762 | $100,000 | $95,238 | $0 |

This pattern shows why operating lease expense is front-loaded in interest (early years) and back-loaded in principal (later years)—a characteristic of any amortizing debt. The [right-of-use asset](/right-of-use-asset-operating-lease/), by contrast, is amortized straight-line, creating a mismatch in expense timing that must be reconciled in the notes.

## Lease Modifications and Remeasurement

If the terms of a lease are modified—for example, if the lessee exercises an option to extend or if the lease term changes—the liability is remeasured. The remeasurement calculates a new present value of remaining payments as of the modification date, using the same discount rate (unless it has changed materially) and adjusts the [right-of-use asset](/right-of-use-asset-operating-lease/) accordingly.

Modifications that reduce the lease term or payable amount may result in a gain; modifications that increase obligations may result in a loss. These adjustments flow through the income statement in the period of modification.

## Operating vs. Finance Lease Liabilities

Both operating and finance leases now require liability recognition. The distinction is principally about substance:

- **Operating lease**: no transfer of ownership; liability reflects the obligation to pay for the use of an asset the lessor controls
- **Finance lease**: transfer of control (or ownership at lease end); the lessee is, in economic substance, a buyer

For balance sheet presentation, companies often disclose operating and finance lease liabilities separately, or may combine them with a note disclosure. The liability measurement method is the same for both; the difference lies in [right-of-use asset](/right-of-use-asset-operating-lease/) amortization and the overall expense pattern.

## Disclosure Requirements and Transparency

Entities must disclose:
- The amount of current and non-current lease liabilities
- A maturity schedule of undiscounted lease payments (by year for the next 5 years and then in total)
- The weighted-average discount rate (IBR) used
- The nature of lease agreements and significant lease terms (e.g., renewal options, termination clauses, purchase options)
- Total lease expense by type

This transparency allows investors to understand:
1. The magnitude of future cash outflows for leasing
2. Whether the lessee has flexibility to terminate leases early
3. The economic interest rates embedded in lease contracts

## Balance Sheet Impact and Leverage Ratios

The recognition of operating lease liabilities increases reported liabilities and thus affects leverage metrics:

- **Debt-to-equity ratio** = Total debt + Lease liabilities ÷ Total equity; this ratio rises for companies with material leases
- **Interest coverage** = EBITDA ÷ (Interest expense + Lease interest); analysts often adjust for lease expense
- **Working capital** = Current assets − (Current liabilities + Current lease liability); liquidity metrics are tighter

Investors and analysts now must account for lease liabilities when assessing financial risk and comparing companies across industries. This leveled the playing field: a retailer with predominantly leased stores is now more directly comparable to a retailer that owns its real estate.

## See also

<div class="wiki-seealso">

### Closely related

- [Right-of-Use Asset for Operating Leases](/right-of-use-asset-operating-lease/) — the flip side of the liability
- [Operating Lease](/operating-lease/) — the lease classification and scope
- [Lease Liability](/lease-liability/) — general concept of lease financing obligations
- Finance Lease Liability — the non-operating counterpart
- Incremental Borrowing Rate — the discount rate used to measure the liability

### Wider context

- [Balance Sheet](/balance-sheet/) — where the liability is classified and split
- [Income Statement](/income-statement/) — interest and amortization expense flows from the liability
- [Cash Flow Statement](/cash-flow-statement/) — lease payments affect operating and financing cash flows
- [Debt Financing](/debt-financing/) — lease liabilities are economically similar to traditional debt

</div>

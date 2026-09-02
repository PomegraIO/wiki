---
title: "Lease Liability"
description: "The accounting obligation to make future lease payments under ASC 842, recognized on the balance sheet as a liability with a corresponding right-of-use asset."
keywords:
  - lease liability
  - asc 842
  - right-of-use asset
  - operating lease accounting
---

*A **lease liability** is the accounting liability to make future lease payments under a lease contract. Under **ASC 842** (the 2019 U.S. accounting standard for leases), almost all leases—operating leases and capital leases—are recorded on the [balance sheet](/wiki/balance-sheet/) as a liability paired with a right-of-use (ROU) asset. The liability is measured at the present value of future lease payments, discounted at the [implicit rate](/wiki/interest-rate/) in the lease or the lessee's incremental borrowing rate.*

<div class="wiki-hatnote">
For the asset side of the transaction, see right-of-use asset. For lease classification, see operating lease and finance lease.
</div>

<aside class="wiki-infobox">

| Element | Treatment |
|---------|-----------|
| **Initial measurement** | Present value of future lease payments; discounted using implicit lease rate or incremental borrowing rate |
| **Subsequent measurement** | Amortized using the effective-interest method; updated for payment changes, modifications, or lease adjustments |
| **Lease payments included** | Fixed payments, variable payments tied to an index, residual value guarantees, termination penalties, lessee options likely to be exercised |
| **Lease term** | Includes renewal options reasonably certain to be exercised; excludes options where lessee has discretion and is unlikely to exercise |
| **Balance sheet classification** | Current portion (≤12 months) and non-current portion (>12 months) |
| **Interest expense** | The discount unwinding over the lease term; recognized in interest expense on the P&L |

</aside>

## Measurement at lease commencement

When a lessee enters a lease, it must estimate the total undiscounted cash flows it will pay over the lease term. These include:

1. **Fixed lease payments**: Regular monthly, quarterly, or annual rent.
2. **Variable lease payments tied to an index**: For example, rent that escalates 2% annually or is tied to a consumer price index (CPI). Estimated variable payments are included in the measurement.
3. **Residual value guarantees**: If the lessee guarantees the asset will be worth a minimum amount at lease-end, the lessee recognizes a liability for the guaranteed amount.
4. **Termination penalties**: If the lease can be terminated early, but only by paying a penalty, the lessee includes the penalty in the measurement if termination is reasonably certain.
5. **Renewal or extension options**: If the lease includes an option to renew (e.g., renew at a lower rate) and management intends to exercise it, the renewal payments are included. If renewal is discretionary and unlikely, they are excluded.

The **lease term** is the non-cancellable period plus any renewal options the lessee is reasonably certain to exercise. For a 5-year lease with a 2-year renewal option, the term is 7 years if the lessee is reasonably certain to renew. If renewal is not reasonably certain, the term is 5 years.

Once estimated, the total undiscounted payments are **discounted to present value** using:
- The **implicit rate** in the lease (the rate built into the lessor's pricing), if known, or
- The lessee's **incremental borrowing rate** (the rate the lessee would pay to borrow funds for a similar term and collateral), if the implicit rate is not known.

**Example**: A manufacturing company leases a production machine for 5 years at $10,000/month, with a 2-year renewal at $8,000/month, which the company is reasonably certain to exercise. The company estimates the implicit rate in the lease is 4% per year.

- **Lease term**: 7 years (5 + 2)
- **Total payments**: $10,000 × 60 months + $8,000 × 24 months = $792,000
- **Discount rate**: 4%
- **Present value**: $10,000 × [PV factor for 60 months at 4%] + $8,000 × [PV factor for 60-84 months at 4%] ≈ $550,000–$600,000

The company records a lease liability of ~$575,000 and a right-of-use asset of ~$575,000 at lease commencement.

## Subsequent measurement and interest expense

After initial recognition, the lease liability is **remeasured using the effective-interest method**. Each month:

1. **Interest expense** is accrued: Lease liability balance × (Discount rate ÷ 12 months)
2. **Lease payment** is made, reducing the liability
3. The liability balance declines, so interest expense also declines over the lease term

**Example (continued)**: 
- Initial liability: $575,000 at 4% annual rate (0.333% monthly)
- Month 1 interest: $575,000 × 0.333% = $1,917
- Month 1 lease payment: $10,000
- Liability reduced by: $10,000 – $1,917 = $8,083
- Ending month 1 liability: $575,000 – $8,083 = $566,917

Over the lease term, interest expense (the time value of money) is separated from principal reduction (the actual cash payment). The **interest expense declines each period** because the outstanding liability decreases.

## Modifications and remeasurement

If the lease is **modified**—the parties agree to change the payment amount, extend the term, or adjust the renewal options—the lessee remeasures the liability. An increase in future payments increases the liability; a decrease reduces it. The ROU asset is also adjusted by the change in the liability.

**Example**: In year 3 of the lease, the lessor and lessee agree to extend the renewal period from 2 years to 3 years at $8,000/month. The lessee remeasures the liability by discounting the additional year of payments and recording the increase.

## Impact on financial statements

**Balance sheet**: The lease liability appears as a liability; the ROU asset appears as an asset (typically grouped with property, plant, and equipment). Over the lease term, the liability declines (as payments are made and principal is paid down); the asset is amortized to zero.

**Income statement**: 
- **Interest expense**: The discount unwinding (interest on the liability)
- **Depreciation expense**: The ROU asset is depreciated straight-line over the lease term

Total expense (interest + depreciation) is front-loaded; it is highest in year 1 and declines over time.

**Cash flow statement**: The lease payment is split into:
- **Operating cash flow**: The interest expense component (a non-cash charge added back)
- **Financing cash flow**: The principal reduction component

## Comparison with pre-ASC 842 (operating lease off-balance-sheet)

Before ASC 842 (which became effective in 2019), **operating leases** were **off-balance-sheet**. A company could lease office space, retail stores, or equipment and record only the monthly expense without recognizing an asset or liability. This inflated leverage ratios (since liabilities were hidden) and made companies with high lease obligations appear less leveraged than comparable companies with owned assets.

The move to ASC 842 brought ~$1.3 trillion in lease liabilities onto U.S. balance sheets and ~€1.6 trillion globally. A company that leased all its retail stores now shows substantial lease liabilities, lowering reported equity and raising debt ratios. This had implications for debt covenants, credit ratings, and leverage-based compensation metrics.

## Disclosure and analysis

Companies disclose lease liabilities in the footnotes, including:
- Summary of lease policies and assumptions
- Maturity schedule of undiscounted future lease payments
- The sensitivity to changes in discount rates
- Modifications and reassessments

Analysts use the maturity schedule to recalculate the liability using alternative discount rates, assessing how management's assumptions affect reported figures. A company that uses a low discount rate inflates the liability; one that uses a high rate deflates it.

## Practical considerations for lessees

**Short-term leases**: Leases with a term of 12 months or less may be expensed as they are incurred without recognizing a liability. Many companies use short-term leases for flexibility.

**Low-value assets**: Leases of low-value assets (below $5,000 typically) may be excluded from ASC 842 measurement, allowing expensing instead.

**Sale-leaseback transactions**: When a company sells an asset and leases it back, special rules apply to determine whether the company derecognizes the asset or retains it on the balance sheet.

**Lessor perspective**: Lessors (equipment suppliers, real estate firms) recognize a **lease receivable** (the present value of future cash inflows) and derecognize or continue to depreciate the underlying asset, depending on the lease classification (operating vs. sales-type).

<div class="wiki-seealso">

### Closely related
- Right-of-Use Asset — The complementary asset side of ASC 842 leases
- [Operating Lease](/wiki/operating-lease/) — A lease recognized on the balance sheet under ASC 842
- [Finance Lease](/wiki/finance-lease/) — A lease that transfers substantially all benefits and risks of ownership
- [ASC 606](/wiki/asc-606/) — The revenue recognition standard (sister standard to ASC 842)

### Wider context
- [Balance Sheet](/wiki/balance-sheet/) — The statement showing assets, liabilities, and equity
- [Liabilities](/wiki/accounts-payable/) — The broader class of accounting obligations
- [Depreciation](/wiki/depreciation/) — The ROU asset is typically depreciated over the lease term
- [Interest Expense](/wiki/interest-on-excess-reserves/) — The discount unwinding on the lease liability

</div>

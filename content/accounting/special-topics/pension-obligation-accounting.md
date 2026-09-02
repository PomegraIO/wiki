---
title: "Pension Obligation Accounting"
description: "Recording defined-benefit pension liabilities, service costs, and remeasurements under ASC 715 and IFRS."
keywords:
  - pension-liability
  - defined-benefit-plan
  - service-cost
  - aoci-remeasurement
  - actuarial-assumptions
---

*Under [accrual accounting](/wiki/accrual-accounting/), a company sponsoring a [defined-benefit pension plan](/wiki/pension-obligation/) must recognize the accrued obligation as a [liability](/wiki/pension-obligation-accounting/) on the balance sheet and expense pension costs on the income statement. The measurement requires actuarial estimates of future payouts, discount rates, and investment returns.*

<div class="wiki-hatnote">For pension economics generally, see [Pension Obligation](/wiki/pension-obligation/). For plan design choices, see [Defined-Benefit Plan](/wiki/pension-obligation/).</div>

<aside class="wiki-infobox">

| Item | Detail |
|------|--------|
| **Accounting standard (US)** | ASC 715 (formerly FAS 87/158) |
| **Accounting standard (IFRS)** | IAS 19 |
| **Key liability component** | Projected Benefit Obligation (PBO) |
| **Key income statement item** | Net periodic pension cost |
| **Remeasurement location** | OCI (Other Comprehensive Income) |
| **Annual measurement date** | Balance sheet date |

</aside>

## Core measurement: the Projected Benefit Obligation (PBO)

The **Projected Benefit Obligation (PBO)** is the present value of all pension benefits earned by employees as of the measurement date, calculated assuming the plan will continue indefinitely and employees will receive projected future salary increases. It differs from the [Accumulated Benefit Obligation (ABO)](/wiki/pension-obligation/), which assumes no future salary growth.

A company sponsoring a pension plan for engineers currently earning $100,000 per year must estimate their salary at retirement (say, age 65), forecast their life expectancy, and discount all promised payments back to today using a [discount rate](/wiki/discount-rate/) (typically the yield on high-quality bonds). If an engineer will earn $150,000 at retirement, receive $2 million in present-value pension benefits, and discount at 5%, the PBO is ~$1.5 million. Summed across all plan participants (active, vested, and retired), the total PBO is the reported pension liability.

## Income statement recognition: the net periodic pension cost

Each period (year or quarter), the company records a **net periodic pension cost** comprising four components:

1. **Service cost:** The increase in PBO due to one more year of service. An employee's PBO grows each year because they're one year closer to payout.

2. **Interest cost:** The PBO accrues "interest" at the assumed discount rate. If the PBO is $1 billion and the discount rate is 5%, interest cost is ~$50 million.

3. **Expected return on plan assets:** Plan assets (bonds, stocks held in trust) are expected to earn a return. If the plan holds $800 million in assets expected to earn 6%, the company records $48 million in expected return.

4. **Amortization of gains/losses:** Actuarial gains (when plan assets outperform or assumption changes reduce future payouts) and losses (the opposite) are smoothed into income over time rather than recognized all at once.

**Net periodic pension cost** = Service cost + Interest cost − Expected return on assets ± Amortization. For a large sponsor with a mature plan, net cost can be modest or even negative if returns exceed expectations and the plan is well-funded.

## The funded status and balance sheet liability

The **Funded Status** = Fair value of plan assets − PBO. If a plan's assets are worth $800 million and the PBO is $1 billion, the unfunded obligation is $200 million, recognized as a [pension liability](/wiki/pension-obligation/) on the balance sheet.

Plans can be **overfunded** (assets exceed PBO) or **underfunded** (the reverse). US accounting rules permit a company to record overfunded plans as assets only if the company will reclaim the surplus (rare), so overfunded plans typically appear as deferred tax assets and equity adjustments. Underfunded plans always appear as liabilities.

## Remeasurement through OCI: actuarial assumptions and returns

Pension accounting segregates **current-period costs** (on the income statement) from **actuarial gains/losses** (on the balance sheet via Other Comprehensive Income, or OCI). When actual investment returns differ from expected returns, or when actuarial assumptions change (discount rates, mortality, inflation), the difference is recorded in OCI and accumulated in **Accumulated Other Comprehensive Income (AOCI)**.

For example:
- A plan assumed 6% asset returns; actual returns were 3%. The $30 million loss enters OCI.
- A plan assumed 4% inflation and 5% discount rate; interest rates rise, discount rate is now 6%. The PBO shrinks; the $50 million gain enters OCI.

These OCI items are amortized into net periodic pension cost in future periods, smoothing the P&L volatility. The full liability (including unrecognized AOCI) always appears on the balance sheet as **Net Pension Liability (or Asset)**.

## Actuarial assumptions and sensitivity

The PBO and cost are highly sensitive to key assumptions:

- **Discount rate:** A 1% drop in the discount rate increases the PBO by 10–15% for a typical plan. Companies select rates using the "AA bond yield curve" or similar benchmarks.
- **Expected return on assets:** Higher assumed returns reduce current-period cost, but the assumption must be justified. Conservative sponsors assume 5–6%; aggressive ones assume 7–8%.
- **Salary increase rate:** The rate at which covered payroll is expected to grow. Inflation expectations and wage inflation assumptions matter.
- **Mortality and turnover:** Plan sponsors use actuarial tables. Longer life expectancy increases the PBO.

Companies must disclose the sensitivity of the PBO and cost to 100 bp changes in assumptions. This disclosure helps investors assess how much of pension cost is "locked in" (service cost, which changes little) versus volatile (interest cost, which swings with discount rates).

## Interaction with funding and contribution policy

Accounting does not force funding. A company can record a large pension expense and liability but contribute little to the plan in that year. However, [ERISA](/wiki/pension-obligation/) (US) and similar regulatory regimes impose minimum funding requirements. A severely underfunded plan may trigger contribution requirements and loss of contribution deductions. Companies balance:

- Accounting liability (net periodic cost, AOCI impact).
- Funding policy (annual contributions to the plan, affected by ERISA rules and cash flow).
- Tax deductions (contributions are deductible; net periodic cost is not).

A company with $200 million unfunded liability might take 10 years to fully fund, contributing $25 million annually while recording $30 million in net periodic cost, with the shortfall accruing to the balance-sheet liability.

## Pension plans in acquisitions and business combinations

When a company acquires another company with a [defined-benefit pension plan](/wiki/pension-obligation/), the acquirer must recognize the full PBO (and fair value of assets) as of the acquisition date. Gains or losses from plan remeasurement immediately before closing often result in "step-ups" or "step-downs" in the opening balance. These are recorded as part of [goodwill](/wiki/goodwill/) or, if the plan assumption changes are purely settlement-driven, as period costs in the quarter of close.

<div class="wiki-seealso">

### Closely related

- [Pension Obligation](/wiki/pension-obligation/) — economic concept and liability recognition
- [Accumulated Depreciation](/wiki/accumulated-depreciation/) — similar liability concept
- [Accrual Accounting](/wiki/accrual-accounting/) — broader method in which pension accounting sits
- [Deferred Tax Liability](/wiki/deferred-tax-liability/) — where AOCI-related tax impacts land

### Wider context

- [Other Comprehensive Income](/wiki/comprehensive-income/) — where actuarial gains/losses appear
- Bond Yield — source of discount rate assumption
- [Actuarial Assumptions](/wiki/pension-obligation/) — mortality, salary, return assumptions
- [Goodwill](/wiki/goodwill/) — treatment of plan remeasurement gains/losses in M&A

</div>

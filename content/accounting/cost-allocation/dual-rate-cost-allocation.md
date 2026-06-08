---
title: "Dual-Rate Cost Allocation"
description: "Dual-rate cost allocation splits a shared cost into fixed and variable components before allocating each separately to user departments."
keywords:
  - dual-rate cost allocation
  - fixed and variable cost allocation
  - two-tier cost allocation
  - cost separation method
  - overhead allocation rates
---

*Dual-rate cost allocation is a two-step process that divides a shared cost pool into a fixed component and a variable component, then allocates each component separately using different allocation bases. This method provides more accurate product costing and department profitability because fixed and variable costs behave differently as volume changes—fixed costs stay constant while variable costs scale with activity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dual-Rate Cost Allocation — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting topics." />

<div class="wiki-infobox-caption">Treating fixed and variable costs separately improves decision-making and variance reporting.</div>

|   |   |
|---|---|
| **Core method** | Separate a cost pool into fixed and variable; allocate each with appropriate bases |
| **Fixed component** | Based on budgeted capacity or long-term needs; allocated to establish cost baseline |
| **Variable component** | Based on actual volume or activity; allocated proportional to usage |
| **Typical application** | Utilities, IT infrastructure, facilities, maintenance, support departments |
| **Allocation bases differ** | Fixed often uses budgeted capacity; variable uses actual consumption |
| **Key advantage** | Isolates the impact of idle capacity from operational inefficiency |
| **Common context** | Standard costing, activity-based costing, responsibility accounting |

</aside>

## The problem with single-rate allocation

Imagine a shared IT department serving three business units. The IT budget for the year is $1,200,000, comprising:
- Salaries and infrastructure: $1,000,000 (fixed—required regardless of demand)
- Software licenses and bandwidth: $200,000 (variable—scales with transaction volume)

Using a single overhead rate, you'd divide the entire $1,200,000 by total anticipated IT service hours (say, 10,000 hours) to get $120 per hour. Each business unit is charged based on hours consumed.

The problem appears in two scenarios:

**Scenario A: Actual usage is 8,000 hours (15% below forecast)**  
You allocate $960,000 (8,000 hours × $120), yet you still incur $1,000,000 in fixed IT infrastructure costs. You've under-allocated, creating an unabsorbed overhead variance—but the variance mixes two different issues: some fixed infrastructure was unused, and variable costs were lower due to reduced volume. It's unclear which.

**Scenario B: One unit's demand surges to 6,000 hours while others drop to 2,000 hours**  
The high-demand unit gets charged $720,000 (6,000 × $120), and the low-demand unit gets $240,000 (2,000 × $120). But most IT fixed costs don't change because one unit used more service. The high-demand unit is overstated, the low-demand unit is understated. Pricing and internal profitability reports become misleading.

A single rate conflates **capacity costs** (the cost of being ready to serve) with **activity costs** (the incremental cost of each transaction). Dual-rate allocation separates them.

## How dual-rate allocation works

**Step 1: Segment the cost pool**

Classify costs as fixed (do not vary with service volume) or variable (scale with volume).

**Example IT department:**

Fixed costs:
- Salaries (IT manager, network engineer): $800,000
- Depreciation on servers and infrastructure: $150,000
- Facility rent (server room): $50,000
- **Total fixed: $1,000,000**

Variable costs:
- Software licenses (usage-based): $100,000
- Bandwidth and hosting (per transaction): $80,000
- Temporary contract support (hired for peak demand): $20,000
- **Total variable: $200,000**

**Step 2: Determine allocation bases**

For fixed costs, use a **capacity-based measure** that reflects the IT department's obligation to be available:

- **Budgeted IT service hours** (the hours the IT team is expected to work): 10,000 hours
- Or: **Peak-period demand** (the busiest month requires this much capacity)
- Or: **Assigned resource headcount** (each business unit has a dedicated IT liaison)

For variable costs, use an **actual activity measure** that drives incremental cost:

- **Actual hours used** in the period
- **Actual transactions processed**
- **Actual gigabytes of data transferred**
- **Actual number of support tickets**

**Step 3: Calculate rates**

Fixed rate = Total fixed costs / Budgeted capacity  
$1,000,000 / 10,000 hours = **$100 per budgeted hour**

Variable rate = Total variable costs / Expected variable volume  
$200,000 / 10,000 hours = **$20 per actual hour**

**Step 4: Allocate to user departments**

Each department is charged two amounts:

1. **Fixed allocation:** Its budgeted or assigned capacity × fixed rate
2. **Variable allocation:** Its actual consumption × variable rate

**Example for three business units:**

Budgeted capacity assigned (fixed basis):
- Unit A: 4,000 hours
- Unit B: 3,500 hours
- Unit C: 2,500 hours
- Total: 10,000 hours

Actual hours used (variable basis):
- Unit A: 4,200 hours
- Unit B: 2,800 hours
- Unit C: 1,500 hours
- Total: 8,500 hours

**Charges:**

Unit A:
- Fixed: 4,000 × $100 = $400,000
- Variable: 4,200 × $20 = $84,000
- **Total: $484,000**

Unit B:
- Fixed: 3,500 × $100 = $350,000
- Variable: 2,800 × $20 = $56,000
- **Total: $406,000**

Unit C:
- Fixed: 2,500 × $100 = $250,000
- Variable: 1,500 × $20 = $30,000
- **Total: $280,000**

**Overall allocation: $1,170,000** (underabsorbed: $30,000 because actual hours were 8,500, not 10,000; the $30,000 represents unused fixed capacity).

## Why the method is superior

**Clearer accountability:** Unit A is charged for the full $400,000 in fixed costs it committed to, regardless of whether it used all 4,000 hours. If Unit A only uses 3,000 hours, it's still accountable for $400,000 fixed + $60,000 variable ($3,000 × $20) = $460,000. The $100,000 difference ($400,000 – $300,000) in fixed charges is a *capacity variance*—a signal that Unit A underutilized its assigned resources, perhaps a strategic choice or a temporary dip. It is not a failure of the IT department to control costs.

**Variable costs move with consumption:** If all units reduce actual hours from 8,500 to 8,000, variable costs drop by exactly $10,000 (500 hours × $20). This transparency helps managers understand the true incremental cost of adding a new transaction or process.

**Idle capacity is visible:** If the IT department was budgeted for 10,000 hours but actual usage is 8,500 hours, the $30,000 unabsorbed fixed variance is tracked separately. Management can ask: "Did we over-budget capacity, or did business decline?" A single-rate method buries this in a murky overhead variance.

**Fairness in service pricing:** If you charge customers for IT services, dual-rate lets you recover fixed costs via the capacity charge (reflecting your obligation to maintain infrastructure) and variable costs via usage fees (reflecting actual consumption). This is how cloud services and utilities actually operate.

## Practical considerations

**Choosing the fixed/variable split:** If your cost data is limited, you can use industry benchmarks or regression analysis on historical cost and volume pairs. Plot 24 months of IT cost and transaction volume; the y-intercept is roughly the fixed component.

**Updating rates:** Dual rates should be recalculated at least annually, or whenever major cost changes occur (a system migration, a salary increase, or a layoff). Stale rates lead to poor allocation and variance distortions.

**Assigning budgeted capacity:** If you assign each unit a fixed portion of IT capacity at the start of the period, make it explicit and stable. Avoid changing it mid-period, or you'll confuse actual variance with arbitrary reallocation.

**Handling actual vs. budgeted variable costs:** Some organizations use budgeted variable rates (planned cost per hour) and then separately track and analyze any gap between budgeted and actual variable costs. Others use actual rates. The former gives better forecasting; the latter shows true current cost.

## Where dual-rate allocation is used

- **Utilities and energy companies:** Fixed transmission infrastructure + variable usage
- **Data centers:** Fixed servers and facilities + variable bandwidth and cooling
- **Shared IT or HR departments:** Fixed staff and systems + variable transactions
- **Manufacturing service departments:** Fixed equipment and staff + variable materials and wear
- **Hotels and hospitality:** Fixed building and staff + variable supplies and housekeeping
- **Hospitals and healthcare:** Fixed operating facilities + variable drugs and disposables

Dual-rate is standard anywhere a service department must maintain capacity and then scale variable inputs with demand.

## See also

<div class="wiki-seealso">

### Closely related

- [Fixed vs Variable Overhead Allocation](/fixed-vs-variable-overhead-allocation/) — General principles of separating cost behavior
- [Service Department Cost Allocation Methods](/service-department-cost-allocation-methods/) — Allocating support costs to operating departments
- [Cost Allocation for Small Businesses](/cost-allocation-small-business/) — Simpler approaches when dual-rate overhead is impractical

### Wider context

- [Accrual Accounting](/accrual-accounting/) — Timing principles for cost recognition
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — Framework for allocation methods and overhead treatment
- [Standard Costing](/cost-basis/) — Use of budgeted rates and variance analysis
- [Income Statement](/income-statement/) — Where allocated overhead appears in cost of goods sold

</div>

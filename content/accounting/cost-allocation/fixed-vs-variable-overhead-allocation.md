---
title: "Fixed vs Variable Overhead Allocation"
description: "Fixed vs variable overhead allocation separates indirect costs by behavior to improve pricing accuracy and variance analysis."
keywords:
  - fixed vs variable overhead allocation
  - overhead cost separation
  - fixed overhead allocation
  - variable overhead allocation
  - overhead variance analysis
  - indirect cost behavior
---

*Fixed and variable overhead allocation is the practice of separating indirect production costs into fixed components (those that don't change with output) and variable components (those that do), then allocating each type to products or departments using different methods. This split matters because fixed and variable costs behave differently as production volume changes, and conflating them leads to poor pricing decisions and misleading variance reports.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fixed vs Variable Overhead Allocation — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting topics." />

<div class="wiki-infobox-caption">Splitting overhead by cost behavior improves both product costing and operational control.</div>

|   |   |
|---|---|
| **Core purpose** | Separate indirect costs to match allocation logic to cost movement |
| **Fixed overhead** | Rent, depreciation, supervisor salary—unchanged by volume |
| **Variable overhead** | Utilities tied to production, indirect materials, hourly indirect labor |
| **Allocation bases** | Fixed: machine hours, headcount; Variable: labor/machine hours, units produced |
| **Key benefit** | Accurate contribution margin and break-even calculations |
| **Main challenge** | Determining which costs are truly fixed vs. variable |
| **Use case** | Essential for standard costing, activity-based costing, and profitability analysis |

</aside>

## Why the distinction exists

Manufacturing plants incur overhead—costs that support production but cannot be traced directly to a single product. Depreciation on factory equipment, plant manager salaries, property taxes, and utilities all sit here. The problem is that not all overhead moves with production volume. Some overhead (like rent) stays constant whether you make 10 units or 1,000; other overhead (like electrical power for machinery) climbs with output.

When you allocate all overhead using a single rate—say, "50% of direct labor cost"—you're implicitly assuming that every dollar of direct labor triggers the same overhead. This works reasonably well if costs actually behave that way. But if your overhead is 70% fixed and 30% variable, a single-rate allocation obscures that reality. You'll undercoat low-volume products and overcoat high-volume products, leading to pricing errors and false profit signals.

## Separating fixed from variable overhead

The first step is categorizing your actual overhead accounts. Common fixed overhead items include:
- Factory building rent or mortgage
- Depreciation on equipment
- Supervisory salaries
- Equipment maintenance contracts
- Property insurance and taxes
- Quality control staff salaries

Common variable overhead items include:
- Indirect production materials (glue, sandpaper, lubricants)
- Machine power and compressed air
- Hourly indirect labor (material handlers, machine setup workers on the floor)
- Waste and scrap (correlated to production)
- Delivery of raw materials

In practice, some accounts are mixed. Utilities might be 60% fixed (baseline heating/cooling) and 40% variable (extra power when machines run). Maintenance might spike during high-production months but have a baseline in low months. The allocation requires judgment—and often requires analyzing historical patterns or staff interviews to estimate the split.

## Allocation bases for fixed overhead

Fixed overhead is most commonly allocated using capacity-based drivers that don't fluctuate with production:

**Machine hours or labor hours available** — If your factory has 10,000 machine hours of capacity per month, allocate fixed overhead per actual machine hour used. This ties fixed cost to the resource constraint.

**Number of production runs or batches** — If setup labor is the main fixed cost, allocate it per batch produced, not per unit.

**Headcount or workspace** — If you're allocating facilities cost, use number of employees or square footage occupied per department.

The key principle: use a base that reflects the fixed resource consumed, not the output volume.

## Allocation bases for variable overhead

Variable overhead moves with output, so use volume-driven bases:

**Direct labor hours or cost** — Traditional; works well if labor volume tracks production volume.

**Machine hours** — Better if machines, not labor, drive variable costs like electricity and wear.

**Units produced** — Simplest if variable costs are genuinely proportional to unit count.

**Material cost or weight** — Useful if overhead (waste, packaging) scales with material input.

The goal is to use a base that actually causes the cost to rise and fall.

## Impact on standard costing and variance analysis

Once you separate overhead, your overhead rate formula changes. Instead of:

> Overhead rate = Total overhead / Total allocation base

You now calculate two rates:

> Fixed overhead rate = Fixed overhead / Expected capacity  
> Variable overhead rate = Variable overhead / Expected volume

When actual results arrive, you can measure two distinct variances. The **fixed overhead variance** shows whether actual capacity was used as expected (a volume or efficiency issue). The **variable overhead variance** shows whether actual variable costs matched the per-unit expectation (a price or efficiency issue). This clarity guides corrective action.

For example: If you budgeted $100,000 fixed overhead and made 10,000 units (fixed rate = $10/unit), but only made 8,000 units, you still incur roughly $100,000 in fixed overhead. The variance signals underutilized capacity, not overspending on variable inputs. By contrast, if variable overhead was $20,000 at full volume but only $14,000 at 8,000 units, that's good control—variable costs scaled down appropriately.

## Challenges in practice

**Cost classification ambiguity** — Many overhead accounts don't fit neatly into "fixed" or "variable." Telephone service has a base monthly charge plus per-minute overages. How much is fixed? You'll need historical data to estimate the split, and the answer may change annually.

**Seasonality and outliers** — A factory that runs year-round may have lower fixed cost per unit in peak months (higher utilization) than in slow months. Allocating a single "fixed" amount can mask this.

**Accuracy vs. simplicity trade-off** — The more refined your overhead split, the more accounting work required each month. Many small businesses use a single overhead rate for simplicity, accepting some costing inaccuracy in exchange for lower processing cost.

**Inflation and cost structure changes** — A retrofit that shifts electricity (variable) to solar depreciation (fixed) alters the split. Renegotiating contracts can swing a cost from variable to fixed. Reanalyzing the split quarterly or annually helps catch these shifts.

## When to use this approach

Fixed vs. variable overhead allocation is standard in:
- **Manufacturing plants** producing multiple products with different profit margins
- **Utilities and energy companies** managing both fixed infrastructure and volume-dependent operations
- **Standard costing systems** that compare actual to budgeted overhead
- **Activity-based costing**, which can assign fixed costs to cost pools and variable costs to activity drivers

Small job shops or make-to-order operations may skip this refinement and use a simpler single rate if overhead is truly proportional to output. But as product mix diversifies, the separation becomes increasingly valuable for pricing discipline.

## See also

<div class="wiki-seealso">

### Closely related

- [Service Department Cost Allocation Methods](/service-department-cost-allocation-methods/) — Allocating shared service costs across departments using direct, step-down, or reciprocal methods
- [Dual-Rate Cost Allocation](/dual-rate-cost-allocation/) — Formal split of a shared cost into fixed and variable components before allocation
- [Cost Allocation for Small Businesses](/cost-allocation-small-business/) — Practical approaches for businesses without dedicated cost accounting resources
- [Cost-Allocation](/accounts-payable/) — General principles of assigning indirect costs to products or departments

### Wider context

- [Accrual Accounting](/accrual-accounting/) — Recognition of costs regardless of cash payment timing
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — Framework governing cost allocation and overhead treatment
- [Cost-Basis](/cost-basis/) — Foundation for tracking and allocating costs in tax and financial reporting
- [Income Statement](/income-statement/) — Where allocated overhead flows into cost of goods sold and operating expenses

</div>

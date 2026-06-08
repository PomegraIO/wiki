---
title: "Process Costing"
description: "An accounting method that averages total costs across equivalent units when identical products flow through continuous processes."
keywords:
  - process costing
  - manufacturing accounting
  - equivalent units
  - cost allocation
  - continuous production
image: "/svg/accounting.svg"
---

*Process costing allocates manufacturing costs across identical units produced in continuous operations. Rather than tracking costs item-by-item, it averages total spending across all units completing a process in a given period, treating partially finished goods as fractional units.*

## Why process costing matters

Companies that make identical products in assembly-line fashion—think cement, chemicals, textiles, or food processing—face a bookkeeping puzzle. A unit started today might not be finished until later. Tracking individual costs per item would be impractical when thousands of interchangeable units flow through pipes and tanks. Process costing solves this by pooling all costs for a production run, calculating an average cost per completed unit, and allocating a proportional share to work still in progress.

This approach dominates capital-heavy, high-volume industries where variation between units is minimal or nonexistent. It separates the accounting challenge from the manufacturing reality: you assign costs based on *production stages*, not individual orders.

## How it differs from job costing

Job costing tracks expenses directly to distinct customer orders or jobs. If you're building custom machinery or doing bespoke contract work, every job gets its own cost ledger. Process costing pools costs by *department* or *process stage* instead. Both are valid; the choice hinges on whether products are custom or identical.

The gap matters operationally. Job costing delivers precision but requires detailed tracking—ideal for low-volume, high-customization work. Process costing accepts averaging as a trade-off for simplicity—essential when tracking 10,000 identical units daily would be inane.

## The role of equivalent units

Inventory rarely sits neatly at 0%. At any period-end, you'll have finished goods and work-in-progress (WIP) at various completion levels. A unit that's 80% complete doesn't consume 100% of labor or materials; it consumes 80%. Process costing converts this partial state into **equivalent units**—a standardized denominator for cost allocation.

If you have 100 units in WIP at 60% completion, you count them as 60 equivalent units. Combined with 500 finished units, your total is 560 equivalent units. If the period cost was $5,600, you divide to get $10 per equivalent unit. The WIP is charged $600 (60 × $10); finished goods absorb $5,000 (500 × $10). See [equivalent units of production](/equivalent-units-of-production/) for the full mechanics.

## Two main approaches

**Weighted-average process costing** blurs the line between opening inventory and current-period production. It adds beginning-WIP costs to current costs and divides by total equivalent units, treating all costs as a single pool. This is simpler to calculate and widely used. See [weighted-average process costing](/weighted-average-process-costing/) for details.

**FIFO process costing** keeps beginning-inventory costs and current-period costs separate. Beginning WIP is finished first using opening balances; only new work is charged at current-period rates. This is more granular and reflects period-specific efficiency but requires extra bookkeeping. See [FIFO process costing](/fifo-process-costing/) for the methodology.

Neither is "right"; they differ mainly in how conservatively you want to separate periods. Weighted-average smooths volatility; FIFO shows period-by-period change.

## Multiple processes and departments

Real factories have multiple stages. Raw materials might enter Dept. A for mixing, move to Dept. B for heating, then to Dept. C for packaging. Each department is a process node. Cost flows downstream: Dept. A passes its output cost to Dept. B, which adds its own costs and passes the combined total to Dept. C.

In this setup, beginning WIP in Dept. B includes costs from Dept. A plus any work Dept. B started but didn't finish last period. You track costs by department, calculating equivalent units and average costs independently for each, then link them as production flows through.

## Recording transactions

As production happens, you record actual costs—materials purchased, payroll, overhead allocated—into cost-of-production accounts. At period-end, you calculate equivalent units and unit costs, then allocate balances to finished goods and ending WIP via journal entries. The cost of goods sold is pulled from finished goods when units ship.

Unlike job costing, where you match specific costs to specific jobs, process costing requires batch calculations. A single journal entry might reflect thousands of units' worth of allocation—acceptable because the goal is departmental cost flow, not line-item precision.

## When process costing breaks down

Process costing assumes high homogeneity. If products vary widely in materials or labor, or if production is sporadic, its averages become unreliable. It also struggles with high defect rates or yield loss; you must adjust equivalent-units calculations to account for normal waste.

For low-volume custom work, the averaging assumption collapses. A single rejected batch might skew the unit cost meaninglessly. In those cases, job costing or hybrid methods work better.

## Practical advantages

Process costing is computationally lightweight once you have the equivalent-units count. It requires no tracing of costs to specific units—a monumental saving in labor-intensive or real-time systems. It also aligns naturally with how large manufacturers think: in terms of batches, runs, and throughput rather than individual items.

The averaging also dampens short-term cost swings. A spike in energy prices one month is amortized across the period's full output, smoothing profitability reports. For stakeholders, this can be a feature (predictable margins) or a bug (hidden efficiency problems).

---

## See also

<div class="wiki-seealso">

### Closely related

- [Equivalent Units of Production](/equivalent-units-of-production/) — Converting partial inventory into full-unit counts for allocation
- [Weighted-Average Process Costing](/weighted-average-process-costing/) — Merging opening and current costs into one pool
- [FIFO Process Costing](/fifo-process-costing/) — Keeping opening-inventory costs separate from current spending
- Job Costing — Tracking costs to distinct orders instead of processes
- Cost Allocation — Methods for assigning indirect costs to products

### Wider context

- Work-in-Progress — Inventory in intermediate stages of completion
- Cost-of-Goods-Sold — Total production expenses matched to revenue
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — Standards governing cost accounting methods
- [Accrual Accounting](/accrual-accounting/) — Recording costs as incurred, not when cash changes

</div>
---
title: "FIFO Process Costing"
description: "A process-costing method that keeps beginning-inventory costs separate from current-period costs, isolating the cost of new production."
keywords:
  - FIFO process costing
  - process costing
  - cost allocation
  - manufacturing accounting
  - equivalent units
image: "/svg/accounting.svg"
---

*FIFO process costing assumes beginning work-in-progress is completed first, then new units started. It separates the costs carried in opening inventory from costs incurred in the current period, calculating unit costs only for new production. This isolates period-to-period cost changes but requires extra bookkeeping.*

## The FIFO flow assumption

FIFO stands for "first in, first out." In [process costing](/process-costing/), it's not a physical inventory rule (units don't have serial numbers) but a cost-tracking convention. The method assumes that:

1. Units in opening work-in-progress (WIP) are completed first during the period.
2. After opening WIP is finished, newly started units are worked on.
3. Any units not finished by period-end become ending WIP.

This ordering lets you isolate costs: opening WIP costs remain unchanged; current-period costs apply only to new work. The result: you see the true cost of production this period, unsullied by old prices or inefficiencies carried from last month.

## Calculating FIFO unit costs

**Example**:
- Opening WIP: 100 units, 30% complete, prior-period costs of $600
- Started this period: 500 units
- Finished and transferred out: 600 units (100 from opening + 500 new)
- Ending WIP: 0 units

Current-period costs: $3,000 (materials and labor)

**Step 1: Calculate equivalent units for *current period only*.**
- To finish opening WIP: 100 units × (100% − 30%) = 70 equivalent units
- To start and finish new units: 500 units × 100% = 500 equivalent units
- **Total current-period equivalent units: 570**

Note: We do *not* count the 100% × 100 units (opening WIP) because it was already in progress and its prior costs are kept separate.

**Step 2: Calculate current-period unit cost.**
- Current cost ÷ Current equivalent units = $3,000 ÷ 570 ≈ $5.26 per equivalent unit

**Step 3: Allocate costs.**
- Cost of opening WIP (unchanged): $600
- Cost to complete opening WIP: 70 × $5.26 ≈ $368
- Total for opening WIP: $600 + $368 = $968
- Cost of new units (500 × $5.26): $2,630
- **Total transferred out: $968 + $2,630 = $3,598**
- Check: $600 (opening) + $3,000 (current) = $3,600 (small rounding difference is normal)

## Why FIFO differs from weighted-average

[Weighted-average process costing](/weighted-average-process-costing/) merges opening and current costs into one pool and divides by all equivalent units—old and new. The result blurs the cost separation.

FIFO asks: "How much did it cost *this period* to do new work?" By isolating current spending and current equivalent units, it reveals period-specific efficiency. If current-period unit cost rises, you know it's because of this period's inputs, labor rates, or inefficiency—not because you're averaging in stale prior costs.

For management reporting, this clarity is powerful. A production manager sees immediately whether tightening controls improved cost this month. For external financial reporting, both methods are acceptable under [GAAP](/generally-accepted-accounting-principles/); auditors don't prefer one over the other provided you're consistent.

## Multiple stages and departments

When production flows through several departments, FIFO isolates costs at each stage. Dept. A's opening WIP cost stays with the units as they move to Dept. B. Dept. B adds its own costs (both for finishing opening units and for processing new units). The opening-WIP cost and Dept. B's current costs are kept separate within Dept. B, so you see what Dept. B alone spent this period.

This multi-stage clarity is FIFO's major operational advantage. You can trace cost drivers by department: if labor cost shot up in Dept. C, you see it reflected in Dept. C's current-period unit cost, separate from Depts. A and B.

## Handling multiple cost streams

Like [weighted-average](/weighted-average-process-costing/), FIFO manages materials, labor, and overhead separately. Materials might be 100% added upfront; labor might be added gradually. The calculations are identical in principle:

- **For materials**: Equivalent units for current work only = units to finish opening WIP at materials' completion % + units started and finished at 100% + units started but not finished at their completion %.
- **Unit cost for materials** = Current material cost ÷ Current material equivalent units.
- **For labor**: Same logic, but labor's completion percentages differ from materials'.

Each cost stream gets its own unit cost; you allocate each separately to finished goods and ending WIP.

## When ending WIP exists

If the period ends with unfinished units, FIFO handles them as a separate bucket:

**Example** (adjusted):
- Opening WIP: 100 units, 30% complete, prior cost $600
- Started: 500 units
- Finished: 500 units
- Ending WIP: 100 units, 60% complete

Current-period costs: $3,000

Equivalent units for current work:
- To finish opening WIP: 100 × 70% = 70 eq. units
- To fully complete started units that are finished: 500 × 100% = 500 eq. units
- To start and partially complete ending WIP: 100 × 60% = 60 eq. units
- **Total: 630 equivalent units**

Current-period unit cost: $3,000 ÷ 630 ≈ $4.76

Cost allocation:
- Opening WIP: $600 (unchanged)
- Cost to complete opening WIP: 70 × $4.76 = $333
- Cost of opening WIP transferred out: $933
- Cost to start and finish 500 units: 500 × $4.76 = $2,380
- **Total transferred out: $933 + $2,380 = $3,313**
- Ending WIP: 60 × $4.76 = $286
- **Total: $3,313 + $286 = $3,599** (≈ $3,600 with rounding)

## The computational burden

FIFO requires more careful tracking than weighted-average. You must distinguish which units came from opening WIP and which were started fresh. You must calculate equivalent units only for current-period work, not for units carried over. Most modern ERPs handle this automatically, but manual calculation is error-prone.

In practice, many firms use weighted-average for financial reporting (it's simpler and sufficient for external stakeholders) and run FIFO calculations in a shadow system for management reporting. This hybrid approach gives operational transparency without complicating the general ledger.

## Inventory cost flows

When FIFO units are sold and transferred to cost of goods sold, the older cost (opening WIP) is recognized first, then newer costs. This mimics the physical flow for commodities and is often required by tax authorities. In inflationary periods, FIFO results in lower current cost of goods sold and higher reported profit compared to weighted-average—a reason some CFOs prefer it for tax filings.

## Consistency and choice

FIFO and weighted-average are not interchangeable within a single set of books—you must choose one and stick with it. A change in method requires [GAAP](/generally-accepted-accounting-principles/) disclosure and often restates prior periods. Most firms choose once and maintain it unless circumstances (e.g., a shift to real-time costing) compel a switch.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Process Costing](/process-costing/) — Overview of cost averaging in continuous production
- [Weighted-Average Process Costing](/weighted-average-process-costing/) — Merging old and new costs into one pool
- [Equivalent Units of Production](/equivalent-units-of-production/) — Converting partial inventory to full-unit equivalents
- Work-in-Progress — Inventory in intermediate stages of completion
- Cost Allocation — Methods for assigning indirect costs to products

### Wider context

- Cost of Goods Sold — Total production costs matched to revenue
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — Standards governing cost methods
- [Accrual Accounting](/accrual-accounting/) — Recording costs as incurred, not when cash changes
- Manufacturing Overhead — Indirect production costs allocated to output

</div>
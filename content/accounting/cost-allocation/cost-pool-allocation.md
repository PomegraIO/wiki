---
title: "Cost Pool Allocation"
description: "Grouping and distributing indirect costs across cost centers or units in proportion to an allocation base."
keywords:
  - cost allocation
  - cost pool
  - indirect costs
  - overhead allocation
---

*The **cost pool** is a grouping of indirect costs (overhead, support functions, depreciation) that are allocated to cost centers, products, or business units using an [allocation base](/wiki/allocation-base/) (labor hours, machine hours, square footage). Cost pool allocation is a foundational technique in [activity-based costing](/wiki/activity-based-costing/) and managerial accounting.*

<div class="wiki-hatnote">For the relationship between cost pools and activity-based cost drivers, see <a href="/wiki/activity-based-costing/">Activity-Based Costing</a>.</div>

<aside class="wiki-infobox">

| Step | Description |
|---|---|
| **1. Identify costs** | Gather all indirect costs to be allocated (rent, utilities, supervision, maintenance). |
| **2. Form pools** | Group related costs into cost pools (e.g., "Building Services," "Quality Control"). |
| **3. Select allocation base** | Choose a measurable driver (machine hours, labor hours, headcount, revenue). |
| **4. Measure activity** | Measure total activity in the base across all cost centers. |
| **5. Calculate rate** | Divide total pool cost by total activity: Cost per unit of base. |
| **6. Apply allocation** | Multiply the rate by each cost center's activity usage. |

</aside>

## The problem cost pools solve

Every organization has costs that cannot be traced directly to a specific product or business unit. A factory's rent, the CFO's salary, IT infrastructure, and quality assurance all benefit multiple products but are not proportional to any single product's output.

Without allocation, these costs—called **overhead** or **indirect costs**—are left in limbo. They must be absorbed somewhere. In simple accounting, they might be lumped into a single "overhead" line and allocated to products as a percentage of labor or material cost. In modern accounting, cost pools and [activity-based costing](/wiki/activity-based-costing/) aim to match costs to the activities that drive them.

The goal is fairness and insight: a product or division should bear the costs it actually consumes. Misallocating costs distorts profitability analysis and can lead to bad strategic decisions (e.g., keeping an "profitable" product that actually consumes enormous support resources).

## Simple allocation: the two-stage approach

A traditional two-stage cost allocation process works as follows:

**Stage 1: Accumulation.** Indirect costs are grouped into a cost pool. For example:
- Building Services pool: rent ($100,000), utilities ($50,000), maintenance ($30,000) = $180,000.
- Administrative pool: CFO salary ($150,000), accounting staff ($80,000), office supplies ($20,000) = $250,000.

**Stage 2: Allocation.** Each pool is allocated to cost centers using a single driver:
- Building Services: allocated based on square footage occupied by each department.
- Administrative: allocated based on headcount or labor cost.

If the factory occupies 50,000 square feet and Department A occupies 5,000 sq ft (10%), Department A is charged $180,000 × 10% = $18,000 in Building Services overhead.

This method is simple but crude. It assumes that all Building Services costs are proportional to square footage, ignoring variation (e.g., a heavy-machinery department may require more maintenance per square foot than a warehouse).

## Activity-based costing and multi-stage allocation

[Activity-based costing](/wiki/activity-based-costing/) (ABC) refines cost pools by decomposing overhead into multiple cost pools, each tied to a specific activity and cost driver.

Example: Instead of one "Manufacturing Support" pool, a company might create:
- **Quality Inspection pool**: Tied to number of units inspected.
- **Material Handling pool**: Tied to number of material moves.
- **Machine Setup pool**: Tied to number of production runs.
- **Supervision pool**: Tied to direct labor hours.

Each pool is allocated using the cost driver that causes the cost to vary. This multi-stage approach is more accurate but requires more data collection.

A product requiring frequent setups will bear more setup costs under ABC than under simple overhead allocation. This insight can be valuable: the company may discover that high-variety, low-volume products are far less profitable than top-line revenue suggests.

## Choosing the allocation base

The allocation base is the denominator—the measure of activity that justifies cost assignment. Common bases include:

- **Direct labor hours**: Assumes overhead is proportional to labor time (reasonable for labor-intensive manufacturing).
- **Machine hours**: Assumes overhead varies with machine utilization (relevant for capital-intensive operations).
- **Units produced**: Simple but often inaccurate; ignores product complexity.
- **Square footage**: Relevant for facilities and utilities.
- **Headcount**: Often used for administrative overhead.
- **Revenue**: Used as a fallback when no better driver is available.

The ideal allocation base:
1. Is **causally related** to the costs in the pool (machinery support is driven by machine hours, not units).
2. Is **objectively measurable** (headcount is clearer than "complexity").
3. Is **consistently available** across all products/cost centers.

A poor choice of base—allocating maintenance costs by revenue, for example—can distort cost analysis and lead to suboptimal decisions.

## Implementation challenges

In practice, cost pool allocation faces several hurdles:

**Data collection**: Measuring the allocation base for every product or cost center is labor-intensive. A factory tracking machine hours for every product may require automated sensors or manual timekeeping, adding cost.

**Shared resources**: Some costs support multiple activities. A single maintenance technician might service both machines and buildings. How much of her cost is in the "Machinery" pool and how much in "Facilities"? The answer is subjective, and different allocations yield different product costs.

**Causality vs. correlation**: A cost may correlate with a driver without being caused by it. A large customer may generate higher IT support costs because the system is more heavily used, but the correlation is loose. Allocating IT costs based on revenue is imperfect.

**Cost of allocation**: The cost of implementing ABC or detailed cost pools can be high relative to the value of the insight. A small company with a single product line might find that a simple allocation is sufficiently accurate.

## Applications in decision-making

Cost pool allocation informs several types of decisions:

**Pricing**: A product's full cost (direct + allocated overhead) establishes a cost floor for pricing. A product that appears unprofitable when allocated high overhead might be discontinued, even if it covers its direct costs. The decision depends on whether the fixed overhead would be eliminated or reallocated elsewhere.

**Make-or-buy**: When deciding whether to outsource a function, comparing the variable cost of outsourcing to the full allocated cost (including fixed overhead) can be misleading. The relevant comparison is outsource cost vs. avoidable cost (the overhead that would actually be eliminated if the function is outsourced).

**Product line profitability**: Allocating overhead reveals which products are truly profitable. A high-revenue but low-complexity product might be more profitable than a high-complexity, lower-revenue product—but only if overhead is allocated accurately.

**Capacity utilization**: Cost pools that are tied to capacity (e.g., depreciation on a machine) illustrate how fully the asset is utilized. If a $500,000 machine is allocated across only a fraction of output, the company might be operating with excess capacity and should consider expanding volume or divesting the asset.

## Standards and disclosure

For external financial reporting ([GAAP](/wiki/generally-accepted-accounting-principles/) and [IFRS](/wiki/international-financial-reporting-standards/)), cost pool allocation methods must be consistent and disclosed. Companies must use [absorption costing](/wiki/absorption-costing/) for inventory valuation: all manufacturing overhead (both fixed and variable) must be allocated to product cost, not expensed. Different allocation methods (FIFO, LIFO, weighted average) can yield different inventory values and profitability.

For internal management purposes, companies often use multiple allocation schemes simultaneously—one for external reporting, one for strategic analysis, one for day-to-day operational decisions. This multiplicity reflects the fact that different decisions require different cost perspectives.

<div class="wiki-seealso">

### Closely related
- [Activity-Based Costing](/wiki/activity-based-costing/)
- [Allocation Base](/wiki/allocation-base/)
- [Absorption Costing](/wiki/absorption-costing/)
- [Overhead Allocation](/wiki/overhead-allocation/)

### Wider context
- [Cost of Debt](/wiki/cost-of-debt/)
- [Contribution Margin](/wiki/contribution-margin/)
- [Break-Even Analysis](/wiki/contribution-margin-percent/)

</div>

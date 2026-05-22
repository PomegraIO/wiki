---
title: "Allocation Base"
description: "The metric used to distribute indirect costs across cost objects, such as products or departments, in activity-based or traditional costing."
keywords:
  - cost allocation
  - overhead allocation
  - activity-based costing
  - cost accounting
---

*An **Allocation Base** is the denominator—the metric—used to apportion a pool of indirect costs to individual products, jobs, or departments. The choice of base directly affects product profitability calculations and can reveal or obscure where value is truly created.*

<aside class="wiki-infobox">

| Allocation method | Typical base |
|---|---|
| Traditional absorption | Labor hours; machine hours |
| Activity-based | Number of setups; number of inspections |
| Overhead | Square footage; headcount |
| Departmental | Direct labor dollars; output units |
| Variable | Units produced; machine hours |

</aside>

## Why allocation base matters

Indirect costs—factory supervision, maintenance, utilities, depreciation—are not easily traceable to individual products. A company must allocate them to derive the full (absorbed) cost of production. If a company allocates overhead to products based on direct labor hours, it assumes labor intensity drives overhead consumption. A high-labor product bears more overhead; an automated product bears less. But if overhead is actually driven by setup frequency (not labor), the labor-based allocation misrepresents product profitability.

Misallocation has real consequences. A company may price low-margin products thinking they are profitable, underprice high-margin products, and gradually lose money on its worst business while neglecting its best. Managers may make bad decisions to shift production toward seemingly profitable products that are actually loss-making once overhead is properly allocated.

## Traditional absorption costing

The most common method is traditional absorption costing, which allocates overhead based on a single base, usually direct labor hours or machine hours. The formula is:

**Overhead rate = Total indirect costs ÷ Total allocation base**

If a factory has $1 million in annual overhead and expects 10,000 labor hours, the overhead rate is $100 per labor hour. A product requiring 100 labor hours is charged $10,000 in overhead. This is simple and was standard for decades.

The flaw: If the factory has diverse products—some requiring many setups (expensive) and others running long production runs (cheap)—the labor-hour base distorts costs. A short-run specialty product is charged the same $100 per labor hour as a high-volume commodity, even though the specialty product consumes far more setup and changeover overhead.

## Activity-based costing (ABC)

Activity-based costing refines allocation by using multiple bases, one for each major cost driver. Instead of a single overhead pool, ABC identifies activities (setups, inspections, packaging, shipping) and allocates the costs of each activity using a base specific to that activity.

For example:
- Setup costs ($100,000 annually) allocated by number of setups (1,000 total setups per year) = $100/setup.
- Inspection costs ($200,000 annually) allocated by number of inspections (10,000 total inspections per year) = $20/inspection.
- Packaging costs ($50,000 annually) allocated by number of shipments (5,000 total shipments per year) = $10/shipment.

A product that requires 50 setups, 200 inspections, and 10 shipments is charged:
- Setups: 50 × $100 = $5,000
- Inspections: 200 × $20 = $4,000
- Packaging: 10 × $10 = $100
- Total overhead allocation: $9,100

This is far more precise than a labor-hours-only approach for a complex, multi-product operation.

## Choosing the right base

The ideal allocation base is one that directly or reasonably proxies the consumption of the overhead cost. Machine hour allocation makes sense if the overhead cost (equipment maintenance, depreciation) varies with machine usage. Labor-hour allocation is sensible if supervision and indirect labor vary with direct labor. Setup-based allocation is appropriate for setup costs.

Some questions to guide selection:
- What actually drives the cost? (root cause analysis)
- Does the base vary proportionally with cost consumption?
- Is the base measurable without excessive detail?
- Does it yield insight into profitability?

Overly complex ABC systems with dozens of cost pools can become unwieldy; overly simple systems misallocate badly. The right balance depends on cost structure and diversity of products.

## Cost pool segmentation

Related to the allocation base is the size and definition of the cost pool itself. A single factory-wide overhead pool assumes one homogeneous production environment. But if a factory has a high-speed automated line and a manual assembly line, overhead allocation should reflect that. Segmenting the overhead into department-level pools or process-level pools allows different bases for different environments.

A manufacturer might have:
- Automated line overhead: allocated by machine hours
- Assembly line overhead: allocated by direct labor hours
- Warehousing overhead: allocated by cubic meters of space

This segmentation improves accuracy at the cost of complexity.

## Variance analysis and variance bases

In standard costing, the allocation base also determines variance analysis. If the overhead rate is $100 per labor hour and actual labor hours exceed budget, the volume variance shows the cost of that excess. Changes in the allocation base (hours worked, machine hours) drive much of the overhead budget variance. Understanding which base drives which variance is crucial for root-cause analysis.

## Implications for pricing and profitability

Product costing directly affects pricing. If a product's true overhead allocation is $50 but the company's allocation base charges it $20, the product is underpriced. Over time, the company will lose money on that product. Conversely, if true allocation is $20 but the base charges $50, the product is overpriced and may lose market share.

Publicly traded companies use absorption costing for financial reporting (GAAP requirement). But internally, many use ABC or department-specific bases for management decisions. The gap between financial costing and management costing can be significant.

## Modern challenges: shared services and intangibles

Modern businesses often have shared services (finance, IT, HR) that support multiple business lines. Allocating shared services overhead is notoriously difficult—is it by headcount, revenue, usage, or square footage? Different companies choose different bases, making comparisons unreliable. The debate over the right allocation base for shared services continues.

Similarly, intangible overhead (software licenses, brand investment) is hard to allocate meaningfully. Some bases (like % of revenue) are arbitrary.

<div class="wiki-seealso">

### Closely related
- [Activity-Based Costing](/wiki/activity-based-costing/) — the refined allocation method.
- [Cost Pool](/wiki/cost-pool-allocation/) — the aggregation of indirect costs.
- [Absorption Costing](/wiki/absorption-costing/) — the broader framework.

### Wider context
- [Standard Costing](/wiki/standard-costing/) — uses allocation bases for variance analysis.
- [Overhead Allocation](/wiki/overhead-allocation/) — the general process of distributing indirect costs.
- [Variable Costing](/wiki/variable-costing/) — an alternative that excludes fixed overhead.

</div>

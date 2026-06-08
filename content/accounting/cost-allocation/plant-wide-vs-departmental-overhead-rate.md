---
title: "Plant-Wide vs Departmental Overhead Rate"
description: "Compare plant-wide and departmental overhead rates to understand when a single factory-wide rate distorts product costs."
keywords:
  - plant-wide overhead rate
  - departmental overhead rate
  - cost allocation method
  - overhead distortion
  - manufacturing costing
  - product cost accuracy
image: /svg/accounting.svg
---

*A **plant-wide overhead rate** spreads all factory costs across production using a single denominator (like machine hours or labor hours), while a **departmental overhead rate** allocates overhead separately within each production area. The choice between them determines whether product costs reflect reality or mask significant cost drivers — and one approach can systematically overcharge or undercharge different products.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Overhead Allocation — two paths</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting." />

<div class="wiki-infobox-caption">Plant-wide rates are simpler; departmental rates reveal hidden cost distortions.</div>

|   |   |
|---|---|
| **Plant-wide rate** | Single overhead rate for entire factory |
| **Departmental rate** | Separate rates per production department |
| **Cost pool** | All overhead | Overhead grouped by department |
| **Allocation base** | Usually one (labor hours, machine hours) | May differ per department |
| **Key advantage** | Simplicity, easier to compute | Accuracy where departments differ drastically |
| **Key risk** | Can badly distort if departments vary | More complex; requires detailed tracking |
| **When to use** | Homogeneous production, similar cost drivers | Diverse departments, high variation in overhead |

</aside>

## The mathematics

A **plant-wide overhead rate** is computed as:

```
Plant-Wide Rate = Total Factory Overhead / Total Allocation Base
```

For example, a factory spends $500,000 on indirect labor, utilities, depreciation, and maintenance across 100,000 total machine hours. The plant-wide rate is $5 per machine hour. Every product is charged $5 of overhead for each machine hour consumed.

A **departmental rate** breaks this down:

```
Department A Rate = Department A Overhead / Department A Allocation Base
Department B Rate = Department B Overhead / Department B Allocation Base
```

If Department A (assembly, labor-intensive) incurs $200,000 overhead and runs 20,000 labor hours, its rate is $10 per hour. Department B (finishing, machine-heavy) incurs $300,000 and uses 60,000 machine hours, so its rate is $5 per machine hour. A product spending 10 labor hours in Assembly and 8 machine hours in Finishing is charged $100 + $40 = $140 in overhead.

## When departmental rates reveal the distortion

Plant-wide rates work only if overhead is driven by the same factor everywhere and departments consume that factor proportionally to their actual overhead costs.

Consider a factory making both hand tools and precision instruments:

- **Department A (Hand Tools)**: Low-overhead assembly area, high labor intensity. $100,000 overhead, 50,000 labor hours, $2/hour departmental rate.
- **Department B (Instruments)**: High-overhead precision area with sophisticated equipment. $400,000 overhead, 20,000 machine hours, $20/machine-hour departmental rate.

Using a plant-wide rate: total overhead $500,000, total hours (labor + machine, blended) 70,000, giving a blended rate of ~$7.14 per "hour"—but this assumes hours are interchangeable, which they are not.

A hand tool that spends 20 labor hours in Department A and zero hours in B should be charged 20 × $2 = $40 under departmental costing. But under plant-wide costing at $7.14/hour, it is overcharged to $143. The overhead cost of the tool inflates artificially.

Conversely, an instrument spending 5 machine hours in Department B should pay 5 × $20 = $100. Plant-wide costing charges only ~$36, underpricing the instrument and masking its true cost.

This distortion drives bad decisions: the underpriced instrument looks more profitable than it is; the hand tool looks less profitable. The firm may push the wrong product mix.

## Choosing an allocation base per department

The power of departmental costing emerges when departments use different bases aligned to their actual cost drivers:

- **Labor-intensive department**: allocate by direct labor hours or labor dollars.
- **Machine-heavy department**: allocate by machine hours or asset depreciation.
- **Utilities or facility costs**: allocate by square footage.

This specificity works only if data collection is feasible. A small job shop with one person handling all overhead might find that one plant-wide base is enough. A large multi-line factory with distinct production zones will likely benefit from departmental granularity.

## Overhead absorption and product costing

Both methods feed into product costing. Under [absorption costing](/absorption-costing/), overhead is attached to inventory on the balance sheet; under [variable costing](/variable-costing/), overhead flows to period expense. Regardless of the costing method, the choice of plant-wide versus departmental determines the magnitude of overhead assigned—and therefore the inventory valuation and periodic profit.

## Activity-based costing as a refinement

Modern manufacturers sometimes layer a third approach: [activity-based costing](/activity-based-costing/), which treats each significant overhead cost driver (machine setups, material handling, quality inspections) as a separate cost pool and assigns overhead based on how much of each activity each product consumes. This is more granular than departmental costing but also more data-intensive.

## Practical constraints and trade-offs

Departmental costing requires:
- Clear department boundaries and cost assignments.
- Reliable measurement of each product's usage of each department's allocation base.
- Regular updates to departmental rates (quarterly or monthly) as overhead changes.

Plant-wide costing is easier to maintain but risks systematic bias if departments are diverse. Many firms use a pragmatic middle ground: plant-wide for simple product lines, departmental for complex or mixed operations, and activity-based costing only where distortion is severe enough to justify the overhead-tracking cost.

The test is whether the simpler method's error matters to your pricing and mix decisions. If a 10% overhead misallocation would change which products you promote, departmental costing pays for itself.

## See also

<div class="wiki-seealso">

### Closely related

- Cost allocation — overview of methods to spread indirect costs
- [Cost allocation vs transfer pricing](/cost-allocation-transfer-pricing-difference/) — internal allocation versus inter-division pricing
- [Absorption costing](/absorption-costing/) — product costing method that includes overhead
- [Activity-based costing](/activity-based-costing/) — allocation method based on activity consumption
- Overhead — definition of indirect manufacturing and period costs

### Wider context

- Cost of goods sold — how product costs flow to income
- Job costing — allocation in project-based manufacturing
- Inventory valuation — impact of costing method on balance sheet

</div>

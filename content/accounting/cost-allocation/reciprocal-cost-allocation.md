---
title: "Reciprocal Cost Allocation"
description: "An overhead-allocation method that solves simultaneous equations to fully capture mutual services between support departments."
keywords:
  - cost allocation
  - service departments
  - overhead assignment
  - simultaneous equations
  - mutual services
image: "/svg/accounting.svg"
---

*The **reciprocal method** of cost allocation redistributes service-department costs by setting up and solving simultaneous equations, allowing full recognition that one support department serves another, which in turn serves the first. Unlike the [step-down method](/step-down-method/) (which follows an arbitrary sequence) or the [direct method](/direct-method-cost-allocation/) (which ignores inter-departmental services), reciprocal allocation treats the organization as an interdependent system where payroll services maintenance and maintenance services payroll equally and completely.*

<div class="wiki-hatnote">

For sequential allocation without simultaneous equations, see [Step-Down Method](/step-down-method/). For direct allocation to production only, see [Direct Method Cost Allocation](/direct-method-cost-allocation/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reciprocal Cost Allocation — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting and finance topics." />

<div class="wiki-infobox-caption">The mathematically precise method: recognizes all mutual support relationships through simultaneous equations.</div>

|   |   |
|---|---|
| **What it is** | A cost-allocation approach that solves simultaneous equations to capture mutual service flows |
| **Also called** | Simultaneous-equation method, algebraic method, or reciprocal-service method |
| **Key assumption** | Service departments fully serve each other; all relationships are two-way |
| **When to use** | When inter-departmental service flows are material and significant |
| **Advantage** | Theoretically most accurate; eliminates sequence bias |
| **Limitation** | Computationally more complex (though software handles it routinely) |
| **Scope** | Manufacturing, healthcare, large service organizations with multiple support units |

</aside>

## The mutual-service problem

Many organizations face a tangled web of internal services. A payroll department processes cheques and benefits for the maintenance department. The maintenance department repairs the building and equipment used by payroll. Each serves the other.

The [step-down method](/step-down-method/) solves this by declaring an order: payroll first, then maintenance. But this is arbitrary. If payroll truly serves maintenance and maintenance truly serves payroll, why should payroll's cost go down before maintenance's? The reciprocal method refuses to choose; it captures both directions simultaneously.

Imagine a manufacturer with two support departments—payroll and maintenance—and two production departments—assembly and finishing. Payroll costs include processing wages for all departments, including maintenance staff. Maintenance costs include repairs to machinery, offices, and the payroll department's computers. The costs flow in both directions, simultaneously.

## Setting up the simultaneous equations

Each service department's total cost is split into two parts: its direct cost and the allocated costs from other service departments serving it.

Let's say:
- Payroll direct cost: £100,000
- Maintenance direct cost: £80,000
- Payroll allocation basis: headcount (maintenance is 5% of total payroll staff, assembly 50%, finishing 45%)
- Maintenance allocation basis: square footage maintained (payroll occupies 10%, maintenance occupies 5%, assembly 40%, finishing 45%)

Let P = total payroll cost (direct + allocated), and M = total maintenance cost (direct + allocated).

**Payroll equation:**
P = £100,000 + (0.05 × M)

(Payroll's total cost equals its direct cost plus 5% of maintenance's total cost.)

**Maintenance equation:**
M = £80,000 + (0.10 × P)

(Maintenance's total cost equals its direct cost plus 10% of payroll's total cost.)

## Solving the equations

From the first equation: P = £100,000 + 0.05M

Substitute into the second: M = £80,000 + 0.10(£100,000 + 0.05M)
M = £80,000 + £10,000 + 0.005M
M = £90,000 + 0.005M
0.995M = £90,000
M = £90,452.26

Now solve for P: P = £100,000 + 0.05(£90,452.26) = £104,522.61

These are the *total* costs of each support department, including all internal service allocations.

## Allocating to production

Once P and M are known, they are allocated to production departments using their predetermined allocation percentages:

- Assembly receives: (£104,522.61 × 50%) + (£90,452.26 × 40%) = £52,261 + £36,181 = £88,442
- Finishing receives: (£104,522.61 × 45%) + (£90,452.26 × 45%) = £47,035 + £40,704 = £87,739

(Maintenance also sends 5% to payroll and 10% is already reflected in payroll's allocation—these internal flows net out in the total.)

## Why reciprocal is theoretically superior

The reciprocal method is the most economically honest. It does not bias results by choosing an arbitrary order. Both support departments' mutual services are fully recognized, and the allocation is reproducible and stable.

If the payroll-to-maintenance percentage changes (fewer maintenance staff processed), the equation adjusts automatically. The method is self-correcting and transparent: any change in allocation assumptions updates both departments' totals simultaneously.

In contrast, the [step-down method](/step-down-method/) produces different results depending on sequence choice. The [direct method](/direct-method-cost-allocation/) ignores inter-departmental services entirely, often understating production-department overhead significantly. Reciprocal avoids both pitfalls.

## Why step-down remains common despite this

Despite reciprocal's theoretical superiority, many organizations use step-down. Why?

**Transparency:** Step-down's sequence is easier for non-accountants to understand and defend. "Payroll goes first because every department uses payroll" is intuitive. Simultaneous equations are not.

**Software and historical practice:** Before widespread spreadsheets, solving simultaneous equations by hand was tedious and error-prone. Step-down was practical. Many organizations locked in step-down decades ago and see no cost to switching.

**Immateriality:** If inter-departmental services are small, the difference between step-down and reciprocal is negligible. The effort to justify a change outweighs the benefit.

**Regulatory context:** Some regulators (e.g., rate-setting agencies for utilities) have long approved step-down and questioned reciprocal as overcomplicating. Challenging an entrenched regulatory stance requires effort.

## Three-or-more department scenarios

Reciprocal shines with three or more support departments. A hospital with payroll, plant operations, and billing departments all serving each other requires a three-equation system. Step-down's bias—allocating payroll first, then plant ops, then billing—systematically understates billing's share of plant-ops costs (since billing has already been allocated before plant ops is stepped down, and plant ops sees none of billing's influence).

Reciprocal solves all three equations simultaneously, capturing every flow. For large, complex organizations, this accuracy justifies the computational effort.

## Implementation in modern systems

Today, any mid-sized accounting system can solve reciprocal equations in seconds. The computational cost is negligible. The bottleneck is no longer math; it is designing the allocation bases (headcount, square footage, machine hours) and keeping them current.

Some firms use reciprocal for external financial statements (if materiality is high), while using step-down for internal management reports (if simplicity is valued for decision-making). This hybrid approach leverages both methods' strengths.

## See also

<div class="wiki-seealso">

### Closely related

- [Step-down method](/step-down-method/) — a sequential allocation approach that is simpler but introduces sequence bias
- [Direct method cost allocation](/direct-method-cost-allocation/) — ignores inter-departmental services; simplest but least accurate
- [Sum-of-years-digits depreciation](/sum-of-years-digits-depreciation/) — an accelerated allocation method in asset accounting

### Wider context

- [Generally accepted accounting principles](/generally-accepted-accounting-principles/) — the framework governing cost-allocation method choice
- [Cost of goods sold](/depreciation/) — the ultimate destination of allocated overhead
- [Income statement](/income-statement/) — where allocated costs affect reported profit
- [Balance sheet](/balance-sheet/) — where inventory carrying allocated overhead appears
- [International financial reporting standards](/international-financial-reporting-standards/) — alternative standards with similar cost-allocation guidance

</div>

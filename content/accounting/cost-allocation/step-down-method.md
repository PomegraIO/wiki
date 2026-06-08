---
title: "Step-Down Method"
description: "A sequential cost-allocation approach that reassigns service-department costs through other support departments before distributing to production."
keywords:
  - cost allocation
  - service departments
  - overhead assignment
  - support cost
  - production departments
image: "/svg/accounting.svg"
---

*The **step-down method** (also called the sequential allocation method) redistributes service-department costs to other departments in a descending order, recognizing that some support functions serve other support functions. A company allocates the most comprehensive service department's costs first, then moves down to less comprehensive ones, until all overhead reaches production departments. Unlike the [direct method](/direct-method-cost-allocation/), which ignores inter-departmental services, SYD acknowledges that the payroll department's work benefits not just production but also the maintenance department.*

<div class="wiki-hatnote">

For the direct approach to cost allocation, see [Direct Method Cost Allocation](/direct-method-cost-allocation/). For simultaneous-equation allocation, see [Reciprocal Cost Allocation](/reciprocal-cost-allocation/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Step-Down Method — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting and finance topics." />

<div class="wiki-infobox-caption">A pragmatic middle ground: recognizes inter-departmental service relationships without solving simultaneous equations.</div>

|   |   |
|---|---|
| **What it is** | A sequential cost-allocation technique for overhead assignment |
| **Also called** | Sequential allocation, cascading method, or tier allocation |
| **Scope** | Primarily manufacturing and large service organizations with multiple support departments |
| **Key assumption** | Some service departments serve other service departments; order matters |
| **When to use** | When inter-departmental services are significant but computational complexity must be limited |
| **Advantage** | Simpler than [reciprocal-cost-allocation](/reciprocal-cost-allocation/) but more realistic than direct |
| **Limitation** | Sequence choice affects results; some reciprocal flows remain unaccounted |

</aside>

## The sequence problem

The defining challenge in step-down is determining which service department's costs to allocate first. A manufacturing plant with a payroll department, maintenance department, and two production lines must choose: does payroll go down first, or maintenance?

This choice matters. If payroll costs are allocated first, the maintenance department—which also receives payroll services—is charged a portion of those costs before maintenance's own costs are allocated to production. If maintenance goes first, payroll receives none of maintenance's benefit allocation, only the primary allocation of payroll's own direct costs.

The standard practice is to allocate the service department that serves the *most* other departments (or the most comprehensive one) first, then step down to narrower departments. This logic: the broadest service should bear its own costs, plus appropriate reallocation from narrower support functions, before production departments bear anything. It's arbitrary, but systematic.

## A worked example

A factory has four departments: payroll (support), maintenance (support), assembly (production), and finishing (production). In a given period:

- Payroll direct costs: £100,000
- Maintenance direct costs: £80,000
- Assembly direct overhead: £200,000
- Finishing direct overhead: £150,000

Payroll services are allocated by headcount: 5% to maintenance, 50% to assembly, 45% to finishing. Maintenance services are allocated by machine hours: 60% to assembly, 40% to finishing.

**Step 1:** Allocate payroll (the most comprehensive, serving both other support and production).
- Maintenance gets: £100,000 × 5% = £5,000
- Assembly gets: £100,000 × 50% = £50,000
- Finishing gets: £100,000 × 45% = £45,000

**Step 2:** Allocate maintenance (now including the £5,000 from payroll).
- Total maintenance cost: £80,000 + £5,000 = £85,000
- Assembly gets: £85,000 × 60% = £51,000
- Finishing gets: £85,000 × 40% = £34,000

**Final result:**
- Assembly overhead: £200,000 + £50,000 + £51,000 = £301,000
- Finishing overhead: £150,000 + £45,000 + £34,000 = £229,000

Production departments bear all support costs, and the sequence has been resolved in one direction only: payroll → maintenance → production.

## Why the sequence biases results

Notice that if maintenance were allocated *before* payroll, the payroll department would receive none of maintenance's cost allocation. This means maintenance's view of payroll labour would be ignored, understating payroll's true service value. Conversely, payroll's view of maintenance would still be captured (since payroll goes last and sees all prior allocations). The sequence advantage tilts toward whichever department is allocated last.

To minimize this bias, practitioners typically identify the service department with the broadest scope—one that serves other support functions extensively—and allocate it first. Departments with more narrow scopes go down the list. The result is not perfect, but it is defensible and reproducible.

## Step-down versus direct and reciprocal

The [direct method](/direct-method-cost-allocation/) skips this problem entirely by allocating service-department costs straight to production only, ignoring inter-departmental services altogether. It is simple and free of sequence bias but economically inaccurate when support departments meaningfully serve each other.

The [reciprocal method](/reciprocal-cost-allocation/) captures all mutual services by solving simultaneous equations. It is the most accurate but also computationally complex and less transparent. Modern accounting systems handle the math easily, but step-down remains popular because its sequence logic is intuitive and explainable to non-accountants.

Step-down is the practical middle ground. It acknowledges that service departments serve each other (more realistic than direct), uses a sequential order that can be documented and defended (simpler than simultaneous equations), and produces results consistent across periods if the sequence is held constant.

## Common pitfalls in application

**Re-allocation error:** Some practitioners mistakenly "re-allocate" to departments that have already been stepped down. Once payroll costs are allocated, payroll should not receive further allocations from lower departments. The step is one-way.

**Sequence inconsistency:** Changing the sequence year to year makes cost comparisons across periods unreliable. Once a sequence is chosen, it should be locked in—documented in the accounting policy—and changed only with auditor approval and clear disclosure.

**Forgetting non-reciprocal flows:** Step-down assumes that if payroll serves maintenance, maintenance does not meaningfully serve payroll back. If both are true (truly reciprocal), step-down is only an approximation. In such cases, [reciprocal allocation](/reciprocal-cost-allocation/) is theoretically superior.

## Regulatory and practical context

Under Generally Accepted Accounting Principles (GAAP), step-down is an accepted method for allocating overhead to inventory and cost of goods sold, provided the allocation basis is reasonable and applied consistently. Financial statement auditors evaluate both the method chosen and the consistency of its application.

Many regulated industries (utilities, telecommunications, insurance) use step-down in rate-setting, since regulators favour methods that are defensible, transparent, and not subject to simultaneous-equation complexity. It balances accuracy with simplicity.

For management accounting, step-down offers a middle-ground insight: it reveals which service departments depend on others, highlights bottlenecks in support services, and can inform decisions about centralising or decentralising functions.

## See also

<div class="wiki-seealso">

### Closely related

- [Direct method cost allocation](/direct-method-cost-allocation/) — allocates service costs straight to production, ignoring inter-department services
- [Reciprocal cost allocation](/reciprocal-cost-allocation/) — uses simultaneous equations to capture mutual service relationships
- [Sum-of-years-digits depreciation](/sum-of-years-digits-depreciation/) — an accelerated method in the cost-allocation family (though distinct from allocation per se)

### Wider context

- [Generally accepted accounting principles](/generally-accepted-accounting-principles/) — the framework within which cost allocation methods are applied
- [Cost of goods sold](/depreciation/) — the primary destination of allocated overhead
- [Income statement](/income-statement/) — where allocated overhead ultimately affects profit
- [Accounts payable](/accounts-payable/) — related to the payables processing that support departments handle
- [Overhead allocation](/depreciation/) — the broader discipline of which step-down is a part

</div>

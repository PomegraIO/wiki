---
title: "Step-Down vs Reciprocal Method: Which Is More Accurate?"
description: "How step-down and reciprocal methods differ in allocating support department costs, and when added complexity of reciprocal actually changes results."
keywords:
  - step-down vs reciprocal method
  - step-down method cost allocation
  - reciprocal method accounting
  - interdepartmental cost allocation
  - support department allocation
  - cost accounting methods
image: "/svg/accounting.svg"
---

*The **step-down** and **reciprocal** methods both allocate support department costs to production departments, but they differ in how they treat interdepartmental service flows: step-down allocates once in a sequence, while reciprocal solves for the true cost by recognizing that support departments serve each other.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Step-Down vs Reciprocal Method — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Both are multi-stage approaches; reciprocal is mathematically truer but adds complexity; step-down is simpler and often "close enough."</div>

|   |   |
|---|---|
| **Mechanism** | Step-down: sequential, one-way allocation; Reciprocal: simultaneous, two-way |
| **Interdepartmental flows** | Step-down: ignored or undercounted; Reciprocal: fully recognized |
| **Accuracy assumption** | Step-down: approximate; Reciprocal: theoretical ideal (still an allocation, not causation) |
| **Computation** | Step-down: straightforward arithmetic; Reciprocal: linear algebra (simultaneous equations) |
| **Materiality threshold** | Differences typically <5% when interdepartmental allocation is <15% of total support |
| **GAAP/IFRS requirement** | Neither explicitly mandated; both acceptable per [ASC 905](/asc-606/) context, [IFRS 15](/ifrs-15/) |
| **Practical use** | Step-down dominates in practice; Reciprocal used for high-interdependency environments |

</aside>

## Foundational Concept: Why Support Costs Matter

Production departments manufacture goods or deliver services; support departments (Human Resources, IT, Accounting, Facilities) sustain operations across the business.

The cost of a product must include a fair share of support costs—HR, IT infrastructure, quality assurance, and building utilities. The allocation method determines how much support cost each product bears. Inaccurate allocation distorts product profitability, pricing, and make-or-buy decisions.

When support departments serve each other (IT maintains the HR system; HR recruits IT staff), the allocation method must decide: should that interdepartmental service be recognized in the final product cost?

## The Step-Down Method: Sequential Allocation

The **step-down method** allocates support department costs to production (and sometimes other support) departments in a predetermined sequence, one level at a time, then *stops allocating back* to departments already processed.

**Mechanical process:**

1. Rank support departments by the extent of their service to other support departments (or arbitrarily).
2. Allocate the first department's total cost to all departments it serves (both support and production).
3. Allocate the second department (which now includes any allocation from the first) to remaining departments.
4. Continue until all support costs are allocated to production.

**Example:**

Three support departments (IT, HR, Facilities) and two production departments (Assembly, Finishing).

- IT cost: \$100,000
- HR cost: \$80,000
- Facilities cost: \$60,000
- Total support: \$240,000

IT serves 40% HR, 20% Facilities, 25% Assembly, 15% Finishing.
HR serves 10% IT (ignored in step-down), 30% Assembly, 60% Finishing.
Facilities serves 20% IT (ignored), 5% HR (ignored), 40% Assembly, 35% Finishing.

**Step 1:** Allocate IT to HR, Facilities, Assembly, Finishing (ignore reciprocal IT service from HR).
- HR gets: 100K × 40% = \$40,000 (IT cost allocated to HR)
- Facilities gets: 100K × 20% = \$20,000
- Assembly gets: 100K × 25% = \$25,000
- Finishing gets: 100K × 15% = \$15,000

**Step 2:** Allocate HR (original \$80K + \$40K from IT = \$120K) to Assembly and Finishing.
- Assembly gets: 120K × 30% = \$36,000 (allocate only to production and remaining support)
- Finishing gets: 120K × 60% = \$72,000
- (Facilities receives nothing, as it was already processed in the sequence)

**Step 3:** Allocate Facilities (\$60K + \$20K from IT = \$80K, ignoring \$5K of HR).
- Assembly gets: 80K × 40% = \$32,000
- Finishing gets: 80K × 35% = \$28,000

**Total allocation to Assembly:** \$25,000 + \$36,000 + \$32,000 = \$93,000
**Total allocation to Finishing:** \$15,000 + \$72,000 + \$28,000 = \$115,000

Notice: Facilities' allocation of 5% HR service to HR (5% × \$80K = \$4,000) is ignored once HR is stepped down.

## The Reciprocal Method: Simultaneous Allocation

The **reciprocal method** recognizes that support departments serve each other and solves a system of simultaneous equations to determine each department's true cost.

**Mechanical process:**

1. Set up equations where each support department's total cost = its original cost + allocated cost from other support departments.
2. Solve the system to find the true cost of each support department.
3. Allocate the solved-for costs to production departments based on usage rates.

**Using the same example:**

Let S(IT), S(HR), S(F) = the solved-for total cost of each support department.

S(IT) = 100,000 + 0.10 × S(HR) + 0.20 × S(F)
S(HR) = 80,000 + 0.40 × S(IT)
S(F) = 60,000 + 0.20 × S(IT) + 0.05 × S(HR)

Solving (by substitution or matrix algebra):
- S(IT) ≈ \$130,435
- S(HR) ≈ \$132,174
- S(F) ≈ \$104,348

(Simplified; exact numbers depend on simultaneous-equation precision.)

**Then allocate to production:**

- Assembly receives: (130,435 × 25%) + (132,174 × 30%) + (104,348 × 40%) ≈ \$98,783
- Finishing receives: (130,435 × 15%) + (132,174 × 60%) + (104,348 × 35%) ≈ \$141,217

**Comparison:**
- Step-down: Assembly \$93,000; Finishing \$115,000
- Reciprocal: Assembly \$98,783; Finishing \$141,217
- Difference: Assembly +5.8%; Finishing +22.8%

In this case, reciprocal significantly reallocates cost because IT and HR have material mutual service.

## When the Difference Matters

The two methods diverge most when:

1. **Support departments have high interdependency**: IT and HR serving each other heavily, or Facilities and IT each needing the other's infrastructure.
2. **Service flows are asymmetric**: One support department serves others far more than it is served back, making the ordering of the step-down sequence heavily influential on results.
3. **Support cost is a large percentage of total cost**: If support is 5% of total, a 20% difference between methods is material; if support is 50%, it is huge.
4. **Product margins are narrow**: When a 3–5% difference in allocated cost changes profitability from loss to break-even or profit, accuracy matters.

The difference is typically **less than 5%** when:
- Interdepartmental allocation is <15% of total support cost.
- The number of support departments is small (fewer reciprocal equations to solve).
- Service relationships are largely one-way (e.g., IT serves many, but is served by few others).

## Materiality and Regulatory Context

[GAAP](/generally-accepted-accounting-principles/) and [IFRS](/international-financial-reporting-standards/) do not mandate a specific method; both are acceptable. ASC 908 (Airlines) and ASC 905 (Airlines—prior) reference support cost allocation but do not prescribe reciprocal over step-down.

In practice, **most companies use step-down** because:
- It is easier to compute and audit.
- The difference is immaterial for many cost structures.
- It is predictable: changing the order of allocation doesn't change the final answer (though it changes *which departments* bear the cost).

**Reciprocal is chosen** when:
- A company has high mutual service (utilities, large hospital systems, multi-division manufacturing).
- Accuracy is critical for regulatory compliance (healthcare, government contracts under cost-reimbursement terms).
- Stakeholders (creditors, partners, regulators) demand the most theoretically correct method.

## Example: When Reciprocal Dramatically Changes Results

Consider a utility company with two main support departments: **Meter Reading** (MR) and **Billing**.

- MR cost: \$5 million (reads customer meters)
- Billing cost: \$4 million (processes payments)
- Two production departments: Residential, Commercial

MR serves Billing directly (Billing receives 20% of MR capacity to read data).
Billing serves MR directly (MR uses Billing's system 15% of the time to issue notices).

**Step-down (allocating MR first):**
- MR is allocated 0% reciprocity from Billing → \$5M allocated as scheduled
- Billing receives \$5M × 20% + original \$4M = \$5M cost to allocate

Result: Residential and Commercial bear cost as if MR were independent.

**Reciprocal:**
- S(MR) = 5M + 0.15 × S(Billing)
- S(Billing) = 4M + 0.20 × S(MR)

Solving: S(MR) ≈ \$5.27M; S(Billing) ≈ \$5.05M

MR's true cost is higher (includes Billing's service), Billing's rises too. The allocation to production departments shifts, potentially affecting rate-setting and cost-recovery calculations.

In rate-regulated utilities, regulators often insist on reciprocal for this reason: the method better reflects the true cost of service to the ratepayer.

## Practical Considerations in Selection

**Choose step-down if:**
- Support interdependency is low (IT supports production mostly, not Facilities).
- Cost accounting is for internal management, not external reporting or contracts.
- Simplicity and auditability are valued over theoretical precision.
- The company has historically used step-down and wants continuity.

**Choose reciprocal if:**
- Support departments have significant mutual service (especially IT, HR, Facilities in large organizations).
- Cost is the basis for pricing or revenue recognition (government contracts, cost-plus rate agreements).
- The company is in a regulated industry where cost allocation affects allowed returns.
- Stakeholder expectations or audit pressures favor the most rigorous method.

## Computational Reality

Step-down requires basic arithmetic (a series of percentage multiplications). Reciprocal requires solving a system of linear equations—manageable by hand for two or three support departments, but increasingly cumbersome for larger matrices.

Modern accounting software (SAP, Oracle, NetSuite) can solve reciprocal systems in seconds. The barrier to adopting reciprocal is no longer computational; it is explanatory (justifying the method to non-technical stakeholders) and organizational (changing ingrained practice).

## See also

<div class="wiki-seealso">

### Closely related

- [Accrual accounting](/accrual-accounting/) — Matching costs to the period and activity they benefit
- Cost of goods sold — How allocated support costs affect reported cost
- [Generally accepted accounting principles](/generally-accepted-accounting-principles/) — Framework within which allocation methods sit
- [International financial reporting standards](/international-financial-reporting-standards/) — IFRS allows both methods; emphasis on faithful representation
- [Revenue recognition](/revenue-recognition/) — [ASC 606](/asc-606/) context; allocating cost to revenue lines

### Wider context

- [Balance sheet](/balance-sheet/) — Impact on inventory valuation (capitalized support cost)
- [Income statement](/income-statement/) — How allocation affects reported profitability per product
- [Activity-based costing](/activity-based-costing/) — Modern alternative to traditional allocation
- [Standard costing](/standard-costing/) — Simplified approach to avoid detailed allocation

</div>
